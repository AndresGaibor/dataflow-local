# Servidor MCP de dfemu

`dfemu mcp` expone el banco de pruebas a un asistente (Claude Code, Copilot, Cursor…) por
[stdio](https://modelcontextprotocol.io/): un mensaje JSON-RPC por línea, sin dependencias nuevas.
El asistente deja de adivinar rutas y comandos, y el servidor decide qué se puede hacer.

```
dfemu mcp --list     # herramientas, riesgo y para qué sirven
dfemu mcp            # servidor en stdio (lo arranca el cliente MCP)
```

## Registrarlo

Claude Code:

```bash
claude mcp add dfemu -- python -m emulator.cli mcp
```

Cualquier otro cliente que lea JSON:

```json
{
  "mcpServers": {
    "dfemu": {
      "command": "python",
      "args": ["-m", "emulator.cli", "mcp"],
      "cwd": "C:/ruta/a/dataflow-local"
    }
  }
}
```

El servidor hereda el entorno: usa el contexto de la CLI de Qlik y `dfemu.local.json`, igual que el
resto de comandos. Sin esos datos responde a las herramientas locales (guía, catálogo, traducción,
búsqueda en la documentación) y falla con un mensaje claro en las que hablan con el tenant.

## Herramientas

Cuarenta, agrupadas por área (la tabla la genera `dfemu mcp --markdown` desde el registro).
La primera llamada debería ser `dfemu_guide`.

<!-- herramientas:inicio -->
<!-- herramientas:inicio -->
| Herramienta | Riesgo | Para qué |
| --- | --- | --- |
| `dfemu_automation_copy` | write | Duplica una automatizacion emu_ con otro nombre emu_. |
| `dfemu_automation_create` | write | Crea una automatizacion emu_. |
| `dfemu_automation_delete` | destructive | Borra una automatizacion emu_ (exige confirm y permiso). |
| `dfemu_automation_run` | execute | Ejecuta una automatizacion emu_ (exige confirm). |
| `dfemu_automation_runs` | read | Ejecuciones de una automatizacion. |
| `dfemu_automation_set_enabled` | write | Habilita o deshabilita una automatizacion emu_. |
| `dfemu_automation_show` | read | Definicion completa de una automatizacion. |
| `dfemu_automation_stop` | execute | Para una ejecucion en curso (exige confirm). |
| `dfemu_automation_update` | write | Cambia nombre o descripcion de una automatizacion emu_. |
| `dfemu_battery_cases` | read | Casos de la bateria de processors. |
| `dfemu_battery_run` | execute | Mide un caso de la bateria contra el tenant (exige confirm). |
| `dfemu_compare` | execute | Compara el emulador con el tenant para un .dfw (exige confirm). |
| `dfemu_coverage` | read | Corre el emulador sobre los samples y resume qué ejecuta y qué no. |
| `dfemu_docs_check` | read | Comprueba que la documentación de help.qlik.com esté completa (docsync --check). |
| `dfemu_docs_search` | read | Busca texto en la documentacion descargada de help.qlik.com. |
| `dfemu_emulate` | read | Ejecuta un .dfw en el emulador local y resume lo escrito. |
| `dfemu_flow_add_node` | write | Inserta un processor tras un nodo y sube el grafo (acepta el tipo o el nombre de la paleta). `feed` conecta entradas extra: {LOOKUP: 'filtro:REJECT'} (obligatoria en map-fields). |
| `dfemu_flow_add_source` | write | Registra un dataset del catalogo como fuente del flujo y añade su nodo (el datasetId y el qri salen de v1/items; el conector se copia de una fuente existente). |
| `dfemu_flow_backup` | read | Guarda el .dfw actual en out/backups y devuelve la ruta. |
| `dfemu_flow_clone` | write | Clona un flujo base en un flujo emu_ nuevo. |
| `dfemu_flow_create` | write | Crea un flujo desde cero (app nueva, no copia): una fuente por dataset y un destino; la plantilla del destino se copia de `base` (shortcut). |
| `dfemu_flow_delete` | destructive | Borra un flujo emu_ (exige confirm y permiso). |
| `dfemu_flow_get` | read | Grafo de un flujo: resumen de nodos o el .dfw completo. |
| `dfemu_flow_list` | read | Flujos visibles y cuales llevan prefijo emu_. |
| `dfemu_flow_push` | write | Sube un grafo a un clon emu_ del flujo base. |
| `dfemu_flow_reload` | execute | Recarga un flujo emu_ y sigue el estado hasta el final (exige confirm). |
| `dfemu_flow_remove_node` | write | Quita un nodo y reconecta sus aristas. |
| `dfemu_flow_restore` | write | Sube un grafo guardado (backup) a un flujo emu_. |
| `dfemu_flow_set_node` | write | Mezcla configuracion en un nodo existente. |
| `dfemu_guide` | read | Mapa de tareas: por donde empezar y en que orden usar el resto. |
| `dfemu_processor_definition` | read | Definición del servidor para un processor: configuración inicial y puertos. |
| `dfemu_processors` | read | Catalogo de processors y que casos tienen medidos. |
| `dfemu_script_get` | read | Script de Qlik actual de una app emu_. |
| `dfemu_script_set` | write | Sube un script de Qlik a una app emu_ (texto o archivo). |
| `dfemu_script_translate` | read | Traduce un script de Qlik a SQL de DuckDB. |
| `dfemu_script_validate` | read | Pide al servidor que valide un script (no escribe). |
| `dfemu_status` | read | Que objetos emu_ hay ahora en el espacio de pruebas. |
| `dfemu_task_delete` | destructive | Borra una tarea de recarga (exige confirm y permiso). |
| `dfemu_task_list` | read | Tareas de recarga programadas de una app emu_. |
| `dfemu_task_schedule` | write | Programa una recarga con una regla RRULE. |
| `dfemu_task_set_enabled` | write | Habilita o deshabilita una tarea. |
| `dfemu_task_start` | execute | Arranca una tarea habilitada (exige confirm). |
<!-- herramientas:fin -->
<!-- herramientas:fin -->
<!-- herramientas:fin -->
<!-- herramientas:fin -->



## Recursos y prompts

Además de herramientas, el servidor publica las dos capacidades que un cliente sabe usar:

- **Recursos** (`resources/list` y `resources/read`): los documentos que hacen falta para trabajar aquí —
  catálogo del MCP, hallazgos medidos de la API, cobertura de script, la skill del proyecto y el README — como
  `dfemu://docs/mcp`, `dfemu://docs/hallazgos`, `dfemu://docs/cobertura-script`, `dfemu://skill/dfemu`,
  `dfemu://readme`. Se truncan a 400 000 caracteres para no inflar el mensaje.
- **Prompts** (`prompts/list` y `prompts/get`): recetas listas para lanzar — `crear-dataflow`, `medir-processor`,
  `capturar-interfaz` y `recargar-app`. Cada una dice la secuencia de herramientas y lo que **no** se puede hacer
  por API, para que el asistente no invente cuerpos.
- **Progreso** (`notifications/progress`): si la llamada trae `_meta.progressToken`, las herramientas largas
  (`dfemu_flow_reload`, `dfemu_automation_run`, `dfemu_compare`) avisan del paso en el que están.

## Permisos

El permiso lo aplica el servidor, no el asistente:

| Riesgo | Por defecto | Cómo cambiarlo |
| --- | --- | --- |
| `read` | permitido | — |
| `write` | permitido | `DFEMU_MCP_ALLOW_WRITE=0` |
| `execute` | permitido, con `confirm: true` | `DFEMU_MCP_ALLOW_EXECUTE=0` |
| `destructive` | **bloqueado** | `DFEMU_MCP_ALLOW_DESTRUCTIVE=1`, y aun así exige `confirm: true` |

Para enseñar el flujo sin escribir nada: `DFEMU_MCP_APPLY=0` convierte toda escritura en un simulacro que
responde qué petición habría hecho (el mismo `DryRun` del CLI).

Además, toda escritura se limita a objetos `emu_*`: el nombre se comprueba en el servidor antes de
tocar el tenant, así que un `dfemu_flow_push` con nombre `produccion` se rechaza sin llamar a la API.
Es la misma regla de `CLAUDE.md`, aplicada aquí en código y con prueba propia.

## Auditoría

Cada llamada deja una línea en `.dfemu-mcp/audit.jsonl` (ignorado por git) con fecha, herramienta,
riesgo, resultado y duración. **Nunca** los argumentos: un script o una ruta pueden llevar datos del
tenant. `DFEMU_MCP_STATE_DIR` cambia la carpeta.

## Skill del proyecto

El repo trae una skill en `.agents/skills/dfemu/SKILL.md` (la que descubre Vibe en este proyecto). Es el mapa
que necesita un asistente: qué comando sirve para cada tarea, la regla de escribir solo en `emu_` con `--apply`,
el orden de intentos cuando la API no deja crear un nodo y cómo comprobar que un cambio está medido.
`tests/test_skill.py` comprueba que su frontmatter es válido, que los comandos que documenta existen y que los
documentos que enlaza están en el repo, así que no se puede quedar desfasada en silencio.

Claude Code lee `.claude/skills/`: para usarla ahí, copia o enlaza la carpeta.

```bash
cp -r .agents/skills/dfemu .claude/skills/dfemu          # Linux/macOS
mklink /D .claude\skills\dfemu .agents\skills\dfemu     # Windows (cmd)
```

## Capturar lo que manda la interfaz

Hay cuerpos que la API no explica (`pivot`, `map-fields`, `subflow`, nodo `script`, `datasources`, import/export
de `.dfw`: responden `ADF-500` o un 500 sin detalle). Cuando haga falta uno, se graba de la pestaña abierta:

```bash
playwright-cli attach --cdp=chrome     # sesión `chrome` (o DFEMU_BROWSER_SESSION)
dfemu flow capture start               # instala el grabador en la pestaña de Qlik Cloud
# ... la acción en la interfaz ...
dfemu flow capture dump --only dataflows --save out/captures/pivot.json
```

`dump` imprime método, ruta sin host, estado y tamaños; con `--save` guarda los cuerpos completos. Es la única
vía que queda para esos nodos, y por eso está a un comando en vez de en un script suelto.

## Límites conocidos

- `pivot`, `map-fields`, `subflow` y el nodo `script` no se pueden crear por API en este tenant; para
  esos está `dfemu flow types` / `dfemu flow add` sobre la sesión de Chrome ya iniciada.
- Las herramientas que hablan con el tenant dependen de la configuración de `dfemu setup`: sin
  contexto de la CLI de Qlik devuelven el error del Bridge tal cual, sin reintentos.
- `dfemu_battery_run` escribe objetos `emu_` temporales y los borra al terminar; cuesta una ejecución
  en Qlik Cloud por caso.

## Qué está probado

`tests/test_mcp.py` (28 pruebas, sin tenant ni red, con un Bridge falso): handshake `initialize`,
`tools/list` con esquemas válidos, notificaciones sin respuesta, JSON roto, errores de método
desconocido y herramienta desconocida, límite `emu_`, cada permiso por separado, que el clon se borra
siempre (`DELETE` presente), y que la auditoría no guarda argumentos. Además se arranca el servidor por
stdio (`python -m emulator.cli mcp`) con `initialize` y `dfemu_guide` reales.
