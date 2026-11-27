"""scripts/processor_coverage.py: cuantos processors del catalogo tienen caso medido."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)
import processor_coverage as pc  # noqa: E402


def test_used_processors_sees_plain_and_chained_cases():
    cases = {
        "uno": ["strings", {"type": "UPPERCASE"}],
        "cadena": ["chain", [["strings", {"type": "TRIM"}], ["math", {"type": "ABSOLUTE"}]]],
    }
    assert pc.used_processors(cases) == {"strings", "math", "chain", "UPPERCASE", "TRIM", "ABSOLUTE"}
    # con el catalogo como filtro se queda solo lo que es un processor
    assert pc.used_processors(cases, {"strings", "math", "fork"}) == {"strings", "math"}


def test_implied_processors_of_a_multi_node_case_are_counted():
    """Un caso `forkunion` usa fork, union, filter y sort aunque el JSON solo diga el tipo."""
    assert pc.used_processors({"x": ["forkunion", {}]}, set(pc.IMPLIED["forkunion"])) == {"fork", "union", "filter", "sort"}


def test_coverage_counts_the_real_catalog():
    cov = pc.coverage()
    assert cov["catalog"] == 24
    assert len(cov["measured"]) + len(cov["pending"]) == cov["catalog"]
    assert "strings" in cov["measured"]      # tiene decenas de casos
    assert "pivot" in cov["pending"]


def test_the_pending_ones_that_cannot_be_measured_are_explained():
    cov = pc.coverage()
    for name in cov["pending"]:
        assert name in pc.BLOCKED, f"{name} sin caso y sin motivo documentado"


def test_readme_block_has_numbers_between_markers(tmp_path):
    cov = pc.coverage()
    block = pc.readme_block(cov)
    assert block.startswith(pc.README_BEGIN) and block.rstrip().endswith(pc.README_END)
    assert f"| processors en el catalogo | {cov['catalog']} |" in block


def test_write_readme_replaces_the_block(tmp_path):
    cov = pc.coverage()
    readme = tmp_path / "README.md"
    readme.write_text("# t\n\n" + pc.README_BEGIN + "\nviejo\n" + pc.README_END + "\n\ncola\n", encoding="utf-8")
    pc.write_readme(cov, str(readme))
    text = readme.read_text(encoding="utf-8")
    assert "viejo" not in text and "# t" in text and "cola" in text
    assert "| casos de bateria |" in text
