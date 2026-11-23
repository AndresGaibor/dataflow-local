"""Construye .dfw sinteticos con la misma forma que los exports reales de Qlik Cloud."""
import json
import uuid

_CONFIGURED = {"$state": "CONFIGURED"}

# processor -> (handles entrantes, handles salientes), segun .dfw reales
_SHAPES = {
    "join": (["DEFAULT", "LOOKUP"], ["DEFAULT"]),
    "filter": (["DEFAULT"], ["DEFAULT", "REJECT"]),
    "fork": (["DEFAULT"], ["DEFAULT"] + [f"OPTIONAL_{i}" for i in range(1, 10)]),
    "union": (["DEFAULT"] + ["OPTIONAL"] * 9, ["DEFAULT"]),
    "script": (["OPTIONAL"] * 10, ["DEFAULT"] + [f"OPTIONAL_{i}" for i in range(1, 10)]),
}


class Flow:
    def __init__(self, name, locale="en-US"):
        self.name, self.nodes, self.edges, self.sources, self.subflows, self.locale = name, [], [], [], [], locale
        self._h = {}  # (node_id, direction, handle_type) -> handle_id
        self._n = 0

    def _id(self):
        # ids deterministas por flujo: regenerar samples/ no ensucia git
        self._n += 1
        return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{self.name}:{self._n}"))

    def _node(self, kind, ctype, label, props, inc, out, x):
        n = {"type": kind, "id": self._id(), "label": label, "graphical": {"position": {"x": x, "y": 120}},
             "handles": {"incoming": [{"id": self._id(), "type": t} for t in inc], "outgoing": [{"id": self._id(), "type": t} for t in out]},
             "component": {"type": ctype, "properties": props}}
        if kind == "source":
            del n["handles"]["incoming"][:]
        if kind == "target":
            del n["handles"]["outgoing"]
        self.nodes.append(n)
        for d in ("incoming", "outgoing"):
            for h in n["handles"].get(d, []):
                self._h[(n["id"], d, h["type"])] = h["id"]
        return n

    def dataset(self, label, file, fields, space="Entrenamiento Dataflow", x=60):
        sid, dsid = self._id(), self._id()
        self.sources.append({"connections": {"DataFiles": {"name": "DataFiles", "typeName": "qix-datafiles", "sourceConnectorID": "qix-datafiles",
                             "dataconnectorPrefix": f"{space}:", "space": self._id()}}, "sourceId": sid, "datasetId": dsid, "qri": None,
                             "tables": [{"databaseName": file, "dataconnectorName": "DataFiles", "dataconnectorPrefix": f"{space}:",
                                         "fields": [{"name": f, "id": self._id()} for f in fields], "tableName": file.rsplit(".", 1)[0],
                                         "formatSpec": "(txt, utf8, embedded labels, delimiter is ',', msq)", "ownerName": "TYPE9_CSV"}]})
        return self._node("source", "analyticsSource", label, {"dataEntity": {"entityId": sid}, "configuration": {}, "type": "dataset"}, [], ["DEFAULT"], x)

    def db(self, label, connector, conn_name, table, fields, space="Entrenamiento Dataflow", x=60):
        """Origen de base de datos via conector ODBC (ej. gbq, postgres)."""
        sid = self._id()
        self.sources.append({"connections": {conn_name: {"name": conn_name, "typeName": "QvOdbcConnectorPackage.exe", "sourceConnectorID": connector,
                             "dataconnectorPrefix": f"{space}:"}}, "sourceId": sid, "datasetId": None, "qri": None,
                             "tables": [{"databaseName": table, "dataconnectorName": conn_name, "dataconnectorPrefix": f"{space}:",
                                         "fields": [{"name": f, "alias": f, "selected": True, "id": self._id()} for f in fields]}]})
        return self._node("source", "analyticsSource", label, {"dataEntity": {"entityId": sid}, "configuration": {}, "type": "connection"}, [], ["DEFAULT"], x)

    def proc(self, ctype, label, cfg, x=380, inc=None, out=None):
        i, o = _SHAPES.get(ctype, (["DEFAULT"], ["DEFAULT"]))
        cfg = dict(cfg)
        if ctype not in ("fork", "subflow"):
            cfg.update(_CONFIGURED)
        return self._node("processor", ctype, label, {"configuration": cfg}, inc or i, out or o, x)

    def target(self, label, file, ext="csv", fmt="txt", connection="GDDestino", ds="File_GoogleDriveConnector", space="Entrenamiento Dataflow", x=920):
        s = {"spaceName": space, "envName": "", "fileName": file, "extension": ext, "format": fmt, "connectionName": connection, "treatAsRelative": False}
        return self._node("target", "analyticsTarget", label, {"configuration": {"name": label, "settings": s, "$datasourceId": ds, **_CONFIGURED}}, ["DEFAULT"], [], x)

    def s3(self, label, key, ext="parquet", fmt="parquet", connection="S3Destino", x=920):
        # supuesto: id de conector S3 (no hay .dfw real con S3); ajustar al ver uno
        return self.target(label, key, ext, fmt, connection, "File_AmazonS3Connector", x=x)

    def link(self, a, b, out="DEFAULT", inc=None):
        """Conecta salida `out` de a con la primera entrada libre (o `inc`) de b."""
        src = self._h[(a["id"], "outgoing", out)]
        used = {e["targetHandle"] for e in self.edges}
        free = [h["id"] for h in b["handles"]["incoming"] if h["id"] not in used and (inc is None or h["type"] == inc)]
        self.edges.append({"id": self._id(), "sourceHandle": src, "targetHandle": free[0]})
        return b

    def chain(self, *nodes):
        for a, b in zip(nodes, nodes[1:]):
            self.link(a, b)
        return nodes[-1]

    def dump(self):
        return {"dataflow": {"id": self._id(), "description": "sintetico", "name": self.name,
                             "context": {"projectId": self._id(), "dataAppId": self._id(), "version": 8, "usage": "DATAFLOW_PREP"},
                             "createdAt": "2026-11-17T00:00:00.000Z", "createdBy": "synthetic", "updatedAt": "2026-11-17T00:00:00.000Z",
                             "updatedBy": "synthetic", "checksum": self._id(), "modelVersion": "1.0.0",
                             "graph": {"nodes": self.nodes, "edges": self.edges}},
                "subflows": self.subflows, "sources": self.sources, "projections": [], "schemas": [], "collationLocale": self.locale}

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.dump(), f, ensure_ascii=False)


