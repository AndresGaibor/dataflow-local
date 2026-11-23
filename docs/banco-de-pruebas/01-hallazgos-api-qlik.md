# Hallazgos: cómo automatizar Data Flows y Qlik script contra Qlik Cloud

Documento vivo. Cada afirmación dice si fue **verificada** (ejecutada contra el tenant el 2026-11-19) o **inferida**. Todo se hizo con la CLI `qlik` v4.0.0 y su contexto ya configurado (usuario con rol `AnalyticsAdmin`, credencial tipo API key); no se usó ninguna otra credencial.

## 1. Resumen

| Necesidad | ¿Se puede? | Cómo |
|---|---|---|
| Listar Data Flows | Sí | `GET v1/items` y filtrar `resourceSubType == "dataflow-prep"` |
| **Descargar** un flujo | Sí | `GET v1/dataflows/{dataflowId}` (grafo idéntico al `.dfw` de la interfaz) |
| **Validar** con el servidor | Sí | campo `validity` al leer o al guardar |
| **Subir** un grafo local | Sí, con límites | clonar y `PUT v1/dataflows/{dataflowId}` con el grafo del `.dfw` (sección 5) |
| Importar o exportar el archivo `.dfw` completo | Parcial (ver 10 quinquies) | `POST v1/dataflows/actions/import` y `/export` dan 403 con API key **y con OAuth**, pero esa ruta era la equivocada: las que existen son `POST v1/dataflow-apps/{id}/actions/export` y `POST v1/dataflow-apps/actions/import` |
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

La vía verificada para subir un grafo es: **clonar un flujo base y reemplazar su grafo** con `PUT`. Las rutas de import y export con archivo existen y responden con API key (apartado 10 quinquies), pero falta cerrar la descarga y la subida del archivo.

Resultados sobre clones `emu_` (cada `.dfw` se subió como grafo):

| `.dfw` | Resultado del servidor | Notas |
|---|---|---|
| `fundamentos_filtro_basico` | VALID | Qlik regeneró el script: fusionó selector de campos y filtro en un solo `LOAD ... WHERE`. |
| `fundamentos_remove_fields` | VALID | Su `sourceId` es distinto al del clon: no hace falta registrar las fuentes. |
| `synthetic/s05_fork_union` | INVALID (aceptado) | Sus fuentes sintéticas no existen en el tenant. Nuestro validador local lo da por válido: no ve fuentes inexistentes. |
| `DF_03_TRANSACCIONES` | INVALID (aceptado) | **Después deja el clon inservible** (7.3). |

Consecuencia: para cualquier `.dfw` local se puede obtener (a) el veredicto real y (b) el script que Qlik genera, en dos llamadas. En una primera tanda (antes del daño del clon) tres flujos reales (`Ajustes Rotativos`, `Ajustes Rotativos(Anual)`, `Copia de Ventas Mensuales (Julio) (1)`) dieron INVALID (1 violación) y nuestro validador VÁLIDO; no es concluyente porque se subieron a un clon sin sus fuentes ni subflows.

No se obtuvo cómo leer `sources`, `subflows`, `projections` ni `schemas` por rutas de `v1/dataflows/{id}/...` (404). Para armar un `.dfw` completo, `sources` se puede reconstruir desde `v1/data-sets/{datasetId}`; `projections` y `schemas` vienen vacíos en todos los ejemplos.

## 5 bis. Subflows: cómo subirlos sin dañar el clon

Verificado el 2026-11-23 con `DF_03_TRANSACCIONES` (un flujo con un nodo `subflow` que contiene una receta de tabla).

