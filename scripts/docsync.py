"""Espejo reproducible de la documentacion de Qlik Cloud (help.qlik.com).

Descarga las paginas que lista el sitemap, las convierte a Markdown con
frontmatter, baja las imagenes referenciadas y deja un manifiesto con el
sha256 de cada pagina para detectar cambios sin volver a bajarlo todo.

    python scripts/docsync.py --list                     # familias y versiones del sitemap
    python scripts/docsync.py                            # espeja la familia por omision
    python scripts/docsync.py --check                    # 0 faltantes: falla si falta algo
    python scripts/docsync.py --limit 5 --out /tmp/x     # piloto

Escribe en `docs/<seccion>/...` y `docs/_images/...`; el manifiesto va en
`docs/manifest.json`. Es idempotente: si el sha256 no cambia, no reescribe.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

INDEX = "https://help.qlik.com/sitemap.xml"
UA = "dfemu-docsync/0.1 (+https://github.com/AndresGaibor/dataflow-local)"
DEFAULT_FAMILY = "cloud-services_en-US"
# carpetas de docs/ escritas a mano: --prune no las toca nunca
PROTECTED = {"banco-de-pruebas", "superpowers"}


def _get(url: str, timeout: int = 60, retries: int = 3, backoff: float = 2.0) -> bytes:
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:  # reintenta
            last = e
            if isinstance(e, urllib.error.HTTPError) and e.code in (404, 403):
                break
            time.sleep(backoff * (attempt + 1))
    raise RuntimeError(f"{url}: {last}")


def _locs(xml: bytes | str) -> list[str]:
    text = xml.decode("utf-8", "replace") if isinstance(xml, bytes) else xml
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)


def sitemaps(xml) -> list[str]:
    """URLs de los sitemaps hijos del indice."""
    return _locs(xml)


def page_urls(xml) -> list[str]:
    """URLs de las paginas de un sitemap, sin repetir y en orden."""
    seen, out = set(), []
    for u in _locs(xml):
        if u.endswith(".htm") and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def families(xml) -> list[str]:
    """Nombres de sitemap del indice (sin la ruta), para elegir familia y version."""
    return [urllib.parse.urlsplit(u).path.lstrip("/") for u in sitemaps(xml)]


ROOTS = {  # prefijo del sitio -> carpeta en docs/ ("" = la seccion de siempre)
    "Sense_Hub": "",
    "Sense_QlikAutomation": "Automate",
    "Sense_GeoOperations": "GeoOperations",
    "Sense_Helpsites": "Helpsites",
}


def target_path(url: str) -> str:
    """`.../Content/Sense_Hub/Scripting/load-data.htm` -> `Scripting/load-data.md`."""
    path = urllib.parse.urlsplit(url).path
    rel = None
    for root, prefix in ROOTS.items():
        if f"/{root}/" in path:
            rel = path.split(f"/{root}/", 1)[1]
            if prefix:
                rel = f"{prefix}/{rel}"
            break
    if rel is None:
        if "/Content/" in path:
            rel = path.split("/Content/", 1)[1]
            parts = rel.split("/")
            rel = "/".join(parts[1:]) if len(parts) > 1 else rel
        else:
            rel = path.lstrip("/")
    stem, _ = os.path.splitext(rel)
    return stem + ".md"


IMG_EXT = re.compile(r"\.(png|jpe?g|gif|svg|webp|bmp)$", re.I)


def image_target(url: str, src: str) -> tuple[str | None, str | None]:
    """(enlace relativo desde el .md, ruta dentro de docs/) de una imagen de Qlik.

    Las paginas usan rutas relativas (`../../Resources/Images/...`) y tambien
    `_images/...`; en los dos casos la imagen se guarda espejando su ruta en
    help.qlik.com, que es lo que evita colisiones entre secciones.
    """
    absolute = urllib.parse.urljoin(url, src)
    parts = urllib.parse.urlsplit(absolute)
    if parts.netloc != "help.qlik.com" or not IMG_EXT.search(parts.path):
        return None, None
    inside = [p for p in parts.path.split("/") if p]
    if inside and inside[0] == "_images":
        inside = inside[1:]
    target = os.path.join("_images", *inside)
    rel = os.path.relpath(target, os.path.dirname(target_path(url)) or ".")
    return rel.replace(os.sep, "/"), target


def image_url(target: str) -> str:
    """Ruta en docs/ -> URL absoluta en help.qlik.com (para descargarla)."""
    inside = os.path.normpath(target).replace(os.sep, "/")
    if inside.startswith("_images/"):
        inside = inside[len("_images/"):]
    return "https://help.qlik.com/" + inside


def _q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def front_matter(meta: dict) -> str:
    lines = ["---"]
    for key in ("title", "source_url", "guide", "product", "version", "last_updated"):
        if meta.get(key) is not None:
            # source_url va sin comillas, como en los documentos ya versionados
            lines.append(f"{key}: {meta[key] if key == 'source_url' else _q(meta[key])}")
    if meta.get("breadcrumbs"):
        lines.append("breadcrumbs: " + json.dumps(meta["breadcrumbs"], ensure_ascii=False))
    lines.append("---")
    return "\n".join(lines) + "\n"


def _content(soup):
    for sel in ("#mc-main-content", ".topicContent", "main"):
        el = soup.select_one(sel)
        if el is not None and len(el.get_text(strip=True)) > 20:
            return el
    return soup.body or soup


def convert(html: str, url: str) -> str:
    """HTML de una pagina de help.qlik.com -> Markdown con frontmatter."""
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(html, "html.parser")
    # la fecha se lee antes de limpiar: su span se elimina del cuerpo
    updated = soup.find("span", class_="last-updated")
    last_updated = re.sub(r"^Last updated:\s*", "", updated.get_text(" ", strip=True)) if updated else ""

    for junk in soup.select("script, style, nav, .search-extras, .next-nav, .last-updated"):
        junk.decompose()

    body_el = _content(soup)
    h1 = body_el.find("h1") or soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else (soup.title.get_text(strip=True) if soup.title else url)

    def meta(name: str) -> str:
        tag = soup.find("meta", attrs={"name": name})
        return (tag.get("content") or "").strip() if tag else ""

    bc = soup.select_one(".breadcrumb")
    breadcrumbs = [a.get_text(" ", strip=True) for a in bc.select("a") if a.get_text(strip=True)] if bc else []

    for img in body_el.find_all("img"):
        rel, _ = image_target(url, img.get("src", ""))
        if rel:
            img["src"] = rel
        else:
            img.decompose()

    md_body = markdownify(str(body_el), heading_style="ATX", bullets="-").strip()
    md_body = re.sub(r"[ \t]+\n", "\n", md_body)
    md_body = re.sub(r"\n{3,}", "\n\n", md_body)
    if h1 and not md_body.lstrip().startswith("# "):
        md_body = f"# {title}\n\n{md_body}"

    meta_dict = {
        "title": title,
        "source_url": url,
        "guide": meta("guide-name"),
        "product": meta("product"),
        "version": meta("version"),
        "last_updated": last_updated,
        "breadcrumbs": breadcrumbs,
    }
    return front_matter(meta_dict) + "\n" + md_body + "\n"


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _read_manifest(root: str) -> dict:
    path = os.path.join(root, "docs", "manifest.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"pages": {}, "images": {}}


def _write_manifest(root: str, state: dict) -> None:
    path = os.path.join(root, "docs", "manifest.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    state["generated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def images_of(md: str) -> list[str]:
    return [m for m in re.findall(r"\]\(([^)\s]+)\)", md) if "_images/" in m]


def sync(urls: list[str], root: str, fetch=_get, workers: int = 4, progress=None, skip_known: bool = False) -> dict:
    """Descarga `urls` a `root/docs` y devuelve el informe de lo hecho.

    Con `skip_known` no se vuelve a bajar lo que ya esta en el manifiesto y en disco;
    sirve para completar imagenes o anadir paginas nuevas sin repetir el corpus.
    """
    state = _read_manifest(root)
    report = {"written": 0, "unchanged": 0, "images": 0, "failed": {}}
    pending_images: dict[str, str] = {}

    def one(url: str):
        known = state["pages"].get(url)
        if skip_known and known and os.path.exists(os.path.join(root, "docs", known["path"])):
            with open(os.path.join(root, "docs", known["path"]), encoding="utf-8") as f:
                return url, f.read(), "skip"  # ya esta: solo se miran sus imagenes
        try:
            return url, convert(fetch(url).decode("utf-8", "replace"), url), None
        except Exception as e:  # red o HTML raro: se informa y se sigue
            return url, None, str(e)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        for n, (url, md, err) in enumerate(pool.map(one, urls), 1):
            if err and err != "skip":
                report["failed"][url] = err
                continue
            skipped = err == "skip"
            rel = target_path(url)
            path = os.path.join(root, "docs", rel)
            sha = _sha(md)
            previous = state["pages"].get(url)
            if skipped:
                report["unchanged"] += 1
            if previous and previous.get("sha256") == sha and os.path.exists(path):
                report["unchanged"] += 1
            else:
                os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(md)
                report["written"] += 1
            state["pages"][url] = {"path": rel.replace(os.sep, "/"), "sha256": sha, "bytes": len(md.encode("utf-8"))}
            for link in images_of(md):
                target = os.path.normpath(os.path.join(os.path.dirname(rel), link))
                pending_images[target] = target
            if progress:
                progress(n, len(urls), url)

    pending = [t for t in sorted(pending_images) if not (state["images"].get(image_url(t)) and os.path.exists(os.path.join(root, "docs", t)))]

    def one_image(target: str):
        try:
            return target, fetch(image_url(target)), None
        except Exception as e:  # una imagen que falla no tumba el espejo
            return target, None, str(e)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        for target, data, err in pool.map(one_image, pending):
            url = image_url(target)
            if err:
                report["failed"][url] = err
                continue
            path = os.path.join(root, "docs", target)
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "wb") as f:
                f.write(data)
            state["images"][url] = {"path": target.replace(os.sep, "/"), "sha256": hashlib.sha256(data).hexdigest()}
            report["images"] += 1

    _write_manifest(root, state)
    return report


def check(urls: list[str], root: str) -> dict:
    """Paginas del sitemap que faltan en disco y enlaces a imagenes rotos."""
    state = _read_manifest(root)
    missing = [u for u in urls if u not in state["pages"] or not os.path.exists(os.path.join(root, "docs", state["pages"][u]["path"]))]
    return {"missing": missing, "broken_images": broken_images(os.path.join(root, "docs"))}


def broken_images(docs_root: str) -> list[str]:
    """Enlaces a `_images/...` que no existen, como `archivo.md -> ruta`."""
    broken = []
    for dirpath, _, names in os.walk(docs_root):
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except UnicodeDecodeError:
                continue
            for link in images_of(text):
                if link.startswith(("http://", "https://")):
                    continue
                absolute = os.path.normpath(os.path.join(dirpath, link))
                if not os.path.exists(absolute):
                    broken.append(f"{os.path.relpath(path, docs_root)} -> {link}")
    return broken


def prune(urls: list[str], root: str) -> list[str]:
    """Borra los `.md` de docs/ que ya no corresponden a ninguna pagina del sitemap."""
    state = _read_manifest(root)
    keep = {os.path.normpath(p["path"]) for p in state["pages"].values() if p.get("path")}
    docs = os.path.join(root, "docs")
    removed = []
    for dirpath, _, names in os.walk(docs):
        if os.path.normpath(dirpath).startswith(os.path.normpath(os.path.join(docs, "_images"))):
            continue
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.normpath(os.path.relpath(full, docs))
            if rel.split(os.sep, 1)[0] in PROTECTED:
                continue
            if rel not in keep:
                os.remove(full)
                removed.append(rel.replace(os.sep, "/"))
    # deja limpio: el manifiesto solo lista lo que sigue en el sitemap
    if removed:
        wanted = set(urls)
        state["pages"] = {u: v for u, v in state["pages"].items() if u in wanted}
        _write_manifest(root, state)
    return removed


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Espeja la documentacion de help.qlik.com en docs/")
    p.add_argument("--list", action="store_true", help="lista familias del sitemap y sale")
    p.add_argument("--family", default=DEFAULT_FAMILY, help=f"sitemap a espejar (por omision {DEFAULT_FAMILY})")
    p.add_argument("--url", help="URL del sitemap (ignora --family)")
    p.add_argument("--out", default=".", help="raiz del repositorio (por omision el directorio actual)")
    p.add_argument("--limit", type=int, help="procesa solo las primeras N paginas (piloto)")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--check", action="store_true", help="no descarga: falla si falta una pagina o una imagen")
    p.add_argument("--no-images", action="store_true", help="no descarga imagenes")
    p.add_argument("--prune", action="store_true", help="borra los .md que ya no estan en el sitemap")
    p.add_argument("--skip-known", action="store_true", help="no vuelve a bajar las paginas ya espejadas")
    a = p.parse_args(argv)

    index = _get(INDEX)
    if a.list:
        for name in families(index):
            print(name)
        return 0

    url = a.url or next((s for s in sitemaps(index) if a.family in urllib.parse.urlsplit(s).path), None)
    if url is None:
        print(f"no hay sitemap '{a.family}' en {INDEX}; usa --list", file=sys.stderr)
        return 2
    urls = page_urls(_get(url))
    if a.limit:
        urls = urls[: a.limit]

    if a.check:
        result = check(urls, a.out)
        for u in result["missing"]:
            print(f"falta: {u}")
        for b in result["broken_images"]:
            print(f"imagen rota: {b}")
        print(f"{len(urls) - len(result['missing'])}/{len(urls)} paginas; {len(result['broken_images'])} imagenes rotas")
        return 1 if (result["missing"] or result["broken_images"]) else 0

    fetch = _get
    if a.no_images:
        fetch = lambda u: b"" if "/_images/" in u else _get(u)
    report = sync(urls, a.out, fetch=fetch, workers=a.workers, skip_known=a.skip_known,
                  progress=lambda n, total, u: print(f"[{n}/{total}] {u}", flush=True))
    if a.prune:
        for gone in prune(urls, a.out):
            print(f"huérfano borrado: {gone}")
    print(json.dumps({"escritas": report["written"], "sin_cambios": report["unchanged"],
                      "imagenes": report["images"], "fallos": len(report["failed"])}, ensure_ascii=False))
    for k, v in list(report["failed"].items())[:10]:
        print(f"  fallo: {k}: {v}", file=sys.stderr)
    return 0 if not report["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
