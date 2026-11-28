# dataflow-local

Banco de pruebas local para los Data Flows de Qlik Cloud: valida, emula y compara flujos (`.dfw`) y traduce su script de Qlik a SQL. Diseño en `docs/superpowers/specs/`, hallazgos de la API en `docs/banco-de-pruebas/`.

## Primeros pasos

Requisitos: Python 3.11 o superior (se prueba con 3.12; el mínimo lo fija DuckDB 2). Para solo emular y traducir en local no hace falta tenant; para comparar contra Qlik Cloud hace falta una API key.

```
pip install -e .          # instala el comando `dfemu` (o: pip install -r requirements.txt y usar python -m emulator.cli)
dfemu setup
```

Todo lo que aparece abajo como `python -m emulator.cli X` también se puede escribir `dfemu X`. El proyecto se instala en modo editable: las rutas (`data/`, `samples/`, `dfemu.local.json`) son las de este repositorio.

`setup` deja todo listo y pide solo lo que falta:

1. **CLI de Qlik.** Si no hay una `qlik` que funcione, ofrece descargar la versión 4.0.0 oficial de `github.com/qlik-oss/qlik-cli` en `.tools/qlik/`, verificando su SHA-256 contra el archivo de checksums del release. Con `--yes` no pregunta. En Windows con una política de control de aplicaciones puede hacer falta un `qlik.exe` firmado: ver el apartado 10 bis de `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`.
2. **Contexto y API key.** Si la CLI no autentica, pide la URL del tenant y la API key (se escribe sin mostrarse) y crea el contexto. Para generar la clave: Qlik Cloud, perfil, Configuración, Claves de API (el administrador debe haberlas habilitado). La clave **solo se guarda en el contexto de la CLI** (carpeta `.qlik` de tu usuario), nunca en este repositorio; mientras corre `qlik context create` es visible en la lista de procesos de tu equipo. Si se filtra, revócala en el tenant y ejecuta `setup` otra vez.
3. **Espacio y flujo base.** Lista los espacios y los flujos del tenant para que elijas dónde puede escribir el banco de pruebas (solo objetos `emu_`) y qué flujo se clona. Se guarda en `dfemu.local.json`, que git ignora. Se pueden pasar `--space` y `--base-app` para no preguntar.

Ejecutarlo de nuevo es seguro: lo que ya funciona se salta.

Después, `python -m emulator.cli --help` lista los comandos; los que escriben en el tenant simulan salvo que se pase `--apply`. Las pruebas locales (`python -m pytest`) no necesitan tenant ni red.

- Para crear un cliente OAuth (opcional, solo si se quiere probar `import`/`export` de `.dfw`): `docs/banco-de-pruebas/02-guia-oauth.md`.

## Orquestación

`python -m emulator.cli task` programa, encadena, arranca y borra tareas de recarga con la API `scheduling` de Qlik. Solo actúa sobre apps `emu_` del espacio de pruebas, y una tarea no arranca si su script escribe en un archivo que no sea `emu_`. Ejemplo:

```
python -m emulator.cli task schedule APP --name emu_diaria --recurrence "RRULE:FREQ=DAILY;BYHOUR=3;BYMINUTE=0;BYSECOND=0" --timezone America/Bogota --enable --apply
python -m emulator.cli task chain OTRA_APP --name emu_despues --after ID_TAREA --on succeeded --enable --apply
python -m emulator.cli task runs ID_TAREA
python -m emulator.cli task enable ID_TAREA --apply   # una tarea deshabilitada no se puede arrancar
```

Sin `--apply` solo simula. Detalles y trampas (tareas deshabilitadas, destinos de Google Drive) en el apartado 10 ter del documento de hallazgos.

`python -m emulator.cli reload APP` recarga una app `emu_` (acepta el id o el nombre del flujo) y sigue el estado `QUEUED → RELOADING → SUCCEEDED/FAILED`, mostrando la linea util del log cuando falla. Igual que el resto, simula sin `--apply`.

## Asistente (MCP)

`dfemu mcp` es un servidor [MCP](https://modelcontextprotocol.io/) en stdio: un asistente lista flujos, lee el
grafo, traduce scripts, mide un caso de la batería y crea automatizaciones sin adivinar comandos. El permiso
lo aplica el servidor: leer siempre, escribir con `DFEMU_MCP_ALLOW_WRITE=0` para apagarlo, ejecutar con
`confirm: true`, borrar bloqueado salvo `DFEMU_MCP_ALLOW_DESTRUCTIVE=1`. Toda escritura se limita a objetos
`emu_*` y cada llamada queda en `.dfemu-mcp/audit.jsonl` (herramienta, riesgo y resultado; nunca los
argumentos). Catálogo de herramientas y cómo registrarlo: [docs/MCP.md](docs/MCP.md); `dfemu mcp --list`. El repo incluye además la skill `.agents/skills/dfemu/SKILL.md` con el mapa de tareas, y
`dfemu flow capture` para grabar los cuerpos que solo manda la interfaz (`pivot`, `datasources`, import/export).
El servidor publica además recursos (documentación y hallazgos), prompts con recetas y notificaciones de progreso.

## Qué cubre y qué no

`dfemu coverage` mide, sobre los `.dfw` de `samples/`, qué processors se usan y qué flujos puede ejecutar el emulador. Con `--stub` las fuentes de base de datos (BigQuery, PostgreSQL...) se sirven con 20 filas enteras de relleno para ver si el resto del flujo ejecuta; como el `.dfw` desidentificado no trae tipos, un error de tipos se marca `no concluyente` y no como fallo. Los límites conocidos están en el apartado 12 del documento de hallazgos: variantes de processors que el servidor no deja descubrir, `pivot` (no se puede crear por API), el nodo `script` (solo se traduce) y la comparación de orden en joins.

**Coste:** cada ejecución en el tenant cuesta. No hace falta repetir la batería contra Qlik Cloud para usar el emulador: lo verificado está en el apartado 9 quater, y las pruebas locales (`python -m pytest`) no tocan la red. Si se añade un caso nuevo, se mide solo ese, con pocas filas.

## Desarrollo

- `python scripts/test_coverage.py` corre las pruebas con `pytest-cov` y publica la cifra en el bloque
  `<!-- tests:inicio -->
| cobertura de pruebas | valor |
| --- | --- |
| lineas de `emulator/` | 82.7 % |
| lineas cubiertas | 3131 de 3786 |
| modulos con menos cobertura | `flowctl.py` (53.5 %), `__init__.py` (69.2 %), `uictl.py` (76.7 %) |
<!-- tests:fin -->
