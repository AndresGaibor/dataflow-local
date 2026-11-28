"""scripts/docsync.py: espejo reproducible de la documentacion de help.qlik.com."""
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)
import docsync as ds  # noqa: E402

URL = "https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data.htm"

PAGE = """<!DOCTYPE html>
<html lang="en"><head>
<meta name="product" content="Qlik Cloud" />
<meta name="version" content="November 2026" />
<meta name="guide-name" content="Qlik Cloud" />
</head><body>
<div class="wrap"><div class="main"><div class="container content"><main class="col-7 qcs">
<div class="article">
  <div class="breadcrumb"><a href="/x">Qlik Cloud</a> / <a href="/y">Scripting</a></div>
  <div class="topicContent"><div id="mc-main-content">
    <h1>Loading data</h1>
    <span class="last-updated">Last updated: 2026-11-27</span>
    <p>Text with <code>inline()</code> code.</p>
    <img src="../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex.png" alt="Example" />
    <table><thead><tr><th>Name</th><th>Means</th></tr></thead>
      <tbody><tr><td>a</td><td>first</td></tr></tbody></table>
    <pre><code>LOAD * INLINE [x];</code></pre>
    <script>var tracker = 1;</script>
  </div></div>
</div>
<div class="search-extras">Leave your feedback here</div>
<nav class="next-nav"><a href="/next">Next</a></nav>
</main></div></div></div>
</body></html>"""


@pytest.fixture
def page_urls():
    return [URL, URL.replace("load-data", "other-page")]


def test_page_urls_from_sitemap_reads_every_loc():
    xml = (
        '<?xml version="1.0"?><urlset>'
        "<url><loc>https://help.qlik.com/a.htm</loc></url>"
        "<url><loc>https://help.qlik.com/b.htm</loc></url>"
        "</urlset>"
    )
    assert ds.page_urls(xml) == ["https://help.qlik.com/a.htm", "https://help.qlik.com/b.htm"]


def test_sitemaps_from_index_lists_children():
    xml = (
        '<?xml version="1.0"?><sitemapindex>'
        "<sitemap><loc>https://help.qlik.com/sitemap_sense_November2026_en-US.xml</loc></sitemap>"
        "<sitemap><loc>https://help.qlik.com/sitemap_replicate_May2026_en-US.xml</loc></sitemap>"
        "</sitemapindex>"
    )
    assert ds.sitemaps(xml) == [
        "https://help.qlik.com/sitemap_sense_November2026_en-US.xml",
        "https://help.qlik.com/sitemap_replicate_May2026_en-US.xml",
    ]


def test_target_path_keeps_the_section_and_the_rest_of_the_tree():
    assert ds.target_path(URL) == "Scripting/load-data.md"


def test_image_target_is_shared_and_deduped_by_url():
    rel, target = ds.image_target(URL, "https://help.qlik.com/_images/en-US/x/y.png")
    assert target == os.path.join("_images", "en-US", "x", "y.png")
    # el enlace se escribe relativo al .md que lo referencia
    assert rel == "../_images/en-US/x/y.png"


def test_convert_has_frontmatter_and_drops_chrome():
    md = ds.convert(PAGE, URL)
    head = md.split("---")[1]
    assert 'title: "Loading data"' in head
    assert f"source_url: {URL}" in head
    assert 'product: "Qlik Cloud"' in head
    assert 'version: "November 2026"' in head
    assert 'last_updated: "2026-11-27"' in head
    assert "breadcrumbs:" in head
    body = md.split("---", 2)[2]
    assert "# Loading data" in body
    assert "Leave your feedback here" not in body
    assert "tracker" not in body  # <script> fuera
    assert "var tracker" not in body


def test_convert_keeps_tables_code_and_rewrites_images():
    md = ds.convert(PAGE, URL)
    assert "| Name | Means |" in md
    assert "LOAD * INLINE" in md
    assert "../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex.png" in md


