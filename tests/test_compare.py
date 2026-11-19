"""Comparador de huellas y `dfemu compare`: pruebas con fakes y tmp_path, sin tocar el tenant."""
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli, compare, dfw, oracle, runner  # noqa: E402
from emulator.bridge import Bridge  # noqa: E402
from fakes import FakeRunner  # noqa: E402

APP = "00000000-0000-0000-0000-000000000001"
GRAPH = {"nodes": [{"id": "n1", "component": {"type": "load"}}]}
SCRIPT = "LOAD DISTINCT * FROM x;"


def fp(rows, columns):
    return {"rows": rows, "columns": columns}


def col(count, distinct, sum=None):
    return {"count": count, "distinct": distinct, "sum": sum}


BASE = fp(3, {"id": col(3, 2, 5.0), "nombre": col(2, 2)})


def test_local_fingerprint_csv(tmp_path):
    p = tmp_path / "clientes.csv"
    p.write_text("id,nombre,monto\n1,ana,10.5\n2,luis,\n2,,4\n", encoding="utf-8")
    assert compare.local_fingerprint(str(p)) == fp(3, {
        "id": col(3, 2, 5.0),
        "nombre": col(2, 2, None),
        "monto": col(2, 2, 14.5),
    })


def test_compare_equal_is_empty():
    assert compare.compare({"t": BASE}, {"t": BASE}) == []


def test_compare_missing_table_on_each_side():
    assert compare.compare({"a": BASE}, {}) == ["tabla 'a' solo en el emulador"]
    assert compare.compare({}, {"a": BASE}) == ["tabla 'a' solo en el tenant"]


def test_compare_rows_differ():
    msgs = compare.compare({"t": fp(3, {})}, {"t": fp(4, {})})
    assert msgs == ["t: filas 3 (emulador) != 4 (tenant)"]


def test_compare_column_missing_on_each_side():
    msgs = compare.compare({"t": fp(3, {"a": col(3, 3)})}, {"t": fp(3, {"b": col(3, 3)})})
    assert msgs == ["t.a: columna solo en el emulador", "t.b: columna solo en el tenant"]


def test_compare_sum_out_of_tolerance():
    msgs = compare.compare({"t": fp(3, {"x": col(3, 3, 5.0)})}, {"t": fp(3, {"x": col(3, 3, 5.5)})})
    assert msgs == ["t.x: sum 5.0 (emulador) != 5.5 (tenant)"]


def test_compare_sum_within_tolerance():
    a = {"t": fp(3, {"x": col(3, 3, 1000000.0)})}
    b = {"t": fp(3, {"x": col(3, 3, 1000000.0 + 1e-4)})}  # diferencia relativa 1e-10
    assert compare.compare(a, b) == []


def test_stem_of_qvd_parquet():
    assert compare.stem_of("out/files/a.qvd.parquet") == "a"
    assert compare.stem_of("x/y/clientes.csv") == "clientes"


def test_local_fingerprints_duplicate_stem_raises():
    with pytest.raises(ValueError, match="destinos con el mismo nombre: a"):
        compare.local_fingerprints(["out/x/a.csv", "out/y/a.qvd.parquet"])


def _dfw(tmp_path):
    p = tmp_path / "flow.dfw"
    p.write_text(json.dumps({"dataflow": {"graph": GRAPH}}), encoding="utf-8")
    return str(p)


def _patch(monkeypatch, tmp_path, remote_rows, csv_text):
    csv = tmp_path / "clientes.csv"
    csv.write_text(csv_text, encoding="utf-8")
    routes = {("GET", f"v1/apps/{APP}/scripts/current"): {"script": SCRIPT, "versionMessage": ""}}
    runner_ = FakeRunner(routes)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(
        runner=runner_, apply=apply, audit_path=str(tmp_path / "audit.jsonl")))
    monkeypatch.setattr(dfw, "validate", lambda d: [])
    monkeypatch.setattr(runner, "run", lambda d, data, out: [
        {"target": "clientes", "dest": str(csv), "rows": 3, "emulated_qvd": False}])
    monkeypatch.setattr(oracle, "run_script", lambda bridge, script, tag: {"clientes": remote_rows})


def test_cli_compare_exit_code(tmp_path, monkeypatch, capsys):
    csv_text = "id\n1\n2\n3\n"
    local_fp = fp(3, {"id": col(3, 3, 6.0)})
    _patch(monkeypatch, tmp_path, fp(3, {"id": col(3, 3, 7.0)}), csv_text)
    with pytest.raises(SystemExit) as e:
        cli.main(["compare", _dfw(tmp_path), "--app", APP])
    assert e.value.code == 1
    assert "clientes.id: sum 6.0 (emulador) != 7.0 (tenant)" in capsys.readouterr().out

    _patch(monkeypatch, tmp_path, local_fp, csv_text)
    cli.main(["compare", _dfw(tmp_path), "--app", APP])  # sin SystemExit: exit 0
    assert "OK: sin diferencias" in capsys.readouterr().out
