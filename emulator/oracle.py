"""Oráculo: ejecuta un script de flujo en un app temporal del espacio permitido y mide sus salidas.

Los STORE se redirigen a DataFiles/emu_*; nada se escribe en destinos de los flujos originales.
TableFp = {"rows": int, "columns": {col: {"count": int, "distinct": int, "sum": float | None}}}
"""
import json
import math
import os
import re
import sys
import time
from typing import NamedTuple

from .bridge import SANDBOX_SPACE_ID, Bridge
from .remote import Remote

DATAFILES_PREFIX = "lib://Entrenamiento Dataflow:DataFiles/"
LOG_TAIL = 500  # caracteres finales del log de recarga que se muestran en los errores

# Sentencia STORE estricta, sobre el texto crudo. group(1) = tabla, group(2) = ruta lib://...
# Regla deliberadamente simple: toda palabra STORE del texto debe ser el inicio de una de estas.
# Limitación aceptada: un comentario, campo [Store], cadena o ruta con "store" se rechaza (fail closed).
_STORE = re.compile(r"(?i)\bSTORE\s+(\[[^\]\r\n]+\]|\w+)\s+INTO\s+\[(lib://[^\]\r\n]+)\]\s*\([^()\r\n]*\)\s*;")
_BOM = "﻿"
_READBACK = "(txt, utf8, embedded labels, delimiter is ',', msq)"


class OracleError(Exception):
    pass


class Retargeted(NamedTuple):
    script: str
    files: dict[str, str]
    tables: dict[str, str]


def _stores(script: str) -> list[re.Match]:
    """Cada palabra STORE del texto crudo debe empezar una sentencia estricta; si no, OracleError."""
    found = list(_STORE.finditer(script))
    starts = {m.start() for m in found}
    for kw in re.finditer(r"(?i)\bSTORE\b", script):
        if kw.start() not in starts:
            raise OracleError(f"palabra STORE en un contexto no reconocido: {script[kw.start():kw.start() + 80]!r}")
    return found


def _stem(path: str) -> str:
    return os.path.splitext(path.rsplit("/", 1)[-1])[0]


def retarget(script: str, tag: str, rowno: bool = False) -> Retargeted:
    if not re.fullmatch(r"[A-Za-z0-9_]+", tag):
        raise OracleError(f"etiqueta inválida: {tag!r}")
    script = script.removeprefix(_BOM)
    matches = _stores(script)
    if not matches:
        raise OracleError("el script no guarda ninguna tabla")
    files: dict[str, str] = {}
    tables: dict[str, str] = {}
    parts: list[str] = []
    last = 0
    for n, m in enumerate(matches, 1):
        stem = _stem(m.group(2))
        if stem in files:
            raise OracleError(f"dos STORE escriben el mismo archivo '{stem}'")
        files[stem] = f"emu_{tag}_{n}.csv"
        tables[stem] = f"emu_out_{n}"
        parts += [script[last:m.start()], f"STORE {m.group(1)} INTO [{DATAFILES_PREFIX}{files[stem]}] (txt);"]
        last = m.end()
    parts.append(script[last:])
    nl = "\r\n" if "\r\n" in script else "\n"
    block = ["QUALIFY *;"]
    for stem in files:
        fields = "*, RecNo() AS [__rowno]" if rowno else "*"  # el numero de fila permite leer las primeras filas en orden
        block += [f"[{tables[stem]}]:", f"LOAD {fields} FROM [{DATAFILES_PREFIX}{files[stem]}] {_READBACK};"]
    parts.append(nl + nl + nl.join(block) + nl)
    return Retargeted("".join(parts), files, tables)


def assert_safe(script: str) -> None:
    for m in _stores(script.removeprefix(_BOM)):
        path = m.group(2)
        name = path[len(DATAFILES_PREFIX):] if path.startswith(DATAFILES_PREFIX) else ""
        if not name.startswith("emu_") or "/" in name or ".." in name:
            raise OracleError(f"STORE fuera de DataFiles/emu_*: {path}")


def parse_tables(text: str) -> dict[str, tuple[int, list[str]]]:
    out = {}
    for line in text.splitlines():
        parts = re.split(r"\s{2,}", line.strip())
        if len(parts) != 4 or not parts[1].isdigit():  # cabecera y fila de RAM total
            continue
        fields = [] if parts[3] == "-" else [f.strip() for f in parts[3].split(",")]
        out[parts[0]] = (int(parts[1]), fields)
    return out


def _num(cell) -> float | None:
    if not isinstance(cell, dict):
        return None
    try:
        v = float(cell.get("qNum"))
    except (TypeError, ValueError):
        return None
    return None if math.isnan(v) else v


def _cells(out: str) -> list:
    try:
        return json.loads(out)[0]["qMatrix"][0]
    except (ValueError, KeyError, IndexError, TypeError) as e:
        raise OracleError("respuesta de eval no reconocida") from e


