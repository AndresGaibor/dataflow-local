# Hallazgos: cómo automatizar Data Flows y Qlik script contra Qlik Cloud

Documento vivo. Cada afirmación dice si fue **verificada** (ejecutada contra el tenant el 2026-11-19) o **inferida**. Todo se hizo con la CLI `qlik` v4.0.0 y su contexto ya configurado (usuario con rol `AnalyticsAdmin`, credencial tipo API key); no se usó ninguna otra credencial.

## 1. Resumen

| Necesidad | ¿Se puede? | Cómo |
|---|---|---|
| Listar Data Flows | Sí | `GET v1/items` y filtrar `resourceSubType == "dataflow-prep"` |
| **Descargar** un flujo | Sí | `GET v1/dataflows/{dataflowId}` (grafo idéntico al `.dfw` de la interfaz) |
| **Validar** con el servidor | Sí | campo `validity` al leer o al guardar |
| **Subir** un grafo local | Sí, con límites | clonar y `PUT v1/dataflows/{dataflowId}` con el grafo del `.dfw` (sección 5) |
| Importar o exportar el archivo `.dfw` completo | No con API key | `POST v1/dataflows/actions/import` y `/export` existen pero devuelven 403 |
| **Modificar** un flujo | Sí | `PUT v1/dataflows/{dataflowId}` |
| Obtener el script que Qlik genera | Sí | `GET v1/apps/{appId}/scripts/current` |
| **Ejecutar** un script | Sí | `POST v1/reloads` y sondear `GET v1/reloads/{id}` |
| **Leer el resultado con datos reales** | Sí | cargar la salida en un app y leer con `qlik app eval` / `qlik app tables` |
| Descargar el archivo de salida tal cual | No | 404/406 en todas las rutas probadas |

## 2. Autorización y reglas de seguridad

| Nivel | Qué | Estado |
|---|---|---|
| 1 | Lectura (listar, leer scripts y flujos) | Autorizado |
| 2 | `validatescript` (valida, no guarda) | Autorizado |
| 3 | Crear, clonar, modificar, ejecutar y borrar objetos `emu_` **solo en el espacio "Entrenamiento Dataflow"** | Autorizado por el usuario ("puedes hacer lo que quieras") |
| 4 | Cualquier otro espacio, o borrar objetos que no creó el banco de pruebas | Requiere confirmación explícita |

Reglas operativas (decisión del asistente, mantenidas aunque la autorización sea amplia):
- Todo objeto creado lleva el prefijo `emu_`.
- Los flujos originales no se modifican: son el juez.
- Un clon no se ejecuta sin cambiar antes su destino de salida (7.1).

## 3. Entorno verificado

- `qlik` 4.0.0 (choco), API 2026-11, un contexto activo hacia el tenant de Qlik Cloud en `us`.
- 47 Data Flows en la primera página de 100 items; 20 espacios. Los `.dfw` de `samples/` (`fundamentos`, `DF_03_TRANSACCIONES`, `normalización`...) existen también en el tenant, en "Entrenamiento Dataflow".
- Espacio de pruebas: **Entrenamiento Dataflow**, con las conexiones `DataFiles` (carpeta de archivos de Qlik) y `GDDestino` (Google Drive).

## 4. Endpoints verificados

Usar `qlik raw <método> <ruta> < /dev/null` (ver 7.2).

