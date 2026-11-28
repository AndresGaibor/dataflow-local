"""La skill del proyecto no se puede quedar desfasada respecto al CLI ni a los documentos.

El frontmatter se lee sin PyYAML: `clave: valor` de primer nivel, que es todo lo que usa la skill.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".agents" / "skills" / "dfemu" / "SKILL.md"


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path.name} sin frontmatter"
    head = text.split("---", 2)[1]
    meta = {}
    for line in head.splitlines():
        if not line.strip() or line[:1].isspace() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta


def test_la_skill_tiene_frontmatter_valido():
    meta = frontmatter(SKILL)
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", meta["name"]) and meta["name"] == SKILL.parent.name
    assert 1 <= len(meta["description"]) <= 1024
    assert "dfemu" in meta["description"].lower()


def test_la_skill_cubre_los_comandos_que_documenta():
    text = SKILL.read_text(encoding="utf-8")
    for cmd in ("dfemu flow capture start", "dfemu flow capture dump", "dfemu mcp --list", "dfemu reload",
                "python -m emulator.cli coverage", "scripts/test_coverage.py", "scripts/docsync.py --check"):
        assert cmd in text, f"la skill no menciona `{cmd}`"


def test_los_documentos_que_enlaza_la_skill_existen():
    text = SKILL.read_text(encoding="utf-8")
    for rel in ("docs/MCP.md", "docs/banco-de-pruebas/01-hallazgos-api-qlik.md"):
        assert rel in text and (ROOT / rel).exists(), rel


def test_el_comando_de_captura_que_documenta_la_skill_existe():
    p = subprocess.run([sys.executable, "-m", "emulator.cli", "flow", "capture", "--help"], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0 and "start" in p.stdout and "dump" in p.stdout


def test_la_skill_no_promete_nada_que_la_api_no_deje():
    # lo medido: estos nodos necesitan la interfaz, y la skill tiene que decirlo
    text = SKILL.read_text(encoding="utf-8").lower()
    for nodo in ("pivot", "map-fields", "subflow", "datasources"):
        assert nodo in text
    assert "adf-500" in text or "500" in text
