import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli  # noqa: E402
from emulator.bridge import Bridge, BridgeError, DryRun, SafetyError  # noqa: E402
from emulator.remote import BASE_APP_ID, Clone, FlowRef, Remote, UnsupportedGraph  # noqa: E402
from fakes import FakeRunner  # noqa: E402

SB = "000000000000000000000000"
OTRO = "otro_espacio"
APP = "00000000-0000-0000-0000-000000000001"
DF = "df-1"

ITEMS = [
    {"name": "fundamentos", "spaceId": SB, "resourceSubType": "dataflow-prep",
     "resourceId": "r1", "resourceAttributes": {"id": "app1"}},
    {"name": "otra", "spaceId": OTRO, "resourceSubType": "dataflow-prep", "resourceId": "r2"},
    {"name": "app normal", "spaceId": SB, "resourceSubType": None,
     "resourceId": "r3", "resourceAttributes": {"id": "app3"}},
]
DATAFLOW = {"id": DF, "name": "fundamentos", "graph": {"nodes": [1, 2, 3]}}
SCRIPT = "LOAD DISTINCT * FROM x;"


def routes(app_id=APP, items=None):
    return {
        ("GET", "v1/items"): ITEMS if items is None else items,
        ("GET", f"v1/dataflow-apps/{app_id}"): {"dataflowId": DF, "id": app_id, "usage": "DATAFLOW_PREP"},
        ("GET", f"v1/dataflows/{DF}"): DATAFLOW,
        ("GET", f"v1/apps/{app_id}/scripts/current"): {"script": SCRIPT, "versionMessage": ""},
    }


def make_bridge(routes_, tmp_path):
    runner = FakeRunner(routes_)
    return Bridge(runner=runner, audit_path=str(tmp_path / "audit.jsonl")), runner


def test_list_dataflows_filters_subtype_and_space(tmp_path):
    b, _ = make_bridge(routes(), tmp_path)
    remote = Remote(b)
    assert remote.list_dataflows() == [
        FlowRef("fundamentos", "app1", SB),
        FlowRef("otra", "r2", OTRO),  # sin resourceAttributes: cae a resourceId
    ]
    assert remote.list_dataflows(SB) == [FlowRef("fundamentos", "app1", SB)]


def test_pull_returns_graph_and_script(tmp_path):
    b, _ = make_bridge(routes(), tmp_path)
    data = Remote(b).pull(APP)
    assert set(data) == {"appId", "dataflowId", "dataflow", "script"}
    assert data["appId"] == APP
    assert data["dataflowId"] == DF
    assert data["dataflow"]["graph"]["nodes"] == [1, 2, 3]
    assert data["script"] == SCRIPT


def test_pull_rejects_invalid_app_id(tmp_path):
    b, _ = make_bridge(routes(), tmp_path)
    with pytest.raises(SafetyError):
        Remote(b).pull("../items")


