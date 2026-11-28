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

Diecisiete, agrupadas por área. La primera llamada debería ser `dfemu_guide`.

| Herramienta | Riesgo | Para qué |
| --- | --- | --- |
| `dfemu_guide` | read | Mapa de tareas por área (`overview`, `dataflow`, `script`, `automate`, `docs`, `battery`). |
| `dfemu_status` | read | Objetos `emu_` del espacio de pruebas: flujos, archivos y automatizaciones. |
| `dfemu_flow_list` | read | Flujos visibles y cuáles llevan prefijo `emu_`. |
| `dfemu_flow_get` | read | `summary` (nodos en una línea) o `graph` (el `.dfw` completo). |
| `dfemu_processors` | read | Los 24 processors del catálogo y cuáles tienen caso medido. |
| `dfemu_script_translate` | read | Script de Qlik → SQL de DuckDB, con lo que no entendió. |
| `dfemu_docs_search` | read | Busca texto en el corpus de `help.qlik.com` ya descargado. |
| `dfemu_battery_cases` | read | Casos de la batería de processors. |
| `dfemu_flow_push` | write | Sube un grafo a un clon `emu_` del flujo base y devuelve la validez del servidor. |
| `dfemu_automation_create` | write | Crea una automatización `emu_`. |
| `dfemu_automation_set_enabled` | write | Habilita o deshabilita una automatización `emu_`. |
| `dfemu_automation_runs` | read | Ejecuciones de una automatización. |
| `dfemu_automation_run` | execute | Ejecuta una automatización (exige `confirm: true`). |
| `dfemu_battery_run` | execute | Mide un caso contra el tenant (exige `confirm: true`). |
| `dfemu_flow_reload` | execute | Recarga un flujo `emu_` y sigue el estado hasta el final (exige `confirm: true`). |
| `dfemu_flow_delete` | destructive | Borra un flujo `emu_`. |
| `dfemu_automation_delete` | destructive | Borra una automatización `emu_`. |

## Permisos

El permiso lo aplica el servidor, no el asistente:

| Riesgo | Por defecto | Cómo cambiarlo |
| --- | --- | --- |
| `read` | permitido | — |
| `write` | permitido | `DFEMU_MCP_ALLOW_WRITE=0` |
| `execute` | permitido, con `confirm: true` | `DFEMU_MCP_ALLOW_EXECUTE=0` |
| `destructive` | **bloqueado** | `DFEMU_MCP_ALLOW_DESTRUCTIVE=1`, y aun así exige `confirm: true` |

Además, toda escritura se limita a objetos `emu_*`: el nombre se comprueba en el servidor antes de
tocar el tenant, así que un `dfemu_flow_push` con nombre `produccion` se rechaza sin llamar a la API.
Es la misma regla de `CLAUDE.md`, aplicada aquí en código y con prueba propia.

## Auditoría

Cada llamada deja una línea en `.dfemu-mcp/audit.jsonl` (ignorado por git) con fecha, herramienta,
riesgo, resultado y duración. **Nunca** los argumentos: un script o una ruta pueden llevar datos del
tenant. `DFEMU_MCP_STATE_DIR` cambia la carpeta.

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
