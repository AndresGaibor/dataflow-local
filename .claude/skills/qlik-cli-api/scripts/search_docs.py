#!/usr/bin/env python3
"""Busca y lee la copia local de qlik.dev (qlik-cli, REST API, QIX, autenticación...).

  python -I search_docs.py "app import" -n 8            # buscar
  python -I search_docs.py "reload" --area toolkits/qlik-cli/reload
  python -I search_docs.py --show toolkits/qlik-cli/app/app-ls.md --max 6000
Solo biblioteca estándar. Las rutas son relativas a docs/.
"""
import argparse, json, re, sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"


def load():
    mf = DOCS / "_manifest.jsonl"
    if not mf.exists():
        sys.exit("Falta docs/_manifest.jsonl: ejecuta  python -I scripts/sync_docs.py")
    return [json.loads(l) for l in mf.read_text(encoding="utf-8").splitlines() if l]


def score(rec, terms, text):
    low, title = text.lower(), rec["title"].lower()
    path = rec["path"].lower()
    s = 0
    for t in terms:
        c = low.count(t)
        if c == 0:
            return 0  # todos los términos deben aparecer (AND)
        s += min(c, 10) + (15 if t in title else 0) + (10 if t in path else 0)
    return s


def snippet(text, term, width=110):
    i = text.lower().find(term)
    if i < 0:
        return ""
    a = max(0, i - width // 2)
    return re.sub(r"\s+", " ", text[a:a + width * 2]).strip()


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # consola de Windows (cp1252) rompe los acentos
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--area", default="", help="prefijo de ruta, p. ej. apis/rest/apps")
    ap.add_argument("--show", help="ruta de una página (relativa a docs/)")
    ap.add_argument("--max", type=int, default=8000, help="caracteres a mostrar con --show")
    a = ap.parse_args()

    if a.show:
        f = (DOCS / a.show).resolve()
        if DOCS.resolve() not in f.parents or not f.is_file():
            sys.exit(f"No existe: {a.show}")
        t = f.read_text(encoding="utf-8")
        print(t[:a.max] + ("\n[... recortado, sube --max ...]" if len(t) > a.max else ""))
        return
    if not a.query:
        ap.error("indica una consulta o --show")

    terms = a.query.lower().split()
    hits = []
    for rec in load():
        if not rec["path"].startswith(a.area):
            continue
        text = (DOCS / rec["path"]).read_text(encoding="utf-8")
        s = score(rec, terms, text)
        if s:
            hits.append((s, rec, text))
    hits.sort(key=lambda h: -h[0])
    if not hits:
        print("Sin resultados. Prueba menos términos o sin --area.")
    for s, rec, text in hits[:a.n]:
        print(f"[{s}] {rec['title']}\n  {rec['path']}\n  {rec['url']}\n  ...{snippet(text, terms[0])}...\n")


if __name__ == "__main__":
    main()
