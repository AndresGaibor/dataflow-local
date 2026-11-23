"""Ejecuta un .dfw sobre DuckDB: origenes (CSV / BD), processors como SQL, destinos a disco o S3 (MinIO)."""
import json
import os
import re

import duckdb

from . import dfw

q = lambda c: '"' + str(c).replace('"', '""') + '"'
lit = lambda s: "'" + str(s).replace("'", "''") + "'"


class Unsupported(Exception):
    pass


class Ctx:
    def __init__(self, data_dir, out_dir, connections=None, s3=None):
        self.con = duckdb.connect()
        self.data_dir, self.out_dir, self.connections, self.s3 = data_dir, out_dir, connections or {}, s3
        self.n, self.attached, self.report = 0, set(), []
        if s3:  # {"endpoint","key","secret"} -> MinIO/S3 real
            self.con.execute("INSTALL httpfs; LOAD httpfs")
            self.con.execute(f"SET s3_endpoint={lit(s3['endpoint'])}; SET s3_access_key_id={lit(s3['key'])}; "
                             f"SET s3_secret_access_key={lit(s3['secret'])}; SET s3_use_ssl=false; SET s3_url_style='path'")

    def view(self, sql):
        self.n += 1
        name = f"v{self.n}"
        self.con.execute(f"CREATE VIEW {name} AS {sql}")
        return name

    def cols(self, v):
        return [r[0] for r in self.con.execute(f"DESCRIBE SELECT * FROM {v}").fetchall()]


# ---------- origenes ----------
def _source(ctx, node, sources):
    p = node["component"]["properties"]
    meta = next((s for s in sources if s["sourceId"] == (p.get("dataEntity") or {}).get("entityId")), None)
    if meta is None:
        # las fuentes de tipo connection no traen tablas en el .dfw: no se pueden emular
        raise Unsupported(f"fuente '{node.get('label')}' sin metadatos de tabla (conexion no emulable)")
    t = meta["tables"][0]
    fields = [f["name"] for f in t["fields"] if f.get("selected", True)]
    sel = ", ".join(q(f) for f in fields)
    if p["type"] == "dataset":
        path = os.path.join(ctx.data_dir, t["databaseName"])
        if not os.path.exists(path):
            raise FileNotFoundError(f"dataset {t['databaseName']} no esta en {ctx.data_dir}")
        raw = ctx.view(f"SELECT {sel} FROM read_csv({lit(path)}, header=true)")
        # Qlik recorta los espacios de los textos al leer un CSV y una celda vacia es texto vacio (cuenta como valor,
        # medido en el tenant); DuckDB no recorta y la lee como NULL. Las columnas numericas con vacios siguen con NULL.
        types = {r[0]: r[1].split("(")[0] for r in ctx.con.execute(f"DESCRIBE SELECT * FROM {raw}").fetchall()}
        trimmed = [f"coalesce(trim({q(f)}), '') AS {q(f)}" if types.get(f) == "VARCHAR" else q(f) for f in fields]
        return ctx.view(f"SELECT {', '.join(trimmed)} FROM {raw}")
    conn = t["dataconnectorName"]
    cfg = ctx.connections.get(conn)
    if not cfg:
        raise Unsupported(f"conexion '{conn}' sin configurar en connections.json")
    if conn not in ctx.attached:
        kind = cfg["type"]  # duckdb | sqlite | postgres
        ctx.con.execute(f"INSTALL {kind}; LOAD {kind}") if kind != "duckdb" else None
        arg = cfg.get("path") or cfg["dsn"]
        ctx.con.execute(f"ATTACH {lit(arg)} AS {q(conn)} (TYPE {kind}, READ_ONLY)")
        ctx.attached.add(conn)
    schema, _, table = t["databaseName"].rpartition(".")
    if cfg["type"] != "postgres":
        schema = ""  # shortcut: sqlite/duckdb ignoran el esquema
    ref = ".".join(q(x) for x in [conn, schema, table] if x)
    return ctx.view(f"SELECT {sel} FROM {ref}")


