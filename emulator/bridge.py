"""Único punto de acceso al tenant vía `qlik` CLI, con política de escritura."""
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from typing import Any, Callable

# Espacio de pruebas donde se permite escribir. Sin valor por omision: se configura
# con DFEMU_SPACE_ID para que ninguna instalacion escriba en un tenant ajeno.
SANDBOX_SPACE_ID = os.environ.get("DFEMU_SPACE_ID", "000000000000000000000000")
PREFIX = "emu_"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(ROOT, ".tools", "qlik")  # donde `dfemu setup` instala la CLI
CLI_FILE = os.path.join(TOOLS_DIR, "qlik.exe" if os.name == "nt" else "qlik")
TIMEOUT_S = 60
VALIDATE = "v1/apps/validatescript"  # única escritura-lectura permitida sin simulación


class SafetyError(Exception):
    pass


class BridgeError(Exception):
    def __init__(self, msg, rc=1, stderr=""):
        super().__init__(msg)
        self.rc = rc
        self.stderr = stderr


class DryRun(Exception):
    def __init__(self, method, path, body):
        super().__init__(f"simulado: {method} {path}")
        self.method = method
        self.path = path
        self.body = body


Runner = Callable[[list[str]], tuple[int, str, str]]


def _qlik_exe() -> str:
    """Ejecutable de la CLI, por orden: DFEMU_QLIK, la instalada por `dfemu setup`, el binario real de
    Chocolatey y el del PATH. En Windows con Code Integrity (WDAC) el acceso directo de Chocolatey
    (`bin/qlik.exe`, sin firma) se bloquea; el binario real, firmado por Qlik, corre."""
    if os.environ.get("DFEMU_QLIK"):
        return os.environ["DFEMU_QLIK"]
    if os.path.isfile(CLI_FILE):
        return CLI_FILE
    choco = os.environ.get("ChocolateyInstall") or r"C:\ProgramData\chocolatey"
    real = os.path.join(choco, "lib", "qlik-cli", "tools", "qlik.exe")
    return real if os.path.isfile(real) else "qlik"


