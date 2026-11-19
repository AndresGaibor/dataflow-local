"""Genera .dfw sinteticos (validos e invalidos) en samples/synthetic/ y samples/invalid/."""
import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator.builder import Flow, agg, calc, flt, join, sel  # noqa: E402

TX = ["transaccion_id", "cuenta_id", "cliente_id", "fecha_ts", "fecha_raw", "tipo", "monto", "monto_texto", "canal", "ciudad", "comercio", "estado"]
CUENTAS = ["cuenta_id", "cliente_id", "tipo_cuenta", "saldo", "estado", "fecha_apertura"]
CLIENTES = ["cliente_id", "cedula", "nombre", "apellido", "fecha_nacimiento", "ciudad", "provincia", "region", "email", "telefono", "segmento", "fecha_registro"]
OUT = {"synthetic": os.path.join(ROOT, "samples", "synthetic"), "invalid": os.path.join(ROOT, "samples", "invalid")}


def s01_db_a_s3():
    """BD Postgres -> filtro (aprobadas / rechazadas) -> agregacion -> S3 parquet + S3 csv de rechazadas."""
    f = Flow("s01_db_a_s3")
    src = f.db("transacciones_pg", "postgres", "PG_Origen", "public.transacciones", TX)
    flt_ = f.proc("filter", "Solo aprobadas", flt(("estado", "EQUAL", "APROBADA"), ("monto", "IS_NOT_NULL", "")), x=300)
    abs_ = f.proc("math", "Monto absoluto", {"type": "ABSOLUTE", "absoluteConfiguration": {"columnsToProcess": ["monto"], "shouldCreateNewColumn": True, "newColumnName": "monto_abs"}}, x=520)
    ag = f.proc("aggregate", "Por canal y ciudad", agg(["canal", "ciudad"], ("SUM", "monto_abs", "total"), ("COUNT", "transaccion_id", "n"), ("AVG", "monto_abs", "ticket")), x=720)
    ok = f.s3("S3 resumen", "bucket-datalake/resumen/canal_ciudad", x=940)
    bad = f.s3("S3 rechazadas", "bucket-datalake/rechazadas/tx", "csv", "txt", x=940)
    f.chain(src, flt_, abs_, ag, ok)
    f.link(flt_, bad, out="REJECT")
    return f


def s02_estrella_ventas():
    """transacciones + cuentas + clientes (dos joins) -> limpieza -> window RANK -> sort -> target."""
    f = Flow("s02_estrella_ventas")
    tx, ct, cl = f.dataset("transacciones", "transacciones.csv", TX), f.dataset("cuentas", "cuentas.csv", CUENTAS), f.dataset("clientes", "clientes.csv", CLIENTES)
    j1 = f.proc("join", "tx + cuentas", join("LEFT_OUTER_JOIN", ("cuenta_id", "cuenta_id")), x=300)
    j2 = f.proc("join", "+ clientes", join("INNER_JOIN", ("cliente_id", "cliente_id")), x=500)
    trim = f.proc("strings", "Trim ciudad", {"type": "TRIM", "trimConfiguration": {"columnsToProcess": ["ciudad"], "shouldCreateNewColumn": False, "newColumnName": ""}}, x=640)
    proper = f.proc("strings", "Proper nombre", {"type": "PROPERCASE", "propercaseConfiguration": {"columnsToProcess": ["nombre"], "shouldCreateNewColumn": True, "newColumnName": "nombre_limpio"}}, x=780)
    num = f.proc("numbers", "monto a numero", {"type": "CONVERT_TO_NUMBER", "convertToNumberConfiguration": {"shouldCreateNewColumn": True, "columnsToProcess": ["monto_texto"], "newColumnName": "monto_num", "decimalSeparator": ".", "thousandSeparator": ","}}, x=920)
    dt = f.proc("date", "Partes de fecha", {"type": "EXTRACT_DATE_PARTS", "extractDateTokensConfiguration": {"columnsToProcess": ["fecha_ts"], "shouldCreateNewColumn": True, "newColumnRename": "", "datePattern": "yyyy-MM-dd HH:mm:ss", "year": True, "month": True, "prefix": ""}}, x=1060)
    ag = f.proc("aggregate", "Por cliente/mes", agg(["cliente_id", "nombre_limpio", "fecha_ts_year", "fecha_ts_month"], ("SUM", "monto_num", "total")), x=1200)
    win = f.proc("window", "Ranking", {"operationConfiguration": {"operationType": "RANK", "operationFields": [], "outputFieldName": "rank_mes", "delimiter": ","},
                 "partitionByConfiguration": {"partitionByFieldList": ["fecha_ts_year", "fecha_ts_month"]}, "sortingConfiguration": {"sortBy": "total", "sortOrder": "DESCENDING"},
                 "rangeConfiguration": {"windowStartType": "UNLIMITED", "windowEndType": "UNLIMITED", "windowStartValue": 1, "windowEndValue": 1}}, x=1340)
    srt = f.proc("sort", "Orden", {"sortFields": [{"fieldPath": "rank_mes", "sortOrder": "ASCENDING"}]}, x=1480)
    tgt = f.s3("S3 ranking", "bucket-datalake/ranking/clientes", x=1620)
    f.link(tx, j1); f.link(ct, j1)
    f.link(j1, j2); f.link(cl, j2)
    f.chain(j2, trim, proper, num, dt, ag, win, srt, tgt)
    return f


