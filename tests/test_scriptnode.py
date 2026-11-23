"""dfemu script-node: crea un nodo `script` por API reutilizando el de una copia (con su schemaEntityId valido)."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli, scriptnode  # noqa: E402
from emulator.bridge import Bridge  # noqa: E402
from emulator.remote import Remote, UnsupportedGraph  # noqa: E402
from fakes import FakeRunner  # noqa: E402

SB = "000000000000000000000000"
BASE = "00000000-0000-0000-0000-0000000000aa"
CLONE_APP, CLONE_DF = "clone-app", "clone-df"
SCRIPT = "[Salida]:\nNoConcatenate\nLOAD *\nResident [fuente];\nDROP TABLE [fuente];"


def src(label="fuente"):
    return {"id": "s", "type": "source", "label": label, "component": {"type": "analyticsSource", "properties": {}},
            "handles": {"outgoing": [{"id": "so", "type": "DEFAULT"}]}}


def script_node(label="Mi script"):
    return {"id": "c", "type": "processor", "label": label,
            "component": {"type": "script", "properties": {"configuration": {
                "$state": "CONFIGURED", "script": SCRIPT, "schemaEntityId": "SCH-DE-LA-COPIA"}}},
            "handles": {"incoming": [{"id": "ci1", "type": "OPTIONAL"}, {"id": "ci2", "type": "OPTIONAL"}],
                        "outgoing": [{"id": "co", "type": "DEFAULT"}]}}


def other():
    return {"id": "o", "type": "processor", "label": "Otro", "component": {"type": "filter", "properties": {}},
            "handles": {"incoming": [{"id": "oi", "type": "DEFAULT"}], "outgoing": [{"id": "oo", "type": "DEFAULT"}]}}


def graph(extra_edge=True):
    edges = [{"id": "e1", "sourceHandle": "so", "targetHandle": "ci1"}] if extra_edge else []
    return {"nodes": [src(), script_node(), other()], "edges": edges}


def routes(g):
    names = {}

    def copy(body):
        names["n"] = body["name"]
        return {"id": CLONE_APP, "dataflowId": CLONE_DF}
    return {
        ("POST", f"v1/dataflow-apps/{BASE}/actions/copy"): copy,
        ("GET", f"v1/dataflows/{CLONE_DF}"): {"id": CLONE_DF, "graph": g, "context": {"dataAppId": CLONE_APP}, "checksum": "c",
                                              "validity": {"status": "UNCHANGED"}},
        ("GET", f"v1/apps/{CLONE_APP}"): lambda _b: {"attributes": {"name": names["n"], "spaceId": SB}},
        ("PUT", f"v1/dataflows/{CLONE_DF}"): {"validity": {"status": "VALID", "nodesConstraintViolations": []}},
        ("GET", f"v1/apps/{CLONE_APP}/scripts/current"): {"script": "///$tab Generated\n" + SCRIPT},
        ("DELETE", f"v1/apps/{CLONE_APP}"): {},
    }


def remote(g, tmp_path):
    runner = FakeRunner(routes(g))
    return Remote(Bridge(runner=runner, apply=True, audit_path=str(tmp_path / "a.jsonl"))), runner


def test_builds_a_reduced_graph_with_the_copied_node_and_a_new_script(tmp_path):
    r, runner = remote(graph(), tmp_path)
    res = scriptnode.push_script_node(r, BASE, "fuente", "Mi script", SCRIPT, "emu_salida")
    put = next(c for c in runner.calls if c[0] == "PUT")[2]["graph"]
    assert [n["label"] for n in put["nodes"]] == ["fuente", "Mi script", "Destino"]  # "Otro" no viaja
    sc = put["nodes"][1]["component"]["properties"]["configuration"]
    assert sc["script"] == SCRIPT and sc["schemaEntityId"] == "SCH-DE-LA-COPIA"  # el id valido de la copia se conserva
    assert len(put["edges"]) == 2
    assert {e["sourceHandle"] for e in put["edges"]} == {"so", "co"}
    assert res.validity["status"] == "VALID" and "Resident" in res.script


def test_the_clone_is_discarded_even_when_the_labels_do_not_exist(tmp_path):
    r, runner = remote(graph(), tmp_path)
    with pytest.raises(UnsupportedGraph, match="no hay un nodo"):
        scriptnode.push_script_node(r, BASE, "fuente", "No existe", SCRIPT, "emu_salida")
    assert not [c for c in runner.calls if c[0] == "PUT"]
    assert ("DELETE", f"v1/apps/{CLONE_APP}") in [(c[0], c[1]) for c in runner.calls]


def test_the_script_node_must_hang_directly_from_the_source(tmp_path):
    r, _ = remote(graph(extra_edge=False), tmp_path)
    with pytest.raises(UnsupportedGraph, match="directamente"):
        scriptnode.push_script_node(r, BASE, "fuente", "Mi script", SCRIPT, "emu_salida")


def test_the_target_name_must_be_an_emu_name(tmp_path):
    r, _ = remote(graph(), tmp_path)
    with pytest.raises(UnsupportedGraph, match="emu_"):
        scriptnode.push_script_node(r, BASE, "fuente", "Mi script", SCRIPT, "salida_real")


def test_cli_writes_the_generated_script(tmp_path, monkeypatch, capsys):
    r, runner = remote(graph(), tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(runner=runner, apply=True, audit_path=str(tmp_path / "a.jsonl")))
    sfile, out = tmp_path / "s.qvs", tmp_path / "gen.qvs"
    sfile.write_text(SCRIPT, encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        cli.main(["script-node", "--base-app", BASE, "--source", "fuente", "--node", "Mi script",
                  "--script", str(sfile), "--out", str(out), "--apply"])
    assert e.value.code == 0
    assert "VALID" in capsys.readouterr().out and "Resident" in out.read_text(encoding="utf-8")


def test_the_new_script_must_declare_the_output_table_registered_in_the_node(tmp_path):
    # el script generado hace STORE de la tabla registrada en el nodo; si el script nuevo declara otra, falla al ejecutarse
    # aunque el servidor diga VALID (medido)
    r, runner = remote(graph(), tmp_path)
    with pytest.raises(UnsupportedGraph, match=r"\[Salida\]"):
        scriptnode.push_script_node(r, BASE, "fuente", "Mi script", SCRIPT.replace("[Salida]", "[Otra]"), "emu_salida")
    assert not [c for c in runner.calls if c[0] == "PUT"]
    assert ("DELETE", f"v1/apps/{CLONE_APP}") in [(c[0], c[1]) for c in runner.calls]
