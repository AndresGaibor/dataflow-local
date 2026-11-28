"""MCP: recursos, prompts, progreso y las herramientas de diagnostico."""
import io
import json
import os
import sys
import types

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import mcp  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge  # noqa: E402
from fakes import FakeRunner  # noqa: E402

A = "b" * 24


def srv(tmp_path, env=None):
    return mcp.Server(tools=mcp.Tools(root=mcp._root()), env={"DFEMU_MCP_STATE_DIR": str(tmp_path)} | (env or {}),
                      state_dir=tmp_path)


# ----- capacidades y recursos -----
def test_initialize_declara_recursos_y_prompts():
    caps = mcp.Server(tools=mcp.Tools(), env={}).handle(
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})["result"]["capabilities"]
    assert caps["tools"] == {"listChanged": False}
    assert caps["resources"] == {"listChanged": False} and caps["prompts"] == {"listChanged": False}


def test_resources_apuntan_a_archivos_que_existen():
    for _uri, _name, path in mcp.RESOURCES:
        assert (mcp._root() / path).exists(), path


def test_resources_list_y_read(tmp_path):
    s = srv(tmp_path)
    uris = [r["uri"] for r in s.handle({"jsonrpc": "2.0", "id": 2, "method": "resources/list"})["result"]["resources"]]
    assert "dfemu://docs/mcp" in uris and "dfemu://skill/dfemu" in uris
    out = s.handle({"jsonrpc": "2.0", "id": 3, "method": "resources/read", "params": {"uri": "dfemu://docs/mcp"}})
    assert "dfemu_guide" in out["result"]["contents"][0]["text"]
    assert out["result"]["contents"][0]["mimeType"] == "text/markdown"


def test_resources_read_rechaza_lo_que_no_conoce(tmp_path):
    s = srv(tmp_path)
    out = s.handle({"jsonrpc": "2.0", "id": 4, "method": "resources/read", "params": {"uri": "dfemu://no"}})
    assert out["error"]["code"] == -32602


def test_resources_read_trunca_archivos_grandes(tmp_path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "grande.md").write_text("x" * (mcp.MAX_RESOURCE + 100), encoding="utf-8")
    tools = mcp.Tools(root=tmp_path)
    s = mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    original = mcp.RESOURCES
    mcp.RESOURCES = [("dfemu://grande", "grande", "docs/grande.md")]
    try:
        out = s.handle({"jsonrpc": "2.0", "id": 5, "method": "resources/read", "params": {"uri": "dfemu://grande"}})
        assert len(out["result"]["contents"][0]["text"]) == mcp.MAX_RESOURCE
    finally:
        mcp.RESOURCES = original


# ----- prompts -----
def test_prompts_list_y_get(tmp_path):
    s = srv(tmp_path)
    nombres = [p["name"] for p in s.handle({"jsonrpc": "2.0", "id": 6, "method": "prompts/list"})["result"]["prompts"]]
    assert set(nombres) == set(mcp.PROMPTS)
    out = s.handle({"jsonrpc": "2.0", "id": 7, "method": "prompts/get",
                    "params": {"name": "crear-dataflow", "arguments": {"objetivo": "filtrar ventas"}}})
    texto = out["result"]["messages"][0]["content"]["text"]
    assert "filtrar ventas" in texto and "dfemu_flow_clone" in texto and "dfemu_flow_reload" in texto


def test_prompts_dicen_la_verdad_sobre_lo_que_no_se_puede_por_api(tmp_path):
    s = srv(tmp_path)
    out = s.handle({"jsonrpc": "2.0", "id": 8, "method": "prompts/get",
                    "params": {"name": "capturar-interfaz", "arguments": {}}})
    texto = out["result"]["messages"][0]["content"]["text"]
    assert "dfemu flow capture start" in texto and "pivot" in texto


def test_prompts_get_desconocido_falla(tmp_path):
    out = srv(tmp_path).handle({"jsonrpc": "2.0", "id": 9, "method": "prompts/get", "params": {"name": "no"}})
    assert out["error"]["code"] == -32602


