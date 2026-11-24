"""`dfemu ui`: maneja el editor de Data Flows abierto en tu Chrome, con salida de texto (sin capturas).

Trabaja sobre la pestana del editor tal como esta: nunca la recarga (se pierde el estado) y no escribe por API
mientras esta abierta. Lo que la interfaz guarda sola se lee despues con `dfemu flow show`.
Cada accion es un `playwright-cli run-code` contra la pestana activa de la sesion de `flowctl.SESSION`.
Detalle y trampas medidas: docs/banco-de-pruebas/04-control-de-chrome.md.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

from . import flowctl

# Utilidades dentro de la pagina. `ref` de un nodo: prefijo de su id o su etiqueta exacta.
_PRE = r"""
const A = ARGS;
const nodeId = ref => page.evaluate(ref => {
  const m = [...document.querySelectorAll('.react-flow__node')].filter(n => n.dataset.id.startsWith(ref) || n.innerText.split('\n')[0].trim().toLowerCase() === ref.toLowerCase());
  if (m.length !== 1) throw new Error('nodo "' + ref + '": ' + m.length + ' coincidencias');
  return m[0].dataset.id;
}, ref);
const nodeLoc = async ref => page.locator(`.react-flow__node[data-id="${await nodeId(ref)}"]`);
const press = async (x, y) => { await page.mouse.move(x, y); await page.mouse.down(); await page.waitForTimeout(80); await page.mouse.up(); };
const center = b => ({x: b.x + b.width / 2, y: b.y + b.height / 2});
const dragTo = async (x1, y1, x2, y2) => { await page.mouse.move(x1, y1); await page.mouse.down(); await page.mouse.move(x2, y2, {steps: 15}); await page.mouse.up(); };
const tab = async name => { await page.getByRole('tab', {name}).evaluate(e => e.getAttribute('aria-selected') === 'true' || e.click()); await page.waitForTimeout(700); };  // pulsar la pestana activa pliega la paleta
const edgeMid = (src, dst = '') => page.evaluate(([src, dst]) => {
  const g = [...document.querySelectorAll(`g.react-flow__edge[aria-label^="Edge from ${src}"]`)].find(e => !dst || e.getAttribute('aria-label').includes(' to ' + dst));
  const p = g && g.querySelector('path.react-flow__edge-path');
  if (!p) throw new Error('no hay arista ' + src + '>' + dst);
  const q = p.ownerSVGElement.createSVGPoint(), l = p.getPointAtLength(p.getTotalLength() / 2);
  q.x = l.x; q.y = l.y; const r = q.matrixTransform(p.getScreenCTM()); return {x: r.x, y: r.y};
}, [src, dst]);
const clickText = async (text, last = true) => { const l = page.getByText(text, {exact: true}); const b = await (last ? l.last() : l.first()).boundingBox(); await press(b.x + b.width / 2, b.y + b.height / 2); };
"""

_JS = {
    "state": r"""
  const nodes = await page.evaluate(() => [...document.querySelectorAll('.react-flow__node')].map(n => { const r = n.getBoundingClientRect(); return n.dataset.id.slice(0, 8) + '  ' + n.innerText.split('\n').slice(0, 3).join(' / ') + '  @' + Math.round(r.x) + ',' + Math.round(r.y); }));
  const edges = await page.evaluate(() => [...document.querySelectorAll('g.react-flow__edge')].map(g => g.getAttribute('aria-label').replace(/Edge from (\w{8})\S* to (\w{8}).*/, '$1>$2')));
  const st = await page.evaluate(() => { const e = [...document.querySelectorAll('*')].find(x => !x.children.length && /^Flujo (de datos no )?v[aá]lido/.test(x.textContent.trim())); return e ? e.textContent.trim() : '?'; });
  return st + '\n' + nodes.join('\n') + '\naristas: ' + edges.join(' ');""",
    "select": r"""
  const b = await (await nodeLoc(A.node)).boundingBox(); await press(b.x + b.width / 2, b.y + 8); await page.waitForTimeout(700); return 'ok';""",
    "panel": r"""
  return (await page.evaluate(() => [...document.querySelectorAll('input, button, textarea, select, [role=combobox], [role=switch], [role=checkbox], [role=radio]')].filter(e => { const r = e.getBoundingClientRect(); return r.x > 1230 && r.y > 100 && r.width > 0; }).map(e => { const lab = e.getAttribute('aria-label') || (e.labels && e.labels[0] && e.labels[0].innerText) || e.placeholder || ''; return (e.getAttribute('role') || e.tagName.toLowerCase()) + ' | ' + lab.trim().slice(0, 40) + ' | ' + (e.value || e.textContent || '').trim().slice(0, 40); }))).join('\n');""",
    "fill": r"""
  await page.evaluate(() => document.querySelectorAll('[data-ui]').forEach(e => e.removeAttribute('data-ui')));
  const role = await page.evaluate(l => { const e = [...document.querySelectorAll('input, textarea, [role=combobox]')].find(x => x.getBoundingClientRect().x > 1230 && [x.getAttribute('aria-label'), x.labels && x.labels[0] && x.labels[0].innerText, x.placeholder].some(t => (t || '').trim().startsWith(l))); if (!e) return null; e.setAttribute('data-ui', '1'); return e.getAttribute('role') || e.tagName.toLowerCase(); }, A.label);
  if (!role) throw new Error('no hay control "' + A.label + '" en el panel (ver `dfemu ui panel`)');
  const c = page.locator('[data-ui="1"]'), b = await c.boundingBox();
  if (role === 'combobox') {
    await press(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600);
    for (const v of A.value.split('|')) { await clickText(v); await page.waitForTimeout(300); }  // varios valores: lista separada por |
    await page.keyboard.press('Escape');
  } else {
    await press(b.x + b.width / 2, b.y + b.height / 2); await page.keyboard.press('Control+A'); await page.keyboard.type(A.value); await page.keyboard.press('Tab');
  }
  await page.waitForTimeout(500); return 'ok';""",
    "button": r"""
  const l = page.getByRole('button', {name: A.name, exact: true}).last(); const b = await l.boundingBox(); await press(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(1500); return 'ok';""",
    "rename": r"""
  const id = await nodeId(A.node), n = page.locator(`.react-flow__node[data-id="${id}"]`);
  const b = await n.boundingBox(); await press(b.x + b.width / 2, b.y + 8); await page.waitForTimeout(800);  // el lapiz solo existe con el nodo seleccionado
  await n.locator('button[aria-label="Edit"]').evaluate(e => e.click()); await page.waitForTimeout(500);
  await page.keyboard.press('Control+A'); await page.keyboard.type(A.text); await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  const now = await n.evaluate(e => e.innerText.split('\n')[0].trim());
  if (now !== A.text) throw new Error('el titulo quedo en "' + now + '"'); return 'ok';""",
    "move": r"""
  const b = await (await nodeLoc(A.node)).boundingBox(); const c = center(b);
  await dragTo(c.x, b.y + 8, c.x + A.dx, b.y + 8 + A.dy); await page.waitForTimeout(1000); return 'ok';""",
    "connect": r"""
  const h = async id => { const b = await page.locator(`.react-flow__handle[data-handleid="${id}"]`).boundingBox(); return center(b); };
  const a = await h(A.src), z = await h(A.dst); await dragTo(a.x, a.y, z.x, z.y); await page.waitForTimeout(1500); return 'ok';""",
    "rm": r"""
  const n = await nodeLoc(A.node);  // menu del nodo > Eliminar; la tecla Suprimir no siempre borra
  await n.locator('button').last().evaluate(e => e.click()); await page.waitForTimeout(600); await clickText('Eliminar'); await page.waitForTimeout(1500); return 'ok';""",
    "add": r"""
  await tab('Procesadores');
  await page.evaluate(n => {
    document.querySelectorAll('[data-probe]').forEach(x => x.removeAttribute('data-probe'));
    const e = [...document.querySelectorAll('[role=tabpanel] *')].find(x => x.children.length === 0 && x.offsetParent !== null && (x.textContent || '').replace(/[​\s]/g, '') === n.replace(/\s/g, ''));  // el texto lleva espacios de ancho cero
    if (!e) throw new Error('no hay "' + n + '" en la paleta'); e.setAttribute('data-probe', '1'); e.scrollIntoView();
  }, A.palette);
  const it = await page.locator('[data-probe="1"]').boundingBox(), t = A.edge ? await edgeMid(A.edge) : {x: A.x, y: A.y}, c = center(it);
  await dragTo(c.x, c.y, t.x, t.y); await page.waitForTimeout(2500); return 'ok';""",
    "unlink": r"""
  const t = await edgeMid(A.src, A.dst); await press(t.x, t.y); await page.waitForTimeout(500); await page.keyboard.press('Delete'); await page.waitForTimeout(1200); return 'ok';""",
    "tool": r"""
  const b = await page.getByRole('button', {name: A.name}).first().boundingBox(); await press(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(1200); return 'ok';""",
    "key": r"""
  await page.keyboard.press(A.key); await page.waitForTimeout(1000); return 'ok';""",
    "script": r"""
  if (A.node) { const b = await (await nodeLoc(A.node)).boundingBox(); await press(b.x + b.width / 2, b.y + 8); await page.waitForTimeout(700); }
  const sw = page.getByRole('switch', {name: 'Script'});
  const flip = async () => { const c = await sw.boundingBox(); await press(c.x + c.width / 2, c.y + c.height / 2); await page.waitForTimeout(2200); };
  const was = await sw.evaluate(e => e.checked === true || e.getAttribute('aria-checked') === 'true');
  if (!was) await flip();
  const txt = await page.evaluate(() => {
    const h = [...document.querySelectorAll('div')].find(d => !d.children.length && d.textContent.trim() === 'Instrucción de script');
    for (let p = h; p && (p = p.parentElement);) if (/\bLOAD\b/i.test(p.innerText) && p.innerText.length > 80) return p.innerText;
    return '';
  });
  if (!was) await flip();  // deja el conmutador como estaba
  return txt.split('\n').filter(l => !/^\s*\d+\s*$/.test(l) && l.trim() !== 'Copiar' && l.trim() !== 'Instrucción de script').join('\n');""",
    "preview": r"""
  const b = await (await nodeLoc(A.node)).boundingBox(); await press(b.x + b.width / 2, b.y + 8); await page.waitForTimeout(600);
  if (await page.getByText('Ver una vista previa de los datos').count()) { await clickText('Ver una vista previa de los datos'); await page.waitForTimeout(7000); }
  return await page.evaluate(() => [...document.querySelectorAll('[role=row], tr')].filter(r => r.getBoundingClientRect().y > 480).slice(0, A_N + 1).map(r => [...r.querySelectorAll('[role=columnheader],[role=gridcell],th,td')].map(c => c.innerText.trim()).join(' | ')).join('\n'));""",
}


def run_js(action: str, **args) -> str:
    body = _JS[action].replace("A_N", str(args.get("n", 5)))
    code = "async page => {" + _PRE.replace("ARGS", json.dumps(args)) + body + "\n}"
    fd, tmp = tempfile.mkstemp(suffix=".js")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        p = subprocess.run(["playwright-cli", f"-s={flowctl.SESSION}", "--raw", "run-code", f"--filename={tmp}"], capture_output=True,
                           text=True, encoding="utf-8", stdin=subprocess.DEVNULL, timeout=120, shell=os.name == "nt")
    except (OSError, subprocess.TimeoutExpired) as e:
        raise flowctl.FlowError(f"playwright-cli no responde: {e}") from e
    finally:
        os.remove(tmp)
    out = p.stdout.strip()
    if out.startswith("### Error") or p.returncode:
        raise flowctl.FlowError(" ".join((out + p.stderr).split())[:400])
    try:
        return json.loads(out)
    except ValueError:
        return out


def handle_id(flow: str, node: str, side: str, kind: str, which: int = 0) -> str:
    """Id de un puerto del nodo, leido por API (solo lectura): side incoming|outgoing, kind DEFAULT|REJECT|LOOKUP|OPTIONAL..."""
    g = flowctl.resolve(flow)["graph"]
    hs = [h["id"] for h in flowctl.find_node(g, node)["handles"].get(side, []) if h["type"] == kind]
    if len(hs) <= which:
        raise flowctl.FlowError(f"'{node}' no tiene puerto {side} {kind}")
    return hs[which]


def run(a) -> str:
    act = a.action
    if act == "connect":  # ids de puerto por API; el arrastre es en la interfaz
        return run_js("connect", src=handle_id(a.flow, a.src, "outgoing", a.out), dst=handle_id(a.flow, a.dst, "incoming", a.to, a.nth))
    if act in ("state", "panel"):
        return run_js(act)
    if act == "unlink":
        return run_js("unlink", src=a.src, dst=a.dst)
    if act in ("select", "rm"):
        return run_js(act, node=a.node)
    if act == "preview":
        return run_js("preview", node=a.node, n=a.rows)
    if act == "fill":
        return run_js("fill", label=a.label, value=a.value)
    if act in ("apply", "cancel"):
        return run_js("button", name="Aplicar" if act == "apply" else "Cancelar")
    if act == "rename":
        return run_js("rename", node=a.node, text=a.text)
    if act == "move":
        return run_js("move", node=a.node, dx=a.dx, dy=a.dy)
    if act == "add":
        return run_js("add", palette=a.palette, edge=a.on, x=a.x, y=a.y)
    if act in ("undo", "redo"):
        return run_js("tool", name="Deshacer" if act == "undo" else "Rehacer")  # botones de la barra; Ctrl+Y no rehace
    if act == "layout":
        return run_js("tool", name="Organizar el flujo")
    if act == "fit":
        return run_js("tool", name="Ajuste de zoom")
    if act == "script":
        return run_js("script", node=a.node)
    raise flowctl.FlowError(f"accion desconocida: {act}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="dfemu ui", description="Control del editor abierto en Chrome (no recarga la pagina)")
    sub = ap.add_subparsers(dest="action", required=True)
    sub.add_parser("state", help="estado, nodos con su posicion y aristas")
    sub.add_parser("panel", help="controles del panel de propiedades (rol | etiqueta | valor)")
    for n, h in (("select", "selecciona un nodo (abre su panel)"), ("rm", "elimina un nodo desde su menu"), ("preview", "vista previa de datos del nodo")):
        s = sub.add_parser(n, help=h)
        s.add_argument("node", help="prefijo del id o etiqueta")
        if n == "preview":
            s.add_argument("--rows", type=int, default=5)
    s = sub.add_parser("fill", help="rellena un control del panel por su etiqueta; en listas desplegables varios valores con |")
    s.add_argument("label"), s.add_argument("value")
    sub.add_parser("apply", help="pulsa Aplicar en el panel"), sub.add_parser("cancel", help="pulsa Cancelar")
    s = sub.add_parser("rename", help="cambia el titulo de un nodo")
    s.add_argument("node"), s.add_argument("text")
    s = sub.add_parser("move", help="arrastra un nodo dx,dy pixeles")
    s.add_argument("node"), s.add_argument("dx", type=int), s.add_argument("dy", type=int)
    s = sub.add_parser("connect", help="une dos nodos arrastrando entre sus puertos")
    s.add_argument("flow"), s.add_argument("src"), s.add_argument("dst")
    s.add_argument("--out", default="DEFAULT", help="puerto de salida (DEFAULT, REJECT, OPTIONAL_1...)"), s.add_argument("--to", default="DEFAULT", help="puerto de entrada (DEFAULT, LOOKUP, OPTIONAL)")
    s.add_argument("--nth", type=int, default=0, help="con varios puertos del mismo tipo, el n-esimo")
    s = sub.add_parser("unlink", help="borra la arista entre dos nodos (prefijos de id de 8 caracteres)")
    s.add_argument("src"), s.add_argument("dst")
    s = sub.add_parser("add", help="arrastra un procesador de la paleta a una arista (--on ORIGEN) o a un punto (--x --y)")
    s.add_argument("palette", help="nombre en la paleta, p. ej. Ordenar"), s.add_argument("--on", help="prefijo del id del nodo origen de la arista")
    s.add_argument("--x", type=int, default=700), s.add_argument("--y", type=int, default=420)
    for n, h in (("undo", "boton Deshacer"), ("redo", "boton Rehacer"), ("layout", "Organizar el flujo"), ("fit", "Ajuste de zoom")):
        sub.add_parser(n, help=h)
    s = sub.add_parser("script", help="script de Qlik que genera el flujo hasta un nodo (vista previa del script)")
    s.add_argument("node", nargs="?", help="nodo a seleccionar antes (por omision, el seleccionado)")
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        print(run(ap.parse_args(argv)))
    except flowctl.FlowError as e:
        sys.exit(f"error: {e}")
    return 0
