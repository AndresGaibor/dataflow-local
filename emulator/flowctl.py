"""`dfemu flow`: control de flujos del tenant pensado para agentes.

Salida compacta (una linea por nodo) para no llenar el contexto, copia de seguridad antes de cada
escritura y sin API key: usa la sesion de Chrome ya iniciada en Qlik Cloud, a traves de
`playwright-cli` (docs/banco-de-pruebas/03-control-de-flujos.md). Las escrituras exigen --apply.
"""
import argparse
import copy
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
import uuid

from .bridge import PREFIX, ROOT, SANDBOX_SPACE_ID, valid_id

SESSION = os.environ.get("DFEMU_BROWSER_SESSION", "chrome")
BACKUPS = os.path.join(ROOT, "out", "backups")
MAX_STALE_PUTS = 6  # igual que Remote.push_graph: un PUT mas por cada nivel de calculate-fields encadenado
# Catalogo de los 24 procesadores de la paleta: tipo -> {palette, label, in, out, cfg inicial}, medido con scripts/ui_probe.py
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "processors.json"), encoding="utf-8") as _f:
    PROCESSORS = json.load(_f)
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


class FlowError(Exception):
    pass


# --- transporte: fetch desde la pestana de Qlik Cloud de tu Chrome -----------------------------
_JS = r"""async page => {
  const p = page.context().pages().find(x => /qlikcloud\.com/.test(x.url()));
  if (!p) return JSON.stringify({status: 0, body: 'no hay pestana de Qlik Cloud abierta'});
  return JSON.stringify(await p.evaluate(async ([m, path, body]) => {
    const h = {'content-type': 'application/json'};
    if (m !== 'GET') h['qlik-csrf-token'] = (await fetch('/api/v1/csrf-token')).headers.get('qlik-csrf-token');
    const r = await fetch('/api/' + path, {method: m, headers: h, body: body === null ? undefined : JSON.stringify(body)});
    return {status: r.status, body: await r.text()};
  }, ARGS));
}"""


def run_js(script: str):
    """Corre un `async page => ...` en la sesion de playwright-cli y devuelve su valor ya decodificado."""
    fd, tmp = tempfile.mkstemp(suffix=".js")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(script)
    try:
        p = subprocess.run(["playwright-cli", f"-s={SESSION}", "--raw", "run-code", f"--filename={tmp}"],
                           capture_output=True, text=True, encoding="utf-8", stdin=subprocess.DEVNULL, timeout=90, shell=os.name == "nt")
    except (OSError, subprocess.TimeoutExpired) as e:
        raise FlowError(f"playwright-cli no responde: {e}") from e
    finally:
        os.remove(tmp)
    try:
        value = json.loads(p.stdout)
    except ValueError as e:
        raise FlowError(f"sesion '{SESSION}' no disponible (attach: playwright-cli attach --cdp=chrome): {(p.stdout + p.stderr)[:200]}") from e
    if isinstance(value, str):  # el script devolvio JSON.stringify(...): se decodifica la segunda vez
        try:
            value = json.loads(value)
        except ValueError:
            pass
    return value


def call(method: str, path: str, body=None):
    r = run_js(_JS.replace("ARGS", json.dumps([method, path, body])))
    if r["status"] == 0 or r["status"] >= 400:
        raise FlowError(f"{method} {path} -> {r['status']}: {r['body'][:300]}")
    return json.loads(r["body"]) if r["body"].strip() else None  # el sobre {status, body} lo pone _JS


# --- captura de los cuerpos que solo manda la interfaz ---------------------------------------
# La interfaz arma en el cliente los cuerpos de pivot, map-fields, subflow, nodo script, datasource
# e import/export: por API ese cuerpo no se puede adivinar (ADF-500). Este grabador los recoge de la
# pestana de Qlik Cloud ya abierta, que es la unica fuente que queda.
_CAPTURE_START = r"""async page => {
  const p = page.context().pages().find(x => /qlikcloud\.com/.test(x.url()));
  if (!p) return JSON.stringify({ok: false, msg: 'no hay pestana de Qlik Cloud abierta'});
  const n = await p.evaluate(() => {
    if (window.__dfemuCap) return window.__dfemuCap.length;
    window.__dfemuCap = [];
    const push = (o) => { try { window.__dfemuCap.push(o); } catch (e) {} };
    const of = window.fetch;
    window.fetch = async (...a) => {
      let url = '', method = 'GET', body = null;
      try { const t = a[0]; url = typeof t === 'string' ? t : (t && t.url) || ''; const o = a[1] || {};
            method = o.method || (t && t.method) || 'GET'; body = o.body === undefined ? null : String(o.body); } catch (e) {}
      const r = await of(...a);
      let text = null;
      try { text = await r.clone().text(); } catch (e) {}
      push({url, method, req: body, status: r.status, res: text});
      return r;
    };
    const oo = XMLHttpRequest.prototype.open, os = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.open = function (m, u) { this.__m = m; this.__u = u; return oo.apply(this, arguments); };
    XMLHttpRequest.prototype.send = function (b) {
      const self = this;
      this.addEventListener('load', () => push({url: String(self.__u), method: self.__m,
        req: typeof b === 'string' ? b : null, status: self.status, res: self.responseText || ''}));
      return os.apply(this, arguments);
    };
    return 0;
  });
  return JSON.stringify({ok: true, n, msg: 'grabador activo: haz la accion en la interfaz y luego `dfemu flow capture dump`'});
}"""

