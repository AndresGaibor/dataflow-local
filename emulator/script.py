"""Traductor del subconjunto de Qlik script que generan los Data Flows.

Cubre `LOAD [DISTINCT] campos [AS alias] FROM [lib://conexion/archivo.csv] (...)
[WHERE condiciones]`, con `STORE` y `DROP TABLE` ignorados (el emulador escribe sus
propias salidas). Cualquier otra construccion se marca como no traducible.
"""
import os
import re

import duckdb

_UNSUPPORTED = "no traducible"


def split_statements(text: str) -> list[str]:
    """Divide por `;` fuera de comillas y corchetes, descartando comentarios."""
    out, buf, depth = [], [], 0
    quote = ""
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            buf.append(ch)
            if ch == quote:
                if i + 1 < len(text) and text[i + 1] == quote:  # comilla escapada
                    buf.append(text[i + 1])
                    i += 1
                else:
                    quote = ""
        elif ch in "'\"":
            quote = ch
            buf.append(ch)
        elif ch == "[":
            depth += 1
            buf.append(ch)
        elif ch == "]":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == "/" and text.startswith("//", i) and not "".join(buf).strip():
            while i < len(text) and text[i] not in "\r\n":  # comentario al inicio de linea
                i += 1
            continue
        elif ch == ";" and depth == 0:
            out.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
        i += 1
    if "".join(buf).strip():
        out.append("".join(buf).strip())
    return [s for s in out if s]


def _split_top(s: str, sep: str = ",") -> list[str]:
    parts, buf, depth, quote = [], [], 0, ""
    for ch in s:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = ""
        elif ch in "'\"":
            quote = ch
            buf.append(ch)
        elif ch in "([":
            depth += 1
            buf.append(ch)
        elif ch in ")]":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if "".join(buf).strip():
        parts.append("".join(buf).strip())
    return parts


