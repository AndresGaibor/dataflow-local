import json
import os
import subprocess
import sys
from types import SimpleNamespace

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import bridge as B  # noqa: E402
from emulator.bridge import Bridge, BridgeError, DryRun, SafetyError  # noqa: E402
from fakes import FakeRunner  # noqa: E402

SB = "000000000000000000000000"
OTRO = "otro_espacio"


def make(routes, tmp_path, apply=False):
    runner = FakeRunner(routes)
    return Bridge(runner=runner, apply=apply, audit_path=str(tmp_path / "audit.jsonl")), runner


def writes(runner):
    return [c for c in runner.calls if c[0] in ("POST", "PUT", "DELETE") or c[1] == "app script set"]


def test_get_decodes_json(tmp_path):
    b, _ = make({("GET", "v1/x"): {"a": 1}}, tmp_path)
    assert b.get("v1/x") == {"a": 1}


def test_get_passes_each_query_as_own_arg(tmp_path):
    seen = []

    def runner(args):
        seen.append(args)
        return 0, "{}", ""

    Bridge(runner=runner, audit_path=str(tmp_path / "a.jsonl")).get("v1/x", {"k": "v", "n": "2"})
    assert seen[0] == ["raw", "get", "v1/x", "--query", "k=v", "--query", "n=2"]


def test_empty_stdout_returns_none(tmp_path):
    b, _ = make({("GET", "v1/x"): (0, "", "")}, tmp_path)
    assert b.get("v1/x") is None


def test_nonzero_exit_raises_bridgeerror(tmp_path):
    b, _ = make({("GET", "v1/x"): (1, "", "boom")}, tmp_path)
    with pytest.raises(BridgeError) as e:
        b.get("v1/x")
    assert e.value.stderr == "boom"
    assert e.value.rc == 1


def test_non_json_stdout_raises_bridgeerror(tmp_path):
    b, _ = make({("GET", "v1/x"): (0, "no json", "")}, tmp_path)
    with pytest.raises(BridgeError):
        b.get("v1/x")


