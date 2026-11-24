"""Escenario de extremo a extremo: clientes + cuentas -> limpieza -> union -> agregacion -> ranking -> formato -> orden.

Un flujo parecido a uno real, con datos pequenos (clientes 500 filas, cuentas 760). Se ejecuta en el emulador y, con el
mismo grafo, en el tenant (flujo `emu_e2e_ventas`, clon del base al que se le registraron las dos fuentes desde el
editor: por API no se puede, ver 9 ter), y se comparan las huellas.

Requisitos: `out/e2e_clone.json` con {"app", "df"} del clon (lo crea `scripts/e2e_ventas.py --init`) y las fuentes
`clientes` y `cuentas` ya registradas en el flujo.
Uso: python scripts/e2e_ventas.py [--escenario ventas|calidad|normalizacion] [--init] [--local]      (--local: solo emulador, sin tocar el tenant; --sin-ventana: omite el RANK; --sin-formato: omite FORMAT_NUMBER)
"""
import copy
import json
import os
import sys
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from emulator import bridge, compare, oracle, runner  # noqa: E402
from emulator.builder import Flow, agg, flt, join  # noqa: E402
from emulator.remote import BASE_APP_ID, Remote  # noqa: E402

CLIENTES = ["cliente_id", "cedula", "nombre", "apellido", "fecha_nacimiento", "ciudad", "provincia", "region",
            "email", "telefono", "segmento", "fecha_registro"]
CUENTAS = ["cuenta_id", "cliente_id", "tipo_cuenta", "saldo", "estado", "fecha_apertura"]
CLONE = os.path.join(ROOT, "out", "e2e_clone.json")
HEAD = 8


def strings(t, key, col, new=False, name=""):
    return {"type": t, key: {"columnsToProcess": [col], "shouldCreateNewColumn": new, "newColumnName": name}}


def build(window=True, formato=True):
    f = Flow("emu_e2e_ventas")
    cl, ct = f.dataset("clientes", "clientes.csv", CLIENTES), f.dataset("cuentas", "cuentas.csv", CUENTAS)
    # rama clientes: limpiar texto
    trim = f.proc("strings", "Trim ciudad", strings("TRIM", "trimConfiguration", "ciudad"), x=200)
    up = f.proc("strings", "Ciudad en mayusculas", strings("UPPERCASE", "uppercaseConfiguration", "ciudad"), x=320)
    proper = f.proc("strings", "Nombre propio", strings("PROPERCASE", "propercaseConfiguration", "nombre", True, "nombre_limpio"), x=440)
    # rama cuentas: solo activas y saldo redondeado a 1 decimal
    act = f.proc("filter", "Solo activas", flt(("estado", "EQUAL", "ACTIVA")), x=200)
    rnd = f.proc("numbers", "Saldo redondeado", {"type": "ROUND", "roundHalfUpConfiguration": {
        "columnsToProcess": ["saldo"], "shouldCreateNewColumn": True, "newColumnName": "saldo_r", "precision": 1}}, x=320)
    jn = f.proc("join", "Cliente + cuenta", join("INNER_JOIN", ("cliente_id", "cliente_id")), x=620)
    ag = f.proc("aggregate", "Por ciudad y tipo", agg(["ciudad", "tipo_cuenta"], ("SUM", "saldo_r", "total"), ("COUNT", "cuenta_id", "n"),
                                                       ("AVG", "saldo_r", "promedio")), x=760)
    srt = f.proc("sort", "Orden final", {"sortFields": [{"fieldPath": "tipo_cuenta", "sortOrder": "ASCENDING"},
                                                        {"fieldPath": "ciudad", "sortOrder": "ASCENDING"}]}, x=1180)
    tgt = f.target("Destino", "emu_e2e_ventas", x=1320)
    f.chain(cl, trim, up, proper, jn)
    f.chain(ct, act, rnd)
    f.link(rnd, jn)  # entrada LOOKUP del join
    mid = [ag]
    if window:
        win = f.proc("window", "Ranking por tipo", {
            "operationConfiguration": {"operationType": "RANK", "operationFields": [], "outputFieldName": "ranking", "delimiter": ","},
            # se ordena por `n` y no por `total`: RANK sobre un SUM decimal falla al recargar (9 quater)
        "partitionByConfiguration": {"partitionByFieldList": ["tipo_cuenta"]},
            "sortingConfiguration": {"sortBy": "n", "sortOrder": "DESCENDING"},
            "rangeConfiguration": {"windowStartType": "UNLIMITED", "windowEndType": "UNLIMITED", "windowStartValue": 1, "windowEndValue": 1}}, x=900)
        mid.append(win)
    if formato:
        fmt = f.proc("numbers", "Total con formato", {"type": "FORMAT_NUMBER", "formatNumberConfiguration": {
            "columnsToProcess": ["total"], "shouldCreateNewColumn": True, "newColumnName": "total_fmt", "outputFormat": "THOUSAND_WITH_2_DECIMAL",
            "customFormat": "", "decimalSeparator": ".", "thousandSeparator": ","}}, x=1040)
        mid.append(fmt)
    f.chain(jn, *mid, srt, tgt)
    return f


