import os
import sys

import duckdb
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from emulator import dfw, runner  # noqa: E402
import make_examples  # noqa: E402

DATA = os.path.join(ROOT, "data", "practica")
TX = os.path.join(DATA, "transacciones.csv")
pytestmark = pytest.mark.skipif(not os.path.exists(TX), reason="faltan los CSV de practica en data/practica")


def sql(q):
    return duckdb.connect().execute(q).fetchall()


def test_s01_bd_origen_a_s3_local(tmp_path):
    db = str(tmp_path / "origen.duckdb")
    c = duckdb.connect(db)
    c.execute(f"CREATE TABLE transacciones AS SELECT * FROM read_csv('{TX}', header=true)")
    c.close()
    out = runner.run(make_examples.s01_db_a_s3().dump(), DATA, str(tmp_path / "out"), {"PG_Origen": {"type": "duckdb", "path": db}})
    ok, bad = out
    exp = sql(f"SELECT canal, ciudad, sum(abs(monto)), count(transaccion_id) FROM read_csv('{TX}') WHERE estado='APROBADA' AND monto IS NOT NULL GROUP BY 1,2 ORDER BY 1,2")
    got = sql(f"SELECT canal, ciudad, total, n FROM read_parquet('{ok['dest']}') ORDER BY 1,2")
    assert len(got) == len(exp) and all(abs(g[2] - e[2]) < 1e-6 and g[3] == e[3] for g, e in zip(got, exp))
    rej = sql(f"SELECT count(*) FROM read_csv('{TX}') WHERE NOT coalesce(estado='APROBADA' AND monto IS NOT NULL, false)")[0][0]
    assert bad["rows"] == rej and bad["dest"].endswith(".csv")


def test_s02_estrella(tmp_path):
    (t,) = runner.run(make_examples.s02_estrella_ventas().dump(), DATA, str(tmp_path))
    assert t["rows"] > 0
    assert sql(f"SELECT count(*) FROM read_parquet('{t['dest']}') WHERE rank_mes = 1")[0][0] > 0


def test_s04_subflow_renombra(tmp_path):
    (t,) = runner.run(make_examples.s04_subflow().dump(), DATA, str(tmp_path))
    cols = [r[0] for r in sql(f"DESCRIBE SELECT * FROM read_csv('{t['dest']}')")]
    assert "id_cuenta" in cols and "cuenta_id" not in cols


def test_s03_script_no_soportado(tmp_path):
    with pytest.raises(runner.Unsupported):
        runner.run(make_examples.s03_fork_union_script().dump(), DATA, str(tmp_path))


def test_xlsx_target_not_executable(tmp_path):
    if not os.path.exists(os.path.join(DATA, "clientes.csv")):
        pytest.skip("faltan clientes.csv en data/practica")
    d = dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))
    tgt = next(n for n in d["dataflow"]["graph"]["nodes"] if n["type"] == "target")
    tgt["component"]["properties"]["configuration"]["settings"]["format"] = "xlsx"
    with pytest.raises(runner.Unsupported, match="xlsx"):
        runner.run(d, DATA, str(tmp_path))


def test_lee_csv_recortando_espacios(tmp_path):  # Qlik recorta los textos al leer un CSV
    d = dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))
    data = tmp_path / "data"
    data.mkdir()
    filas = (
        "cliente_id,cedula,nombre,apellido,fecha_nacimiento,ciudad,provincia,region,email,telefono,segmento,fecha_registro\n"
        "1,1700000001,ana,perez,1990-01-01, Cuenca ,Azuay,Sierra,ana@correo.ec,0970000001,BASICO,2020-01-01\n"
        "2,1700000002,luis,paz,1991-01-01,Cuenca,Azuay,Sierra,luis@correo.ec,0970000002,BASICO,2020-01-01\n"
    )
    (data / "clientes.csv").write_text(filas, encoding="utf-8")
    (t,) = runner.run(d, str(data), str(tmp_path / "out"))
    got = sql(f"SELECT DISTINCT ciudad FROM read_csv('{t['dest']}')")
    assert got == [("Cuenca",)]


def test_conexion_sin_configurar(tmp_path):
    with pytest.raises(runner.Unsupported):
        runner.run(make_examples.s01_db_a_s3().dump(), DATA, str(tmp_path), {})


def test_zzz_target_not_executable(tmp_path):
    if not os.path.exists(os.path.join(DATA, "clientes.csv")):
        pytest.skip("faltan clientes.csv en data/practica")
    d = dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw"))
    tgt = next(n for n in d["dataflow"]["graph"]["nodes"] if n["type"] == "target")
    tgt["component"]["properties"]["configuration"]["settings"]["format"] = "zzz"
    with pytest.raises(runner.Unsupported, match="zzz"):
        runner.run(d, DATA, str(tmp_path))


def _typed(cfg, sql="SELECT ' abc ' AS x"):
    ctx = runner.Ctx(".", ".")
    out = runner._typed(ctx, "strings", cfg, ctx.view(sql))["DEFAULT"]
    return ctx.con.execute(f"SELECT * FROM {out}").fetchall()


def test_strings_uppercase():
    cfg = {"type": "UPPERCASE", "uppercaseConfiguration": {
        "columnsToProcess": ["x"], "newColumnName": "", "shouldCreateNewColumn": False}}
    assert _typed(cfg) == [(" ABC ",)]


def test_strings_replace_starts_with():
    cfg = {"type": "REPLACE_ON_VALUE", "replaceOnValueConfiguration": {
        "cellValue": {"operator": "STARTS_WITH", "value": "593"},
        "columnsToProcess": ["x"], "newColumnName": "",
        "replaceMethod": "REPLACE_MATCHING_WITH_VALUE", "replaceValue": "0",
        "shouldCreateNewColumn": False}}
    assert _typed(cfg, "SELECT '593123' AS x") == [("0123",)]


def test_strings_replace_cell_equals():
    cfg = {"type": "REPLACE_ON_VALUE", "replaceOnValueConfiguration": {
        "cellValue": {"operator": "EQUALS", "value": " "},
        "columnsToProcess": ["x"], "newColumnName": "",
        "replaceMethod": "REPLACE_CELL_WITH_VALUE", "replaceValue": "",
        "shouldCreateNewColumn": False}}
    assert _typed(cfg, "SELECT ' ' AS x") == [("",)]
