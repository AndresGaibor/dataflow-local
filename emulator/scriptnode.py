"""Nodo `script` por API.

El `schemaEntityId` de un nodo `script` lo crea la interfaz con rutas que no se exponen a la API (todo `POST` bajo
`v1/dataflows/...` responde 403): un nodo `script` no se puede crear desde cero. Pero `actions/copy` de un flujo que
ya tiene nodos `script` asigna `schemaEntityId` nuevos y validos a la copia. Aqui se parte de esa copia, se arma un grafo
reducido (fuente -> nodo `script` de la copia -> destino nuevo) y se cambia solo el texto del script. El servidor no
comprueba el texto contra el esquema registrado (medido con columnas de salida distintas). Ver 9 quater del documento de
hallazgos.
"""
import copy
import re
import uuid

from .builder import Flow
from .bridge import PREFIX
from .remote import Remote, UnsupportedGraph, PushResult


def _node(graph: dict, label: str, kind: str) -> dict:
    found = [n for n in graph["nodes"] if n.get("label") == label and n.get("type") == kind]
    if not found:
        raise UnsupportedGraph(f"en el flujo base no hay un nodo {kind} con la etiqueta {label!r}")
    return found[0]


def reduced_graph(graph: dict, source_label: str, node_label: str, script: str, target_file: str) -> dict:
    """Grafo con la fuente, el nodo `script` (con `script` cambiado y su `schemaEntityId` intacto) y un destino nuevo."""
    if not target_file.startswith(PREFIX):
        raise UnsupportedGraph(f"el archivo de salida debe empezar por {PREFIX!r}: {target_file!r}")
    src = _node(graph, source_label, "source")
    sc = copy.deepcopy(_node(graph, node_label, "processor"))
    if sc["component"]["type"] != "script":
        raise UnsupportedGraph(f"el nodo {node_label!r} no es un nodo script")
    cfg = sc["component"]["properties"]["configuration"]
    # El script que genera Qlik hace STORE de la tabla de salida registrada en el nodo (la primera `[Nombre]:` de su script
    # original). Si el nuevo no la declara, el servidor da VALID igualmente y falla al ejecutarse (medido).
    registered = re.search(r"^\s*\[([^\]]+)\]\s*:", cfg.get("script", ""), re.MULTILINE)
    if registered and not re.search(r"^\s*\[" + re.escape(registered.group(1)) + r"\]\s*:", script, re.MULTILINE | re.IGNORECASE):
        raise UnsupportedGraph(f"el script nuevo debe declarar la tabla de salida [{registered.group(1)}] (la registrada en el nodo)")
    cfg["script"] = script
    src_out = {h["id"] for h in src["handles"]["outgoing"]}
    sc_in = {h["id"] for h in sc["handles"]["incoming"]}
    edge = next((e for e in graph["edges"] if e["sourceHandle"] in src_out and e["targetHandle"] in sc_in), None)
    if edge is None:
        raise UnsupportedGraph(f"el nodo {node_label!r} no cuelga directamente de la fuente {source_label!r}")
    tgt = Flow("x").target("Destino", target_file)
    out = next(h["id"] for h in sc["handles"]["outgoing"] if h["type"] == "DEFAULT")
    return {"nodes": [src, sc, tgt], "edges": [edge, {"id": str(uuid.uuid4()), "sourceHandle": out,
                                                       "targetHandle": tgt["handles"]["incoming"][0]["id"]}]}


def push_script_node(remote: Remote, base_app_id: str, source_label: str, node_label: str, script: str,
                     target_file: str = "emu_script_node") -> PushResult:
    """Sube el grafo reducido a una copia descartable de `base_app_id` y devuelve la validez y el script que genera Qlik."""
    clone = remote.clone(base_app_id, "emu_v_" + uuid.uuid4().hex[:8])
    try:
        graph = remote._get(f"v1/dataflows/{clone.dataflow_id}")["graph"]
        return remote.push_graph(clone, reduced_graph(graph, source_label, node_label, script, target_file))
    finally:
        remote.discard(clone.app_id)
