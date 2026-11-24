"""El escenario de extremo a extremo (scripts/e2e_ventas.py) en el emulador, con los datos de practica.
Coincidio con el tenant el 2026-11-24; aqui solo se protege que siga produciendo lo mismo."""
import os
import sys

import duckdb

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, ROOT)
import e2e_ventas  # noqa: E402
from emulator import runner  # noqa: E402


def test_e2e_ventas_runs_and_has_the_columns_measured_in_the_tenant(tmp_path):
    (t,) = runner.run(e2e_ventas.build().dump(), os.path.join(ROOT, "data", "practica"), str(tmp_path))
    cur = duckdb.connect().execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    cols, rows = [d[0] for d in cur.description], cur.fetchall()
    assert cols == ["ciudad", "tipo_cuenta", "total", "n", "promedio", "ranking", "total_fmt"]
    assert len(rows) == 30
    assert rows[0][:2] == ("AMBATO", "AHORROS")
    assert rows[0][2] == "264896.2"  # ROUND([saldo], 0.1) de Qlik divide por el paso (ver test_round_with_a_step...)
    assert rows[0][6] == "264,896.20"
