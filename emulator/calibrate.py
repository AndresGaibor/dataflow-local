"""Calibra el validador local (dfw.validate) contra el veredicto del servidor sobre mutaciones de un .dfw."""
import copy
from typing import Callable, NamedTuple

from . import dfw
from .bridge import BridgeError


def _nodes(d):
    return d["dataflow"]["graph"]["nodes"]


def _of(d, ctype):
    return next(n for n in _nodes(d) if n["component"]["type"] == ctype)


def _cfg(n):
    return n["component"]["properties"]["configuration"]


def _target_settings(d):
    return _cfg(next(n for n in _nodes(d) if n["type"] == "target"))["settings"]


def _sin_aristas(d):
    d["dataflow"]["graph"]["edges"] = []


def _target_sin_filename(d):
    _target_settings(d)["fileName"] = ""


def _target_sin_extension(d):
    _target_settings(d)["extension"] = ""


def _formato_xlsx(d):
    _target_settings(d)["format"] = "xlsx"


def _formato_invalido(d):
    _target_settings(d)["format"] = "zzz"


def _sin_target(d):
    d["dataflow"]["graph"]["nodes"] = [n for n in _nodes(d) if n["type"] != "target"]
    d["dataflow"]["graph"]["edges"] = []


def _sin_source(d):
    d["dataflow"]["graph"]["nodes"] = [n for n in _nodes(d) if n["type"] != "source"]


def _processor_sin_configurar(d):
    for n in _nodes(d):
        if n["type"] not in ("source", "target"):
            _cfg(n)["$state"] = "UNCONFIGURED"


def _selectors_vacios(d):
    _cfg(_of(d, "field-selector"))["selectors"] = []


def _ids_duplicados(d):
    _nodes(d)[1]["id"] = _nodes(d)[0]["id"]


MUTATIONS: dict[str, Callable[[dict], None]] = {
    "sin_aristas": _sin_aristas,
    "target_sin_fileName": _target_sin_filename,
    "target_sin_extension": _target_sin_extension,
    "formato_xlsx": _formato_xlsx,
    "formato_invalido": _formato_invalido,
    "sin_target": _sin_target,
    "sin_source": _sin_source,
    "processor_sin_configurar": _processor_sin_configurar,
    "selectors_vacios": _selectors_vacios,
    "ids_duplicados": _ids_duplicados,
}


class Row(NamedTuple):
    name: str
    local_valid: bool
    remote: str
    agree: bool


def run_battery(base_dfw: dict, remote_status: Callable[[dict], str]) -> list[Row]:
    rows = []
    for name, mut in MUTATIONS.items():
        d = copy.deepcopy(base_dfw)
        mut(d)
        local_valid = not dfw.validate(d)
        try:
            remote = remote_status(d["dataflow"]["graph"])
        except BridgeError:  # una fila fallida no oculta las demas
            remote = "ERROR"
        agree = remote != "ERROR" and local_valid == (remote not in ("INVALID", "REJECTED"))
        rows.append(Row(name, local_valid, remote, agree))
    return rows


def format_rows(rows: list[Row]) -> str:
    lines = [f"{'mutacion':<24} | {'local':<7} | {'servidor':<9} | coincide"]
    for r in rows:
        local = "VALID" if r.local_valid else "INVALID"
        lines.append(f"{r.name:<24} | {local:<7} | {r.remote:<9} | {'OK' if r.agree else 'DISCREPA'}")
    return "\n".join(lines)


def disagreements(rows: list[Row]) -> list[Row]:
    return [r for r in rows if not r.agree]
