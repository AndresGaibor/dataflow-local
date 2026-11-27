"""Carga `dfemu.local.json` (creado por `dfemu setup`) como variables de entorno por omision."""
import json
import os

try:
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dfemu.local.json"),
              encoding="utf-8") as _fh:
        for _k, _v in json.load(_fh).items():
            os.environ.setdefault(_k, str(_v))
except (OSError, ValueError):
    pass

try:  # version del paquete instalado; en modo editable o sin instalar vale la declarada
    from importlib.metadata import PackageNotFoundError, version as _version

    __version__ = _version("dfemu")
except Exception:  # noqa: BLE001 - sin metadatos (repo sin instalar)
    __version__ = "0.1.0"
