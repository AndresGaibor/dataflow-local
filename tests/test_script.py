"""Traductor de Qlik script: subconjunto de Data Flow y marcas de no traducible."""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import cli, script  # noqa: E402

SCRIPT = """///$tab Main
SET ThousandSep=',';
SET DecimalSep='.';
///$tab Generated
// [clientes]
[Seleccionar campos 1]:
NOCONCATENATE
LOAD DISTINCT
\t[cliente_id] AS [id_cliente],
\t[segmento],
\t[ciudad]
FROM [lib://Entrenamiento Dataflow:DataFiles/clientes.csv] (txt, utf8, embedded labels, delimiter is ',', msq)
WHERE [ciudad] = 'Quito' OR [ciudad] = 'Guayaquil';

STORE [Seleccionar campos 1] INTO [lib://Entrenamiento Dataflow:GDDestino/clientes.csv] (txt);

DROP TABLE [Seleccionar campos 1];
"""


SCRIPT_FULL = SCRIPT.replace("\t[segmento],\n", "\t[segmento],\n\t[nombre],\n\t[apellido],\n\t[fecha_nacimiento],\n\t[fecha_registro],\n") \
                   .replace("WHERE [ciudad] = 'Quito' OR [ciudad] = 'Guayaquil'", "")


def test_split_statements_respects_commas_in_options():
    sts = script.split_statements(SCRIPT)
    assert len(sts) == 5  # 2 SET, LOAD, STORE, DROP
    assert "delimiter is ','" in sts[2]


def test_translate_load_from_csv_with_where(tmp_path):
    (tmp_path / "clientes.csv").write_text(
        "cliente_id,segmento,ciudad\n1,A,Quito\n", encoding="utf-8")
    sql, reasons = script.translate(SCRIPT, str(tmp_path))
    assert reasons == []
    assert sql.startswith("SELECT DISTINCT \"cliente_id\" AS \"id_cliente\"")
    assert f"read_csv('{tmp_path / 'clientes.csv'}', header=true)" in sql
    assert sql.endswith("WHERE \"ciudad\" = 'Quito' OR \"ciudad\" = 'Guayaquil'")


def test_translate_runs_and_filters(tmp_path):
    (tmp_path / "clientes.csv").write_text(
        "cliente_id,segmento,ciudad\n1,A,Quito\n2,B,Loja\n3,C,Guayaquil\n", encoding="utf-8")
    sql, _ = script.translate(SCRIPT, str(tmp_path))
    rows, cols = script.run(sql)
    assert cols == ["id_cliente", "segmento", "ciudad"]
    assert rows == [(1, "A", "Quito"), (3, "C", "Guayaquil")]


@pytest.mark.skipif(not os.path.exists(os.path.join(ROOT, "data", "practica", "clientes.csv")),
                    reason="faltan los CSV de practica en data/practica")
def test_translated_fundamentos_matches_emulator(tmp_path):
    """El script traducido y el grafo emulado dan las mismas huellas."""
    from emulator import compare, dfw, runner
    import duckdb
    data = os.path.join(ROOT, "data", "practica")
    sql, _ = script.translate(SCRIPT_FULL, data)
    local = tmp_path / "local.csv"
    con = duckdb.connect()
    con.execute(f"COPY ({sql}) TO '{local}' (FORMAT csv, HEADER)")
    con.close()
    (emu,) = runner.run(dfw.load(os.path.join(ROOT, "samples", "fundamentos.dfw")), data, str(tmp_path / "out"))
    key = compare.stem_of(emu["dest"])
    assert compare.compare({key: compare.local_fingerprint(str(local))},
                           {key: compare.local_fingerprint(emu["dest"])}) == []


def test_translate_trims_text_like_qlik(tmp_path):
    (tmp_path / "clientes.csv").write_text(
        "cliente_id,segmento,ciudad\n1,A, Quito \n2,B,Loja\n", encoding="utf-8")
    sql, _ = script.translate(SCRIPT, str(tmp_path))
    rows, _ = script.run(sql)
    assert rows == [(1, "A", "Quito")]  # el WHERE iguala tras recortar


def test_translate_rejects_unsupported_statements(tmp_path):
    sql, reasons = script.translate(
        "LOAD [a] FROM [lib://x/tabla.qvd] (qvd);\nJOIN [otra]\nLOAD [b] RESIDENT [x];", str(tmp_path))
    assert sql is None
    assert any("solo .csv" in r for r in reasons)


def test_translate_rejects_expressions(tmp_path):
    sql, reasons = script.translate(
        "LOAD SubField([tel], '-', 1) AS [x] FROM [lib://c/datos.csv] (txt);", str(tmp_path))
    assert sql is None and "campo no soportado" in reasons[0]


def test_cli_translate_run(tmp_path, capsys):
    (tmp_path / "clientes.csv").write_text(
        "cliente_id,segmento,ciudad\n1,A,Quito\n2,B,Loja\n", encoding="utf-8")
    p = tmp_path / "script.qvs"
    p.write_text(SCRIPT, encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        cli.main(["translate", str(p), "--data", str(tmp_path), "--run"])
    assert e.value.code == 0
    out = capsys.readouterr().out
    assert "1 filas, 3 columnas: id_cliente, segmento, ciudad" in out


def test_cli_translate_unsupported_exits_1(tmp_path, capsys):
    p = tmp_path / "script.qvs"
    p.write_text("LOAD [a] FROM [lib://x/tabla.qvd] (qvd);", encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        cli.main(["translate", str(p)])
    assert e.value.code == 1
    assert "no traducible" in capsys.readouterr().out