| Acción | Llamada | Resultado |
|---|---|---|
| Listar Data Flows | `GET v1/items?resourceType=app&limit=100` | OK. El subtipo es `dataflow-prep` (el otro repo del autor filtra `qix-df`, incorrecto aquí). |
| De app a flujo | `GET v1/dataflow-apps/{appId}` | OK. Devuelve `dataflowId`, distinto del `appId`. |
| **Descargar** | `GET v1/dataflows/{dataflowId}` | OK. Devuelve `id, name, description, graph, context, modelVersion, checksum, createdAt/By, updatedAt/By, validity`. `graph` es idéntico a `dataflow.graph` del `.dfw` de la interfaz (comparado con `samples/fundamentos.dfw`). |
| **Validar** | `validity` (`status`, `label`, `nodesConstraintViolations`) | OK. Códigos vistos: `NODE_TOPOLOGY_NOT_FULFILLED`, `POTENTIAL_STALE_EXPRESSION`. Estados: `VALID`, `INVALID`, `UNCHANGED`. |
| Script generado | `GET v1/apps/{appId}/scripts/current` | OK. Devuelve `script` y `versionMessage`. |
| **Clonar** | `POST v1/dataflow-apps/{appId}/actions/copy` con `{"name","usage":"DATAFLOW_PREP","spaceId"}` | OK. Devuelve `id`, `dataflowId`, `details`. El clon aparece en el catálogo sin `POST v1/items`. El nombre interno del flujo conserva el original. |
| **Modificar o subir grafo** | `PUT v1/dataflows/{dataflowId}` con el cuerpo completo del `GET` **sin `validity`** | OK. Devuelve el flujo con su nuevo `validity`. |
| Metadatos de una fuente | `GET v1/data-sets/{datasetId}` | OK. `sources[].datasetId` del `.dfw` es el id del data set del catálogo; `sources[].sourceId` es solo un identificador interno del flujo (no existe en el catálogo). |
| Validar script | `POST v1/apps/validatescript` con `{"script": "..."}` | OK. `Errors` y `Warnings` con línea y columna. |
| Crear app vacía | `POST v1/apps` con `{"attributes":{"name","spaceId"}}` | OK. |
| Cargar script | `qlik app script set <archivo.qvs> --app <appId>` | OK. |
| **Ejecutar** | `POST v1/reloads` con `{"appId"}`; sondear `GET v1/reloads/{id}` hasta `SUCCEEDED`/`FAILED` | OK (unos 3 s en un script pequeño). `qlik reload create --appId <id> --quiet < /dev/null` también funciona. |
| Log de ejecución | campo `log` del reload (incluye `TRACE`) | OK. |
| **Leer datos de salida** | recargar la salida en el app y usar `qlik app tables --app <id>` (filas por tabla), `qlik app eval --app <id> 'Count(id)' 'Sum(id)'` y `qlik app eval --app <id> 'Only(valor)' by id` (filas) | OK. Probado: salida de 3 filas leída completa. |
| Ubicar un archivo de salida | `GET v1/data-files?connectionId=<id DataFiles>&name=<archivo>` | OK (solo metadatos). |

## 5. Subir un `.dfw` local: lo que funciona y sus límites

Como el import de `.dfw` está cerrado a la API key, la vía verificada es: **clonar un flujo base y reemplazar su grafo** con `PUT`.

Resultados sobre clones `emu_` (cada `.dfw` se subió como grafo):

| `.dfw` | Resultado del servidor | Notas |
|---|---|---|
| `fundamentos_filtro_basico` | VALID | Qlik regeneró el script: fusionó selector de campos y filtro en un solo `LOAD ... WHERE`. |
| `fundamentos_remove_fields` | VALID | Su `sourceId` es distinto al del clon: no hace falta registrar las fuentes. |
| `synthetic/s05_fork_union` | INVALID (aceptado) | Sus fuentes sintéticas no existen en el tenant. Nuestro validador local lo da por válido: no ve fuentes inexistentes. |
| `DF_03_TRANSACCIONES` | INVALID (aceptado) | **Después deja el clon inservible** (7.3). |

Consecuencia: para cualquier `.dfw` local se puede obtener (a) el veredicto real y (b) el script que Qlik genera, en dos llamadas. En una primera tanda (antes del daño del clon) tres flujos reales (`Ajustes Rotativos`, `Ajustes Rotativos(Anual)`, `Copia de Ventas Mensuales (Julio) (1)`) dieron INVALID (1 violación) y nuestro validador VÁLIDO; no es concluyente porque se subieron a un clon sin sus fuentes ni subflows.

No se obtuvo cómo leer `sources`, `subflows`, `projections` ni `schemas` por rutas de `v1/dataflows/{id}/...` (404). Para armar un `.dfw` completo, `sources` se puede reconstruir desde `v1/data-sets/{datasetId}`; `projections` y `schemas` vienen vacíos en todos los ejemplos.

## 6. Paridad entre el validador del servidor y `emulator/dfw.py`

Método: se muta una copia de `samples/fundamentos.dfw`, se sube el grafo a un clon con `PUT` y se lee `validity`; la misma mutación pasa por `dfw.validate`. Las mutaciones y sus nombres están en `emulator/calibrate.py`. Medido el 2026-11-19 contra el tenant.

