import argparse
import glob
import json
import os
import re
import sys
import unicodedata
import uuid

from . import calibrate, compare, dfw, oracle
from .bridge import SANDBOX_SPACE_ID, Bridge, BridgeError, DryRun, SafetyError
from .remote import Remote, UnsupportedGraph


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


def _validate_remote(files, apply: bool) -> int:
    remote = Remote(make_bridge(apply))
    bad = 0
    for pat in files:
        for f in sorted(glob.glob(pat)):
            res = remote.validity_of(dfw.load(f)["dataflow"]["graph"])
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
        local = compare.local_fingerprints([t["dest"] for t in targets])
    except ValueError as e:
        sys.exit(f"error: {e}")
    bridge = make_bridge(a.apply)
    try:
        if a.app:
            script = Remote(bridge).script_of(a.app)  # solo lectura del original
        else:
            res = Remote(bridge).validity_of(d["dataflow"]["graph"])  # clon descartable
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


def main(argv=None):
    ap = argparse.ArgumentParser(prog="dfemu")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("files", nargs="+")
    v.add_argument("--remote", action="store_true", help="sube el grafo a un clon en el tenant y lee su validez")
    v.add_argument("--apply", action="store_true", help="ejecutar la subida (sin esto solo simula)")
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
    cp.add_argument("--apply", action="store_true", help="ejecutar en el tenant (sin esto solo simula)")
    a = ap.parse_args(argv)
    if a.cmd == "validate":
        if a.remote:
            try:
                sys.exit(1 if _validate_remote(a.files, a.apply) else 0)
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