_CAPTURE_DUMP = r"""async page => {
  const p = page.context().pages().find(x => /qlikcloud\.com/.test(x.url()));
  if (!p) return JSON.stringify({ok: false, msg: 'no hay pestana de Qlik Cloud abierta', items: []});
  const items = await p.evaluate(() => window.__dfemuCap || []);
  return JSON.stringify({ok: true, items});
}"""


def capture_summary(items: list, only: str = "") -> str:
    """Una linea por peticion. La URL sale sin host: el host lleva el tenant."""
    rows = []
    for it in items:
        url = re.sub(r"^https?://[^/]+", "", str(it.get("url") or ""))
        if only and only not in url:
            continue
        rows.append(f"{str(it.get('method')):6} {url[:78]:78} {it.get('status')}  "
                    f"req {len(it.get('req') or ''):6}  res {len(it.get('res') or ''):6}")
    return "\n".join(rows) or "sin peticiones capturadas"


def capture(action: str, only: str = "", out: str = "") -> str:
    """start: instala el grabador; dump: vuelca lo capturado (con `out`, guarda el JSON completo)."""
    if action == "start":
        r = run_js(_CAPTURE_START)
        return r.get("msg") if r.get("ok") else f"error: {r.get('msg')}"
    if action != "dump":
        raise FlowError(f"accion de captura desconocida: {action}")
    r = run_js(_CAPTURE_DUMP)
    if not r.get("ok"):
        raise FlowError(r.get("msg") or "no se pudo leer la captura")
    items = r.get("items") or []
    if out:
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=1)
        return f"{capture_summary(items, only)}\n\n{len(items)} peticiones guardadas en {out}"
    return capture_summary(items, only)


# --- politica de escritura ------------------------------------------------------------------
def _allowed_names() -> set:
    """Nombres extra autorizados por el usuario en dfemu.local.json (ignorado por git): `allow_flows`."""
    try:
        with open(os.path.join(ROOT, "dfemu.local.json"), encoding="utf-8") as f:
            return set(json.load(f).get("allow_flows", []))
    except (OSError, ValueError):
        return set()


def check_writable(df: dict) -> None:
    name = df.get("name", "")
    if name in _allowed_names():
        return
    app = valid_id(aid := (df.get("context") or {}).get("dataAppId", "")) and call("GET", f"v1/apps/{aid}") or {}
    attrs = app.get("attributes") or {}
    if not (str(attrs.get("name", "")).startswith(PREFIX) and attrs.get("spaceId") == SANDBOX_SPACE_ID):
        raise FlowError(f"'{name}' no se puede escribir: no es emu_* del espacio de pruebas ni esta en allow_flows de dfemu.local.json")


# --- operaciones sobre el grafo (puras) -------------------------------------------------------
def find_node(g: dict, ref: str) -> dict:
    hits = [n for n in g["nodes"] if n["id"].startswith(ref) or n["label"].lower() == ref.lower()]
    if len(hits) != 1:
        raise FlowError(f"nodo '{ref}': {len(hits)} coincidencias entre {[n['id'][:8] + ' ' + n['label'] for n in g['nodes']]}")
    return hits[0]


def _handle(n: dict, side: str, kind: str = "DEFAULT"):
    return next((h for h in (n.get("handles") or {}).get(side, []) if h["type"] == kind), None)


def _edge(g: dict, sh: str, th: str) -> dict:
    owner = {h["id"]: n["id"] for n in g["nodes"] for s in (n.get("handles") or {}).values() for h in s}
    return {"id": f"reactflow__edge-{owner[sh]}{sh}-{owner[th]}{th}", "sourceHandle": sh, "targetHandle": th}