- **Un subflow es otro `dataflow` de la misma app**, no parte del grafo. El nodo subflow lo referencia con `component.properties.configuration.dataflowId`. `GET v1/dataflows/{ese id}` devuelve su grafo (`linkedSource` → `edit-column` → `noOpTarget`), con `context.dataAppId` igual a la app padre y un nombre `Subflow <id del nodo> of <flujo>`. No existe como `dataflow-app`: `GET v1/dataflow-apps/{id}` da `ADF-002`.
- **Clonar un flujo copia también sus subflows**, con ids nuevos que pertenecen al clon. El nodo conserva el mismo id (`55067239-...` en el original y en el clon), así que sirve para emparejarlos. Volver a subir el grafo propio del clon es seguro (`UNCHANGED`).
- **La causa del daño** era subir un grafo cuyos nodos subflow apuntan a los `dataflowId` del **original**: el servidor intenta crear el subflow en el clon y choca con el id ajeno.
- **Solución** (`Remote._with_clone_subflows`): tras clonar, leer el grafo del clon, emparejar cada nodo subflow por su id y reescribir su `dataflowId` con el del clon antes del `PUT`. Con eso el servidor acepta el grafo y el clon sigue sano en subidas posteriores (probado con dos `PUT` seguidos).
- **Límite:** el flujo base debe ser uno que ya tenga ese subflow (en la práctica, el flujo del que viene el grafo). Un nodo subflow que el base no tiene no se puede crear: `UnsupportedGraph` con el mensaje "use --base-app", sin subir nada y descartando el clon. Se indica con `dfemu validate --remote --apply --base-app APP archivo.dfw` o `dfemu compare --push --base-app APP`.
- **Qué no cubre:** el contenido del subflow se toma del flujo base tal cual; un `.dfw` que cambie la receta dentro del subflow no la modifica en el clon (no se probó `PUT v1/dataflows/{id del subflow}`).

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
3. **Subir un grafo con subflows apuntando a los subflows del original daña el clon.** Tras subir `DF_03_TRANSACCIONES` a un clon de otro flujo, todo `PUT` posterior fallaba con `SUBFLOW_CREATION_ERROR: Resource conflict. Expected ID <clon>, but got <otro id>`, incluso con el grafo original. **Resuelto el 2026-11-23, ver 5 bis.** Un clon dañado sigue sin tener arreglo: se descarta (borrar y clonar de nuevo).
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

## 9 quater. Processors: emulador frente al tenant

Verificado el 2026-11-23 con `scripts/processor_battery.py`: **65 casos**: 54 individuales (`clientes` → un processor → destino; los joins usan un `fork` con una rama filtrada) y 11 cadenas de 3 o 4 pasos (ver más abajo), ejecutados en el emulador y, con el mismo grafo, en el tenant (clon `emu_v_*` del flujo base, script generado por Qlik, app `emu_oracle_*`), comparando huellas. Los casos están en `scripts/processor_battery_cases.json`. **Resultado final: los 65 coinciden** (contenido, y orden y formato de las 8 primeras filas, salvo lo indicado en "Orden y formato"). La primera pasada (15 casos) dio diferencias en todos; las 11 cadenas coincidieron a la primera una vez corregidos los processors sueltos.

### Cómo mide el tenant (importante)
El oráculo no mide el resultado en memoria: **vuelve a cargar el CSV que escribió el flujo** (`oracle._READBACK`) y mide la tabla cargada. En Qlik un archivo no tiene `NULL`: toda celda vacía es el texto vacío, que cuenta como valor y es distinto. Por eso `compare.fingerprint_of` cuenta `count(*)` para todas las columnas y suma 1 al número de distintos si hay algún `NULL`. Esto cubre de una vez los `NULL` que produce el emulador (join sin pareja, conversión de texto no numérico, celda vacía de la fuente). La suma sigue ignorando los vacíos. Una versión intermedia calculaba la huella en memoria; era una aproximación equivocada y se descartó.

### Qué se encontró y se corrigió en el emulador (pruebas en `tests/test_processors_vs_qlik.py`)

| Comportamiento de Qlik | Antes en el emulador |
|---|---|
| Una celda vacía de un CSV es **texto vacío** (con 12 emails vacíos: `IsNull` da falso, `Coalesce([x], 'z')` conserva el vacío, `[x] = ''` es verdadero). También en el traductor de scripts | Las leía como `NULL` |
| `data-cleansing FILL_WITH_VALUE` ("Fill cells with value") pone la constante en **todas** las celdas; rellenar solo las vacías es `REPLACE_WITH_VALUE` | Rellenaba solo los `NULL` |
| `split-field`: columnas `campo-split_N`; la **última parte conserva el resto** (`SubField(c, ' ', 1)` y `Mid(c, Index(c, ' ', 1) + 1)`, vacío si no hay separador) | `campo_N` y la segunda palabra |
| `EXTRACT_DATE_PARTS`: el prefijo es `newColumnRename` si no está vacío (`fecha_` da `fecha__day`) | Siempre el nombre de la columna |
| `strings REPLACE_ON_VALUE`: matriz operador x método (ver abajo) | Soportaba 3 de las 8 combinaciones |