# --- helpers de configuracion de processors ---
def sel(*fields):  # fields: "campo" o ("campo", "alias")
    return {"selectors": [{"path": f if isinstance(f, str) else f[0], "field": f if isinstance(f, str) else f[0],
                           "output": "" if isinstance(f, str) else f[1], "selected": True} for f in fields], "distinct": False}


def flt(*conds, op="ALL"):  # conds: (columna, operador, valor)
    return {"logicalOpType": op, "filters": [{"columnName": c, "function": "EMPTY", "operator": o, "compareWith": "VALUE", "value": v,
                                              "columnToCompareWith": ""} for c, o, v in conds]}


def agg(group, *ops):  # ops: (operacion, campo, salida)
    return {"groupBy": [{"fieldPath": g} for g in group],
            "operations": [{"operation": o, "fieldPaths": [f], "delimiter": ",", "outputFieldPath": out} for o, f, out in ops]}


def join(kind, *keys):  # keys: (izq, der)
    return {"joinFunction": kind, "conditions": [{"leftKey": l, "rightKey": r, "keepBothKeysInOutput": False} for l, r in keys]}


def calc(*exprs):  # exprs: (nombre, expresion Qlik)
    return {"calculateFields": [{"newColumnName": n, "expressionStatement": e, "anchorColumn": "", "rightOfAnchor": False, "fieldReferences": []}
                                for n, e in exprs]}