def build_calidad():
    """transacciones_enero -> partes y aritmetica de fechas, CUT -> filtro con REJECT -> dos ramas -> union -> orden."""
    f = Flow("emu_e2e_calidad")
    tx = f.dataset("transacciones_enero", "transacciones_enero.csv", ["transaccion_id", "fecha", "monto"])
    parts = f.proc("date", "Partes de fecha", {"type": "EXTRACT_DATE_PARTS", "extractDateTokensConfiguration": {
        "columnsToProcess": ["fecha"], "shouldCreateNewColumn": True, "newColumnRename": "", "datePattern": "yyyy-MM-dd HH:mm:ss",
        "year": True, "month": True, "day": True}}, x=200)
    mod = f.proc("date", "Vence en 7 dias", {"type": "MODIFY_DATES", "modifyDateConfiguration": {
        "columnsToProcess": ["fecha"], "newColumnRename": "vence", "shouldCreateNewColumn": True, "datePattern": "dd/MM/yyyy",
        "timeUnit": "DAY", "useWith": "VALUE", "column": "", "constantValue": 7}}, x=320)
    iso = f.proc("date", "Vence ISO", {"type": "FORMAT_DATES", "formatDatesConfiguration": {
        "columnsToProcess": ["vence"], "newColumnRename": "vence_iso", "shouldCreateNewColumn": True, "format": "YYYYMMDD_DASH",
        "datePattern": "YYYY-MM-DD hh:mm:ss.fff"}}, x=440)
    cut = f.proc("strings", "Sin prefijo T", {"type": "CUT", "cutConfiguration": {
        "columnsToProcess": ["transaccion_id"], "newColumnName": "id_num", "shouldCreateNewColumn": True,
        "pattern": {"value": "T", "operator": "CONTAINS"}}}, x=560)
    pos = f.proc("filter", "Ingresos", flt(("monto", "GREATER_OR_EQUAL", "0")), x=680)
    rnd = f.proc("numbers", "Ingreso redondeado", {"type": "ROUND", "roundHalfUpConfiguration": {
        "columnsToProcess": ["monto"], "shouldCreateNewColumn": True, "newColumnName": "monto_aj", "precision": 0}}, x=800)
    ab = f.proc("math", "Egreso en positivo", {"type": "ABSOLUTE", "absoluteConfiguration": {
        "columnsToProcess": ["monto"], "shouldCreateNewColumn": True, "newColumnName": "monto_aj"}}, x=800)
    un = f.proc("union", "Unir ramas", {"unionAll": True}, x=940)
    srt = f.proc("sort", "Orden", {"sortFields": [{"fieldPath": "transaccion_id", "sortOrder": "ASCENDING"}]}, x=1060)
    tgt = f.target("Destino", "emu_e2e_calidad", x=1180)
    f.chain(tx, parts, mod, iso, cut, pos, rnd, un)
    f.link(pos, ab, out="REJECT")
    f.link(ab, un)
    f.chain(un, srt, tgt)
    return f