def _fingerprints(bridge: Bridge, app_id: str, rt: Retargeted, head: int = 0) -> dict:
    tables = parse_tables(bridge.cli_read(["app", "tables", "--app", app_id]))
    fp = {}
    for stem, table in rt.tables.items():
        if table not in tables:
            raise OracleError(f"la tabla {table} no aparece en el modelo")
        rows, fields = tables[table]
        fields = [f for f in fields if not f.endswith("__rowno")]
        qs = [f if f.startswith(table + ".") else f"{table}.{f}" for f in fields]
        cols = {}
        if qs:  # un solo app eval por tabla: tres medidas por campo, en orden
            exprs = []
            for q in qs:
                exprs += [f"Count([{q}])", f"Count(distinct [{q}])", f"Sum([{q}])"]
            cells = _cells(bridge.cli_read(["app", "eval", "--app", app_id, *exprs, "--json"]))
            if len(cells) != len(exprs):
                raise OracleError(f"el eval devolvió {len(cells)} celdas; se esperaban {len(exprs)}")
            for i, q in enumerate(qs):
                count, distinct = _num(cells[3 * i]), _num(cells[3 * i + 1])
                if count is None or distinct is None:
                    raise OracleError(f"conteo no numérico para {q}")
                cols[q[len(table) + 1:]] = {"count": int(count), "distinct": int(distinct),
                                            "sum": _num(cells[3 * i + 2])}
        if head and qs:  # texto de las primeras filas de cada columna, en el orden del archivo
            heads = [f"Concat(If([{table}.__rowno] <= {head}, Text([{q}])), '|', [{table}.__rowno])" for q in qs]
            hcells = _cells(bridge.cli_read(["app", "eval", "--app", app_id, *heads, "--json"]))
            if len(hcells) != len(heads):
                raise OracleError(f"el eval de primeras filas devolvió {len(hcells)} celdas; se esperaban {len(heads)}")
            for q, cell in zip(qs, hcells):
                cols[q[len(table) + 1:]]["head"] = (cell.get("qText") or "") if isinstance(cell, dict) else ""
        fp[stem] = {"rows": rows, "columns": cols}
    return fp


def _wait_reload(bridge: Bridge, rid: str, timeout: int, poll_seconds: float) -> tuple[str, str]:
    deadline = time.monotonic() + timeout
    while True:
        r = bridge.get(f"v1/reloads/{rid}") or {}
        status, log = r.get("status"), str(r.get("log") or "")
        if status in ("SUCCEEDED", "FAILED"):
            return status, log
        if time.monotonic() >= deadline:
            raise OracleError(f"timeout tras {timeout}s esperando la recarga: {log[-LOG_TAIL:]}")
        time.sleep(poll_seconds)


def _best_effort(what: str, fn, arg) -> None:
    try:
        fn(arg)
    except Exception as e:  # la limpieza nunca oculta el error original
        print(f"aviso: no se pudo {what}: {e}", file=sys.stderr)


def run_script(bridge: Bridge, script: str, tag: str, timeout: int = 180,
               poll_seconds: float = 2, head: int = 0) -> dict:
    rt = retarget(script, tag, rowno=bool(head))
    assert_safe(rt.script)
    remote = Remote(bridge)
    app_id = reload_id = None
    reload_done = False
    try:
        created = bridge.post("v1/apps", {"attributes": {"name": f"emu_oracle_{tag}",
                                                         "spaceId": SANDBOX_SPACE_ID}}) or {}
        app_id = (created.get("attributes") or {}).get("id")
        if not app_id:
            raise OracleError("respuesta sin id de app")
        bridge.script_set(app_id, rt.script)
        errors = (bridge.post("v1/apps/validatescript", {"script": rt.script}) or {}).get("Errors") or []
        if errors:
            e = errors[0]
            raise OracleError(f"validación: {e.get('Msg')} (línea {e.get('Line')})")
        reload_id = (bridge.post("v1/reloads", {"appId": app_id}) or {}).get("id")
        if not reload_id:
            raise OracleError("respuesta sin id de recarga")
        status, log = _wait_reload(bridge, reload_id, timeout, poll_seconds)
        reload_done = True
        if status != "SUCCEEDED":
            raise OracleError(f"la recarga falló: {log[-LOG_TAIL:]}")
        return _fingerprints(bridge, app_id, rt, head)
    finally:
        if reload_id and not reload_done:  # recarga viva: cancelarla antes de borrar nada
            _best_effort("cancelar la recarga", bridge.post, f"v1/reloads/{reload_id}/actions/cancel")
        if app_id:
            _best_effort(f"borrar el app {app_id}", remote.discard, app_id)
        if reload_id:  # solo si la recarga llegó a iniciarse
            _best_effort("borrar los archivos emu_", remote.discard_files, list(rt.files.values()))