| mutación | servidor | emulador antes | emulador ahora |
|---|---|---|---|
| `sin_aristas` | INVALID | INVALID | INVALID |
| `target_sin_fileName` | INVALID | INVALID | INVALID |
| `target_sin_extension` | INVALID | INVALID | INVALID |
| `formato_xlsx` | VALID | VALID | VALID |
| `formato_invalido` (`"zzz"`) | VALID | INVALID | VALID |
| `sin_target` | INVALID | INVALID | INVALID |
| `sin_source` | REJECTED | INVALID | INVALID |
| `processor_sin_configurar` (`$state: UNCONFIGURED`) | VALID | INVALID | VALID |
| `selectors_vacios` | INVALID | VALID | INVALID |
| `ids_duplicados` | REJECTED | INVALID | INVALID |

Conclusión:

- El servidor tiene dos capas. Un rechazo estructural (`REJECTED`: error HTTP `DATAFLOW_STRUCTURAL_ERROR` en el `PUT`, p. ej. ciclos, ids duplicados o fuente eliminada) y el campo `validity` (`INVALID`). Solo `INVALID` cuenta como inválido en la tabla, pero `REJECTED` también lo es.
- El servidor no valida el valor de `format` del target ni un `$state` aislado. El emulador tampoco los comprueba ahora, por eso `TARGET_FORMATS` y la regla de `$state` se eliminaron. Un valor de `format` que el emulador no escribe se rechaza al ejecutar, no al validar.
- `GHOST_SOURCE` (una fuente que no existe en el tenant) es solo remoto: el validador local no puede verlo sin conexión y no lo replica.

## 7. Trampas

1. **Un clon escribe en el mismo destino que el original.** Verificado: el `STORE` del script de un clon de `fundamentos` apunta a la misma ruta de `GDDestino` (Google Drive) que el original. Ejecutar un clon sobrescribiría la salida original. Hay que cambiar el destino antes (por ejemplo a `DataFiles` con prefijo `emu_`).
2. **Los cuelgues de la CLI se deben a stdin.** `qlik item ls --limit 10` y `qlik reload create` se quedaban esperando; con `< /dev/null` ambos responden al instante. Regla: ejecutar siempre `qlik ... < /dev/null`.
3. **Subir un grafo con subflows daña el clon.** Tras subir `DF_03_TRANSACCIONES`, todo `PUT` posterior falla con `SUBFLOW_CREATION_ERROR: Resource conflict. Expected ID <clon>, but got <otro id>`, incluso con el grafo original. Un clon dañado se descarta (borrar y clonar de nuevo). Un clon por cada subida con subflows.
4. **`PUT` exige el cuerpo completo menos `validity`.** `PATCH` da 405; sin `id` o sin `createdAt` da error estructural; el cuerpo del `GET` tal cual y solo `{name,description,graph}` dan 500.
5. El servidor **acepta** grafos inválidos y solo marca `INVALID`; no los rechaza.
6. Los scripts del tenant llevan `μ`: la consola de Windows (cp1252) falla al imprimirlos; usar `sys.stdout.reconfigure(encoding="utf-8")`.
7. Los datos salen de una sola página de 100 items; puede haber más flujos.

## 8. Cómo comparar resultados

Se descartó descargar el archivo (404/406). Camino verificado:
1. Tomar el script que Qlik genera (`scripts/current`) o el propio.
2. Cambiar los `STORE` hacia `lib://Entrenamiento Dataflow:DataFiles/emu_*.csv` y añadir, al final, un `LOAD` del archivo escrito, sin borrarlo.
3. Ejecutar con `POST v1/reloads`.
4. Leer con `qlik app tables` (filas), `qlik app eval` (agregados) y `qlik app eval ... by <clave>` (filas completas).
5. Comparar con lo que calcula el emulador sobre el mismo resultado.

El script de Qlik no es una traducción 1 a 1 del grafo (fusiona nodos), por eso la comparación es de **resultados**, no de texto.

Dos diferencias del emulador frente a Qlik, corregidas el 2026-11-19 y verificadas con `dfemu compare` sobre `fundamentos` (500 filas, 7 columnas, sin diferencias):
1. Qlik recorta los espacios de los textos al leer un CSV; el emulador ahora también (`runner._source`). En `clientes.csv`, `ciudad` pasa de 36 valores distintos a 29, que es lo que ve Qlik.
2. Qlik suma las fechas como números y el emulador no calcula suma para columnas de fecha. El comparador ya no compara la suma cuando solo un lado la tiene.