def test_cli_pull_writes_file(tmp_path, monkeypatch):
    b, _ = make_bridge(routes(), tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    cli.main(["pull", APP, "--out", str(tmp_path)])
    assert (tmp_path / "fundamentos.pull.json").exists()
    saved = json.loads((tmp_path / "fundamentos.pull.json").read_text(encoding="utf-8"))
    assert saved["script"] == SCRIPT


def test_cli_pull_suffixes_name_when_existing_content_differs(tmp_path, monkeypatch):
    b, _ = make_bridge(routes(), tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    (tmp_path / "fundamentos.pull.json").write_text('{"otro": 1}', encoding="utf-8")
    cli.main(["pull", APP, "--out", str(tmp_path)])
    assert json.loads((tmp_path / "fundamentos.pull.json").read_text(encoding="utf-8")) == {"otro": 1}
    assert (tmp_path / "fundamentos_00000000.pull.json").exists()


def test_cli_pull_all_defaults_to_sandbox(tmp_path, monkeypatch):
    b, runner = make_bridge(routes(app_id="app1"), tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    cli.main(["pull", "--all", "--out", str(tmp_path)])
    assert [p.name for p in tmp_path.glob("*.pull.json")] == ["fundamentos.pull.json"]
    assert ("GET", "v1/dataflow-apps/r2") not in [(c[0], c[1]) for c in runner.calls]


def test_cli_pull_without_target_is_argparse_error(tmp_path, monkeypatch):
    b, _ = make_bridge(routes(), tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    with pytest.raises(SystemExit) as e:
        cli.main(["pull", "--out", str(tmp_path)])
    assert e.value.code == 2


def test_cli_pull_all_continues_after_failure(tmp_path, monkeypatch, capsys):
    items = [
        {"name": "uno", "spaceId": SB, "resourceSubType": "dataflow-prep", "resourceAttributes": {"id": "app1"}},
        {"name": "dos", "spaceId": SB, "resourceSubType": "dataflow-prep", "resourceAttributes": {"id": "app2"}},
    ]
    rt = routes(app_id="app1", items=items)
    rt[("GET", "v1/dataflow-apps/app2")] = (1, "", "boom")
    b, _ = make_bridge(rt, tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    with pytest.raises(SystemExit) as e:
        cli.main(["pull", "--all", "--out", str(tmp_path)])
    assert e.value.code == 1
    assert (tmp_path / "fundamentos.pull.json").exists()  # el primero se escribió
    assert "app2" in capsys.readouterr().err


def test_cli_pull_single_failure_exits_1_without_traceback(tmp_path, monkeypatch, capsys):
    rt = routes()
    rt[("GET", f"v1/dataflow-apps/{APP}")] = (1, "", "boom")
    b, _ = make_bridge(rt, tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    with pytest.raises(SystemExit) as e:
        cli.main(["pull", APP, "--out", str(tmp_path)])
    assert e.value.code == 1
    assert APP in capsys.readouterr().err


def test_empty_stdout_gives_clear_error(tmp_path, monkeypatch, capsys):
    rt = routes()
    rt[("GET", f"v1/dataflow-apps/{APP}")] = (0, "", "")
    b, _ = make_bridge(rt, tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    with pytest.raises(SystemExit) as e:
        cli.main(["pull", APP, "--out", str(tmp_path)])
    assert e.value.code == 1
    assert "respuesta" in capsys.readouterr().err


def test_item_without_space_is_listed_and_skipped_by_all(tmp_path, monkeypatch):
    items = [
        {"name": "personal", "resourceSubType": "dataflow-prep", "resourceAttributes": {"id": "app9"}},
        {"resourceSubType": "dataflow-prep"},  # sin id de app: se omite
    ]
    b, _ = make_bridge(routes(items=items), tmp_path)
    assert Remote(b).list_dataflows() == [FlowRef("personal", "app9", "")]
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    cli.main(["pull", "--all", "--out", str(tmp_path)])  # no rompe
    assert list(tmp_path.glob("*.pull.json")) == []


def _plain_items(n):
    return [{"name": f"x{i}", "spaceId": SB, "resourceSubType": None, "resourceId": f"r{i}"} for i in range(n)]


def test_truncation_warning_at_100_items_only(tmp_path, capsys):
    b, _ = make_bridge(routes(items=_plain_items(99)), tmp_path)
    Remote(b).list_dataflows()
    assert "truncado" not in capsys.readouterr().err
    b, _ = make_bridge(routes(items=_plain_items(100)), tmp_path)
    Remote(b).list_dataflows()
    assert "posible listado truncado: 100 items" in capsys.readouterr().err


def test_accented_name_and_unicode_script_round_trip(tmp_path, monkeypatch):
    rt = routes()
    rt[("GET", f"v1/dataflows/{DF}")] = {"id": DF, "name": "Ñandú Ventas", "graph": {"nodes": []}}
    script = "// μ-cálculo\nLOAD DISTINCT * FROM x;"
    rt[("GET", f"v1/apps/{APP}/scripts/current")] = {"script": script, "versionMessage": ""}
    b, _ = make_bridge(rt, tmp_path)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: b)
    cli.main(["pull", APP, "--out", str(tmp_path)])
    path = tmp_path / "Nandu_Ventas.pull.json"
    assert path.exists()
    assert json.loads(path.read_text(encoding="utf-8"))["script"] == script


# --- Task 3: subir y validar con el servidor -------------------------------
CLONE_APP = "clone-app"
CLONE_DF = "clone-df"
GRAPH = {"nodes": [{"id": "n1", "component": {"type": "load"}}]}
SUBFLOW_GRAPH = {"nodes": [{"id": "n1", "component": {"type": "subflow"}}]}


def _put_resp(status, violations=()):
    return {"id": CLONE_DF, "validity": {"status": status, "label": status,
                                          "nodesConstraintViolations": list(violations)}}


def write_routes(put=None):
    names = {"name": "emu_v_x"}

    def copy(body):
        names["name"] = body["name"]
        return {"id": CLONE_APP, "dataflowId": CLONE_DF, "details": {}}

    return {
        ("POST", f"v1/dataflow-apps/{APP}/actions/copy"): copy,
        ("GET", f"v1/dataflows/{CLONE_DF}"): {
            "id": CLONE_DF, "name": "emu_v_x", "graph": {"nodes": []}, "checksum": "c",
            "context": {"dataAppId": CLONE_APP}, "validity": {"status": "UNCHANGED"}},
        ("GET", f"v1/apps/{CLONE_APP}"): lambda _b: {"attributes": {"name": names["name"], "spaceId": SB}},
        ("PUT", f"v1/dataflows/{CLONE_DF}"): put or (lambda _b: _put_resp("VALID")),
        ("DELETE", f"v1/apps/{CLONE_APP}"): {},
        ("GET", f"v1/apps/{CLONE_APP}/scripts/current"): {"script": SCRIPT, "versionMessage": ""},
    }


def apply_bridge(rt, tmp_path):
    runner = FakeRunner(rt)
    return Bridge(runner=runner, apply=True, audit_path=str(tmp_path / "audit.jsonl")), runner


def test_push_graph_put_body_has_no_validity_and_new_graph(tmp_path):
    b, runner = apply_bridge(write_routes(), tmp_path)
    res = Remote(b).push_graph(Clone(CLONE_APP, CLONE_DF, "emu_v_x"), GRAPH)
    put = [c for c in runner.calls if c[0] == "PUT"][0]
    assert "validity" not in put[2]
    assert put[2]["graph"] == GRAPH
    assert put[2]["context"] == {"dataAppId": CLONE_APP}
    assert res.validity["status"] == "VALID"
    assert res.script == SCRIPT


def test_validity_of_discards_clone_when_put_fails(tmp_path):
    rt = write_routes()
    rt[("PUT", f"v1/dataflows/{CLONE_DF}")] = (1, "", "boom")
    b, runner = apply_bridge(rt, tmp_path)
    with pytest.raises(BridgeError):
        Remote(b).validity_of(GRAPH, base_app_id=APP)
    assert ("DELETE", f"v1/apps/{CLONE_APP}") in [(c[0], c[1]) for c in runner.calls]


def test_validity_of_rejects_subflow_graph_without_any_call(tmp_path):
    b, runner = apply_bridge(write_routes(), tmp_path)
    with pytest.raises(UnsupportedGraph):
        Remote(b).validity_of(SUBFLOW_GRAPH, base_app_id=APP)
    assert runner.calls == []


def test_validity_of_dry_run_creates_nothing(tmp_path):
    runner = FakeRunner(write_routes())
    b = Bridge(runner=runner, apply=False, audit_path=str(tmp_path / "audit.jsonl"))
    with pytest.raises(DryRun):
        Remote(b).validity_of(GRAPH, base_app_id=APP)
    assert [c for c in runner.calls if c[0] in ("POST", "PUT")] == []


def test_clone_outside_sandbox_impossible(tmp_path):
    b, runner = apply_bridge(write_routes(), tmp_path)
    Remote(b).validity_of(GRAPH, base_app_id=APP)
    copy = [c for c in runner.calls if c[1].endswith("/actions/copy")][0]
    assert copy[2]["spaceId"] == SB
    assert copy[2]["name"].startswith("emu_v_") and len(copy[2]["name"]) == len("emu_v_") + 8


def _patch_bridge(monkeypatch, rt, tmp_path):
    runner = FakeRunner(rt)
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(
        runner=runner, apply=apply, audit_path=str(tmp_path / "audit.jsonl")))
    return runner


def _dfw(tmp_path):
    p = tmp_path / "flow.dfw"
    p.write_text(json.dumps({"dataflow": {"graph": GRAPH}}), encoding="utf-8")
    return str(p)


def test_cli_validate_remote_exit_code(tmp_path, monkeypatch, capsys):
    rt = write_routes(put=lambda _b: _put_resp("INVALID", [
        {"code": "E1", "title": "Falta columna", "level": "ERROR", "nodeId": "n1", "label": "x"}]))
    _patch_bridge(monkeypatch, rt, tmp_path)
    with pytest.raises(SystemExit) as e:
        cli.main(["validate", "--remote", "--apply", _dfw(tmp_path)])
    assert e.value.code == 1
    out = capsys.readouterr().out
    assert "INVALID" in out and "   - E1: Falta columna" in out

    _patch_bridge(monkeypatch, write_routes(), tmp_path)
    with pytest.raises(SystemExit) as e:
        cli.main(["validate", "--remote", "--apply", _dfw(tmp_path)])
    assert e.value.code == 0


def test_cli_validate_remote_simulation_prints_and_exits_0(tmp_path, monkeypatch, capsys):
    _patch_bridge(monkeypatch, write_routes(), tmp_path)
    with pytest.raises(SystemExit) as e:
        cli.main(["validate", "--remote", _dfw(tmp_path)])
    assert e.value.code == 0
    assert f"[simulación] POST v1/dataflow-apps/{BASE_APP_ID}/actions/copy" in capsys.readouterr().out


# --- rechazo estructural del servidor (PUT con error HTTP, no con validity) ---
CYCLE_ERR = ('Error: {"errors": [{"code": "DATAFLOW_STRUCTURAL_ERROR", "title": "Dataflow\'s structure is invalid", '
             '"detail": "Dataflow has at least one cycle"}], "traceId": "t1"}')


def test_validity_of_structural_rejection_is_rejected_and_discards_clone(tmp_path):
    rt = write_routes()
    rt[("PUT", f"v1/dataflows/{CLONE_DF}")] = (1, "", CYCLE_ERR)
    b, runner = apply_bridge(rt, tmp_path)
    res = Remote(b).validity_of(GRAPH, base_app_id=APP)
    assert res.validity["status"] == "REJECTED"
    assert "cycle" in res.validity["label"]
    assert res.validity["nodesConstraintViolations"] == []
    assert res.script == ""
    assert ("DELETE", f"v1/apps/{CLONE_APP}") in [(c[0], c[1]) for c in runner.calls]


def test_structural_rejection_without_json_uses_raw_stderr(tmp_path):
    rt = write_routes()
    rt[("PUT", f"v1/dataflows/{CLONE_DF}")] = (1, "", "DATAFLOW_STRUCTURAL_ERROR sin formato")
    b, _ = apply_bridge(rt, tmp_path)
    res = Remote(b).validity_of(GRAPH, base_app_id=APP)
    assert res.validity["status"] == "REJECTED"
    assert "DATAFLOW_STRUCTURAL_ERROR" in res.validity["label"]


def test_put_other_error_still_raises(tmp_path):
    rt = write_routes()
    rt[("PUT", f"v1/dataflows/{CLONE_DF}")] = (1, "", "boom")
    b, _ = apply_bridge(rt, tmp_path)
    with pytest.raises(BridgeError):
        Remote(b).validity_of(GRAPH, base_app_id=APP)


def test_cli_validate_remote_rejected_exit_1(tmp_path, monkeypatch, capsys):
    rt = write_routes()
    rt[("PUT", f"v1/dataflows/{CLONE_DF}")] = (1, "", CYCLE_ERR)
    _patch_bridge(monkeypatch, rt, tmp_path)
    with pytest.raises(SystemExit) as e:
        cli.main(["validate", "--remote", "--apply", _dfw(tmp_path)])
    assert e.value.code == 1
    out = capsys.readouterr().out
    assert ": REJECTED" in out and "   - " in out and "cycle" in out
