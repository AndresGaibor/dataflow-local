"""Qlik Automate por API: listar, leer, crear, modificar, borrar y ejecutar automatizaciones.

Todo pasa por el `Bridge`, asi que solo toca objetos `emu_*` del espacio de
pruebas y simula salvo que se pase `--apply`. Las rutas son las vigentes
(`api/workflows/automations`); `api/v1/automations` esta deprecada.
"""
import os

from .bridge import PREFIX, SANDBOX_SPACE_ID, SafetyError, valid_id

BASE = "api/workflows/automations"


def _id(automation_id: str) -> str:
    if not valid_id(automation_id):
        raise SafetyError(f"id de automatización inválido: {automation_id!r}")
    return automation_id


def ls(bridge) -> list[dict]:
    """Automatizaciones visibles para la credencial."""
    return (bridge.get(BASE) or {}).get("data") or []


def show(bridge, automation_id: str) -> dict:
    """Definición completa (incluye `workspace`, los bloques del editor)."""
    return bridge.get(f"{BASE}/{_id(automation_id)}") or {}


def new(bridge, name: str, workspace: dict | None = None, description: str = "") -> dict:
    """Crea una automatización; el nombre debe empezar por `emu_`."""
    if not name.startswith(PREFIX):
        raise SafetyError(f"el nombre debe empezar por {PREFIX!r}: {name!r}")
    body = {"name": name, "spaceId": SANDBOX_SPACE_ID}
    if workspace is not None:
        body["workspace"] = workspace
    if description:
        body["description"] = description
    return bridge.post(BASE, body) or {}


def set(bridge, automation_id: str, **fields) -> dict:
    """Actualiza campos de una automatización (por omision: lo que ya tiene)."""
    _id(automation_id)
    body = {"name": fields.pop("name", None) or show(bridge, automation_id).get("name"), **fields}
    return bridge.put(f"{BASE}/{automation_id}", {k: v for k, v in body.items() if v is not None}) or {}


def rm(bridge, automation_id: str) -> None:
    bridge.delete(f"{BASE}/{_id(automation_id)}")


def enable(bridge, automation_id: str) -> dict:
    return bridge.post(f"{BASE}/{_id(automation_id)}/actions/enable", {}) or {}


def disable(bridge, automation_id: str) -> dict:
    return bridge.post(f"{BASE}/{_id(automation_id)}/actions/disable", {}) or {}


def copy(bridge, automation_id: str, name: str) -> dict:
    """Duplica una automatización con un nombre nuevo (también `emu_`)."""
    if not name.startswith(PREFIX):
        raise SafetyError(f"el nombre debe empezar por {PREFIX!r}: {name!r}")
    return bridge.post(f"{BASE}/{_id(automation_id)}/actions/copy",
                       {"name": name, "spaceId": SANDBOX_SPACE_ID}) or {}


def run(bridge, automation_id: str) -> dict:
    """Lanza una ejecución (escribe: sin `--apply` el Bridge simula)."""
    return bridge.post(f"{BASE}/{_id(automation_id)}/runs", {}) or {}


def runs(bridge, automation_id: str) -> list[dict]:
    return (bridge.get(f"{BASE}/{_id(automation_id)}/runs") or {}).get("data") or []


def run_get(bridge, automation_id: str, run_id: str) -> dict:
    return bridge.get(f"{BASE}/{_id(automation_id)}/runs/{_id(run_id)}") or {}


def stop(bridge, automation_id: str, run_id: str) -> dict:
    return bridge.post(f"{BASE}/{_id(automation_id)}/runs/{_id(run_id)}/actions/stop", {}) or {}