# ---------- helpers de processors ----------
def _per_col(ctx, v, c, fn, token=None):
    """aplica fn(expr_sql) a columnsToProcess; en sitio o como columna nueva"""
    targets, new = c["columnsToProcess"], c.get("shouldCreateNewColumn")
    name = c.get("newColumnName") or c.get("newColumnRename")
    out = [f"{fn(q(x))} AS {q(x)}" if x in targets and not new else q(x) for x in ctx.cols(v)]
    if new:
        out += [f"{fn(q(t))} AS {q(name if name and len(targets) == 1 else t + '_new')}" for t in targets]
    return f"SELECT {', '.join(out)} FROM {v}"


_FUNCS = {"SubField": "split_part", "Upper": "upper", "Lower": "lower", "Trim": "trim", "Len": "length", "Left": "left",
          "Right": "right", "If": "if", "Floor": "floor", "Ceil": "ceil", "Round": "round", "Abs": "abs"}


def qexpr(s):
    """expresion Qlik -> SQL DuckDB (subconjunto)"""
    s = re.sub(r"\[([^\]]+)\]", lambda m: q(m.group(1)), s)
    s = re.sub(r"IsNull\(([^()]*)\)", r"(\1 IS NULL)", s)
    for f in set(re.findall(r"([A-Za-z_]\w*)\s*\(", s)):
        if f in _FUNCS:
            s = re.sub(rf"\b{f}\s*\(", _FUNCS[f] + "(", s)
        elif f.lower() not in _FUNCS.values() and f != "split_part":
            raise Unsupported(f"funcion Qlik '{f}' no soportada en calculate-fields")
    return s.replace("&", "||")


def _cond(f):
    col = q(f["columnName"])
    rhs = q(f["columnToCompareWith"]) if f["compareWith"] == "COLUMN" else lit(f["value"])
    op = f["operator"]
    simple = {"EQUAL": "=", "NOT_EQUAL": "<>", "GREATER": ">", "GREATER_OR_EQUAL": ">=", "LOWER": "<", "LOWER_OR_EQUAL": "<="}
    if op in simple:
        return f"({col} {simple[op]} {rhs})"
    if op == "IS_NOT_NULL":
        return f"({col} IS NOT NULL)"
    if op == "IS_NULL":
        return f"({col} IS NULL)"
    if op == "MATCH_REGEX":
        return f"regexp_matches(CAST({col} AS VARCHAR), {rhs})"
    if op == "CONTAINS":
        return f"(CAST({col} AS VARCHAR) LIKE '%' || {rhs} || '%')"
    raise Unsupported(f"filter operator {op}")


def _jfmt(p):  # patron Java/Qlik -> strptime
    for a, b in (("yyyy", "%Y"), ("YYYY", "%Y"), ("MM", "%m"), ("dd", "%d"), ("DD", "%d"), ("HH", "%H"), ("hh", "%H"),
                 ("mm", "%M"), ("ss", "%S"), ("fff", "%g")):
        p = p.replace(a, b)
    return p


_DATE_TOKENS = {"year": "year", "month": "month", "day": "day", "quarter": "quarter", "hour24": "hour", "minute": "minute",
                "second": "second", "dayOfWeek": "dayofweek", "dayOfYear": "dayofyear", "weekOfYear": "week"}