**Matriz de `REPLACE_ON_VALUE`** (scripts de Qlik medidos; `c` es la columna, `v` el valor buscado, `r` el reemplazo):

| Operador | `REPLACE_CELL_WITH_VALUE` (toda la celda) | `REPLACE_MATCHING_WITH_VALUE` (solo la parte) |
|---|---|---|
| `EQUALS` | `IF(Match(c, v), r, c)` | igual que la celda completa |
| `STARTS_WITH` | `IF(Match(Left(c, Len(v)), v), r, c)` | prefijo reemplazado por `r` |
| `ENDS_WITH` | `IF(Match(Right(c, Len(v)), v), r, c)` | `Left(c, Len(c) - Len(v)) & r` |
| `CONTAINS` | `IF(Index(c, v), r, c)` | `replace` de la parte |

### Cadenas de varios processors
Once cadenas (`cadena_*` en `scripts/processor_battery_cases.json`), todas coinciden con el tenant:

| Cadena | Pasos |
|---|---|
| `cadena_limpiar_texto` | `TRIM` → `UPPERCASE` → `REPLACE_ON_VALUE` (contiene) |
| `cadena_filtrar_agregar_ordenar` | filtro `ANY` → agregación `COUNT`/`SUM` → orden descendente |
| `cadena_derivar_filtrar` | `ABSOLUTE` → `MULTIPLY` por constante → filtro numérico sobre la columna nueva |
| `cadena_fechas_agregar` | `EXTRACT_DATE_PARTS` (año) → agregación por la columna derivada |
| `cadena_concat_hash_quitar` | `CONCAT` → `HASH_DATA` sobre la columna nueva → `field-remover` |
| `cadena_dividir_reemplazar` | `split-field` → `REPLACE_ON_VALUE` sobre `campo-split_2` (nombre con guion) |
| `cadena_filtrar_ventana` | filtro → `RANK` → filtro sobre la columna de la ventana |
| `cadena_vacios_agregar` | `REPLACE_WITH_VALUE` (vacíos) → `FILL_WITH_VALUE` → agregación con `COUNT_DISTINCT` |
| `cadena_numero_agregar` | `CONVERT_TO_NUMBER` de texto con vacíos → agregación `SUM` |
| `cadena_join_agregar` | `fork` + join izquierdo (autounión) → agregación sobre la columna de la rama derecha |
| `cadena_fork_union_ordenar` | `fork` en dos filtros → `union` → orden |

**Lo que estas pruebas no miden:** los tipos exactos de columna y las filas más allá de las 8 primeras (ver siguiente apartado).

### Crear `calculate-fields` y `script` por API
Las dos cosas se dieron por imposibles al principio y se resolvieron el 2026-11-23.

**`calculate-fields`** (9 casos `calc_*`: `Upper`, `If`, `&`, `Left`, `Len`, `SubField`, `Round`, aritmética, varias expresiones en un nodo y dos nodos encadenados; los 9 coinciden con el tenant, incluidas las 8 primeras filas).
- Un nodo nuevo sale `INVALID` con `POTENTIAL_STALE_EXPRESSION` ("la expresión debe reevaluarse por un cambio en un nodo anterior"). **Un `PUT` idéntico lo limpia**: el servidor evalúa las expresiones al volver a ver el nodo. El tercer `PUT` ya responde `UNCHANGED`.
- Con nodos encadenados cada `PUT` evalúa **un nivel más** (dos niveles: `INVALID`, `INVALID`, `VALID`). `Remote.push_graph` repite el `PUT` mientras solo queden advertencias de ese tipo, con un tope (`MAX_STALE_PUTS` = 6). Si aparece cualquier otra violación no repite.
- La estructura del nodo es la de siempre (`calculateFields`: `newColumnName`, `expressionStatement`, `anchorColumn`, `rightOfAnchor`, `fieldReferences` vacío); no hace falta nada más.