## 9. Seguridad

Ninguna credencial del tenant vive en este repo: la CLI `qlik` usa su propio contexto y el emulador solo toma de `DFEMU_SPACE_ID` y `DFEMU_BASE_APP` el espacio y el flujo base. Los `.dfw` de `samples/` están desidentificados con `scripts/deidentify.py`.

## 9 bis. Cobertura del corpus

`dfemu coverage` sobre los 29 `.dfw` de `samples/` da `ejecuta=6`, `requiere conexion=11`, `borrador=11`, `solo tenant=1`. Los processors usados en el corpus se emulan todos salvo `script`, que solo se ejecuta en el tenant. Fuera del corpus quedan sin emulación `pivot`, `unpivot`, `map-fields` y `clear-cells`: no hay ningún `.dfw` real que los use, así que no se inventó su configuración.

Variantes reales añadidas el 2026-11-19 tras revisar los 18 flujos del tenant: `strings.UPPERCASE`, `REPLACE_ON_VALUE` con `STARTS_WITH` y `REPLACE_CELL_WITH_VALUE` con `EQUALS`.

## 9 ter. Traductor de script

Cada sentencia con nombre es una tabla; `RESIDENT [T]` lee otra tabla del script; `LEFT|INNER|RIGHT|OUTER JOIN([T])` (sin tipo = outer, como Qlik) une por los campos en común y falla si no hay; `GROUP BY` solo con campos simples. Expresiones: `Upper`, `Trim`, `Year`, `Month`, `IsNull`, `Coalesce`, `If` y condiciones simples; agregaciones `Sum`, `Avg`, `Min`, `Max`, `Count` y `Count(DISTINCT ...)`. `SET`, `TRACE`, `STORE` y `DROP TABLE` se ignoran (el `STORE` fija la tabla de salida). Los textos se recortan al leer el CSV, como en Qlik. Todo lo demás se marca no traducible; nunca se pasa SQL crudo.

Medición el 2026-11-23 sobre los 18 scripts distintos de `out/corpus*/`: 3 se traducen (los de `fundamentos`, con huellas iguales al emulador sobre `data/practica`). Los otros 15: 10 cargan desde BigQuery o Postgres con `LIB CONNECT` y `SELECT` (necesitan conexión), 3 son flujos inválidos (`throw`), 1 lee un `.xlsx` y 1 no carga ninguna tabla. **Verificado contra el tenant el 2026-11-23** con `dfemu translate script --compare --apply` (ejecuta el script en una app `emu_oracle_*`, compara huellas con la traducción local y limpia): un flujo `clientes` → fork → field-selector → join (LEFT OUTER, autounión por `cliente_id`) → aggregate por `segmento`. El servidor generó `RESIDENT` y `LEFT JOIN([T])`; filas, `Count` y `Sum` coinciden con la traducción, y una variante con `Avg`, `Min`, `Max` y una resta da `OK: sin diferencias`. Comportamiento de Qlik medido y reproducido en la traducción: `Sum` de solo nulos o de texto da 0; `Avg` de solo nulos da nulo; `Count` cuenta también los textos. El script real del servidor quedó como fixture en `tests/fixtures/join_agg.qvs`.

**Divergencia conocida:** `Avg` sobre valores grandes (aquí ~1,7·10⁹) sale cuantizado en el modelo de Qlik (el texto es `1.7000002e+09`; 4 promedios distintos pasan a 2 valores y su suma cambia en el noveno dígito). `dfemu` la reporta como diferencia en `distinct` y `sum` de esa columna; no es un error de la traducción. Con magnitudes pequeñas coincide.

**Limitaciones del banco de pruebas descubiertas:** el `entityId` de cada nodo fuente es propio del flujo (el mismo dataset tiene un id distinto en cada flujo), así que un grafo nuevo no puede referenciar datasets del catálogo (`GHOST_SOURCE`); solo sirve reutilizar las fuentes del flujo base clonado. Por la misma razón los `.dfw` de `samples/` (con ids desidentificados) no se pueden subir al tenant; para eso se usan los grafos descargados con `dfemu pull` en `out/`. Sin cubrir: `LIB CONNECT`, `xlsx`/`qvd`, `CONCATENATE`, `Match`, `SubField`, `Window`, varios destinos `STORE`, joins entre campos comunes de distinto tipo y `Sum`/`Avg` con parte de los valores nulos.

