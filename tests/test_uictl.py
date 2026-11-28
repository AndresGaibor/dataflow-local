import json
import shutil
import subprocess

import pytest

from emulator import uictl


@pytest.mark.skipif(shutil.which("node") is None, reason="hace falta node para comprobar la sintaxis del JavaScript")
@pytest.mark.parametrize("action", sorted(uictl._JS))
def test_el_javascript_de_cada_accion_es_valido(action, tmp_path):
    """Un `\\n` mal escapado dentro del JS ya rompio una accion: se comprueba cada una con `node --check`."""
    code = "const f = async page => {" + uictl._PRE.replace("ARGS", json.dumps({})) + uictl._JS[action].replace("A_N", "5") + "\n};"
    f = tmp_path / f"{action}.js"
    f.write_text(code, encoding="utf-8")
    r = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:300]


def test_el_cli_acepta_las_acciones_documentadas(monkeypatch, capsys):
    llamadas = []
    monkeypatch.setattr(uictl, "run_js", lambda action, **a: llamadas.append((action, a)) or "ok")
    for argv in (["rename", "n", "t"], ["move", "n", "5", "-3"], ["fill", "Campo", "x|y"], ["apply"], ["undo"], ["add", "Ordenar", "--on", "abcd1234"], ["dataset", "cuentas.csv"], ["unlink", "a", "b"], ["rm", "n"], ["script"]):
        assert uictl.main(argv) == 0
    assert [a for a, _ in llamadas] == ["rename", "move", "fill", "button", "tool", "add", "dataset", "unlink", "rm", "script"]