def run_processor(ctx, t, cfg, ins, node):
    """devuelve {tipo_de_handle: vista}"""
    v = ins[0] if ins else None
    D = lambda sql: {"DEFAULT": ctx.view(sql)}
    if t == "filter":
        conds = [_cond(f) for f in cfg["filters"]]
        w = (" AND " if cfg["logicalOpType"] == "ALL" else " OR ").join(conds)
        return {"DEFAULT": ctx.view(f"SELECT * FROM {v} WHERE {w}"), "REJECT": ctx.view(f"SELECT * FROM {v} WHERE NOT COALESCE({w}, false)")}
    if t == "field-selector":
        s = [x for x in cfg["selectors"] if x.get("selected", True)]
        return D(f"SELECT {'DISTINCT ' if cfg.get('distinct') else ''}{', '.join(q(x['path']) + ' AS ' + q(x['output'] or x['path']) for x in s)} FROM {v}")
    if t == "field-remover":
        drop = [x["path"] for x in cfg["selectors"] if x.get("selected", True)]
        return D(f"SELECT * EXCLUDE ({', '.join(q(x) for x in drop)}) FROM {v}")
    if t == "sort":
        return D(f"SELECT * FROM {v} ORDER BY {', '.join(q(s['fieldPath']) + (' DESC' if s['sortOrder'] == 'DESCENDING' else '') for s in cfg['sortFields'])}")
    if t == "fork":
        return {"DEFAULT": v, **{f"OPTIONAL_{i}": v for i in range(1, 10)}}
    if t == "union":
        return D(" UNION ALL BY NAME ".join(f"SELECT * FROM {i}" for i in ins) if cfg["unionAll"] else " UNION BY NAME ".join(f"SELECT * FROM {i}" for i in ins))
    if t == "join":
        l, r = ins
        lc, rc = ctx.cols(l), ctx.cols(r)
        drop = {c["rightKey"] for c in cfg["conditions"] if not c.get("keepBothKeysInOutput")}
        rsel = [f"r.{q(c)} AS {q(c + '_1' if c in lc else c)}" for c in rc if c not in drop]  # shortcut: colision -> sufijo _1
        kind = {"INNER_JOIN": "INNER", "LEFT_OUTER_JOIN": "LEFT", "RIGHT_OUTER_JOIN": "RIGHT", "FULL_OUTER_JOIN": "FULL"}[cfg["joinFunction"]]
        on = " AND ".join(f"l.{q(c['leftKey'])} = r.{q(c['rightKey'])}" for c in cfg["conditions"])
        return D(f"SELECT l.*{''.join(', ' + x for x in rsel)} FROM {l} l {kind} JOIN {r} r ON {on}")
    if t == "aggregate":
        ops = {"SUM": "sum", "COUNT": "count", "AVG": "avg", "MIN": "min", "MAX": "max", "MEDIAN": "median", "COUNT_DISTINCT": "count(DISTINCT"}
        g = [x["fieldPath"] for x in cfg["groupBy"]]
        sel = [q(x) for x in g]
        for o in cfg["operations"]:
            if o["operation"] not in ops:
                raise Unsupported(f"aggregate {o['operation']}")
            f = q(o["fieldPaths"][0])
            e = f"count(DISTINCT {f})" if o["operation"] == "COUNT_DISTINCT" else f"{ops[o['operation']]}({f})"
            sel.append(f"{e} AS {q(o['outputFieldPath'])}")
        return D(f"SELECT {', '.join(sel)} FROM {v}" + (f" GROUP BY {', '.join(q(x) for x in g)}" if g else ""))
    if t == "calculate-fields":
        return D(f"SELECT *, {', '.join(qexpr(c['expressionStatement']) + ' AS ' + q(c['newColumnName']) for c in cfg['calculateFields'])} FROM {v}")
    if t == "window":
        op = cfg["operationConfiguration"]
        if op["operationType"] not in ("RANK", "ROW_NUMBER", "DENSE_RANK"):
            raise Unsupported(f"window {op['operationType']}")
        part = ", ".join(q(x) for x in cfg["partitionByConfiguration"]["partitionByFieldList"])
        s = cfg["sortingConfiguration"]
        fn = op["operationType"].lower()
        return D(f"SELECT *, {fn}() OVER ({'PARTITION BY ' + part if part else ''} ORDER BY {q(s['sortBy'])} "
                 f"{'DESC' if s['sortOrder'] == 'DESCENDING' else ''}) AS {q(op['outputFieldName'])} FROM {v}")
    if t == "sample":
        k = cfg["type"]
        if k == "SAMPLE_FIRST_ROWS":
            return D(f"SELECT * FROM {v} LIMIT {int(cfg['sampleFirstRowsConfiguration']['rowCount'])}")
        if k == "SAMPLE_RANDOM_ROWS":  # semilla fija: ejecuciones repetibles
            return D(f"SELECT * FROM {v} USING SAMPLE {float(cfg['sampleRandomRowsConfiguration']['rowShare'])}% (bernoulli, 42)")
        if k == "SAMPLE_N_RANDOM_ROWS":
            return D(f"SELECT * FROM {v} USING SAMPLE {int(cfg['sampleNRandomRowsConfiguration']['rowCount'])} ROWS (reservoir, 42)")
        raise Unsupported(f"sample {k}")
    if t == "edit-column":
        c = cfg["renameColumnConfiguration"]
        return D(f"SELECT * RENAME ({q(c['columnsToProcess'][0])} AS {q(c['newColumnName'])}) FROM {v}")
    if t == "subflow":
        sf = next(s for s in ctx.subflows if s["id"] == cfg["dataflowId"])
        return {"DEFAULT": next(iter(run_graph(ctx, sf["graph"], [], {"linkedSource": v}).values()))}
    if t == "script":
        raise Unsupported("script de Qlik: validado pero no ejecutable en el emulador")
    return _typed(ctx, t, cfg, v)


