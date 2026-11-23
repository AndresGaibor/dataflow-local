import argparse
import collections
import glob
import json
import os
import re
import sys
import unicodedata
import uuid

from . import calibrate, compare, coverage, dfw, oracle, tasks
from . import script as qvs
from .bridge import SANDBOX_SPACE_ID, Bridge, BridgeError, DryRun, SafetyError
from .remote import BASE_APP_ID, Remote, UnsupportedGraph


def make_bridge(apply: bool) -> Bridge:
    return Bridge(apply=apply)


def _sanitize(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def _write_pull(data: dict, out: str) -> str:
    os.makedirs(out, exist_ok=True)
    base = _sanitize(data["dataflow"].get("name") or "") or _sanitize(data["appId"])
    text = json.dumps(data, ensure_ascii=False, indent=2)
    path = os.path.join(out, base + ".pull.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            if f.read() != text:  # no sobrescribir un flujo distinto con el mismo nombre
                path = os.path.join(out, f"{base}_{data['appId'][:8]}.pull.json")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def _validate_remote(files, apply: bool, base_app: str | None = None) -> int:
    remote = Remote(make_bridge(apply))
    bad = 0
    for pat in files:
        for f in sorted(glob.glob(pat)):
            res = remote.validity_of(dfw.load(f)["dataflow"]["graph"], base_app or BASE_APP_ID)
            status = res.validity["status"]
            print(f"{f}: {status}")
            for m in res.validity.get("nodesConstraintViolations") or []:
                print(f"   - {m['code']}: {m['title']}")
            if status == "REJECTED":
                print(f"   - {res.validity['label']}")
            bad += status in ("INVALID", "REJECTED")
    return bad


def _pull(a) -> None:
    remote = Remote(make_bridge(False))  # pull es solo lectura
    try:
        if a.app_id:
            apps = [a.app_id]
        else:
            apps = [r.app_id for r in remote.list_dataflows(None if a.all_spaces else SANDBOX_SPACE_ID)]
    except (BridgeError, SafetyError) as e:
        sys.exit(f"error: {e}")
    failed = 0
    for app in apps:
        try:
            print(_write_pull(remote.pull(app), a.out))
        except (BridgeError, SafetyError) as e:
            failed += 1
            print(f"error en {app}: {e}", file=sys.stderr)
    if failed:
        sys.exit(1)


def _read_script(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if path.endswith(".json"):
        return json.loads(text)["script"]
    return text


def _translate(a) -> int:
    sql, reasons = qvs.translate(_read_script(a.file), a.data)
    if sql is None:
        print("no traducible:")
        for r in reasons:
            print(f"  - {r}")
        return 1
    print(sql)
    if a.run:
        rows, cols = qvs.run(sql)
        print(f"{len(rows)} filas, {len(cols)} columnas: {', '.join(cols)}")
    if a.compare:
        return _compare_translation(a, sql)
    return 0


def _compare_translation(a, sql: str) -> int:
    """Ejecuta el script original en el tenant y lo compara con el resultado de la traduccion."""
    text = _read_script(a.file)
    stem = qvs.store_stem(text)
    if stem is None:
        print("error: el script no tiene STORE; no hay resultado que comparar")
        return 1
    path = os.path.join(a.out, "translated", stem + ".csv")
    qvs.write_csv(sql, path)
    local = {compare.stem_of(path): compare.fingerprint_of(f"({sql})")}  # en memoria: el CSV no distingue vacio de NULL
    try:
        remote = oracle.run_script(make_bridge(a.apply), text, uuid.uuid4().hex[:8])
    except DryRun as e:
        print(f"[simulación] {e.method} {e.path}")
        return 0
    except (BridgeError, SafetyError, oracle.OracleError) as e:
        print(f"error: {e}")
        return 1
    diffs = compare.compare(local, remote)
    for m in diffs:
        print(m)
    print("OK: sin diferencias" if not diffs else f"{len(diffs)} diferencias")
    return 1 if diffs else 0


def _coverage(a) -> int:
    paths = a.files or coverage.default_paths()
    rows = coverage.report(paths, a.data)
    counts = collections.Counter()
    for path in paths:
        try:
            counts.update(coverage.processors_of(dfw.load(path)))
        except ValueError:
            pass  # el estado del archivo ya lo reporta coverage.report
    print("processors usados en el corpus:")
    for (t, v), n in sorted(counts.items()):
        print(f"  {t}{'.' + v if v else ''}: {n}")
    print("archivos:")
    for path, estado, detalle in rows:
        print(f"  {estado:<18} {path}" + (f"  ({detalle[:90]})" if detalle else ""))
    resumen = collections.Counter(e for _, e, _ in rows)
    print("resumen: " + ", ".join(f"{k}={v}" for k, v in sorted(resumen.items())))
    return 1 if resumen.get(coverage.FALLA) else 0


def _cleanup(a) -> None:
    remote = Remote(make_bridge(a.apply))
    try:
        flows, files = remote.list_emu()
    except (BridgeError, SafetyError) as e:
        sys.exit(f"error: {e}")
    for r in flows:
        print(f"app {r.name} ({r.app_id})")
    for n in files:
        print(f"archivo {n}")
    if not flows and not files:
        print("nada que limpiar")
        return
    if not a.apply:
        print("[simulación] usa --apply para borrar")
        return
    for r in flows:
        remote.discard(r.app_id)
    remote.discard_files(files)
    print(f"borrados: {len(flows)} app(s), {len(files)} archivo(s)")


def _compare(a) -> None:
    d = dfw.load(a.file)
    errs = dfw.validate(d)
    if errs:
        sys.exit("error: el .dfw no es valido: " + "; ".join(errs))
    from . import runner
    try:
        targets = runner.run(d, a.data, a.out)
    except runner.Unsupported as e:
        sys.exit(f"no soportado por el emulador: {e}")
    try:
        local = compare.target_fingerprints(targets)
    except ValueError as e:
        sys.exit(f"error: {e}")
    bridge = make_bridge(a.apply)
    try:
        if a.app:
            script = Remote(bridge).script_of(a.app)  # solo lectura del original
        else:
            res = Remote(bridge).validity_of(d["dataflow"]["graph"], a.base_app or BASE_APP_ID)  # clon descartable
            if res.validity["status"] == "REJECTED" or not res.script:
                sys.exit(f"error: el servidor no generó script: {res.validity.get('label', '')}")
            script = res.script
        remote = oracle.run_script(bridge, script, uuid.uuid4().hex[:8])
    except DryRun as e:
        print(f"[simulación] {e.method} {e.path}")
        sys.exit(0)
    except (BridgeError, SafetyError, UnsupportedGraph, oracle.OracleError) as e:
        sys.exit(f"error: {e}")
    diffs = compare.compare(local, remote)
    for m in diffs:
        print(m)
    if diffs:
        sys.exit(1)
    print("OK: sin diferencias")


def _validate(files):
    bad = 0
    for pat in files:
        for f in sorted(glob.glob(pat)):
            errs = dfw.validate(dfw.load(f))
            print(("OK   " if not errs else "FAIL ") + f)
            for m in errs:
                print("   -", m)
            bad += bool(errs)
    return bad


def _task(a) -> int:
    b = make_bridge(a.apply)
    try:
        if a.action == "ls":
            for t in tasks.list_tasks(b, a.app):
                print(f"{t.get('id')}  {'habilitada' if t.get('enabled') else 'deshabilitada'}  {t.get('name')}")
        elif a.action == "schedule":
            t = tasks.schedule(b, a.app, a.name, a.recurrence, a.timezone, a.enable)
            print(f"tarea {t.get('id')} creada ({'habilitada' if t.get('enabled') else 'deshabilitada'})")
        elif a.action == "chain":
            t = tasks.chain(b, a.app, a.name, a.after, a.on, a.enable)
            print(f"tarea {t.get('id')} creada: se ejecuta cuando {a.after} termina ({a.on})")
        elif a.action == "start":
            print(tasks.start(b, a.task).get("message", "iniciada"))
        elif a.action == "runs":
            for r in tasks.runs(b, a.task):
                print(f"{r.get('id')}  {r.get('status')}  {r.get('startedAt', '')}  {r.get('endedAt', '')}")
        elif a.action in ("enable", "disable"):
            tasks.set_enabled(b, a.task, a.action == "enable")
            print(f"tarea {'habilitada' if a.action == 'enable' else 'deshabilitada'}")
        elif a.action == "rm":
            tasks.delete(b, a.task)
            print("tarea borrada")
    except DryRun as e:
        print(f"[simulación] {e.method} {e.path}")
    except (BridgeError, SafetyError, ValueError) as e:
        print(f"error: {e}")
        if "CHO-012" in str(e):
            print("la tarea esta deshabilitada: habilitela con `task enable TAREA --apply`")
        return 1
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="dfemu")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("files", nargs="+")
    v.add_argument("--remote", action="store_true", help="sube el grafo a un clon en el tenant y lee su validez")
    v.add_argument("--apply", action="store_true", help="ejecutar la subida (sin esto solo simula)")
    v.add_argument("--base-app", help="flujo a clonar (por omision DFEMU_BASE_APP); para grafos con subflows, el flujo del que vienen")
    c = sub.add_parser("calibrate", help="compara el validador local con el servidor sobre mutaciones")
    c.add_argument("--base", default="samples/fundamentos.dfw")
    c.add_argument("--apply", action="store_true", help="consultar al tenant (sin esto solo simula)")
    r = sub.add_parser("run", help="valida y ejecuta un .dfw")
    r.add_argument("file")
    r.add_argument("--data", default="data/practica", help="carpeta con los CSV de los datasets")
    r.add_argument("--out", default="out")
    r.add_argument("--connections", help="json: {conexion: {type: duckdb|sqlite|postgres, path|dsn}}")
    r.add_argument("--s3", action="store_true", help="escribir a S3/MinIO real (env S3_ENDPOINT, S3_KEY, S3_SECRET)")
    p = sub.add_parser("pull", help="descarga flujos del tenant (solo lectura) a un .pull.json")
    p.add_argument("app_id", nargs="?", help="id de la app del flujo")
    p.add_argument("--all", action="store_true", help="todos los flujos del espacio permitido")
    p.add_argument("--all-spaces", action="store_true", help="todos los flujos de todos los espacios")
    p.add_argument("--out", default="out/corpus")
    cp = sub.add_parser("compare", help="ejecuta el emulador y compara sus salidas con el tenant")
    cp.add_argument("file")
    origen = cp.add_mutually_exclusive_group(required=True)
    origen.add_argument("--app", help="id de la app del flujo original (solo lectura)")
    origen.add_argument("--push", action="store_true", help="sube el grafo a un clon descartable")
    cp.add_argument("--data", default="data/practica", help="carpeta con los CSV de los datasets")
    cp.add_argument("--out", default="out")
    cp.add_argument("--base-app", help="con --push: flujo a clonar (por omision DFEMU_BASE_APP)")
    cp.add_argument("--apply", action="store_true", help="ejecutar en el tenant (sin esto solo simula)")
    tk = sub.add_parser("task", help="programa, encadena, arranca y borra tareas de recarga de apps emu_")
    ap_apply = argparse.ArgumentParser(add_help=False)
    ap_apply.add_argument("--apply", action="store_true", help="ejecutar en el tenant (sin esto solo simula)")
    tsub = tk.add_subparsers(dest="action", required=True)
    t = tsub.add_parser("ls", help="lista las tareas de una app", parents=[ap_apply])
    t.add_argument("app")
    t = tsub.add_parser("schedule", help="recarga la app segun una regla RRULE", parents=[ap_apply])
    t.add_argument("app")
    t.add_argument("--name", required=True)
    t.add_argument("--recurrence", required=True, help="p. ej. RRULE:FREQ=DAILY;BYHOUR=3;BYMINUTE=0;BYSECOND=0")
    t.add_argument("--timezone", default="UTC")
    t.add_argument("--enable", action="store_true", help="crear habilitada (por omision queda deshabilitada)")
    t = tsub.add_parser("chain", help="recarga la app cuando termina otra tarea", parents=[ap_apply])
    t.add_argument("app")
    t.add_argument("--name", required=True)
    t.add_argument("--after", required=True, help="id de la tarea previa")
    t.add_argument("--on", default="succeeded", choices=tasks.STATUSES)
    t.add_argument("--enable", action="store_true")
    t = tsub.add_parser("start", help="arranca una tarea habilitada", parents=[ap_apply])
    t.add_argument("task")
    t = tsub.add_parser("runs", help="ultimas ejecuciones de una tarea", parents=[ap_apply])
    t.add_argument("task")
    for act, txt in (("enable", "habilita una tarea (hace falta para arrancarla)"), ("disable", "deshabilita una tarea")):
        t = tsub.add_parser(act, help=txt, parents=[ap_apply])
        t.add_argument("task")
    t = tsub.add_parser("rm", help="borra una tarea", parents=[ap_apply])
    t.add_argument("task")
    su = sub.add_parser("setup", help="instala la CLI de Qlik, crea el contexto (pide la API key) y fija el espacio de pruebas")
    su.add_argument("--yes", action="store_true", help="descargar la CLI sin preguntar")
    su.add_argument("--space", help="id del espacio de pruebas (si no, se elige de una lista)")
    su.add_argument("--base-app", help="id del flujo base (si no, se elige de una lista)")
    cl = sub.add_parser("cleanup", help="borra apps y archivos emu_* del espacio permitido")
    cl.add_argument("--apply", action="store_true", help="borrar de verdad (sin esto solo lista)")
    co = sub.add_parser("coverage", help="mide que processors usa el corpus y que se puede ejecutar")
    co.add_argument("files", nargs="*", help="archivos .dfw (por omision, samples/**/*.dfw)")
    co.add_argument("--data", default="data/practica", help="carpeta con los CSV de los datasets")
    tr = sub.add_parser("translate", help="traduce un script de Qlik (qvs o .pull.json) a SQL de DuckDB")
    tr.add_argument("file")
    tr.add_argument("--data", default="data/practica", help="carpeta con los CSV de los datasets")
    tr.add_argument("--run", action="store_true", help="ejecutar el SQL traducido")
    tr.add_argument("--compare", action="store_true", help="ejecutar el script en el tenant y comparar las huellas con la traduccion")
    tr.add_argument("--apply", action="store_true", help="con --compare: ejecutar en el tenant (sin esto solo simula)")
    tr.add_argument("--out", default="out")
    a = ap.parse_args(argv)
    if a.cmd == "validate":
        if a.remote:
            try:
                sys.exit(1 if _validate_remote(a.files, a.apply, a.base_app) else 0)
            except DryRun as e:
                print(f"[simulación] {e.method} {e.path}")
                sys.exit(0)
            except (BridgeError, SafetyError, UnsupportedGraph) as e:
                sys.exit(f"error: {e}")
        sys.exit(1 if _validate(a.files) else 0)
    if a.cmd == "calibrate":
        remote = Remote(make_bridge(a.apply))
        try:
            rows = calibrate.run_battery(dfw.load(a.base), lambda g: remote.validity_of(g).validity["status"])
        except DryRun as e:
            print(f"[simulación] {e.method} {e.path}")
            sys.exit(0)
        except (BridgeError, SafetyError, UnsupportedGraph) as e:
            sys.exit(f"error: {e}")
        print(calibrate.format_rows(rows))
        sys.exit(1 if calibrate.disagreements(rows) else 0)
    if a.cmd == "compare":
        return _compare(a)
    if a.cmd == "task":
        sys.exit(_task(a))
    if a.cmd == "setup":
        from . import setup
        try:
            return setup.run(a.yes, a.space, a.base_app)
        except (setup.SetupError, BridgeError, EOFError) as e:
            sys.exit(f"error: {e}")
    if a.cmd == "cleanup":
        return _cleanup(a)
    if a.cmd == "coverage":
        sys.exit(_coverage(a))
    if a.cmd == "translate":
        sys.exit(_translate(a))
    if a.cmd == "pull":
        if not (a.app_id or a.all or a.all_spaces):
            ap.error("pull requiere APP_ID, --all o --all-spaces")
        return _pull(a)
    if _validate([a.file]):
        sys.exit("no se ejecuta: el .dfw no es valido")
    from . import runner
    conns = json.load(open(a.connections, encoding="utf-8")) if a.connections else {}
    s3 = {"endpoint": os.environ["S3_ENDPOINT"], "key": os.environ["S3_KEY"], "secret": os.environ["S3_SECRET"]} if a.s3 else None
    try:
        for t in runner.run(dfw.load(a.file), a.data, a.out, conns, s3):
            print(f"  -> {t['dest']}  ({t['rows']} filas){'  [qvd emulado como parquet]' if t['emulated_qvd'] else ''}")
    except runner.Unsupported as e:
        sys.exit(f"no soportado por el emulador: {e}")


if __name__ == "__main__":
    main()
