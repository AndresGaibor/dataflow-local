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
    assert "SELECT DISTINCT \"cliente_id\" AS \"id_cliente\"" in sql
    assert f"read_csv('{tmp_path / 'clientes.csv'}', header=true)" in sql
    assert "WHERE \"ciudad\" = 'Quito' OR \"ciudad\" = 'Guayaquil'" in sql


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


# --- cadena de tablas, joins, expresiones y agregaciones -------------------

def _csv(tmp_path, name, text):
    (tmp_path / name).write_text(text, encoding="utf-8")


def _go(tmp_path, text):
    sql, reasons = script.translate(text, str(tmp_path))
    assert reasons == [], reasons
    return script.run(sql)


def test_translate_resident_chain(tmp_path):
    _csv(tmp_path, "v.csv", "x,z,c\n1,a,Q\n2,b,L\n3,c,Q\n")
    rows, cols = _go(tmp_path, """
[Unir 1]:
NOCONCATENATE
LOAD [x], [z], [c]
FROM [lib://c:DataFiles/v.csv] (txt, utf8, embedded labels, delimiter is ',', msq)
WHERE [c] = 'Q';

[Cadenas 1]:
NOCONCATENATE
LOAD [x] AS [y], [z]
RESIDENT [Unir 1];
DROP TABLE [Unir 1];

STORE [Cadenas 1] INTO [lib://DataFiles/o.csv] (txt);
DROP TABLE [Cadenas 1];
""")
    assert cols == ["y", "z"] and sorted(rows) == [(1, "a"), (3, "c")]


def test_translate_unknown_resident_is_reported(tmp_path):
    sql, reasons = script.translate("[B]:\nLOAD [x] RESIDENT [Nope];", str(tmp_path))
    assert sql is None and any("Nope" in r for r in reasons)


JOIN_SCRIPT = """
[Unir 1]:
NOCONCATENATE
LOAD [id], [v] FROM [lib://c:DataFiles/a.csv] (txt);

{kind} JOIN([Unir 1])
\t// [b]:
\tLOAD [id], [w] FROM [lib://c:DataFiles/b.csv] (txt);
"""


@pytest.mark.parametrize("kind,expected", [
    ("LEFT", [(1, "a", "x"), (2, "b", None)]),
    ("INNER", [(1, "a", "x")]),
    ("OUTER", [(1, "a", "x"), (2, "b", None), (3, None, "z")]),
])
def test_translate_joins(tmp_path, kind, expected):
    _csv(tmp_path, "a.csv", "id,v\n1,a\n2,b\n")
    _csv(tmp_path, "b.csv", "id,w\n1,x\n3,z\n")
    rows, cols = _go(tmp_path, JOIN_SCRIPT.format(kind=kind))
    assert cols == ["id", "v", "w"] and sorted(rows, key=str) == sorted(expected, key=str)


def test_translate_join_without_common_fields_is_reported(tmp_path):
    _csv(tmp_path, "a.csv", "id,v\n1,a\n")
    _csv(tmp_path, "b.csv", "k,w\n1,x\n")
    sql, reasons = script.translate(JOIN_SCRIPT.format(kind="LEFT").replace("[id], [w]", "[k], [w]"), str(tmp_path))
    assert sql is None and any("sin campos en comun" in r for r in reasons)


@pytest.mark.parametrize("expr,expected", [
    ("Upper([t])", "ABC"),
    ("Trim([t])", "abc"),
    ("Year([d])", 2024),
    ("Month([d])", 3),
    ("IsNull([n])", True),
    ("Coalesce([n], 'z')", "z"),
    ("If([k] > 1, 'big', 'small')", "big"),
])
def test_translate_expressions(tmp_path, expr, expected):
    _csv(tmp_path, "e.csv", "t,d,n,k\nabc,2024-03-05,,2\n")
    rows, _ = _go(tmp_path, f"LOAD {expr} AS [r] FROM [lib://c/e.csv] (txt);")
    assert rows == [(expected,)]


