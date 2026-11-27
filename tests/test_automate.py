"""`dfemu automate`: CRUD de Qlik Automate por API, con las reglas del Bridge."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import automate, cli  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge, SafetyError  # noqa: E402
from fakes import FakeRunner  # noqa: E402

A = "b" * 24
BASE = "workflows/automations"


def emu_routes(extra=None):
    routes = {
        ("GET", BASE): [{"id": A, "name": "emu_demo", "spaceId": SANDBOX_SPACE_ID}],
        ("GET", f"{BASE}/{A}"): {"id": A, "name": "emu_demo", "spaceId": SANDBOX_SPACE_ID},
        ("POST", BASE): {"id": A, "name": "emu_demo", "spaceId": SANDBOX_SPACE_ID},
    }
    routes.update(extra or {})
    return routes


def test_ls_lists_automations():
    b = Bridge(runner=FakeRunner(emu_routes()))
    assert automate.ls(b) == [{"id": A, "name": "emu_demo", "spaceId": SANDBOX_SPACE_ID}]


def test_show_reads_one_automation():
    b = Bridge(runner=FakeRunner(emu_routes()))
    assert automate.show(b, A)["name"] == "emu_demo"


def test_new_requires_the_emu_prefix():
    b = Bridge(runner=FakeRunner(emu_routes()), apply=True)
    with pytest.raises(SafetyError):
        automate.new(b, "demo_sin_prefijo")
    assert automate.new(b, "emu_nueva")["id"] == A


def test_new_sends_name_and_space():
    r = FakeRunner(emu_routes())
    automate.new(Bridge(runner=r, apply=True), "emu_nueva")
    body = [c for c in r.calls if c[0] == "POST"][-1][2]
    assert body["name"] == "emu_nueva"
    assert body["spaceId"]  # sale del entorno (espacio de pruebas)


def test_rm_refuses_an_automation_that_is_not_emu():
    r = FakeRunner(emu_routes({("GET", f"{BASE}/C"): {"id": "C", "name": "produccion", "spaceId": SANDBOX_SPACE_ID}}))
    with pytest.raises(SafetyError):
        automate.rm(Bridge(runner=r, apply=True), "C")
    assert ("DELETE", f"{BASE}/C", None) not in r.calls


def test_rm_deletes_an_emu_automation():
    r = FakeRunner(emu_routes({("DELETE", f"{BASE}/{A}"): {}}))
    automate.rm(Bridge(runner=r, apply=True), A)
    assert ("DELETE", f"{BASE}/{A}", None) in r.calls


def test_enable_and_disable_post_their_action():
    r = FakeRunner(emu_routes({("POST", f"{BASE}/{A}/actions/enable"): {}, ("POST", f"{BASE}/{A}/actions/disable"): {}}))
    b = Bridge(runner=r, apply=True)
    automate.enable(b, A)
    automate.disable(b, A)
    paths = [c[1] for c in r.calls if c[0] == "POST"]
    assert f"{BASE}/{A}/actions/enable" in paths
    assert f"{BASE}/{A}/actions/disable" in paths


def test_run_and_runs_use_the_runs_routes():
    r = FakeRunner(emu_routes({
        ("POST", f"{BASE}/{A}/runs"): {"id": "run-1"},
        ("GET", f"{BASE}/{A}/runs"): [{"id": "run-1"}],
    }))
    b = Bridge(runner=r, apply=True)
    assert automate.run(b, A)["id"] == "run-1"
    body = [c for c in r.calls if c[0] == "POST" and c[1].endswith("/runs")][-1][2]
    assert body == {"context": "api"}  # obligatorio para el servidor
    assert automate.runs(b, A) == [{"id": "run-1"}]


def test_copy_sends_the_new_name_and_space():
    r = FakeRunner(emu_routes({("POST", f"{BASE}/{A}/actions/copy"): {"id": "D"}}))
    automate.copy(Bridge(runner=r, apply=True), A, "emu_copia")
    body = [c for c in r.calls if c[0] == "POST" and c[1].endswith("/copy")][-1][2]
    assert body == {"name": "emu_copia", "spaceId": SANDBOX_SPACE_ID}


def test_writes_simulate_without_apply():
    r = FakeRunner(emu_routes({("DELETE", f"{BASE}/{A}"): {}}))
    with pytest.raises(Exception) as exc:
        automate.rm(Bridge(runner=r, apply=False), A)
    assert exc.type.__name__ == "DryRun"
    assert ("DELETE", f"{BASE}/{A}", None) not in r.calls


def test_cli_automate_ls_prints_names(monkeypatch, capsys):
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=FakeRunner(emu_routes())))
    cli.main(["automate", "ls"])
    out = capsys.readouterr().out
    assert "emu_demo" in out and A in out


def test_cli_automate_rm_requires_apply(monkeypatch, capsys):
    r = FakeRunner(emu_routes({("DELETE", f"{BASE}/{A}"): {}}))
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=r, apply=False))
    cli.main(["automate", "rm", A])
    assert "simulación" in capsys.readouterr().out
    assert ("DELETE", f"{BASE}/{A}", None) not in r.calls


def test_cli_automate_run_applies(monkeypatch, capsys):
    r = FakeRunner(emu_routes({("POST", f"{BASE}/{A}/runs"): {"id": "run-9"}}))
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=r, apply=True))
    cli.main(["automate", "run", A, "--apply"])
    assert "run-9" in capsys.readouterr().out
