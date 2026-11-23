"""Oráculo de ejecución: pruebas con FakeRunner, sin tocar el tenant."""
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator.bridge import Bridge, BridgeError, DryRun  # noqa: E402
from emulator.oracle import OracleError, assert_safe, parse_tables, retarget, run_script  # noqa: E402
from emulator.remote import Remote  # noqa: E402
from fakes import FakeRunner  # noqa: E402

SB = "000000000000000000000000"
APP = "app-e1"
TAG = "t1"
FILE = "emu_t1_1.csv"
READ_FILE = "lib://Entrenamiento Dataflow:DataFiles/emu_t1_1.csv"
CANCEL = ("POST", "v1/reloads/rel-1/actions/cancel")
DELETE_APP = ("DELETE", f"v1/apps/{APP}")
DELETE_FILES = ("POST", "v1/data-files/actions/delete")

FUNDAMENTOS = "\r\n".join([
    "///$tab Main",
    "SET ThousandSep=',';",
    "SET DecimalSep='.';",
    "SET MoneyThousandSep=',';",
    "SET MoneyDecimalSep='.';",
    "SET MoneyFormat='$ ###0.00;-$ ###0.00';",
    "SET TimeFormat='h:mm:ss TT';",
    "SET DateFormat='M/D/YYYY';",
    "SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';",
    "SET FirstWeekDay=6;",
    "SET BrokenWeeks=1;",
    "SET ReferenceDay=0;",
    "SET FirstMonthOfYear=1;",
    "SET CollationLocale='en-US';",
    "SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';",
    "SET LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December';",
    "SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';",
    "SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';",
    "SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';",
    "",
    "///$tab Generated",
    "// [clientes]",
    "[Seleccionar campos 1]:",
    "NOCONCATENATE",
    "LOAD DISTINCT",
    "\t[cliente_id] AS [id_cliente],",
    "\t[segmento],",
    "\t[nombre],",
    "\t[apellido],",
    "\t[ciudad],",
    "\t[fecha_nacimiento],",
    "\t[fecha_registro]",
    "FROM [lib://Entrenamiento Dataflow:DataFiles/clientes.csv] (txt, utf8, embedded labels, delimiter is ',', msq);",
    "",
    "STORE [Seleccionar campos 1] INTO [lib://Entrenamiento Dataflow:GDDestino/carpeta-demo/clientes.csv] (txt);",
    "",
    "DROP TABLE [Seleccionar campos 1];",
    "",
    "",
])

GDDEST = "lib://Entrenamiento Dataflow:GDDestino/a/x.csv"

TABLES = ("NAME          ROW COUNT     RAM     FIELDS\n"
          "emu_out_1     3             16      emu_out_1.id, emu_out_1.valor\n"
          "Total RAM     -             175     -")
CELL_NAN = {"qText": "NaN", "qNum": "NaN", "qState": "L"}
CELL_3 = {"qText": "3", "qNum": 3, "qState": "L"}
# una fila con seis celdas: Count, Count(distinct), Sum por cada campo
EVALS = [{"qMatrix": [[CELL_3, CELL_3, CELL_NAN, CELL_3, CELL_3, CELL_NAN]]}]


def routes(validate=None, reload_state=None):
    state = {"appId": APP, "status": "SUCCEEDED", "log": ""}
    state.update(reload_state or {})
    return {
        ("POST", "v1/apps"): {"attributes": {"id": APP, "name": f"emu_oracle_{TAG}", "spaceId": SB}},
        ("CLI", "app script set"): "",
        ("POST", "v1/apps/validatescript"): validate or {"Errors": [], "Warnings": []},
        ("POST", "v1/reloads"): {"id": "rel-1"},
        ("GET", "v1/reloads/rel-1"): state,
        ("POST", "v1/reloads/rel-1/actions/cancel"): {},
        ("CLI", "app tables"): TABLES,
        ("CLI", "app eval"): EVALS,
        ("GET", f"v1/apps/{APP}"): {"attributes": {"name": f"emu_oracle_{TAG}", "spaceId": SB}},
        ("DELETE", f"v1/apps/{APP}"): {},
        ("GET", "v1/data-connections"): [{"qName": "GDDestino", "id": "conn-2"},
                                         {"qName": "DataFiles", "id": "conn-1"}],
        ("GET", "v1/data-files"): [{"id": "f1", "name": FILE}, {"id": "f2", "name": "emu_t1_12.csv"}],
        ("GET", "v1/data-files/f1"): {"id": "f1", "name": FILE, "spaceId": SB},
        ("POST", "v1/data-files/actions/delete"): {},
    }