## 10. Objetos creados en el tenant

Todos en "Entrenamiento Dataflow", prefijo `emu_`. El 2026-11-19 la limpieza dejó el espacio sin objetos `emu_`:

```
python -m emulator.cli cleanup           # lista lo que borraría
python -m emulator.cli cleanup --apply   # borra apps y archivos emu_*
```

`cleanup` nunca toca objetos sin prefijo `emu_` ni de otro espacio. Tras ejecutarlo, una segunda pasada responde "nada que limpiar".

## 10 bis. Windows: la CLI `qlik` bloqueada por Code Integrity

**Síntoma (verificado el 2026-11-23):** `qlik` falla con "Una directiva de Control de aplicaciones bloqueó este archivo" en PowerShell y con "Permission denied" en Git Bash. El registro `Microsoft-Windows-CodeIntegrity/Operational` trae los eventos 3033 y 3077: el archivo bloqueado es `C:\ProgramData\chocolatey\bin\qlik.exe`.

**Causa:** ese archivo es un acceso directo (shim) que genera Chocolatey. No está firmado y la política WDAC de la máquina solo admite binarios con firma de nivel empresarial. El binario real, `C:\ProgramData\chocolatey\lib\qlik-cli\tools\qlik.exe`, está firmado por QlikTech International AB y sí corre (versión 4.0.0).

**Solución automática:** `emulator/bridge.py` (`_qlik_exe`) elige el ejecutable en este orden, sin tocar el PATH:

1. la variable `DFEMU_QLIK`, si existe (ruta completa a un `qlik.exe`);
2. la CLI que instala `dfemu setup` en `.tools/qlik/`;
3. `%ChocolateyInstall%\lib\qlik-cli\tools\qlik.exe` (o `C:\ProgramData\chocolatey\lib\qlik-cli\tools\qlik.exe`), siempre que exista;
4. `qlik` del PATH.

Si el sistema impide ejecutarlo (`OSError`), el puente devuelve el código 126 y un mensaje que remite a `dfemu setup` o a `DFEMU_QLIK`; si no hay CLI, devuelve 127 con la misma remisión. Verificado el 2026-11-23 con `dfemu cleanup` desde Git Bash.

**Instalación automática (`dfemu setup`):** descarga `qlik-<sistema>-x86_64` de `github.com/qlik-oss/qlik-cli/releases/download/v4.0.0/`, comprueba su SHA-256 contra `qlik_4.0.0_checksums.txt` del mismo release y extrae solo el binario. Alcance de la comprobación: detecta descargas corruptas, no un release comprometido. El release solo publica x86_64 (en Apple Silicon corre con Rosetta; Linux arm64 no tiene binario). Si una política WDAC también bloquea el binario descargado, `setup` lo dice y pide `DFEMU_QLIK`. Verificado: la CLI instalada por Chocolatey es el mismo binario firmado por QlikTech International AB.

**API key:** `setup` la pide sin mostrarla y la entrega a `qlik context create|update --api-key`; la CLI la guarda en su propio contexto. No se escribe en el repositorio, en `dfemu.local.json` ni en el registro de auditoría. Limitación de la CLI: no admite la clave por variable de entorno ni por entrada estándar, así que durante esa llamada es visible en la lista de procesos.

**Uso manual en PowerShell (fuera del emulador):** anteponer la carpeta al PATH de la sesión: `$env:PATH = "C:\ProgramData\chocolatey\lib\qlik-cli\tools;" + $env:PATH`. Git Bash no puede ejecutar el shim. Al canalizar la salida de `qlik raw` hacia Python desde PowerShell se añade un BOM; usar `ConvertFrom-Json` en PowerShell o leer con `utf-8-sig`.

## 10 ter. Orquestación: tareas programadas y encadenadas

Verificado el 2026-11-23 con la API `scheduling` (la API `reload-tasks` está obsoleta; `v1/tasks` también aparece como reemplazada). Implementado en `emulator/tasks.py` y `dfemu task`.

**Endpoints** (con `qlik raw`, ruta relativa a `/api/`, sin el prefijo `v1/`):

