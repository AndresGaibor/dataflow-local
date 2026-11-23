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


def run_join(tmp_path, kind):
    """a.csv (ids 1,2,3,4) y b.csv (ids 3,1,9) unidos por id; devuelve (columnas, filas) del archivo de salida."""
    from emulator.builder import join
    (tmp_path / "a.csv").write_text("id,v\n1,a1\n2,a2\n3,a3\n4,a4\n", encoding="utf-8")
    (tmp_path / "b.csv").write_text("id,w\n3,b3\n1,b1\n9,b9\n", encoding="utf-8")
    f = Flow("t")
    a, b = f.dataset("a", "a.csv", ["id", "v"]), f.dataset("b", "b.csv", ["id", "w"])
    j = f.proc("join", "j", join(kind, ("id", "id")))
    f.link(a, j)
    f.link(b, j)
    f.chain(j, f.target("Destino", "salida"))
    (t,) = runner.run(f.dump(), str(tmp_path), str(tmp_path / "out"))
    cur = duckdb.connect().execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    return [d[0] for d in cur.description], cur.fetchall()


@pytest.mark.parametrize("kind,ids", [
    ("INNER_JOIN", ["1", "3"]),                       # filas de la izquierda, en su orden
    ("LEFT_OUTER_JOIN", ["1", "2", "3", "4"]),
    ("FULL_OUTER_JOIN", ["1", "2", "3", "4", "9"]),   # izquierda en su orden y despues las que solo estan a la derecha
])
def test_join_output_order_is_deterministic_left_then_right_only(tmp_path, kind, ids):
    # orden propio del emulador (reproducible); el de Qlik con claves repetidas no se pudo deducir, ver 9 quater
    cols, out = run_join(tmp_path, kind)
    assert [r[cols.index("id")] for r in out] == ids


def test_full_join_takes_the_key_from_the_right_side_for_right_only_rows(tmp_path):
    cols, out = run_join(tmp_path, "FULL_OUTER_JOIN")
    last = out[-1]
    assert last[cols.index("id")] == "9" and last[cols.index("w")] == "b9" and last[cols.index("v")] in ("", None)


def run_chain(tmp_path, csv_text, fields, steps):
    """t.csv -> varios processors en serie -> destino; devuelve (columnas, filas) del archivo de salida."""
    (tmp_path / "t.csv").write_text(csv_text, encoding="utf-8")
    f = Flow("t")
    src = f.dataset("t", "t.csv", fields)
    nodes = [f.proc(t, f"p{i}", c) for i, (t, c) in enumerate(steps)]
    f.chain(src, *nodes, f.target("Destino", "salida"))
    (t,) = runner.run(f.dump(), str(tmp_path), str(tmp_path / "out"))
    cur = duckdb.connect().execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    return [d[0] for d in cur.description], cur.fetchall()


def test_split_leaves_null_not_empty_text_when_the_part_does_not_exist(tmp_path):
    # en Qlik, SubField fuera de rango y Mid(c, '') dan NULL: un paso posterior ve NULL (Count = 0; reemplazar "vacios" no lo toca)
    split = ["split-field", {"type": "SPLIT_TEXT_IN_PARTS", "splitTextInPartsConfiguration": {
        "columnsToProcess": ["n"], "customSeparatorValue": "", "parts": 2, "separator": "SPACE"}}]
    count = ["aggregate", {"groupBy": [{"fieldPath": "id"}], "operations": [
        {"operation": "COUNT", "fieldPaths": ["n-split_2"], "delimiter": ",", "outputFieldPath": "c2"}]}]
    cols, out = run_chain(tmp_path, "id,n\n1,Garcia Perez\n2,Solo\n", ["id", "n"], [split, count])
    assert {r[cols.index("id")]: r[cols.index("c2")] for r in out} == {"1": "1", "2": "0"}


def test_replace_cell_equals_empty_does_not_touch_a_null_part(tmp_path):
    split = ["split-field", {"type": "SPLIT_TEXT_IN_PARTS", "splitTextInPartsConfiguration": {
        "columnsToProcess": ["n"], "customSeparatorValue": "", "parts": 2, "separator": "SPACE"}}]
    rep = ["strings", {"type": "REPLACE_ON_VALUE", "replaceOnValueConfiguration": {
        "cellValue": {"operator": "EQUALS", "value": ""}, "columnsToProcess": ["n-split_2"], "newColumnName": "",
        "replaceMethod": "REPLACE_CELL_WITH_VALUE", "replaceValue": "SIN", "shouldCreateNewColumn": False}}]
    cols, out = run_chain(tmp_path, "id,n\n2,Solo\n", ["id", "n"], [split, rep])
    assert out[0][cols.index("n-split_2")] in ("", None)  # medido en la cadena cadena_dividir_reemplazar: no se reemplaza