def s03_fork_union_script():
    """Fork en 3 ramas por canal -> filtros -> union -> script Qlik (2 salidas) -> 2 targets."""
    return _fork_union("s03_fork_union_script", True)


def s05_fork_union():
    """Igual que s03 pero sin script: ejecutable de punta a punta (agregacion con processors)."""
    return _fork_union("s05_fork_union", False)


def _fork_union(name, with_script):
    f = Flow(name)
    src = f.dataset("transacciones", "transacciones.csv", TX)
    fk = f.proc("fork", "Fork", {}, x=260)
    f.link(src, fk)
    branches = []
    for i, canal in enumerate(("ATM", "WEB", "POS")):
        b = f.proc("filter", f"Canal {canal}", flt(("canal", "EQUAL", canal)), x=480)
        f.link(fk, b, out="DEFAULT" if i == 0 else f"OPTIONAL_{i}")
        branches.append(b)
    un = f.proc("union", "Union canales", {"unionAll": True}, x=700)
    for b in branches:
        f.link(b, un)
    if not with_script:
        ag = f.proc("aggregate", "Resumen", agg(["canal"], ("SUM", "monto", "total"), ("COUNT", "transaccion_id", "n")), x=920)
        t1 = f.target("Destino", "salida/resumen_canal", x=1140)
        f.chain(un, ag, t1)
        return f
    script = ("[Resumen]:\nNoConcatenate\nLOAD\n    canal,\n    Sum(monto) as total,\n    Count(transaccion_id) as n\nResident [Union canales]\nGroup By canal;\n")
    sc = f.proc("script", "Script Qlik", {"script": script, "schemaEntityId": ""}, x=920)
    f.link(un, sc)
    t1, t2 = f.target("Destino 1", "salida/resumen", x=1140), f.target("Destino 2", "salida/detalle", x=1140)
    f.link(sc, t1); f.link(sc, t2, out="OPTIONAL_1")
    return f


def s04_subflow():
    """Flujo con subflow (receta de tabla: renombrado de columnas) en el medio."""
    f = Flow("s04_subflow")
    src = f.dataset("cuentas", "cuentas.csv", CUENTAS)
    sub_id = "sub-" + src["id"][:8]
    sf = Flow("Subflow de " + f.name)
    ls = sf._node("source", "linkedSource", "Linked Dataflow", {"dataEntity": {"entityId": "00000000-0000-0000-0000-000000000001"}, "configuration": {}}, [], ["DEFAULT"], 60)
    rn = sf._node("processor", "edit-column", "RENAME_1", {"configuration": {"type": "RENAME", "renameColumnConfiguration": {"columnsToProcess": ["cuenta_id"], "newColumnName": "id_cuenta"},
                  "filterConfiguration": {"logicalOpType": "ALL", "filters": []}, "$state": "CONFIGURED"}}, ["DEFAULT"], ["DEFAULT"], 300)
    nt = sf._node("target", "noOpTarget", "No operation target", {"configuration": {}}, ["DEFAULT"], [], 540)
    sf.chain(ls, rn, nt)
    d = sf.dump()["dataflow"]
    d["id"] = sub_id
    f.subflows.append({"id": sub_id, "name": d["name"], "description": "", "context": d["context"], "graph": d["graph"]})
    sb = f.proc("subflow", "Receta de tabla 1", {"dataflowId": sub_id}, x=380)
    tgt = f.target("Destino", "salida/cuentas_renombradas", x=700)
    f.chain(src, sb, tgt)
    return f


