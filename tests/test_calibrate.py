import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import calibrate, dfw  # noqa: E402
from emulator.bridge import BridgeError  # noqa: E402

BASE = dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))
NAMES = {"sin_aristas", "target_sin_fileName", "target_sin_extension", "formato_xlsx", "formato_invalido",
         "sin_target", "sin_source", "processor_sin_configurar", "selectors_vacios", "ids_duplicados"}


def test_mutations_do_not_touch_base():
    before = copy.deepcopy(BASE)
    calibrate.run_battery(BASE, lambda g: "VALID")
    assert BASE == before


def test_battery_covers_all_names():
    assert set(calibrate.MUTATIONS) == NAMES
    assert {r.name for r in calibrate.run_battery(BASE, lambda g: "VALID")} == NAMES


def test_agree_logic():
    rows = calibrate.run_battery(BASE, lambda g: "INVALID")
    assert any(r.local_valid for r in rows) and any(not r.local_valid for r in rows)
    for r in rows:
        assert r.remote == "INVALID"
        assert r.agree == (not r.local_valid)
    assert calibrate.disagreements(rows) == [r for r in rows if not r.agree]


def test_unchanged_counts_as_valid():
    rows = calibrate.run_battery(BASE, lambda g: "UNCHANGED")
    for r in rows:
        assert r.agree == r.local_valid


def test_rejected_counts_as_invalid():
    rows = calibrate.run_battery(BASE, lambda g: "REJECTED")
    for r in rows:
        assert r.agree == (not r.local_valid)


def test_bridge_error_row_does_not_stop_battery():
    state = {"n": 0}

    def remote(g):
        state["n"] += 1
        if state["n"] == 1:
            raise BridgeError("boom")
        return "VALID"

    rows = calibrate.run_battery(BASE, remote)
    assert [r.name for r in rows] == list(calibrate.MUTATIONS)
    assert rows[0].remote == "ERROR" and rows[0].agree is False
    assert rows[0].local_valid is False  # sin_aristas: el veredicto local se calcula igual
    assert all(r.remote == "VALID" for r in rows[1:])


# veredictos del servidor (tenant, 2026-11-19): True = VALID, False = INVALID/REJECTED
RECORDED = {"sin_aristas": False, "target_sin_fileName": False, "target_sin_extension": False,
            "formato_xlsx": True, "formato_invalido": True, "sin_target": False, "sin_source": False,
            "processor_sin_configurar": True, "selectors_vacios": False, "ids_duplicados": False}


def test_local_matches_recorded_server_verdicts():
    assert set(RECORDED) == NAMES
    for name, mut in calibrate.MUTATIONS.items():
        d = copy.deepcopy(BASE)
        mut(d)
        assert (dfw.validate(d) == []) == RECORDED[name], name