**`script`**
- Con `PUT` doble desaparece `POTENTIAL_STALE_SCRIPT`, pero el servidor exige `configuration.schemaEntityId` (`VALUE_MISSING_ON_REQUIRED_FIELD`). Ese id lo crea la interfaz al detectar el esquema de salida. Vacío o prestado de otro flujo da `500 INTERNAL_SERVER_ERROR`. No es un dataset ni un item, y ninguna ruta de lectura lo resuelve. Los `POST` que lo crearían (todo `POST` bajo `v1/dataflows/...`) responden `403` sin detalle, con API key y con OAuth; los `GET` equivalentes, "no existe".
- **Vía que sí funciona**: `actions/copy` de un flujo que ya tiene nodos `script` **asigna `schemaEntityId` nuevos y válidos a la copia**. Se parte de esa copia, se arma un grafo reducido (fuente, nodo `script` de la copia, destino nuevo) y se cambia solo el texto del script. Resultado: `VALID`, el tenant lo ejecuta y el traductor lo traduce. El servidor no comprueba el texto contra el esquema registrado: con un script cuyas columnas de salida **difieren** de las del esquema da `VALID`, el tenant lo ejecuta y la salida usa las columnas del script.
- **Una sola cosa sí debe coincidir: el nombre de la tabla de salida.** El script que genera Qlik hace `STORE` de la tabla registrada en el nodo (la primera `[Nombre]:` de su script original, p. ej. `[FechasNormalizadas]`). Si el script nuevo declara otra (`[Resultado]`), el servidor responde `VALID` igualmente y el `STORE` apunta a una tabla que no existe: falla al ejecutarse.
- El texto debe seguir las reglas de la documentación del nodo: `Resident` de la tabla de entrada (el nombre de la entrada es la etiqueta del nodo anterior), `NoConcatenate LOAD` y `Drop Table` de la entrada.
- Esto verifica el **traductor** con scripts de nodo `script` (el emulador no los ejecuta). Para ello se amplió el traductor: nombres de campo y alias **sin corchetes** (`id,`, `as fecha`), operadores con precedencia (`OR`, `AND`, comparaciones, `&`, `+ - * /`), paréntesis y `Len`/`Lower`. `&` usa `concat`, que trata `NULL` como texto vacío, como Qlik.
- **Diferencia que se midió y no se corrigió**: en una columna de texto con aspecto de fecha, Qlik **unifica los textos que interpreta como la misma fecha** al cargar el CSV (`2026-09-09` y `09/09/2026`), y cuenta 18 valores distintos donde el emulador cuenta 20. Afecta solo a `distinct` de esas columnas.
- **Comando**: `dfemu script-node --base-app APP --source ETIQUETA --node ETIQUETA --script archivo.qvs [--target emu_x] [--out out/script_node.qvs] --apply` (`emulator/scriptnode.py`). Copia el flujo base, arma el grafo reducido, valida y guarda el script generado; se niega si el script nuevo no declara la tabla de salida registrada. Después, `dfemu translate out/script_node.qvs --compare --apply` lo ejecuta en el tenant y lo compara con la traducción local.
- No se añadió a la batería porque depende de un flujo base con nodos `script` de cada tenant.

### Orden y formato de lo escrito
Las huellas cuentan filas, distintos y sumas, pero no ven el orden ni el texto de las celdas. Una sonda que **carga el archivo del tenant con el número de fila** (`RecNo()`) y compara el texto de las primeras 8 filas de cada columna con las del emulador encontró 5 diferencias reales, ya corregidas. La comprobación es ahora permanente: `dfemu compare --rows N`, y `scripts/processor_battery.py` compara 8 filas de cada caso (`HEAD`).

| Comportamiento de Qlik (medido) | Antes en el emulador |
|---|---|
| Un número entero se escribe sin `.0` (`1700000001`), un decimal tal cual (`1700000259.5`) | `1700000001.0` |
| Una fecha convertida (`CONVERT_TO_DATE`, `CONVERT_TO_TIMESTAMP`) se escribe con los `SET` del script: en-US `M/D/YYYY` (`5/24/2019`) y `M/D/YYYY h:mm:ss TT` (`5/24/2019 12:00:00 AM`). Una fecha que solo pasa de largo conserva su texto original | ISO (`2019-05-24`) |
| `aggregate` devuelve los grupos en el orden de **primera aparición** en la tabla de origen | Orden arbitrario de DuckDB |
| `window` (`RANK`, `ROW_NUMBER`) devuelve las filas en el **orden de origen** con la columna nueva | Las reordenaba por la ventana |
| `split-field`: una parte que no existe es **`NULL`** (no `''`), y por eso un `REPLACE_ON_VALUE` posterior de "vacíos" no la toca | `''` |
| Join `FULL` o `RIGHT` con filas que solo existen a la derecha: la clave sale de la derecha (el emulador descartaba la clave derecha y quedaba vacía) | Clave vacía |

