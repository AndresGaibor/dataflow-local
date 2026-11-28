"""Servidor MCP (stdio) de dfemu: expone el banco de pruebas a un asistente.

Sin dependencias nuevas: JSON-RPC 2.0 con un mensaje por linea sobre stdin/stdout,
el transporte que define MCP para stdio.

El permiso lo aplica el servidor, no el asistente. Cada herramienta declara su riesgo:

| riesgo        | por defecto | como cambiarlo                                    |
|---------------|-------------|---------------------------------------------------|
| `read`        | permitido   | —                                                 |
| `write`       | permitido   | `DFEMU_MCP_ALLOW_WRITE=0`                         |
| `execute`     | permitido   | `DFEMU_MCP_ALLOW_EXECUTE=0`; exige `confirm=true`  |
| `destructive` | bloqueado   | `DFEMU_MCP_ALLOW_DESTRUCTIVE=1`; exige `confirm`   |

Ademas, toda escritura se limita a objetos `emu_*`: el nombre se comprueba en el
servidor antes de tocar el tenant. Cada llamada deja una linea en
`<estado>/audit.jsonl` con herramienta, riesgo, resultado y duracion; nunca los
argumentos, para no filtrar credenciales ni datos.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

PROTOCOL = "2025-06-18"
SERVER = {"name": "dfemu", "version": "0.1.0"}
RISK_ENV = {"write": "DFEMU_MCP_ALLOW_WRITE", "execute": "DFEMU_MCP_ALLOW_EXECUTE",
            "destructive": "DFEMU_MCP_ALLOW_DESTRUCTIVE"}


class Denied(Exception):
    """La herramienta existe pero el servidor no la autoriza tal como se llamó."""


class Failed(Exception):
    """La herramienta se autoriza pero falló al ejecutarse."""


def _root() -> Path:
    return Path(__file__).resolve().parent.parent


GUIDE = {
    "overview": (
        "dfemu es el banco de pruebas de los Data Flows de Qlik Cloud: emulador local (DuckDB), traductor de\n"
        "script y comparador contra el tenant. Con este servidor MCP puedes, en orden:\n"
        "1. `dfemu_status` para saber que hay ahora en el espacio de pruebas (solo objetos emu_).\n"
        "2. `dfemu_flow_list` / `dfemu_flow_get` para leer los flujos existentes y su grafo.\n"
        "3. `dfemu_processors` para saber que processors se pueden usar y con que evidencia.\n"
        "4. `dfemu_flow_push` para escribir un grafo en un clon emu_ (nunca en un flujo real).\n"
        "5. `dfemu_battery_cases` / `dfemu_battery_run` para medir un processor contra el tenant.\n"
        "6. `dfemu_docs_search` para buscar en la documentacion descargada de help.qlik.com.\n"
        "Toda escritura exige un nombre emu_* y queda auditada."
    ),
    "dataflow": (
        "Ciclo de un Data Flow:\n"
        "- `dfemu_flow_get` con `format=graph` devuelve el `.dfw` completo: nodos, handles y edges.\n"
        "- construye el grafo nuevo (o reutiliza el de un flujo parecido) y pasalo a `dfemu_flow_push`\n"
        "  con un nombre `emu_*`; el servidor clona el flujo base, lo sube y responde la validez del servidor.\n"
        "- `dfemu_processors` dice que processors estan medidos; lo que no este medido, no lo afirmes.\n"
        "- `pivot`, `map-fields`, `subflow` y el nodo `script` no se pueden crear por API en este tenant: para esos\n"
        "  usa `dfemu flow types` y `dfemu flow add TIPO --after NODO` (sesion de Chrome ya iniciada y exige --apply)."
    ),
    "script": (
        "Qlik script:\n"
        "- `dfemu_script_translate` traduce un script de Qlik a SQL de DuckDB y explica que no entiende.\n"
        "- para trabajar contra el tenant usa la CLI: `dfemu script get|set|validate`.\n"
        "- el inventario de constructs del corpus esta en docs/banco-de-pruebas/05-cobertura-script.md."
    ),
    "automate": (
        "Qlik Automate (ruta vigente `api/v1/workflows/automations`):\n"
        "- `dfemu_automation_create` crea una automatizacion `emu_*`.\n"
        "- `dfemu_automation_set_enabled` la habilita o deshabilita.\n"
        "- `dfemu_automation_run` la ejecuta (exige `confirm=true`); `dfemu_automation_runs` lista sus ejecuciones.\n"
        "- `dfemu_automation_delete` la borra, y solo si el servidor tiene habilitado lo destructivo."
    ),
    "docs": (
        "Documentacion: `dfemu_docs_search` busca texto en el corpus descargado de help.qlik.com\n"
        "(docs/, docs/Automate/). `python scripts/docsync.py --check` comprueba que no falte ninguna pagina;\n"
        "`--pull` la vuelve a descargar y actualiza docs/manifest.json con su sha256."
    ),
    "battery": (
        "Bateria de processors: cada caso es fuente -> processor(es) -> destino, se ejecuta en el emulador y en\n"
        "el tenant, y se comparan contenido y las primeras filas. `dfemu_battery_cases` lista los casos;\n"
        "`dfemu_battery_run` mide uno contra el tenant (exige `confirm=true` y escribe objetos emu_ temporales)."
    ),
}


def _emu_name(name: str, what: str = "el objeto") -> str:
    if not isinstance(name, str) or not name.startswith("emu_"):
        raise Denied(f"{what} debe empezar por `emu_` (recibido: {name!r})")
    return name


def _text(s: str) -> dict:
    return {"content": [{"type": "text", "text": s}]}


class Tools:
    """Implementaciones. `remote_factory` permite inyectar un doble en las pruebas."""

    def __init__(self, root: Path | None = None, remote_factory=None, bridge_factory=None, env: dict | None = None):
        self.root = Path(root) if root else _root()
        self.env = dict(os.environ if env is None else env)
        self._remote_factory = remote_factory
        self._bridge_factory = bridge_factory
        self._bridges: dict[bool, object] = {}
        self._remotes: dict[bool, object] = {}

    # ----- infraestructura -----
    def bridge(self, apply: bool):
        apply = apply and self.env.get("DFEMU_MCP_APPLY", "1") != "0"  # simulacro global
        if apply not in self._bridges:
            if self._bridge_factory:
                b = self._bridge_factory(apply)
            else:
                from . import bridge

                b = bridge.Bridge(apply=apply)
            self._bridges[apply] = b
        return self._bridges[apply]

    def remote(self, apply: bool = False):
        if apply not in self._remotes:
            if self._remote_factory:
                r = self._remote_factory(apply)
            else:
                from .remote import Remote

                r = Remote(self.bridge(apply))
            self._remotes[apply] = r
        return self._remotes[apply]

    def _flow(self, name: str):
        for f in self.remote(False).list_dataflows():
            if f.name == name or f.app_id == name:
                return f
        raise Failed(f"no existe un flujo `{name}`")

    # ----- lectura -----
    def guide(self, mode: str = "overview") -> str:
        if mode not in GUIDE:
            raise Failed(f"modo desconocido `{mode}`; usa uno de: {', '.join(GUIDE)}")
        return GUIDE[mode]

    def status(self) -> str:
        flows, files = self.remote(False).list_emu()
        from . import automate

        autos = automate.ls(self.bridge(False))
        lines = ["objetos emu_ en el espacio de pruebas", "", "flujos:"]
        lines += [f"- {f.name} ({f.app_id})" for f in flows] or ["- (ninguno)"]
        lines += ["", "archivos:"] + ([f"- {n}" for n in files] or ["- (ninguno)"])
        lines += ["", f"automatizaciones: {len(autos)}"]
        lines += [f"- {a.get('name')} ({a.get('id')})" for a in autos] or ["- (ninguna)"]
        return "\n".join(lines)

    def flow_list(self) -> str:
        refs = self.remote(False).list_dataflows()
        emu = [f for f in refs if (f.name or "").startswith("emu_")]
        lines = [f"{len(refs)} flujos visibles; {len(emu)} con prefijo emu_", ""]
        lines += [f"- {f.name} ({f.app_id})" for f in emu] or ["- (ninguno)"]
        return "\n".join(lines)

    def flow_get(self, flow: str, format: str = "summary") -> str:  # noqa: A002 - el nombre lo fija el esquema
        ref = self._flow(flow)
        dump = self.remote(False).pull(ref.app_id)
        graph = (dump.get("dataflow") or {}).get("graph") or dump.get("graph") or {}
        if format == "graph":
            return json.dumps(dump, ensure_ascii=False, indent=1)
        nodes = graph.get("nodes") or []
        lines = [f"{ref.name} ({ref.app_id})", f"nodos: {len(nodes)}", ""]
        for n in nodes:
            c = n.get("component") or {}
            props = c.get("properties") or {}
            name = props.get("processorType") or props.get("type") or c.get("type")
            lines.append(f"- {n.get('label') or name}: {c.get('type')} ({name})")
        return "\n".join(lines)

    def processors(self) -> str:
        cat = json.loads((self.root / "emulator" / "processors.json").read_text(encoding="utf-8"))
        types = sorted(cat) if isinstance(cat, dict) else sorted(cat)
        cases_file = self.root / "scripts" / "processor_battery_cases.json"
        cases = json.loads(cases_file.read_text(encoding="utf-8")) if cases_file.exists() else {}
        covered = set()
        for ctype, cfg in cases.values():
            if isinstance(cfg, dict) and cfg.get("type"):
                covered.add(cfg["type"])
        lines = [f"catalogo: {len(types)} processors; casos de bateria: {len(cases)}", ""]
        for t in types:
            lines.append(f"- {t}: {'con caso medido' if t in covered else 'sin caso'}")
        return "\n".join(lines)

    def script_translate(self, qvs: str = "", path: str = "") -> str:
        from . import script as sc

        if path:
            text = Path(path).read_text(encoding="utf-8")
        elif qvs:
            text = qvs
        else:
            raise Failed("pasa `qvs` con el script o `path` con el archivo")
        sql, reasons = sc.translate(text, str(self.root / "data" / "practica"))
        if sql is None:
            return "no se pudo traducir:\n" + "\n".join(f"- {r}" for r in reasons)
        head = f"SQL de DuckDB ({len(sql.splitlines())} lineas):\n\n{sql}"
        return head + ("\n\nsin traducir:\n" + "\n".join(f"- {r}" for r in reasons) if reasons else "")

    def docs_search(self, query: str, limit: int = 20) -> str:
        if not query.strip():
            raise Failed("`query` no puede ir vacio")
        hits, total = [], 0
        for p in sorted((self.root / "docs").rglob("*.md")):
            try:
                for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if query.lower() in line.lower():
                        total += 1
                        if len(hits) < max(1, min(limit, 100)):
                            hits.append(f"{p.relative_to(self.root).as_posix()}:{i}: {line.strip()[:180]}")
            except OSError:
                continue
        if not hits:
            return f"sin coincidencias para `{query}` en docs/"
        return f"{total} coincidencias (mostrando {len(hits)}):\n\n" + "\n".join(hits)

    def battery_cases(self) -> str:
        f = self.root / "scripts" / "processor_battery_cases.json"
        cases = json.loads(f.read_text(encoding="utf-8"))
        lines = [f"{len(cases)} casos", ""]
        for name, (ctype, cfg) in cases.items():
            ptype = cfg.get("type") if isinstance(cfg, dict) else "cadena"
            lines.append(f"- {name} ({ctype}: {ptype})")
        return "\n".join(lines)

    # ----- escritura -----
    def flow_push(self, base: str, name: str, graph: dict | None = None, graph_file: str = "") -> str:
        _emu_name(name, "el nombre del flujo")
        if graph is None:
            if not graph_file:
                raise Failed("pasa `graph` o `graph_file` con el .dfw")
            graph = json.loads(Path(graph_file).read_text(encoding="utf-8"))
        if "dataflow" in graph:
            graph = graph["dataflow"]["graph"]
        elif "graph" in graph:
            graph = graph["graph"]
        ref = self._flow(base)
        remote = self.remote(True)
        clone = remote.clone(ref.app_id, name)
        try:
            res = remote.push_graph(clone, graph)
        finally:
            remote.discard(clone.app_id)
        status = res.validity.get("status")
        codes = [v.get("code") for v in res.validity.get("nodesConstraintViolations") or []]
        return f"{name}: {status}" + (f" {codes}" if codes else "") + f"\nnodos: {len(graph.get('nodes') or [])}"

    def automation_create(self, name: str, description: str = "") -> str:
        _emu_name(name, "el nombre de la automatizacion")
        from . import automate

        a = automate.new(self.bridge(True), name, None, description)
        return f"automatizacion creada: {a.get('name')} ({a.get('id')})"

    def automation_set_enabled(self, automation: str, enabled: bool = True) -> str:
        from . import automate

        a = (automate.enable if enabled else automate.disable)(self.bridge(True), automation)
        return f"{a.get('name')}: {'habilitada' if enabled else 'deshabilitada'}"

    # ----- ejecucion y borrado -----
    def automation_run(self, automation: str, context: str = "api") -> str:
        from . import automate

        r = automate.run(self.bridge(True), automation, context)
        return f"ejecucion lanzada: {r.get('id')} ({r.get('status')})"

    def automation_runs(self, automation: str) -> str:
        from . import automate

        rows = automate.runs(self.bridge(False), automation)
        if not rows:
            return "sin ejecuciones"
        return "\n".join(f"- {r.get('id')} {r.get('status')} {r.get('startedAt', '')}" for r in rows)

    def battery_run(self, case: str) -> str:
        sys.path.insert(0, str(self.root / "scripts"))
        try:
            import processor_battery as pb
        except ImportError as e:  # pragma: no cover - depende del arbol
            raise Failed(f"no se pudo importar la bateria: {e}") from e
        if case not in pb.CASES:
            raise Failed(f"caso desconocido `{case}`")
        b = pb.bridge.Bridge(apply=True)
        r = pb.Remote(b)
        status, detail = pb.run_case(case, b, r, pb.base_entity(r), str(self.root / "data" / "practica"),
                                     str(self.root / "out" / "battery"))
        return f"{case}: {status} {detail}".strip()

    def flow_reload(self, flow: str, timeout: float = 180) -> str:
        from . import reload

        ref = self._flow(flow)
        _emu_name(ref.name, "el flujo a recargar")
        r = reload.run(self.bridge(True), ref.app_id, wait_for=True, timeout=float(timeout))
        return f"{ref.name}: " + reload.summary(r)

    # ----- edicion de grafos por API (sin navegador) -----
    def _graph_of(self, flow: str):
        """Flujo emu_ + su volcado + el grafo, comprobando el prefijo antes de tocar nada."""
        ref = self._flow(flow)
        _emu_name(ref.name, "el flujo a editar")
        dump = self.remote(False).pull(ref.app_id)
        graph = (dump.get("dataflow") or {}).get("graph") or {}
        if not graph:
            raise Failed(f"`{ref.name}` no tiene grafo legible")
        return ref, dump, graph

    def _push(self, ref, dump: dict, graph: dict, nota: str = "") -> str:
        from .remote import Clone

        res = self.remote(True).push_graph(Clone(ref.app_id, dump["dataflowId"], ref.name), graph)
        status = res.validity.get("status")
        codes = [v.get("code") for v in res.validity.get("nodesConstraintViolations") or []]
        line = f"{ref.name}: {status}" + (f" {codes}" if codes else "") + f" ({len(graph.get('nodes') or [])} nodos)"
        return line + (f"\n{nota}" if nota else "")

    def flow_add_node(self, flow: str, type: str, after: str, config: dict | None = None, label: str = "") -> str:
        from . import flowctl

        ref, dump, graph = self._graph_of(flow)
        ctype = next((k for k, s in flowctl.PROCESSORS.items() if type in (k, s.get("palette"))), type)
        nuevo = flowctl.add_node(graph, ctype, after, label or flowctl.PROCESSORS.get(ctype, {}).get("label", ctype),
                                 config or {})
        insertado = [n for n in nuevo["nodes"] if n["id"] not in {x["id"] for x in graph["nodes"]}]
        nota = f"nodo {insertado[0].get('label')} ({insertado[0].get('id')}) tras {after}" if insertado else ""
        return self._push(ref, dump, nuevo, nota)

    def flow_set_node(self, flow: str, node: str, config: dict | None = None, label: str | None = None) -> str:
        from . import flowctl

        ref, dump, graph = self._graph_of(flow)
        return self._push(ref, dump, flowctl.set_node(graph, node, config or {}, label), f"nodo {node} actualizado")

    def flow_remove_node(self, flow: str, node: str) -> str:
        from . import flowctl

        ref, dump, graph = self._graph_of(flow)
        return self._push(ref, dump, flowctl.remove_node(graph, node), f"nodo {node} quitado y aristas reconectadas")

    def flow_clone(self, base: str, name: str) -> str:
        _emu_name(name, "el nombre del clon")
        ref = self._flow(base)
        c = self.remote(True).clone(ref.app_id, name)
        return f"{name}: {c.app_id} (clon de {ref.name})"

    def flow_backup(self, flow: str) -> str:
        ref, dump, _graph = self._graph_of(flow)
        out = self.root / "out" / "backups"
        out.mkdir(parents=True, exist_ok=True)
        path = out / f"{ref.name}-{time.strftime('%Y%m%d-%H%M%S')}.json"
        path.write_text(json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
        return f"copia de {ref.name} en {path.relative_to(self.root).as_posix()}"

    def flow_restore(self, flow: str, file: str) -> str:
        ref, dump, _graph = self._graph_of(flow)
        data = json.loads(Path(file).read_text(encoding="utf-8"))
        graph = (data.get("dataflow") or data).get("graph") or data.get("graph")
        if not graph:
            raise Failed(f"`{file}` no trae un grafo (`dataflow.graph`)")
        return self._push(ref, dump, graph, f"restaurado desde {file}")

    # ----- Qlik script -----
    def script_get(self, app: str) -> str:
        ref = self._flow(app)
        return f"script de {ref.name}:\n\n" + self.bridge(False).script_get(ref.app_id)

    def script_set(self, app: str, script: str = "", path: str = "") -> str:
        ref = self._flow(app)
        _emu_name(ref.name, "la app del script")
        if path:
            text = Path(path).read_text(encoding="utf-8", newline="")
        elif script:
            text = script
        else:
            raise Failed("pasa `script` con el texto o `path` con el archivo .qvs")
        self.bridge(True).script_set(ref.app_id, text)
        return f"{ref.name}: script subido ({len(text.splitlines())} lineas)"

    def script_validate(self, script: str = "", path: str = "") -> str:
        if path:
            text = Path(path).read_text(encoding="utf-8", newline="")
        elif script:
            text = script
        else:
            raise Failed("pasa `script` o `path`")
        errors = self.bridge(False).script_validate(text)
        return "sin errores" if not errors else "\n".join(f"- {e.get('qErrorString') or e}" for e in errors)

    # ----- automatizaciones: definicion y parada -----
    def automation_show(self, automation: str) -> str:
        from . import automate

        return json.dumps(automate.show(self.bridge(False), automation), ensure_ascii=False, indent=1)

    def automation_update(self, automation: str, name: str = "", description: str = "") -> str:
        from . import automate

        info = automate.show(self.bridge(False), automation)
        _emu_name(info.get("name") or "", "la automatizacion a modificar")
        fields = {k: v for k, v in (("name", name), ("description", description)) if v}
        if not fields:
            raise Failed("nada que cambiar: pasa `name` o `description`")
        if "name" in fields:
            _emu_name(fields["name"], "el nombre nuevo")
        a = automate.set(self.bridge(True), automation, **fields)
        return f"{a.get('name')} ({a.get('id')}): {', '.join(sorted(fields))} actualizado"

    def automation_copy(self, automation: str, name: str) -> str:
        from . import automate

        _emu_name(name, "el nombre de la copia")
        a = automate.copy(self.bridge(True), automation, name)
        return f"copia creada: {a.get('name')} ({a.get('id')})"

    def automation_stop(self, automation: str, run_id: str) -> str:
        from . import automate

        r = automate.stop(self.bridge(True), automation, run_id)
        return f"{run_id}: {r.get('status', 'parada solicitada')}"

    # ----- tareas de recarga (scheduling) -----
    def task_list(self, app: str) -> str:
        from . import tasks

        ref = self._flow(app)
        rows = tasks.list_tasks(self.bridge(False), ref.app_id)
        if not rows:
            return f"{ref.name}: sin tareas"
        return "\n".join(f"- {t.get('id')} {'habilitada' if t.get('enabled') else 'deshabilitada'} {t.get('name')}"
                         for t in rows)

    def task_schedule(self, app: str, name: str, recurrence: str, timezone: str = "UTC", enabled: bool = False) -> str:
        from . import tasks

        ref = self._flow(app)
        _emu_name(ref.name, "la app de la tarea")
        t = tasks.schedule(self.bridge(True), ref.app_id, name, recurrence, timezone, enabled)
        return f"tarea {t.get('id')} creada ({'habilitada' if t.get('enabled') else 'deshabilitada'})"

    def task_start(self, task: str) -> str:
        from . import tasks

        return str(tasks.start(self.bridge(True), task).get("message") or "tarea arrancada")

    def task_set_enabled(self, task: str, enabled: bool = True) -> str:
        from . import tasks

        tasks.set_enabled(self.bridge(True), task, enabled)
        return f"tarea {'habilitada' if enabled else 'deshabilitada'}"

    def task_delete(self, task: str) -> str:
        from . import tasks

        tasks.delete(self.bridge(True), task)
        return "tarea borrada"

    # ----- emulador local -----
    def emulate(self, file: str, data_dir: str = "data/practica", head: int = 3) -> str:
        from . import compare, dfw, runner

        dump = dfw.load(file)
        out = self.root / "out" / "mcp"
        res = runner.run(dump, str(self.root / data_dir), str(out))
        fps = compare.local_fingerprints([t["dest"] for t in res], head=int(head))
        lines = [f"{len(res)} destinos escritos en out/mcp/"]
        for t in res:
            stem = Path(str(t["dest"])).stem
            cols = len((fps.get(stem) or {}).get("columns") or {})
            lines.append(f"- {stem}: {t.get('rows')} filas, {cols} columnas")
        return "\n".join(lines)

    def flow_delete(self, flow: str) -> str:
        ref = self._flow(flow)
        _emu_name(ref.name, "el flujo a borrar")
        self.remote(True).discard(ref.app_id)
        return f"flujo borrado: {ref.name} ({ref.app_id})"

    def automation_delete(self, automation: str) -> str:
        from . import automate

        info = automate.show(self.bridge(False), automation)
        _emu_name(info.get("name") or "", "la automatizacion a borrar")
        automate.rm(self.bridge(True), automation)
        return f"automatizacion borrada: {info.get('name')} ({automation})"


def _schema(props: dict, required: list[str] | None = None) -> dict:
    return {"type": "object", "properties": props, "required": required or [], "additionalProperties": False}


_S = {"type": "string"}
_B = {"type": "boolean"}
_I = {"type": "integer"}

# name -> (riesgo, resumen, esquema, metodo)
REGISTRY: dict[str, tuple[str, str, dict, str]] = {
    "dfemu_guide": ("read", "Mapa de tareas: por donde empezar y en que orden usar el resto.", _schema(
        {"mode": {"type": "string", "enum": list(GUIDE), "default": "overview"}}), "guide"),
    "dfemu_status": ("read", "Que objetos emu_ hay ahora en el espacio de pruebas.", _schema({}), "status"),
    "dfemu_flow_list": ("read", "Flujos visibles y cuales llevan prefijo emu_.", _schema({}), "flow_list"),
    "dfemu_flow_get": ("read", "Grafo de un flujo: resumen de nodos o el .dfw completo.", _schema(
        {"flow": _S, "format": {"type": "string", "enum": ["summary", "graph"], "default": "summary"}},
        ["flow"]), "flow_get"),
    "dfemu_processors": ("read", "Catalogo de processors y que casos tienen medidos.", _schema({}), "processors"),
    "dfemu_script_translate": ("read", "Traduce un script de Qlik a SQL de DuckDB.", _schema(
        {"qvs": _S, "path": _S}), "script_translate"),
    "dfemu_docs_search": ("read", "Busca texto en la documentacion descargada de help.qlik.com.", _schema(
        {"query": _S, "limit": _I}, ["query"]), "docs_search"),
    "dfemu_battery_cases": ("read", "Casos de la bateria de processors.", _schema({}), "battery_cases"),
    "dfemu_flow_push": ("write", "Sube un grafo a un clon emu_ del flujo base.", _schema(
        {"base": _S, "name": _S, "graph": {"type": "object"}, "graph_file": _S}, ["base", "name"]), "flow_push"),
    "dfemu_automation_create": ("write", "Crea una automatizacion emu_.", _schema(
        {"name": _S, "description": _S}, ["name"]), "automation_create"),
    "dfemu_automation_set_enabled": ("write", "Habilita o deshabilita una automatizacion emu_.", _schema(
        {"automation": _S, "enabled": _B}, ["automation"]), "automation_set_enabled"),
    "dfemu_automation_runs": ("read", "Ejecuciones de una automatizacion.", _schema(
        {"automation": _S}, ["automation"]), "automation_runs"),
    "dfemu_automation_run": ("execute", "Ejecuta una automatizacion emu_ (exige confirm).", _schema(
        {"automation": _S, "context": _S, "confirm": _B}, ["automation"]), "automation_run"),
    "dfemu_battery_run": ("execute", "Mide un caso de la bateria contra el tenant (exige confirm).", _schema(
        {"case": _S, "confirm": _B}, ["case"]), "battery_run"),
    # ----- edicion de grafos (API) -----
    "dfemu_flow_clone": ("write", "Clona un flujo base en un flujo emu_ nuevo.", _schema(
        {"base": _S, "name": _S}, ["base", "name"]), "flow_clone"),
    "dfemu_flow_add_node": ("write", "Inserta un processor tras un nodo y sube el grafo (acepta el tipo o el nombre de la paleta).",
                            _schema({"flow": _S, "type": _S, "after": _S, "config": {"type": "object"}, "label": _S},
                                    ["flow", "type", "after"]), "flow_add_node"),
    "dfemu_flow_set_node": ("write", "Mezcla configuracion en un nodo existente.", _schema(
        {"flow": _S, "node": _S, "config": {"type": "object"}, "label": _S}, ["flow", "node"]), "flow_set_node"),
    "dfemu_flow_remove_node": ("write", "Quita un nodo y reconecta sus aristas.", _schema(
        {"flow": _S, "node": _S}, ["flow", "node"]), "flow_remove_node"),
    "dfemu_flow_backup": ("read", "Guarda el .dfw actual en out/backups y devuelve la ruta.", _schema(
        {"flow": _S}, ["flow"]), "flow_backup"),
    "dfemu_flow_restore": ("write", "Sube un grafo guardado (backup) a un flujo emu_.", _schema(
        {"flow": _S, "file": _S}, ["flow", "file"]), "flow_restore"),
    # ----- Qlik script -----
    "dfemu_script_get": ("read", "Script de Qlik actual de una app emu_.", _schema({"app": _S}, ["app"]), "script_get"),
    "dfemu_script_set": ("write", "Sube un script de Qlik a una app emu_ (texto o archivo).", _schema(
        {"app": _S, "script": _S, "path": _S}, ["app"]), "script_set"),
    "dfemu_script_validate": ("read", "Pide al servidor que valide un script (no escribe).", _schema(
        {"script": _S, "path": _S}), "script_validate"),
    # ----- automatizaciones -----
    "dfemu_automation_show": ("read", "Definicion completa de una automatizacion.", _schema(
        {"automation": _S}, ["automation"]), "automation_show"),
    "dfemu_automation_update": ("write", "Cambia nombre o descripcion de una automatizacion emu_.", _schema(
        {"automation": _S, "name": _S, "description": _S}, ["automation"]), "automation_update"),
    "dfemu_automation_copy": ("write", "Duplica una automatizacion emu_ con otro nombre emu_.", _schema(
        {"automation": _S, "name": _S}, ["automation", "name"]), "automation_copy"),
    "dfemu_automation_stop": ("execute", "Para una ejecucion en curso (exige confirm).", _schema(
        {"automation": _S, "run_id": _S, "confirm": _B}, ["automation", "run_id"]), "automation_stop"),
    # ----- tareas de recarga -----
    "dfemu_task_list": ("read", "Tareas de recarga programadas de una app emu_.", _schema({"app": _S}, ["app"]), "task_list"),
    "dfemu_task_schedule": ("write", "Programa una recarga con una regla RRULE.", _schema(
        {"app": _S, "name": _S, "recurrence": _S, "timezone": _S, "enabled": _B},
        ["app", "name", "recurrence"]), "task_schedule"),
    "dfemu_task_start": ("execute", "Arranca una tarea habilitada (exige confirm).", _schema(
        {"task": _S, "confirm": _B}, ["task"]), "task_start"),
    "dfemu_task_set_enabled": ("write", "Habilita o deshabilita una tarea.", _schema(
        {"task": _S, "enabled": _B}, ["task"]), "task_set_enabled"),
    "dfemu_task_delete": ("destructive", "Borra una tarea de recarga (exige confirm y permiso).", _schema(
        {"task": _S, "confirm": _B}, ["task"]), "task_delete"),
    # ----- emulador local -----
    "dfemu_emulate": ("read", "Ejecuta un .dfw en el emulador local y resume lo escrito.", _schema(
        {"file": _S, "data_dir": _S, "head": _I}, ["file"]), "emulate"),
    "dfemu_flow_reload": ("execute", "Recarga un flujo emu_ y sigue el estado hasta el final (exige confirm).", _schema(
        {"flow": _S, "timeout": {"type": "number", "default": 180}, "confirm": _B}, ["flow"]), "flow_reload"),
    "dfemu_flow_delete": ("destructive", "Borra un flujo emu_ (exige confirm y permiso).", _schema(
        {"flow": _S, "confirm": _B}, ["flow"]), "flow_delete"),
    "dfemu_automation_delete": ("destructive", "Borra una automatizacion emu_ (exige confirm y permiso).", _schema(
        {"automation": _S, "confirm": _B}, ["automation"]), "automation_delete"),
}


class Server:
    def __init__(self, tools: Tools | None = None, env: dict | None = None, state_dir: Path | None = None):
        self.tools = tools or Tools()
        self.env = dict(os.environ if env is None else env)
        self.tools.env = self.env  # el simulacro global tambien lo ve el emulador
        self.state_dir = Path(state_dir) if state_dir else Path(self.env.get("DFEMU_MCP_STATE_DIR") or
                                                               self.tools.root / ".dfemu-mcp")

    # ----- permisos y auditoria -----
    def check(self, name: str, args: dict) -> str:
        if name not in REGISTRY:
            raise Failed(f"herramienta desconocida `{name}`")
        risk = REGISTRY[name][0]
        if risk == "read":
            return risk
        if risk == "write":
            if self.env.get("DFEMU_MCP_ALLOW_WRITE", "1") == "0":
                raise Denied("escritura deshabilitada (DFEMU_MCP_ALLOW_WRITE=0)")
            return risk
        if risk == "execute":
            if self.env.get("DFEMU_MCP_ALLOW_EXECUTE", "1") == "0":
                raise Denied("ejecucion deshabilitada (DFEMU_MCP_ALLOW_EXECUTE=0)")
            if args.get("confirm") is not True:
                raise Denied(f"`{name}` ejecuta en el tenant: repite la llamada con confirm=true")
            return risk
        if self.env.get("DFEMU_MCP_ALLOW_DESTRUCTIVE", "0") != "1":
            raise Denied("borrado deshabilitado (DFEMU_MCP_ALLOW_DESTRUCTIVE=1 para habilitarlo)")
        if args.get("confirm") is not True:
            raise Denied(f"`{name}` borra en el tenant: repite la llamada con confirm=true")
        return risk

    def audit(self, name: str, risk: str, ok: bool, ms: int) -> None:
        try:
            self.state_dir.mkdir(parents=True, exist_ok=True)
            with (self.state_dir / "audit.jsonl").open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "tool": name,
                                     "risk": risk, "ok": ok, "ms": ms}, ensure_ascii=False) + "\n")
        except OSError:
            pass  # la auditoria nunca tumba una llamada

    def call(self, name: str, args: dict) -> dict:
        started = time.monotonic()
        risk = "read"
        try:
            risk = self.check(name, args)
            method = getattr(self.tools, REGISTRY[name][3])
            allowed = {k: v for k, v in args.items() if k != "confirm"}
            out = method(**allowed)
            self.audit(name, risk, True, int((time.monotonic() - started) * 1000))
            return _text(out)
        except (Denied, Failed, TypeError, ValueError) as e:
            self.audit(name, risk, False, int((time.monotonic() - started) * 1000))
            return {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True}
        except Exception as e:  # noqa: BLE001 - el cliente ve el fallo, no la traza
            from .bridge import DryRun

            if isinstance(e, DryRun):  # simulacro: no se escribio nada
                self.audit(name, risk, True, int((time.monotonic() - started) * 1000))
                return _text(f"simulado: {e.method} {e.path} (activa las escrituras con DFEMU_MCP_APPLY=1)")
            self.audit(name, risk, False, int((time.monotonic() - started) * 1000))
            return {"content": [{"type": "text", "text": f"error: {type(e).__name__}: {e}"}], "isError": True}

    def list_tools(self) -> list[dict]:
        return [{"name": n, "description": d, "inputSchema": s} for n, (_r, d, s, _m) in REGISTRY.items()]

    # ----- protocolo -----
    def handle(self, msg: dict) -> dict | None:
        method = msg.get("method")
        mid = msg.get("id")
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "protocolVersion": msg.get("params", {}).get("protocolVersion") or PROTOCOL,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": SERVER,
                "instructions": "Llama primero a dfemu_guide; toda escritura va a objetos emu_ y queda auditada."}}
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": mid, "result": {"tools": self.list_tools()}}
        if method == "tools/call":
            p = msg.get("params") or {}
            return {"jsonrpc": "2.0", "id": mid, "result": self.call(str(p.get("name")), p.get("arguments") or {})}
        if method == "ping":
            return {"jsonrpc": "2.0", "id": mid, "result": {}}
        if mid is None:  # notificacion (p. ej. notifications/initialized): no se responde
            return None
        return {"jsonrpc": "2.0", "id": mid,
                "error": {"code": -32601, "message": f"metodo no soportado: {method}"}}

    def serve(self, stdin=None, stdout=None) -> None:
        fin, fout = stdin or sys.stdin, stdout or sys.stdout
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                fout.write(json.dumps({"jsonrpc": "2.0", "id": None,
                                       "error": {"code": -32700, "message": "no es JSON"}}) + "\n")
                fout.flush()
                continue
            resp = self.handle(msg)
            if resp is not None:
                fout.write(json.dumps(resp, ensure_ascii=False) + "\n")
                fout.flush()


DOCS_INI, DOCS_FIN = "<!-- herramientas:inicio -->", "<!-- herramientas:fin -->"


def markdown_table() -> str:
    """Tabla del catalogo para docs/MCP.md: una fila por herramienta, generada del registro."""
    rows = [DOCS_INI, "| Herramienta | Riesgo | Para qué |", "| --- | --- | --- |"]
    rows += [f"| `{n}` | {r} | {d} |" for n, (r, d, _s, _m) in sorted(REGISTRY.items())]
    rows.append(DOCS_FIN)
    return chr(10).join(rows)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--markdown" in argv:
        print(markdown_table())
        return 0
    if "--list" in argv:
        for name, (risk, desc, _s, _m) in REGISTRY.items():
            print(f"{name:32} {risk:12} {desc}")
        return 0
    Server().serve()
    return 0
