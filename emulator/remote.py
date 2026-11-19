"""Lectura de flujos del tenant (solo GET, a través de Bridge)."""
import json
import os
import sys
import uuid
from typing import NamedTuple

from .bridge import PREFIX, SANDBOX_SPACE_ID, Bridge, BridgeError, SafetyError, valid_id

# Flujo base que solo se lee y se clona; se configura con DFEMU_BASE_APP.
BASE_APP_ID = os.environ.get("DFEMU_BASE_APP", "00000000-0000-0000-0000-000000000001")
LIST_LIMIT = 100  # tope de `v1/items`; por encima de él el listado puede estar truncado


class FlowRef(NamedTuple):
    name: str
    app_id: str
    space_id: str


class UnsupportedGraph(Exception):
    pass


class Clone(NamedTuple):
    app_id: str
    dataflow_id: str
    name: str


class PushResult(NamedTuple):
    validity: dict
    script: str


REJECT_CODE = "DATAFLOW_STRUCTURAL_ERROR"  # el servidor rechaza el PUT con error HTTP, sin validity


def _rejection_label(stderr: str) -> str:
    """detail (o title) del primer error del JSON que sigue a 'Error:'; si no se lee, el inicio de stderr."""
    try:
        body, _ = json.JSONDecoder().raw_decode(stderr, stderr.index("{"))
        err = body["errors"][0]
        return err.get("detail") or err.get("title") or stderr[:200]
    except (ValueError, KeyError, IndexError, TypeError):
        return stderr[:200]


def _check(x: str) -> str:
    if not valid_id(x):
        raise SafetyError(f"id inválido: {x!r}")
    return x


class Remote:
    def __init__(self, bridge: Bridge):
        self._b = bridge

    def _get(self, path: str, key: str | None = None):
        v = self._b.get(path)
        if not isinstance(v, dict) or (key is not None and key not in v):
            raise BridgeError(f"respuesta sin datos válidos de {path}")
        return v[key] if key is not None else v

    def list_dataflows(self, space_id: str | None = None) -> list[FlowRef]:
        resp = self._b.get("v1/items", {"resourceType": "app", "limit": LIST_LIMIT})
        items = (resp.get("data") or []) if isinstance(resp, dict) else (resp or [])
        if len(items) >= LIST_LIMIT:
            print(f"posible listado truncado: {len(items)} items", file=sys.stderr)
        refs = []
        for it in items:
            app_id = (it.get("resourceAttributes") or {}).get("id") or it.get("resourceId")
            if it.get("resourceSubType") != "dataflow-prep" or not app_id:
                continue
            refs.append(FlowRef(it.get("name") or "", app_id, it.get("spaceId") or ""))
        return [r for r in refs if space_id is None or r.space_id == space_id]

    def dataflow_id(self, app_id: str) -> str:
        return self._get(f"v1/dataflow-apps/{_check(app_id)}", "dataflowId")

    def script_of(self, app_id: str) -> str:
        return self._get(f"v1/apps/{_check(app_id)}/scripts/current", "script")

    def clone(self, base_app_id: str, name: str) -> Clone:
        resp = self._b.post(f"v1/dataflow-apps/{_check(base_app_id)}/actions/copy",
                            {"name": name, "usage": "DATAFLOW_PREP", "spaceId": SANDBOX_SPACE_ID})
        if not isinstance(resp, dict) or "id" not in resp or "dataflowId" not in resp:
            raise BridgeError("respuesta sin datos válidos de la copia")
        return Clone(_check(resp["id"]), _check(resp["dataflowId"]), name)

    def push_graph(self, clone: Clone, graph: dict) -> PushResult:
        df = self._get(f"v1/dataflows/{_check(clone.dataflow_id)}")
        body = {k: v for k, v in df.items() if k != "validity"}
        body["graph"] = graph
        try:
            resp = self._b.put(f"v1/dataflows/{clone.dataflow_id}", body)
        except BridgeError as e:
            if REJECT_CODE not in (e.stderr or ""):
                raise
            return PushResult({"status": "REJECTED", "label": _rejection_label(e.stderr),
                               "nodesConstraintViolations": []}, "")
        if not isinstance(resp, dict) or "validity" not in resp:
            raise BridgeError("respuesta del PUT sin validity")
        return PushResult(resp["validity"], self.script_of(clone.app_id))

    def discard(self, app_id: str) -> None:
        self._b.delete(f"v1/apps/{_check(app_id)}")

    def _datafiles_conn_id(self) -> str:
        conns = self._b.get("v1/data-connections", {"spaceId": SANDBOX_SPACE_ID, "limit": 50})
        if not isinstance(conns, list):
            raise BridgeError("respuesta sin datos válidos de conexiones")
        datafiles = [c for c in conns if (c.get("qName") or c.get("name")) == "DataFiles"]
        if not datafiles:
            raise BridgeError("no se encontró la conexión DataFiles")
        return _check(datafiles[0]["id"])

    def list_emu(self) -> tuple[list[FlowRef], list[str]]:
        """Apps y archivos `emu_*` del espacio permitido; nada de otros espacios.

        No usa `list_dataflows`: tambien hay que borrar apps `emu_*` que no son de flujo.
        """
        resp = self._b.get("v1/items", {"resourceType": "app", "limit": LIST_LIMIT})
        items = (resp.get("data") or []) if isinstance(resp, dict) else (resp or [])
        if len(items) >= LIST_LIMIT:
            print(f"posible listado truncado: {len(items)} items", file=sys.stderr)
        flows = []
        for it in items:
            app_id = (it.get("resourceAttributes") or {}).get("id") or it.get("resourceId")
            if app_id and it.get("spaceId") == SANDBOX_SPACE_ID and str(it.get("name", "")).startswith(PREFIX):
                flows.append(FlowRef(it.get("name") or "", app_id, it["spaceId"]))
        found = self._b.get("v1/data-files", {"connectionId": self._datafiles_conn_id(), "limit": 100}) or []
        files = sorted({f["name"] for f in found if str(f.get("name", "")).startswith(PREFIX)})
        return flows, files

    def discard_files(self, names: list[str]) -> None:
        if not names:
            return
        conn_id = self._datafiles_conn_id()
        ids = []
        for name in names:
            found = self._b.get("v1/data-files", {"connectionId": conn_id, "name": name}) or []
            ids += [f["id"] for f in found if f.get("name") == name]  # coincidencia exacta
        if ids:
            self._b.post("v1/data-files/actions/delete", {"delete": [{"id": i} for i in ids]})

    def validity_of(self, graph: dict, base_app_id: str = BASE_APP_ID) -> PushResult:
        # subflow daña el clon: se rechaza antes de tocar el tenant
        if any(isinstance(n, dict) and (n.get("component") or {}).get("type") == "subflow"
               for n in graph.get("nodes", [])):
            raise UnsupportedGraph("el grafo tiene nodos subflow; no se sube")
        clone = self.clone(base_app_id, "emu_v_" + uuid.uuid4().hex[:8])
        try:
            return self.push_graph(clone, graph)
        finally:
            try:
                self.discard(clone.app_id)
            except (BridgeError, SafetyError) as e:  # no ocultar el error original
                print(f"aviso: no se pudo descartar el clon {clone.app_id}: {e}", file=sys.stderr)

    def pull(self, app_id: str) -> dict:
        df_id = _check(self.dataflow_id(app_id))
        return {
            "appId": app_id,
            "dataflowId": df_id,
            "dataflow": self._get(f"v1/dataflows/{df_id}"),
            "script": self.script_of(app_id),
        }