REQ_IN = {"map-fields": ["LOOKUP"]}  # medido: el servidor exige la entrada LOOKUP conectada


def _ref_handle(g: dict, ref: str) -> dict:
    """`nodo` o `nodo:PUERTO` -> el handle de salida que se conecta."""
    node, _, port = ref.partition(":")
    h = _handle(find_node(g, node), "outgoing", port or "DEFAULT")
    if not h:
        raise FlowError(f"'{node}' no tiene salida {port or 'DEFAULT'}")
    return h


def add_node(g: dict, ctype: str, after: str, label: str, cfg: dict, feeds: dict | None = None) -> dict:
    """Inserta un procesador tras `after`: todo lo que colgaba de su salida DEFAULT pasa a colgar del nuevo.

    `feeds` conecta entradas extra por tipo de puerto: {"LOOKUP": "filtro:REJECT"}. Las que el servidor
    exige (REQ_IN) y queden al aire se rechazan aqui, para no subir un grafo que el tenant marca INVALID
    con NODE_TOPOLOGY_NOT_FULFILLED.
    """
    g = copy.deepcopy(g)
    a = find_node(g, after)
    out = _handle(a, "outgoing")
    if not out:
        raise FlowError(f"'{a['label']}' no tiene salida")
    spec = PROCESSORS.get(ctype, {"in": ["DEFAULT"], "out": ["DEFAULT"], "cfg": {}})  # tipo desconocido: un puerto de cada
    new_id = str(uuid.uuid4())
    ins = [{"id": str(uuid.uuid4()), "type": t} for t in spec["in"]]
    outs = [{"id": str(uuid.uuid4()), "type": t} for t in spec["out"]]
    h_in, h_out = next((h["id"] for h in ins if h["type"] == "DEFAULT"), ins[0]["id"]), outs[0]["id"]  # `script` solo tiene entradas OPTIONAL
    base = copy.deepcopy(spec["cfg"])
    cfg = merge(base, {**cfg, "$state": cfg.get("$state", "CONFIGURED")}) if cfg else base  # con configuracion propia pasa a CONFIGURED
    pos = a["graphical"]["position"]
    nuevo = {
        "type": "processor", "id": new_id, "label": label,
        "graphical": {"position": {"x": pos["x"] + 160, "y": pos["y"] + 140}},
        "handles": {"incoming": ins, "outgoing": outs},
        "component": {"type": ctype, "properties": {"configuration": cfg}}}
    g["nodes"].append(nuevo)
    for e in g["edges"]:
        if e["sourceHandle"] == out["id"]:
            e["sourceHandle"] = h_out
    for e in g["edges"]:
        e.update(_edge(g, e["sourceHandle"], e["targetHandle"]))
    g["edges"].append(_edge(g, out["id"], h_in))
    for port, ref in (feeds or {}).items():
        th = _handle(nuevo, "incoming", port)
        if not th:
            raise FlowError(f"'{label}' no tiene entrada {port}; sus entradas son {[h['type'] for h in ins]}")
        g["edges"].append(_edge(g, _ref_handle(g, ref)["id"], th["id"]))
    al_aire = [p for p in REQ_IN.get(ctype, [])
               if (h := _handle(nuevo, "incoming", p)) and not any(e["targetHandle"] == h["id"] for e in g["edges"])]
    if al_aire:  # el servidor lo marca NODE_TOPOLOGY_NOT_FULFILLED, asi que se dice antes de subirlo
        raise FlowError(f"{ctype} necesita {' y '.join(al_aire)} conectada: pasa feeds={{'{al_aire[0]}': 'nodo[:PUERTO]'}}")
    return g


def merge(dst: dict, patch: dict) -> dict:
    for k, v in patch.items():
        dst[k] = merge(dst[k], v) if isinstance(dst.get(k), dict) and isinstance(v, dict) else v
    return dst


def set_node(g: dict, ref: str, cfg: dict, label: str | None) -> dict:
    g = copy.deepcopy(g)
    n = find_node(g, ref)
    if cfg:
        merge(n["component"].setdefault("properties", {}).setdefault("configuration", {}), cfg)
    if label:
        n["label"] = label
    return g


