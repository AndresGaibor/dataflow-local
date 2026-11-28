"""CI y cobertura publicada: el workflow y el bloque del README no se desincronizan.

Se comprueba con regex sobre el texto del workflow para no añadir PyYAML como dependencia.
"""
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github" / "workflows" / "tests.yml"


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_matrix_runs_ubuntu_and_windows_with_both_pythons(workflow):
    assert re.search(r"os:\s*\[\s*ubuntu-latest,\s*windows-latest\s*\]", workflow)
    assert re.search(r'python-version:\s*\[\s*"3\.11",\s*"3\.12"\s*\]', workflow)
    assert "fail-fast: false" in workflow


def test_steps_cover_tests_coverage_mcp_and_samples(workflow):
    assert "pytest" in workflow and "--cov=emulator" in workflow
    assert "scripts/test_coverage.py --check" in workflow
    assert "emulator.cli mcp --list" in workflow
    assert "emulator.cli coverage" in workflow


def test_workflow_uses_existing_actions(workflow):
    assert re.search(r"uses: actions/checkout@v\d+", workflow)
    assert re.search(r"uses: actions/setup-python@v\d+", workflow)


def test_requirements_pin_everything_the_ci_installs():
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "duckdb==" in text and "pytest==" in text and "pytest-cov==" in text
    # los tests no pueden depender de paquetes que el CI no instala
    for name in ("yaml", "requests", "httpx"):
        for test in (ROOT / "tests").glob("*.py"):
            assert f"import {name}" not in test.read_text(encoding="utf-8"), f"{test.name} importa {name}"


def test_readme_block_matches_the_last_coverage_report():
    report = ROOT / "out" / "coverage.json"
    if not report.exists():
        pytest.skip("sin out/coverage.json: corre python scripts/test_coverage.py")
    cov = load_script("test_coverage")
    data = json.loads(report.read_text(encoding="utf-8"))
    assert cov.table(data) in (ROOT / "README.md").read_text(encoding="utf-8")


def test_table_reports_totals_and_the_lowest_modules():
    cov = load_script("test_coverage")
    data = {"totals": {"percent_covered": 81.25, "covered_lines": 130, "num_statements": 160},
            "files": {"emulator/a.py": {"summary": {"percent_covered": 50.0, "num_statements": 10}},
                      "emulator/b.py": {"summary": {"percent_covered": 95.0, "num_statements": 10}},
                      "emulator/c.py": {"summary": {"percent_covered": 10.0, "num_statements": 10}},
                      "emulator/d.py": {"summary": {"percent_covered": 70.0, "num_statements": 10}}}}
    block = cov.table(data)
    assert "81.2 %" in block and "130 de 160" in block
    assert block.index("`c.py` (10.0 %)") < block.index("`a.py` (50.0 %)")
    assert "`b.py`" not in block  # solo los tres mas bajos


def test_check_fails_when_the_readme_is_stale(tmp_path, monkeypatch):
    cov = load_script("test_coverage")
    monkeypatch.setattr(cov, "ROOT", tmp_path)
    monkeypatch.setattr(cov, "REPORT", tmp_path / "out" / "coverage.json")
    (tmp_path / "out").mkdir()
    cov.REPORT.write_text(json.dumps({"totals": {"percent_covered": 90.0, "covered_lines": 9,
                                                 "num_statements": 10}, "files": {}}), encoding="utf-8")
    (tmp_path / "README.md").write_text("sin bloque\n", encoding="utf-8")

    class Out(io.StringIO):
        def reconfigure(self, **kw):
            pass

    monkeypatch.setattr(sys, "stdout", Out())
    assert cov.main(["--check"]) == 1
    assert cov.main(["--readme"]) == 0
    assert cov.main(["--check"]) == 0
    assert "<!-- tests:inicio -->" in (tmp_path / "README.md").read_text(encoding="utf-8")


def test_check_tolera_decimas_entre_plataformas(tmp_path, monkeypatch):
    cov = load_script("test_coverage")
    monkeypatch.setattr(cov, "ROOT", tmp_path)
    monkeypatch.setattr(cov, "REPORT", tmp_path / "out" / "coverage.json")
    (tmp_path / "out").mkdir()

    class Out(io.StringIO):
        def reconfigure(self, **kw):
            pass

    monkeypatch.setattr(sys, "stdout", Out())
    (tmp_path / "README.md").write_text("| lineas de `emulator/` | 84.3 % |\n", encoding="utf-8")

    def report(pct: float) -> None:
        cov.REPORT.write_text(json.dumps({"totals": {"percent_covered": pct, "covered_lines": 1,
                                                     "num_statements": 1}, "files": {}}), encoding="utf-8")

    report(84.0)  # Linux vs Windows pueden diferir en decimas
    assert cov.main(["--check"]) == 0
    report(86.0)  # eso ya no es una decima
    assert cov.main(["--check"]) == 1
