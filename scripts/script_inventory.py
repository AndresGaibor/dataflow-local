"""Inventario de constructs de Qlik script sobre el corpus.

Dice que sentencias y funciones aparecen en los scripts reales y si el traductor
las cubre. La cobertura no se escribe a mano: se contrasta con lo que
`emulator/script.py` sabe ejecutar.

El resultado de traducir cada script se informa aparte, porque los nodos de
script de un flujo son fragmentos que hacen RESIDENT de tablas que crea otro
nodo: traducirlos sueltos casi nunca puede funcionar y eso no mide cobertura.

    python scripts/script_inventory.py                 # corpus de out/ y samples/
    python scripts/script_inventory.py --write         # escribe el informe en docs/
    python scripts/script_inventory.py --json          # inventario en JSON
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from emulator import script as qvs  # noqa: E402

STATEMENT = re.compile(r"[A-Za-z_][A-Za-z_ ]*")
FUNC = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
# palabras que abren sentencia en Qlik script; no son funciones aunque lleven parentesis
KEYWORDS = {
    "LOAD", "SELECT", "RESIDENT", "FROM", "WHERE", "GROUP", "ORDER", "JOIN", "KEEP", "CONCATENATE",
    "NOCONCATENATE", "LEFT", "RIGHT", "INNER", "OUTER", "FULL", "SET", "LET", "TRACE", "DROP",
    "STORE", "THROW", "IF", "THEN", "ELSE", "END", "FOR", "NEXT", "DO", "LOOP", "SUB", "CALL",
    "SQL", "EXIT", "SWITCH", "CASE", "DEFAULT", "UNLESS", "AND", "OR", "NOT", "AS", "INLINE",
    "TXT", "QVD", "DELIMITER", "LABELS", "IS", "BY", "ON", "REPLACE",
}

# lo que emulator/script.py:translate sabe ejecutar; se contrasta con _HEAD y su lista de saltos
KNOWN_STATEMENTS = {
    "LOAD", "SELECT", "SET", "TRACE", "DROP", "STORE", "THROW", "NOCONCATENATE",
    "LEFT JOIN", "INNER JOIN", "RIGHT JOIN", "OUTER JOIN", "FULL JOIN",
}


def _clean(text: str) -> str:
    text = re.sub(r"(?m)^\s*//.*$", "", text)
    return re.sub(r"(?s)/\*.*?\*/", "", text)


def statements(text: str) -> list[str]:
    """Primera palabra (o par `LEFT JOIN`) de cada sentencia."""
    out = []
    for st in qvs.split_statements(_clean(text)):
        st = st.strip()
        if not st:
            continue
        m = STATEMENT.match(st)
        if not m:
            continue
        words = m.group(0).upper().split()
        head = words[0]
        if head in ("LEFT", "RIGHT", "INNER", "OUTER", "FULL") and len(words) > 1:
            head = f"{head} {words[1]}"
        out.append(head)
    return out


def functions(text: str) -> list[str]:
    """Funciones llamadas (en mayusculas), sin palabras clave de sentencia."""
    return [n.upper() for n in FUNC.findall(_clean(text)) if n.upper() not in KEYWORDS]


def _walk(node, label=None):
    """(etiqueta, script) de cada nodo con `configuration.script`, sin repetir."""
    if isinstance(node, dict):
        label = node.get("label", label)
        comp = node.get("component")
        owner = comp if isinstance(comp, dict) else None
        props = (owner or node).get("properties")
        if owner is not None:
            label = node.get("label") or owner.get("label") or label
        cfg = props.get("configuration") if isinstance(props, dict) else None
        if isinstance(cfg, dict) and isinstance(cfg.get("script"), str) and cfg["script"].strip():
            yield label or "script", cfg["script"]
            return  # ya salio el script: no se baja al component para no repetirlo
        for value in (node if owner is not None else node).values():
            if owner is not None and value is comp:
                continue
            yield from _walk(value, label)
        if owner is None:
            return
        yield from _walk(owner, label)
    elif isinstance(node, list):
        for value in node:
            yield from _walk(value, label)


def scripts_from_json(obj) -> dict:
    """{etiqueta: script} de un grafo `.dfw` o `.pull.json`."""
    out = {}
    for label, script in _walk(obj):
        key, n = label, 2
        while key in out:  # dos nodos con la misma etiqueta
            key, n = f"{label}#{n}", n + 1
        out[key] = script
    return out


def scripts_from_paths(paths) -> dict:
    """Scripts de los `.qvs`, `.dfw` y `.pull.json` indicados."""
    out = {}
    for path in paths:
        stem = os.path.splitext(os.path.basename(path))[0]
        try:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
        except OSError:
            continue
        if path.endswith(".qvs"):
            if raw.strip():
                out[stem] = raw
            continue
        try:
            data = json.loads(raw)
        except ValueError:
            continue
        for label, script in scripts_from_json(data).items():
            out[f"{stem}:{label}"] = script
    return out


def default_paths(root: str = ROOT) -> list[str]:
    paths = sorted(glob.glob(os.path.join(root, "out", "**", "*.pull.json"), recursive=True))
    paths += sorted(glob.glob(os.path.join(root, "samples", "**", "*.dfw"), recursive=True))
    paths += sorted(glob.glob(os.path.join(root, "samples", "**", "*.qvs"), recursive=True))
    return paths


def _known_functions() -> set[str]:
    return {name.upper() for name in qvs._FUNCS}


def inventory(scripts: dict, translate=None, data_dir: str | None = None) -> dict:
    """Cobertura por construct y resultado de traducir cada script por separado."""
    translate = translate or qvs.translate
    data_dir = data_dir if data_dir is not None else os.path.join(ROOT, "data")

    per_script = {}
    for name, text in scripts.items():
        try:
            sql, reasons = translate(text, data_dir)
        except Exception as e:  # noqa: BLE001 - el traductor puede reventar con entradas raras
            sql, reasons = None, [f"excepcion: {e}"]
        per_script[name] = {"ok": bool(sql), "reasons": reasons}

    constructs: dict[str, dict] = {}
    for text in scripts.values():
        items = [("sentencia", s) for s in statements(text)] + [("funcion", f) for f in functions(text)]
        for kind, item in items:
            slot = constructs.setdefault(item, {"kind": kind, "scripts": 0})
            slot["scripts"] += 1

    known_funcs = _known_functions()
    for item, slot in constructs.items():
        known = item in KNOWN_STATEMENTS if slot["kind"] == "sentencia" else item in known_funcs
        slot["status"] = "cubierto" if known else "no cubierto"

    return {
        "scripts": len(scripts),
        "translated": sum(1 for v in per_script.values() if v["ok"]),
        "sin_contexto": {k: v["reasons"] for k, v in per_script.items() if not v["ok"]},
        "constructs": constructs,
    }


def report_md(inv: dict) -> str:
    uncovered = [c for c, v in inv["constructs"].items() if v["status"] != "cubierto"]
    head = [
        "# Cobertura de Qlik script",
        "",
        "Generado por `python scripts/script_inventory.py --write`; no se edita a mano.",
        "",
        f"- Scripts del corpus: {inv['scripts']}",
        f"- Constructs distintos: {len(inv['constructs'])}",
        f"- Sin cubrir por el traductor: {len(uncovered)}",
        f"- Scripts que traducen sueltos: {inv['translated']} de {inv['scripts']} "
        "(un nodo de script es un fragmento con RESIDENT del resto del flujo; no mide cobertura)",
        "",
    ]
    if uncovered:
        head += ["## Constructs sin cubrir", ""]
        head += [f"- `{c}` ({inv['constructs'][c]['kind']}, {inv['constructs'][c]['scripts']} scripts)"
                 for c in sorted(uncovered)]
        head.append("")
    rows = ["| construct | tipo | scripts | estado |", "| --- | --- | --- | --- |"]
    for item in sorted(inv["constructs"], key=lambda k: (-inv["constructs"][k]["scripts"], k)):
        c = inv["constructs"][item]
        rows.append(f"| `{item}` | {c['kind']} | {c['scripts']} | {c['status']} |")
    return "\n".join(head + rows) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Inventario de constructs de Qlik script sobre el corpus")
    p.add_argument("paths", nargs="*", help="archivos .qvs/.dfw/.pull.json (por omision, corpus y samples)")
    p.add_argument("--write", action="store_true", help="escribe docs/banco-de-pruebas/05-cobertura-script.md")
    p.add_argument("--json", action="store_true", help="imprime el inventario en JSON")
    p.add_argument("--out", default=".", help="raiz del repositorio")
    a = p.parse_args(argv)

    scripts = scripts_from_paths(a.paths or default_paths(os.path.abspath(a.out)))
    if not scripts:
        print("no hay scripts en el corpus (¿falta out/corpus? usa dfemu pull)", file=sys.stderr)
        return 2
    inv = inventory(scripts)
    if a.json:
        print(json.dumps(inv, ensure_ascii=False, indent=1))
    else:
        md = report_md(inv)
        if a.write:
            target = os.path.join(a.out, "docs", "banco-de-pruebas", "05-cobertura-script.md")
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="\n") as f:
                f.write(md)
            print(f"escrito {target}")
        else:
            print(md)
    return 0 if not [c for c, v in inv["constructs"].items() if v["status"] != "cubierto"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
