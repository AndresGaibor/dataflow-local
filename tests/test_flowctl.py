import pytest

from emulator import flowctl


def _node(i, kind, label, ins=(), outs=()):
    return {"type": kind, "id": i, "label": label, "graphical": {"position": {"x": 0, "y": 0}},
            "handles": {"incoming": [{"id": h, "type": "DEFAULT"} for h in ins], "outgoing": [{"id": h, "type": t} for h, t in outs]},
            "component": {"type": "x", "properties": {"configuration": {}}}}


def _graph():
    g = {"nodes": [_node("a1", "source", "src", outs=[("ao", "DEFAULT")]),
                   _node("b1", "target", "dst", ins=["bi"])], "edges": []}
    g["edges"] = [flowctl._edge(g, "ao", "bi")]
    return g


def _links(g):
    own = {h["id"]: n["label"] for n in g["nodes"] for s in n["handles"].values() for h in s}
    return {(own[e["sourceHandle"]], own[e["targetHandle"]]) for e in g["edges"]}


def test_add_inserta_en_la_arista_y_rm_la_repara():
    g = flowctl.add_node(_graph(), "filter", "src", "f", {"filters": []})
    assert _links(g) == {("src", "f"), ("f", "dst")}
    assert [h["type"] for h in g["nodes"][-1]["handles"]["outgoing"]] == ["DEFAULT", "REJECT"]
    assert g["nodes"][-1]["component"]["properties"]["configuration"]["$state"] == "CONFIGURED"
    assert _links(flowctl.remove_node(g, "f")) == {("src", "dst")}


def test_set_mezcla_diccionarios_y_reemplaza_listas():
    g = flowctl.add_node(_graph(), "filter", "src", "f", {"a": {"x": 1, "y": 2}, "l": [1, 2]})
    cfg = flowctl.set_node(g, "f", {"a": {"y": 3}, "l": [9]}, None)["nodes"][-1]["component"]["properties"]["configuration"]
    assert (cfg["a"], cfg["l"]) == ({"x": 1, "y": 3}, [9])


def test_nodo_ambiguo_o_inexistente_falla():
    with pytest.raises(flowctl.FlowError):
        flowctl.find_node(_graph(), "zz")


def test_la_etiqueta_exacta_manda_sobre_un_id_que_empieza_igual():
    # un uuid que empieza por las mismas letras que la etiqueta no puede ganarle (CI fallo asi)
    g = {"nodes": [_node("f9e71392-x", "x", "otro"), _node("zz", "x", "f")], "edges": []}
    assert flowctl.find_node(g, "f")["id"] == "zz"


def test_escritura_solo_en_emu_o_permitidos(monkeypatch):
    monkeypatch.setattr(flowctl, "_allowed_names", lambda: {"ok"})
    monkeypatch.setattr(flowctl, "call", lambda *a: {"attributes": {"name": "fundamentos", "spaceId": "x"}})
    flowctl.check_writable({"name": "ok"})
    with pytest.raises(flowctl.FlowError):
        flowctl.check_writable({"name": "fundamentos", "context": {"dataAppId": "abc"}})


def test_simulacion_no_escribe(monkeypatch, tmp_path):
    monkeypatch.setattr(flowctl, "check_writable", lambda df: None)
    monkeypatch.setattr(flowctl, "call", lambda *a: pytest.fail("no debe llamar al tenant"))
    monkeypatch.setattr(flowctl, "ROOT", str(tmp_path))
    df = {"id": "d", "name": "n", "graph": _graph()}
    assert "simulacion" in flowctl.push(df, _graph(), apply=False)


def test_catalogo_de_procesadores_y_puertos():
    assert len(flowctl.PROCESSORS) == 24
    assert flowctl.PROCESSORS["join"]["in"] == ["DEFAULT", "LOOKUP"]
    g = flowctl.add_node(_graph(), "script", "src", "s", {})  # script: entradas OPTIONAL, sin DEFAULT
    n = g["nodes"][-1]
    assert [h["type"] for h in n["handles"]["incoming"]] == ["OPTIONAL"] * 10
    assert _links(g) == {("src", "s"), ("s", "dst")}
    assert n["component"]["properties"]["configuration"]["$state"] == "UNCONFIGURED"  # sin --cfg conserva el estado inicial


def test_add_sin_cfg_usa_la_configuracion_inicial():
    cfg = flowctl.add_node(_graph(), "sort", "src", "o", {})["nodes"][-1]["component"]["properties"]["configuration"]
    assert cfg["sortFields"] == [{"fieldPath": "", "sortOrder": "ASCENDING"}]


