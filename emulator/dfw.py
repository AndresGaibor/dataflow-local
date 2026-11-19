"""Carga y valida archivos .dfw (export de Qlik Cloud Data Flow). Esquema inferido de .dfw reales."""
import json

# processor -> claves obligatorias dentro de configuration (observadas en .dfw reales)
REQUIRED = {
    "aggregate": ["groupBy", "operations"], "calculate-fields": ["calculateFields"],
    "data-cleansing": ["type"], "date": ["type"], "field-concatenator": ["type", "concatConfiguration"],
    "field-remover": ["selectors"], "field-selector": ["selectors"],
    "filter": ["filters", "logicalOpType"], "join": ["joinFunction", "conditions"],
    "masking": ["type"], "math": ["type"], "numbers": ["type"], "sample": ["type"],
    "script": ["script"], "sort": ["sortFields"], "split-field": ["type"], "strings": ["type"],
    "union": ["unionAll"], "window": ["operationConfiguration", "partitionByConfiguration", "sortingConfiguration"],
    "fork": [], "subflow": ["dataflowId"], "edit-column": ["type"],
}
# processor -> {type: clave con su configuracion especifica}
TYPED = {
    "data-cleansing": {"REPLACE_WITH_VALUE": "replaceWithValueConfiguration", "FILL_WITH_VALUE": "fillWithValueConfiguration"},
    "date": {"EXTRACT_DATE_PARTS": "extractDateTokensConfiguration", "CONVERT_TO_DATE": "convertToDateConfiguration",
             "CONVERT_TO_TIMESTAMP": "convertToTimestampConfiguration"},
    "masking": {"HASH_DATA": "hashDataConfiguration"},
    "math": {"ABSOLUTE": "absoluteConfiguration", "MULTIPLY": "multiplyConfiguration"},
    "numbers": {"CONVERT_TO_NUMBER": "convertToNumberConfiguration"},
    "split-field": {"SPLIT_TEXT_IN_PARTS": "splitTextInPartsConfiguration"},
    "strings": {"PROPERCASE": "propercaseConfiguration", "REMOVE_NON_NUM_CHARS": "removeNonNumCharsConfiguration",
                "REPLACE_ON_VALUE": "replaceOnValueConfiguration", "TRIM": "trimConfiguration"},
    "field-concatenator": {"CONCAT": "concatConfiguration"},
    # shortcut: edit-column (receta de tabla, dentro de subflows) solo conoce RENAME; agregar tipos al verlos
    "edit-column": {"RENAME": "renameColumnConfiguration"},
    "sample": {"SAMPLE_RANDOM_ROWS": "sampleRandomRowsConfiguration", "SAMPLE_FIRST_ROWS": "sampleFirstRowsConfiguration",
               "SAMPLE_N_RANDOM_ROWS": "sampleNRandomRowsConfiguration",
               "SAMPLE_STRATIFIED_RANDOM_ROWS": "sampleStratifiedRandomRowsConfiguration"},
}
# shortcut: enums = valores vistos en .dfw reales + docs; ampliar al aparecer valores nuevos
JOIN_FUNCTIONS = {"INNER_JOIN", "LEFT_OUTER_JOIN", "RIGHT_OUTER_JOIN", "FULL_OUTER_JOIN"}
LOGICAL_OPS = {"ALL", "ANY"}
MAX_SCRIPTS, MAX_SCRIPT_OUTPUTS = 50, 2  # limites documentados (data-flow-processor-script.md)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _handles(graph):
    """handle_id -> (node, direction, handle_type)"""
    out = {}
    for n in graph["nodes"]:
        for d in ("incoming", "outgoing"):
            for h in n.get("handles", {}).get(d, []):
                out[h["id"]] = (n, d, h["type"])
    return out


