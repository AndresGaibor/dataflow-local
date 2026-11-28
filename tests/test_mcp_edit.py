"""MCP: editar el grafo, el script, las automatizaciones y las tareas sin salir del servidor."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import mcp  # noqa: E402
from emulator.bridge import SANDBOX_SPACE_ID, Bridge  # noqa: E402
from fakes import FakeRunner  # noqa: E402

APP, DF = "a" * 24, "c" * 24
NODE_SRC, NODE_DST = "s" * 24, "t" * 24
A = "b" * 24


def graph():
    return {"nodes": [
        {"type": "source", "id": NODE_SRC, "label": "clientes", "graphical": {"position": {"x": 0, "y": 0}},
         "handles": {"incoming": [], "outgoing": [{"id": "h_src", "type": "DEFAULT"}]},
         "component": {"type": "analyticsSource", "properties": {"configuration": {}}}},
        {"type": "target", "id": NODE_DST, "label": "Destino", "graphical": {"position": {"x": 900, "y": 0}},
         "handles": {"incoming": [{"id": "h_dst", "type": "DEFAULT"}], "outgoing": []},
         "component": {"type": "analyticsTarget", "properties": {"configuration": {}}}}],
        "edges": [{"id": "e1", "source": NODE_SRC, "sourceHandle": "h_src", "target": NODE_DST, "targetHandle": "h_dst"}]}


def routes(flow_name="emu_demo"):
    estado = {"graph": graph()}

    def leer(body):
        return {"graph": estado["graph"], "validity": {}, "context": {"dataAppId": APP}}

    def escribir(body):
        estado["graph"] = body["graph"]
        return {"validity": {"status": "VALID", "nodesConstraintViolations": []}}

    return {
        ("GET", "v1/items"): {"data": [
            {"resourceType": "app", "resourceSubType": "dataflow-prep", "spaceId": SANDBOX_SPACE_ID,
             "name": flow_name, "resourceAttributes": {"id": APP}},
            {"resourceType": "app", "resourceSubType": "dataflow-prep", "spaceId": SANDBOX_SPACE_ID,
             "name": "produccion", "resourceAttributes": {"id": "9" * 24}}]},
        ("GET", f"v1/apps/{APP}"): {"attributes": {"name": flow_name, "spaceId": SANDBOX_SPACE_ID}},
        ("GET", f"v1/dataflow-apps/{APP}"): {"dataflowId": DF},
        ("GET", f"v1/dataflows/{DF}"): leer,
        ("PUT", f"v1/dataflows/{DF}"): escribir,
        ("GET", f"v1/apps/{APP}/scripts/current"): {"script": "LOAD 1 AS a;"},
        ("POST", "workflows/automations"): {"id": A, "name": "emu_nueva"},
        ("GET", "workflows/automations"): [{"id": A, "name": "emu_demo_auto"}],
        ("GET", f"workflows/automations/{A}"): {"id": A, "name": "emu_demo_auto", "spaceId": SANDBOX_SPACE_ID},
        ("PUT", f"workflows/automations/{A}"): {"id": A, "name": "emu_renombrada"},
        ("POST", f"workflows/automations/{A}/actions/copy"): {"id": "d" * 24, "name": "emu_copia"},
        ("POST", f"workflows/automations/{A}/runs/{'e' * 24}/actions/stop"): {"status": "STOPPED"},
        ("GET", "scheduling/tasks"): {"data": [{"id": A, "name": "emu_diaria", "enabled": True}]},
        ("POST", f"scheduling/tasks/resources/{APP}/actions/reload/on-time-schedule"):
            {"id": A, "name": "emu_diaria", "enabled": True},
        ("POST", f"scheduling/tasks/{A}/actions/start"): {"message": "tarea arrancada"},
        ("PATCH", f"scheduling/tasks/{A}"): {},
        ("DELETE", f"scheduling/tasks/{A}"): {},
        ("GET", f"scheduling/tasks/{A}"): {"id": A, "resourceId": APP, "enabled": True},
        ("CLI", "app script set"): "",
    }


def server(tmp_path, env=None, flow_name="emu_demo"):
    r = FakeRunner(routes(flow_name))
    tools = mcp.Tools(bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    return mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)} | (env or {}), state_dir=tmp_path), r


def call(srv, tool, **args):
    return srv.call(tool, args)


def text(resp):
    return resp["content"][0]["text"]


def last_put(r):
    return [c for c in r.calls if c[0] == "PUT"][-1][2]["graph"]


# ----- edicion del grafo -----
def test_add_node_inserta_el_processor_y_sube_el_grafo(tmp_path):
    srv, r = server(tmp_path)
    out = text(call(srv, "dfemu_flow_add_node", flow="emu_demo", type="filter", after=NODE_SRC,
                    config={"filters": []}, label="Filtro"))
    assert "VALID" in out and "3 nodos" in out
    g = last_put(r)
    assert len(g["nodes"]) == 3
    nuevo = [n for n in g["nodes"] if n["label"] == "Filtro"][0]
    assert nuevo["component"]["type"] == "filter"


def test_add_node_acepta_el_nombre_de_la_paleta(tmp_path):
    srv, r = server(tmp_path)
    call(srv, "dfemu_flow_add_node", flow="emu_demo", type="Filtro", after=NODE_SRC)
    nuevo = [n for n in last_put(r)["nodes"] if n["label"] == "Filtro"][0]
    assert nuevo["component"]["type"] == "filter"


def test_set_node_mezcla_la_configuracion(tmp_path):
    srv, r = server(tmp_path)
    out = text(call(srv, "dfemu_flow_set_node", flow="emu_demo", node=NODE_SRC, config={"x": 1}))
    assert "actualizado" in out
    nodo = [n for n in last_put(r)["nodes"] if n["id"] == NODE_SRC][0]
    assert nodo["component"]["properties"]["configuration"] == {"x": 1}


def test_remove_node_reconecta_las_aristas(tmp_path):
    srv, r = server(tmp_path)
    call(srv, "dfemu_flow_add_node", flow="emu_demo", type="filter", after=NODE_SRC, label="Filtro")
    g1 = last_put(r)
    filtro = [n for n in g1["nodes"] if n["label"] == "Filtro"][0]["id"]
    out = text(call(srv, "dfemu_flow_remove_node", flow="emu_demo", node=filtro))
    assert "quitado" in out
    g2 = last_put(r)
    assert len(g2["nodes"]) == 2 and len(g2["edges"]) == 1  # vuelve a haber una sola arista


def test_editar_un_flujo_que_no_es_emu_se_rechaza(tmp_path):
    srv, r = server(tmp_path)
    resp = call(srv, "dfemu_flow_add_node", flow="produccion", type="filter", after=NODE_SRC)
    assert resp["isError"] and "emu_" in text(resp)
    assert not [c for c in r.calls if c[0] == "PUT"]


def test_backup_y_restore(tmp_path):
    srv, r = server(tmp_path)
    srv.tools.root = tmp_path
    out = text(call(srv, "dfemu_flow_backup", flow="emu_demo"))
    assert "out/backups" in out
    copia = next((tmp_path / "out" / "backups").glob("emu_demo-*.json"))
    data = json.loads(copia.read_text(encoding="utf-8"))
    assert data["appId"] == APP
    assert "VALID" in text(call(srv, "dfemu_flow_restore", flow="emu_demo", file=str(copia)))


def test_restore_de_un_archivo_sin_grafo_falla(tmp_path):
    srv, _ = server(tmp_path)
    malo = tmp_path / "malo.json"
    malo.write_text("{}", encoding="utf-8")
    resp = call(srv, "dfemu_flow_restore", flow="emu_demo", file=str(malo))
    assert resp["isError"] and "grafo" in text(resp)


def test_clone_crea_un_emu_nuevo(tmp_path):
    r = FakeRunner(routes())
    r.routes[("POST", f"v1/dataflow-apps/{APP}/actions/copy")] = {"id": "f" * 24, "dataflowId": "g" * 24}
    tools = mcp.Tools(bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    srv = mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    assert "f" * 24 in text(call(srv, "dfemu_flow_clone", base="emu_demo", name="emu_copia"))
    assert call(srv, "dfemu_flow_clone", base="emu_demo", name="sin_prefijo")["isError"]


# ----- Qlik script -----
def test_script_get_y_set(tmp_path):
    srv, r = server(tmp_path)
    assert "LOAD 1" in text(call(srv, "dfemu_script_get", app="emu_demo"))
    assert "script subido" in text(call(srv, "dfemu_script_set", app="emu_demo", script="LOAD 2 AS b;"))
    subido = [c for c in r.calls if c[0] == "CLI" and c[1] == "app script set"][-1][2]
    assert subido == "LOAD 2 AS b;"


def test_script_set_necesita_texto_o_archivo(tmp_path):
    srv, _ = server(tmp_path)
    assert call(srv, "dfemu_script_set", app="emu_demo")["isError"]


def test_script_validate_devuelve_los_errores(tmp_path):
    r = FakeRunner({("POST", "v1/apps/validatescript"): {"Errors": [{"qErrorString": "syntax error"}]}})
    tools = mcp.Tools(bridge_factory=lambda apply: Bridge(runner=r, apply=apply))
    srv = mcp.Server(tools=tools, env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    assert "syntax error" in text(call(srv, "dfemu_script_validate", script="LOAD"))
    r.routes[("POST", "v1/apps/validatescript")] = {"Errors": []}
    assert "sin errores" in text(call(srv, "dfemu_script_validate", script="LOAD 1;"))


# ----- automatizaciones -----
def test_automation_show_update_copy_stop(tmp_path):
    srv, r = server(tmp_path)
    assert "emu_demo_auto" in text(call(srv, "dfemu_automation_show", automation=A))
    assert "name actualizado" in text(call(srv, "dfemu_automation_update", automation=A, name="emu_renombrada"))
    assert "emu_copia" in text(call(srv, "dfemu_automation_copy", automation=A, name="emu_copia"))
    assert call(srv, "dfemu_automation_update", automation=A, name="sin_prefijo")["isError"]
    stopped = call(srv, "dfemu_automation_stop", automation=A, run_id="e" * 24, confirm=True)
    assert "STOPPED" in text(stopped)


def test_automation_update_sin_campos_avisa(tmp_path):
    srv, _ = server(tmp_path)
    assert call(srv, "dfemu_automation_update", automation=A)["isError"]


# ----- tareas -----
def test_tareas_listar_programar_arrancar_y_borrar(tmp_path):
    srv, _ = server(tmp_path)
    assert "emu_diaria" in text(call(srv, "dfemu_task_list", app="emu_demo"))
    creada = text(call(srv, "dfemu_task_schedule", app="emu_demo", name="emu_diaria",
                       recurrence="RRULE:FREQ=DAILY;BYHOUR=3", enabled=True))
    assert "tarea" in creada
    assert call(srv, "dfemu_task_start", task=A)["isError"]  # sin confirm
    assert "arrancada" in text(call(srv, "dfemu_task_start", task=A, confirm=True))
    assert "deshabilitada" in text(call(srv, "dfemu_task_set_enabled", task=A, enabled=False))
    assert call(srv, "dfemu_task_delete", task=A, confirm=True)["isError"]  # destructivo bloqueado


# ----- simulacro global y emulador -----
def test_el_simulacro_global_no_escribe(tmp_path):
    srv, r = server(tmp_path, env={"DFEMU_MCP_APPLY": "0"})
    out = text(call(srv, "dfemu_flow_add_node", flow="emu_demo", type="filter", after=NODE_SRC))
    assert "simulado" in out
    assert not [c for c in r.calls if c[0] == "PUT"]


def test_emulate_ejecuta_un_dfw_local(tmp_path):
    srv = mcp.Server(tools=mcp.Tools(root=mcp._root()), env={"DFEMU_MCP_STATE_DIR": str(tmp_path)}, state_dir=tmp_path)
    out = text(call(srv, "dfemu_emulate", file="samples/fundamentos_filtro_basico.dfw"))
    assert "destinos escritos" in out
