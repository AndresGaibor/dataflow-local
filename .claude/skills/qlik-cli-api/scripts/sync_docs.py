#!/usr/bin/env python3
"""Descarga qlik.dev (sitemap) como Markdown a docs/ y genera docs/_manifest.jsonl.

Uso:  python -I sync_docs.py            # todo el sitio
      python -I sync_docs.py --only toolkits/qlik-cli   # solo un prefijo
Solo usa la biblioteca estándar. Pide cada página a la URL oficial con sufijo .md
(qlik.dev publica esa variante), con pocas conexiones en paralelo para no cargar el sitio.
"""
import argparse, json, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = "https://qlik.dev"
UA = "qlik-cli-api-skill-sync/1.0"
WORKERS = 4  # cortesía con el sitio; ~2000 páginas tardan pocos minutos
ROOT = Path(__file__).resolve().parent.parent / "docs"


def get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
    return None


def page_urls(prefix):
    xml = get(f"{BASE}/sitemap-0.xml")
    if not xml:
        sys.exit("No se pudo leer el sitemap de qlik.dev")
    urls = re.findall(r"<loc>([^<]+)</loc>", xml)
    return [u for u in urls if u.removeprefix(BASE + "/").startswith(prefix)]


def rel_path(url):
    p = url.removeprefix(BASE).strip("/")
    return (p or "index") + ".md"


def fetch(url):
    body = get(url.rstrip("/") + ".md")
    if not body:
        return url, None
    out = ROOT / rel_path(url)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")  # qlik.dev ya incluye front matter (source, last_updated)
    m = re.search(r"^#\s+(.+)$", body, re.M)
    lu = re.search(r"^last_updated:\s*(\S+)", body, re.M)
    return url, {"path": rel_path(url).replace("\\", "/"), "url": url,
                 "title": m.group(1).strip() if m else rel_path(url),
                 "last_updated": lu.group(1) if lu else "", "bytes": len(body)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="prefijo de ruta, p. ej. toolkits/qlik-cli")
    a = ap.parse_args()
    urls = page_urls(a.only)
    print(f"{len(urls)} páginas a descargar")
    ok, fail = [], []
    with ThreadPoolExecutor(WORKERS) as ex:
        for i, (u, rec) in enumerate(ex.map(fetch, urls), 1):
            (ok if rec else fail).append(rec or u)
            if i % 200 == 0:
                print(f"  {i}/{len(urls)}")
    ROOT.mkdir(parents=True, exist_ok=True)
    manifest = ROOT / "_manifest.jsonl"
    old = {}
    if a.only and manifest.exists():  # sincronización parcial: conserva el resto
        for line in manifest.read_text(encoding="utf-8").splitlines():
            r = json.loads(line); old[r["url"]] = r
    for r in ok:
        old[r["url"]] = r
    manifest.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in sorted(old.values(), key=lambda r: r["path"])) + "\n", encoding="utf-8")
    (ROOT / "_synced.txt").write_text(time.strftime("%Y-%m-%d"), encoding="utf-8")
    print(f"OK {len(ok)}  fallidas {len(fail)}")
    for u in fail:
        print("  sin .md:", u)


if __name__ == "__main__":
    main()
