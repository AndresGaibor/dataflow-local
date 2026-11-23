# dataflow-local: reglas del proyecto

Banco de pruebas para los Data Flows de Qlik Cloud (emulador, comparador, traductor de scripts). Lo medido contra el tenant está en `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`; empezar por ahí, no repetir pruebas ya hechas.

## Seguridad (repositorio público)
- El tenant solo se escribe a través de `Bridge` y solo sobre objetos `emu_*` del espacio de pruebas. Nada que no empiece por `emu_` se modifica ni se borra. Las escrituras exigen `--apply`; sin él, simulan.
- Nunca imprimir ni guardar credenciales. No usar `qlik ... --verbose` (imprime el token). La API key vive solo en el contexto de la CLI; los secretos se piden con `getpass`, no por el chat ni por línea de comandos.
- Antes de cada `push`, buscar en lo que sale: claves/JWT, el host del tenant y los ids del espacio y de los flujos. **No se hace `push` sin que el usuario lo pida**; se commitea en local y se pregunta.
- `out/`, `dfemu.local.json`, `connections.local.json` y `.tools/` están ignorados por git y pueden contener datos reales. Los `samples/*.dfw` están desidentificados y no se pueden subir al tenant.

## Cómo trabajar
- Primero la prueba, luego el código. Comportamiento de Qlik: **medirlo en el tenant antes de afirmarlo**, y documentarlo en el apartado 9 quater. Una conclusión sacada de datos que ya venían ordenados fue falsa una vez (orden del `JOIN`).
- Si falta algo en el tenant, hacerlo por API o con el JSON del grafo; no pedirle al usuario que lo cree en la interfaz.
- La batería contra el tenant (`scripts/processor_battery.py`) escribe en el tenant y tarda: lanzarla por tandas de 6 a 12 casos y en segundo plano. Si el sistema la corta por memoria, limpiar (`dfemu cleanup --apply`) y no relanzarla sin que se pida. Errores transitorios del tenant (`RELOADS-010`, `GENERIC ABORTED`): reintentar el caso.
- Windows: la CLI de Qlik funciona con el binario firmado (ver `dfemu setup` y 10 bis); Git Bash no puede ejecutar el acceso directo de Chocolatey. Al escribir archivos con barras invertidas o saltos de línea dentro de cadenas, usar las herramientas de edición, no `python - <<EOF` con `\\n`: el escapado los corrompe.

## Recetas aprendidas (detalle en los documentos)
- **`calculate-fields` por API**: un nodo nuevo sale `INVALID` (`POTENTIAL_STALE_EXPRESSION`); un `PUT` idéntico lo limpia y cada nivel encadenado necesita uno más. `Remote.push_graph` ya lo hace (tope `MAX_STALE_PUTS`).
- **Nodo `script`**: no se puede crear desde cero (el `schemaEntityId` lo crea la interfaz con rutas `POST` bloqueadas). Se reutiliza el de una copia con `dfemu script-node`; el script nuevo debe declarar la tabla de salida registrada en el nodo, o el servidor da `VALID` y falla al ejecutar. El emulador no ejecuta `script`: se verifica con `dfemu translate --compare`.
- **Descubrir la configuración JSON de un processor**: con `{}` el servidor responde `VALUE_MISSING_ON_REQUIRED_FIELD` con `parameters.attributePath`; rellenar y repetir. Ignora las claves desconocidas, pero un enum inválido lista sus valores. `unpivot` se crea así; `pivot` exige un `schemaEntityId` de la interfaz (no se verificó). `scripts/discover_config.py` automatiza el método; con el `type` y sin el objeto `xxxConfiguration` el servidor da un `500` sin detalle, y algunas variantes (`ROUND`, `FLOOR`, `CUT`...) dan `500` aunque se rellene todo: no hay forma de descubrirlas sin un ejemplo de la interfaz.
- **Subflows**: clonar copia sus subflows con ids nuevos; reescribir el `dataflowId` de cada nodo antes del `PUT` (`Remote._with_clone_subflows`, `--base-app`).
- **Fuentes**: el `entityId` de un nodo fuente es propio de cada flujo; un grafo nuevo solo puede reutilizar las fuentes del flujo base clonado.
- **Import/export de `.dfw`**: las rutas son `v1/dataflow-apps/...`; el id del archivo subido a `temp-contents` viaja en una cabecera que `qlik raw` no muestra. No hace falta OAuth; la vía que se usa es clonar y reemplazar el grafo.
- **El oráculo recarga el CSV escrito**: en Qlik un archivo no tiene `NULL`; una celda vacía es un valor (`''`). La huella local se mide igual. Orden y formato se comparan en las 8 primeras filas, salvo `HASH_DATA` (no usa `md5`) y los joins (su orden no es reproducible: se comparan por contenido).
- **Tareas**: `dfemu task`; una tarea deshabilitada no se puede arrancar (`CHO-012`); solo arranca si todo `STORE` del script escribe en un archivo `emu_*`.