def test_dry_run_raises_dryrun_and_calls_nothing(tmp_path):
    routes = {("POST", "v1/dataflow-apps/X/actions/copy"): {}}
    b, runner = make(routes, tmp_path, apply=False)
    body = {"name": "emu_copia", "spaceId": SB}
    with pytest.raises(DryRun) as e:
        b.post("v1/dataflow-apps/X/actions/copy", body)
    assert e.value.body == body
    assert not [c for c in runner.calls if c[0] == "POST"]
    line = json.loads((tmp_path / "audit.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert line["applied"] is False


def test_copy_outside_sandbox_rejected(tmp_path):
    routes = {("POST", "v1/dataflow-apps/X/actions/copy"): {}}
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/dataflow-apps/X/actions/copy", {"name": "emu_x", "spaceId": OTRO})
    assert not writes(runner)


def test_copy_name_without_prefix_rejected(tmp_path):
    routes = {("POST", "v1/dataflow-apps/X/actions/copy"): {}}
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/dataflow-apps/X/actions/copy", {"name": "fundamentos", "spaceId": SB})
    assert not writes(runner)


def test_copy_requires_post_method(tmp_path):
    routes = {("PUT", "v1/dataflow-apps/X/actions/copy"): {}}
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.put("v1/dataflow-apps/X/actions/copy", {"name": "emu_x", "spaceId": SB})
    assert not writes(runner)


def test_put_dataflow_requires_emu_owner(tmp_path):
    routes = {
        ("GET", "v1/dataflows/DF"): {"context": {"dataAppId": "A"}},
        ("GET", "v1/apps/A"): {"attributes": {"name": "fundamentos", "spaceId": SB}},
        ("PUT", "v1/dataflows/DF"): {"ok": True},
    }
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.put("v1/dataflows/DF", {"x": 1})
    assert not writes(runner)

    routes[("GET", "v1/apps/A")] = {"attributes": {"name": "emu_x", "spaceId": SB}}
    b, runner = make(routes, tmp_path, apply=True)
    assert b.put("v1/dataflows/DF", {"x": 1}) == {"ok": True}
    assert [c[:2] for c in writes(runner)] == [("PUT", "v1/dataflows/DF")]


@pytest.mark.parametrize("name, space, permitido", [
    ("emu_x", SB, True),
    ("fundamentos", SB, False),
    ("emu_x", OTRO, False),
])
def test_delete_app_requires_emu_in_sandbox(tmp_path, name, space, permitido):
    routes = {
        ("GET", "v1/apps/A"): {"attributes": {"name": name, "spaceId": space}},
        ("DELETE", "v1/apps/A"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    if permitido:
        b.delete("v1/apps/A")
        assert [c[:2] for c in writes(runner)] == [("DELETE", "v1/apps/A")]
    else:
        with pytest.raises(SafetyError):
            b.delete("v1/apps/A")
        assert not writes(runner)


def test_unknown_write_route_rejected(tmp_path):
    b, runner = make({("POST", "v1/spaces"): {}}, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/spaces", {"name": "emu_x"})
    assert not writes(runner)


def test_validatescript_allowed_in_dry_run(tmp_path):
    b, _ = make({("POST", "v1/apps/validatescript"): {"valid": True}}, tmp_path, apply=False)
    assert b.post("v1/apps/validatescript", {"script": "x"}) == {"valid": True}


def test_audit_line_written(tmp_path):
    routes = {("POST", "v1/dataflow-apps/X/actions/copy"): {"id": "Z"}}
    b, _ = make(routes, tmp_path, apply=True)
    assert b.post("v1/dataflow-apps/X/actions/copy", {"name": "emu_c", "spaceId": SB}) == {"id": "Z"}
    line = json.loads((tmp_path / "audit.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert set(line) == {"ts", "method", "path", "applied"}
    assert (line["method"], line["path"], line["applied"]) == ("POST", "v1/dataflow-apps/X/actions/copy", True)


def test_body_roundtrips_utf8(tmp_path):
    routes = {("POST", "v1/apps"): lambda body: body}
    b, _ = make(routes, tmp_path, apply=True)
    body = {"attributes": {"name": "emu_μ", "spaceId": SB}}
    assert b.post("v1/apps", body) == body


def test_script_set_requires_emu_app(tmp_path):
    routes = {
        ("GET", "v1/apps/A"): {"attributes": {"name": "fundamentos", "spaceId": SB}},
        ("CLI", "app script set"): (0, "", ""),
    }
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.script_set("A", "SELECT 1;")
    assert not writes(runner)

    routes[("GET", "v1/apps/A")] = {"attributes": {"name": "emu_x", "spaceId": SB}}
    b, runner = make(routes, tmp_path, apply=True)
    b.script_set("A", "SELECT 1; -- μ")
    assert ("CLI", "app script set", "SELECT 1; -- μ") in runner.calls


def test_cli_read_rejects_other_commands(tmp_path):
    routes = {("CLI", "app tables"): "T1\nT2", ("CLI", "app eval"): "42"}
    b, runner = make(routes, tmp_path)
    with pytest.raises(SafetyError):
        b.cli_read(["app", "script", "get", "A"])
    assert b.cli_read(["app", "tables", "--app", "A"]) == "T1\nT2"
    assert b.cli_read(["app", "eval", "--app", "A", "1+1", "--json"]) == "42"


def test_qlik_runner_closes_stdin_and_sets_timeout(monkeypatch):
    seen = {}

    def fake_run(cmd, **kwargs):
        seen["cmd"] = cmd
        seen.update(kwargs)
        return SimpleNamespace(returncode=0, stdout="{}", stderr="")

    monkeypatch.setattr(B.subprocess, "run", fake_run)
    monkeypatch.setattr(B, "_qlik_exe", lambda: "qlik")
    assert B.qlik_runner(["raw", "get", "v1/x"]) == (0, "{}", "")
    assert seen["cmd"][0] == "qlik"
    assert seen["stdin"] is subprocess.DEVNULL
    assert seen["timeout"] == 60


@pytest.mark.parametrize("exc, rc", [
    (subprocess.TimeoutExpired(["qlik"], 60), 124),
    (FileNotFoundError("qlik"), 127),
    (OSError(4551, "bloqueado por la politica de control de aplicaciones"), 126),
])
def test_qlik_runner_exceptions_become_bridgeerror(monkeypatch, tmp_path, exc, rc):
    def boom(cmd, **kwargs):
        raise exc

    monkeypatch.setattr(B.subprocess, "run", boom)
    b = Bridge(runner=B.qlik_runner, audit_path=str(tmp_path / "a.jsonl"))
    with pytest.raises(BridgeError) as e:
        b.get("v1/x")
    assert e.value.rc == rc


def test_qlik_exe_resolution(monkeypatch, tmp_path):
    real = tmp_path / "lib" / "qlik-cli" / "tools" / "qlik.exe"
    monkeypatch.delenv("DFEMU_QLIK", raising=False)
    monkeypatch.setenv("ChocolateyInstall", str(tmp_path))
    assert B._qlik_exe() == "qlik"  # sin binario real: el del PATH
    real.parent.mkdir(parents=True)
    real.write_bytes(b"")
    assert B._qlik_exe() == str(real)  # el firmado gana al acceso directo
    monkeypatch.setenv("DFEMU_QLIK", "C:/otro/qlik.exe")
    assert B._qlik_exe() == "C:/otro/qlik.exe"  # el override gana a todo


def test_reload_of_non_emu_app_rejected(tmp_path):
    routes = {
        ("GET", "v1/apps/A"): {"attributes": {"name": "fundamentos", "spaceId": SB}},
        ("POST", "v1/reloads"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/reloads", {"appId": "A"})
    assert not writes(runner)


def test_data_files_delete_rejects_when_one_id_not_emu(tmp_path):
    routes = {
        ("GET", "v1/data-files/d1"): {"name": "emu_a", "spaceId": SB},
        ("GET", "v1/data-files/d2"): {"name": "fundamentos", "spaceId": SB},
        ("POST", "v1/data-files/actions/delete"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/data-files/actions/delete", {"delete": [{"id": "d1"}, {"id": "d2"}]})
    assert not writes(runner)


def test_data_files_delete_accepts_dict_items_only(tmp_path):
    routes = {
        ("GET", "v1/data-files/d1"): {"name": "emu_a", "spaceId": SB},
        ("POST", "v1/data-files/actions/delete"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    b.post("v1/data-files/actions/delete", {"delete": [{"id": "d1"}]})
    assert [c[:2] for c in writes(runner)] == [("POST", "v1/data-files/actions/delete")]

    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/data-files/actions/delete", {"delete": ["d1"]})  # cadena suelta: rechazada
    assert not writes(runner)


def test_reload_cancel_allowed_only_for_emu_app(tmp_path):
    routes = {
        ("GET", "v1/reloads/R1"): {"appId": "A"},
        ("GET", "v1/apps/A"): {"attributes": {"name": "emu_oracle_t", "spaceId": SB}},
        ("POST", "v1/reloads/R1/actions/cancel"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    b.post("v1/reloads/R1/actions/cancel")
    assert [c[:2] for c in writes(runner)] == [("POST", "v1/reloads/R1/actions/cancel")]

    routes[("GET", "v1/apps/A")] = {"attributes": {"name": "fundamentos", "spaceId": SB}}
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/reloads/R1/actions/cancel")
    assert not writes(runner)


def test_script_set_writes_crlf_bytes_unchanged(tmp_path):
    class BytesRunner(FakeRunner):
        seen = []

        def __call__(self, args):
            if args[:3] == ["app", "script", "set"]:
                with open(args[3], "rb") as f:  # lee el archivo tal como está en disco
                    self.seen.append(f.read())
            return super().__call__(args)

    runner = BytesRunner({("GET", "v1/apps/A"): {"attributes": {"name": "emu_x", "spaceId": SB}},
                          ("CLI", "app script set"): ""})
    b = Bridge(runner=runner, apply=True, audit_path=str(tmp_path / "audit.jsonl"))
    b.script_set("A", "LOAD 1;\r\nLOAD 2;\r\n")
    assert runner.seen == [b"LOAD 1;\r\nLOAD 2;\r\n"]


def test_app_create_outside_sandbox_space_rejected(tmp_path):
    b, runner = make({("POST", "v1/apps"): {}}, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/apps", {"attributes": {"name": "emu_x", "spaceId": OTRO}})
    assert not writes(runner)


def test_empty_owner_id_rejected_without_lookup(tmp_path):
    routes = {
        ("GET", "v1/dataflows/DF"): {"context": {"dataAppId": ""}},
        ("PUT", "v1/dataflows/DF"): {},
    }
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.put("v1/dataflows/DF", {"x": 1})
    assert not [c for c in runner.calls if c[1].startswith("v1/apps/")]


def test_script_set_empty_app_id_rejected_without_lookup(tmp_path):
    b, runner = make({}, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.script_set("", "SELECT 1;")
    assert runner.calls == []


def test_ids_with_slash_rejected_before_lookup(tmp_path):
    b, runner = make({}, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.script_set("a/b", "SELECT 1;")
    assert runner.calls == []

    routes = {("GET", "v1/dataflows/DF"): {"context": {"dataAppId": "a/b"}}, ("PUT", "v1/dataflows/DF"): {}}
    b, runner = make(routes, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.put("v1/dataflows/DF", {"x": 1})
    assert [c[:2] for c in runner.calls] == [("GET", "v1/dataflows/DF")]

    b, runner = make({}, tmp_path, apply=True)
    with pytest.raises(SafetyError):
        b.post("v1/data-files/actions/delete", {"delete": [{"id": "ok/x"}]})
    assert runner.calls == []


# --- tareas programadas (scheduling) -------------------------------------------

EMU = {"attributes": {"name": "emu_x", "spaceId": SB}}
REAL = {"attributes": {"name": "fundamentos", "spaceId": SB}}
SAFE = "LOAD [a] FROM [lib://c/a.csv] (txt);\nSTORE [T] INTO [lib://c:GDDestino/emu_t.csv] (txt);\nDROP TABLE [T];"
UNSAFE = SAFE.replace("emu_t.csv", "clientes.csv")


def _sched(tmp_path, app, extra=None):
    routes = {("GET", "v1/apps/A"): app, ("GET", "v1/apps/B"): REAL,
              ("GET", "scheduling/tasks/T1"): {"resourceId": "A"}, ("GET", "scheduling/tasks/T2"): {"resourceId": "B"},
              ("GET", "v1/apps/A/scripts/current"): {"script": SAFE},
              ("POST", "scheduling/tasks/resources/A/actions/reload/on-time-schedule"): {"id": "T9"},
              ("POST", "scheduling/tasks/resources/A/actions/reload/on-task-event"): {"id": "T9"},
              ("POST", "scheduling/tasks/T1/actions/start"): {}, ("DELETE", "scheduling/tasks/T1"): {},
              ("POST", "scheduling/tasks/T2/actions/start"): {}, ("DELETE", "scheduling/tasks/T2"): {}, **(extra or {})}
    return make(routes, tmp_path, apply=True)


SCHED = "scheduling/tasks/resources/A/actions/reload/on-time-schedule"
CHAIN = "scheduling/tasks/resources/A/actions/reload/on-task-event"


def test_schedule_allowed_only_for_emu_app(tmp_path):
    b, runner = _sched(tmp_path, EMU)
    b.post(SCHED, {"name": "n", "recurrence": "RRULE:FREQ=DAILY"})
    assert len(writes(runner)) == 1
    b, runner = _sched(tmp_path, REAL)
    with pytest.raises(SafetyError):
        b.post(SCHED, {"name": "n", "recurrence": "RRULE:FREQ=DAILY"})
    assert not writes(runner)


def test_chain_requires_emu_upstream_task(tmp_path):
    b, _ = _sched(tmp_path, EMU)
    b.post(CHAIN, {"name": "n", "onTaskId": "T1"})
    with pytest.raises(SafetyError):  # la tarea previa es de una app que no es emu_
        b.post(CHAIN, {"name": "n", "onTaskId": "T2"})
    with pytest.raises(SafetyError):
        b.post(CHAIN, {"name": "n"})


def test_start_requires_emu_app_and_emu_store_targets(tmp_path):
    b, runner = _sched(tmp_path, EMU)
    b.post("scheduling/tasks/T1/actions/start", None)
    with pytest.raises(SafetyError):  # la app de T2 no es emu_
        b.post("scheduling/tasks/T2/actions/start", None)
    b, runner = _sched(tmp_path, EMU, {("GET", "v1/apps/A/scripts/current"): {"script": UNSAFE}})
    with pytest.raises(SafetyError, match="STORE"):  # escribiria en un archivo que no es emu_
        b.post("scheduling/tasks/T1/actions/start", None)
    assert not writes(runner)


@pytest.mark.parametrize("script", ["IF 1 THEN STORE [T] INTO [lib://c/clientes.csv] (txt); END IF", "STORE T INTO x;"])
def test_start_rejects_store_it_cannot_read(tmp_path, script):
    b, _ = _sched(tmp_path, EMU, {("GET", "v1/apps/A/scripts/current"): {"script": script}})
    with pytest.raises(SafetyError):
        b.post("scheduling/tasks/T1/actions/start", None)


def test_delete_task_only_for_emu_app(tmp_path):
    b, _ = _sched(tmp_path, EMU)
    b.delete("scheduling/tasks/T1")
    with pytest.raises(SafetyError):
        b.delete("scheduling/tasks/T2")
