"""Orquestacion: programa, encadena, arranca y borra tareas de recarga con la API `scheduling`.

Solo aplica a apps `emu_` del espacio de pruebas (lo hace cumplir `Bridge`). Una tarea no arranca si
el script de su app escribe en un archivo que no es `emu_`. Verificado el 2026-11-23: ver
docs/banco-de-pruebas/01-hallazgos-api-qlik.md, apartado 10 ter.
"""
from .bridge import Bridge, SafetyError, valid_id

STATUSES = ("succeeded", "failed", "any")


def _app(app_id: str) -> str:
    if not valid_id(app_id):
        raise SafetyError(f"id de app inválido: {app_id!r}")
    return app_id


def _rows(resp) -> list[dict]:
    return resp.get("data", []) if isinstance(resp, dict) else (resp or [])


def schedule(b: Bridge, app_id: str, name: str, recurrence: str, timezone: str = "UTC", enabled: bool = False) -> dict:
    """Tarea que recarga la app segun una regla RFC 5545 (`RRULE:FREQ=DAILY;BYHOUR=3;...`)."""
    return b.post(f"scheduling/tasks/resources/{_app(app_id)}/actions/reload/on-time-schedule",
                  {"name": name, "recurrence": recurrence, "timezone": timezone, "enabled": enabled}) or {}


def chain(b: Bridge, app_id: str, name: str, after_task: str, status: str = "succeeded", enabled: bool = False) -> dict:
    """Tarea que recarga la app cuando `after_task` termina con `status`."""
    if status not in STATUSES:
        raise ValueError(f"estado {status!r}; use uno de {', '.join(STATUSES)}")
    return b.post(f"scheduling/tasks/resources/{_app(app_id)}/actions/reload/on-task-event",
                  {"name": name, "onTaskId": after_task, "onTaskStatus": status, "enabled": enabled}) or {}


def list_tasks(b: Bridge, app_id: str) -> list[dict]:
    return _rows(b.get("scheduling/tasks", {"resourceId": _app(app_id)}))


def start(b: Bridge, task_id: str) -> dict:
    """Arranca la tarea ya. Qlik rechaza las deshabilitadas (CHO-012): crearla con enabled=True."""
    return b.post(f"scheduling/tasks/{task_id}/actions/start") or {}


def runs(b: Bridge, task_id: str) -> list[dict]:
    if not valid_id(task_id):
        raise SafetyError(f"id de tarea inválido: {task_id!r}")
    return _rows(b.get(f"scheduling/tasks/{task_id}/runs"))


def delete(b: Bridge, task_id: str) -> None:
    b.delete(f"scheduling/tasks/{task_id}")


def set_enabled(b: Bridge, task_id: str, enabled: bool) -> None:
    """Habilita o deshabilita una tarea (JSON Patch, RFC 6902). El puente solo admite este cambio."""
    if not valid_id(task_id):
        raise SafetyError(f"id de tarea inválido: {task_id!r}")
    b.patch(f"scheduling/tasks/{task_id}", [{"op": "replace", "path": "/enabled", "value": enabled}])
