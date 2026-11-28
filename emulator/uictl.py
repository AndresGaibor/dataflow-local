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
  // El nombre accesible sale de aria-label, aria-labelledby (es lo que usa Qlik: los comboboxes del panel
  // no traen aria-label, solo un <span id> que los etiqueta), <label> o placeholder. Sin esto, el panel del
  // Pivotar se veia como tres comboboxes vacios y no habia forma de rellenarlos por etiqueta.
  const lineas = await page.evaluate(() => {
    const nom = e => (e.getAttribute('aria-label') || (e.getAttribute('aria-labelledby') || '').split(/\s+/).map(i => (document.getElementById(i) || {}).textContent || '').join(' ') || (e.labels && e.labels[0] && e.labels[0].innerText) || e.placeholder || '').trim().replace(/\s+/g, ' ').slice(0, 50);
    const sel = 'input, button, textarea, select, [role=combobox], [role=switch], [role=checkbox], [role=radio], [role=option]';
    const todos = [...document.querySelectorAll(sel)].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    const caja = document.querySelector('[role=dialog], [aria-label="Propiedades"], aside');
    const dentro = caja ? todos.filter(e => caja.contains(e)) : [];
    const fuera = todos.filter(e => e.getBoundingClientRect().x > 1230);
    return (dentro.length ? dentro : fuera.length ? fuera : todos).map(e => (e.getAttribute('role') || e.tagName.toLowerCase()) + ' | ' + nom(e) + ' | ' + ((e.value || e.textContent || '').trim().slice(0, 44)));
  });
  return lineas.join('\n');""",
    "steps": r"""
  // Motor unico de la interfaz: ejecuta una lista de pasos en ESTA sesion de pagina. Hay que encadenarlos
  // porque el panel flotante de propiedades se cierra al soltar la pestana: dos procesos de `playwright-cli`
  // seguidos no ven el mismo panel (medido con el Pivotar).
  //   {"accion":"abrir","node":"Pivotar"}          abre el panel de un nodo (hover + clic)
  //   {"accion":"fill","label":"Campo","value":"x"} rellena por nombre accesible, o por --testid si lo hay
  //   {"accion":"click","text":"Ejecutar y aplicar"} pulsa boton, pestana o texto
  //   {"accion":"wait","ms":1500}
  const abrir = async ref => {
    const loc = await nodeLoc(ref), b = await loc.boundingBox();
    await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(800);
    await press(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(2200);
  };
  const halla = async p => {
    if (p.testid) {  // algunos testid salen con basura pegada ("pivot.valueFieldName}"), asi que se acepta el prefijo
      const l = page.locator('[data-testid="' + p.testid + '"]');
      if (await l.count()) return l.first();
      const marcado = await page.evaluate(t => {
        document.querySelectorAll('[data-ui]').forEach(e => e.removeAttribute('data-ui'));
        const e = [...document.querySelectorAll('[data-testid]')].find(x => x.dataset.testid.startsWith(t) && !x.dataset.testid.endsWith('.menuTrigger'));
        if (!e) return false; e.setAttribute('data-ui', '1'); return true;
      }, p.testid);
      if (marcado) return page.locator('[data-ui="1"]').first();
    }
    const nombre = p.label || p.text;
    if (!nombre) return null;  // un paso por testid no trae texto: sin el no se consulta por nombre (Playwright revienta)
    for (const l of [page.getByRole('combobox', {name: nombre}), page.getByLabel(nombre), page.getByRole('textbox', {name: nombre})]) if (await l.count()) return l.first();
    return null;
  };
  const lee = loc => loc.evaluate(e => (e.value || e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 60));
  const pulsa = async loc => { await loc.click({force: true, timeout: 8000}).catch(async () => { await loc.dispatchEvent('click'); }); };
  const opcion = async v => {  // 1) opcion con role=option; 2) fila del portal con el texto exacto
    const pulsada = await page.evaluate(v => {
      const vis = e => e.getBoundingClientRect().width > 0;
      const ops = [...document.querySelectorAll('[role=option]')].filter(vis).filter(o => (o.textContent || '').trim() === v);
      if (ops.length) { ops[0].click(); return true; }
      const hojas = [...document.querySelectorAll('*')].filter(e => !e.children.length && vis(e) && (e.textContent || '').trim() === v);
      if (!hojas.length) return false; hojas[hojas.length - 1].click(); return true;
    }, v);
    await page.waitForTimeout(900); return pulsada;
  };
  const informe = [];
  for (const p of A.steps) {
    if (p.accion === 'wait') { await page.waitForTimeout(p.ms || 1000); informe.push({accion: 'wait', ok: true}); continue; }
    if (p.accion === 'abrir') { await abrir(p.node); informe.push({accion: 'abrir', node: p.node, ok: true}); continue; }
    if (p.accion === 'click') {
      let ok = false;
      for (const l of [page.getByRole('button', {name: p.text}), page.getByRole('tab', {name: p.text}), page.getByLabel(p.text), page.getByText(p.text, {exact: true})]) {
        if (await l.count()) { await l.last().click({force: true, timeout: 15000}).catch(async () => l.last().dispatchEvent('click')); ok = true; break; }
      }
      await page.waitForTimeout(p.ms || 1500); informe.push({accion: 'click', text: p.text, ok}); continue;
    }
    const ctrl = await halla(p);
    if (!ctrl) { informe.push({accion: p.accion, label: p.label, testid: p.testid, ok: false, valor: null}); continue; }
    const rol = (await ctrl.getAttribute('role')) || 'textbox';
    if (rol !== 'combobox') {
      await pulsa(ctrl); await page.keyboard.press('Control+A'); await page.keyboard.type(p.value);
      await page.keyboard.press('Tab'); await page.waitForTimeout(400);
    } else {
      for (const v of String(p.value).split('|')) {  // varios valores: separados por |
        if ((await lee(ctrl)) === v) continue;  // ya estaba
        await pulsa(ctrl); await page.waitForTimeout(1200);
        if (!(await opcion(v))) { await page.keyboard.type(v); await page.waitForTimeout(400); await page.keyboard.press('Enter'); await page.waitForTimeout(600); }
      }
    }
    const ahora = await lee(ctrl);
    informe.push({accion: 'fill', label: p.label, testid: p.testid, pedido: p.value, valor: ahora, ok: ahora === String(p.value).split('|').pop()});
  }
  return JSON.stringify(informe);""",
    "options": r"""
  await page.evaluate(() => document.querySelectorAll('[data-ui]').forEach(e => e.removeAttribute('data-ui')));
  const ok = await page.evaluate(l => { const e = [...document.querySelectorAll('[role=combobox]')].find(x => x.getBoundingClientRect().x > 1230 && [x.getAttribute('aria-label'), x.labels && x.labels[0] && x.labels[0].innerText].some(t => (t || '').trim().startsWith(l))); if (e) e.setAttribute('data-ui', '1'); return !!e; }, A.label);
  if (!ok) throw new Error('no hay lista "' + A.label + '" en el panel (ver `dfemu ui panel`)');
  const b = await page.locator('[data-ui="1"]').boundingBox(); await press(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600);
  const o = await page.evaluate(() => [...document.querySelectorAll('[role=option]')].map(e => e.textContent.trim()));
  await page.keyboard.press('Escape'); return o.join(' | ');""",
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
  // La paleta escucha los DragEvent HTML5: con mouse.down/move/up no se mueve nada (medido). Se lanzan
  // dragstart/dragover/drop con un DataTransfer, que es lo que abre el catalogo o deja el procesador.
  await tab(A.tab || 'Procesadores');
  const t = A.edge ? await edgeMid(A.edge) : {x: A.x, y: A.y};
  const res = await page.evaluate(o => {
    const row = [...document.querySelectorAll('[role=tabpanel] *')].find(x => x.children.length === 0 && x.offsetParent !== null && (x.textContent || '').replace(/[​\s]/g, '') === o.name.replace(/\s/g, ''));
    if (!row) return 'no hay "' + o.name + '" en la paleta';
    let src = row; while (src && src.getAttribute('draggable') !== 'true') src = src.parentElement;
    const pane = document.querySelector('.react-flow__pane');
    if (!src || !pane) return 'sin origen o lienzo';
    const r = src.getBoundingClientRect(), p = pane.getBoundingClientRect(), dt = new DataTransfer();
    const fire = (el, type, x, y) => el.dispatchEvent(new DragEvent(type, {bubbles: true, cancelable: true, composed: true, dataTransfer: dt, clientX: x, clientY: y}));
    fire(src, 'dragstart', r.x + 10, r.y + 10); fire(pane, 'dragenter', o.x, o.y); fire(pane, 'dragover', o.x, o.y);
    fire(pane, 'drop', o.x, o.y); fire(src, 'dragend', o.x, o.y);
    return 'ok';
  }, {name: A.palette, x: t.x, y: t.y});
  if (res !== 'ok') throw new Error(res);
  await page.waitForTimeout(2500); return 'ok';""",
    "dataset": r"""
  // Carga un dataset del catalogo como fuente: el arrastre de la paleta es HTML5, asi que se lanzan los
  // DragEvent con un DataTransfer (los clics sinteticos no abren el catalogo). Medido: abre el dialogo
  // "Catalogo de datos" y deja el nodo.
  await tab(A.tab || 'Fuentes');
  const started = await page.evaluate(o => {
    const n = o.name;
    const row = [...document.querySelectorAll('[role=tabpanel] *')].find(x => x.children.length === 0 && x.offsetParent !== null && (x.textContent || '').replace(/[​\s]/g, '') === n.replace(/\s/g, ''));
    if (!row) return 'no hay "' + n + '" en la paleta';
    let src = row; while (src && src.getAttribute('draggable') !== 'true') src = src.parentElement;
    const pane = document.querySelector('.react-flow__pane');
    if (!src || !pane) return 'sin origen o lienzo';
    const r = src.getBoundingClientRect(), p = pane.getBoundingClientRect(), dt = new DataTransfer();
    const fire = (el, type, x, y) => el.dispatchEvent(new DragEvent(type, {bubbles: true, cancelable: true, composed: true, dataTransfer: dt, clientX: x, clientY: y}));
    const x = p.x + o.x, y = p.y + o.y;
    fire(src, 'dragstart', r.x + 10, r.y + 10); fire(pane, 'dragenter', x, y); fire(pane, 'dragover', x, y);
    fire(pane, 'drop', x, y); fire(src, 'dragend', x, y);
    return 'ok';
  }, {name: A.palette || 'Conjuntos de datos', x: A.x || 420, y: A.y || 260});
  if (started !== 'ok') throw new Error(started);
  await page.waitForSelector('[role=dialog]', {timeout: 20000});
  await page.waitForTimeout(800);
  const caja = page.locator('[role=dialog] input[aria-label="Buscar datos"], [role=dialog] input[placeholder*="uscar"]').first();
  await caja.fill(A.dataset);
  await page.waitForTimeout(2500);
  // la busqueda deja pocas filas: la ultima casilla es la del resultado (la primera es "seleccionar todo")
  const btn = page.getByRole('button', {name: /Cargar en el flujo|Añadir al flujo|Agregar al flujo|Cargar selecci|Seleccionar/i}).last();
  const cajas = page.locator('[role=dialog] input[type=checkbox]');
  const b = await cajas.last().boundingBox();
  if (!b) throw new Error('la tabla del catalogo no muestra casillas para ' + A.dataset);
  await press(b.x + b.width / 2, b.y + b.height / 2);
  await page.waitForTimeout(900);
  await btn.waitFor({state: 'visible', timeout: 10000});
  await btn.click({timeout: 20000});
  await page.waitForTimeout(4000);
  const fin = await page.evaluate(() => ({dialogos: document.querySelectorAll('[role=dialog]').length,
                                          nodos: document.querySelectorAll('.react-flow__node').length}));
  const marcada = 'casillas ' + await cajas.count();
  return 'ok [' + marcada + '] dialogos ' + fin.dialogos + ', nodos ' + fin.nodos;""",
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
    if act in ("fill", "click", "steps"):
        if act == "steps":
            if isinstance(a.steps, list):
                pasos = a.steps
            elif os.path.isfile(a.steps):
                with open(a.steps, encoding="utf-8") as f:
                    pasos = json.load(f)
            else:
                pasos = json.loads(a.steps)
        elif act == "fill":
            pasos = [{"accion": "fill", "label": a.label, "value": a.value}]
        else:
            pasos = [{"accion": "click", "text": a.text, "ms": a.wait}]
        if getattr(a, "node", None):  # el panel del nodo hay que abrirlo en la misma sesion de pagina
            pasos = [{"accion": "abrir", "node": a.node}] + pasos
        informe = run_js("steps", steps=pasos)
        if isinstance(informe, str):
            try:
                informe = json.loads(informe)
            except ValueError:
                return informe
        lineas = [f"{x.get('accion')} {x.get('label') or x.get('testid') or x.get('text') or x.get('node') or ''}"
                  f" = {x.get('valor') if x.get('valor') is not None else ''}".rstrip() + ("" if x.get("ok") else "   <- sin efecto")
                  for x in informe]
        if any(not x.get("ok") for x in informe):
            raise flowctl.FlowError("pasos sin efecto:\n" + "\n".join(lineas))
        return "\n".join(lineas)
    if act == "options":
        return run_js("options", label=a.label)
    if act in ("apply", "cancel"):
        if act == "cancel":
            return run_js("button", name="Cancelar")
        # el boton se llama de una forma u otra segun el nodo: "Aplicar" o "Ejecutar y aplicar"
        for nombre in ("Aplicar", "Ejecutar y aplicar"):
            try:
                return run_js("button", name=nombre)
            except flowctl.FlowError as e:
                ultimo = e
        raise ultimo
    if act == "rename":
        return run_js("rename", node=a.node, text=a.text)
    if act == "move":
        return run_js("move", node=a.node, dx=a.dx, dy=a.dy)
    if act == "add":
        return run_js("add", palette=a.palette, edge=a.on, x=a.x, y=a.y, tab=a.tab)
    if act == "dataset":
        return run_js("dataset", dataset=a.dataset, palette=a.palette, x=a.x, y=a.y, tab=a.tab)
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
    for n, h in (("fill", "rellena un control del panel por su etiqueta; en listas desplegables varios valores con |"),
                 ("click", "pulsa un boton, pestana o texto visible por su nombre (sin coordenadas)")):
        s = sub.add_parser(n, help=h)
        s.add_argument("label" if n == "fill" else "text")
        if n == "fill":
            s.add_argument("value")
        else:
            s.add_argument("--wait", type=int, default=1500, help="milisegundos a esperar tras pulsar")
        s.add_argument("--node", help="abre antes el panel de este nodo (la misma sesion de pagina)")
    s = sub.add_parser("steps", help="ejecuta una receta JSON de pasos en una sola sesion: abrir/fill/click/wait")
    s.add_argument("steps", help="ruta del JSON o la lista en linea")
    s = sub.add_parser("options", help="opciones de una lista desplegable del panel")
    s.add_argument("label")
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
    s = sub.add_parser("dataset", help="carga un dataset del catalogo como fuente (abre el catalogo y confirma)")
    s.add_argument("dataset", help="nombre del dataset, p. ej. cuentas.csv")
    s.add_argument("--palette", default="Conjuntos de datos", help="fila de la paleta (por omision, Conjuntos de datos)")
    s.add_argument("--tab", default="Fuentes"), s.add_argument("--x", type=int, default=420), s.add_argument("--y", type=int, default=260)
    s = sub.add_parser("add", help="arrastra un procesador de la paleta a una arista (--on ORIGEN) o a un punto (--x --y)")
    s.add_argument("palette", help="nombre en la paleta, p. ej. Ordenar"), s.add_argument("--on", help="prefijo del id del nodo origen de la arista")
    s.add_argument("--x", type=int, default=700), s.add_argument("--y", type=int, default=420)
    s.add_argument("--tab", default="Procesadores", help="pestana de la paleta: Fuentes, Procesadores o Destinos")
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
