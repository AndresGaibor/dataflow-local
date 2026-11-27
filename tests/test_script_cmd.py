"""Comando `dfemu script`: leer, escribir y validar el script de una app emu_."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import cli  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge, SafetyError  # noqa: E402
from fakes import FakeRunner  # noqa: E402

APP = "a" * 24
SCRIPT = "SET ThousandSep=',';\n[Ordenes]: LOAD 1 as x;\n"


def test_script_get_reads_the_current_script():
    r = FakeRunner({("GET", f"v1/apps/{APP}/scripts/current"): {"script": SCRIPT}})
    assert Bridge(runner=r).script_get(APP) == SCRIPT


def test_script_get_rejects_an_invalid_id_without_calling_qlik():
    r = FakeRunner({})
    with pytest.raises(SafetyError):
        Bridge(runner=r).script_get("a/b")
    assert r.calls == []


def test_script_validate_returns_the_server_errors():
    r = FakeRunner({("POST", "v1/apps/validatescript"): {"Errors": ["Invalid expression"]}})
    assert Bridge(runner=r).script_validate("LOAD ;") == ["Invalid expression"]


def test_script_validate_without_errors_is_empty():
    r = FakeRunner({("POST", "v1/apps/validatescript"): {}})
    assert Bridge(runner=r).script_validate("LOAD 1 as x;") == []


def test_cli_script_get_prints_the_script(monkeypatch, capsys):
    b = Bridge(runner=FakeRunner({("GET", f"v1/apps/{APP}/scripts/current"): {"script": SCRIPT}}))
    monkeypatch.setattr(cli, "make_bridge", lambda ap: b)
    cli.main(["script", "get", APP])
    assert capsys.readouterr().out == SCRIPT


def test_cli_script_set_simulates_without_apply(monkeypatch, tmp_path, capsys):
    qvs = tmp_path / "a.qvs"
    qvs.write_text(SCRIPT, encoding="utf-8")
    r = FakeRunner({("GET", f"v1/apps/{APP}"): {"attributes": {"name": "emu_prueba", "spaceId": SANDBOX_SPACE_ID}}})
    b = Bridge(runner=r, apply=False)
    monkeypatch.setattr(cli, "make_bridge", lambda ap: b)
    cli.main(["script", "set", APP, str(qvs)])  # sin --apply solo simula
    assert "simulación" in capsys.readouterr().out
    assert ("CLI", "app script set", None) not in r.calls  # no se escribio nada


def test_cli_script_set_applies_the_file(monkeypatch, tmp_path):
    qvs = tmp_path / "a.qvs"
    qvs.write_text(SCRIPT, encoding="utf-8")
    r = FakeRunner({
        ("GET", f"v1/apps/{APP}"): {"attributes": {"name": "emu_prueba", "spaceId": SANDBOX_SPACE_ID}},
        ("CLI", "app script set"): "",
    })
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=r, apply=True))
    cli.main(["script", "set", APP, str(qvs)])
    assert ("CLI", "app script set", SCRIPT) in r.calls


def test_cli_script_validate_says_ok(monkeypatch, tmp_path, capsys):
    qvs = tmp_path / "a.qvs"
    qvs.write_text("LOAD 1 as x;", encoding="utf-8")
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=FakeRunner({("POST", "v1/apps/validatescript"): {}})))
    cli.main(["script", "validate", str(qvs)])
    assert "OK" in capsys.readouterr().out


def test_cli_script_validate_lists_errors_and_fails(monkeypatch, tmp_path, capsys):
    qvs = tmp_path / "a.qvs"
    qvs.write_text("LOAD ;", encoding="utf-8")
    monkeypatch.setattr(cli, "make_bridge", lambda ap: Bridge(runner=FakeRunner({("POST", "v1/apps/validatescript"): {"Errors": ["Invalid expression"]}})))
    with pytest.raises(SystemExit) as exc:
        cli.main(["script", "validate", str(qvs)])
    assert "Invalid expression" in str(exc.value)
