import os

import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "tenant: toca el tenant real de Qlik (requiere DFEMU_TENANT=1)")


def pytest_collection_modifyitems(config, items):
    if os.environ.get("DFEMU_TENANT") == "1":
        return
    skip = pytest.mark.skip(reason="prueba de tenant real; definir DFEMU_TENANT=1 para ejecutarla")
    for item in items:
        if "tenant" in item.keywords:
            item.add_marker(skip)