def remove_node(g: dict, ref: str) -> dict:
    """Quita el nodo y reconecta lo que llegaba con lo que salia por DEFAULT; lo de REJECT se descarta."""
    g = copy.deepcopy(g)
    n = find_node(g, ref)
    hs = {h["id"]: h["type"] for s in (n.get("handles") or {}).values() for h in s}
    ins = [e for e in g["edges"] if e["targetHandle"] in hs]
    outs = [e for e in g["edges"] if e["sourceHandle"] in hs and hs[e["sourceHandle"]] == "DEFAULT"]
    g["edges"] = [e for e in g["edges"] if e not in ins and e["sourceHandle"] not in hs]
    g["nodes"] = [x for x in g["nodes"] if x["id"] != n["id"]]
    g["edges"] += [_edge(g, i["sourceHandle"], o["targetHandle"]) for i in ins for o in outs]
    return g


# --- lectura compacta -------------------------------------------------------------------------
def _cfg(n: dict, full: bool) -> str:
    c = {k: v for k, v in ((n["component"].get("properties") or {}).get("configuration") or {}).items() if k != "$state"}
    s = json.dumps(c, ensure_ascii=False, separators=(",", ":"))
    return s if full or len(s) <= 90 else s[:87] + "..."


def render(df: dict, full: bool = False) -> str:
    g = df["graph"]
    v = df["validity"]
    lines = [f"{df['name']}  {v['status']}  df={df['id'][:8]}  {len(g['nodes'])} nodos"]
    lines += [f"{n['id'][:8]} {n['type']}/{n['component']['type']}  {n['label']}  {_cfg(n, full)}" for n in g["nodes"]]
    own = {h["id"]: (n["id"][:8], h["type"]) for n in g["nodes"] for s in (n.get("handles") or {}).values() for h in s}
    lines.append("aristas: " + " ".join(f"{own[e['sourceHandle']][0]}{'~>' if own[e['sourceHandle']][1] == 'REJECT' else '>'}{own[e['targetHandle']][0]}" for e in g["edges"]))
    lines += [f"! {x.get('nodeId', '')[:8]} {x.get('code')}" for x in v.get("nodesConstraintViolations") or []]
    return "\n".join(lines)


# --- flujos -----------------------------------------------------------------------------------
def resolve(ref: str) -> dict:
    if UUID.fullmatch(ref):
        try:
            return call("GET", f"v1/dataflows/{call('GET', f'v1/dataflow-apps/{ref}')['dataflowId']}")
        except FlowError:
            return call("GET", f"v1/dataflows/{ref}")
    items = call("GET", "v1/items?resourceType=app&limit=100&name=" + urllib.parse.quote(ref)) or {}
    hits = [i for i in (items.get("data") or []) if i.get("name") == ref and i.get("resourceSubType") == "dataflow-prep"]
    if len(hits) != 1:
        raise FlowError(f"flujo '{ref}': {len(hits)} coincidencias; use el id")
    return resolve((hits[0].get("resourceAttributes") or {}).get("id") or hits[0]["resourceId"])


