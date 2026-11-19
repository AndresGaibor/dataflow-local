"""Cobertura del corpus: processors usados y si el emulador puede ejecutar cada flujo.

Estados por archivo: `ejecuta`, `borrador` (no valida), `solo tenant` (script de Qlik),
`requiere conexion` (fuente sin tablas en el .dfw o conexion sin configurar) y `falla`.
"""
import collections
import glob
import os
import tempfile

from . import dfw, runner

EJECUTA, BORRADOR, SOLO_TENANT, REQUIERE_CONEXION, FALLA = (
    "ejecuta", "borrador", "solo tenant", "requiere conexion", "falla")


def processors_of(d: dict) -> collections.Counter:
    """(processor, variante) -> veces, contando subflujos."""
    out = collections.Counter()
    for sf in [d["dataflow"]] + d.get("subflows", []):
        for n in sf["graph"]["nodes"]:
            if n.get("type") != "processor":
                continue
            c = n["component"]
            cfg = (c.get("properties") or {}).get("configuration") or {}
            out[(c.get("type"), cfg.get("type"))] += 1
    return out


def classify(exc: Exception) -> tuple[str, str]:
    if isinstance(exc, runner.Unsupported):
        msg = str(exc)
        if "script de Qlik" in msg:
            return SOLO_TENANT, msg
        if "conexion" in msg:
            return REQUIERE_CONEXION, msg
    return FALLA, f"{type(exc).__name__}: {exc}"


def run_file(path: str, data_dir: str) -> tuple[str, str]:
    try:
        d = dfw.load(path)
    except ValueError as e:
        return FALLA, f"no es JSON: {e}"
    errs = dfw.validate(d)
    if errs:
        return BORRADOR, errs[0]
    try:
        with tempfile.TemporaryDirectory() as tmp:
            runner.run(d, data_dir, tmp)
        return EJECUTA, ""
    except Exception as e:  # el estado resume el motivo; el detalle queda en la fila
        return classify(e)


def report(paths: list[str], data_dir: str) -> list[tuple[str, str, str]]:
    return [(p, *run_file(p, data_dir)) for p in paths]


def default_paths() -> list[str]:
    return sorted(glob.glob(os.path.join("samples", "**", "*.dfw"), recursive=True))
