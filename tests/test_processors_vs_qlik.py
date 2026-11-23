"""Comportamientos del emulador medidos contra el tenant (2026-11-23, ver docs/banco-de-pruebas/01-hallazgos-api-qlik.md, 9 quater)."""
import os
import sys

import duckdb
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import runner  # noqa: E402
from emulator.builder import Flow  # noqa: E402


def run_one(tmp_path, csv_text, fields, ctype, cfg):
    """clientes.csv -> un processor -> destino; devuelve (columnas, filas) del archivo de salida."""
    (tmp_path / "t.csv").write_text(csv_text, encoding="utf-8")
    f = Flow("t")
    src = f.dataset("t", "t.csv", fields)
    p = f.proc(ctype, "p", cfg)
    f.chain(src, p, f.target("Destino", "salida"))
    (t,) = runner.run(f.dump(), str(tmp_path), str(tmp_path / "out"))
    con = duckdb.connect()
    cur = con.execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    cols = [d[0] for d in cur.description]
    return cols, cur.fetchall()


def test_empty_csv_cells_are_empty_text_not_null_like_in_qlik(tmp_path):
    # Qlik cuenta la celda vacia de un CSV como valor (Count = 500 en clientes.csv); DuckDB la leia como NULL (488)
    from emulator import script
    (tmp_path / "t.csv").write_text("id,t\n1,\n2,x\n3, \n", encoding="utf-8")
    sql, reasons = script.translate("LOAD [id], [t] FROM [lib://c/t.csv] (txt);", str(tmp_path))
    assert reasons == []
    rows, _ = script.run(f"SELECT count(t), count(DISTINCT t) FROM ({sql})")
    assert rows == [(3, 2)]  # '', 'x' y '' (tras recortar) son 3 valores y 2 distintos
    # el CSV de salida no distingue '' de NULL: se mide con COUNT por id (cuenta los valores no nulos)
    cols, out = run_one(tmp_path, "id,t\n1,\n2,x\n3, \n", ["id", "t"], "aggregate",
                        {"groupBy": [{"fieldPath": "id"}],
                         "operations": [{"operation": "COUNT", "fieldPaths": ["t"], "delimiter": ",", "outputFieldPath": "n"}]})
    assert {r[cols.index("id")]: r[cols.index("n")] for r in out} == {"1": "1", "2": "1", "3": "1"}


def test_fill_with_value_replaces_every_cell(tmp_path):
    # "Fill cells with value" rellena TODAS las celdas (script de Qlik: 'X' AS [t]); vaciar solo las vacias es REPLACE_WITH_VALUE
    cfg = {"type": "FILL_WITH_VALUE", "fillWithValueConfiguration": {"columnsToProcess": ["t"], "defaultValue": "X", "mode": "WITH_VALUE"}}
    cols, out = run_one(tmp_path, "id,t\n1,\n2,a\n3,b\n", ["id", "t"], "data-cleansing", cfg)
    assert sorted({r[cols.index("t")] for r in out}) == ["X"]


def test_split_text_names_and_last_part_keeps_the_rest(tmp_path):
    # Qlik: SubField(c, ' ', 1) AS [c-split_1] y Mid(c, Index(c, ' ', 1) + 1) AS [c-split_2] ('' si no hay separador)
    cfg = {"type": "SPLIT_TEXT_IN_PARTS", "splitTextInPartsConfiguration": {
        "columnsToProcess": ["n"], "customSeparatorValue": "", "parts": 2, "separator": "SPACE"}}
    cols, out = run_one(tmp_path, "id,n\n1,Garcia Perez Lopez\n2,Solo\n", ["id", "n"], "split-field", cfg)
    assert "n-split_1" in cols and "n-split_2" in cols and "n_1" not in cols
    got = {r[0]: (r[cols.index("n-split_1")], r[cols.index("n-split_2")]) for r in out}
    assert got["1"] == ("Garcia", "Perez Lopez")
    assert got["2"][0] == "Solo" and got["2"][1] in ("", None)  # el CSV no distingue '' de NULL


@pytest.mark.parametrize("rename,expected", [("f_", ["f__day", "f__year"]), ("", ["d_day", "d_year"])])
def test_extract_date_parts_prefix_is_new_column_rename_or_the_column(tmp_path, rename, expected):
    cfg = {"type": "EXTRACT_DATE_PARTS", "extractDateTokensConfiguration": {
        "columnsToProcess": ["d"], "datePattern": "YYYY-MM-DD", "day": True, "year": True,
        "shouldCreateNewColumn": True, "newColumnRename": rename}}
    cols, _ = run_one(tmp_path, "id,d\n1,2024-03-05\n", ["id", "d"], "date", cfg)
    assert sorted(c for c in cols if c not in ("id", "d")) == sorted(expected)


def test_runner_fingerprint_counts_empty_text_even_though_the_csv_file_cannot(tmp_path):
    from emulator import compare
    (tmp_path / "t.csv").write_text("id,t\n1,\n2,x\n", encoding="utf-8")
    f = Flow("t")
    src = f.dataset("t", "t.csv", ["id", "t"])
    p = f.proc("sort", "p", {"sortFields": [{"fieldPath": "id", "sortOrder": "ASCENDING"}]})
    f.chain(src, p, f.target("Destino", "salida"))
    (t,) = runner.run(f.dump(), str(tmp_path), str(tmp_path / "out"))
    assert t["fingerprint"]["columns"]["t"]["count"] == 2  # '' y 'x'
    assert compare.local_fingerprint(t["dest"])["columns"]["t"]["count"] == 1  # el archivo leido si pierde el vacio
    assert compare.target_fingerprints([t])["salida"] == t["fingerprint"]