def test_translate_group_by_aggregates(tmp_path):
    _csv(tmp_path, "g.csv", "k,a,b\nA,1,x\nA,2,x\nB,5,y\n")
    rows, cols = _go(tmp_path, """
[T]:
LOAD [k], [a], [b] FROM [lib://c/g.csv] (txt);
[R]:
LOAD [k], Sum([a]) AS [total], Avg([a]) AS [media], Count(DISTINCT [b]) AS [n]
RESIDENT [T]
GROUP BY [k];
DROP TABLE [T];
""")
    assert cols == ["k", "total", "media", "n"]
    assert sorted(rows) == [("A", 3, 1.5, 1), ("B", 5, 5.0, 1)]


def test_translate_group_by_with_free_field_is_reported(tmp_path):
    _csv(tmp_path, "g.csv", "k,a,b\nA,1,x\n")
    sql, reasons = script.translate(
        "[T]:\nLOAD [k], [b], Sum([a]) AS [s] FROM [lib://c/g.csv] (txt)\nGROUP BY [k];", str(tmp_path))
    assert sql is None and any("GROUP BY" in r for r in reasons)


# --- comportamiento verificado contra el tenant el 2026-11-23 -----------------

def test_sum_of_nulls_or_text_is_zero_and_avg_of_nulls_is_null(tmp_path):
    _csv(tmp_path, "g.csv", "k,t,n\nA,x,\nA,y,\n")
    rows, cols = _go(tmp_path, """
[R]:
LOAD [k], Sum([n]) AS [s_nul], Sum([t]) AS [s_txt], Avg([n]) AS [a_nul], Count([t]) AS [c_txt]
FROM [lib://c/g.csv] (txt)
GROUP BY [k];
""")
    assert rows == [("A", 0, 0, None, 2)]  # Qlik: Sum sin numeros = 0, Avg sin numeros = nulo, Count cuenta el texto


FIXTURE = os.path.join(ROOT, "tests", "fixtures", "join_agg.qvs")  # script que genero el servidor para fork + join + aggregate


@pytest.mark.skipif(not os.path.exists(os.path.join(ROOT, "data", "practica", "clientes.csv")),
                    reason="faltan los CSV de practica en data/practica")
def test_server_generated_join_aggregate_script():
    data = os.path.join(ROOT, "data", "practica")
    with open(FIXTURE, encoding="utf-8") as fh:
        sql, reasons = script.translate(fh.read(), data)
    assert reasons == []
    rows, cols = script.run(sql)
    assert cols == ["segmento", "n", "suma_ced", "media_ced"]
    expected, _ = script.run(
        f"SELECT trim(segmento), count(*), sum(cedula), avg(cedula) "
        f"FROM read_csv('{data}/clientes.csv', header=true) GROUP BY 1")
    assert sorted(rows) == sorted(expected)


def test_store_stem():
    assert script.store_stem("STORE [T] INTO [lib://x:GDDestino/emu_a.csv] (txt);") == "emu_a"
    assert script.store_stem("LOAD [a] FROM [lib://x/a.csv] (txt);") is None


def test_cli_translate_compare_simulates_without_apply(tmp_path, capsys):
    _csv(tmp_path, "g.csv", "k,v\nA,1\nA,2\n")
    p = tmp_path / "s.qvs"
    p.write_text("[T]:\nLOAD [k], Sum([v]) AS [s] FROM [lib://c/g.csv] (txt) GROUP BY [k];\n"
                 "STORE [T] INTO [lib://c:GDDestino/emu_t.csv] (txt);\n", encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        cli.main(["translate", str(p), "--data", str(tmp_path), "--compare", "--out", str(tmp_path / "o")])
    assert e.value.code == 0
    assert "[simulación]" in capsys.readouterr().out
    assert (tmp_path / "o" / "translated" / "emu_t.csv").exists()


def test_cli_translate_compare_requires_store(tmp_path, capsys):
    _csv(tmp_path, "g.csv", "k\nA\n")
    p = tmp_path / "s.qvs"
    p.write_text("LOAD [k] FROM [lib://c/g.csv] (txt);", encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        cli.main(["translate", str(p), "--data", str(tmp_path), "--compare", "--out", str(tmp_path / "o")])
    assert e.value.code == 1 and "no tiene STORE" in capsys.readouterr().out
