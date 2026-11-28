"""Recarga de una app emu_ por `v1/reloads`: lanzar, seguir el estado y resumir el error."""
import os
import sys
import types

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import cli, mcp, reload  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge, SafetyError  # noqa: E402
from fakes import FakeRunner  # noqa: E402

APP = "a" * 24
RID = "r" * 24


def runner(states, app=APP, log=""):
    """`states` se consume en cada GET; el POST devuelve QUEUED. Incluye la app emu_ y su log."""
    seq = list(states)

    def next_state(body):
        return seq.pop(0) if len(seq) > 1 else seq[0]

    return FakeRunner({
        ("POST", "v1/reloads"): {"id": RID, "status": "QUEUED", "appId": app},
        ("GET", f"v1/reloads/{RID}"): lambda body: {"id": RID, "status": next_state(body), "log": log},
        ("GET", f"v1/apps/{app}"): {"attributes": {"name": "emu_x", "spaceId": SANDBOX_SPACE_ID}},
    })


def test_start_posts_the_app_id():
    r = runner(["QUEUED"])
    started = reload.start(Bridge(runner=r, apply=True), APP)
    assert started["id"] == RID and started["status"] == "QUEUED"
    assert r.calls[-1][2] == {"appId": APP}


def test_start_rejects_a_response_without_id():
    r = FakeRunner({("POST", "v1/reloads"): {"status": "QUEUED"},
                    ("GET", f"v1/apps/{APP}"): {"attributes": {"name": "emu_x", "spaceId": SANDBOX_SPACE_ID}}})
    b = Bridge(runner=r, apply=True)
    with pytest.raises(ValueError):
        reload.start(b, APP)


def test_wait_reports_the_states_until_succeeded():
    res = reload.wait(Bridge(runner=runner(["QUEUED", "RELOADING", "SUCCEEDED"]), apply=True), RID, interval=0)
    assert res["ok"] is True
    assert res["states"] == ["QUEUED", "RELOADING", "SUCCEEDED"]


def test_wait_stops_on_failed_and_keeps_the_log():
    def states():
        return ["QUEUED", "FAILED"]

    r = FakeRunner({
        ("GET", f"v1/reloads/{RID}"): (lambda body, seq=states(): {"id": RID, "status": seq.pop(0),
                                                                   "log": "ReloadID: x\nStarted loading data\nThe following error(s) occurred:\nCannot open file: 'lib://a'\n"}),
    })
    res = reload.wait(Bridge(runner=r, apply=True), RID, interval=0)
    assert res["ok"] is False and res["status"] == "FAILED"
    line = reload.summary(res)
    assert "FAILED" in line and "Cannot open file" in line
    assert "ReloadID" not in line  # el ruido del motor no llega a la consola


def test_wait_gives_up_at_the_timeout():
    res = reload.wait(Bridge(runner=runner(["QUEUED"]), apply=True), RID, timeout=0, interval=0)
    assert res["ok"] is False and res["status"] == "QUEUED"


def test_run_without_wait_does_not_poll():
    r = runner(["QUEUED"])
    res = reload.run(Bridge(runner=r, apply=True), APP, wait_for=False)
    assert res["ok"] is None and res["states"] == ["QUEUED"]
    assert not [c for c in r.calls if c[0] == "GET" and c[1].startswith("v1/reloads")]  # no consulta el estado


def test_bridge_refuses_to_reload_an_app_that_is_not_emu():
    r = FakeRunner({("GET", f"v1/apps/{APP}"): {"attributes": {"name": "produccion", "spaceId": SANDBOX_SPACE_ID}}})
    with pytest.raises(SafetyError):
        reload.start(Bridge(runner=r, apply=True), APP)
    assert not [c for c in r.calls if c[0] == "POST"]


# ----- CLI -----
def _args(**kw):
    base = dict(app=APP, apply=True, no_wait=False, timeout=5, interval=0)
    base.update(kw)
    return types.SimpleNamespace(**base)


def test_cli_dry_run_only_simulates(monkeypatch, capsys):
    r = runner(["QUEUED"])
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(runner=r, apply=apply))
    assert cli.main(["reload", APP]) == 0
    assert "simulación" in capsys.readouterr().out


def test_cli_resolves_a_flow_name(monkeypatch, capsys):
    r = runner(["SUCCEEDED"])
    r.routes[("GET", "v1/items")] = {"data": [{"resourceType": "app", "resourceSubType": "dataflow-prep",
                                               "spaceId": SANDBOX_SPACE_ID, "name": "emu_e2e", "resourceAttributes": {"id": APP}}]}
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(runner=r, apply=apply))
    assert cli.main(["reload", "emu_e2e", "--apply", "--interval", "0"]) == 0
    assert "SUCCEEDED" in capsys.readouterr().out


def test_cli_fails_when_the_reload_fails(monkeypatch, capsys):
    r = runner(["FAILED"], log="The following error(s) occurred:\nboom\n")
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(runner=r, apply=apply))
    assert cli.main(["reload", APP, "--apply", "--interval", "0"]) == 1
    assert "boom" in capsys.readouterr().out


def test_cli_rejects_something_that_is_neither_id_nor_flow(monkeypatch, capsys):
    r = FakeRunner({("GET", "v1/items"): {"data": []}})  # sin la app: ni id ni nombre
    monkeypatch.setattr(cli, "make_bridge", lambda apply: Bridge(runner=r, apply=apply))
    assert cli.main(["reload", "no/existe", "--apply"]) == 1
    assert "ni id de app ni flujo" in capsys.readouterr().out


# ----- MCP -----
def test_mcp_reload_needs_confirm(tmp_path):
    srv = mcp.Server(tools=mcp.Tools(), env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    resp = srv.call("dfemu_flow_reload", {"flow": "emu_x"})
    assert resp["isError"] and "confirm=true" in resp["content"][0]["text"]


def test_mcp_reload_only_touches_emu_flows(tmp_path):
    r = runner(["SUCCEEDED"])
    r.routes[("GET", "v1/items")] = {"data": [{"resourceType": "app", "resourceSubType": "dataflow-prep",
                                               "spaceId": SANDBOX_SPACE_ID, "name": "real", "resourceAttributes": {"id": APP}}]}
    tools = mcp.Tools(bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    srv = mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    resp = srv.call("dfemu_flow_reload", {"flow": "real", "confirm": True})
    assert resp["isError"] and "emu_" in resp["content"][0]["text"]
    assert not [c for c in r.calls if c[0] == "POST"]