def backup(df: dict) -> str:
    os.makedirs(BACKUPS, exist_ok=True)
    path = os.path.join(BACKUPS, f"{re.sub(r'[^A-Za-z0-9_-]+', '_', df['name'])}-{time.strftime('%Y%m%d-%H%M%S')}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(df, f, ensure_ascii=False, indent=1)
    return path


def push(df: dict, graph: dict, apply: bool) -> str:
    check_writable(df)
    os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
    with open(os.path.join(ROOT, "out", "audit.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.strftime("%FT%T"), "method": "PUT", "path": f"v1/dataflows/{df['id']}", "applied": apply, "via": "browser"}) + "\n")
    if not apply:
        return f"[simulacion] {len(df['graph']['nodes'])} -> {len(graph['nodes'])} nodos; use --apply"
    saved = backup(df)
    cur = df
    for _ in range(MAX_STALE_PUTS):
        body = {k: v for k, v in cur.items() if k != "validity"}
        body["graph"] = graph
        cur = call("PUT", f"v1/dataflows/{df['id']}", body)
        codes = {x.get("code") for x in cur["validity"].get("nodesConstraintViolations") or []}
        if codes != {"POTENTIAL_STALE_EXPRESSION"}:  # un PUT identico lo limpia (receta de CLAUDE.md)
            break
    return f"{render(cur)}\ncopia: {os.path.relpath(saved, ROOT)}"


def _json(s: str) -> dict:
    try:
        v = json.loads(s or "{}")
    except ValueError as e:
        raise FlowError(f"--cfg no es JSON: {e}") from e
    if not isinstance(v, dict):
        raise FlowError("--cfg debe ser un objeto JSON")
    return v


def run(a) -> str:
    if a.action == "ls":
        items = call("GET", "v1/items?resourceType=app&limit=100") or {}
        return "\n".join(f"{(i.get('resourceAttributes') or {}).get('id') or i['resourceId']}  {i['name']}"
                         for i in items.get("data", []) if i.get("resourceSubType") == "dataflow-prep")
    if a.action == "types":
        return "\n".join(f"{t:17} {s['palette']:18} in={','.join(s['in'])} out={','.join(s['out'])}" for t, s in PROCESSORS.items())
    if a.action == "capture":  # no necesita un flujo: trabaja sobre la pestana abierta
        return capture(a.step, a.only, a.save)
    df = resolve(a.flow)
    if a.action == "show":
        return render(df, a.full)
    if a.action == "node":
        return json.dumps(find_node(df["graph"], a.node), ensure_ascii=False, indent=1)
    if a.action == "backup":
        return backup(df)
    if a.action == "add":
        t = next((k for k, s in PROCESSORS.items() if a.type in (k, s["palette"])), a.type)  # acepta el tipo o el nombre de la paleta
        feeds = {}
        for f in a.feed or []:
            port, _, ref = f.partition("=")
            if not port or not ref:
                raise FlowError(f"--feed espera PUERTO=NODO[:PUERTO], no '{f}'")
            feeds[port] = ref
        g = add_node(df["graph"], t, a.after, a.label or PROCESSORS.get(t, {}).get("label", t), _json(a.cfg), feeds)
    elif a.action == "set":
        g = set_node(df["graph"], a.node, _json(a.cfg), a.label)
    elif a.action == "rm":
        g = remove_node(df["graph"], a.node)
    elif a.action == "restore":
        with open(a.file, encoding="utf-8") as f:
            data = json.load(f)
        g = data.get("d", data)["graph"]  # acepta tanto `flow backup` como el volcado {a, d} de la primera copia
    return push(df, g, a.apply)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="dfemu flow", description="Control compacto de flujos (sesion de Chrome via playwright-cli)")
    sub = ap.add_subparsers(dest="action", required=True)
    w = argparse.ArgumentParser(add_help=False)
    w.add_argument("--apply", action="store_true", help="escribir en el tenant (sin esto solo simula)")
    sub.add_parser("ls", help="flujos: id y nombre")
    sub.add_parser("types", help="los 24 procesadores de la paleta: tipo, nombre en la interfaz y puertos")
    c = sub.add_parser("capture", help="graba los cuerpos que manda la interfaz (pivot, datasource, import/export...)")
    c.add_argument("step", choices=["start", "dump"])
    c.add_argument("--only", default="", help="dump: solo peticiones cuya URL contenga este texto")
    c.add_argument("--save", default="", help="dump: guarda el JSON completo en esta ruta")
    for name, hlp in (("show", "nodos y aristas en pocas lineas"), ("node", "JSON completo de un nodo"), ("backup", "guarda el flujo en out/backups")):
        s = sub.add_parser(name, help=hlp)
        s.add_argument("flow", help="id (app o dataflow) o nombre exacto")
        if name == "show":
            s.add_argument("--full", action="store_true", help="configuracion completa de cada nodo")
        if name == "node":
            s.add_argument("node", help="prefijo del id o etiqueta")
    s = sub.add_parser("add", help="inserta un procesador tras un nodo", parents=[w])
    s.add_argument("flow"), s.add_argument("type", help="p. ej. filter, field-selector")
    s.add_argument("--after", required=True), s.add_argument("--label"), s.add_argument("--cfg", help="JSON de la configuracion")
    s.add_argument("--feed", action="append", metavar="PUERTO=NODO[:PUERTO]",
                   help="conecta una entrada extra (p. ej. LOOKUP=filtro:REJECT); el servidor exige la LOOKUP de map-fields")
    s = sub.add_parser("set", help="mezcla configuracion en un nodo", parents=[w])
    s.add_argument("flow"), s.add_argument("node"), s.add_argument("--cfg", default="{}"), s.add_argument("--label")
    s = sub.add_parser("rm", help="quita un nodo y reconecta", parents=[w])
    s.add_argument("flow"), s.add_argument("node")
    s = sub.add_parser("restore", help="vuelve a un backup", parents=[w])
    s.add_argument("flow"), s.add_argument("file")
    sys.stdout.reconfigure(encoding="utf-8")  # las etiquetas llevan tildes; la consola de Windows no es UTF-8
    try:
        print(run(ap.parse_args(argv)))
    except FlowError as e:
        sys.exit(f"error: {e}")
    return 0