Solo se midió la configuración regional en-US: otras conservan el formato ISO (`ctx.locale`, `_qlik_text_format`).

**Lo que no se pudo reproducir**
- **Orden de salida de un `JOIN` de Qlik.** Con claves únicas y ya ordenadas coincide con el orden de la tabla izquierda. Pero con la rama izquierda en orden descendente y claves únicas, Qlik devolvió el resultado en orden **ascendente** (el script tenía `ORDER BY [cedula] DESC` en la tabla izquierda y el `STORE` salió igualmente ascendente). Con una clave repetida y sucia (`ciudad`) agrupa por clave, en un orden que no es alfabético (empezó por `Cuenca`), y dentro de cada grupo reordena las filas con una regla que no se dedujo. Una primera conclusión ("Qlik conserva el orden de la izquierda") era falsa y salió de datos que ya venían ordenados. El emulador usa un orden determinista propio (izquierda y luego las filas solo-derecha) y la batería compara los joins **por contenido**, no por orden (`NO_HEAD` con `"*"`).
- **`HASH_DATA`**: los valores no pueden coincidir (el emulador usa `md5`; Qlik genera otra cadena), así que se excluye esa columna de la comparación de filas.

**Errores transitorios del tenant al repetir la batería** (no son fallos del emulador; reintentar el caso):
- `RELOADS-010 Service Unavailable` al consultar la recarga.
- `could not open app ... Request aborted (15 GENERIC ABORTED)` al abrir la app para leer las tablas.
- Un `scripts/processor_battery.py` interrumpido a mitad (p. ej. por falta de memoria del equipo) puede dejar una app `emu_oracle_*` y un archivo `emu_*.csv`: `dfemu cleanup --apply` los borra. Con poca memoria libre conviene lanzar los casos por tandas de 6 a 12.

### Lo que el servidor dijo sobre sus propios tipos
- **Ventanas (`window`)**: los tipos válidos son `FIRST`, `AVG`, `MAX`, `CONCATENATE`, `LAST`, `SUM`, `COUNT_DISTINCT`, `ROW_NUMBER`, `COUNT`, `MIN` y `RANK`. **`DENSE_RANK` no existe** (el servidor responde `BAD_REQUEST ... not one of the values accepted for Enum class`). El emulador cubre `RANK` y `ROW_NUMBER`; las ventanas de agregación (`SUM`, `AVG`...) con rango no están emuladas.
- **Agregaciones** reales en los flujos: `SUM`, `AVG`, `COUNT`, `MEDIAN`, `MAX`, `MIN`, `COUNT_DISTINCT`. **Filtros**: `EQUAL`, `NOT_EQUAL`, `GREATER`, `GREATER_OR_EQUAL`, `LOWER`, `LOWER_OR_EQUAL`, `IS_NOT_NULL`, `MATCH_REGEX`, con `logicalOpType` `ALL` o `ANY`. **Joins**: `INNER_JOIN`, `LEFT_OUTER_JOIN`, `FULL_OUTER_JOIN`.

### Límites que quedan
- `Avg` sobre valores grandes (~1,7·10⁹) sale cuantizado en Qlik (ver 9 ter); la batería usa solo `COUNT` y `SUM` en el caso de agregación simple.
- `split-field` con `parts` mayor que 2 supone la misma regla (solo se midió con 2).
- `script` no se puede crear desde cero por API (ver "Crear `calculate-fields` y `script` por API"); el emulador no ejecuta nodos `script`, que se verifican con el traductor.
- `masking.HASH_DATA` se emula con `md5`; la huella solo ve cuenta y distintos, así que no detecta que el algoritmo sea otro.
- `sample.SAMPLE_RANDOM_ROWS` es aleatorio y no se compara.
- Los joins se probaron como autounión (misma fuente en dos ramas): un join entre dos datasets distintos necesita una segunda fuente registrada en el flujo, y no se encontró cómo crearla por API.

