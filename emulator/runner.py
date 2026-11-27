"""Ejecuta un .dfw sobre DuckDB: origenes (CSV / BD), processors como SQL, destinos a disco o S3 (MinIO)."""
import json
import os
import re

import duckdb

from . import dfw

BS = chr(92)
q = lambda c: '"' + str(c).replace('"', '""') + '"'
lit = lambda s: "'" + str(s).replace("'", "''") + "'"


class Unsupported(Exception):
    pass


class Ctx:
    def __init__(self, data_dir, out_dir, connections=None, s3=None):
        self.con = duckdb.connect()
        self.data_dir, self.out_dir, self.connections, self.s3 = data_dir, out_dir, {} if connections is None else connections, s3
        self.n, self.attached, self.report = 0, set(), []
        self.locale = ""  # collationLocale del flujo; de el salen los SET de formato de fecha del script de Qlik
        self.fixed_decimals = {}  # columna -> decimales fijos al escribir (salida de ROUND/CEIL/FLOOR con precision > 0)
        self.converted_dates = {}  # columna -> 'date' | 'timestamp' (salida de CONVERT_TO_DATE / CONVERT_TO_TIMESTAMP)
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
# numero en-US como lo lee Qlik: miles con coma solo en grupos de 3, punto decimal, signo opcional
_NUM_RE = r"^[+-]?(DIGITS+|DIGITS{1,3}(,DIGITS{3})+)([.]DIGITS+)?$".replace("DIGITS", BS + "d")


