// Grabador de red a nivel de CDP: lo que `dfemu flow capture` no ve (service worker, peticiones de otra
// pestana, recargas que borran el gancho de fetch). Escribe JSONL con method, ruta sin host y cuerpo.
//
//   node scripts/cdp_capture.mjs --port 9222 --match dataflow --out out/captures/cdp.jsonl
//
// Se apoya en la instancia de Chrome con --remote-debugging-port; no abre navegador ni toca la sesion.
import { appendFileSync, mkdirSync } from 'node:fs';
import { dirname } from 'node:path';

const args = Object.fromEntries(process.argv.slice(2).reduce((acc, v, i, all) => {
  if (v.startsWith('--')) acc.push([v.slice(2), all[i + 1] && !all[i + 1].startsWith('--') ? all[i + 1] : true]);
  return acc;
}, []));
const port = args.port || '9222';
const barrido = String(args.match || 'dataflow');
const out = args.out || 'out/captures/cdp.jsonl';
const segundos = Number(args.seconds || 900);

const host = `http://[::1]:${port}`;
const lista = await (await fetch(`${host}/json/list`)).json();
const paginas = lista.filter(p => p.type === 'page');
const page = paginas.find(p => String(p.url).includes(barrido)) || paginas.find(p => /qlikcloud/.test(p.url)) || paginas[0];
if (!page) {
  console.error('no hay ninguna pestana abierta en ese Chrome');
  process.exit(2);
}
const ruta = String(page.url).replace(/^https?:\/\/[^/]+/, '');
console.log(`grabando en ${ruta} (filtro: ${barrido}) -> ${out}`);
mkdirSync(dirname(out), { recursive: true });

const ws = new WebSocket(page.webSocketDebuggerUrl);
let id = 0;
const pendientes = new Map();
const visto = new Map();
const enviar = (method, params = {}) => ws.send(JSON.stringify({ id: ++id, method, params }));
const limpiar = u => String(u || '').replace(/^https?:\/\/[^/]+/, '');

ws.addEventListener('open', () => {
  enviar('Network.enable', { maxPostDataSize: 5_000_000 });
  enviar('Page.enable');
  enviar('Runtime.enable');
});
ws.addEventListener('message', ev => {
  let msg;
  try { msg = JSON.parse(ev.data); } catch { return; }
  const { method, params } = msg;
  if (method === 'Network.requestWillBeSent') {
    const r = params.request || {};
    const u = limpiar(r.url);
    if (!u.includes(barrido)) return;
    visto.set(params.requestId, u);
    const cuerpo = r.postData ?? null;
    const linea = { ts: new Date().toISOString(), method: r.method, url: u, reqBytes: cuerpo ? cuerpo.length : 0 };
    appendFileSync(out, JSON.stringify({ ...linea, req: cuerpo }) + '\n');
    console.log(`> ${r.method} ${u}  ${cuerpo ? cuerpo.length + 'b' : ''}`);
  } else if (method === 'Network.responseReceived' && visto.has(params.requestId)) {
    appendFileSync(out, JSON.stringify({ ts: new Date().toISOString(), status: params.response.status,
      url: visto.get(params.requestId) }) + '\n');
    console.log(`< ${params.response.status} ${visto.get(params.requestId)}`);
  } else if (method === 'Runtime.consoleAPICalled') {
    const texto = (params.args || []).map(a => a.value ?? a.description ?? '').join(' ');
    if (/error|fail/i.test(texto)) console.log(`! ${texto.slice(0, 160)}`);
  }
});
ws.addEventListener('error', e => { console.error('ws error', e.message || e); process.exit(3); });
ws.addEventListener('close', () => process.exit(0));
setTimeout(() => { console.log('fin del tiempo de grabacion'); ws.close(); }, segundos * 1000);