class CaptureRunner(FakeRunner):
    """Además guarda los argumentos de los comandos CLI (app eval, app tables, ...)."""

    def __init__(self, rt):
        super().__init__(rt)
        self.cli = []

    def __call__(self, args):
        if args[0] != "raw":
            self.cli.append(list(args))
        return super().__call__(args)


def make(tmp_path, rt):
    runner = CaptureRunner(rt)
    return Bridge(runner=runner, apply=True, audit_path=str(tmp_path / "audit.jsonl")), runner


def keys_of(runner):
    return [(c[0], c[1]) for c in runner.calls]


# --- retarget / assert_safe ------------------------------------------------
def test_retarget_rewrites_every_store():
    r = retarget(FUNDAMENTOS, TAG)
    assert "GDDestino" not in r.script
    assert f"STORE [Seleccionar campos 1] INTO [{READ_FILE}] (txt);" in r.script
    assert "QUALIFY *;" in r.script
    assert "[emu_out_1]:" in r.script
    assert (f"LOAD * FROM [{READ_FILE}] "
            "(txt, utf8, embedded labels, delimiter is ',', msq);") in r.script
    assert r.files == {"clientes": FILE}
    assert r.tables == {"clientes": "emu_out_1"}


def test_assert_safe_rejects_original_store():
    with pytest.raises(OracleError):
        assert_safe(FUNDAMENTOS)


def test_assert_safe_accepts_retargeted():
    assert_safe(retarget(FUNDAMENTOS, TAG).script)


def test_retarget_unknown_store_raises():
    with pytest.raises(OracleError):
        retarget("STORE a, b FROM t INTO [lib://Entrenamiento Dataflow:DataFiles/x.csv];", TAG)


EXPLOIT_SINGLE = "\r\n".join([
    "STORE a INTO [lib://Entrenamiento Dataflow:DataFiles/ok.csv] (txt);",
    "SET a='x",
    f"y'; STORE t INTO [{GDDEST}] (txt); SET b='z",
    "w';",
])
EXPLOIT_DOUBLE = EXPLOIT_SINGLE.replace("'", '"')
BYPASS = [
    ("a_if_then", f"IF 1=1 THEN STORE t INTO [{GDDEST}] (txt); END IF"),
    ("b_when", f"WHEN 1 STORE t INTO [{GDDEST}] (txt);"),
    ("c_rem_quote", f"REM it's a note; STORE t INTO [{GDDEST}] (txt); SET x='a';"),
    ("d_unbracketed_lib", f"LOAD * FROM lib://A/f.csv (txt);\r\nSTORE [t] INTO [{GDDEST}] (txt);"),
    ("e_bom", f"﻿STORE t INTO [{GDDEST}] (txt);"),
    ("ordinary_then_hidden", f"STORE t INTO [lib://Entrenamiento Dataflow:DataFiles/ok.csv] (txt);\r\n"
                             f"IF 1=1 THEN STORE u INTO [{GDDEST}] (txt); END IF"),
    ("exploit_single_quote", EXPLOIT_SINGLE),
    ("exploit_double_quote", EXPLOIT_DOUBLE),
]