def _typed(ctx, t, cfg, v):
    k, D = cfg.get("type"), (lambda sql: {"DEFAULT": ctx.view(sql)})
    if t == "math":
        if k == "ABSOLUTE":
            return D(_per_col(ctx, v, cfg["absoluteConfiguration"], lambda x: f"abs({x})"))
        c = cfg["multiplyConfiguration"]
        rhs = q(c["selectedColumn"]) if c["mode"] == "WITH_FIELD" else str(c["constantValue"])
        return D(_per_col(ctx, v, c, lambda x: f"({x} * {rhs})"))
    if t == "strings":
        c = cfg[dfw.TYPED["strings"][k]]
        S = lambda x: f"CAST({x} AS VARCHAR)"
        if k == "TRIM":
            return D(_per_col(ctx, v, c, lambda x: f"trim({S(x)})"))
        if k == "PROPERCASE":
            return D(_per_col(ctx, v, c, lambda x: f"array_to_string(list_transform(string_split(lower({S(x)}), ' '), lambda w: upper(w[1:1]) || w[2:]), ' ')"))
        if k == "REMOVE_NON_NUM_CHARS":
            return D(_per_col(ctx, v, c, lambda x: f"regexp_replace({S(x)}, '[^0-9]', '', 'g')"))
        if k == "UPPERCASE":
            return D(_per_col(ctx, v, c, lambda x: f"upper({S(x)})"))
        if k == "REPLACE_ON_VALUE":
            op, val, rep = c["cellValue"]["operator"], lit(c["cellValue"]["value"]), lit(c["replaceValue"])
            # matriz operador x metodo medida en el tenant (scripts de Qlik: Match, Left/Right con Len, Index)
            cond = {"EQUALS": lambda x: f"{S(x)} = {val}", "STARTS_WITH": lambda x: f"starts_with({S(x)}, {val})",
                    "ENDS_WITH": lambda x: f"ends_with({S(x)}, {val})", "CONTAINS": lambda x: f"contains({S(x)}, {val})"}.get(op)
            if cond and c["replaceMethod"] == "REPLACE_CELL_WITH_VALUE":  # toda la celda
                return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN {cond(x)} THEN {rep} ELSE {S(x)} END"))
            if cond and c["replaceMethod"] == "REPLACE_MATCHING_WITH_VALUE":  # solo la parte que coincide (EQUALS: toda la celda)
                if op == "CONTAINS":
                    return D(_per_col(ctx, v, c, lambda x: f"replace({S(x)}, {val}, {rep})"))
                new = {"EQUALS": lambda x: rep, "STARTS_WITH": lambda x: f"{rep} || substr({S(x)}, length({val}) + 1)",
                       "ENDS_WITH": lambda x: f"substr({S(x)}, 1, length({S(x)}) - length({val})) || {rep}"}[op]
                return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN {cond(x)} THEN {new(x)} ELSE {S(x)} END"))
        raise Unsupported(f"strings {k} {c.get('replaceMethod', '')}")
    if t == "numbers":
        c = cfg["convertToNumberConfiguration"]
        return D(_per_col(ctx, v, c, lambda x: f"TRY_CAST(replace(replace(CAST({x} AS VARCHAR), {lit(c['thousandSeparator'])}, ''), {lit(c['decimalSeparator'])}, '.') AS DOUBLE)"))
    if t == "masking":
        return D(_per_col(ctx, v, cfg["hashDataConfiguration"], lambda x: f"md5(CAST({x} AS VARCHAR))"))
    if t == "data-cleansing":
        if k == "REPLACE_WITH_VALUE":
            c = cfg["replaceWithValueConfiguration"]
            return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN {x} IS NULL OR trim(CAST({x} AS VARCHAR)) = '' THEN {lit(c['defaultValue'])} ELSE {x} END"))
        c = cfg["fillWithValueConfiguration"]
        if c.get("mode") != "WITH_VALUE":
            raise Unsupported(f"data-cleansing FILL_WITH_VALUE modo {c.get('mode')}")
        # "Fill cells with value" rellena TODAS las celdas (Qlik: 'X' AS [campo]); las vacias son REPLACE_WITH_VALUE
        return D(_per_col(ctx, v, {**c, "shouldCreateNewColumn": False}, lambda x: lit(c['defaultValue'])))
    if t == "split-field":
        c = cfg["splitTextInPartsConfiguration"]
        sep = " " if c["separator"] == "SPACE" else c["customSeparatorValue"]
        col = c["columnsToProcess"][0]
        n, S = c["parts"], f"CAST({q(col)} AS VARCHAR)"
        # Qlik: SubField(c, sep, i) AS [c-split_i]; la ultima parte conserva el resto (Mid(c, Index(c, sep, n-1) + 1)), '' si falta.
        # shortcut: para parts > 2 se supone la misma regla (solo se midio parts = 2); verificar con un flujo de 3 partes
        parts = [f"split_part({S}, {lit(sep)}, {i}) AS {q(f'{col}-split_{i}')}" for i in range(1, n)]
        parts.append(f"array_to_string(list_slice(string_split({S}, {lit(sep)}), {n}, 1000000), {lit(sep)}) AS {q(f'{col}-split_{n}')}")
        return D(f"SELECT *, {', '.join(parts)} FROM {v}")
    if t == "field-concatenator":
        c = cfg["concatConfiguration"]
        a, b = q(c["columnsToProcess"][0]), q(c["selectedColumn"])
        sep = (f"CASE WHEN coalesce(CAST({a} AS VARCHAR),'') <> '' AND coalesce(CAST({b} AS VARCHAR),'') <> '' THEN {lit(c['separator'])} ELSE '' END"
               if c["separatorCondition"] == "BOTH_VALUES_NOT_EMPTY" else lit(c["separator"]))
        e = f"{lit(c['prefix'])} || coalesce(CAST({a} AS VARCHAR),'') || {sep} || coalesce(CAST({b} AS VARCHAR),'') || {lit(c['suffix'])}"
        name = c["newColumnName"] or f"{c['columnsToProcess'][0]}_{c['selectedColumn']}"  # shortcut: nombre por defecto supuesto
        return D(f"SELECT *, {e} AS {q(name)} FROM {v}") if c["shouldCreateNewColumn"] else D(f"SELECT * REPLACE ({e} AS {a}) FROM {v}")
    if t == "date":
        return D(_date(ctx, v, k, cfg[dfw.TYPED["date"][k]]))
    raise Unsupported(f"processor {t}")


