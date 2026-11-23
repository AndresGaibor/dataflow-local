import os

import pytest

# Las pruebas locales fijan ids de relleno aunque exista dfemu.local.json (lo carga emulator/__init__.py,
# que se importa despues de este archivo). Con DFEMU_TENANT=1 se usan los ids reales.
if os.environ.get("DFEMU_TENANT") != "1":
    os.environ["DFEMU_SPACE_ID"] = "000000000000000000000000"
    os.environ["DFEMU_BASE_APP"] = "00000000-0000-0000-0000-000000000001"


def pytest_configure(config):
    config.addinivalue_line("markers", "tenant: toca el tenant real de Qlik (requiere DFEMU_TENANT=1)")


def pytest_collection_modifyitems(config, items):
    if os.environ.get("DFEMU_TENANT") == "1":
        return
    skip = pytest.mark.skip(reason="prueba de tenant real; definir DFEMU_TENANT=1 para ejecutarla")
    for item in items:
        if "tenant" in item.keywords:
            item.add_marker(skip)