# --- unpivot (CROSSTABLE de Qlik) ------------------------------------------------------------------------------

def unpivot_cfg(cols, attr="atributo", val="valor"):
    return {"unpivotColumns": cols, "attributeColumn": attr, "valueColumn": val}


def test_unpivot_turns_columns_into_rows_keeping_the_other_columns_as_keys(tmp_path):
    cols, out = run_one(tmp_path, "id,a,b\n1,x,y\n2,z,w\n", ["id", "a", "b"], "unpivot", unpivot_cfg(["a", "b"]))
    assert cols == ["id", "atributo", "valor"]
    assert [tuple(r) for r in out] == [("1", "a", "x"), ("1", "b", "y"), ("2", "a", "z"), ("2", "b", "w")]  # por fila y por columna


def test_unpivot_of_a_middle_column_keeps_the_other_columns_in_their_order(tmp_path):
    cols, out = run_one(tmp_path, "id,x,k\n1,5,A\n", ["id", "x", "k"], "unpivot", unpivot_cfg(["x"]))
    assert cols == ["id", "k", "atributo", "valor"] and [tuple(r) for r in out] == [("1", "A", "x", "5")]


def test_unpivot_mixed_types_become_text_and_empty_cells_are_kept(tmp_path):
    cols, out = run_one(tmp_path, "id,n,t\n1,10,\n", ["id", "n", "t"], "unpivot", unpivot_cfg(["n", "t"]))
    # la celda vacia no se descarta (CROSSTABLE solo omite los NULL); el CSV de salida no distingue '' de NULL
    assert [tuple(r[:2]) for r in out] == [("1", "n"), ("1", "t")] and out[0][2] == "10"


# --- variantes de strings descubiertas con scripts/discover_config.py ---------------------------------------------

def test_lowercase_in_place_and_into_a_new_column(tmp_path):
    cfg = {"type": "LOWERCASE", "lowercaseConfiguration": {"columnsToProcess": ["n"], "newColumnName": "", "shouldCreateNewColumn": False}}
    cols, out = run_one(tmp_path, "id,n\n1,Guayaquil\n", ["id", "n"], "strings", cfg)
    assert out[0][cols.index("n")] == "guayaquil"
    cfg["lowercaseConfiguration"].update({"newColumnName": "n_min", "shouldCreateNewColumn": True})
    cols, out = run_one(tmp_path, "id,n\n1,Guayaquil\n", ["id", "n"], "strings", cfg)
    assert out[0][cols.index("n")] == "Guayaquil" and out[0][cols.index("n_min")] == "guayaquil"


# --- math: operaciones binarias y unarias (hipotesis; la bateria las contrasta con el tenant) --------------------

def math_cfg(subtype, key, const=0, mode="WITH_VALUE", selected=""):
    return {"type": subtype, key: {"columnsToProcess": ["n"], "constantValue": const, "mode": mode, "newColumnName": "m",
                                   "selectedColumn": selected, "shouldCreateNewColumn": True}}


@pytest.mark.parametrize("subtype,key,n,const,expected", [
    ("ADD", "addConfiguration", 10, 5, "15"),
    ("SUBTRACT", "subtractConfiguration", 10, 4, "6"),
    ("DIVIDE", "divideConfiguration", 10, 4, "2.5"),
    ("MODULO", "moduloConfiguration", 10, 3, "1"),
    ("POW_NUMBERS", "powNumbersConfiguration", 10, 2, "100"),
    ("MIN_NUMBERS", "minNumbersConfiguration", 10, 7, "7"),
    ("MAX_NUMBERS", "maxNumbersConfiguration", 10, 7, "10"),
    ("NEGATE_NUMBERS", "negateNumbersConfiguration", 10, 0, "-10"),
    ("SQUARE_ROOT_NUMBERS", "squareRootNumbersConfiguration", 16, 0, "4"),
])
def test_math_operations_with_a_constant(tmp_path, subtype, key, n, const, expected):
    cols, out = run_one(tmp_path, f"id,n,k\n1,{n},3\n", ["id", "n", "k"], "math", math_cfg(subtype, key, const))
    assert out[0][cols.index("m")] == expected


def test_math_add_with_another_field(tmp_path):
    cols, out = run_one(tmp_path, "id,n,k\n1,10,3\n", ["id", "n", "k"], "math",
                        math_cfg("ADD", "addConfiguration", mode="WITH_FIELD", selected="k"))
    assert out[0][cols.index("m")] == "13"


