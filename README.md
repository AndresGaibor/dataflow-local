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

## Qué cubre y qué no

`dfemu coverage` mide, sobre los `.dfw` de `samples/`, qué processors se usan y qué flujos puede ejecutar el emulador. Con `--stub` las fuentes de base de datos (BigQuery, PostgreSQL...) se sirven con 20 filas enteras de relleno para ver si el resto del flujo ejecuta; como el `.dfw` desidentificado no trae tipos, un error de tipos se marca `no concluyente` y no como fallo. Los límites conocidos están en el apartado 12 del documento de hallazgos: variantes de processors que el servidor no deja descubrir, `pivot` (no se puede crear por API), el nodo `script` (solo se traduce) y la comparación de orden en joins.

**Coste:** cada ejecución en el tenant cuesta. No hace falta repetir la batería contra Qlik Cloud para usar el emulador: lo verificado está en el apartado 9 quater, y las pruebas locales (`python -m pytest`) no tocan la red. Si se añade un caso nuevo, se mide solo ese, con pocas filas.

## Desarrollo

- `python -m pytest` corre todo sin tenant ni red. `tests/conftest.py` fija ids de relleno aunque exista `dfemu.local.json`; con `DFEMU_TENANT=1` usa los ids reales y activa las pruebas contra el tenant.
- `python scripts/docsync.py` replica la documentación de Qlik Cloud desde `help.qlik.com` (sitemap `cloud-services_en-US`, ~3.000 páginas): escribe `docs/<sección>/**.md` con frontmatter (`source_url`, `version`, `last_updated`, `sha256`), baja las imágenes a `docs/_images/` (ignorado por git) y deja `docs/manifest.json`. Es idempotente: `--check` falla si falta una página o una imagen, `--prune` borra los `.md` que ya no están en el sitemap y `--list` lista las familias disponibles. La documentación de Qlik Automate queda en `docs/Automate/`.
- Los `.dfw` de `samples/` tienen ids desidentificados: sirven para validar y emular en local, no se pueden subir al tenant. Para eso se usan los grafos descargados con `dfemu pull` en `out/` (ignorado por git).
- `dfemu automate ls|show|new|set|rm|enable|disable|copy|run|runs` controla Qlik Automate por API (`api/workflows/automations`, la ruta vigente): las escrituras solo sobre automatizaciones `emu_*` del espacio de pruebas y con `--apply`; `new` acepta `--workspace archivo.json` con los bloques del editor.
- `dfemu script get APP` / `dfemu script set APP FILE --apply` / `dfemu script validate FILE` leen, escriben y validan el script de una app (las escrituras solo en apps `emu_` y con `--apply`; `validate` no escribe).
- `dfemu script-node` crea un nodo `script` por API (reutilizando el de una copia de un flujo que ya los tiene) y guarda el script que genera Qlik, para verificarlo con `dfemu translate --compare`. Las reglas de trabajo del proyecto están en `CLAUDE.md`.
- `dfemu translate SCRIPT --compare --apply` ejecuta un script de Qlik en el tenant y lo compara con su traducción local a SQL.
- `python scripts/script_inventory.py --write` mide qué constructs de Qlik script aparecen en el corpus (`out/**/*.pull.json`, `samples/`) y cuáles cubre el traductor; deja la tabla en `docs/banco-de-pruebas/05-cobertura-script.md`. Un nodo de script es un fragmento con `RESIDENT` de tablas que crea otro nodo, así que la cobertura se mide contra lo que el traductor conoce, no traduciendo cada fragmento suelto.
- `python scripts/e2e_ventas.py [--escenario ventas|calidad|normalizacion] [--local]` ejecuta un flujo de varios nodos (por omision `ventas`: clientes + cuentas, 12 nodos; `normalizacion` y `calidad`: datos sucios de 20 filas, sin editor) en el emulador y en el tenant y compara (`--local`: solo emulador; la primera vez hay que registrar las fuentes en el editor, ver 9 quater).
- `python scripts/processor_battery.py [CASO ...]` ejecuta los casos indicados (o los 129) en el emulador y en el tenant y compara los resultados (escribe en el tenant, cuesta, y limpia lo que crea; lanzar solo los casos nuevos). Es la prueba que más ha corregido al emulador: ver el apartado 9 quater del documento de hallazgos.
- Los objetos creados en el tenant llevan el prefijo `emu_`; `dfemu cleanup --apply` borra apps y archivos `emu_` de `DataFiles`. Los archivos escritos en carpetas de Google Drive no los ve.

## Cobertura

<!-- cobertura:inicio -->
| cobertura de Qlik script | valor |
| --- | --- |
| scripts en el corpus | 8 |
| constructs distintos | 13 |
| sin cubrir | 0 |
| cubiertos sin medir en el tenant | 5 |
<!-- cobertura:fin -->
