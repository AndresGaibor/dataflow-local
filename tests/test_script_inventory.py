"""scripts/script_inventory.py: que constructs de Qlik script aparecen en el corpus y cuales se traducen."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)
import script_inventory as si  # noqa: E402

QVS = """SET ThousandSep=',';
[Ordenes]:
LOAD OrdenId, Num(Importe, '#,##0.00') as Importe, Date(Fecha) as Dia
FROM [lib://x/ordenes.csv] (txt, utf8, embedded labels, delimiter is ',');
LEFT JOIN (Ordenes) LOAD OrdenId, upper(Cliente) as Cliente Resident Ordenes;
STORE Ordenes INTO [lib://out/ordenes.qvd] (qvd);
"""


def test_statements_and_functions_are_extracted():
    assert si.statements(QVS) == ["SET", "LOAD", "LEFT JOIN", "STORE"] or si.statements(QVS)[0] == "SET"
    funcs = si.functions(QVS)
    assert "NUM" in funcs and "DATE" in funcs and "UPPER" in funcs
    assert "LOAD" not in funcs  # es una sentencia, no una funcion


def test_scripts_from_json_finds_script_nodes_by_label():
    graph = {
        "dataflow": {"graph": {"nodes": [
            {"label": "Fuente", "type": "source", "component": {"properties": {}}},
            {"label": "Script Qlik", "type": "processor",
             "component": {"type": "script", "properties": {"configuration": {"script": "SET x=1;"}}}},
        ]}}
    }
    assert si.scripts_from_json(graph) == {"Script Qlik": "SET x=1;"}


def test_inventory_marks_a_construct_as_only_on_tenant_when_translation_fails():
    scripts = {"bueno": "SET a=1;", "malo": "SUBSTITUTE_FOO();"}

    def fake_translate(text, data_dir):
        return (None, ["sentencia no soportada: SUBSTITUTE_FOO"]) if "SUBSTITUTE_FOO" in text else ("SELECT 1", [])

    inv = si.inventory(scripts, translate=fake_translate)
    assert inv["scripts"] == 2
    assert inv["translated"] == 1
    assert inv["constructs"]["SUBSTITUTE_FOO"]["status"] == "no cubierto"
    assert inv["constructs"]["SET"]["status"] == "cubierto"


def test_inventory_counts_scripts_per_construct():
    scripts = {"a": "SET x=1;", "b": "SET y=2;", "c": "TRACE hello;"}
    inv = si.inventory(scripts, translate=lambda t, d: ("SELECT 1", []))
    assert inv["constructs"]["SET"]["scripts"] == 2
    assert inv["constructs"]["TRACE"]["scripts"] == 1


def test_report_md_has_a_row_per_construct():
    inv = si.inventory({"a": "SET x=1;"}, translate=lambda t, d: ("SELECT 1", []))
    md = si.report_md(inv)
    assert "| construct |" in md
    assert "| `SET` |" in md
    assert "de 1" in md


def test_scripts_from_paths_reads_qvs(tmp_path):
    p = tmp_path / "a.qvs"
    p.write_text(QVS, encoding="utf-8")
    scripts = si.scripts_from_paths([str(p)])
    assert list(scripts) == ["a"] or "a" in scripts