def _date(ctx, v, k, c):
    col = c["columnsToProcess"][0]
    S = f"CAST({q(col)} AS VARCHAR)"
    if k == "EXTRACT_DATE_PARTS":
        ts = f"try_strptime({S}, {lit(_jfmt(c['datePattern']))})"
        prefix = c.get("newColumnRename") or col  # medido: con rename "fecha_" Qlik genera [fecha__day]
        parts = [f"{_DATE_TOKENS[t]}({ts}) AS {q(f'{prefix}_{t}')}" for t in _DATE_TOKENS if c.get(t)]
        for t in c:
            if c[t] is True and t not in _DATE_TOKENS and t not in ("shouldCreateNewColumn", "amPm"):
                raise Unsupported(f"date token {t}")
        return f"SELECT *, {', '.join(parts)} FROM {v}"
    cast = "DATE" if k == "CONVERT_TO_DATE" else "TIMESTAMP"
    e = f"TRY_CAST({S} AS {cast})" if c["format"] == "auto" else f"CAST(try_strptime({S}, {lit(_jfmt(c['datePattern']))}) AS {cast})"
    name = c["newColumnRename"] or col
    return f"SELECT *, {e} AS {q(name)} FROM {v}" if c["shouldCreateNewColumn"] and name != col else f"SELECT * REPLACE ({e} AS {q(col)}) FROM {v}"