# --- captura de los cuerpos que solo manda la interfaz ---------------------------------------
def test_capture_summary_esconde_el_host_y_filtra():
    items = [
        {"url": "https://tenant.us.qlikcloud.com/api/v1/dataflow-apps/x/datasources", "method": "POST",
         "status": 201, "req": "{}", "res": "ok"},
        {"url": "https://tenant.us.qlikcloud.com/api/v1/items", "method": "GET", "status": 200, "req": None, "res": "[]"},
    ]
    todo = flowctl.capture_summary(items)
    assert "tenant.us" not in todo  # el host no se imprime
    assert "POST   /api/v1/dataflow-apps/x/datasources" in todo
    solo = flowctl.capture_summary(items, only="datasources")
    assert "datasources" in solo and "/api/v1/items" not in solo
    assert flowctl.capture_summary([]) == "sin peticiones capturadas"


def test_capture_start_instala_el_grabador(monkeypatch):
    visto = {}

    def fake_run_js(script):
        visto["script"] = script
        return {"ok": True, "n": 0, "msg": "grabador activo"}

    monkeypatch.setattr(flowctl, "run_js", fake_run_js)
    assert flowctl.capture("start") == "grabador activo"
    assert "XMLHttpRequest.prototype.send" in visto["script"] and "window.fetch" in visto["script"]


def test_capture_start_sin_pestana_no_miente(monkeypatch):
    monkeypatch.setattr(flowctl, "run_js", lambda s: {"ok": False, "msg": "no hay pestana de Qlik Cloud abierta"})
    assert flowctl.capture("start") == "error: no hay pestana de Qlik Cloud abierta"


def test_capture_dump_guarda_el_json(monkeypatch, tmp_path):
    items = [{"url": "/api/v1/dataflows/x", "method": "PUT", "status": 200, "req": '{"graph":{}}', "res": "{}"}]
    monkeypatch.setattr(flowctl, "run_js", lambda s: {"ok": True, "items": items})
    destino = tmp_path / "captura.json"
    salida = flowctl.capture("dump", out=str(destino))
    assert "1 peticiones guardadas" in salida and destino.exists()
    import json as _json
    assert _json.loads(destino.read_text(encoding="utf-8")) == items


def test_capture_dump_falla_si_la_sesion_no_lee(monkeypatch):
    monkeypatch.setattr(flowctl, "run_js", lambda s: {"ok": False, "msg": "sin sesion"})
    with pytest.raises(flowctl.FlowError):
        flowctl.capture("dump")


def test_capture_rechaza_una_accion_desconocida():
    with pytest.raises(flowctl.FlowError):
        flowctl.capture("borrar")


def test_map_fields_sin_lookup_se_rechaza_antes_de_subirlo():
    # medido en el tenant: con la entrada LOOKUP al aire el nodo sale NODE_TOPOLOGY_NOT_FULFILLED
    g = flowctl.add_node(_graph(), "filter", "src", "f", {})
    with pytest.raises(flowctl.FlowError) as e:
        flowctl.add_node(g, "map-fields", "f", "mf", {"columnsToProcess": ["segmento"]})
    assert "LOOKUP" in str(e.value) and "feed" in str(e.value)


def test_la_entrada_extra_se_conecta_por_su_puerto():
    g = flowctl.add_node(flowctl.add_node(_graph(), "filter", "src", "f", {}), "map-fields", "f", "mf",
                         {"columnsToProcess": ["segmento"], "mapFrom": "segmento", "mapTo": "SEG"},
                         {"LOOKUP": "f:REJECT"})
    mf = flowctl.find_node(g, "mf")
    loo = flowctl._handle(mf, "incoming", "LOOKUP")["id"]
    assert ("f", "mf") in _links(g) or ("f", "mf") in _links(g)
    assert any(e["targetHandle"] == loo for e in g["edges"])
    assert {h["type"] for h in mf["handles"]["incoming"]} == {"DEFAULT", "LOOKUP"}


def test_una_entrada_que_el_nodo_no_tiene_falla():
    with pytest.raises(flowctl.FlowError) as e:
        flowctl.add_node(_graph(), "filter", "src", "f", {}, {"LOOKUP": "src"})
    assert "no tiene entrada LOOKUP" in str(e.value)


def test_un_puerto_de_salida_inexistente_falla():
    g = flowctl.add_node(_graph(), "filter", "src", "f", {})
    with pytest.raises(flowctl.FlowError) as e:
        flowctl.add_node(g, "map-fields", "f", "mf", {"columnsToProcess": ["x"]}, {"LOOKUP": "src:REJECT"})
    assert "no tiene salida REJECT" in str(e.value)
