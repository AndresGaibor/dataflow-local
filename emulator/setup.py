"""`dfemu setup`: deja el entorno listo para hablar con el tenant.

1. instala la CLI `qlik` oficial en `.tools/qlik/` si no hay una que funcione;
2. crea el contexto de la CLI pidiendo la URL y la API key (la clave no se muestra ni se guarda aqui);
3. elige el espacio de pruebas y el flujo base y los guarda en `dfemu.local.json` (ignorado por git).
"""
import getpass
import hashlib
import io
import json
import os
import platform
import re
import sys
import tarfile
import urllib.request
import zipfile
from urllib.parse import urlparse

from . import bridge
from .bridge import CLI_FILE, ROOT, TOOLS_DIR

CLI_VERSION = "4.0.0"  # version verificada; subirla solo tras probar la nueva
RELEASES = "https://github.com/qlik-oss/qlik-cli/releases/download"
LOCAL_CONFIG = os.path.join(ROOT, "dfemu.local.json")
PROBE = ["raw", "get", "v1/users/me"]  # lectura de la propia identidad: prueba que el contexto autentica


class SetupError(Exception):
    pass


def _download(url: str) -> bytes:
    if not url.startswith("https://"):
        raise SetupError(f"solo se descarga por https: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "dfemu-setup"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:  # noqa: S310 (https verificado arriba)
            return r.read()
    except OSError as e:
        raise SetupError(f"no se pudo descargar {url}: {e}") from e


def asset_name(system: str | None = None, machine: str | None = None) -> str:
    """Archivo del release para este sistema; el release solo publica x86_64."""
    system, machine = system or platform.system(), (machine or platform.machine()).lower()
    kind = {"Windows": "Windows-x86_64.zip", "Linux": "Linux-x86_64.tar.gz", "Darwin": "Darwin-x86_64.tar.gz"}.get(system)
    if kind is None:
        raise SetupError(f"sistema no soportado: {system}")
    if machine not in ("amd64", "x86_64", "arm64") or (machine == "arm64" and system != "Darwin"):
        raise SetupError(f"el release de qlik-cli no tiene binario para {system}/{machine}; instalelo a mano y defina DFEMU_QLIK")
    return "qlik-" + kind  # en Apple Silicon corre con Rosetta


def install_cli(download=_download, system: str | None = None, machine: str | None = None) -> str:
    """Descarga la CLI, verifica su SHA-256 contra el archivo de checksums del release y la extrae."""
    name = asset_name(system, machine)
    sums = download(f"{RELEASES}/v{CLI_VERSION}/qlik_{CLI_VERSION}_checksums.txt").decode("utf-8", "replace")
    expected = {p[1].lstrip("*"): p[0] for p in (ln.split() for ln in sums.splitlines()) if len(p) == 2}.get(name)
    if not expected:
        raise SetupError(f"{name} no aparece en el archivo de checksums")
    blob = download(f"{RELEASES}/v{CLI_VERSION}/{name}")
    if hashlib.sha256(blob).hexdigest() != expected.lower():
        raise SetupError(f"el SHA-256 de {name} no coincide con el del release; no se instala")
    want = os.path.basename(CLI_FILE)
    data = None
    if name.endswith(".zip"):
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            member = next((n for n in z.namelist() if os.path.basename(n) == want), None)
            data = z.read(member) if member else None
    else:
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as t:
            member = next((m for m in t.getmembers() if m.isfile() and os.path.basename(m.name) == want), None)
            data = t.extractfile(member).read() if member else None
    if data is None:
        raise SetupError(f"{want} no esta dentro de {name}")
    os.makedirs(TOOLS_DIR, exist_ok=True)
    with open(CLI_FILE, "wb") as fh:
        fh.write(data)
    os.chmod(CLI_FILE, 0o755)
    return CLI_FILE


def cli_works(runner=bridge.qlik_runner) -> bool:
    return runner(["version"])[0] == 0


def ensure_cli(runner=bridge.qlik_runner, ask=input, install=install_cli, assume_yes=False) -> str:
    if cli_works(runner):
        return "CLI de Qlik: ok"
    if not assume_yes and ask(f"No hay una CLI de Qlik que funcione. Descargar qlik-cli v{CLI_VERSION} "
                              f"de github.com/qlik-oss en {TOOLS_DIR}? [s/N] ").strip().lower() not in ("s", "si", "y", "yes"):
        raise SetupError("sin la CLI de Qlik no se puede continuar")
    path = install()
    if not cli_works(runner):
        raise SetupError(f"se instalo {path} pero no se puede ejecutar (¿politica de control de aplicaciones?); "
                         "defina DFEMU_QLIK con un qlik.exe permitido")
    return f"CLI de Qlik instalada en {path}"


def _context_name(server: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "", urlparse(server).hostname or "") or "qlik"


def ensure_context(runner=bridge.qlik_runner, ask=input, secret=getpass.getpass) -> str:
    """Si la CLI ya autentica no hace nada; si no, pide la URL y la API key y crea el contexto."""
    if runner(PROBE)[0] == 0:
        return "Contexto de Qlik: ok"
    if not sys.stdin.isatty() and ask is input:
        raise SetupError("falta un contexto de Qlik y no hay terminal para pedir la clave: ejecute `dfemu setup` en una terminal")
    server = ask("URL del tenant (https://<tenant>.<region>.qlikcloud.com): ").strip().rstrip("/")
    if urlparse(server).scheme != "https" or not urlparse(server).hostname:
        raise SetupError("la URL debe empezar por https://")
    key = secret("API key (se escribe sin mostrarse; se guarda solo en el contexto de la CLI): ").strip()
    if not key:
        raise SetupError("API key vacia")
    name = _context_name(server)
    # la CLI solo acepta la clave como argumento: queda visible en la lista de procesos mientras corre
    rc, _, err = runner(["context", "create", name, "--server", server, "--api-key", key])
    if rc != 0:  # el contexto ya existia: se actualiza
        rc, _, err = runner(["context", "update", name, "--server", server, "--api-key", key])
    if rc != 0:
        raise SetupError("no se pudo crear el contexto: " + err.replace(key, "***").strip()[:200])
    runner(["context", "use", name])
    if runner(PROBE)[0] != 0:
        raise SetupError("el contexto se creo pero el tenant rechaza la clave; revise la URL y que la clave este vigente")
    return f"Contexto de Qlik '{name}' creado"


def load_local() -> dict:
    try:
        with open(LOCAL_CONFIG, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_local(**values) -> None:
    cfg = {**load_local(), **values}
    with open(LOCAL_CONFIG, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh, indent=2)


def _pick(label: str, options: list[tuple[str, str]], ask) -> str:
    for i, (name, _) in enumerate(options, 1):
        print(f"  {i}. {name}")
    n = ask(f"{label} (numero): ").strip()
    if not n.isdigit() or not 1 <= int(n) <= len(options):
        raise SetupError(f"opcion invalida: {n!r}")
    return options[int(n) - 1][1]


def ensure_workspace(b, ask=input, space: str | None = None, base_app: str | None = None) -> str:
    """Fija DFEMU_SPACE_ID y DFEMU_BASE_APP (de los argumentos, del entorno o preguntando)."""
    from .remote import Remote
    space = space or os.environ.get("DFEMU_SPACE_ID")
    if not space:
        spaces = b.get("v1/spaces", {"limit": 100}) or []
        spaces = spaces.get("data", []) if isinstance(spaces, dict) else spaces
        if not spaces:
            raise SetupError("el tenant no devolvio espacios")
        print("Espacio donde el banco de pruebas puede escribir (solo objetos emu_):")
        space = _pick("Espacio", [(s["name"], s["id"]) for s in spaces], ask)
    base_app = base_app or os.environ.get("DFEMU_BASE_APP")
    if not base_app:
        flows = Remote(b).list_dataflows(space)
        if not flows:
            save_local(DFEMU_SPACE_ID=space)
            return "Espacio guardado; no hay flujos en el para usar de base (DFEMU_BASE_APP queda sin definir)"
        print("Flujo base (solo se lee y se clona):")
        base_app = _pick("Flujo", [(f.name, f.app_id) for f in flows], ask)
    save_local(DFEMU_SPACE_ID=space, DFEMU_BASE_APP=base_app)
    os.environ["DFEMU_SPACE_ID"], os.environ["DFEMU_BASE_APP"] = space, base_app
    return f"Guardado en {os.path.basename(LOCAL_CONFIG)}"


def run(assume_yes=False, space=None, base_app=None) -> None:
    """Orquesta los tres pasos; imprime cada resultado."""
    print(ensure_cli(assume_yes=assume_yes))
    print(ensure_context())
    print(ensure_workspace(bridge.Bridge(), space=space, base_app=base_app))