# ----- progreso -----
def _servidor_con_progreso(tmp_path):
    s = srv(tmp_path)

    def falso(**kw):
        s.tools._progress("paso 1")
        s.tools._progress("paso 2")
        return "hecho"

    mcp.REGISTRY.setdefault("dfemu_progress_test", ("read", "prueba", mcp._schema({}), "falso"))
    setattr(s.tools, "falso", falso)
    return s


def test_serve_emite_notificaciones_de_progreso(tmp_path):
    s = _servidor_con_progreso(tmp_path)
    fin = io.StringIO(json.dumps({"jsonrpc": "2.0", "id": 10, "method": "tools/call",
                                  "params": {"name": "dfemu_progress_test", "arguments": {},
                                             "_meta": {"progressToken": "tok-1"}}}) + "\n")
    fout = io.StringIO()
    try:
        s.serve(stdin=fin, stdout=fout)
    finally:
        mcp.REGISTRY.pop("dfemu_progress_test", None)
    lineas = [json.loads(x) for x in fout.getvalue().splitlines()]
    avisos = [x for x in lineas if x.get("method") == "notifications/progress"]
    assert [a["params"]["message"] for a in avisos] == ["paso 1", "paso 2"]
    assert all(a["params"]["progressToken"] == "tok-1" for a in avisos)
    assert lineas[-1]["result"]["content"][0]["text"] == "hecho"


def test_sin_token_no_hay_notificaciones(tmp_path):
    s = _servidor_con_progreso(tmp_path)
    fin = io.StringIO(json.dumps({"jsonrpc": "2.0", "id": 11, "method": "tools/call",
                                  "params": {"name": "dfemu_progress_test", "arguments": {}}}) + "\n")
    fout = io.StringIO()
    try:
        s.serve(stdin=fin, stdout=fout)
    finally:
        mcp.REGISTRY.pop("dfemu_progress_test", None)
    assert "notifications/progress" not in fout.getvalue()


# ----- automation_run espera -----
def _auto_bridge(estados):
    seq = list(estados)

    def siguiente(body=None):
        return {"data": [{"id": "r" * 24, "status": seq.pop(0) if len(seq) > 1 else seq[0]}]}

    r = FakeRunner({
        ("GET", f"workflows/automations/{A}"): {"id": A, "name": "emu_x", "spaceId": SANDBOX_SPACE_ID},
        ("POST", f"workflows/automations/{A}/runs"): {"id": "r" * 24, "status": "started"},
        ("GET", f"workflows/automations/{A}/runs"): siguiente,
    })
    tools = mcp.Tools(bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    return mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": "out/test-state"}), r


def test_automation_run_sigue_el_estado_hasta_el_final(tmp_path):
    s, _r = _auto_bridge(["running", "finished"])
    s.tools.root = mcp._root()
    out = s.call("dfemu_automation_run", {"automation": A, "confirm": True})["content"][0]["text"]
    assert "running" in out and "finished" in out


def test_automation_run_puede_no_esperar(tmp_path):
    s, _r = _auto_bridge(["running"])
    out = s.call("dfemu_automation_run", {"automation": A, "confirm": True, "wait": False})["content"][0]["text"]
    assert "lanzada" in out


# ----- herramientas de diagnostico -----
def test_coverage_corre_el_emulador_sobre_los_samples(tmp_path):
    out = srv(tmp_path).call("dfemu_coverage", {})["content"][0]["text"]
    assert "flujos:" in out and "ejecuta=" in out


def test_docs_check_usa_el_script_y_resume(tmp_path, monkeypatch):
    class Hecho:
        returncode = 0
        stdout = "2964/2964 paginas; 0 imagenes rotas\n"
        stderr = ""

    import subprocess

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: Hecho())
    out = srv(tmp_path).call("dfemu_docs_check", {})["content"][0]["text"]
    assert out.startswith("ok:") and "2964/2964" in out


def test_compare_exige_confirmacion(tmp_path):
    resp = srv(tmp_path).call("dfemu_compare", {"file": "samples/fundamentos_filtro_basico.dfw"})
    assert resp["isError"] and "confirm=true" in resp["content"][0]["text"]
