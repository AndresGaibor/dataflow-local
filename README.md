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
