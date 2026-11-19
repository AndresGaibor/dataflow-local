"""Pruebas contra el tenant real: solo con DFEMU_TENANT=1 (marcador `tenant`)."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli  # noqa: E402


@pytest.mark.tenant
def test_compare_fundamentos_against_tenant():
    try:
        cli.main(["compare", "samples/fundamentos.dfw", "--app", os.environ.get("DFEMU_BASE_APP", "00000000-0000-0000-0000-000000000001"), "--apply"])
    except SystemExit as e:
        assert e.code in (0, None), e.code
