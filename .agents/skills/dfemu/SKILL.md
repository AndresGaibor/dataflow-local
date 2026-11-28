---
name: dfemu
description: Load when working on Qlik Cloud Data Flows from this repo — emulating a .dfw locally, translating its Qlik script, comparing emulator vs tenant, measuring a processor against the tenant, capturing the payloads only the UI sends (pivot, map-fields, subflow, script node, datasources, import/export), or driving this repo through its MCP server (`dfemu mcp`). Triggers - "dataflow", "data flow de qlik", ".dfw", "emulador de dataflow", "comparar con el tenant", "bateria de processors", "dfemu flow", "dfemu ui", "dfemu mcp", "script de qlik a sql", "recargar app emu_".
metadata:
  version: 1.0.0
  scope: project
---

# dfemu: banco de pruebas de los Data Flows de Qlik Cloud

Este repo emula `.dfw` con DuckDB, traduce el script de Qlik a SQL y compara resultados con el tenant.
Todo lo que se afirma sobre Qlik se **mide** primero: los hallazgos viven en
`docs/banco-de-pruebas/01-hallazgos-api-qlik.md` (apartados 9 quater y 12) y no se repiten pruebas ya hechas.

## Regla de oro

- Se escribe **solo** en objetos `emu_*` del espacio de pruebas, y solo con `--apply`. Sin `--apply` todo simula.
- Nunca imprimir credenciales ni el host del tenant. Nada de `qlik ... --verbose` (imprime el token).
- Antes de afirmar cómo se comporta Qlik, medirlo en el tenant y dejar la evidencia en el documento de hallazgos.

## Por dónde empezar según la tarea

| Tarea | Camino |
| --- | --- |
| Saber qué se puede hacer | `dfemu mcp --list` (herramientas del asistente) o `python -m emulator.cli --help` |
| Emular un `.dfw` y ver qué processors usa | `python -m emulator.cli coverage [--stub]` |
| Traducir un script de Qlik a SQL | `python -m emulator.cli translate ARCHIVO [--run] [--compare --apply]` |
| Comparar emulador contra el tenant | `python -m emulator.cli compare ARCHIVO --apply` |
| Medir un processor contra el tenant | `python -m emulator.cli mcp` → `dfemu_battery_run`, o `python scripts/processor_battery.py CASO` |
| Leer el grafo de un flujo | `dfemu flow show FLUJO [--full]` / `dfemu flow node FLUJO NODO` |
| Añadir o cambiar un nodo | `dfemu flow add TIPO --after NODO --cfg JSON --apply`, `dfemu flow set`, `dfemu flow rm` |
| Crear un flujo desde cero con sus nodos | `dfemu flow add` sobre un clon `emu_`, o `scripts/e2e_ventas.py --escenario ...` |
| Recargar una app | `dfemu reload APP [--apply]` (acepta nombre de flujo o id) |
| Saber la configuración de un processor | MCP: `dfemu_processor_definition` (el servidor da la config inicial y los puertos) |
| Editar el grafo desde un asistente | MCP: `dfemu_flow_add_node`, `dfemu_flow_set_node`, `dfemu_flow_remove_node`, `dfemu_flow_backup`, `dfemu_flow_restore` |
| Cambiar el script de una app | MCP: `dfemu_script_get`, `dfemu_script_set`, `dfemu_script_validate` |
| Probar sin tocar el tenant | `DFEMU_MCP_APPLY=0` deja todas las escrituras del MCP en simulacro |
| Ejecutar un .dfw en local | MCP: `dfemu_emulate` |
| Qlik Automate | `dfemu automate ls|new|show|run|runs|enable|disable|rm` |
| Buscar en la documentación de Qlik | `dfemu_docs_search` (MCP) o grep en `docs/` |

## Nodos que la interfaz crea a mano: qué deja la API y qué no

Medido, no supuesto (apartado 12). `dfemu_flow_add_node` inserta los cuatro processors y el servidor dice qué falta:

| Nodo | Por API | Lo que falta |
|---|---|---|
| `subflow` | queda **VALID** | nada: el clon trae el subflow propio |
| `map-fields` | entra y se configura | la entrada `LOOKUP` conectada (`feed`: `{"LOOKUP": "filtro:REJECT"}`) y la resolución de campos |
| `pivot` | entra y se configura, y **la interfaz también lo crea sin manos** (`dfemu ui add Pivotar`) | `schemaEntityId`, que solo crea Aplicar |
| `script` | entra y se configura | `schemaEntityId`; el `POTENTIAL_STALE_SCRIPT` lo limpia otro PUT |
| `datasources` | `ADF-500` con `{}`, `{datasetId}` o `{datasetId,sourceId}` | el cuerpo entero |
| import/export `.dfw` | sin cuerpo conocido | el archivo que manda la interfaz |