def qlik_runner(args: list[str]) -> tuple[int, str, str]:
    exe = _qlik_exe()
    if os.environ.get("DFEMU_QLIK_CONTEXT") and args[:1] != ["context"]:  # otro contexto sin activarlo; `context ...` los gestiona `setup`
        args = ["--context", os.environ["DFEMU_QLIK_CONTEXT"], *args]
    try:
        p = subprocess.run([exe, *args], capture_output=True, text=True, encoding="utf-8",
                           stdin=subprocess.DEVNULL, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout tras {TIMEOUT_S}s"
    except FileNotFoundError:  # la CLI no está instalada
        return 127, "", "no se encontro la CLI qlik; ejecute `python -m emulator.cli setup`"
    except OSError as e:  # p. ej. bloqueada por una politica de control de aplicaciones
        return 126, "", f"no se pudo ejecutar {exe}: {e}. Ejecute `python -m emulator.cli setup` o defina DFEMU_QLIK con la ruta del qlik.exe firmado"
    return p.returncode, p.stdout, p.stderr


def _parse(out: str) -> Any:
    if not out.strip():
        return None
    try:
        return json.loads(out)
    except ValueError as e:
        raise BridgeError(f"salida no JSON: {out[:200]}") from e


ID_RE = re.compile(r"[A-Za-z0-9_-]+")  # ids que se interpolan en rutas de búsqueda


def valid_id(x: Any) -> bool:
    return isinstance(x, str) and ID_RE.fullmatch(x) is not None


def _is_emu(attrs: dict) -> bool:
    return str(attrs.get("name", "")).startswith(PREFIX) and attrs.get("spaceId") == SANDBOX_SPACE_ID


class Bridge:
    def __init__(self, runner: Runner = qlik_runner, apply: bool = False,
                 audit_path: str = "out/audit.jsonl"):
        self._runner = runner
        self._apply = apply
        self._audit_path = audit_path

    # --- ejecución ---------------------------------------------------------
    def _run(self, args: list[str]) -> str:
        rc, out, err = self._runner(args)
        if rc != 0:
            raise BridgeError(f"qlik {' '.join(args[:2])} falló (rc={rc}): {err.strip()}", rc, err)
        return out

    def _raw(self, method: str, path: str, query: dict | None = None, body: Any = None) -> Any:
        args = ["raw", method.lower(), path]
        for k, v in (query or {}).items():
            args += ["--query", f"{k}={v}"]
        tmp = None
        if body is not None:
            fd, tmp = tempfile.mkstemp(suffix=".json")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(body, f, ensure_ascii=False)
            args += ["--body-file", tmp]
        try:
            return _parse(self._run(args))
        finally:
            if tmp:
                os.remove(tmp)

    # --- política ----------------------------------------------------------
    def _app_is_emu(self, app_id: str) -> bool:
        if not valid_id(app_id):
            raise SafetyError(f"id de app inválido: {app_id!r}")
        resp = self._raw("GET", f"v1/apps/{app_id}") or {}
        return _is_emu(resp.get("attributes") or {})

    def _authorize(self, method: str, path: str, body: Any) -> None:
        ok = False
        if method == "POST" and path == "v1/apps" and isinstance(body, dict):
            attrs = body.get("attributes") or {}
            ok = _is_emu(attrs)
        elif method == "POST" and re.fullmatch(r"v1/dataflow-apps/[^/]+/actions/copy", path):
            ok = isinstance(body, dict) and _is_emu({"name": body.get("name"), "spaceId": body.get("spaceId")})
        elif method == "PUT" and (m := re.fullmatch(r"v1/dataflows/([^/]+)", path)):
            if not valid_id(m.group(1)):
                raise SafetyError(f"id de flujo inválido: {m.group(1)!r}")
            df = self._raw("GET", path) or {}
            ok = self._app_is_emu((df.get("context") or {}).get("dataAppId", ""))
        elif method == "POST" and path == "v1/reloads":
            ok = isinstance(body, dict) and self._app_is_emu(str(body.get("appId", "")))
        elif method == "POST" and (m := re.fullmatch(r"v1/reloads/([^/]+)/actions/cancel", path)):
            if not valid_id(m.group(1)):
                raise SafetyError(f"id de recarga inválido: {m.group(1)!r}")
            ok = self._app_is_emu(str((self._raw("GET", f"v1/reloads/{m.group(1)}") or {}).get("appId", "")))
        elif m := re.fullmatch(r"v1/apps/([^/]+)", path):
            if method == "DELETE":
                ok = self._app_is_emu(m.group(1))
        elif method == "POST" and path == "v1/data-files/actions/delete":
            items = body.get("delete") if isinstance(body, dict) else None
            ids = [i.get("id") if isinstance(i, dict) else None for i in items] if isinstance(items, list) else []
            if not ids or not all(valid_id(i) for i in ids):
                raise SafetyError("lista de ids de archivos inválida")
            ok = all(_is_emu(self._raw("GET", f"v1/data-files/{i}") or {}) for i in ids)
        elif method == "POST" and (m := re.fullmatch(r"scheduling/tasks/resources/([^/]+)/actions/reload/(on-time-schedule|on-task-event)", path)):
            ok = self._app_is_emu(m.group(1))
            if ok and m.group(2) == "on-task-event":  # la tarea previa tambien debe ser de una app emu_
                up = body.get("onTaskId") if isinstance(body, dict) else None
                ok = isinstance(up, str) and self._task_app_is_emu(up)
        elif method == "POST" and (m := re.fullmatch(r"scheduling/tasks/([^/]+)/actions/start", path)):
            app = self._task_app(m.group(1))
            ok = self._app_is_emu(app) and self._stores_only_emu(app)
        elif method == "DELETE" and (m := re.fullmatch(r"scheduling/tasks/([^/]+)", path)):
            ok = self._task_app_is_emu(m.group(1))
        elif method == "PATCH" and (m := re.fullmatch(r"scheduling/tasks/([^/]+)", path)):
            # solo habilitar o deshabilitar: un unico `replace` de /enabled con un booleano
            patch_ok = (isinstance(body, list) and len(body) == 1 and isinstance(body[0], dict)
                        and body[0].get("op") == "replace" and body[0].get("path") == "/enabled"
                        and isinstance(body[0].get("value"), bool) and set(body[0]) == {"op", "path", "value"})
            ok = patch_ok and self._task_app_is_emu(m.group(1))
        if not ok:
            raise SafetyError(f"escritura no permitida: {method} {path}")

    def _task_app(self, task_id: str) -> str:
        if not valid_id(task_id):
            raise SafetyError(f"id de tarea inválido: {task_id!r}")
        return str((self._raw("GET", f"scheduling/tasks/{task_id}") or {}).get("resourceId", ""))

    def _task_app_is_emu(self, task_id: str) -> bool:
        return self._app_is_emu(self._task_app(task_id))

    def _stores_only_emu(self, app_id: str) -> bool:
        """Una tarea solo arranca si todo STORE del script escribe en un archivo emu_ (no pisa salidas reales)."""
        script = str((self._raw("GET", f"v1/apps/{app_id}/scripts/current") or {}).get("script", ""))
        words = [mm.start() for mm in re.finditer(r"(?i)\bSTORE\b", script)]
        good = [mm.start() for mm in re.finditer(
            r"(?i)\bSTORE\s+\[[^\]]+\]\s+INTO\s+\[lib://[^\]$]*/emu_[^/\]$]*\]", script)]  # sin `$`: una variable se expande al ejecutar
        if words != good:
            raise SafetyError("el script tiene un STORE que no escribe en un archivo emu_; la tarea no se ejecuta")
        return True

    def _audit(self, method: str, path: str, applied: bool) -> None:
        os.makedirs(os.path.dirname(self._audit_path) or ".", exist_ok=True)
        line = {"ts": datetime.now(timezone.utc).isoformat(), "method": method, "path": path,
                "applied": applied}
        with open(self._audit_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(line) + "\n")

    def _write(self, method: str, path: str, body: Any = None) -> Any:
        self._authorize(method, path, body)
        self._audit(method, path, self._apply)
        if not self._apply:
            raise DryRun(method, path, body)
        return self._raw(method, path, body=body)

    # --- API pública -------------------------------------------------------
    def get(self, path: str, query: dict | None = None) -> Any:
        return self._raw("GET", path, query=query)

    def post(self, path: str, body: dict | None = None) -> Any:
        if path == VALIDATE:
            return self._raw("POST", path, body=body)
        return self._write("POST", path, body)

    def put(self, path: str, body: dict) -> Any:
        return self._write("PUT", path, body)

    def delete(self, path: str) -> Any:
        return self._write("DELETE", path)

    def patch(self, path: str, body: list) -> Any:
        return self._write("PATCH", path, body)

    def script_set(self, app_id: str, script: str) -> None:
        if not self._app_is_emu(app_id):
            raise SafetyError(f"app no permitida para script: {app_id}")
        self._audit("CLI", f"app/{app_id}/script", self._apply)
        if not self._apply:
            raise DryRun("CLI", f"app/{app_id}/script", script)
        fd, tmp = tempfile.mkstemp(suffix=".qvs")
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:  # sin traducir CRLF
                f.write(script)
            self._run(["app", "script", "set", tmp, "--app", app_id])
        finally:
            os.remove(tmp)

    def cli_read(self, args: list[str]) -> str:
        if args[:2] not in (["app", "tables"], ["app", "eval"]):
            raise SafetyError(f"comando de lectura no permitido: {args[:2]}")
        return self._run(args)