def build_normalizacion():
    """fechas_sucias + numeros_sucios (20 filas cada una, formatos mezclados) -> conversiones -> union por id -> orden."""
    f = Flow("emu_e2e_normalizacion")
    fe = f.dataset("fechas_sucias", "fechas_sucias.csv", ["id", "fecha_raw"])
    nu = f.dataset("numeros_sucios", "numeros_sucios.csv", ["id", "numero_raw"])
    fd = f.proc("date", "Fecha a date", {"type": "CONVERT_TO_DATE", "convertToDateConfiguration": {
        "columnsToProcess": ["fecha_raw"], "datePattern": "YYYY-MM-DD", "format": "auto", "newColumnRename": "fecha_d", "shouldCreateNewColumn": True}}, x=240)
    nn = f.proc("numbers", "Numero a number", {"type": "CONVERT_TO_NUMBER", "convertToNumberConfiguration": {
        "columnsToProcess": ["numero_raw"], "decimalSeparator": ".", "newColumnName": "numero", "shouldCreateNewColumn": True, "thousandSeparator": ","}}, x=240)
    jn = f.proc("join", "Fecha + numero", join("INNER_JOIN", ("id", "id")), x=480)
    srt = f.proc("sort", "Orden", {"sortFields": [{"fieldPath": "id", "sortOrder": "ASCENDING"}]}, x=620)
    tgt = f.target("Destino", "emu_e2e_normalizacion", x=760)
    f.chain(fe, fd, jn)
    f.chain(nu, nn)
    f.link(nn, jn)
    f.chain(jn, srt, tgt)
    return f


def graph_for(flow, entities):
    """grafo del flujo con los entityId de las fuentes registradas en el clon (por etiqueta del nodo)."""
    g = copy.deepcopy(flow.dump()["dataflow"]["graph"])
    for n in g["nodes"]:
        if n["component"]["type"] == "analyticsSource":
            n["component"]["properties"]["dataEntity"]["entityId"] = entities[n["label"]]
    return g


def main(argv):
    name = argv[argv.index("--escenario") + 1] if "--escenario" in argv else "ventas"
    flow = {"calidad": build_calidad, "normalizacion": build_normalizacion}.get(name, lambda: None)() or build(window="--sin-ventana" not in argv, formato="--sin-formato" not in argv)
    clone_file = CLONE if name == "ventas" else os.path.join(ROOT, "out", f"e2e_{name}_clone.json")
    dump = flow.dump()
    data = os.path.join(ROOT, "data", "practica")
    local = compare.local_fingerprints([t["dest"] for t in runner.run(dump, data, os.path.join(ROOT, "out", "e2e"))], head=HEAD)
    print("emulador OK:", {k: v.get("rows") if isinstance(v, dict) else v for k, v in list(local.items())[:3]})
    if "--local" in argv:
        return 0
    b = bridge.Bridge(apply=True)
    r = Remote(b)
    if "--init" in argv:
        base = BASE_APP_ID
        if name == "normalizacion":  # el flujo `normalizacion` del espacio ya tiene registradas estas fuentes; se copia (solo lectura) a un emu_*
            items = b.get("v1/items", {"spaceId": json.load(open(os.path.join(ROOT, "dfemu.local.json")))["DFEMU_SPACE_ID"], "limit": 100})
            base = next(i["resourceId"] for i in (items if isinstance(items, list) else items["data"]) if i.get("name", "").startswith("normaliza"))
        c = r.clone(base, f"emu_e2e_{name}")
        json.dump({"app": c.app_id, "df": c.dataflow_id}, open(clone_file, "w"))
        print("clon creado; registre las fuentes desde el editor y repita sin --init")
        return 0
    ids = json.load(open(clone_file))
    df = r._get(f"v1/dataflows/{ids['df']}")
    ents = {n["label"]: n["component"]["properties"]["dataEntity"]["entityId"] for n in df["graph"]["nodes"] if n["type"] == "source"}
    clone = type("C", (), {"app_id": ids["app"], "dataflow_id": ids["df"], "name": f"emu_e2e_{name}"})()
    res = r.push_graph(clone, graph_for(flow, ents))
    if res.validity.get("status") != "VALID" or not res.script:
        print("SERVIDOR", res.validity.get("status"), json.dumps(res.validity.get("nodesConstraintViolations"))[:600])
        return 1
    remote = oracle.run_script(b, res.script, uuid.uuid4().hex[:8], head=HEAD)
    diffs = compare.compare(local, remote, skip_head=frozenset())
    print("OK: emulador y tenant coinciden" if not diffs else "DIFERENCIAS:\n  " + "\n  ".join(diffs))
    return 1 if diffs else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
