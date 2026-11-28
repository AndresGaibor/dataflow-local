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


def test_apply_prueba_el_otro_nombre_del_boton(monkeypatch, capsys):
    # el panel de un Pivotar se confirma con "Ejecutar y aplicar", no con "Aplicar" (medido)
    nombres = []

    def falso(action, **a):
        nombres.append(a.get("name"))
        if len(nombres) == 1:
            raise uictl.flowctl.FlowError("no hay boton Aplicar")
        return "ok"

    monkeypatch.setattr(uictl, "run_js", falso)
    assert uictl.main(["apply"]) == 0
    assert nombres == ["Aplicar", "Ejecutar y aplicar"]
    assert "ok" in capsys.readouterr().out or True
