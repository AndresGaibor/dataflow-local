"""dfemu setup: instalacion de la CLI, contexto con API key y espacio de pruebas (todo simulado)."""
import hashlib
import io
import json
import zipfile

import pytest

from emulator import setup as S


def make_zip(member="qlik.exe", data=b"BIN"):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr(f"qlik-Windows-x86_64/{member}", data)
    return buf.getvalue()


def fake_download(zip_bytes, sha=None):
    sums = f"{sha or hashlib.sha256(zip_bytes).hexdigest()}  qlik-Windows-x86_64.zip\n"

    def dl(url):
        return sums.encode() if url.endswith("checksums.txt") else zip_bytes
    return dl


@pytest.fixture
def tools(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "TOOLS_DIR", str(tmp_path / "bin"))
    monkeypatch.setattr(S, "CLI_FILE", str(tmp_path / "bin" / "qlik.exe"))
    monkeypatch.setattr(S, "LOCAL_CONFIG", str(tmp_path / "local.json"))
    for k in ("DFEMU_SPACE_ID", "DFEMU_BASE_APP"):  # setenv+delenv: al terminar se restaura el estado original
        monkeypatch.setenv(k, "x")
        monkeypatch.delenv(k)
    return tmp_path


@pytest.mark.parametrize("system,machine,name", [
    ("Windows", "AMD64", "qlik-Windows-x86_64.zip"),
    ("Linux", "x86_64", "qlik-Linux-x86_64.tar.gz"),
    ("Darwin", "arm64", "qlik-Darwin-x86_64.tar.gz"),
])
def test_asset_name(system, machine, name):
    assert S.asset_name(system, machine) == name


@pytest.mark.parametrize("system,machine", [("Linux", "aarch64"), ("FreeBSD", "x86_64"), ("Windows", "arm64")])
def test_asset_name_unsupported(system, machine):
    with pytest.raises(S.SetupError):
        S.asset_name(system, machine)


def test_install_cli_verifies_and_extracts(tools):
    path = S.install_cli(fake_download(make_zip()), "Windows", "AMD64")
    assert path == S.CLI_FILE and open(path, "rb").read() == b"BIN"


def test_install_cli_rejects_bad_checksum(tools):
    with pytest.raises(S.SetupError, match="SHA-256"):
        S.install_cli(fake_download(make_zip(), sha="0" * 64), "Windows", "AMD64")
    assert not (tools / "bin" / "qlik.exe").exists()


def test_install_cli_without_binary_in_archive(tools):
    with pytest.raises(S.SetupError, match="no esta dentro"):
        S.install_cli(fake_download(make_zip(member="otro.txt")), "Windows", "AMD64")


def test_download_refuses_plain_http():
    with pytest.raises(S.SetupError):
        S._download("http://ejemplo.com/x")


def runner_from(results):
    """results: lista de rc por llamada, en orden; registra los argumentos."""
    calls = []

    def run(args):
        calls.append(args)
        rc = results[len(calls) - 1] if len(calls) <= len(results) else 0
        return rc, "", "boom sk-SECRET" if rc else ""
    run.calls = calls
    return run


def test_ensure_cli_noop_when_it_works():
    assert "ok" in S.ensure_cli(runner=runner_from([0]), ask=lambda p: pytest.fail("no debe preguntar"))


def test_ensure_cli_declined():
    with pytest.raises(S.SetupError, match="sin la CLI"):
        S.ensure_cli(runner=runner_from([127]), ask=lambda p: "n", install=lambda: pytest.fail("no debe instalar"))


def test_ensure_cli_installs_then_checks():
    out = S.ensure_cli(runner=runner_from([127, 0]), ask=lambda p: "s", install=lambda: "/x/qlik")
    assert "/x/qlik" in out
    with pytest.raises(S.SetupError, match="no se puede ejecutar"):
        S.ensure_cli(runner=runner_from([127, 126]), install=lambda: "/x/qlik", assume_yes=True)


def test_ensure_context_noop_when_authenticated():
    r = runner_from([0])
    assert "ok" in S.ensure_context(r, ask=lambda p: pytest.fail("no debe preguntar"))
    assert r.calls == [S.PROBE]


def test_ensure_context_creates_with_key_and_never_echoes_it():
    answers = iter(["https://t1.us.qlikcloud.com/"])
    r = runner_from([1, 0, 0, 0])  # probe falla, create ok, use ok, probe ok
    msg = S.ensure_context(r, ask=lambda p: next(answers), secret=lambda p: "sk-SECRET")
    assert r.calls[1] == ["context", "create", "t1.us.qlikcloud.com", "--server", "https://t1.us.qlikcloud.com",
                          "--api-key", "sk-SECRET"]
    assert "sk-SECRET" not in msg and "t1.us.qlikcloud.com" in msg


def test_ensure_context_updates_existing_and_masks_key_in_errors():
    r = runner_from([1, 1, 1])  # probe, create y update fallan
    with pytest.raises(S.SetupError) as e:
        S.ensure_context(r, ask=lambda p: "https://t1.us.qlikcloud.com", secret=lambda p: "sk-SECRET")
    assert "sk-SECRET" not in str(e.value) and r.calls[2][1] == "update"


def test_ensure_context_rejects_http_url_and_empty_key():
    with pytest.raises(S.SetupError, match="https"):
        S.ensure_context(runner_from([1]), ask=lambda p: "http://t1", secret=lambda p: "k")
    with pytest.raises(S.SetupError, match="vacia"):
        S.ensure_context(runner_from([1]), ask=lambda p: "https://t1.us.qlikcloud.com", secret=lambda p: " ")


class FakeBridge:
    def get(self, path, params=None):
        if path == "v1/spaces":
            return [{"name": "Otro", "id": "S0"}, {"name": "Entrenamiento", "id": "S1"}]
        return {"data": [{"name": "base", "resourceId": "A1", "resourceSubType": "dataflow-prep", "spaceId": "S1"},
                         {"name": "ajeno", "resourceId": "A2", "resourceSubType": "dataflow-prep", "spaceId": "S0"}]}


def test_ensure_workspace_picks_and_saves(tools, monkeypatch):
    answers = iter(["2", "1"])
    S.ensure_workspace(FakeBridge(), ask=lambda p: next(answers))
    assert json.load(open(S.LOCAL_CONFIG)) == {"DFEMU_SPACE_ID": "S1", "DFEMU_BASE_APP": "A1"}


def test_ensure_workspace_uses_arguments_without_asking(tools, monkeypatch):
    S.ensure_workspace(FakeBridge(), ask=lambda p: pytest.fail("no debe preguntar"), space="S1", base_app="A1")
    assert json.load(open(S.LOCAL_CONFIG))["DFEMU_BASE_APP"] == "A1"


def test_ensure_workspace_invalid_choice(tools, monkeypatch):
    with pytest.raises(S.SetupError, match="invalida"):
        S.ensure_workspace(FakeBridge(), ask=lambda p: "9")


def test_ensure_workspace_ignores_a_stored_base_app_from_another_space(tools, monkeypatch):
    monkeypatch.setenv("DFEMU_SPACE_ID", "S0")
    monkeypatch.setenv("DFEMU_BASE_APP", "A-DE-S0")
    answers = iter(["1"])
    S.ensure_workspace(FakeBridge(), ask=lambda p: next(answers), space="S1")
    assert json.load(open(S.LOCAL_CONFIG)) == {"DFEMU_SPACE_ID": "S1", "DFEMU_BASE_APP": "A1"}  # no arrastra el de S0
