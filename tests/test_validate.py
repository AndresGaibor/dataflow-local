import glob
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from emulator import dfw  # noqa: E402
import make_examples  # noqa: E402

# exports reales que son borradores a medias (nodos sin conectar / sin configurar)
DRAFTS = {"DF_03_TRANSACCIONES.dfw", "Repaso Dataflow Demo.dfw", "normalización.dfw"}
REAL = [f for f in sorted(glob.glob(os.path.join(ROOT, "samples", "*.dfw")))]


@pytest.fixture(scope="session", autouse=True)
def generated():
    make_examples.main()


@pytest.mark.parametrize("path", REAL, ids=os.path.basename)
def test_real(path):
    errs = dfw.validate(dfw.load(path))
    assert bool(errs) == (os.path.basename(path) in DRAFTS), errs


@pytest.mark.parametrize("fn", make_examples.VALID, ids=lambda f: f.__name__)
def test_synthetic_valid(fn):
    assert dfw.validate(fn().dump()) == []


def test_xlsx_target_is_valid_locally():  # el servidor acepta xlsx (medido en el tenant)
    d = dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))
    tgt = next(n for n in d["dataflow"]["graph"]["nodes"] if n["type"] == "target")
    tgt["component"]["properties"]["configuration"]["settings"]["format"] = "xlsx"
    assert dfw.validate(d) == []


@pytest.mark.parametrize("name", make_examples.INVALID)
def test_invalid(name):
    fn, mut, expected = make_examples.INVALID[name]
    errs = dfw.validate(make_examples._mutate(fn, mut))
    assert any(expected in e for e in errs), errs


def _fund():
    return dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))


def _cfg_of(d, kind):
    n = next(n for n in d["dataflow"]["graph"]["nodes"] if n["type"] == kind or n["component"]["type"] == kind)
    return n["component"]["properties"]["configuration"]


def test_unknown_target_format_not_checked_locally():  # el servidor no valida el valor de format
    d = _fund()
    _cfg_of(d, "target")["settings"]["format"] = "zzz"
    assert dfw.validate(d) == []


def test_unconfigured_state_not_checked_locally():  # el servidor: $state solo no invalida
    d = _fund()
    for n in d["dataflow"]["graph"]["nodes"]:
        if n["type"] not in ("source", "target"):
            n["component"]["properties"]["configuration"]["$state"] = "UNCONFIGURED"
    assert dfw.validate(d) == []


def test_empty_field_selector_is_invalid():
    d = _fund()
    _cfg_of(d, "field-selector")["selectors"] = []
    assert any("field-selector sin campos seleccionados" in e for e in dfw.validate(d))


def test_field_selector_with_no_selected_field_is_invalid():
    d = _fund()
    for s in _cfg_of(d, "field-selector")["selectors"]:
        s["selected"] = False
    assert any("field-selector sin campos seleccionados" in e for e in dfw.validate(d))