def test_doubles_are_written_with_14_significant_digits_like_qlik(tmp_path):
    # medido en el tenant con raiz cuadrada: Qlik escribe 1.4142135623731 donde DuckDB da 1.4142135623730951
    cols, out = run_one(tmp_path, "id,n\n1,2\n2,5\n3,16\n", ["id", "n"], "math",
                        {"type": "SQUARE_ROOT_NUMBERS", "squareRootNumbersConfiguration": {
                            "columnsToProcess": ["n"], "newColumnName": "m", "shouldCreateNewColumn": True}})
    assert [r[cols.index("m")] for r in out] == ["1.4142135623731", "2.2360679774998", "4"]


# --- variantes cuya expresion se leyo en el script que genera Qlik (2026-11-23) ------------------------------------

def vcfg(subtype, key, **extra):
    return {"type": subtype, key: {"columnsToProcess": ["n"], "newColumnName": "m", "shouldCreateNewColumn": True, **extra}}


def test_compute_length_creates_col_length_with_the_length(tmp_path):  # Len([c]) AS [c_length]
    cols, out = run_one(tmp_path, "id,n\n1,Quito\n", ["id", "n"], "strings", vcfg("COMPUTE_LENGTH", "computeLengthConfiguration"))
    assert out[0][cols.index("n_length")] == "5"


def test_contains_creates_col_contains_value_with_true_or_false(tmp_path):  # IF(Index([c], 'ui'), Dual('TRUE', -1), Dual('FALSE', 0))
    cols, out = run_one(tmp_path, "id,n\n1,Quito\n2,Loja\n", ["id", "n"], "strings",
                        vcfg("CONTAINS", "containsConfiguration", constantValue="ui"))
    assert [r[cols.index("n_contains_ui")] for r in out] == ["TRUE", "FALSE"]


def test_padding_defaults_and_substring_defaults(tmp_path):
    # sin parametros Qlik genera Repeat('0', 5 - Len(c)) & c y Mid(c, 1, 5); no se conocen las claves de los parametros
    cols, out = run_one(tmp_path, "id,n\n1,ab\n2,abcdefg\n", ["id", "n"], "strings", vcfg("PADDING", "paddingConfiguration"))
    assert [r[cols.index("m")] for r in out] == ["000ab", "abcdefg"]  # lpad de DuckDB truncaria 'abcdefg'
    cols, out = run_one(tmp_path, "id,n\n1,Guayaquil\n", ["id", "n"], "strings", vcfg("SUBSTRING", "substringConfiguration"))
    assert out[0][cols.index("m")] == "Guaya"


def test_convert_to_string_and_remove_non_alpha_num(tmp_path):
    cols, out = run_one(tmp_path, "id,n\n1,5\n", ["id", "n"], "strings", vcfg("CONVERT_TO_STRING", "convertToStringConfiguration"))
    assert out[0][cols.index("m")] == "5"
    cols, out = run_one(tmp_path, "id,n\n1,a.b-c d1\n", ["id", "n"], "strings",
                        vcfg("REMOVE_NON_ALPHA_NUM_CHARS", "removeNonAlphaNumCharsConfiguration"))
    assert out[0][cols.index("m")] == "abcd1"  # KeepChar solo conserva letras y digitos


def test_remove_negative_values_blanks_them_in_place(tmp_path):  # IF([c] < 0, Null(), [c]) AS [c]
    cols, out = run_one(tmp_path, "id,n\n1,-5\n2,7\n", ["id", "n"], "numbers",
                        vcfg("REMOVE_NEGATIVE_VALUES", "removeNegativeValuesConfiguration"))
    assert [r[cols.index("n")] for r in out] == [None, "7"] and "m" not in cols


@pytest.mark.parametrize("unit,expected", [
    ("YEAR", "1/1/1998"), ("MONTH", "9/1/1998"), ("DAY", "9/13/1998"), ("HOUR", "9/13/1998 12:00:00 AM"),
])
def test_truncate_date_creates_col_truncated_in_the_script_date_format(tmp_path, unit, expected):
    cfg = vcfg("TRUNCATE_DATE", "truncateDateConfiguration", timeUnit=unit)
    cols, out = run_one(tmp_path, "id,n\n1,1998-09-13\n", ["id", "n"], "date", cfg)
    assert out[0][cols.index("n_truncated")] == expected


def test_truncate_date_rejects_the_units_the_server_rejects(tmp_path):
    from emulator import runner as r
    with pytest.raises(r.Unsupported):
        run_one(tmp_path, "id,n\n1,1998-09-13\n", ["id", "n"], "date", vcfg("TRUNCATE_DATE", "truncateDateConfiguration", timeUnit="WEEK"))