def _ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def _literal(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


_AGG = r"\b(?:sum|avg|count|min|max)\s*\("
_FUNCS = {"upper": "upper({0})", "lower": "lower({0})", "len": "length({0})", "trim": "trim({0})", "year": "year({0})", "month": "month({0})",
          # verificado en el tenant (2026-11-23): Sum de solo nulos o de texto da 0; Avg de solo nulos da NULL
          "isnull": "({0} IS NULL)", "sum": "COALESCE(SUM(TRY_CAST({0} AS DOUBLE)), 0)",
          "avg": "AVG(TRY_CAST({0} AS DOUBLE))", "min": "MIN({0})",
          "max": "MAX({0})", "count": "COUNT({0})"}


_FMT_TOKENS = [("YYYY", "%Y"), ("YY", "%y"), ("MM", "%m"), ("DD", "%d"),
               ("hh", "%H"), ("mm", "%M"), ("ss", "%S"), ("M", "%m"), ("D", "%d")]


# funciones que `translate` sabe resolver (las de `_FUNCS` mas las que tienen rama propia);
# es la fuente de verdad que usa scripts/script_inventory.py para medir cobertura
KNOWN_FUNCTIONS = {"IF", "COALESCE", "PICK", "DATE", "TIMESTAMP", "NULL", "MATCHREGEX", "MATCHREGEXI"}
# implementadas segun la ayuda oficial (docs/Scripting/), pendientes de medir en el tenant:
# el resto de funciones conocidas ya se midio contra Qlik (ver 9 quater del documento de hallazgos)
DOCUMENTED_ONLY = {"PICK", "DATE", "TIMESTAMP", "NULL", "MATCHREGEX", "MATCHREGEXI"}


def _strftime(literal: str) -> str | None:
    """`'YYYY-MM-DD'` (ya como literal SQL) -> `'%Y-%m-%d'`; None si hay tokens que no conocemos."""
    m = re.fullmatch(r"'([^']*)'", literal)
    if not m:
        return None
    out, i, pat = "", 0, m.group(1)
    while i < len(pat):
        for token, repl in _FMT_TOKENS:
            if pat.startswith(token, i):
                out += repl
                i += len(token)
                break
        else:
            if pat[i] in "-/:., ":
                out += pat[i]
                i += 1
            else:
                return None
    return f"'{out}'"


KNOWN_FUNCTIONS |= {name.upper() for name in _FUNCS}


def _call(e: str):
    """(nombre, argumentos) si `e` es una sola llamada `Nombre(...)`, si no None."""
    m = re.fullmatch(r"([A-Za-z_]+)\s*\((.*)\)", e, re.DOTALL)
    if not m:
        return None
    depth = 0
    for ch in m.group(2):  # shortcut: parentesis dentro de textos cuentan, mejorar si aparece un caso real
        depth += (ch == "(") - (ch == ")")
        if depth < 0:
            return None
    return m.group(1).lower(), m.group(2)


_IDENT = r"[A-Za-z_][A-Za-z0-9_]*"  # campo sin corchetes (Qlik lo permite y los scripts de un nodo `script` lo usan)
# de menor a mayor precedencia; cada nivel: operadores -> SQL
_BINARY = [({"OR": "OR"}), ({"AND": "AND"}), ({"<>": "<>", "<=": "<=", ">=": ">=", "=": "=", "<": "<", ">": ">"}),
           ({"&": "&"}), ({"+": "+", "-": "-"}), ({"*": "*", "/": "/"})]


def _split_top_op(e: str, ops) -> tuple[str, str, str] | None:
    """(izquierda, operador, derecha) por el ULTIMO operador de `ops` fuera de parentesis, corchetes y comillas
    (asociatividad por la izquierda); None si no hay. `+` y `-` unarios no cuentan como operador."""
    depth, quote, hit, i = 0, "", None, 0
    while i < len(e):
        ch = e[i]
        if quote:
            quote = "" if ch == quote else quote  # '' (comilla escapada) cierra y reabre
        elif ch in "'\"":
            quote = ch
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif depth == 0:
            for op in sorted(ops, key=len, reverse=True):
                if e[i:i + len(op)].upper() != op:
                    continue
                before, after = e[:i].rstrip(), e[i + len(op):i + len(op) + 1]
                if op.isalpha() and (re.match(r"\w", e[i - 1:i]) or re.match(r"\w", after)):
                    continue  # OR/AND dentro de otra palabra
                if op in "+-" and (not before or before[-1] in "(,+-*/&<>="):
                    continue  # signo unario
                hit = i, op
                i += len(op) - 1
                break
        i += 1
    return (e[:hit[0]], hit[1], e[hit[0] + len(hit[1]):]) if hit else None


def _wrapped(e: str) -> bool:
    """True si el primer parentesis de `e` es el que se cierra en el ultimo caracter: `(a + b)` si, `(a) + (b)` no."""
    if not (e.startswith("(") and e.endswith(")")):
        return False
    depth = 0
    for k, ch in enumerate(e):
        depth += (ch == "(") - (ch == ")")
        if depth == 0 and k < len(e) - 1:
            return False
    return True


def _expr_sql(e: str) -> str | None:
    """Expresion de Qlik a SQL de DuckDB; None si no se reconoce."""
    e = e.strip()
    if m := re.fullmatch(r"\[([^\]]+)\]", e):
        return _ident(m.group(1))
    if re.fullmatch(r"-?\d+(?:\.\d+)?|'(?:[^']|'')*'", e):
        return e
    if re.fullmatch(_IDENT, e):
        return _ident(e)
    for ops in _BINARY:
        if sp := _split_top_op(e, ops):
            left, op, right = sp
            a, c = _expr_sql(left), _expr_sql(right)
            if a is None or c is None:
                return None
            if op == "&":  # en Qlik & trata NULL como texto vacio
                return f"concat({a}, {c})"
            return f"({a} {op} {c})"
    if _wrapped(e):
        return _expr_sql(e[1:-1])
    if call := _call(e):
        name, args = call
        if name == "count" and (md := re.match(r"DISTINCT\s+(.*)$", args, re.IGNORECASE | re.DOTALL)):
            inner = _expr_sql(md.group(1))
            return f"COUNT(DISTINCT {inner})" if inner else None
        if name == "null" and not args.strip():
            return "NULL"  # NULL() de Qlik
        a = [_expr_sql(x) for x in _split_top(args)]
        if not a or None in a:
            return None
        if name == "if" and len(a) == 3:
            return f"(CASE WHEN {a[0]} THEN {a[1]} ELSE {a[2]} END)"
        if name == "coalesce":
            return f"coalesce({', '.join(a)})"
        if name == "pick" and len(a) >= 2:  # pick(n, e1, ..., eN): n-esima expresion
            n, values = a[0], a[1:]
            cases = " ".join(f"WHEN {n} = {i} THEN {v}" for i, v in enumerate(values[:-1], 1))
            return f"(CASE {cases} ELSE {values[-1]} END)"
        if name in ("date", "timestamp"):  # Date()/Timestamp() con el formato de Qlik
            cast = "DATE" if name == "date" else "TIMESTAMP"
            default = "'%Y-%m-%d'" if name == "date" else "'%Y-%m-%d %H:%M:%S'"
            if len(a) == 1:
                return f"strftime(CAST({a[0]} AS {cast}), {default})"
            fmt = _strftime(a[1]) if len(a) == 2 else None
            return f"strftime(CAST({a[0]} AS {cast}), {fmt})" if fmt else None
        if name in ("matchregexi", "matchregex") and len(a) == 2:  # el sufijo i = sin distinguir mayusculas
            flag = ", 'i'" if name == "matchregexi" else ""
            return f"regexp_matches(CAST({a[0]} AS VARCHAR), {a[1]}{flag})"
        t = _FUNCS.get(name)
        return t.format(*a) if t and len(a) == 1 else None
    if re.search(r"\b(?!AND\b|OR\b|NOT\b)[A-Za-z_]+\s*\(", e, re.IGNORECASE):
        return None  # llamada que no conocemos: no se deja pasar como SQL crudo
    return _where(e)


def _item(item: str):
    """Campo de un LOAD -> (sql, es_agregado, campo_origen | None); None si no se traduce."""
    s = item.strip()
    if s == "*":
        return "*", False, None
    m = re.fullmatch(rf"(.+?)\s+AS\s+(?:\[([^\]]+)\]|({_IDENT}))", s, re.IGNORECASE | re.DOTALL)
    expr, alias = (m.group(1), m.group(2) or m.group(3)) if m else (s, None)
    sql = _expr_sql(expr)
    src = re.fullmatch(rf"\[([^\]]+)\]|({_IDENT})", expr.strip())
    if sql is None or (alias is None and not src):
        return None
    return (f"{sql} AS {_ident(alias)}" if alias else sql), bool(re.search(_AGG, expr, re.IGNORECASE)), \
        ((src.group(1) or src.group(2)) if src else None)


def _where(cond: str) -> str | None:
    if not re.fullmatch(r"[\s\[\]A-Za-z0-9_ÁÉÍÓÚÜÑáéíóúüñ.,'\"<>=!()%*+-]+", cond):
        return None
    sql = re.sub(r"\[([^\]]+)\]", lambda m: _ident(m.group(1)), cond)
    sql = re.sub(r"\b(AND|OR|NOT)\b", lambda m: m.group(1).upper(), sql, flags=re.IGNORECASE)
    return sql


def _source_file(path: str) -> str | None:
    name = path.rsplit("/", 1)[-1]
    return name if name.lower().endswith(".csv") else None


def _reader(path: str) -> str | None:
    """read_csv con los textos recortados, como hace Qlik; None si no se puede leer."""
    if not os.path.exists(path):
        return None
    con = duckdb.connect()
    try:
        desc = con.execute(f"DESCRIBE SELECT * FROM read_csv({_literal(path)}, header=true)").fetchall()
    except duckdb.Error:
        return None
    finally:
        con.close()
    base = f"read_csv({_literal(path)}, header=true)"
    # como Qlik: textos recortados y celda vacia = texto vacio (cuenta como valor), no NULL
    trims = [f"coalesce(trim({_ident(r[0])}), '') AS {_ident(r[0])}" for r in desc if r[1].split("(")[0] == "VARCHAR"]
    return f"(SELECT * REPLACE ({', '.join(trims)}) FROM {base})" if trims else base


_HEAD = re.compile(
    r"(?:\[(?P<name>[^\]]+)\]:\s*)?(?:NOCONCATENATE\s+)?"
    r"(?:(?P<kind>LEFT|INNER|RIGHT|OUTER)?\s*JOIN\s*\(\s*\[(?P<jt>[^\]]+)\]\s*\)\s*)?"
    r"LOAD\s+(?P<distinct>DISTINCT\s+)?(?P<body>.*)$", re.IGNORECASE | re.DOTALL)
_JOINS = {None: "FULL", "LEFT": "LEFT", "INNER": "INNER", "RIGHT": "RIGHT", "OUTER": "FULL"}  # JOIN sin tipo = outer en Qlik


def _with(ctes: list[tuple[str, str]]) -> str:
    return "WITH " + ", ".join(f"{_ident(n)} AS ({q})" for n, q in ctes) + " " if ctes else ""


def _columns(ctes: list[tuple[str, str]], sql: str) -> list[str]:
    con = duckdb.connect()
    try:
        return [r[0] for r in con.execute(f"DESCRIBE {_with(ctes)}SELECT * FROM ({sql})").fetchall()]
    finally:
        con.close()


def _load(m: re.Match, cur: dict, data_dir: str, reasons: list[str]) -> str | None:
    """SELECT de un LOAD ... (FROM csv | RESIDENT) [WHERE] [GROUP BY]; None si no se traduce."""
    body = m.group("body")
    mx = re.search(r"\bFROM\s+\[([^\]]+)\]\s*(\([^)]*\))?|\bRESIDENT\s+\[([^\]]+)\]", body, re.IGNORECASE)
    if not mx:
        reasons.append("LOAD sin FROM ni RESIDENT")
        return None
    items = []
    for raw in _split_top(body[:mx.start()]):
        it = _item(raw)
        if it is None:
            reasons.append(f"campo no soportado: {raw[:40]}")
            return None
        items.append(it)
    if mx.group(3):
        if mx.group(3) not in cur:
            reasons.append(f"RESIDENT de una tabla desconocida: {mx.group(3)}")
            return None
        source = _ident(cur[mx.group(3)])
    else:
        name = _source_file(mx.group(1))
        if name is None:
            reasons.append(f"origen no soportado (solo .csv): {mx.group(1)}")
            return None
        source = _reader(os.path.join(data_dir, name))
        if source is None:
            reasons.append(f"no se pudo leer el CSV: {name}")
            return None
    rest = body[mx.end():].strip()
    group = None
    if mg := re.search(r"\bGROUP\s+BY\b(.*)$", rest, re.IGNORECASE | re.DOTALL):
        group, rest = [k.strip() for k in _split_top(mg.group(1).strip())], rest[:mg.start()].strip()
    where = ""
    if mw := re.fullmatch(r"WHERE\b(.*)", rest, re.IGNORECASE | re.DOTALL):
        cond = _where(mw.group(1).strip())
        if cond is None:
            reasons.append(f"WHERE no soportado: {mw.group(1).strip()[:40]}")
            return None
        where = f" WHERE {cond}"
    elif rest:
        reasons.append(f"clausula no soportada: {rest[:40]}")
        return None
    tail = ""
    has_agg = any(a for _, a, _ in items)
    if group is not None or has_agg:
        keys = [mk.group(1) for k in (group or []) if (mk := re.fullmatch(r"\[([^\]]+)\]", k))]
        if group is None or len(keys) != len(group):
            reasons.append("agregacion sin GROUP BY de campos simples")
            return None
        free = [src or sql for sql, agg, src in items if not agg and src not in keys]
        if free:
            reasons.append(f"campo fuera del GROUP BY: {free[0]}")
            return None
        tail = " GROUP BY " + ", ".join(_ident(k) for k in keys)
    return (f"SELECT {'DISTINCT ' if m.group('distinct') else ''}{', '.join(i[0] for i in items)} "
            f"FROM {source}{where}{tail}")


def translate(text: str, data_dir: str) -> tuple[str | None, list[str]]:
    """Devuelve (SQL, motivos). SQL es None si el script no es traducible.

    Cada sentencia con nombre es una tabla (un CTE); `JOIN([T])` la reemplaza por el join;
    el resultado es la tabla del STORE o, sin STORE, la ultima. shortcut: un solo destino y sin
    autoconcatenacion de LOADs con los mismos campos, mejorar si aparecen flujos que los usen.
    """
    ctes: list[tuple[str, str]] = []  # (id del CTE, SELECT)
    cur: dict[str, str] = {}  # nombre de tabla -> id del CTE vigente
    stored: list[str] = []
    reasons: list[str] = []
    last = ""
    for st in split_statements(text):
        st = re.sub(r"(?m)^\s*//.*$", "", st).strip()
        mh = re.match(r"[A-Za-z_]+", st)
        head = mh.group(0).upper() if mh else ""
        if head == "THROW":
            reasons.append("el flujo se declara invalido (throw)")
            continue
        if ms := re.match(r"STORE\s+\[([^\]]+)\]", st, re.IGNORECASE):
            stored.append(ms.group(1))
            continue
        if head in ("SET", "TRACE", "DROP", "NOCONCATENATE"):
            continue
        m = _HEAD.match(st)
        if not m:
            reasons.append(f"sentencia no soportada: {st.splitlines()[0][:60]}")
            continue
        sel = _load(m, cur, data_dir, reasons)
        if sel is None:
            continue
        if m.group("jt"):
            t = m.group("jt")
            if t not in cur:
                reasons.append(f"JOIN sobre una tabla desconocida: {t}")
                continue
            try:
                right = _columns(ctes, sel)
                common = [c for c in _columns(ctes, f"SELECT * FROM {_ident(cur[t])}") if c in right]
            except duckdb.Error as e:  # campo inexistente, tipo incompatible, CSV ilegible
                reasons.append(f"no se pudo resolver los campos del join sobre {t}: {str(e).splitlines()[0][:80]}")
                continue
            if not common:
                reasons.append(f"join sin campos en comun: {t}")
                continue
            sel = (f"SELECT * FROM {_ident(cur[t])} {_JOINS[m.group('kind') and m.group('kind').upper()]} JOIN "
                   f"({sel}) AS j USING ({', '.join(_ident(c) for c in common)})")
            name = t
        else:
            name = m.group("name") or f"_load{len(ctes) + 1}"
        cte = f"{name}~{len(ctes)}"
        ctes.append((cte, sel))
        cur[name] = cte
        last = name  # el orden del diccionario no sirve: un JOIN reasigna una clave existente
    if reasons:
        return None, reasons
    if not ctes:
        return None, ["el script no carga ninguna tabla"]
    dests = set(stored) or {last}
    if len(dests) != 1 or next(iter(dests)) not in cur:
        return None, [f"el traductor produce un solo SQL; destinos: {', '.join(sorted(dests))}"]
    return f"{_with(ctes)}SELECT * FROM {_ident(cur[next(iter(dests))])}", []


def run(sql: str):
    con = duckdb.connect()
    try:
        return con.execute(sql).fetchall(), [d[0] for d in con.execute(f"DESCRIBE ({sql})").fetchall()]
    finally:
        con.close()


def store_stem(text: str) -> str | None:
    """Nombre (sin extension) del primer destino de un STORE, o None si no hay."""
    m = re.search(r"\bSTORE\s+\[[^\]]+\]\s+INTO\s+\[([^\]]+)\]", text, re.IGNORECASE)
    return os.path.splitext(m.group(1).rsplit("/", 1)[-1])[0] if m else None


def write_csv(sql: str, path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    con = duckdb.connect()
    try:
        con.execute(f"COPY ({sql}) TO {_literal(path)} (FORMAT csv, HEADER)")
    finally:
        con.close()
