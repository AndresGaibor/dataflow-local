"""Desidentifica los .dfw de `samples/` para poder publicarlos.

Reemplaza de forma determinista (misma entrada -> misma salida) los
identificadores del tenant: UUID, ids de 24 hex, hashes de 40/64 hex, QRI,
tokens de carpeta de Google Drive y los catalogos de conectores que exponen
nombres de datasets del cliente.

Uso:
    python scripts/deidentify.py samples          # reescribe en sitio
    python scripts/deidentify.py samples --check  # solo informa
"""
import argparse
import hashlib
import json
import os
import re
import sys

# sin \b a la izquierda/derecha: los ids de arista concatenan UUID con otros textos
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
HEX24 = re.compile(r"\b[0-9a-f]{24}\b")
HEX40_64 = re.compile(r"\b[0-9a-f]{40,64}\b")
QRI = re.compile(r"qri:qdf:space://([^#\s\"]+)#([^\s\"]+)")
DRIVE = re.compile(r"\b16j1s-[A-Za-z0-9_-]{10,}\b")
NOMBRES = [
    (re.compile(r"Google_BigQuery_lafavorita-\d+"), "Google_BigQuery_demo"),
    (re.compile(r"lafavorita-\d+"), "proyecto-demo"),
]
SUSPECT = [UUID, HEX24, HEX40_64, QRI, DRIVE, re.compile(r"lafavorita"),
           re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")]


MARCA_HEX = "dec0de"  # los ids desidentificados se reconocen a simple vista


def _hex(value: str, n: int) -> str:
    if value.startswith(MARCA_HEX):
        return value
    return MARCA_HEX + hashlib.sha256(("dfemu:" + value).encode()).hexdigest()[:n - len(MARCA_HEX)]


MARCA_UUID = "dec0de00-0000-4000-8000-"  # prefijo fijo: los uuid desidentificados se reconocen a simple vista


def _uuid(value: str) -> str:
    if value.startswith(MARCA_UUID):
        return value
    return MARCA_UUID + hashlib.sha256(("dfemu:" + value).encode()).hexdigest()[:12]


def _qri(m: re.Match) -> str:
    # el token del espacio y el del dataset no son hexadecimales: se sustituyen por hashes del mismo largo
    space = _hex(m.group(1), len(m.group(1)))
    item = _hex(m.group(2), len(m.group(2)))
    return f"qri:qdf:space://{space}#{item}"


def scrub_text(s: str) -> str:
    for pat, repl in NOMBRES:
        s = pat.sub(repl, s)
    s = QRI.sub(_qri, s)
    s = DRIVE.sub("carpeta-demo", s)
    s = UUID.sub(lambda m: _uuid(m.group(0)), s)
    s = HEX40_64.sub(lambda m: _hex(m.group(0), len(m.group(0))), s)
    s = HEX24.sub(lambda m: _hex(m.group(0), 24), s)
    return s


def scrub(obj):
    """Recorre el .dfw; en los conectores descarta el catalogo de datasets del cliente."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "inputOptions":  # listado cacheado de bases/tablas del tenant
                continue
            out[scrub_text(k) if isinstance(k, str) else k] = scrub(v)
        return out
    if isinstance(obj, list):
        return [scrub(v) for v in obj]
    if isinstance(obj, str):
        return scrub_text(obj)
    return obj


def scrub_select_properties(d: dict) -> None:
    """Las selecciones no aportan al emulador y nombran bases del cliente."""
    for src in d.get("sources", []):
        for table in src.get("tables", []):
            for prop in (table.get("connectorProperties") or {}).get("selectProperties", []):
                if isinstance(prop, dict) and prop.get("value"):
                    prop["value"] = "demo"


def identifiers(text: str) -> set[str]:
    found = set()
    for pat in SUSPECT:
        found |= {m.group(0) for m in pat.finditer(text) if MARCA_HEX not in m.group(0)}
    return found


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="samples")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    paths = []
    for base, _, files in os.walk(args.root):
        paths += [os.path.join(base, f) for f in files if f.endswith(".dfw")]
    bad = 0
    for path in sorted(paths):
        with open(path, encoding="utf-8-sig") as f:
            original = f.read()
        data = scrub(json.loads(original))
        scrub_select_properties(data)
        text = json.dumps(data, ensure_ascii=False)
        left = [i for i in identifiers(original) if i in text]
        if left:
            bad += 1
            print(f"{path}: {len(left)} identificadores sin sustituir: {left[:5]}")
        if not args.check:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
    print(f"{len(paths)} archivos revisados, {bad} con restos")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
