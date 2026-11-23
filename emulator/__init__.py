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
