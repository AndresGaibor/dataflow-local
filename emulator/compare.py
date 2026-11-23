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


def local_fingerprint(dest: str, head: int = 0) -> dict:
    """Huella de un archivo. Con `head` agrega por columna el texto de las primeras filas ('|' como separador, celda
    vacia incluida), para comparar el orden y el formato de lo escrito; solo para CSV."""
    fp = fingerprint_of(_reader(dest))
    if head and dest.endswith(".csv"):
        cols = list(fp["columns"])
        con = duckdb.connect()
        try:
            aggs = ", ".join("string_agg(coalesce(" + q(c) + ", ''), '|')" for c in cols)
            row = con.execute(f"SELECT {aggs} FROM (SELECT * FROM read_csv({lit(dest)}, header=true, all_varchar=true) "
                              f"LIMIT {int(head)})").fetchone()
        finally:
            con.close()
        for c, h in zip(cols, row):
            fp["columns"][c]["head"] = h or ""
    return fp


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


def local_fingerprints(dests: list[str], head: int = 0) -> dict[str, dict]:
    stems = [stem_of(d) for d in dests]
    for s in stems:
        if stems.count(s) > 1:
            raise ValueError(f"destinos con el mismo nombre: {s}")
    return {stem_of(d): local_fingerprint(d, head) for d in dests}


def _close(a, b, rel_tol: float) -> bool:
    if a is None or b is None:
        return a is None and b is None
    return abs(a - b) <= rel_tol * max(abs(a), abs(b), 1.0)


def compare(local: dict[str, dict], remote: dict[str, dict], rel_tol: float = 1e-9, skip_head=frozenset()) -> list[str]:
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
            lh, rh = lc[c].get("head"), rc[c].get("head")
            if lh is not None and rh is not None and c not in skip_head and lh != rh:  # `skip_head`: p. ej. HASH_DATA
                msgs.append(f"{t}.{c}: primeras filas {lh[:60]!r} (emulador) != {rh[:60]!r} (tenant)")
    return sorted(msgs)