@pytest.mark.parametrize("name, script", BYPASS, ids=[b[0] for b in BYPASS])
def test_bypass_shapes_are_rewritten_and_raw_is_rejected(name, script):
    r = retarget(script, TAG)
    assert "GDDestino" not in r.script
    assert_safe(r.script)
    with pytest.raises(OracleError):
        assert_safe(script)


@pytest.mark.parametrize("script", [
    "// store sales\r\nSTORE [t] INTO [" + GDDEST + "] (txt);",
    "/* STORE later */\r\nSTORE [t] INTO [" + GDDEST + "] (txt);",
    "LOAD [Store] AS x FROM [lib://Entrenamiento Dataflow:DataFiles/clientes.csv] (txt);\r\n"
    "STORE [t] INTO [" + GDDEST + "] (txt);",
    "LET y=Store;\r\nSTORE [t] INTO [" + GDDEST + "] (txt);",
    "LOAD * FROM [lib://Entrenamiento Dataflow:DataFiles/store.csv] (txt);\r\n"
    "STORE [t] INTO [" + GDDEST + "] (txt);",
    "STORE a, b FROM t INTO [x];",
], ids=["line_comment", "block_comment_word", "bracket_field", "let_field", "path_store_csv", "unparseable"])
def test_store_word_in_unrecognized_context_raises(script):
    with pytest.raises(OracleError):
        retarget(script, TAG)


def test_block_comment_with_full_statement_is_rewritten_not_hidden():
    script = ("/* STORE x INTO [lib://Entrenamiento Dataflow:GDDestino/z/x.csv] (txt); */\r\n"
              "STORE [t] INTO [lib://Entrenamiento Dataflow:GDDestino/a/y.csv] (txt);")
    r = retarget(script, TAG)
    assert "GDDestino" not in r.script
    assert_safe(r.script)


def test_apostrophe_in_comment_is_fine():
    script = "// cliente's datos\r\nSTORE [t] INTO [" + GDDEST + "] (txt);"
    r = retarget(script, TAG)
    assert r.files == {"x": FILE}
    assert "GDDestino" not in r.script


def test_still_working_shapes():
    script = "\r\n".join([
        "LOAD * FROM lib://A/f.csv (txt);",
        "store [t] into [" + GDDEST + "] (txt);",
        "STORE\t[u]\tINTO\t[lib://Entrenamiento Dataflow:GDDestino/a/y.csv]\t(txt);",
    ])
    r = retarget(script, TAG)
    assert "lib://A/f.csv (txt);" in r.script
    assert "GDDestino" not in r.script
    assert set(r.files) == {"x", "y"}
    assert_safe(r.script)


def test_unbracketed_lib_path_is_not_a_comment():
    # `lib://` no es comentario: el STORE ordinario tras el LOAD se reescribe, no se oculta
    script = f"LOAD * FROM lib://A/f.csv (txt);\r\nSTORE [t] INTO [{GDDEST}] (txt);"
    r = retarget(script, TAG)
    assert "lib://A/f.csv (txt);" in r.script
    assert "GDDestino" not in r.script
    with pytest.raises(OracleError):  # el original, sin reescribir, sigue siendo inseguro
        assert_safe(script)


def test_leading_bom_store_is_retargeted_not_hidden():
    script = f"﻿STORE t INTO [{GDDEST}] (txt);"
    r = retarget(script, TAG)
    assert "GDDestino" not in r.script
    assert_safe(r.script)
    with pytest.raises(OracleError):
        assert_safe(script)


def test_assert_safe_rejects_non_emu_datafiles_target():
    script = "STORE t INTO [lib://Entrenamiento Dataflow:DataFiles/clientes.csv] (txt);"
    with pytest.raises(OracleError):
        assert_safe(script)


def test_retarget_keeps_non_ascii():
    r = retarget(FUNDAMENTOS, TAG)
    assert "SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;" in r.script


def test_retarget_without_store_raises():
    with pytest.raises(OracleError, match="ninguna tabla"):
        retarget("LOAD 1 AS a;", TAG)


