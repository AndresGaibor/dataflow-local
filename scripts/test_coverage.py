"""Cobertura de pruebas de `emulator/`, publicada en el README.

`pytest-cov` escribe `out/coverage.json` (ignorado por git) y este script lo resume en el bloque
`<!-- tests:inicio -->` del README, para que la cifra no se quede vieja ni se escriba a mano.

Uso:
    python scripts/test_coverage.py            # corre las pruebas con cobertura y actualiza el README
    python scripts/test_coverage.py --readme   # solo reescribe el README desde out/coverage.json
    python scripts/test_coverage.py --check    # falla si el README no coincide con out/coverage.json

El CI corre las pruebas con `--cov` y despues `--check`: si alguien cambia el codigo sin regenerar el
bloque, el trabajo falla en vez de publicar una cifra falsa.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "out" / "coverage.json"
INI, FIN = "<!-- tests:inicio -->", "<!-- tests:fin -->"
LOW = 3  # modulos con menos cobertura que se nombran
TOLERANCE = 0.5  # puntos porcentuales entre plataformas (la cifra se publica, no se clava)


def run() -> int:
    """Corre la suite con cobertura y deja el JSON."""
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "-m", "pytest", "-q", "--cov=emulator", f"--cov-report=json:{REPORT}"]
    print(" ".join(cmd))
    return subprocess.call(cmd, cwd=ROOT)


def load() -> dict:
    if not REPORT.exists():
        raise SystemExit(f"falta {REPORT.relative_to(ROOT)}: corre `python scripts/test_coverage.py`")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def table(data: dict) -> str:
    totals = data.get("totals") or {}
    percent = float(totals.get("percent_covered") or 0.0)
    covered, total = int(totals.get("covered_lines") or 0), int(totals.get("num_statements") or 0)
    files = []
    for name, info in (data.get("files") or {}).items():
        pct = float((info.get("summary") or {}).get("percent_covered") or 0.0)
        if (info.get("summary") or {}).get("num_statements"):
            files.append((pct, Path(name).name))
    files.sort()
    lows = ", ".join(f"`{n}` ({p:.1f} %)" for p, n in files[:LOW]) or "—"
    return "\n".join([
        INI,
        "| cobertura de pruebas | valor |",
        "| --- | --- |",
        f"| lineas de `emulator/` | {percent:.1f} % |",
        f"| lineas cubiertas | {covered} de {total} |",
        f"| modulos con menos cobertura | {lows} |",
        FIN,
    ])


def write(data: dict) -> bool:
    """Reescribe el bloque del README. Devuelve True si cambió algo."""
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    block = table(data)
    if INI in text and FIN in text:
        before, rest = text.split(INI, 1)
        _, after = rest.split(FIN, 1)
        new = before + block + after
    else:
        new = text.rstrip("\n") + "\n\n" + block + "\n"
    if new == text:
        return False
    readme.write_text(new, encoding="utf-8", newline="\n")
    return True


def published_percent(text: str) -> float | None:
    """Porcentaje que dice el README, para comparar sin exigir el mismo recuento de lineas."""
    import re

    m = re.search(r"lineas de `emulator/` \|\s*([0-9.]+)\s*%", text)
    return float(m.group(1)) if m else None


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    check = "--check" in argv
    if check or "--readme" in argv:
        data = load()
        if check:
            text = (ROOT / "README.md").read_text(encoding="utf-8")
            # la cifra se publica; otras plataformas pueden diferir en decimas (rutas, os.name...)
            publicado = published_percent(text)
            medido = float((data.get("totals") or {}).get("percent_covered") or 0.0)
            if publicado is None:
                print("el README no tiene el bloque de cobertura: corre `python scripts/test_coverage.py --readme`")
                return 1
            if abs(publicado - medido) > TOLERANCE:
                print(f"README desactualizado: publica {publicado:.1f} % y la suite mide {medido:.1f} % "
                      f"(tolerancia {TOLERANCE}); corre `python scripts/test_coverage.py --readme`")
                return 1
            print(f"README al dia ({publicado:.1f} % publicado, {medido:.1f} % medido)")
            return 0
        print("README actualizado" if write(data) else "README ya estaba al dia")
        return 0
    rc = run()
    if rc:
        return rc
    data = load()
    print(table(data).splitlines()[2])
    write(data)
    print(f"cobertura publicada en README.md ({data['totals']['percent_covered']:.1f} %)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
