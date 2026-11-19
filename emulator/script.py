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


def _field(item: str) -> str | None:
    m = re.fullmatch(r"\[([^\]]+)\](?:\s+AS\s+\[([^\]]+)\])?", item.strip(), re.IGNORECASE)
    if m:
        return f"{_ident(m.group(1))} AS {_ident(m.group(2) or m.group(1))}"
    m = re.fullmatch(r"\*", item.strip())
    return "*" if m else None


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
    trims = [f"trim({_ident(r[0])}) AS {_ident(r[0])}" for r in desc if r[1].split("(")[0] == "VARCHAR"]
    return f"(SELECT * REPLACE ({', '.join(trims)}) FROM {base})" if trims else base


def translate(text: str, data_dir: str) -> tuple[str | None, list[str]]:
    """Devuelve (SQL, motivos). SQL es None si el script no es traducible."""
    loads, reasons = [], []
    for st in split_statements(text):
        mh = re.match(r"[A-Za-z_]+", st)
        head = mh.group(0).upper() if mh else ""
        if head == "THROW":
            reasons.append("el flujo se declara invalido (throw)")
            continue
        if head in ("SET", "TRACE", "STORE", "DROP", "NOCONCATENATE"):
            continue
        m = re.match(r"(?:\[[^\]]+\]:\s*)?(?:NOCONCATENATE\s+)?LOAD\s+(DISTINCT\s+)?(.*)$",
                     st, re.IGNORECASE | re.DOTALL)
        if not m:
            reasons.append(f"sentencia no soportada: {st.splitlines()[0][:60]}")
            continue
        body = m.group(2)
        mx = re.search(r"\bFROM\s+\[([^\]]+)\]\s*(\([^)]*\))?", body, re.IGNORECASE)
        if not mx:
            reasons.append("LOAD sin FROM")
            continue
        fields_sql = []
        for item in _split_top(body[:mx.start()]):
            f = _field(item)
            if f is None:
                reasons.append(f"campo no soportado: {item[:40]}")
                break
            fields_sql.append(f)
        name = _source_file(mx.group(1))
        if name is None:
            reasons.append(f"origen no soportado (solo .csv): {mx.group(1)}")
        rest = body[mx.end():].strip()
        where = ""
        mw = re.search(r"\bWHERE\b(.*)$", rest, re.IGNORECASE | re.DOTALL)
        if mw:
            cond = _where(mw.group(1).strip())
            if cond is None:
                reasons.append(f"WHERE no soportado: {mw.group(1).strip()[:40]}")
            where = f" WHERE {cond}" if cond else ""
        elif rest:
            reasons.append(f"clausula no soportada: {rest[:40]}")
        if name and len(fields_sql) and not reasons:
            reader = _reader(os.path.join(data_dir, name))
            if reader is None:
                reasons.append(f"no se pudo leer el CSV: {name}")
            else:
                loads.append(f"SELECT {'DISTINCT ' if m.group(1) else ''}{', '.join(fields_sql)} "
                             f"FROM {reader}{where}")
    if reasons:
        return None, reasons
    if len(loads) != 1:
        return None, [f"{len(loads)} LOAD ejecutables; el traductor cubre uno por script"]
    return loads[0], []


def run(sql: str):
    con = duckdb.connect()
    try:
        return con.execute(sql).fetchall(), [d[0] for d in con.execute(f"DESCRIBE ({sql})").fetchall()]
    finally:
        con.close()
