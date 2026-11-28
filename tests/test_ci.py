"""CI y cobertura publicada: el workflow y el bloque del README no se desincronizan.

Sin push no hay CI ejecutado, asi que lo que si se puede comprobar en local es el contrato: la matriz
(trabajo de Windows incluido), los pasos, y que la cifra del README sea la del ultimo `coverage.json`.
"""
import importlib.util
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github" / "workflows" / "tests.yml"


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def workflow():
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def test_matrix_runs_ubuntu_and_windows_with_both_pythons(workflow):
    job = workflow["jobs"]["pytest"]
    matrix = job["strategy"]["matrix"]
    assert set(matrix["os"]) == {"ubuntu-latest", "windows-latest"}
    assert set(matrix["python-version"]) == {"3.11", "3.12"}
    assert job["strategy"]["fail-fast"] is False


def test_steps_cover_tests_coverage_mcp_and_samples(workflow):
    runs = "\n".join(s.get("run", "") for s in workflow["jobs"]["pytest"]["steps"])
    assert "pytest" in runs and "--cov=emulator" in runs
    assert "scripts/test_coverage.py --check" in runs
    assert "emulator.cli mcp --list" in runs
    assert "emulator.cli coverage" in runs


def test_workflow_installs_from_the_pinned_requirements(workflow):
    uses = [s.get("uses", "") for s in workflow["jobs"]["pytest"]["steps"]]
    assert any(u.startswith("actions/checkout@") for u in uses)
    assert any(u.startswith("actions/setup-python@") for u in uses)


def test_requirements_pin_pytest_cov():
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "pytest-cov==" in text


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