| Operación | Llamada | Notas |
|---|---|---|
| Programar | `POST scheduling/tasks/resources/{appId}/actions/reload/on-time-schedule` | cuerpo: `name`, `recurrence` (RFC 5545 con prefijo `RRULE:`), `timezone` (IANA, por omisión `UTC`), `enabled` (por omisión `false`), opcionales `startDateTime`, `endDateTime`, `partial`, `description` |
| Encadenar | `POST scheduling/tasks/resources/{appId}/actions/reload/on-task-event` | cuerpo: `name`, `onTaskId`, `onTaskStatus` (`succeeded` por omisión, `failed` o `any`), `enabled` |
| Listar | `GET scheduling/tasks?resourceId={appId}` | devuelve un arreglo en la raíz (no `{data: [...]}`) |
| Arrancar | `POST scheduling/tasks/{id}/actions/start` | responde `{"code": "CHO-000", "message": "OK"}` |
| Corridas | `GET scheduling/tasks/{id}/runs` | cada corrida trae `status` (`RUNNING`, `SUCCEEDED`, `FAILED`), `log`, `endedAt`, `actionId` |
| Habilitar o deshabilitar | `PATCH scheduling/tasks/{id}` | cuerpo: JSON Patch (RFC 6902), un arreglo con `[{"op": "replace", "path": "/enabled", "value": true}]`; responde sin cuerpo. `qlik raw` admite `patch` |
| Borrar | `DELETE scheduling/tasks/{id}` | |

**Lo que se comprobó en vivo**
- Programar y encadenar crean la tarea con `version` "1.0.0", un estado `init_state` y `start.schedule` con la regla y la zona. La tarea nace **deshabilitada** salvo que se pida `enabled`.
- **Una tarea deshabilitada no se puede arrancar a mano**: `422 CHO-012 "Task is disabled"`. Para probar un arranque hay que crearla habilitada (el planificador la ejecutaría a su hora, así que se borra al terminar).
- **Habilitar y deshabilitar funciona** (2026-11-23): una tarea creada deshabilitada falla al arrancar con `CHO-012`; tras `PATCH enabled=true` arranca y termina `SUCCEEDED`; con `enabled=false` vuelve a quedar deshabilitada en el listado.
- **El encadenamiento funciona de punta a punta**: se arrancó la tarea A, terminó `SUCCEEDED` y la tarea B (encadenada con `on-task-event`, habilitada) arrancó sola y terminó `SUCCEEDED` unos 3 s después.
- Los endpoints aceptan apps de Data Flow (`DATAFLOW_PREP`). La tarea creada no lleva campo `usage`. Un clon del flujo base con el destino cambiado a un archivo `emu_` se ejecutó como tarea: `SUCCEEDED`, 500 filas leídas y 500 escritas.
- Errores documentados por la API: `CHO-001` cuerpo inválido, `CHO-003` app inexistente o sin permiso `app:reload`, `CHO-014` la app ya tiene el máximo de tareas, `CHO-017` regla o zona rechazada (la frecuencia mínima es `MINUTELY`), `CHO-018` cuota por usuario, `CHO-016` `onTaskId` inexistente.

**Reglas de seguridad añadidas a `Bridge._authorize`**
1. Programar y encadenar: solo si la app es `emu_` del espacio de pruebas; al encadenar, la app de la tarea previa también debe serlo.
2. Arrancar: la app debe ser `emu_` **y** todo `STORE` de su script debe escribir en un archivo `emu_` (`STORE [t] INTO [lib://.../emu_x.csv]`). Cualquier otra aparición de la palabra `STORE` bloquea el arranque.
3. Borrar una tarea: solo si su app es `emu_`.
4. Habilitar o deshabilitar (`PATCH`): solo si su app es `emu_` y el cuerpo es exactamente un `replace` de `/enabled` con un booleano; cualquier otro campo, operación o forma se rechaza.

La regla 2 es necesaria: **un clon de un flujo conserva el destino del original**. El primer intento de arrancar una tarea sobre un clon sin cambios lo rechazó el puente ("el script tiene un STORE que no escribe en un archivo emu_"); sin la guarda habría sobrescrito la salida real.