def test_retarget_duplicate_stem_raises():
    line = "STORE [t] INTO [lib://Entrenamiento Dataflow:GDDestino/a/clientes.csv] (txt);"
    with pytest.raises(OracleError):
        retarget(line + "\r\n" + line.replace("/a/", "/b/"), TAG)


def test_retarget_rejects_bad_tag():
    with pytest.raises(OracleError):
        retarget(FUNDAMENTOS, "x]y")


# --- parse_tables ----------------------------------------------------------
def test_parse_tables_sample():
    text = ("NAME          ROW COUNT     RAM     FIELDS\n"
            "Salida        3             16      id, valor\n"
            "Total RAM     -             175     -")
    assert parse_tables(text) == {"Salida": (3, ["id", "valor"])}


# --- run_script ------------------------------------------------------------
def test_run_script_fingerprint_batched_and_wired(tmp_path):
    b, runner = make(tmp_path, routes())
    fp = run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert fp == {"clientes": {"rows": 3, "columns": {
        "id": {"count": 3, "distinct": 3, "sum": None},
        "valor": {"count": 3, "distinct": 3, "sum": None},
    }}}
    # una sola llamada app eval por tabla, con los campos calificados
    evals = [a for a in runner.cli if a[:2] == ["app", "eval"]]
    assert len(evals) == 1
    assert "Count([emu_out_1.id])" in evals[0]
    assert "Count(distinct [emu_out_1.valor])" in evals[0]
    # el script que llega a la CLI y a validatescript apunta a DataFiles/emu_*
    sent = [c[2] for c in runner.calls if c[:2] == ("POST", "v1/apps/validatescript")][0]["script"]
    set_body = [c[2] for c in runner.calls if c[:2] == ("CLI", "app script set")][0]
    for script in (sent, set_body):
        assert "GDDestino" not in script
        assert f"DataFiles/{FILE}" in script
    assert DELETE_APP in keys_of(runner)
    assert DELETE_FILES in keys_of(runner)


def test_run_script_cleans_up_when_reload_fails(tmp_path):
    b, runner = make(tmp_path, routes(reload_state={"status": "FAILED", "log": "x" * 600 + "ERR FINAL"}))
    with pytest.raises(OracleError, match="ERR FINAL"):
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert DELETE_APP in keys_of(runner)
    assert DELETE_FILES in keys_of(runner)
    assert CANCEL not in keys_of(runner)  # FAILED ya es terminal: no hay nada que cancelar


def test_run_script_timeout_cancels_before_deleting_app(tmp_path):
    b, runner = make(tmp_path, routes(reload_state={"status": "RELOADING", "log": "aun"}))
    with pytest.raises(OracleError, match="timeout"):
        run_script(b, FUNDAMENTOS, TAG, timeout=0, poll_seconds=0)
    keys = keys_of(runner)
    assert CANCEL in keys
    assert keys.index(CANCEL) < keys.index(DELETE_APP)


def test_run_script_rejects_validatescript_errors(tmp_path):
    val = {"Errors": [{"Msg": "Syntax error", "Line": 4, "Column": 2}], "Warnings": []}
    b, runner = make(tmp_path, routes(validate=val))
    with pytest.raises(OracleError, match="Syntax error") as e:
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert "4" in str(e.value)
    assert ("POST", "v1/reloads") not in keys_of(runner)
    assert DELETE_APP in keys_of(runner)


def test_script_set_failure_cleans_app_and_surfaces_original_error(tmp_path):
    rt = routes()
    rt[("CLI", "app script set")] = (1, "", "boom-set")
    b, runner = make(tmp_path, rt)
    with pytest.raises(BridgeError, match="boom-set"):
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert DELETE_APP in keys_of(runner)
    assert DELETE_FILES not in keys_of(runner)  # la recarga nunca se inició


def test_fingerprint_failure_still_cleans_up(tmp_path):
    rt = routes()
    rt[("CLI", "app tables")] = (1, "", "boom-tables")
    b, runner = make(tmp_path, rt)
    with pytest.raises(BridgeError, match="boom-tables"):
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert DELETE_APP in keys_of(runner)
    assert DELETE_FILES in keys_of(runner)


