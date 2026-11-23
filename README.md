# dataflow-local

Banco de pruebas local para los Data Flows de Qlik Cloud: valida, emula y compara flujos (`.dfw`) y traduce su script de Qlik a SQL. Diseño en `docs/superpowers/specs/`, hallazgos de la API en `docs/banco-de-pruebas/`.

## Primeros pasos

Requisitos: Python 3.12 y acceso a un tenant de Qlik Cloud con una API key.

```
pip install -r requirements.txt
python -m emulator.cli setup
```

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

## Desarrollo

- `python -m pytest` corre todo sin tenant ni red. `tests/conftest.py` fija ids de relleno aunque exista `dfemu.local.json`; con `DFEMU_TENANT=1` usa los ids reales y activa las pruebas contra el tenant.
- Los `.dfw` de `samples/` tienen ids desidentificados: sirven para validar y emular en local, no se pueden subir al tenant. Para eso se usan los grafos descargados con `dfemu pull` en `out/` (ignorado por git).
- `dfemu translate SCRIPT --compare --apply` ejecuta un script de Qlik en el tenant y lo compara con su traducción local a SQL.
- `python scripts/processor_battery.py` ejecuta 65 casos (54 processors y 11 cadenas) en el emulador y en el tenant y compara los resultados (escribe en el tenant y limpia lo que crea). Es la prueba que más ha corregido al emulador: ver el apartado 9 quater del documento de hallazgos.
- Los objetos creados en el tenant llevan el prefijo `emu_`; `dfemu cleanup --apply` borra apps y archivos `emu_` de `DataFiles`. Los archivos escritos en carpetas de Google Drive no los ve.