VALID = [s01_db_a_s3, s02_estrella_ventas, s03_fork_union_script, s04_subflow, s05_fork_union]


def _mutate(fn, mut):
    d = fn().dump()
    mut(d)
    return d


def _nodes(d):
    return d["dataflow"]["graph"]["nodes"]


def _find(d, ctype):
    return next(n for n in _nodes(d) if n["component"]["type"] == ctype)


def _cycle(d):  # ultimo nodo -> primer processor (agrega arista de vuelta)
    ns = [n for n in _nodes(d) if n["type"] == "processor"]
    a, b = ns[-1], ns[0]
    b["handles"]["incoming"].append({"id": "cyc-in", "type": "OPTIONAL"})
    a["handles"]["outgoing"].append({"id": "cyc-out", "type": "OPTIONAL"})
    d["dataflow"]["graph"]["edges"].append({"id": "cyc", "sourceHandle": "cyc-out", "targetHandle": "cyc-in"})


def _drop_edge(d):
    d["dataflow"]["graph"]["edges"].pop(0)


def _bad_join(d):
    _find(d, "join")["component"]["properties"]["configuration"]["joinFunction"] = "CROSS_JOIN"


def _no_target(d):
    d["dataflow"]["graph"]["nodes"] = [n for n in _nodes(d) if n["type"] != "target"]
    d["dataflow"]["graph"]["edges"] = []


def _missing_cfg(d):
    del _find(d, "aggregate")["component"]["properties"]["configuration"]["groupBy"]


def _too_many_script_outs(d):
    sc = _find(d, "script")
    for h in sc["handles"]["outgoing"]:
        if h["type"] == "OPTIONAL_2":
            t = copy.deepcopy(_find(d, "analyticsTarget"))
            t["id"] = "extra-t"
            t["handles"]["incoming"][0]["id"] = "extra-in"
            d["dataflow"]["graph"]["nodes"].append(t)
            d["dataflow"]["graph"]["edges"].append({"id": "extra", "sourceHandle": h["id"], "targetHandle": "extra-in"})


def _target_sin_extension(d):
    _find(d, "analyticsTarget")["component"]["properties"]["configuration"]["settings"]["extension"] = ""


def _bad_subflow_ref(d):
    _find(d, "subflow")["component"]["properties"]["configuration"]["dataflowId"] = "no-existe"


INVALID = {  # nombre -> (flujo base, mutacion, error esperado)
    "i01_ciclo": (s02_estrella_ventas, _cycle, "ciclos"),
    "i02_arista_borrada": (s02_estrella_ventas, _drop_edge, "sin conectar"),
    "i03_join_invalido": (s02_estrella_ventas, _bad_join, "joinFunction"),
    "i04_sin_target": (s01_db_a_s3, _no_target, "sin nodo target"),
    "i05_falta_groupby": (s01_db_a_s3, _missing_cfg, "groupBy"),
    "i07_script_3_salidas": (s03_fork_union_script, _too_many_script_outs, "salidas conectadas"),
    "i08_target_sin_extension": (s01_db_a_s3, _target_sin_extension, "settings.extension vacio"),
    "i09_subflow_inexistente": (s04_subflow, _bad_subflow_ref, "subflow referenciado"),
}


def main():
    import json
    for d in OUT.values():
        os.makedirs(d, exist_ok=True)
    for fn in VALID:
        fn().save(os.path.join(OUT["synthetic"], fn.__name__ + ".dfw"))
    for name, (fn, mut, _) in INVALID.items():
        with open(os.path.join(OUT["invalid"], name + ".dfw"), "w", encoding="utf-8") as fh:
            json.dump(_mutate(fn, mut), fh, ensure_ascii=False)
    print(f"{len(VALID)} validos, {len(INVALID)} invalidos")


if __name__ == "__main__":
    main()