def test_sync_writes_page_manifest_and_images(tmp_path, page_urls):
    fetch = lambda url: b"PNG" if url.endswith(".png") else PAGE.encode("utf-8")
    report = ds.sync(page_urls, tmp_path, fetch=fetch)
    assert report["written"] == 2
    assert report["unchanged"] == 0
    state = json.loads((tmp_path / "docs" / "manifest.json").read_text(encoding="utf-8"))
    assert set(state["pages"]) == set(page_urls)
    assert all(len(v["sha256"]) == 64 for v in state["pages"].values())
    assert (tmp_path / "docs" / "Scripting" / "load-data.md").exists()
    assert (tmp_path / "docs" / "_images" / "en-US" / "cloud-services" / "Subsystems" / "Hub" / "Content" / "Resources" / "Images" / "ex.png").exists()


def test_sync_is_idempotent_and_does_not_rewrite(tmp_path, page_urls):
    fetch = lambda url: b"PNG" if url.endswith(".png") else PAGE.encode("utf-8")
    ds.sync(page_urls, tmp_path, fetch=fetch)
    target = tmp_path / "docs" / "Scripting" / "load-data.md"
    before = target.stat().st_mtime_ns
    report = ds.sync(page_urls, tmp_path, fetch=fetch)
    assert report["written"] == 0
    assert report["unchanged"] == 2
    assert target.stat().st_mtime_ns == before


def test_check_reports_missing_and_returns_zero_when_complete(tmp_path, page_urls):
    fetch = lambda url: b"PNG" if url.endswith(".png") else PAGE.encode("utf-8")
    assert ds.check(page_urls, tmp_path)["missing"] == page_urls
    ds.sync(page_urls, tmp_path, fetch=fetch)
    assert ds.check(page_urls, tmp_path)["missing"] == []
    assert ds.check(page_urls + [URL + "?x=1"], tmp_path)["missing"] == [URL + "?x=1"]


def test_offline_corpus_has_no_broken_image_links():
    """Los .md del repo no pueden referenciar imagenes que no existen en docs/_images.

    `docs/_images/` esta ignorado por git (son ~5.000 binarios): en un clon sin sincronizar no hay
    imagenes que comprobar, asi que se omite en vez de fallar.
    """
    if not os.path.isdir(os.path.join(ROOT, "docs", "_images")):
        pytest.skip("sin docs/_images: corre `python scripts/docsync.py` para comprobarlas")
    broken = ds.broken_images(os.path.join(ROOT, "docs"))
    assert broken == []

AUTOMATE = "https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm"


def test_target_path_maps_qlik_automation_under_docs_automate():
    assert ds.target_path(AUTOMATE) == "Automate/introduction/home-automation.md"


def test_prune_removes_pages_that_are_not_in_the_manifest(tmp_path, page_urls):
    fetch = lambda url: b"PNG" if url.endswith(".png") else PAGE.encode("utf-8")
    ds.sync(page_urls[:1], tmp_path, fetch=fetch)
    orphan = tmp_path / "docs" / "Scripting" / "viejo.md"
    orphan.write_text("contenido", encoding="utf-8")
    removed = ds.prune(page_urls[:1], tmp_path)
    assert removed == ["Scripting/viejo.md"]
    assert not orphan.exists()
    assert (tmp_path / "docs" / "Scripting" / "load-data.md").exists()

def test_image_target_handles_the_relative_resources_path():
    rel, target = ds.image_target(URL, '../../Resources/Images/Dataflow/x.png')
    assert target == os.path.join('_images', 'en-US', 'cloud-services', 'Subsystems', 'Hub', 'Content', 'Resources', 'Images', 'Dataflow', 'x.png')
    assert rel == '../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/x.png'


def test_image_url_is_the_inverse_of_image_target():
    rel, target = ds.image_target(URL, '../../Resources/Images/Dataflow/x.png')
    assert ds.image_url(target) == 'https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/x.png'


def test_prune_never_touches_the_curated_docs(tmp_path, page_urls):
    fetch = lambda url: b"PNG" if url.endswith(".png") else PAGE.encode("utf-8")
    ds.sync(page_urls[:1], tmp_path, fetch=fetch)
    curated = tmp_path / "docs" / "banco-de-pruebas" / "01-hallazgos-api-qlik.md"
    curated.parent.mkdir(parents=True, exist_ok=True)
    curated.write_text("hallazgos", encoding="utf-8")
    plan = tmp_path / "docs" / "superpowers" / "plans" / "p.md"
    plan.parent.mkdir(parents=True, exist_ok=True)
    plan.write_text("plan", encoding="utf-8")
    assert ds.prune(page_urls[:1], tmp_path) == []
    assert curated.exists() and plan.exists()