def validate_graph(graph, where, sources_meta=None):
    errs = []
    e = lambda m: errs.append(f"{where}: {m}")
    nodes = graph.get("nodes", [])
    ids = [n["id"] for n in nodes]
    if len(ids) != len(set(ids)):
        e("ids de nodo duplicados")
    hs = _handles(graph)
    kinds = [n["type"] for n in nodes]
    if where == "dataflow" and "source" not in kinds:
        e("sin nodo source")
    if where == "dataflow" and "target" not in kinds:
        e("sin nodo target")
    linked, adj = set(), {i: [] for i in ids}
    for ed in graph.get("edges", []):
        a, b = hs.get(ed["sourceHandle"]), hs.get(ed["targetHandle"])
        if not a or not b:
            e(f"arista con handle inexistente {ed['id'][:30]}")
            continue
        if a[1] != "outgoing" or b[1] != "incoming":
            e("arista con direccion invalida")
        linked |= {ed["sourceHandle"], ed["targetHandle"]}
        adj[a[0]["id"]].append(b[0]["id"])
    for n in nodes:
        c = n["component"]
        label = f"{c['type']} '{n.get('label')}'"
        cfg = c.get("properties", {}).get("configuration", {})
        for d in ("incoming", "outgoing"):
            for h in n.get("handles", {}).get(d, []):
                # REJECT (filter) y los OPTIONAL pueden quedar sin conectar
                if h["type"] == "DEFAULT" and h["id"] not in linked:
                    e(f"{label}: handle {d} sin conectar")
        if n["type"] == "source":
            _check_source(c, e, label, sources_meta)
        elif n["type"] == "target":
            _check_target(c, cfg, e, label)
        else:
            _check_processor(n, c["type"], cfg, e, label)
    color = {}

    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color.get(v) == 1 or (v not in color and dfs(v)):
                return True
        color[u] = 2
        return False

    if any(i not in color and dfs(i) for i in ids):
        e("el grafo tiene ciclos")
    scripts = [n for n in nodes if n["component"]["type"] == "script"]
    if len(scripts) > MAX_SCRIPTS:
        e(f"{len(scripts)} script processors (max {MAX_SCRIPTS})")
    for n in scripts:
        outs = sum(1 for h in n["handles"]["outgoing"] if h["id"] in linked)
        if outs > MAX_SCRIPT_OUTPUTS:
            e(f"script '{n.get('label')}' con {outs} salidas conectadas (max {MAX_SCRIPT_OUTPUTS})")
    return errs


def _check_source(c, e, label, meta):
    p = c.get("properties", {})
    if c["type"] == "linkedSource":  # entrada de un subflow
        return
    if c["type"] != "analyticsSource" or p.get("type") not in ("dataset", "connection"):
        e(f"{label}: source invalido")
        return
    eid = p.get("dataEntity", {}).get("entityId")
    if not eid:
        e(f"{label}: sin dataEntity.entityId")
    elif meta is not None and p["type"] == "dataset" and eid not in meta:  # connections no se listan en sources
        e(f"{label}: entityId {eid[:8]}.. no esta en 'sources'")


def _check_target(c, cfg, e, label):
    if c["type"] == "noOpTarget":  # salida de un subflow
        return
    s = cfg.get("settings", {})
    for k in ("fileName", "extension", "format"):
        if not s.get(k):
            e(f"{label}: settings.{k} vacio")


def _check_processor(n, t, cfg, e, label):
    if t not in REQUIRED:
        e(f"{label}: processor desconocido")
        return
    for k in REQUIRED[t]:
        if k not in cfg:
            e(f"{label}: falta configuration.{k}")
    if t == "field-selector" and not any(x.get("selected", True) for x in cfg.get("selectors", [])):
        e(f"{label}: field-selector sin campos seleccionados")  # servidor: selectors vacio es INVALID
    if t in TYPED and "type" in cfg:
        key = TYPED[t].get(cfg["type"])
        if key is None:
            e(f"{label}: type '{cfg['type']}' desconocido")
        elif key not in cfg:
            e(f"{label}: falta {key}")
    if t == "join":
        if cfg.get("joinFunction") not in JOIN_FUNCTIONS:
            e(f"{label}: joinFunction invalido")
        if not cfg.get("conditions"):
            e(f"{label}: join sin condiciones")
    if t == "filter":
        if cfg.get("logicalOpType") not in LOGICAL_OPS:
            e(f"{label}: logicalOpType invalido")
        if not cfg.get("filters"):
            e(f"{label}: sin filtros")
    if t == "aggregate" and not cfg.get("operations"):
        e(f"{label}: aggregate sin operaciones")
    if t == "union" and len(n["handles"]["incoming"]) < 2:
        e(f"{label}: union necesita >=2 entradas")


def validate(d):
    if "dataflow" not in d or "graph" not in d["dataflow"]:
        return ["no es un .dfw (falta dataflow.graph)"]
    meta = {s["sourceId"] for s in d.get("sources", [])}
    errs = validate_graph(d["dataflow"]["graph"], "dataflow", meta)
    for sf in d.get("subflows", []):
        errs += validate_graph(sf["graph"], f"subflow {sf['id'][:8]}")
    refs = {n["component"]["properties"]["configuration"].get("dataflowId")
            for n in d["dataflow"]["graph"]["nodes"] if n["component"]["type"] == "subflow"}
    if refs - {s["id"] for s in d.get("subflows", [])}:
        errs.append("dataflow: subflow referenciado que no existe en 'subflows'")
    return errs
