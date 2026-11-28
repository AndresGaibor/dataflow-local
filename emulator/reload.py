"""Recarga de una app emu_ por la API de Qlik Cloud (`v1/reloads`).

Medido el 2026-11-27 contra el tenant: `POST v1/reloads {"appId": ...}` responde el objeto de recarga con
`id` y `status: QUEUED`; `GET v1/reloads/{id}` pasa por `RELOADING` y termina en `SUCCEEDED` o `FAILED`.
En `FAILED` el campo `log` trae el error del motor (por ejemplo, un destino de Google Drive con ruta
invalida). El Bridge solo autoriza la recarga de apps `emu_` del espacio de pruebas.
"""
from __future__ import annotations

import time

TERMINAL = ("SUCCEEDED", "FAILED", "CANCELED", "ABORTED")


def start(bridge, app_id: str) -> dict:
    """Lanza la recarga y devuelve el objeto de recarga del servidor."""
    resp = bridge.post("v1/reloads", {"appId": app_id})
    if not isinstance(resp, dict) or "id" not in resp:
        raise ValueError("respuesta de v1/reloads sin id")
    return resp


def status(bridge, reload_id: str) -> dict:
    resp = bridge.get(f"v1/reloads/{reload_id}")
    if not isinstance(resp, dict) or "status" not in resp:
        raise ValueError(f"respuesta de v1/reloads/{reload_id} sin status")
    return resp


def wait(bridge, reload_id: str, timeout: float = 300, interval: float = 2.0) -> dict:
    """Espera al estado final. Devuelve la ultima respuesta, con `ok` añadido."""
    deadline = time.monotonic() + timeout
    seen, last = [], None
    while True:
        last = status(bridge, reload_id)
        if not seen or seen[-1] != last["status"]:
            seen.append(last["status"])
        if last["status"] in TERMINAL or time.monotonic() >= deadline:
            break
        time.sleep(interval)
    out = dict(last)
    out["ok"] = last["status"] == "SUCCEEDED"
    out["states"] = seen
    return out


def run(bridge, app_id: str, wait_for: bool = True, timeout: float = 300, interval: float = 2.0) -> dict:
    """Lanza la recarga y, si se pide, espera al final."""
    started = start(bridge, app_id)
    if not wait_for:
        return {**started, "ok": None, "states": [started.get("status")]}
    return wait(bridge, started["id"], timeout, interval)


def summary(res: dict) -> str:
    """Una linea para la consola, sin volcar el log entero."""
    states = " / ".join(res.get("states") or [])
    line = f"recarga {res.get('id')}: {states}"
    log = res.get("log") or ""
    if res.get("status") != "SUCCEEDED" and log:
        # el motor repite el error a mitad del log; la linea util es la del mensaje
        err = [l for l in log.splitlines() if l.strip() and not l.startswith(("ReloadID", "Started", "("))]
        line += f"\n  {err[-1][:200] if err else log.splitlines()[-1][:200]}"
    return line