def _qlik_symbols(ctx, view, text_cols, fields):
    """Qlik guarda cada valor distinto de un campo una sola vez: los textos que interpreta como el mismo numero o la misma fecha
    quedan con el primer texto leido (medido: '1,200.50' sale como '1200.50' si ya habia un '1200.50'; '09/09/2026' como
    '2026-09-09'). Numeros: `_NUM_RE`; fechas: YYYY-MM-DD, M/D/YYYY, con hora o con T.
    shortcut: solo configuracion regional en-US; no se unifica un numero con una fecha ni se conocen todos los formatos de fecha."""
    if not text_cols:
        return view
    keys = []
    for f in text_cols:
        c = q(f)
        dt = ", ".join(f"try_strptime({c}, '{fmt}')" for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"))
        keys.append(f"CASE WHEN regexp_matches({c}, {lit(_NUM_RE)}) THEN 'n' || CAST(CAST(replace({c}, ',', '') AS DOUBLE) AS VARCHAR) "
                    f"ELSE 'd' || CAST(coalesce({dt}) AS VARCHAR) END AS {q('__k_' + f)}")
    inner = ctx.view(f"SELECT *, row_number() OVER () AS __rn, {', '.join(keys)} FROM {view}")
    cols = [f"CASE WHEN {q('__k_' + f)} IS NULL THEN {q(f)} ELSE first_value({q(f)}) OVER (PARTITION BY {q('__k_' + f)} ORDER BY __rn) END AS {q(f)}"
            if f in text_cols else q(f) for f in fields]
    return ctx.view(f"SELECT {', '.join(cols)} FROM {inner} ORDER BY __rn")  # la ventana reordena: se conserva el orden del archivo


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
    if cfg["type"] == "stub":
        # relleno para probar la forma de un flujo sin su base de datos: pocas filas enteras; el .dfw desidentificado no trae tipos,
        # asi que los textos, fechas y decimales no se ejercitan (shortcut: usar un duckdb/sqlite real si importan)
        cols = [f"((i * {n + 3}) % 97 + 1) AS {q(f)}" for n, f in enumerate(fields)]
        return ctx.view(f"SELECT {', '.join(cols)} FROM range({int(cfg.get('rows', 20))}) t(i)")
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


_TEXT_FUNCS = ("SubField", "Upper", "Lower", "Trim", "Len", "Left", "Right")


def _first_arg_end(s, i):
    """posicion del fin del primer argumento de la llamada que abre en s[i-1] == '(' (respeta comillas y parentesis anidados)"""
    depth, quote = 0, None
    for j in range(i, len(s)):
        ch = s[j]
        if quote:
            quote = None if ch == quote else quote
        elif ch in "'\"":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                return j
            depth -= 1
        elif ch == "," and depth == 0:
            return j
    return len(s)


def _cast_text_args(s):
    """Qlik acepta numeros en sus funciones de texto; DuckDB exige VARCHAR: envuelve el primer argumento en CAST"""
    for f in _TEXT_FUNCS:
        pos = 0
        while True:
            m = re.compile(rf"\b{f}\s*\(").search(s, pos)
            if not m:
                break
            end = _first_arg_end(s, m.end())
            s = f"{s[:m.end()]}CAST({s[m.end():end]} AS VARCHAR){s[end:]}"
            pos = m.end()
    return s


def qexpr(s):
    """expresion Qlik -> SQL DuckDB (subconjunto)"""
    s = re.sub(r"\[([^\]]+)\]", lambda m: q(m.group(1)), s)
    s = _cast_text_args(s)
    s = re.sub(r"IsNull\(([^()]*)\)", r"(\1 IS NULL)", s)
    for f in set(re.findall(r"([A-Za-z_]\w*)\s*\(", s)):
        if f in _FUNCS:
            s = re.sub(rf"\b{f}\s*\(", _FUNCS[f] + "(", s)
        elif f.lower() not in _FUNCS.values() and f not in ("split_part", "CAST"):
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
    return re.sub(r"(?<!%)d", "%-d", re.sub(r"(?<!%)M", "%-m", p))  # M y d sueltos: sin cero a la izquierda (medido: 'M/d/yyyy' lee 9/9/2026)


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
        # Orden de salida determinista: filas de la izquierda en su orden y al final las que solo estan a la derecha. NO es el orden
        # de Qlik, que no se pudo deducir (con claves unicas y ordenadas coincide; con claves repetidas agrupa por clave y reordena
        # las filas dentro del grupo): por eso la bateria compara los joins por contenido y no por orden.
        # En las filas solo-derecha la clave viene de la derecha (medido en FULL y RIGHT)
        lsel = "l.* EXCLUDE (__ln)"
        if kind in ("FULL", "RIGHT"):
            lsel += " REPLACE (" + ", ".join(f"coalesce(l.{q(c['leftKey'])}, r.{q(c['rightKey'])}) AS {q(c['leftKey'])}"
                                             for c in cfg["conditions"] if c["rightKey"] in drop) + ")" if drop else ""
        return D(f"SELECT {lsel}{''.join(', ' + x for x in rsel)} FROM (SELECT *, row_number() OVER () AS __ln FROM {l}) l "
                 f"{kind} JOIN (SELECT *, row_number() OVER () AS __rn FROM {r}) r ON {on} ORDER BY l.__ln NULLS LAST, r.__rn")
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
        if not g:
            return D(f"SELECT {', '.join(sel)} FROM {v}")
        # Qlik devuelve los grupos en el orden en que aparecen en la tabla de origen (medido); DuckDB no lo garantiza
        return D(f"SELECT {', '.join(sel)} FROM (SELECT *, row_number() OVER () AS __rn FROM {v}) "
                 f"GROUP BY {', '.join(q(x) for x in g)} ORDER BY min(__rn)")
    if t == "calculate-fields":
        return D(f"SELECT *, {', '.join(qexpr(c['expressionStatement']) + ' AS ' + q(c['newColumnName']) for c in cfg['calculateFields'])} FROM {v}")
    if t == "window":
        op = cfg["operationConfiguration"]
        kind = op["operationType"]
        part = ", ".join(q(x) for x in cfg["partitionByConfiguration"]["partitionByFieldList"])
        s = cfg["sortingConfiguration"]
        order = f"ORDER BY {q(s['sortBy'])} {'DESC' if s['sortOrder'] == 'DESCENDING' else ''}"
        over = f"{'PARTITION BY ' + part if part else ''} {order}"
        if kind in ("RANK", "ROW_NUMBER"):
            fn = f"{kind.lower()}()"
        else:
            # Window(agg(c), particion, 'ASC'|'DESC', orden[, 1, inicio, fin]) en el script de Qlik; sin rango, toda la particion
            f = q(op["operationFields"][0])
            num = f"TRY_CAST({f} AS DOUBLE)"
            fns = {"SUM": f"sum({num})", "AVG": f"avg({num})", "MIN": f"min({num})", "MAX": f"max({num})",
                   "COUNT": f"count({f})", "FIRST": f"first_value({f})", "LAST": f"last_value({f})",
                   "COUNT_DISTINCT": f"list({f})", "CONCATENATE": f"string_agg(CAST({f} AS VARCHAR), {lit(op.get('delimiter', ','))} ORDER BY CAST({f} AS VARCHAR))"}  # Concat ordena por el texto, no por el orden de la ventana (medido)
            if kind not in fns:
                raise Unsupported(f"window {kind}")
            r = cfg["rangeConfiguration"]
            bound = lambda t, n, unl: {"UNLIMITED": unl, "CURRENT": "CURRENT ROW", "PRECEDING": f"{n} PRECEDING", "FOLLOWING": f"{n} FOLLOWING"}[t]
            frame = (f"ROWS BETWEEN {bound(r['windowStartType'], r['windowStartValue'], 'UNBOUNDED PRECEDING')} AND "
                     f"{bound(r['windowEndType'], r['windowEndValue'], 'UNBOUNDED FOLLOWING')}")
            fn, over = fns[kind], f"{over} {frame}"
        # Qlik devuelve las filas en el orden de origen con la columna de la ventana (medido); no las reordena por ella
        expr = f"{fn} OVER ({over})"
        if kind == "COUNT_DISTINCT":  # DuckDB no admite DISTINCT con orden ni marco: se cuentan los distintos de la lista del marco
            expr = f"len(list_distinct({expr}))"
        if kind == "AVG":
            expr = f"CAST(printf('%.8g', {expr}) AS DOUBLE)"  # medido: Window(Avg()) llega con 8 cifras significativas
        return D(f"SELECT * EXCLUDE (__rn) FROM (SELECT *, {expr} AS {q(op['outputFieldName'])} "
                 f"FROM (SELECT *, row_number() OVER () AS __rn FROM {v})) ORDER BY __rn")
    if t == "unpivot":
        # CROSSTABLE(atributo, valor, n) de Qlik: las columnas no seleccionadas quedan como claves (en su orden), cada columna
        # seleccionada pasa a una fila por cada fila de origen, y los NULL se omiten. Los valores se mezclan como texto
        cols = cfg["unpivotColumns"]
        keys = [c for c in ctx.cols(v) if c not in cols]
        ksql = ", ".join(q(c) for c in keys)
        parts = [f"SELECT {ksql + ', ' if keys else ''}{lit(c)} AS {q(cfg['attributeColumn'])}, CAST({q(c)} AS VARCHAR) AS "
                 f"{q(cfg['valueColumn'])}, __rn, {i} AS __ord FROM (SELECT *, row_number() OVER () AS __rn FROM {v}) WHERE {q(c)} IS NOT NULL"
                 for i, c in enumerate(cols)]
        out = ", ".join([q(c) for c in keys] + [q(cfg["attributeColumn"]), q(cfg["valueColumn"])])
        return D(f"SELECT {out} FROM ({' UNION ALL '.join(parts)}) ORDER BY __rn, __ord")
    if t == "pivot":
        raise Unsupported("pivot: no se pudo crear por API (necesita un schemaEntityId que crea la interfaz), asi que no se verifico contra el tenant")
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
        c = cfg[dfw.TYPED["math"][k]]
        # Qlik: Sin, Cos, Tan, Log10, Log; el logaritmo de un no positivo es NULL (DuckDB daria error)
        unary = {"ABSOLUTE": "abs({x})", "NEGATE_NUMBERS": "(-{x})", "SQUARE_ROOT_NUMBERS": "sqrt({x})", "SIN_NUMBERS": "sin({x})",
                 "COS_NUMBERS": "cos({x})", "TAN_NUMBERS": "tan({x})", "EXPONENTIEL_NUMBERS": "exp({x})",
                 "LOGARITHM_NUMBERS": "CASE WHEN {x} > 0 THEN log10({x}) END", "NATURAL_LOGARITHM_NUMBERS": "CASE WHEN {x} > 0 THEN ln({x}) END"}
        if k in unary:
            return D(_per_col(ctx, v, c, lambda x: unary[k].format(x=x)))
        # operaciones con otro campo (mode WITH_FIELD) o con un valor fijo; hipotesis contrastada con el tenant en la bateria
        binary = {"MULTIPLY": "({x} * {r})", "ADD": "({x} + {r})", "SUBTRACT": "({x} - {r})", "DIVIDE": "({x} / {r})",
                  "MODULO": "({x} % {r})", "POW_NUMBERS": "pow({x}, {r})", "MIN_NUMBERS": "least({x}, {r})",
                  "MAX_NUMBERS": "greatest({x}, {r})"}
        if k not in binary:
            raise Unsupported(f"math {k}")
        rhs = q(c["selectedColumn"]) if c["mode"] == "WITH_FIELD" else str(c["constantValue"])
        return D(_per_col(ctx, v, c, lambda x: binary[k].format(x=x, r=rhs)))
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
        if k == "LOWERCASE":
            return D(_per_col(ctx, v, c, lambda x: f"lower({S(x)})"))
        # expresiones leidas en el script que genera Qlik (2026-11-23); los parametros finos (ancho del relleno, posiciones de
        # SUBSTRING) no se descubrieron: se emulan los valores por defecto del servidor (5)
        if k == "COMPUTE_LENGTH":  # Len([c]) AS [c_length]
            return D(_derived(v, c, "length", lambda x: f"length({S(x)})"))
        if k == "CONTAINS":  # IF(Index([c], 'v'), Dual('TRUE', -1), Dual('FALSE', 0)) AS [c_contains_v]
            val = lit(c["constantValue"])
            return D(_derived(v, c, f"contains_{c['constantValue']}",
                              lambda x: f"CASE WHEN strpos({S(x)}, {val}) > 0 THEN 'TRUE' ELSE 'FALSE' END"))
        if k == "PADDING":  # Repeat('0', 5 - Len([c])) & [c] | [c] & Repeat(...) segun paddingPosition (medido 2026-11-27)
            size = int(c.get("size", 5) or 5)
            ch = str(c.get("paddingCharacter", "0") or "0").replace("'", "''")
            rep = f"repeat('{ch}', greatest({size} - length({S('%s')}), 0))"
            if str(c.get("paddingPosition", "LEFT")).upper() == "RIGHT":
                return D(_per_col(ctx, v, c, lambda x: f"{S(x)} || " + rep % x))
            return D(_per_col(ctx, v, c, lambda x: rep % x + f" || {S(x)}"))
        if k == "SUBSTRING":  # Mid([c], desde[, largo]) con los argumentos que genera Qlik (medido 2026-11-27)
            cfg_sub = c

            def _sub(x: str) -> str:
                frm = cfg_sub.get("fromType", "FROM_BEGINNING")
                to = cfg_sub.get("toType", "TO_INDEX")  # sin claves Qlik genera Mid(c, 1, 5)
                idx = int(cfg_sub.get("fromIndex", 0) or 0)
                if frm == "FROM_BEGINNING":
                    start = "1"
                elif frm == "FROM_INDEX":
                    start = f"{idx + 1}"
                elif frm == "FROM_N_BEFORE_END":  # medido: Mid(c, Len(c) - (n-1))
                    n_end = int(cfg_sub.get("fromNBeforeEnd", 0) or 0)
                    start = f"(length({x}) - {max(n_end - 1, 0)})"
                else:
                    raise Unsupported(f"SUBSTRING {frm}")
                if to == "TO_END":  # todo el texto desde `start`
                    if frm == "FROM_BEGINNING":
                        return x  # Qlik no emite nada: el campo pasa igual
                    if frm == "FROM_N_BEFORE_END":  # Qlik: Coalesce(EmptyIsNull(Mid(...)),[c])
                        return f"coalesce(nullif(substr({x}, {start}), ''), {x})"
                    return f"substr({x}, {start})"
                if to == "TO_INDEX":
                    n = int(cfg_sub.get("toIndex", 5) or 5)
                    return f"substr({x}, {start}, {n if frm == 'FROM_BEGINNING' else n - idx + 1})"
                if to == "TO_N_BEFORE_END":  # Qlik: Mid([c], start, Len([c]) - n)
                    return f"substr({x}, {start}, length({x}) - {int(cfg_sub.get('toNBeforeEnd', 0) or 0)})"
                raise Unsupported(f"SUBSTRING {to}")

            return D(_per_col(ctx, v, c, _sub))
        if k == "CONVERT_TO_STRING":  # Text([c])
            return D(_per_col(ctx, v, c, lambda x: S(x)))
        if k == "REMOVE_NON_ALPHA_NUM_CHARS":  # KeepChar([c], ALPHA_NUM_CHARS); shortcut: solo letras ASCII y digitos
            return D(_per_col(ctx, v, c, lambda x: f"regexp_replace({S(x)}, '[^A-Za-z0-9]', '', 'g')"))
        if k == "MATCHES_PATTERN":  # IF(CountRegEx([c], regex), Dual('TRUE',-1), Dual('FALSE',0)) AS [c_matching] (medido 2026-11-27)
            pats = {"ANY_WORD_CASE_INSENSITIVE": "^[a-zA-Z]+$", "ANY_LITERAL_WITH_ALPHA_NUMERIC_CHARACTERS": "^[a-zA-Z0-9]+$",
                    "NUMBER": "^[0-9]+$", "A_WORD_IN_LOWERCASE": "^[a-z]+$", "A_WORD_IN_UPPERCASE": "^[A-Z]+$"}
            pat = pats.get(str(c.get("proposedPattern", "ANY_WORD_CASE_INSENSITIVE")))
            if pat is None:  # OTHER: el servidor responde 500 y no hay regex que copiar
                raise Unsupported(f"matches pattern {c.get('proposedPattern')}")
            return D(_derived(v, c, "matching", lambda x: f"CASE WHEN regexp_matches({S(x)}, '{pat}') THEN 'TRUE' ELSE 'FALSE' END"))
        if k == "REMOVE_CONSECUTIVE_CHARACTERS":  # ReplaceRegEx([c], '(\Q\\s\E){2,}', ' '): con el patron por defecto no cambia nada util
            return D(_per_col(ctx, v, c, lambda x: S(x)))
        if k == "CUT":  # EQUALS: IF(Match([c], 'a'), '', [c]); CONTAINS: Replace([c], 'a', ''); STARTS_WITH/ENDS_WITH: corta el borde; shortcut: sin regex
            c = cfg["cutConfiguration"]
            op, val = c["pattern"]["operator"], lit(c["pattern"]["value"])
            if op == "EQUALS":
                return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN {S(x)} = {val} THEN '' ELSE {S(x)} END"))
            if op == "CONTAINS":
                return D(_per_col(ctx, v, c, lambda x: f"replace({S(x)}, {val}, '')"))
            if op == "STARTS_WITH":  # corta el prefijo cuando coincide
                return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN starts_with({S(x)}, {val}) THEN substr({S(x)}, length({val}) + 1) ELSE {S(x)} END"))
            if op == "ENDS_WITH":  # corta el sufijo cuando coincide
                return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN ends_with({S(x)}, {val}) THEN substr({S(x)}, 1, length({S(x)}) - length({val})) ELSE {S(x)} END"))
            raise Unsupported(f"strings CUT {op}")
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
        if k == "REMOVE_NEGATIVE_VALUES":  # IF([c] < 0, Null(), [c]) AS [c]: siempre en sitio, aunque pida columna nueva
            c = cfg["removeNegativeValuesConfiguration"]
            return D(_per_col(ctx, v, {**c, "shouldCreateNewColumn": False},
                              lambda x: f"CASE WHEN TRY_CAST({x} AS DOUBLE) < 0 THEN NULL ELSE {x} END"))
        if k == "COMPARE_NUMBERS":  # IF([c] op valor, Dual('TRUE',-1), Dual('FALSE',0)) (medido 2026-11-27)
            cn = cfg["compareNumbersConfiguration"]
            ops = {"EQUALS": "=", "EQUAL": "=", "NOT_EQUALS": "<>", "GREATER_THAN": ">", "GREATER_OR_EQUAL": ">=",
                   "LESS_THAN": "<", "LESS_OR_EQUAL": "<=", "GREATER_THAN_OR_EQUAL": ">=", "LESS_THAN_OR_EQUAL": "<="}
            op = ops.get(cn.get("comparisonOperator", "EQUALS"))
            if op is None:
                raise Unsupported(f"compare numbers {cn.get('comparisonOperator')}")
            if cn.get("comparisonType") in ("FIELD", "OTHER_COLUMN") and cn.get("column"):
                rhs = f"TRY_CAST({q(cn['column'])} AS DOUBLE)"
            else:
                rhs = str(cn.get("constantValue", 0))
            return D(_per_col(ctx, v, cn, lambda x: f"CASE WHEN TRY_CAST({x} AS DOUBLE) {op} {rhs} THEN 'TRUE' ELSE 'FALSE' END"))
        if k == "ROUND_DOWN_REAL":  # IF([c] > 0, Floor([c]), Ceil([c])): hacia cero
            return D(_per_col(ctx, v, cfg["roundDownRealConfiguration"], lambda x: f"trunc(TRY_CAST({x} AS DOUBLE))"))
        if k in _ROUND:  # ROUND([c], 0.01) / CEIL([c], 0.1) / FLOOR([c], 0.1): paso 10^-precision (ROUND(x) si es 0)
            c, fn = cfg[dfw.TYPED["numbers"][k]], _ROUND[k]
            p = int(c.get("precision") or 0)

            def rnd(x):
                x = f"TRY_CAST({x} AS DOUBLE)"
                if p == 0:
                    return f"{fn}({x})"
                # medido con saldos de .x5: Qlik divide por el paso (ROUND([c], 0.1)), round(x, 1) daria otro resultado
                return f"{fn}({x} / {10.0 ** -p}) * {10.0 ** -p}"
            # medido: con precision > 0 Qlik escribe siempre `p` decimales (-35.00, -35.0); sigue siendo un numero. Con 0 el formato
            # tambien alcanza a las filas de otra rama con el mismo nombre de columna tras un UNION (45.75 sale como 46)
            tg = c["columnsToProcess"]
            for t in tg:
                name = (c.get("newColumnName") if len(tg) == 1 and c.get("newColumnName") else t + "_new") if c.get("shouldCreateNewColumn") else t
                ctx.fixed_decimals[name] = p
            return D(_per_col(ctx, v, c, rnd))
        if k == "ROUND_DOWN":  # IF([c] > 0, Floor([c]), CEIL([c])): igual que ROUND_DOWN_REAL
            return D(_per_col(ctx, v, cfg["removeFractionalPartConfiguration"], lambda x: f"trunc(TRY_CAST({x} AS DOUBLE))"))
        if k == "FORMAT_NUMBER":
            c = cfg["formatNumberConfiguration"]
            return D(_per_col(ctx, v, c, lambda x: _format_number(c, f"TRY_CAST({x} AS DOUBLE)")))
        c = cfg["convertToNumberConfiguration"]
        # num(num#([c], '#', dec, mil)): solo un numero bien formado (miles en grupos de 3); '10,5', '1.200,50' o 'NaN' dan NULL (medido)
        dec, mil = c["decimalSeparator"] or ".", c["thousandSeparator"]
        e = lambda ch: "[" + ch.replace(BS, BS * 2) + "]"
        whole = f"DIGITS+|DIGITS{{1,3}}({e(mil)}DIGITS{{3}})+" if mil else "DIGITS+"
        pat = f"^[+-]?({whole})({e(dec)}DIGITS+)?$".replace("DIGITS", BS + "d")
        return D(_per_col(ctx, v, c, lambda x: f"CASE WHEN regexp_matches(trim(CAST({x} AS VARCHAR)), {lit(pat)}) THEN "
                                              f"TRY_CAST(replace(replace(trim(CAST({x} AS VARCHAR)), {lit(mil)}, ''), {lit(dec)}, '.') AS DOUBLE) END"))
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
        # una parte que no existe es NULL, no '' (SubField fuera de rango y Mid(c, '') dan NULL; medido en una cadena con REPLACE_ON_VALUE)
        parts = [f"CASE WHEN len(string_split({S}, {lit(sep)})) >= {i} THEN split_part({S}, {lit(sep)}, {i}) END AS {q(f'{col}-split_{i}')}"
                 for i in range(1, n)]
        parts.append(f"CASE WHEN len(string_split({S}, {lit(sep)})) >= {n} THEN "
                     f"array_to_string(list_slice(string_split({S}, {lit(sep)}), {n}, 1000000), {lit(sep)}) END AS {q(f'{col}-split_{n}')}")
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


_ROUND = {"ROUND": "round", "CEIL": "ceil", "FLOOR": "floor"}
_FMT = {"THOUSAND_WITHOUT_DECIMAL": (0, False), "THOUSAND_WITH_1_DECIMAL": (1, False), "THOUSAND_WITH_2_DECIMAL": (2, False),
        "PERCENTAGE_WITHOUT_DECIMAL": (0, True), "PERCENTAGE_WITH_1_DECIMAL": (1, True), "PERCENTAGE_WITH_2_DECIMAL": (2, True)}


def _format_number(c, x):
    """num([c], '#,##0.00', dec, mil) / num([c], '0.0%', ...); shortcut: sin formato personalizado (CUSTOM)"""
    if c["outputFormat"] not in _FMT:
        raise Unsupported(f"FORMAT_NUMBER {c['outputFormat']}")
    d, pct = _FMT[c["outputFormat"]]
    if pct:  # el porcentaje no lleva separador de miles
        return f"replace(format('{{:.{d}f}}', round({x} * 100, {d})), '.', {lit(c['decimalSeparator'])}) || '%'"
    body = f"format('{{:,.{d}f}}', round({x}, {d}))"
    return f"replace(replace(replace({body}, ',', chr(1)), '.', {lit(c['decimalSeparator'])}), chr(1), {lit(c['thousandSeparator'])})"


_TRUNC = {"YEAR": ("year", "date"), "MONTH": ("month", "date"), "DAY": ("day", "date"),
          "HOUR": ("hour", "timestamp"), "MINUTE": ("minute", "timestamp"), "SECOND": ("second", "timestamp")}


def _derived(v, c, suffix, fn):
    """columna nueva `<col>_<suffix>` por cada columna a procesar (el nombre no sale de newColumnName: medido en Qlik)"""
    return f"SELECT *, {', '.join(f'{fn(q(t))} AS {q(t + chr(95) + suffix)}' for t in c['columnsToProcess'])} FROM {v}"


_AUTO_DATES = ("%Y-%m-%d", "%m/%d/%Y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S")


def _date(ctx, v, k, c):
    col = c["columnsToProcess"][0]
    S = f"CAST({q(col)} AS VARCHAR)"
    if k == "TRUNCATE_DATE":  # YearStart/MonthStart/Floor(x)/Floor(x*24)/24... AS [c_truncated]; WEEK y sub-segundos los rechaza el servidor
        if c["timeUnit"] not in _TRUNC:
            raise Unsupported(f"TRUNCATE_DATE {c['timeUnit']}: el servidor no lo compila")
        unit, kind = _TRUNC[c["timeUnit"]]
        ctx.converted_dates[f"{col}_truncated"] = kind
        return _derived(v, c, "truncated", lambda x: f"CAST(date_trunc('{unit}', TRY_CAST(CAST({x} AS VARCHAR) AS TIMESTAMP)) AS {kind.upper()})")
    if k == "EXTRACT_DATE_PARTS":
        src = S
        if ctx.locale.lower().startswith("en") and ctx.converted_dates.get(col) in ("date", "timestamp"):  # medido: el patron se aplica al texto M/D/YYYY de la fecha
            src = f"strftime({q(col)}, '%-m/%-d/%Y')" if ctx.converted_dates[col] == "date" else f"strftime({q(col)}, '%-m/%-d/%Y %-I:%M:%S %p')"
        ts = f"try_strptime({src}, {lit(_jfmt(c['datePattern']))})"
        prefix = c.get("newColumnRename") or col  # medido: con rename "fecha_" Qlik genera [fecha__day]
        parts = [f"{_DATE_TOKENS[t]}({ts}) AS {q(f'{prefix}_{t}')}" for t in _DATE_TOKENS if c.get(t)]
        for t in c:
            if c[t] is True and t not in _DATE_TOKENS and t not in ("shouldCreateNewColumn", "amPm"):
                raise Unsupported(f"date token {t}")
        return f"SELECT *, {', '.join(parts)} FROM {v}"
    if k in ("FORMAT_DATES", "MODIFY_DATES"):
        name = c.get("newColumnRename") or col
        d = f"TRY_CAST({S} AS DATE)"
        if k == "FORMAT_DATES":  # Date([c], 'YYYY-MM-DD'); shortcut: solo el formato YYYYMMDD_DASH
            if c["format"] != "YYYYMMDD_DASH":
                raise Unsupported(f"FORMAT_DATES {c['format']}")
            e = f"strftime({d}, '%Y-%m-%d')"
        else:  # Date([c] + n); shortcut: solo dias y valor fijo; la fecha sale con el formato del SET (ver _qlik_text_format)
            if c["timeUnit"] != "DAY" or c["useWith"] != "VALUE":
                raise Unsupported(f"MODIFY_DATES {c['timeUnit']} {c['useWith']}")
            e = f"CAST({d} + {int(c['constantValue'])} * INTERVAL 1 DAY AS DATE)"
            ctx.converted_dates[name] = "date"
        return f"SELECT *, {e} AS {q(name)} FROM {v}" if c["shouldCreateNewColumn"] and name != col else f"SELECT * REPLACE ({e} AS {q(col)}) FROM {v}"
    cast = "DATE" if k == "CONVERT_TO_DATE" else "TIMESTAMP"
    # auto: solo los formatos que Qlik reconoce con el SET en-US (medido: '2026/09/09', '09-09-2026' y 'M/D/YYYY hh:mm' dan NULL)
    auto = ", ".join(f"CAST(try_strptime({S}, '{fmt}') AS {cast})" for fmt in _AUTO_DATES)
    e = f"coalesce({auto})" if c["format"] == "auto" else f"CAST(try_strptime({S}, {lit(_jfmt(c['datePattern']))}) AS {cast})"
    name = c["newColumnRename"] or col
    ctx.converted_dates[name] = "date" if k == "CONVERT_TO_DATE" else "timestamp"
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


def _qlik_text_format(ctx, view):
    """Formato de las celdas de un CSV como las escribe Qlik (medido en el tenant, ver 9 quater):
    un numero entero no lleva `.0`, y una fecha convertida usa el SET del script (en-US: M/D/YYYY y M/D/YYYY h:mm:ss TT).
    shortcut: solo en-US; otras configuraciones regionales conservan el formato ISO, y los decimales de segundo no se emulan."""
    swaps = []
    en = ctx.locale.lower().startswith("en")
    for name, typ in ((r[0], r[1].split("(")[0]) for r in ctx.con.execute(f"DESCRIBE SELECT * FROM {view}").fetchall()):
        c = q(name)
        if typ in ("DOUBLE", "FLOAT") and name in ctx.fixed_decimals:
            swaps.append(f"format('{{:.{ctx.fixed_decimals[name]}f}}', {c}) AS {c}")
        elif typ in ("DOUBLE", "FLOAT"):
            # Qlik escribe los numeros con 14 cifras significativas (medido: sqrt(2) -> 1.4142135623731) y sin `.0`;
            # shortcut: a partir de 1e14 se conserva el texto de DuckDB (no se midio como escribe Qlik esos valores)
            swaps.append(f"CASE WHEN abs({c}) < 1e14 THEN printf('%.14g', {c}) "
                         f"ELSE regexp_replace(CAST({c} AS VARCHAR), '[.]0$', '') END AS {c}")
        elif en and ctx.converted_dates.get(name) == "date" and typ == "DATE":
            swaps.append(f"strftime({c}, '%-m/%-d/%Y') AS {c}")
        elif en and ctx.converted_dates.get(name) == "timestamp" and typ.startswith("TIMESTAMP"):
            swaps.append(f"strftime({c}, '%-m/%-d/%Y %-I:%M:%S %p') AS {c}")
    return ctx.view(f"SELECT * REPLACE ({', '.join(swaps)}) FROM {view}") if swaps else view


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
    if fmt == "csv":
        # lo que mide el oraculo es la recarga del CSV: ahi Qlik unifica los textos que son el mismo numero o fecha. Las expresiones
        # del flujo ven el texto de cada fila (medido: CUT sobre '09/09/2026' conserva '09/09/2026'), por eso se unifica al escribir.
        cols = ctx.cols(view)
        types = {r[0]: r[1].split("(")[0] for r in ctx.con.execute(f"DESCRIBE SELECT * FROM {view}").fetchall()}
        view = _qlik_symbols(ctx, view, [c for c in cols if types.get(c) == "VARCHAR"], cols)
        view = _qlik_text_format(ctx, view)
    ctx.con.execute(f"COPY (SELECT * FROM {view}) TO {lit(dest)} ({opts})")
    rows = ctx.con.execute(f"SELECT count(*) FROM {view}").fetchone()[0]
    return {"target": n["label"], "dest": dest, "rows": rows, "emulated_qvd": emulated}


def run(d, data_dir, out_dir, connections=None, s3=None):
    ctx = Ctx(data_dir, out_dir, connections, s3)
    ctx.subflows = d.get("subflows", [])
    ctx.locale = d.get("collationLocale") or ""
    targets = run_graph(ctx, d["dataflow"]["graph"], d["sources"], {})
    return [_write(ctx, n, v) for n, v in targets.values()]
