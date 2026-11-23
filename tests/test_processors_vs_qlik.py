"""Comportamientos del emulador medidos contra el tenant (2026-11-23, ver docs/banco-de-pruebas/01-hallazgos-api-qlik.md, 9 quater)."""
import os
import sys

import duckdb
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import runner  # noqa: E402
from emulator.builder import Flow  # noqa: E402


def run_one(tmp_path, csv_text, fields, ctype, cfg, locale="en-US"):
    """clientes.csv -> un processor -> destino; devuelve (columnas, filas) del archivo de salida."""
    (tmp_path / "t.csv").write_text(csv_text, encoding="utf-8")
    f = Flow("t", locale=locale)
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


def test_fingerprint_sees_a_written_csv_the_way_qlik_reloads_it():
    # el oraculo del tenant vuelve a cargar el CSV escrito: ahi no hay NULL, una celda vacia es un valor ('') que cuenta
    # (join izquierdo sin pareja, CONVERT_TO_NUMBER de texto no numerico... todo NULL del emulador queda como celda vacia)
    import tempfile
    from emulator import compare
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "t.csv")
        open(path, "w", encoding="utf-8").write("id,t,n\n1,,5\n2,x,\n3,x,7\n")
        fp = compare.local_fingerprint(path)
    assert fp["rows"] == 3
    assert fp["columns"]["t"] == {"count": 3, "distinct": 2, "sum": None}  # '', 'x'
    assert fp["columns"]["n"] == {"count": 3, "distinct": 3, "sum": 12.0}  # 5, 7 y vacio; la suma ignora el vacio


@pytest.mark.parametrize("op,val,method,new,expected", [
    # script de Qlik medido en el tenant (2026-11-23); texto de prueba: 'Guayaquil'
    ("STARTS_WITH", "Gua", "REPLACE_CELL_WITH_VALUE", "X", "X"),             # IF(Match(Left(c, Len(v)), v), rep, c)
    ("STARTS_WITH", "Gua", "REPLACE_MATCHING_WITH_VALUE", "X", "Xyaquil"),
    ("ENDS_WITH", "quil", "REPLACE_CELL_WITH_VALUE", "X", "X"),              # IF(Match(Right(c, Len(v)), v), rep, c)
    ("ENDS_WITH", "quil", "REPLACE_MATCHING_WITH_VALUE", "X", "GuayaX"),     # Left(c, Len(c) - Len(v)) & rep
    ("CONTAINS", "ya", "REPLACE_CELL_WITH_VALUE", "X", "X"),                 # IF(Index(c, v), rep, c)
    ("CONTAINS", "ya", "REPLACE_MATCHING_WITH_VALUE", "X", "GuaXquil"),
    ("EQUALS", "Guayaquil", "REPLACE_CELL_WITH_VALUE", "X", "X"),
    ("EQUALS", "Guayaquil", "REPLACE_MATCHING_WITH_VALUE", "X", "X"),        # IF(Match(c, v), rep, c)
    ("EQUALS", "Quito", "REPLACE_CELL_WITH_VALUE", "X", "Guayaquil"),
])
def test_replace_on_value_matrix(tmp_path, op, val, method, new, expected):
    cfg = {"type": "REPLACE_ON_VALUE", "replaceOnValueConfiguration": {
        "cellValue": {"operator": op, "value": val}, "columnsToProcess": ["c"], "newColumnName": "",
        "replaceMethod": method, "replaceValue": new, "shouldCreateNewColumn": False}}
    cols, out = run_one(tmp_path, "id,c\n1,Guayaquil\n", ["id", "c"], "strings", cfg)
    assert out[0][cols.index("c")] == expected


# --- orden y formato de lo que se escribe (sonda fila a fila contra el tenant, 2026-11-23) --------------------

def test_numbers_are_written_like_qlik_without_trailing_dot_zero(tmp_path):
    cfg = {"type": "CONVERT_TO_NUMBER", "convertToNumberConfiguration": {
        "columnsToProcess": ["n"], "decimalSeparator": ".", "thousandSeparator": ",", "newColumnName": "m", "shouldCreateNewColumn": True}}
    cols, out = run_one(tmp_path, "id,n\n1,5\n2,7.5\n3,-4\n", ["id", "n"], "numbers", cfg)
    assert [r[cols.index("m")] for r in out] == ["5", "7.5", "-4"]  # antes: 5.0, 7.5, -4.0


def test_window_keeps_the_original_row_order(tmp_path):
    # Qlik devuelve las filas en el orden de origen con la columna de la ventana; no las reordena por la ventana
    cfg = {"operationConfiguration": {"operationType": "RANK", "operationFields": [], "outputFieldName": "rk", "delimiter": ","},
           "partitionByConfiguration": {"partitionByFieldList": []}, "sortingConfiguration": {"sortBy": "v", "sortOrder": "DESCENDING"},
           "rangeConfiguration": {"windowStartType": "UNLIMITED", "windowEndType": "UNLIMITED", "windowStartValue": 1, "windowEndValue": 1}}
    cols, out = run_one(tmp_path, "id,v\n1,10\n2,30\n3,20\n", ["id", "v"], "window", cfg)
    assert [r[cols.index("id")] for r in out] == ["1", "2", "3"]
    assert [r[cols.index("rk")] for r in out] == ["3", "1", "2"]


def test_aggregate_returns_groups_in_order_of_first_appearance(tmp_path):
    cfg = {"groupBy": [{"fieldPath": "s"}], "operations": [{"operation": "COUNT", "fieldPaths": ["id"], "delimiter": ",", "outputFieldPath": "n"}]}
    cols, out = run_one(tmp_path, "id,s\n1,B\n2,A\n3,B\n4,C\n5,A\n", ["id", "s"], "aggregate", cfg)
    assert [r[cols.index("s")] for r in out] == ["B", "A", "C"]


@pytest.mark.parametrize("ctype,key,expected", [
    ("CONVERT_TO_DATE", "convertToDateConfiguration", "5/24/2019"),                       # DateFormat='M/D/YYYY'
    ("CONVERT_TO_TIMESTAMP", "convertToTimestampConfiguration", "5/24/2019 12:00:00 AM"),  # TimestampFormat='M/D/YYYY h:mm:ss TT'
])
def test_converted_dates_use_the_en_us_script_format(tmp_path, ctype, key, expected):
    cfg = {"type": ctype, key: {"columnsToProcess": ["d"], "datePattern": "YYYY-MM-DD", "format": "custom",
                                "newColumnRename": "f", "shouldCreateNewColumn": True}}
    cols, out = run_one(tmp_path, "id,d\n1,2019-05-24\n", ["id", "d"], "date", cfg)
    assert out[0][cols.index("f")] == expected
    assert out[0][cols.index("d")] == "2019-05-24"  # una fecha que solo pasa de largo conserva su texto original


def test_converted_dates_keep_iso_for_a_locale_other_than_en(tmp_path):
    # el formato sale de los SET del script segun la configuracion regional del flujo; solo se midio en-US
    cfg = {"type": "CONVERT_TO_DATE", "convertToDateConfiguration": {"columnsToProcess": ["d"], "datePattern": "YYYY-MM-DD",
           "format": "custom", "newColumnRename": "f", "shouldCreateNewColumn": True}}
    cols, out = run_one(tmp_path, "id,d\n1,2019-05-24\n", ["id", "d"], "date", cfg, locale="es-ES")
    assert out[0][cols.index("f")] == "2019-05-24"