### Limpieza
Tras una pasada completa puede quedar listada una app `emu_oracle_*` que ya no existe (`GET v1/apps/{id}` da 404): el índice de items de Qlik tarda en actualizarse. `dfemu cleanup --apply` lo avisa ("ya no existe") y sigue con el resto en lugar de fallar.

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

Límites de la regla 2: una ruta de `STORE` con una variable de Qlik (`$(...)`) se rechaza, porque se expande al ejecutar y podría apuntar fuera de un archivo `emu_`; y la guarda no ve escrituras hechas por otros medios (`EXECUTE`, `Include` de otro archivo, SQL contra una base). Protege contra el caso real (clonar un flujo y ejecutarlo sin cambiar el destino), no contra un script hecho para evadirla. Dos límites conocidos que se dejaron así: la guarda no comprueba que la biblioteca (`lib://...`) sea la del espacio de pruebas, solo que el archivo se llame `emu_*`; y cualquier aparición de la palabra `STORE` (un campo llamado `[Store]`, un comentario) bloquea el arranque aunque el script sea legítimo, porque falla del lado seguro.

La regla 2 es necesaria: **un clon de un flujo conserva el destino del original**. El primer intento de arrancar una tarea sobre un clon sin cambios lo rechazó el puente ("el script tiene un STORE que no escribe en un archivo emu_"); sin la guarda habría sobrescrito la salida real.

**Destinos de Google Drive (`GDDestino`)**
- El conector exige la ruta `{idCarpeta}/{archivo}`. Si se cambia el `fileName` del nodo destino por un nombre sin carpeta, la recarga falla con `Expecting a file path of format {folderId}/{fileName}`. Hay que conservar el prefijo de carpeta del original y cambiar solo el nombre (`<carpeta>/emu_xxx`).
- `dfemu cleanup` solo ve los archivos de la conexión `DataFiles`: **un archivo escrito en una carpeta de Google Drive no se borra solo**. La verificación del 2026-11-23 dejó `emu_task_136997.csv` en la carpeta de `GDDestino` del espacio; se borró a mano el mismo día. Lección: tras ejecutar un flujo con destino en Google Drive, revisar esa carpeta. Buscarlo con el conector de Google Drive de Claude no lo encuentra: la cuenta del conector `GDDestino` no es la misma que la del conector de Claude. No hay llamada de la API de Qlik para listar o borrar archivos de un conector de Drive, así que este hueco no se puede automatizar con lo que hay hoy.

**Pendiente de esta fase:** `usage: DATAFLOW_PREP` en una tarea creada con `POST scheduling/tasks` (opción avanzada) no se probó; las tareas sobre flujos reales (no `emu_`) quedan fuera de la autorización actual.

## 10 quater. Clientes OAuth: lo aprendido

Guía completa, paso a paso y desde cero, en `02-guia-oauth.md`. Lo esencial, verificado el 2026-11-23:

- Un cliente M2M necesita, además de la casilla M2M y el scope `user_default`, el **consentimiento "De confianza"**. Sin él, `POST /oauth/token` responde `401 OAUTH-5 "oauth client is not approved with trusted consent method"`; la CLI lo muestra como un 401 genérico con el cuerpo vacío.
- Las URL de redireccionamiento y los orígenes permitidos se dejan vacíos en M2M: el asistente deja continuar así.
- `qlik context init` **activa** el contexto nuevo, aunque falle. Con credenciales inválidas rompe todos los comandos hasta `qlik context use <contexto de siempre>`.
- La API key de un usuario que no es Tenant Admin no puede listar clientes OAuth (`OAUTH-CLIENTS-27`).
- La prueba directa a `/oauth/token` con PowerShell (`Read-Host -AsSecureString`) enseña el error real que la CLI oculta.
- El token de un cliente M2M con `user_default` dura 21600 s (6 horas).

## 10 quinquies. Importar y exportar `.dfw` con archivo

