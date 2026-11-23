"""dfemu task: programar, encadenar, arrancar y borrar tareas de apps emu_ (con tenant simulado)."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli, tasks  # noqa: E402
from emulator.bridge import Bridge, SafetyError  # noqa: E402
from fakes import FakeRunner  # noqa: E402

SB = "000000000000000000000000"
SCRIPT = "STORE [T] INTO [lib://c:GDDestino/emu_t.csv] (txt);"
SCHED = "scheduling/tasks/resources/A/actions/reload/on-time-schedule"
CHAIN = "scheduling/tasks/resources/A/actions/reload/on-task-event"


def bridge(tmp_path, apply=True, extra=None):
    routes = {("GET", "v1/apps/A"): {"attributes": {"name": "emu_x", "spaceId": SB}},
              ("GET", "scheduling/tasks/T1"): {"resourceId": "A"},
              ("GET", "v1/apps/A/scripts/current"): {"script": SCRIPT},
              ("POST", SCHED): {"id": "T2", "enabled": False}, ("POST", CHAIN): {"id": "T3", "enabled": False},
              ("POST", "scheduling/tasks/T1/actions/start"): {"message": "OK"},
              ("DELETE", "scheduling/tasks/T1"): {}, **(extra or {})}
    runner = FakeRunner(routes)
    return Bridge(runner=runner, apply=apply, audit_path=str(tmp_path / "a.jsonl")), runner


def body_of(runner, path):
    return next(c[2] for c in runner.calls if c[1] == path)


def test_schedule_sends_the_rrule_and_creates_disabled_by_default(tmp_path):
    b, r = bridge(tmp_path)
    assert tasks.schedule(b, "A", "n", "RRULE:FREQ=DAILY;BYHOUR=3", "America/Bogota")["id"] == "T2"
    assert body_of(r, SCHED) == {"name": "n", "recurrence": "RRULE:FREQ=DAILY;BYHOUR=3",
                                 "timezone": "America/Bogota", "enabled": False}


def test_chain_sends_upstream_task_and_status(tmp_path):
    b, r = bridge(tmp_path)
    tasks.chain(b, "A", "n", "T1", "failed", enabled=True)
    assert body_of(r, CHAIN) == {"name": "n", "onTaskId": "T1", "onTaskStatus": "failed", "enabled": True}
    with pytest.raises(ValueError):
        tasks.chain(b, "A", "n", "T1", "casi")


def test_list_and_runs_accept_a_list_or_a_data_envelope(tmp_path):
    b, _ = bridge(tmp_path, extra={("GET", "scheduling/tasks"): [{"id": "T1"}],
                                   ("GET", "scheduling/tasks/T1/runs"): {"data": [{"status": "SUCCEEDED"}]}})
    assert tasks.list_tasks(b, "A") == [{"id": "T1"}]
    assert tasks.runs(b, "T1") == [{"status": "SUCCEEDED"}]


def test_ids_are_validated_before_building_paths(tmp_path):
    b, _ = bridge(tmp_path)
    with pytest.raises(SafetyError):
        tasks.schedule(b, "../x", "n", "RRULE:FREQ=DAILY")
    with pytest.raises(SafetyError):
        tasks.runs(b, "a/b")


def test_start_and_delete(tmp_path):
    b, _ = bridge(tmp_path)
    assert tasks.start(b, "T1")["message"] == "OK"
    tasks.delete(b, "T1")


def run_cli(tmp_path, monkeypatch, capsys, argv, apply=True, extra=None):
    b, runner = bridge(tmp_path, apply=apply, extra=extra)
    monkeypatch.setattr(cli, "make_bridge", lambda ap: b)
    with pytest.raises(SystemExit) as e:
        cli.main(argv)
    return e.value.code, capsys.readouterr().out, runner


def test_cli_schedule_dry_run_writes_nothing(tmp_path, monkeypatch, capsys):
    code, out, runner = run_cli(tmp_path, monkeypatch, capsys,
                                ["task", "schedule", "A", "--name", "n", "--recurrence", "RRULE:FREQ=DAILY"], apply=False)
    assert code == 0 and "[simulación]" in out
    assert not [c for c in runner.calls if c[0] == "POST"]


def test_cli_ls_and_start(tmp_path, monkeypatch, capsys):
    code, out, _ = run_cli(tmp_path, monkeypatch, capsys, ["task", "ls", "A"],
                           extra={("GET", "scheduling/tasks"): [{"id": "T1", "enabled": True, "name": "diaria"}]})
    assert code == 0 and "T1  habilitada  diaria" in out
    code, out, _ = run_cli(tmp_path, monkeypatch, capsys, ["task", "start", "T1", "--apply"])
    assert code == 0 and "OK" in out


def test_cli_start_refuses_a_task_that_would_overwrite_real_output(tmp_path, monkeypatch, capsys):
    unsafe = {("GET", "v1/apps/A/scripts/current"): {"script": SCRIPT.replace("emu_t", "clientes")}}
    code, out, runner = run_cli(tmp_path, monkeypatch, capsys, ["task", "start", "T1"], extra=unsafe)
    assert code == 1 and "STORE" in out
    assert not [c for c in runner.calls if c[0] == "POST"]
