"""Runner falso para probar el Bridge sin tocar el tenant ni el CLI real."""
import json


class FakeRunner:
    """Rutas: (MÉTODO, ruta) para `qlik raw`; ("CLI", "app script set|tables|eval") para motor.

    Valor de ruta: JSON-able (stdout), (rc, stdout, stderr), o callable(body) -> valor.
    Un str en ruta CLI se devuelve tal cual como stdout de texto.
    """

    def __init__(self, routes):
        self.routes = routes
        self.calls = []  # (método, ruta, cuerpo decodificado UTF-8 o None)

    def __call__(self, args):
        if args[0] == "raw":
            key = (args[1].upper(), args[2])
            body = None
            if "--body-file" in args:
                with open(args[args.index("--body-file") + 1], encoding="utf-8") as f:
                    body = json.load(f)
        else:
            key = ("CLI", " ".join(args[:3]) if args[1] == "script" else " ".join(args[:2]))
            body = None
            if key[1] == "app script set":
                with open(args[3], encoding="utf-8") as f:
                    body = f.read()
        self.calls.append((key[0], key[1], body))

        if key not in self.routes:
            return 1, "", f"sin ruta fake para {key}"
        value = self.routes[key]
        if callable(value):
            value = value(body)
        if isinstance(value, tuple):
            return value
        if key[0] == "CLI" and isinstance(value, str):
            return 0, value, ""
        return 0, json.dumps(value, ensure_ascii=False), ""
