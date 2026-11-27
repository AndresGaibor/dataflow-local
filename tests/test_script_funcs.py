"""Funciones de Qlik que el traductor cubria a medias: Date, Timestamp, Null, Pick y MatchRegExi.

La definicion de cada una esta en `docs/Scripting/` (espejo local de la ayuda de Qlik).
"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import script  # noqa: E402

FROM = " FROM [lib://s/in.csv] (txt, utf8, embedded labels, delimiter is ',');\n"
DATA = tempfile.mkdtemp(prefix="funcs_")
with open(os.path.join(DATA, "in.csv"), "w", encoding="utf-8") as _f:
    _f.write("d,t,n\n2026-09-09,abc,2\n2026-10-01,ABC,1\n")


def sql_of(expr: str) -> str:
    """Traduce una sola expresion dentro de un LOAD y devuelve el SQL."""
    qvs = f"[out]:\nLOAD {expr} AS x{FROM}STORE [out] INTO [lib://s/out.csv] (txt);\n"
    sql, reasons = script.translate(qvs, DATA)
    assert sql, reasons
    return sql


def test_date_without_format_is_iso():
    assert "strftime(CAST(\"d\" AS DATE), '%Y-%m-%d')" in sql_of("Date([d])")


def test_date_with_qlik_format_is_translated():
    assert "'%Y-%m'" in sql_of("Date([d], 'YYYY-MM')")


def test_date_with_an_unknown_format_is_not_translated():
    sql, reasons = script.translate(f"[out]:\nLOAD Date([d], 'QQQQ') AS x{FROM}", DATA)
    assert sql is None and reasons


def test_timestamp_keeps_the_time():
    assert "strftime(CAST(\"d\" AS TIMESTAMP), '%Y-%m-%d %H:%M:%S')" in sql_of("Timestamp([d])")


def test_null_is_null():
    assert "NULL" in sql_of("Null()")


def test_pick_returns_the_nth_expression():
    sql = sql_of("Pick(2, 'A', 'B', 'C')")
    assert sql.count("WHEN 2 = ") == 2  # n=2: dos ramas, la ultima no se evalua
    assert "'B'" in sql


def test_pick_of_a_field_index_uses_case():
    sql = sql_of("Pick([n], 'A', 'B')")
    assert 'CASE WHEN "n" = 1 THEN \'A\'' in sql


def test_matchregexi_is_case_insensitive():
    sql = sql_of("MatchRegExi([t], '^a')")
    assert "regexp_matches" in sql and "'i'" in sql


def test_matchregex_is_case_sensitive():
    sql = sql_of("MatchRegEx([t], '^a')")
    assert "regexp_matches" in sql and "'i'" not in sql


def test_the_translated_sql_runs_and_gives_the_values_of_qlik():
    """No basta con que compile: se ejecuta en DuckDB y se miran los valores."""
    import duckdb

    qvs = (f"[out]:\nLOAD Date([d]) AS dia, Timestamp([d]) AS ts, Pick([n], 'uno', 'dos') AS p, "
           f"MatchRegExi([t], '^a') AS m, Null() AS nada{FROM}"
           "STORE [out] INTO [lib://s/out.csv] (txt);\n")
    sql, reasons = script.translate(qvs, DATA)
    assert sql, reasons
    rows = duckdb.sql(sql).fetchall()
    assert rows[0][0] == "2026-09-09"
    assert rows[0][1] == "2026-09-09 00:00:00"
    assert rows[0][2] == "dos"      # n = 2
    assert rows[0][3] is True       # MatchRegExi no distingue mayusculas
    assert rows[0][4] is None       # Null()


def test_date_of_floor_is_the_date_part():
    """`Date(Floor([c]))` es lo que genera Qlik al convertir un campo."""
    sql = sql_of("Date(Floor([d]))")
    # reconoce el formato del texto (M/D/YYYY ademas de ISO), como Qlik
    assert "try_strptime(\"d\", '%m/%d/%Y')" in sql
    assert "floor(" not in sql


def test_floor_alone_rounds_numbers():
    assert "floor(TRY_CAST(\"n\" AS DOUBLE))" in sql_of("Floor([n])")