Verificado el 2026-11-23, con la API key y con un cliente OAuth M2M (rol `TenantAdmin`, scope `user_default`). **OAuth no cambió nada:** lo que funciona con uno funciona con el otro, y lo que da 403 lo da con ambos.

| Llamada | Resultado |
|---|---|
| `POST v1/dataflows/actions/export`, `.../import`, `v1/dataflows/{id}/actions/export`, `v1/dataflows/export` | **403** sin detalle (`{"status": 403, "error": "Forbidden", "path": ...}`) con API key y con OAuth: ruta equivocada o no expuesta |
| `POST v1/dataflow-apps/{appId}/actions/export` (con o sin cuerpo) | **200**, devuelve solo `{"fileName": "fundamentos.dfw"}` |
| `POST v1/dataflow-apps/actions/import` con `{}` | **400 `ADF-406` "The request is missing a file ID"**: la ruta existe y exige el id de un archivo ya subido |
| `POST v1/dataflow-apps/actions/export`, `v1/dataflow-apps/import`, `v1/dataflow-apps/{id}/export` | 404 |
| `GET v1/dataflow-apps/{id}/actions/export[/{fileName}]`, `.../exports` | 404 |
| `POST v1/temp-contents?filename=X&ttl=60` (cuerpo `application/octet-stream`) | **rc 0** con cuerpo vacío: el archivo se sube, pero su id viaja en la cabecera `Location` |

**Lo que se concluye**
- El 403 que se anotó al principio era por usar `v1/dataflows/...`; la API correcta es `v1/dataflow-apps/...`. No hace falta OAuth para esto. El cliente OAuth creado puede borrarse (ver 10 quater).
- **Importar** sería: subir el `.dfw` a `POST v1/temp-contents` (almacén temporal, TTL máximo 3 días), tomar el id de la cabecera `Location`, y llamar a `POST v1/dataflow-apps/actions/import` con ese id (el nombre exacto del campo falta por confirmar; el servidor dice "file ID").
- **Exportar** devuelve el nombre del archivo; dónde se descarga el contenido no se encontró (el cuerpo no lo trae y las rutas `GET` probadas dan 404).

**Por qué quedó abierto:** `qlik raw` solo imprime el cuerpo de la respuesta. La cabecera `Location` solo se ve con `--verbose`, que también imprime el token de autorización, así que no se usó. Opciones para seguir: (a) un cliente HTTP propio que pida el token con el flujo OAuth M2M y lea la cabecera sin imprimirla (más código y manejo de credenciales), (b) la subida con el protocolo tus (`POST v1/temp-contents/files`), que también devuelve `Location`, o (c) seguir con la vía de clonar y reemplazar el grafo, que ya cubre lo que el banco de pruebas necesita.

## 10 sexies. Qlik MCP Server: evaluado, no se usa

Evaluado el 2026-11-23 a partir de las páginas de ayuda de Qlik ("Administering Qlik MCP", "Qlik MCP tools" y "Connecting to the Qlik MCP server"); **no se probó en vivo**. La página de herramientas se leyó incompleta y la clasificación de lectura o escritura de cada herramienta es una inferencia por nombre y descripción.

**Qué es:** un servidor al que se conectan clientes MCP (Claude, ChatGPT u otros) en `https://<tenant>/api/ai/mcp`. Autenticación **solo OAuth**, como el usuario que conecta (no admite API key). Lo activa un administrador del tenant (permiso "Qlik MCP" en Funciones y acciones, más un cliente OAuth con los scopes `user_default` y `mcp:execute`) y un administrador debe ser el primero en conectar cada cliente. Cuenta como consumo: cada 5 llamadas facturables restan una "pregunta" del cupo mensual, con un máximo de 300 llamadas por usuario por minuto.

**Qué ofrece (unas 106 herramientas):** descubrimiento y metadatos de apps, scripts de carga y recargas de **apps** (`qlik_get_script`, `qlik_update_script`, `qlik_start_app_reload`, `qlik_get_reload_status`, `qlik_get_reload_log`, `qlik_create_app`), automatizaciones, datasets y calidad de datos, productos de datos, glosario, linaje, elementos maestros, marcadores, selecciones, hojas y gráficos, y Qlik Predict.

