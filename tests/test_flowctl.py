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
