"""Cobertura del corpus: conteo de processors y clasificacion de estados."""
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli, coverage, runner  # noqa: E402


def graph(*tipos):
    return {"nodes": [{"id": f"n{i}", "type": "processor",
                       "component": {"type": t, "properties": {"configuration": {}}}}
                      for i, t in enumerate(tipos)]}


def test_processors_of_counts_types_and_variants():
    d = {"dataflow": {"graph": graph("filter", "strings")},
         "subflows": [{"id": "s1", "graph": graph("join", "filter")}]}
    d["dataflow"]["graph"]["nodes"][1]["component"]["properties"]["configuration"]["type"] = "TRIM"
    counts = coverage.processors_of(d)
    assert counts[("filter", None)] == 2
    assert counts[("strings", "TRIM")] == 1
    assert counts[("join", None)] == 1


def test_classify_separates_tenant_connection_and_failure():
    assert coverage.classify(runner.Unsupported("script de Qlik: validado pero no ejecutable"))[0] == coverage.SOLO_TENANT
    assert coverage.classify(runner.Unsupported("conexion 'X' sin configurar"))[0] == coverage.REQUIERE_CONEXION
    assert coverage.classify(RuntimeError("boom")) == (coverage.FALLA, "RuntimeError: boom")


def test_run_file_marks_draft(tmp_path):
    p = tmp_path / "vacio.dfw"
    p.write_text(json.dumps({"dataflow": {"graph": {"nodes": []}}}), encoding="utf-8")
    assert coverage.run_file(str(p), str(tmp_path))[0] == coverage.BORRADOR


def test_run_file_connection_without_metadata_needs_connection():
    path = os.path.join(ROOT, "samples", "Copia de Ventas Mensuales (Julio).dfw")
    estado, detalle = coverage.run_file(path, os.path.join(ROOT, "data", "practica"))
    assert estado == coverage.REQUIERE_CONEXION
    assert "sin metadatos" in detalle


@pytest.mark.skipif(not os.path.exists(os.path.join(ROOT, "data", "practica", "clientes.csv")),
                    reason="faltan los CSV de practica en data/practica")
def test_cli_coverage_exit_0_with_runnable_sample(capsys):
    with pytest.raises(SystemExit) as e:
        cli.main(["coverage", os.path.join("samples", "fundamentos.dfw")])
    assert e.value.code == 0
    out = capsys.readouterr().out
    assert "ejecuta" in out and "resumen: ejecuta=1" in out
