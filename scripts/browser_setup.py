"""Deja listo el control de tu Chrome para los agentes y comprueba cada paso.

    python scripts/browser_setup.py            # comprueba e instala lo que falte (playwright-cli) y conecta la sesion
    python scripts/browser_setup.py --mcp      # ademas registra los MCP playwright y chrome-devtools en Claude Code
    python scripts/browser_setup.py --detach   # cierra la sesion (despues desmarque la depuracion remota en Chrome)

Lo unico que no se puede automatizar es marcar la casilla de depuracion remota en Chrome (paso 2 de
docs/banco-de-pruebas/04-control-de-chrome.md): es una decision de seguridad del usuario.
"""
import argparse
import os
import shutil
import subprocess
import sys

SESSION = os.environ.get("DFEMU_BROWSER_SESSION", "chrome")
USER_DATA = {  # donde Chrome escribe DevToolsActivePort cuando la depuracion remota esta activa
    "nt": os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "User Data"),
    "darwin": os.path.expanduser("~/Library/Application Support/Google/Chrome"),
}.get(os.name if os.name == "nt" else sys.platform, os.path.expanduser("~/.config/google-chrome"))


def run(*cmd: str, timeout: int = 180) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", stdin=subprocess.DEVNULL,
                           timeout=timeout, shell=os.name == "nt")
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, str(e)
    return p.returncode, (p.stdout + p.stderr).strip()


def step(ok: bool, msg: str, hint: str = "") -> bool:
    print(("[ok]  " if ok else "[FALTA] ") + msg + ("" if ok else f"\n        -> {hint}"))
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mcp", action="store_true", help="registra los MCP playwright y chrome-devtools (nivel usuario)")
    ap.add_argument("--detach", action="store_true", help="cierra la sesion")
    a = ap.parse_args()
    if a.detach:
        print(run("playwright-cli", f"-s={SESSION}", "detach")[1])
        print("Ahora desmarque 'Allow remote debugging' en chrome://inspect/#remote-debugging")
        return 0
    if not step(shutil.which("node") is not None, "Node.js", "instale Node 20 o superior (https://nodejs.org)"):
        return 1
    if shutil.which("playwright-cli") is None:
        print("instalando @playwright/cli ...")
        run("npm", "install", "-g", "@playwright/cli@latest")
    if not step(shutil.which("playwright-cli") is not None, "playwright-cli", "npm install -g @playwright/cli@latest"):
        return 1
    if a.mcp and shutil.which("claude"):
        for name, pkg in (("playwright", ["@playwright/mcp@latest", "--browser", "chrome"]), ("chrome-devtools", ["chrome-devtools-mcp@latest", "--autoConnect"])):
            cmd = ["claude", "mcp", "add", "--scope", "user", name, "--"] + (["cmd", "/c"] if os.name == "nt" else []) + ["npx", "-y", *pkg]
            rc, out = run(*cmd)
            print(f"mcp {name}: " + (out.splitlines()[0] if out else "registrado"))
    active = os.path.isfile(os.path.join(USER_DATA, "DevToolsActivePort"))
    if not step(active, "Chrome con depuracion remota activa",
                "en Chrome abra chrome://inspect/#remote-debugging y marque 'Allow remote debugging for this browser instance'; "
                "si Chrome pide confirmar la conexion, acepte; luego repita este script"):
        return 1
    rc, out = run("playwright-cli", "attach", "--cdp=chrome")
    if not step(rc == 0 or "attached" in out, f"sesion '{SESSION}' conectada", out[:300]):
        return 1
    rc, out = run("playwright-cli", f"-s={SESSION}", "tab-list")
    tabs = [ln for ln in out.splitlines() if ln.startswith("- ")]
    print(f"      {len(tabs)} pestanas abiertas")
    qlik = any("qlikcloud.com" in t for t in tabs)
    step(qlik, "pestana de Qlik Cloud abierta (los comandos `dfemu flow` hacen fetch desde ella)", "abra su tenant de Qlik Cloud en Chrome e inicie sesion")
    print("\nListo. Pruebe: python -m emulator.cli flow ls")
    return 0


if __name__ == "__main__":
    sys.exit(main())
