"""Cobertura de processors: cuantos del catalogo tienen caso medido en la bateria.

Lee `emulator/processors.json` (la paleta descubierta) y
`scripts/processor_battery_cases.json` (los casos) y publica el resumen en el
README entre marcadores, para que la cifra no se escriba a mano.

    python scripts/processor_coverage.py            # imprime la tabla
    python scripts/processor_coverage.py --readme   # regenera el bloque del README
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "emulator", "processors.json")
CASES = os.path.join(ROOT, "scripts", "processor_battery_cases.json")
README_BEGIN = "<!-- processors:inicio -->"
README_END = "<!-- processors:fin -->"

# tipos de caso que arman un grafo con varios processors dentro (ver build() de la bateria)
IMPLIED = {
    "forkunion": {"fork", "union", "filter", "sort"},
    "join": {"fork", "join", "filter", "field-selector"},
    "joinchain": {"fork", "join", "filter", "field-selector", "sort"},
}

# processors que no se pueden medir con la credencial actual y por que (ver apartado 12)
BLOCKED = {
    "pivot": "sin donante de schemaEntityId (ningun flujo accesible tiene pivot)",
    "script": "el nodo hay que crearlo desde la interfaz",
    "subflow": "ningun flujo accesible trae subflows",
    "map-fields": "configuracion sin semantica documentada",
}


def used_processors(cases: dict, allowed=None) -> set[str]:
    """Processors que aparecen en algun caso (los casos `chain` traen listas de pasos).

    `allowed` filtra por el catalogo: el JSON de un caso tambien trae valores
    como `UPPERCASE` o `TRIM`, que son variantes y no processors.
    """
    used = set()
    for case in cases.values():
        if isinstance(case, list) and case and case[0] in IMPLIED:
            used |= IMPLIED[case[0]]
        stack = [case]
        while stack:
            item = stack.pop()
            if isinstance(item, str):
                if allowed is None or item in allowed:
                    used.add(item)
            elif isinstance(item, list):
                stack.extend(item)
            elif isinstance(item, dict):
                stack.extend(item.values())
    return used


def coverage() -> dict:
    catalog = json.load(open(CATALOG, encoding="utf-8"))
    cases = json.load(open(CASES, encoding="utf-8"))
    used = used_processors(cases, set(catalog))
    measured = sorted(p for p in catalog if p in used)
    pending = sorted(p for p in catalog if p not in used)
    return {
        "catalog": len(catalog),
        "cases": len(cases),
        "measured": measured,
        "pending": pending,
        "blocked": {p: BLOCKED[p] for p in pending if p in BLOCKED},
        "other": [p for p in pending if p not in BLOCKED],
    }


def readme_block(cov: dict) -> str:
    rows = [
        README_BEGIN,
        "| cobertura de processors | valor |",
        "| --- | --- |",
        f"| processors en el catalogo | {cov['catalog']} |",
        f"| casos de bateria | {cov['cases']} |",
        f"| con al menos un caso medido | {len(cov['measured'])} |",
        f"| sin caso | {len(cov['pending'])} |",
        README_END,
    ]
    return "\n".join(rows)


def report(cov: dict) -> str:
    lines = [
        f"processors en el catalogo: {cov['catalog']}",
        f"casos de bateria: {cov['cases']}",
        f"con al menos un caso: {len(cov['measured'])}",
        f"sin caso: {len(cov['pending'])}",
    ]
    for p in cov["pending"]:
        why = cov["blocked"].get(p, "pendiente de caso")
        lines.append(f"  - {p}: {why}")
    return "\n".join(lines)


def write_readme(cov: dict, path: str) -> None:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    block = readme_block(cov)
    if README_BEGIN in text and README_END in text:
        head, _, rest = text.partition(README_BEGIN)
        _, _, tail = rest.partition(README_END)
        text = head + block + tail
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Cobertura de processors medida por la bateria")
    p.add_argument("--readme", action="store_true", help="regenera el bloque del README")
    p.add_argument("--out", default=ROOT, help="raiz del repositorio")
    a = p.parse_args(argv)
    cov = coverage()
    print(report(cov))
    if a.readme:
        write_readme(cov, os.path.join(a.out, "README.md"))
        print("README actualizado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
