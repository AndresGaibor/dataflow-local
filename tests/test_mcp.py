"""Servidor MCP: protocolo, permisos por riesgo, limite emu_ y auditoria."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import mcp  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge  # noqa: E402
from fakes import FakeRunner  # noqa: E402

APP, NEW = "a" * 24, "b" * 24
DF, DF2 = "c" * 24, "d" * 24


def items(*names):
    return {"data": [{"resourceType": "app", "resourceSubType": "dataflow-prep", "spaceId": SANDBOX_SPACE_ID,
                      "resourceAttributes": {"id": APP if i == 0 else f"{i}" * 24}, "name": n}
                     for i, n in enumerate(names)]}


def routes(names=("emu_demo", "real_demo")):
    return {
        ("GET", "v1/items"): items(*names),
        ("GET", f"v1/dataflow-apps/{APP}"): {"dataflowId": DF},
        ("GET", f"v1/dataflows/{DF}"): {"graph": {"nodes": [
            {"label": "clientes", "component": {"type": "analyticsSource", "properties": {}}}]}},
        ("GET", f"v1/apps/{APP}/scripts/current"): {"script": "LOAD * Inline [a];"},
        ("POST", f"v1/dataflow-apps/{APP}/actions/copy"): {"id": NEW, "dataflowId": DF2},
        ("GET", f"v1/dataflows/{DF2}"): {"graph": {}, "validity": {}, "context": {"dataAppId": NEW}},
        ("PUT", f"v1/dataflows/{DF2}"): {"validity": {"status": "VALID", "nodesConstraintViolations": []}},
        ("GET", f"v1/apps/{NEW}/scripts/current"): {"script": "LOAD 1;"},
        ("GET", f"v1/apps/{NEW}"): {"attributes": {"name": "emu_prueba", "spaceId": SANDBOX_SPACE_ID}},
        ("GET", f"v1/apps/{APP}"): {"attributes": {"name": "emu_demo", "spaceId": SANDBOX_SPACE_ID}},
        ("DELETE", f"v1/apps/{NEW}"): {},
        ("DELETE", f"v1/apps/{APP}"): {},
        ("POST", "workflows/automations"): {"id": NEW, "name": "emu_nueva", "spaceId": SANDBOX_SPACE_ID},
        ("GET", "workflows/automations"): [{"id": NEW, "name": "emu_nueva"}],
    }


def server(tmp_path, env=None, names=("emu_demo", "real_demo")):
    r = FakeRunner(routes(names))
    t = mcp.Tools(root=mcp._root(), bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    return mcp.Server(tools=t, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)} | (env or {}), state_dir=tmp_path), r


def call(srv, tool, **args):
    return srv.call(tool, args)


def text(resp):
    return resp["content"][0]["text"]


# ----- protocolo -----
def test_initialize_declares_tools_and_server_info():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = srv.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                      "params": {"protocolVersion": "2025-06-18", "capabilities": {}}})
    assert out["result"]["protocolVersion"] == "2025-06-18"
    assert out["result"]["capabilities"]["tools"] == {"listChanged": False}
    assert out["result"]["serverInfo"]["name"] == "dfemu"


def test_notifications_get_no_response():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    assert srv.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None


def test_unknown_method_is_an_error():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = srv.handle({"jsonrpc": "2.0", "id": 7, "method": "completion/complete"})
    assert out["error"]["code"] == -32601


def test_tools_list_has_the_guide_and_valid_schemas():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    tools = srv.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})["result"]["tools"]
    names = [t["name"] for t in tools]
    assert "dfemu_guide" in names and "dfemu_flow_push" in names
    assert names == sorted(mcp.REGISTRY) or set(names) == set(mcp.REGISTRY)
    for t in tools:
        assert t["inputSchema"]["type"] == "object"
        assert t["description"]


def test_serve_reads_lines_and_skips_notifications():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    fin = io.StringIO("\n".join([
        json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}),
        json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}),
        json.dumps({"jsonrpc": "2.0", "id": 3, "method": "tools/list"}),
    ]) + "\n")
    fout = io.StringIO()
    srv.serve(stdin=fin, stdout=fout)
    lines = [json.loads(x) for x in fout.getvalue().splitlines()]
    assert [x["id"] for x in lines] == [1, 3]


def test_broken_json_reports_a_parse_error():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    fout = io.StringIO()
    srv.serve(stdin=io.StringIO("{no es json}\n"), stdout=fout)
    assert json.loads(fout.getvalue())["error"]["code"] == -32700


# ----- lectura -----
def test_guide_lists_every_mode():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = text(call(srv, "dfemu_guide", mode="overview"))
    assert "banco de pruebas" in out
    for mode in mcp.GUIDE:
        assert text(call(srv, "dfemu_guide", mode=mode))


def test_guide_rejects_unknown_mode():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    resp = call(srv, "dfemu_guide", mode="inventado")
    assert resp["isError"] and "modo desconocido" in text(resp)


def test_flow_list_marks_emu_prefix(tmp_path):
    srv, _ = server(tmp_path)
    out = text(call(srv, "dfemu_flow_list"))
    assert "2 flujos visibles" in out and "1 con prefijo emu_" in out
    assert "emu_demo" in out and "real_demo" not in out


def test_flow_get_summary_reads_the_graph(tmp_path):
    srv, _ = server(tmp_path)
    out = text(call(srv, "dfemu_flow_get", flow="emu_demo"))
    assert "nodos: 1" in out and "clientes" in out


def test_flow_get_graph_returns_the_dump(tmp_path):
    srv, _ = server(tmp_path)
    dump = json.loads(text(call(srv, "dfemu_flow_get", flow="emu_demo", format="graph")))
    assert dump["appId"] == APP and dump["script"].startswith("LOAD")


def test_flow_get_unknown_is_an_error(tmp_path):
    srv, _ = server(tmp_path)
    resp = call(srv, "dfemu_flow_get", flow="no_existe")
    assert resp["isError"] and "no existe" in text(resp)


def test_processors_counts_the_catalog():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = text(call(srv, "dfemu_processors"))
    assert "catalogo: 24 processors" in out
    assert "pivot" in out


def test_battery_cases_lists_the_json():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = text(call(srv, "dfemu_battery_cases"))
    assert "casos" in out and "cmp_gt" in out


def test_docs_search_finds_a_line(tmp_path):
    (tmp_path / "docs" / "sub").mkdir(parents=True)
    (tmp_path / "docs" / "sub" / "page.md").write_text("linea uno\nel Data Flow se recarga\n", encoding="utf-8")
    srv = mcp.Server(tools=mcp.Tools(root=tmp_path), env={})
    out = text(call(srv, "dfemu_docs_search", query="recarga"))
    assert "docs/sub/page.md:2" in out


def test_docs_search_rejects_empty_query():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    assert call(srv, "dfemu_docs_search", query="  ")["isError"]


def test_script_translate_returns_sql():
    srv = mcp.Server(tools=mcp.Tools(), env={})
    out = text(call(srv, "dfemu_script_translate", qvs="LOAD 1 AS a;"))
    assert "SQL de DuckDB" in out or "no se pudo traducir" in out


# ----- escritura: limite emu_ y permisos -----
def test_write_needs_the_emu_prefix(tmp_path):
    srv, r = server(tmp_path)
    resp = call(srv, "dfemu_flow_push", base="emu_demo", name="produccion", graph={"nodes": []})
    assert resp["isError"] and "emu_" in text(resp)
    assert not [c for c in r.calls if c[0] == "POST"]


def test_write_can_be_disabled(tmp_path):
    srv, _ = server(tmp_path, env={"DFEMU_MCP_ALLOW_WRITE": "0"})
    resp = call(srv, "dfemu_automation_create", name="emu_x")
    assert resp["isError"] and "deshabilitada" in text(resp)


def test_flow_push_clones_and_discards(tmp_path):
    srv, r = server(tmp_path)
    out = text(call(srv, "dfemu_flow_push", base="emu_demo", name="emu_prueba", graph={"nodes": []}))
    assert "VALID" in out
    assert ("DELETE", f"v1/apps/{NEW}", None) in r.calls  # el clon se borra siempre


def test_automation_create_goes_through_the_bridge(tmp_path):
    srv, r = server(tmp_path)
    assert "emu_nueva" in text(call(srv, "dfemu_automation_create", name="emu_nueva"))
    body = [c for c in r.calls if c[0] == "POST"][-1][2]
    assert body["name"] == "emu_nueva" and body["spaceId"] == SANDBOX_SPACE_ID


# ----- ejecucion y borrado -----
def test_execute_requires_confirm(tmp_path):
    srv, _ = server(tmp_path)
    resp = call(srv, "dfemu_automation_run", automation=NEW)
    assert resp["isError"] and "confirm=true" in text(resp)


def test_execute_can_be_disabled(tmp_path):
    srv, _ = server(tmp_path, env={"DFEMU_MCP_ALLOW_EXECUTE": "0"})
    resp = call(srv, "dfemu_automation_run", automation=NEW, confirm=True)
    assert resp["isError"] and "deshabilitada" in text(resp)


def test_destructive_is_blocked_by_default(tmp_path):
    srv, _ = server(tmp_path)
    resp = call(srv, "dfemu_flow_delete", flow="emu_demo", confirm=True)
    assert resp["isError"] and "DFEMU_MCP_ALLOW_DESTRUCTIVE=1" in text(resp)


def test_destructive_needs_confirm_even_when_allowed(tmp_path):
    srv, _ = server(tmp_path, env={"DFEMU_MCP_ALLOW_DESTRUCTIVE": "1"})
    assert call(srv, "dfemu_automation_delete", automation=NEW)["isError"]


def test_flow_delete_refuses_a_flow_without_prefix(tmp_path):
    srv, r = server(tmp_path, env={"DFEMU_MCP_ALLOW_DESTRUCTIVE": "1"})
    resp = call(srv, "dfemu_flow_delete", flow="real_demo", confirm=True)
    assert resp["isError"] and "emu_" in text(resp)
    assert ("DELETE", f"v1/apps/{APP}", None) not in r.calls


# ----- auditoria -----
def test_audit_records_tool_risk_and_result_but_not_arguments(tmp_path):
    srv, _ = server(tmp_path)
    call(srv, "dfemu_guide", mode="overview")
    call(srv, "dfemu_flow_delete", flow="emu_demo", confirm=True)  # falla: destructivo bloqueado
    lines = [json.loads(x) for x in (tmp_path / "audit.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [x["tool"] for x in lines] == ["dfemu_guide", "dfemu_flow_delete"]
    assert lines[0]["risk"] == "read" and lines[0]["ok"] is True
    assert lines[1]["ok"] is False
    assert "mode" not in json.dumps(lines) and "overview" not in json.dumps(lines)


def test_unknown_tool_is_an_error(tmp_path):
    srv, _ = server(tmp_path)
    resp = call(srv, "dfemu_no_existe")
    assert resp["isError"] and "desconocida" in text(resp)


def test_la_tabla_de_docs_sale_del_registro():
    docs = (mcp._root() / "docs" / "MCP.md").read_text(encoding="utf-8")
    assert mcp.markdown_table() in docs
    assert docs.count("| `dfemu_") == len(mcp.REGISTRY)