def test_cleanup_error_does_not_mask_original(tmp_path, capsys):
    rt = routes(reload_state={"status": "FAILED", "log": "LOG-X"})
    rt[("DELETE", f"v1/apps/{APP}")] = (1, "", "no borra")
    b, _ = make(tmp_path, rt)
    with pytest.raises(OracleError, match="LOG-X"):
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert "aviso" in capsys.readouterr().err


def test_dry_run_first_write_does_no_cleanup_traffic(tmp_path):
    runner = CaptureRunner(routes())
    b = Bridge(runner=runner, apply=False, audit_path=str(tmp_path / "audit.jsonl"))
    with pytest.raises(DryRun):
        run_script(b, FUNDAMENTOS, TAG, poll_seconds=0)
    assert runner.calls == []


# --- Remote.discard_files ----------------------------------------------------
def test_discard_files_deletes_only_exact_names(tmp_path):
    b, runner = make(tmp_path, routes())
    Remote(b).discard_files([FILE])
    deletes = [c for c in runner.calls if c[:2] == DELETE_FILES]
    assert deletes[0][2] == {"delete": [{"id": "f1"}]}  # "emu_t1_12.csv" no coincide y no se borra


def test_discard_files_without_names_does_nothing(tmp_path):
    b, runner = make(tmp_path, routes())
    Remote(b).discard_files([])
    assert runner.calls == []


# --- primeras filas ---------------------------------------------------------------------------------------

def test_retarget_rowno_adds_the_row_number_to_the_readback():
    script = f"[t]:\r\nLOAD * FROM [lib://c/a.csv] (txt);\r\nSTORE [t] INTO [{GDDEST}] (txt);"
    assert "RecNo() AS [__rowno]" not in retarget(script, TAG).script  # por omision, como siempre
    assert f"LOAD *, RecNo() AS [__rowno] FROM [{READ_FILE}]" in retarget(script, TAG, rowno=True).script


class FakeEval:
    """Bridge falso para _fingerprints: `app tables` y `app eval` (medidas y primeras filas)."""

    def __init__(self):
        self.evals = []

    def cli_read(self, args):
        if args[:2] == ["app", "tables"]:
            return ("Name  Rows  Size  Fields\n"
                    "emu_out_1  2  1  emu_out_1.id, emu_out_1.nombre, emu_out_1.__rowno\n")
        exprs = args[args.index("--app") + 2:args.index("--json")]
        self.evals.append(exprs)
        cell = lambda e: ({"qNum": "2", "qText": "2"} if e.startswith("Count") else {"qNum": "NaN", "qText": "1|2"} if e.startswith("Concat") else {"qNum": "3", "qText": "3"})
        return json.dumps([{"qMatrix": [[cell(e) for e in exprs]]}])


def test_fingerprints_skip_the_rowno_column_and_add_heads_only_when_asked():
    from emulator.oracle import Retargeted, _fingerprints
    rt = Retargeted("", {"salida": "f.csv"}, {"salida": "emu_out_1"})
    plain = _fingerprints(FakeEval(), "app", rt)
    assert sorted(plain["salida"]["columns"]) == ["id", "nombre"] and "head" not in plain["salida"]["columns"]["id"]
    b = FakeEval()
    with_head = _fingerprints(b, "app", rt, head=5)
    assert with_head["salida"]["columns"]["id"]["head"] == "1|2" and "__rowno" not in with_head["salida"]["columns"]
    heads = [e for ex in b.evals for e in ex if e.startswith("Concat")]
    assert heads == ["Concat(If([emu_out_1.__rowno] <= 5, Text([emu_out_1.id])), '|', [emu_out_1.__rowno])",
                     "Concat(If([emu_out_1.__rowno] <= 5, Text([emu_out_1.nombre])), '|', [emu_out_1.__rowno])"]
