"""Bateria de processors: cada caso es `clientes` -> un processor -> destino, ejecutado en el emulador y en el tenant.

Para cada caso: arma el grafo con `emulator.builder`, lo sube a un clon descartable `emu_v_*` del flujo base
(reutilizando su fuente `clientes`), toma el script que genera Qlik, lo ejecuta en una app `emu_oracle_*` y
compara las huellas con las del emulador. Todo lo que crea lo borra al terminar.

Requisitos: `dfemu setup` hecho; `DFEMU_BASE_APP` debe ser un flujo cuya fuente sea `clientes.csv` (de `data/practica`).
Uso: python scripts/processor_battery.py [caso ...]      (sin argumentos, todos; escribe en el tenant)
Los casos estan en processor_battery_cases.json. `calculate-fields` no se prueba: un PUT no puede provocar la
evaluacion de la expresion y el servidor responde POTENTIAL_STALE_EXPRESSION.
"""
import copy
import json
import os
import sys
import traceback
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import bridge, compare, oracle, runner  # noqa: E402
from emulator.builder import Flow  # noqa: E402
from emulator.remote import BASE_APP_ID, Remote  # noqa: E402

CLIENTES = ["cliente_id", "cedula", "nombre", "apellido", "fecha_nacimiento", "ciudad", "provincia", "region",
            "email", "telefono", "segmento", "fecha_registro"]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "processor_battery_cases.json"), encoding="utf-8") as fh:
    CASES = json.load(fh)


def base_entity(remote: Remote) -> str:
    """id de la fuente del flujo base (el `entityId` es propio de cada flujo, ver 9 ter)."""
    df = remote._get(f"v1/dataflows/{remote.dataflow_id(BASE_APP_ID)}")
    for n in df["graph"]["nodes"]:
        if n["component"]["type"] == "analyticsSource":
            return n["component"]["properties"]["dataEntity"]["entityId"]
    raise SystemExit("el flujo base no tiene una fuente")


def build(name: str, entity: str):
    ctype, cfg = CASES[name]
    f = Flow(f"emu_p_{name}")
    src = f.dataset("clientes", "clientes.csv", CLIENTES)
    f.chain(src, f.proc(ctype, name, cfg, x=380), f.target("Destino", f"emu_p_{name}", x=700))
    dump = f.dump()
    graph = copy.deepcopy(dump["dataflow"]["graph"])
    for n in graph["nodes"]:
        if n["component"]["type"] == "analyticsSource":
            n["component"]["properties"]["dataEntity"]["entityId"] = entity
    return dump, graph


def run_case(name: str, b: bridge.Bridge, r: Remote, entity: str, data: str, out: str) -> tuple[str, str]:
    dump, graph = build(name, entity)
    try:
        local = compare.target_fingerprints(runner.run(dump, data, os.path.join(out, name)))
    except Exception as e:  # noqa: BLE001
        return "EMULADOR", f"{type(e).__name__}: {str(e)[:150]}"
    clone = r.clone(BASE_APP_ID, "emu_v_" + uuid.uuid4().hex[:8])
    try:
        res = r.push_graph(clone, graph)
    finally:
        r.discard(clone.app_id)
    if res.validity.get("status") != "VALID" or not res.script:
        codes = [v.get("code") for v in res.validity.get("nodesConstraintViolations") or []]
        return "SERVIDOR " + str(res.validity.get("status")), str(codes)
    try:
        remote = oracle.run_script(b, res.script, uuid.uuid4().hex[:8])
    except Exception as e:  # noqa: BLE001
        return "TENANT", f"{type(e).__name__}: {str(e)[:200]}"
    diffs = compare.compare(local, remote)
    return ("OK" if not diffs else "DIFERENCIAS"), "; ".join(diffs)[:400]


def main(names: list[str]) -> int:
    for n in names:
        if n not in CASES:
            raise SystemExit(f"caso desconocido: {n}. Casos: {', '.join(CASES)}")
    b = bridge.Bridge(apply=True)
    r = Remote(b)
    entity = base_entity(r)
    bad = 0
    for name in names or list(CASES):
        try:
            status, detail = run_case(name, b, r, entity, os.path.join(ROOT, "data", "practica"), os.path.join(ROOT, "out", "battery"))
        except Exception:  # noqa: BLE001
            status, detail = "ERROR", traceback.format_exc().splitlines()[-1][:200]
        bad += status != "OK"
        print(f"{name:14} {status:18} {detail}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
