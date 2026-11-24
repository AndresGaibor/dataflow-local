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


def test_normalizacion_matches_what_the_tenant_wrote(tmp_path):
    # columnas medidas en el tenant el 2026-11-24 (fechas_sucias + numeros_sucios, 20 filas con formatos mezclados)
    (t,) = runner.run(e2e_ventas.build_normalizacion().dump(), os.path.join(ROOT, "data", "practica"), str(tmp_path))
    cur = duckdb.connect().execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    cols, rows = [d[0] for d in cur.description], cur.fetchall()
    col = lambda c: ["" if r[cols.index(c)] is None else r[cols.index(c)] for r in rows]  # noqa: E731
    assert col("fecha_raw") == "2026-09-09|2026-09-09|09-09-2026|2026/09/09|09-SEP-2026|2026-02-28|29/02/2024|29/02/2025|31/04/2026|31/02/2026|2026-13-01|2026-00-10||2026-07-15|15.07.2026|2026-09-09 14:37:24|09/09/2026 14:37|2026-09-09 14:37:24|2026-12-31 23:59:59|01/01/2026 00:00".split("|")
    assert col("fecha_d") == "9/9/2026|9/9/2026||||2/28/2026||||||||7/15/2026||9/9/2026||9/9/2026|12/31/2026|".split("|")
    assert col("numero_raw") == "1200.50|1.200,50|1200.50|150|0|-45.75|99.90|10,5|1 234,56|2.345.678,90|2,345,678.90|$1,234.56|USD 450.00||NaN|1.234|1,234|000123.40|-1.200,00|+250.5".split("|")
    assert col("numero") == "1200.5||1200.5|150|0|-45.75|99.9||||2345678.9|||||1.234|1234|123.4||250.5".split("|")


def test_calidad_matches_what_the_tenant_wrote(tmp_path):
    # medido en el tenant el 2026-11-24: partes de fecha sobre una fecha convertida, +7 dias, ISO, CUT, filtro con REJECT y UNION
    (t,) = runner.run(e2e_ventas.build_calidad().dump(), os.path.join(ROOT, "data", "practica"), str(tmp_path))
    cur = duckdb.connect().execute(f"SELECT * FROM read_csv('{t['dest']}', header=true, all_varchar=true)")
    cols, rows = [d[0] for d in cur.description], cur.fetchall()
    col = lambda c: ["" if r[cols.index(c)] is None else r[cols.index(c)] for r in rows]  # noqa: E731
    assert col("fecha_d_year")[:8] == "2026|2026||||2026||".split("|")
    assert col("fecha_d_day")[:8] == "9|9||||28||".split("|")
    assert col("vence_iso")[:8] == "2026-09-16|2026-09-16||||2026-03-07||".split("|")
    assert col("fecha_cut")[:2] == ["20260909", "09/09/2026"]  # la expresion ve el texto de cada fila; la recarga es la que unifica
    assert col("numero_aj")[:8] == "1201||1201|150|0|46|100|".split("|")  # 45.75 sale 46: el formato de ROUND alcanza a la otra rama del UNION
    assert sum(float(x) for x in col("numero_aj") if x) == 2349986.0