**Por qué no sirve para este proyecto**
- **No tiene ninguna herramienta de Data Flows** (flujos `dataflow-prep`), que es todo lo que hace este proyecto. Tampoco de tareas programadas (`scheduling`), ni de `dataflow-apps/actions/copy`, ni de `PUT` de grafos.
- Lo único que se solapa (crear una app, poner su script, recargar y leer el modelo) ya lo hace la CLI y la API REST con más control, y pasa por `Bridge`, que solo permite escribir objetos `emu_*`. El MCP actúa con todos los permisos del usuario y **sin esa guarda**.
- Exige OAuth y administración del tenant, y gasta cupo de preguntas. Para automatizar y verificar, la API key de la CLI basta.

**Dónde sí tendría sentido (fuera de este proyecto):** que una persona consulte con un asistente apps, datasets, glosario y linaje del tenant en lenguaje natural. Para eso no hace falta nada de este repositorio.

**Si algún día hiciera falta probarlo:** activar el permiso, crear el cliente OAuth con la URL de redirección del cliente MCP, conectar primero con la cuenta de administrador y comprobar con la lista de herramientas si aparece alguna de Data Flows (la página lo desmiente hoy).

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
| `dfemu script-node --base-app APP --source E --node E --script f.qvs [--apply]` | crea un nodo `script` por API reutilizando el de una copia y guarda el script que genera Qlik (ver 9 quater) |
| `dfemu validate archivo.dfw` | valida el `.dfw` con el validador local |
| `dfemu validate --remote --apply [--base-app APP] archivo.dfw` | sube el grafo a un clon y lee la validez del servidor |
| `dfemu calibrate --apply` | compara el validador local con el servidor sobre una batería de mutaciones |
| `dfemu pull [APP_ID\|--all]` | descarga flujos a `out/corpus/*.pull.json` (solo lectura) |
| `dfemu run archivo.dfw --data data/practica` | ejecuta el flujo sobre DuckDB |
| `dfemu compare archivo.dfw (--app APP\|--push [--base-app APP]) --apply` | compara resultados del emulador con el tenant |
| `dfemu cleanup [--apply]` | lista o borra apps y archivos `emu_*` |
| `dfemu coverage [archivos...]` | mide qué processors usa el corpus y si cada flujo se puede ejecutar |
| `python scripts/processor_battery.py [caso ...]` | batería de 65 casos (54 processors y 11 cadenas), emulador frente al tenant (escribe en el tenant; limpia lo que crea) |
| `dfemu translate script.qvs\|.pull.json [--run] [--compare [--apply]]` | traduce el script de Qlik a SQL de DuckDB; con `--run` lo ejecuta y con `--compare --apply` lo compara con la ejecución real en el tenant |

El espacio de escritura se configura con `DFEMU_SPACE_ID`, el flujo base con `DFEMU_BASE_APP` la CLI con `DFEMU_QLIK` (ver 10 bis) y, para usar otro contexto de la CLI sin activarlo, `DFEMU_QLIK_CONTEXT` (ver `02-guia-oauth.md`).

## 12. Pendiente

- Modificar la receta dentro de un subflow (`PUT v1/dataflows/{id del subflow}`): no se probó; hoy el subflow se toma del flujo base (ver 5 bis).
- Import y export de `.dfw` con archivo: ver 10 quinquies. OAuth no era necesario (la API key sirve); falta obtener el id de la subida a `temp-contents` (viene en la cabecera `Location`, que la CLI no muestra) y la descarga del archivo exportado.
- Cliente OAuth `dfemu-prueba`: ya borrado en el tenant y el contexto `dfemu-oauth` ya no está en la CLI (2026-11-23). Si hace falta otro, la guía es `02-guia-oauth.md`.
- Comparar línea a línea el script de un clon con el original (se observó que difieren sin analizar por qué).
- Orquestación: ver "Pendiente de esta fase" en el apartado 10 ter (`usage` en tareas avanzadas, flujos reales).
- Limpieza de archivos escritos en carpetas de Google Drive (`GDDestino`): `dfemu cleanup` solo cubre `DataFiles` y no hay API de Qlik para listar o borrar en un conector de Drive; se borran a mano.
- Crear fuentes nuevas en un flujo: el `entityId` de cada nodo fuente es propio del flujo y no se encontró cómo registrar una (ver 9 ter).
