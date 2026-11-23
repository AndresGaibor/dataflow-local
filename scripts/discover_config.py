"""Descubre la configuracion JSON de un processor a partir de lo que dice el servidor.

Con la configuracion vacia el servidor responde `VALUE_MISSING_ON_REQUIRED_FIELD` y en `parameters.attributePath` dice que campo
falta; un valor invalido de un tipo enumerado lista los validos (`Enum class: [...]`). Se rellena el campo y se repite hasta que
el servidor deja de quejarse. Ignora las claves desconocidas. Usa una sola copia descartable `emu_v_*` por processor.

Uso: python scripts/discover_config.py strings:LOWERCASE math:ADD numbers:ROUND   (tipo:subtipo; sin subtipo, solo el tipo)
Escribe el resultado en out/discovered_configs.json. Requiere `dfemu setup` hecho y un flujo base cuya fuente sea `clientes.csv`.
"""
import copy
import json
import os
import re
import sys
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

MAX_ROUNDS = 12
_NUMERIC_HINTS = ("start", "end", "length", "width", "count", "position", "index", "precision", "decimals", "digits", "places",
                  "size", "times")


def set_path(cfg: dict, path: str, value) -> None:
    """Pone `value` en `cfg` siguiendo una ruta como /substringConfiguration/start, creando los diccionarios que falten."""
    keys = [k for k in path.split("/") if k]
    node = cfg
    for k in keys[:-1]:
        node = node.setdefault(k, {})
    node[keys[-1]] = value


def config_key(subtype: str) -> str:
    """Clave del objeto de configuracion de un subtipo: SUBSTRING -> substringConfiguration (algun nombre es irregular)."""
    head, *rest = subtype.lower().split("_")
    return head + "".join(w.capitalize() for w in rest) + "Configuration"


def guess_value(name: str):
    """Valor de partida para un campo segun su nombre; el servidor corrige lo que no encaje."""
    n = name.lower()
    if name.endswith("Configuration"):
        return {}
    if n.startswith(("should", "is", "keep", "case")):
        return False
    if n.endswith(("toprocess", "columns", "fields")):
        return ["ciudad"]
    if "newcolumn" in n:
        return ""
    if any(k in n for k in _NUMERIC_HINTS):
        return 1
    return "x"


def enum_field(message: str):
    """(objeto, campo, valores) del error de un enum invalido, o None. Lee la cadena de referencia de Jackson."""
    m = re.search(r"Enum class: \[([^\]]*)\]", message)
    if not m:
        return None
    chain = message[message.find("reference chain"):]
    names = re.findall(r'\[\\?"(\w+)\\?"\]', chain)
    if len(names) < 2:
        return None
    return names[-2], names[-1], [v.strip() for v in m.group(1).split(",")]


def _graph(ctype: str, cfg: dict, entity: str) -> dict:
    from emulator.builder import Flow
    import processor_battery as pb
    f = Flow("emu_p_discover")
    src = f.dataset("clientes", "clientes.csv", pb.CLIENTES)
    f.chain(src, f.proc(ctype, "p", cfg), f.target("Destino", "emu_p_discover"))
    g = copy.deepcopy(f.dump()["dataflow"]["graph"])
    for n in g["nodes"]:
        if n["component"]["type"] == "analyticsSource":
            n["component"]["properties"]["dataEntity"]["entityId"] = entity
    return g


def discover(remote, clone, entity: str, ctype: str, subtype: str | None):
    """(configuracion, resultado). El resultado es el estado final del servidor o por que se paro."""
    # con el tipo y sin su objeto de configuracion el servidor falla con un 500 sin detalle; algunos subtipos (ROUND, FLOOR,
    # SUBSTRING...) tambien lo dan si faltan los campos habituales o la columna no es del tipo adecuado: se parte de ellos
    column = {"numbers": "cedula", "math": "cedula", "date": "fecha_nacimiento"}.get(ctype, "ciudad")
    base = {"columnsToProcess": [column], "newColumnName": "", "shouldCreateNewColumn": False}
    cfg = {"type": subtype, config_key(subtype): base} if subtype else {}
    for _ in range(MAX_ROUNDS):
        try:
            res = remote.push_graph(clone, _graph(ctype, cfg, entity))
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            found = enum_field(msg)
            if not found:
                return cfg, "ERROR: " + msg.replace("\n", " ")[:240]
            parent, field, values = found
            (cfg.get(parent) if isinstance(cfg.get(parent), dict) else cfg)[field] = values[0]
            continue
        viol = res.validity.get("nodesConstraintViolations") or []
        missing = [v["parameters"]["attributePath"] for v in viol if v.get("code") == "VALUE_MISSING_ON_REQUIRED_FIELD"]
        if not missing:
            return cfg, f"{res.validity.get('status')} {[v.get('code') for v in viol]}"
        for path in missing:
            set_path(cfg, path, guess_value(path.rsplit("/", 1)[-1]))
    return cfg, "demasiadas rondas"


def main(args: list[str]) -> int:
    from emulator import bridge
    from emulator.remote import BASE_APP_ID, Remote
    import processor_battery as pb
    b = bridge.Bridge(apply=True)
    remote = Remote(b)
    entity = pb.base_entity(remote)
    out_path = os.path.join(ROOT, "out", "discovered_configs.json")
    found = json.load(open(out_path, encoding="utf-8")) if os.path.exists(out_path) else {}
    for arg in args:
        ctype, _, subtype = arg.partition(":")
        clone = remote.clone(BASE_APP_ID, "emu_v_" + uuid.uuid4().hex[:8])
        try:
            cfg, result = discover(remote, clone, entity, ctype, subtype or None)
        finally:
            remote.discard(clone.app_id)
        found[arg] = {"config": cfg, "resultado": result}
        print(f"{arg:34} {result[:70]}\n   {json.dumps(cfg, ensure_ascii=False)}", flush=True)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        json.dump(found, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