Orden de intentos, del más barato al más caro:

1. **Descubrir la configuración por error del servidor**: mandar `{}` o un enum inválido y leer el mensaje
   (`VALUE_MISSING_ON_REQUIRED_FIELD`, `Cannot deserialize ... not one of the values accepted for Enum class`).
   Así salieron los seis operadores de `COMPARE_NUMBERS`, los patrones de `MATCHES_PATTERN` y las nueve unidades
   de `MODIFY_DATES`. `scripts/discover_config.py` automatiza el método.
2. **Crear el nodo con la interfaz ya abierta** (`dfemu ui add "Pivotar" --on NODO --apply`, `dfemu ui options`,
   `dfemu ui fill`, `dfemu ui apply`) y leerlo luego por API con `dfemu flow node`.
3. **Grabar lo que manda la interfaz** cuando hace falta el cuerpo exacto:

```bash
playwright-cli attach --cdp=chrome          # una vez; la sesión se llama `chrome` (DFEMU_BROWSER_SESSION)
dfemu flow capture start                    # instala el grabador en la pestaña de Qlik Cloud
# ... aquí se hace la acción en la interfaz: añadir Pivot, importar un .dfw, crear una fuente ...
dfemu flow capture dump --only dataflows --save out/captures/pivot.json
```

`dump` imprime una línea por petición (método, ruta sin host, estado y tamaño) y con `--save` guarda los cuerpos
completos. De ahí sale el JSON que la API no explica; después se documenta en el apartado 12 y, si procede, se
añade el caso a la batería.

## Servidor MCP (`dfemu mcp`)

- Registro en Claude Code: `claude mcp add dfemu -- python -m emulator.cli mcp`. Catálogo: `docs/MCP.md`.
- Riesgos: `read` libre; `write` con `DFEMU_MCP_ALLOW_WRITE=0` para apagarlo; `execute` exige `confirm: true`;
  `destructive` bloqueado salvo `DFEMU_MCP_ALLOW_DESTRUCTIVE=1` **y** `confirm: true`.
- Toda escritura se limita a nombres `emu_*` y cada llamada queda en `.dfemu-mcp/audit.jsonl` (sin argumentos).
- Empieza por `dfemu_guide` (modos `overview`, `dataflow`, `script`, `automate`, `docs`, `battery`).
- Publica también recursos (`dfemu://docs/hallazgos`, `dfemu://skill/dfemu`...) y prompts (`crear-dataflow`,
  `medir-processor`, `capturar-interfaz`, `recargar-app`): úsalos antes de inventar una secuencia.
- Las herramientas largas emiten `notifications/progress` si el cliente manda `_meta.progressToken`.

## Antes de dar algo por bueno

```bash
python -m pytest -q                       # suite local, sin tenant ni red
python scripts/test_coverage.py           # publica la cobertura en el README (el CI corre --check)
python scripts/docsync.py --check         # documentación de Qlik completa (0 faltantes)
python scripts/processor_coverage.py --readme && python scripts/script_inventory.py --readme
```

Un cambio de comportamiento en Qlik necesita además su caso medido: si no se puede medir, se marca `shortcut:`
en el código y se explica el límite en el apartado 12. No se afirma "funciona" sin una ejecución que lo demuestre.

## Trampas conocidas

- Windows: la CLI de Qlik necesita `< /dev/null` o se cuelga; al escribir archivos con `\n` dentro de cadenas usa
  las herramientas de edición (`write_file`, `edit`), no heredocs de Python.
- Un nodo `calculate-fields` nuevo sale `INVALID` (`POTENTIAL_STALE_EXPRESSION`): un `PUT` idéntico lo limpia y
  cada nivel encadenado necesita uno más (`Remote.push_graph` ya lo hace).
- `valid_id` acepta cadenas como `emu_e2e_calidad`: si un comando admite id o nombre, resuelve el nombre primero.
- Las listas de la API llegan como array pelado, no como `{"data": [...]}`; `v1/items` sí las envuelve.