# ---------- grafo ----------
def run_graph(ctx, graph, sources, bind):
    """ejecuta un grafo en orden topologico; devuelve {id_target: vista}. bind: {'linkedSource': vista} para subflows"""
    nodes = {n["id"]: n for n in graph["nodes"]}
    src_of = {e["targetHandle"]: e["sourceHandle"] for e in graph["edges"]}
    produced, targets, pending = {}, {}, list(nodes.values())
    while pending:
        progress = False
        for n in list(pending):
            inc = n.get("handles", {}).get("incoming", [])
            if not all(h["id"] in src_of and src_of[h["id"]] in produced for h in inc if h["id"] in src_of or h["type"] == "DEFAULT"):
                continue
            ins = [produced[src_of[h["id"]]] for h in inc if h["id"] in src_of]
            ct, cfg = n["component"]["type"], n["component"]["properties"].get("configuration", {})
            if n["type"] == "source":
                out = {"DEFAULT": bind["linkedSource"] if ct == "linkedSource" else _source(ctx, n, sources)}
            elif n["type"] == "processor":
                out = run_processor(ctx, ct, cfg, ins, n)
            else:
                targets[n["id"]] = (n, ins[0])
                out = {}
            for h in n.get("handles", {}).get("outgoing", []):
                if h["type"] in out:
                    produced[h["id"]] = out[h["type"]]
            pending.remove(n)
            progress = True
        if not progress:
            raise RuntimeError("no se pudo resolver el orden de ejecucion (nodos sin conectar)")
    return {k: v[1] for k, v in targets.items()} if bind else targets


def _write(ctx, n, view):
    cfg = n["component"]["properties"]["configuration"]
    s = cfg["settings"]
    if s["format"] not in ("txt", "qvd", "parquet"):  # el servidor acepta otros valores; el emulador no los escribe
        raise Unsupported(f"target {s['format']}: validado pero no ejecutable en el emulador")
    name = s["fileName"].lstrip("/")
    s3 = "AmazonS3" in cfg.get("$datasourceId", "")
    emulated = s["format"] == "qvd"  # qvd es propietario: se escribe parquet
    fmt = "parquet" if s["format"] in ("qvd", "parquet") else "csv"
    suffix = ".qvd.parquet" if emulated else f".{s['extension']}"
    if s3 and ctx.s3:
        dest = f"s3://{name}{suffix}"
    else:
        dest = os.path.join(ctx.out_dir, "s3" if s3 else s.get("connectionName", "files"), name + suffix)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
    opts = "FORMAT parquet" if fmt == "parquet" else "FORMAT csv, HEADER"
    ctx.con.execute(f"COPY (SELECT * FROM {view}) TO {lit(dest)} ({opts})")
    rows = ctx.con.execute(f"SELECT count(*) FROM {view}").fetchone()[0]
    return {"target": n["label"], "dest": dest, "rows": rows, "emulated_qvd": emulated}


def run(d, data_dir, out_dir, connections=None, s3=None):
    ctx = Ctx(data_dir, out_dir, connections, s3)
    ctx.subflows = d.get("subflows", [])
    targets = run_graph(ctx, d["dataflow"]["graph"], d["sources"], {})
    return [_write(ctx, n, v) for n, v in targets.values()]