**Destinos de Google Drive (`GDDestino`)**
- El conector exige la ruta `{idCarpeta}/{archivo}`. Si se cambia el `fileName` del nodo destino por un nombre sin carpeta, la recarga falla con `Expecting a file path of format {folderId}/{fileName}`. Hay que conservar el prefijo de carpeta del original y cambiar solo el nombre (`<carpeta>/emu_xxx`).
- `dfemu cleanup` solo ve los archivos de la conexión `DataFiles`: **un archivo escrito en una carpeta de Google Drive no se borra solo**. La verificación del 2026-11-23 dejó `emu_task_136997.csv` en la carpeta de `GDDestino` del espacio; hay que borrarlo a mano. Buscarlo con el conector de Google Drive de Claude no lo encuentra: la cuenta del conector `GDDestino` no es la misma que la del conector de Claude. No hay llamada de la API de Qlik para listar o borrar archivos de un conector de Drive, así que este hueco no se puede automatizar con lo que hay hoy.

**Pendiente de esta fase:** `usage: DATAFLOW_PREP` en una tarea creada con `POST scheduling/tasks` (opción avanzada) no se probó; las tareas sobre flujos reales (no `emu_`) quedan fuera de la autorización actual.

## 11. Comandos del banco de pruebas

Todos los comandos son simulación por defecto; las escrituras en el tenant requieren `--apply`.

| Comando | Qué hace |
|---|---|
| `dfemu setup [--yes] [--space ID] [--base-app ID]` | instala la CLI de Qlik, crea el contexto pidiendo la API key y fija el espacio y el flujo base |
| `dfemu task ls APP` | lista las tareas de una app `emu_` |
| `dfemu task schedule APP --name N --recurrence RRULE [--timezone TZ] [--enable] [--apply]` | programa la recarga de una app `emu_` |
| `dfemu task chain APP --name N --after TAREA [--on succeeded\|failed\|any] [--enable] [--apply]` | encadena: recarga la app cuando termina otra tarea |
| `dfemu task enable TAREA [--apply]` / `disable TAREA [--apply]` | habilita o deshabilita una tarea |
| `dfemu task start TAREA [--apply]` / `runs TAREA` / `rm TAREA [--apply]` | arranca (solo habilitadas), consulta corridas o borra |
| `dfemu validate archivo.dfw` | valida el `.dfw` con el validador local |
| `dfemu validate --remote --apply archivo.dfw` | sube el grafo a un clon y lee la validez del servidor |
| `dfemu calibrate --apply` | compara el validador local con el servidor sobre una batería de mutaciones |
| `dfemu pull [APP_ID\|--all]` | descarga flujos a `out/corpus/*.pull.json` (solo lectura) |
| `dfemu run archivo.dfw --data data/practica` | ejecuta el flujo sobre DuckDB |
| `dfemu compare archivo.dfw (--app APP\|--push) --apply` | compara resultados del emulador con el tenant |
| `dfemu cleanup [--apply]` | lista o borra apps y archivos `emu_*` |
| `dfemu coverage [archivos...]` | mide qué processors usa el corpus y si cada flujo se puede ejecutar |
| `dfemu translate script.qvs\|.pull.json [--run] [--compare [--apply]]` | traduce el script de Qlik a SQL de DuckDB; con `--run` lo ejecuta y con `--compare --apply` lo compara con la ejecución real en el tenant |

El espacio de escritura se configura con `DFEMU_SPACE_ID`, el flujo base con `DFEMU_BASE_APP` y, solo si hace falta, la CLI con `DFEMU_QLIK` (ver 10 bis).

## 12. Pendiente

- Subir grafos con subflows (probar si el `PUT` admite un campo `subflows`) y evitar el daño del clon.
- Credencial OAuth (en lugar de API key) para ver si habilita `actions/import` y `actions/export`.
- Comparar línea a línea el script de un clon con el original (se observó que difieren sin analizar por qué).
- Orquestación: ver "Pendiente de esta fase" en el apartado 10 ter (`usage` en tareas avanzadas, flujos reales).
- Limpieza de archivos escritos en carpetas de Google Drive (`GDDestino`): `dfemu cleanup` solo cubre `DataFiles` y no hay API de Qlik para listar o borrar en un conector de Drive; se borran a mano.
- Crear fuentes nuevas en un flujo: el `entityId` de cada nodo fuente es propio del flujo y no se encontró cómo registrar una (ver 9 ter).
