"""Comparador: huellas del emulador (archivos locales) frente a las del tenant (oráculo).

TableFp = {"rows": int, "columns": {col: {"count": int, "distinct": int, "sum": float | None}}}
"""
import os

import duckdb

q = lambda c: '"' + str(c).replace('"', '""') + '"'
lit = lambda s: "'" + str(s).replace("'", "''") + "'"
NUMERIC = {"TINYINT", "SMALLINT", "INTEGER", "BIGINT", "HUGEINT", "UTINYINT", "USMALLINT", "UINTEGER",
           "UBIGINT", "UHUGEINT", "FLOAT", "REAL", "DOUBLE", "DECIMAL"}


def stem_of(dest: str) -> str:
    name = os.path.basename(dest).removesuffix(".parquet").removesuffix(".qvd")
    return os.path.splitext(name)[0]


def _reader(path: str) -> str:
    if path.endswith(".csv"):
        return f"read_csv({lit(path)}, header=true)"
    if path.endswith(".parquet"):
        return f"read_parquet({lit(path)})"
    raise ValueError(f"formato no soportado para la huella: {path}")


def local_fingerprint(dest: str) -> dict:
    return fingerprint_of(_reader(dest))


def fingerprint_of(src: str, con=None) -> dict:
    """Huella de una relacion SQL (vista o lectura de archivo), medida como la ve el oraculo del tenant: este vuelve a
    cargar el archivo escrito (oracle._READBACK), y en Qlik un archivo no tiene NULL; todo NULL del emulador (join sin
    pareja, conversion fallida, celda vacia) es una celda vacia que cuenta como valor."""
    own = con is None
    con = con or duckdb.connect()
    try:
        desc = con.execute(f"DESCRIBE SELECT * FROM {src}").fetchall()
        exprs = ["count(*)"]
        for name, typ, *_ in desc:
            c = q(name)
            # como Qlik al cargar el archivo escrito: no hay NULL, una celda vacia es un valor ('') que cuenta y es distinto
            exprs += ["count(*)", f"count(DISTINCT {c}) + CASE WHEN count(*) > count({c}) THEN 1 ELSE 0 END",
                      f"sum(CAST({c} AS DOUBLE))" if typ.split("(")[0] in NUMERIC else "NULL"]
        row = con.execute(f"SELECT {', '.join(exprs)} FROM {src}").fetchone()
    finally:
        if own:
            con.close()
    columns = {}
    for i, (name, _, *_) in enumerate(desc):
        count, distinct, total = row[1 + 3 * i: 4 + 3 * i]
        columns[name] = {"count": count, "distinct": distinct,
                         "sum": None if total is None else float(total)}
    return {"rows": row[0], "columns": columns}


def local_fingerprints(dests: list[str]) -> dict[str, dict]:
    stems = [stem_of(d) for d in dests]
    for s in stems:
        if stems.count(s) > 1:
            raise ValueError(f"destinos con el mismo nombre: {s}")
    return {stem_of(d): local_fingerprint(d) for d in dests}


def _close(a, b, rel_tol: float) -> bool:
    if a is None or b is None:
        return a is None and b is None
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def compare(local: dict[str, dict], remote: dict[str, dict], rel_tol: float = 1e-9) -> list[str]:
    msgs = [f"tabla '{t}' solo en el emulador" for t in local.keys() - remote.keys()]
    msgs += [f"tabla '{t}' solo en el tenant" for t in remote.keys() - local.keys()]
    for t in sorted(local.keys() & remote.keys()):
        a, b = local[t], remote[t]
        if a["rows"] != b["rows"]:
            msgs.append(f"{t}: filas {a['rows']} (emulador) != {b['rows']} (tenant)")
        lc, rc = a["columns"], b["columns"]
        msgs += [f"{t}.{c}: columna solo en el emulador" for c in lc.keys() - rc.keys()]
        msgs += [f"{t}.{c}: columna solo en el tenant" for c in rc.keys() - lc.keys()]
        for c in sorted(lc.keys() & rc.keys()):
            for k in ("count", "distinct", "sum"):
                x, y = lc[c][k], rc[c][k]
                if k == "sum" and (x is None or y is None):
                    continue  # Qlik suma fechas como numeros: si un lado no tiene suma, no se compara
                ok = _close(x, y, rel_tol) if k == "sum" else x == y
                if not ok:
                    msgs.append(f"{t}.{c}: {k} {x} (emulador) != {y} (tenant)")
    return sorted(msgs)
