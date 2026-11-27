"""Metadatos del CLI: `--version` y salida en UTF-8 aunque la consola sea cp1252."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import __version__  # noqa: E402
from emulator import cli  # noqa: E402


class _FakeStream:
    def __init__(self):
        self.calls = []

    def reconfigure(self, **kw):
        self.calls.append(kw)


def test_utf8_stdout_reconfigures_both_streams(monkeypatch):
    out, err = _FakeStream(), _FakeStream()
    monkeypatch.setattr(cli.sys, "stdout", out)
    monkeypatch.setattr(cli.sys, "stderr", err)
    cli.utf8_stdout()
    assert out.calls == [{"encoding": "utf-8", "errors": "replace"}]
    assert err.calls == [{"encoding": "utf-8", "errors": "replace"}]


def test_utf8_stdout_tolerates_streams_without_reconfigure(monkeypatch):
    class Plain:
        pass

    monkeypatch.setattr(cli.sys, "stdout", Plain())
    monkeypatch.setattr(cli.sys, "stderr", Plain())
    cli.utf8_stdout()  # no lanza


def test_version_flag_prints_the_package_version():
    p = subprocess.run([sys.executable, "-m", "emulator.cli", "--version"], cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0
    assert p.stdout.strip() == f"dfemu {__version__}"


def test_flow_types_survives_a_cp1252_console():
    """Con la consola en cp1252 la salida debe seguir siendo UTF-8 valido."""
    env = dict(os.environ, PYTHONIOENCODING="cp1252")
    p = subprocess.run([sys.executable, "-m", "emulator.cli", "flow", "types"], cwd=ROOT, capture_output=True, env=env)
    assert p.returncode == 0, p.stderr
    text = p.stdout.decode("utf-8")  # falla si se colo un byte cp1252
    assert "Unión" in text
    assert "Uni\ufffdb" not in text
