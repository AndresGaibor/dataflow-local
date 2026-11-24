"""Sondea el editor SIN recargarlo: arrastra cada procesador de la paleta sobre una arista, lee por API (solo
lectura) el nodo que crea la interfaz (tipo, puertos, configuracion inicial, validez) y lo borra desde la interfaz.

    python scripts/ui_probe.py FLUJO ORIGEN "Ordenar" "Unir" ...    # ORIGEN: prefijo del id del nodo cuya salida se corta
Resultado compacto en stdout y detalle en out/ui_probe.json (ignorado por git). Requiere la sesion `chrome` y la
pestana del editor de FLUJO abierta y activa. Con esto se genero emulator/processors.json.
Aviso: "Receta de tabla" crea un subflow en el tenant que no se borra al eliminar el nodo.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from emulator import flowctl, uictl  # noqa: E402


def main(flow: str, src: str, names: list[str]) -> None:
    base = flowctl.resolve(flow)
    flowctl.check_writable(base)
    ids = {n["id"] for n in base["graph"]["nodes"]}
    out = {}
    for name in names:
        res = uictl.run_js("add", palette=name, edge=src, x=0, y=0)
        df = flowctl.resolve(base["id"])
        new = [n for n in df["graph"]["nodes"] if n["id"] not in ids]
        info = {"drop": res, "validity": df["validity"]["status"], "nodes": [
            {"type": n["component"]["type"], "label": n["label"],
             "in": [h["type"] for h in n["handles"].get("incoming", [])], "out": [h["type"] for h in n["handles"].get("outgoing", [])],
             "cfg": (n["component"].get("properties") or {}).get("configuration")} for n in new]}
        out[name] = info
        print(f"{name:20} {info['validity']:8} " + ("; ".join(f"{n['type']} in={n['in']} out={n['out']}" for n in info["nodes"]) or "sin nodo"), flush=True)
        for n in new:
            uictl.run_js("rm", node=n["id"])
        left = len(flowctl.resolve(base["id"])["graph"]["nodes"])
        if left != len(ids):
            print(f"aviso: quedan {left} nodos (base {len(ids)}); paro", flush=True)
            break
    os.makedirs(os.path.join(flowctl.ROOT, "out"), exist_ok=True)
    with open(os.path.join(flowctl.ROOT, "out", "ui_probe.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
