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

Verificado el 2026-11-23 y 24 con `DF_03_TRANSACCIONES` (un flujo con un nodo `subflow` que contiene una receta de tabla).

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

Verificado el 2026-11-23 con `scripts/processor_battery.py`: **129 casos**: 115 individuales y 3 cadenas más (`clientes` → un processor → destino; los joins usan un `fork` con una rama filtrada) y 11 cadenas de 3 o 4 pasos (ver más abajo), ejecutados en el emulador y, con el mismo grafo, en el tenant (clon `emu_v_*` del flujo base, script generado por Qlik, app `emu_oracle_*`), comparando huellas. Los casos están en `scripts/processor_battery_cases.json`. **Resultado final: los 129 coinciden** (111 el 2026-11-23 y 15 variantes descubiertas con la interfaz el 2026-11-24; en estas, `ROUND`/`CEIL`/`FLOOR` con precisión > 0 diferían solo en los decimales fijos y se corrigieron) (contenido, y orden y formato de las 8 primeras filas, salvo lo indicado en "Orden y formato"). La primera pasada (15 casos) dio diferencias en todos; las 11 cadenas coincidieron a la primera una vez corregidos los processors sueltos.

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

### `unpivot` y `pivot`
**Cómo se descubrieron las claves del JSON** (sirve para cualquier processor): con una configuración vacía, el servidor responde `VALUE_MISSING_ON_REQUIRED_FIELD` y en `parameters.attributePath` dice **qué campo falta** (`/fieldToPivot`, `/unpivotColumns`...). Se rellena ese campo y se repite hasta que deja de quejarse. El servidor **ignora las claves desconocidas** (no las lista), pero un valor inválido de un tipo enumerado sí enumera los válidos (`not one of the values accepted for Enum class: [...]`). Un tipo de nodo desconocido y el resto de la estructura salen de las pruebas.

**`unpivot`** (4 casos `unpivot_*`; los 4 coinciden con el tenant, incluidas las 8 primeras filas):
- Claves: `unpivotColumns` (lista), `attributeColumn` (nombre de la columna con los nombres de campo) y `valueColumn`. Se crea por API sin más (no pide `schemaEntityId`).
- Qlik genera `CROSSTABLE('atributo', 'valor', n) LOAD ...`: las columnas **no seleccionadas** quedan como claves en su orden (también si la columna seleccionada está en el medio), después van la columna de atributo y la de valor; cada fila de origen da una fila por cada columna seleccionada, en ese orden (por fila y luego por columna). Los `NULL` se omiten; una celda vacía de CSV no (es texto vacío). Los valores de columnas de tipos distintos se escriben como texto.
- Un nombre igual para las dos columnas nuevas da `DUPLICATE_COLUMN_NAMES_IN_TABLE`.

**`pivot`** (**no se pudo verificar**; el emulador responde que no lo soporta y por qué):
- Claves: `fieldToPivot`, `valueField`, `aggregation` y `delimiter`; `aggregation` admite `AVG`, `MAX`, `CONCATENATE`, `SUM`, `COUNT_DISTINCT`, `COUNT`, `MIN` y `ONLY` (sin agregación). Las demás columnas son las claves de agrupación.
- Exige `schemaEntityId`: el esquema de las columnas dinámicas lo calcula la interfaz ("el flujo tiene que ejecutarse en segundo plano primero", dice la documentación). Sin él: `VALUE_MISSING_ON_REQUIRED_FIELD`. Un id **prestado** del nodo `script` de una copia da `500 Unable to find projection with entityId...`: la proyección está ligada a su nodo, así que el truco del nodo `script` (reutilizar el nodo entero) no sirve aquí.
- Para medirlo haría falta un nodo `pivot` creado en la interfaz dentro de un flujo del espacio, y generalizar `dfemu script-node` para reutilizarlo.

### Variantes de cada processor: cuáles existen y cuáles están verificadas
El servidor lista todas las variantes de un processor si se le manda un `type` inválido (`Enum class: [...]`). `scripts/discover_config.py` descubre la configuración de cada una (resultados en `out/discovered_configs.json`).

**Reglas del descubrimiento**
- El objeto de configuración se llama como el tipo en camelCase más `Configuration` (`LOWERCASE` → `lowercaseConfiguration`; `REMOVE_NON_ALPHA_NUM_CHARS` → `removeNonAlphaNumCharsConfiguration`). Con el `type` y **sin** ese objeto el servidor da un `500 INTERNAL_SERVER_ERROR` **sin ningún detalle**; con el objeto vacío ya dice qué campo falta.
- Algunas variantes (`SUBSTRING`) solo se resuelven con los campos habituales desde el principio: `columnsToProcess`, `newColumnName`, `shouldCreateNewColumn`.
- Otras dan `500` sin detalle aunque se pongan esos campos (`CUT`, `ROUND`, `FLOOR`, `CEIL`, `ROUND_DOWN`, `FORMAT_NUMBER`, `MODIFY_DATES`, `FORMAT_DATES`, `EXPONENTIEL_NUMBERS`): por API no se descubren. **Se descubren creando el nodo en la interfaz** (`dfemu ui add`, `ui options`, `ui fill`, `ui apply`) y leyéndolo con `dfemu flow node` (2026-11-24). El nodo sale con todas las sub-configuraciones y el servidor fija `type` al aplicar. Atención: el desplegable de columnas es multiselección (rellenarlo dos veces deselecciona) y la función nueva borra las columnas ya elegidas.

**Claves descubiertas con la interfaz (2026-11-24).** `numbers`: `ROUND` → `roundHalfUpConfiguration`, `CEIL` → `roundCeilConfiguration`, `FLOOR` → `roundFloorConfiguration` (los tres con `precision`), `ROUND_DOWN` → `removeFractionalPartConfiguration` (la interfaz lo llama «Eliminar la parte fraccional»; `ROUND_DOWN_REAL` es «modo down»), `FORMAT_NUMBER` → `formatNumberConfiguration` (`outputFormat` `THOUSAND_WITHOUT_DECIMAL`, `THOUSAND_WITH_1_DECIMAL`, `THOUSAND_WITH_2_DECIMAL`, `PERCENTAGE_WITHOUT_DECIMAL`, `PERCENTAGE_WITH_1_DECIMAL`, `PERCENTAGE_WITH_2_DECIMAL`, personalizado con `customFormat`; `decimalSeparator`, `thousandSeparator`). `math`: `EXPONENTIEL_NUMBERS` → `exponentialNumbersConfiguration`. `strings`: `CUT` → `cutConfiguration` con `pattern: {value, operator}` (`EQUALS`, `CONTAINS`, `STARTS_WITH`, `ENDS_WITH`, expresión regular). `date`: `FORMAT_DATES` → `formatDatesConfiguration` (`format: YYYYMMDD_DASH`, `datePattern`, `newColumnRename`), `MODIFY_DATES` → `modifyDateConfiguration` (`timeUnit`, `useWith: VALUE|COLUMN`, `constantValue`, `column`), `TIME_SINCE` → `computeTimeSinceConfiguration` (`until: NOW`, `timeUnit`, `datePattern`). Las expresiones que genera Qlik: `ROUND([c])` / `ROUND([c], 0.01)`, `CEIL([c], 0.1)`, `FLOOR([c], 0.1)`, `IF([c] > 0, Floor([c]), CEIL([c]))`, `num([c], '#,##0.00', '.', ',')`, `num([c], '0.0%', '.', ',')`, `Exp([c])`, `IF(Match([c], 'a'), '', [c])` (`EQUALS`), `Replace([c], 'a', '')` (`CONTAINS`), `Date([c], 'YYYY-MM-DD')`, `Date([c] + 3)`. **Formato medido:** con `precision` > 0 Qlik escribe siempre esos decimales (`-35.00`, `-35.0`); con 0, entero. El valor sigue siendo un número (se puede sumar después): el formato solo se aplica al escribir. **Con paso, Qlik divide por el paso** (`ROUND([c], 0.1)` = `round(x/0.1)*0.1`): para un saldo de `2934.35` da `2934.3`, no `2934.4` como `round(x, 1)`; lo midió el escenario de extremo a extremo con 760 cuentas.

| Processor | Verificadas contra el tenant | Configuración descubierta, sin emular | Sin descubrir o sin probar |
|---|---|---|---|
| `strings` | `UPPERCASE`, `LOWERCASE`, `PROPERCASE`, `TRIM`, `REPLACE_ON_VALUE` (matriz completa), `REMOVE_NON_NUM_CHARS`, `COMPUTE_LENGTH`, `CONTAINS`, `PADDING`*, `SUBSTRING`*, `CONVERT_TO_STRING`, `REMOVE_NON_ALPHA_NUM_CHARS`, `MATCHES_PATTERN`*, `REMOVE_CONSECUTIVE_CHARACTERS`*, `CUT` (`EQUALS`, `CONTAINS`)* | | `FUZZY_MATCHING` (la interfaz no lo guardó) |
| `math` | `ABSOLUTE`, `MULTIPLY`, `ADD`, `SUBTRACT`, `DIVIDE`, `MODULO`, `POW_NUMBERS`, `MIN_NUMBERS`, `MAX_NUMBERS`, `NEGATE_NUMBERS`, `SQUARE_ROOT_NUMBERS`, `SIN_NUMBERS`, `COS_NUMBERS`, `TAN_NUMBERS`, `LOGARITHM_NUMBERS`, `NATURAL_LOGARITHM_NUMBERS`, `EXPONENTIEL_NUMBERS` | | `NUMERIC_OPS` (no está en la interfaz) |
| `numbers` | `CONVERT_TO_NUMBER`, `REMOVE_NEGATIVE_VALUES`, `ROUND_DOWN_REAL`, `COMPARE_NUMBERS`*, `ROUND`, `CEIL`, `FLOOR` (precisión 0, 1, 2), `ROUND_DOWN`, `FORMAT_NUMBER` (`THOUSAND_*`, `PERCENTAGE_*`; no el personalizado) | | `FORMAT_MONEY` (no está en la interfaz) |
| `date` | `EXTRACT_DATE_PARTS`, `CONVERT_TO_DATE`, `CONVERT_TO_TIMESTAMP`, `TRUNCATE_DATE` (`YEAR`, `MONTH`, `DAY`, `HOUR`), `FORMAT_DATES` (`YYYYMMDD_DASH`, `YYYYMMDD`), `MODIFY_DATES` (las 9 unidades, valor fijo) | `TIME_SINCE` (depende de `NOW`: no se puede comparar) | `CONVERT_TO_TIME`, `COMPARE_DATES` (la interfaz usa campos con máscara que no se rellenan por teclado), `DATE_FROM_PARTS`, `TIME_FROM_PARTS`, `TIMESTAMP_FROM_PARTS` |
| `split-field` | `SPLIT_TEXT_IN_PARTS` | | `EXTRACT_VALUES_BY_REGEX` |
| `window` | `RANK`, `ROW_NUMBER`, `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`, `COUNT_DISTINCT`, `FIRST`, `LAST`, `CONCATENATE` (con rango) | | |
| `unpivot` | todas | | |
| `pivot` | | claves conocidas | no se puede crear por API (ver arriba) |

**Variantes leídas del script de Qlik y verificadas (11 casos):** `COMPUTE_LENGTH` crea `[c_length]` (`Len`); `CONTAINS` crea `[c_contains_<valor>]` con `TRUE`/`FALSE` (`Index`, distingue mayúsculas); `PADDING` es `Repeat('0', 5 - Len(c)) & c` (nunca trunca) y `SUBSTRING` es `Mid(c, 1, 5)`: *solo se comprobaron los valores por defecto, no se descubrieron las claves de ancho y posición*; `CONVERT_TO_STRING` es `Text`; `REMOVE_NON_ALPHA_NUM_CHARS` es `KeepChar` (letras y dígitos ASCII); `REMOVE_NEGATIVE_VALUES` es `IF(c < 0, Null(), c)` siempre en sitio aunque se pida columna nueva; `TRUNCATE_DATE` crea `[c_truncated]` (`YearStart`, `MonthStart`, `Floor`, `Floor(x*24)/24`...; `MINUTE` y `SECOND` compilan pero no se midieron) y el servidor rechaza `WEEK`, `MILLISECOND` y `MICROSECOND` ("unsupported formats for truncate date"), igual que el emulador. El nombre de la columna nueva en `COMPUTE_LENGTH`, `CONTAINS` y `TRUNCATE_DATE` no sale de `newColumnName`.

**Trigonometría y logaritmos:** `Sin`, `Cos`, `Tan`, `Log10` (`LOGARITHM_NUMBERS`) y `Log` (`NATURAL_LOGARITHM_NUMBERS`) sobre la columna; el logaritmo de un valor no positivo da vacío (verificado con datos negativos). Con `*`: solo se comprobaron los valores por defecto, no se descubrieron las claves para cambiarlos: `MATCHES_PATTERN` usa `CountRegEx(c, '^[a-zA-Z]+$')` y crea `[c_matching]` (`TRUE`/`FALSE`); `COMPARE_NUMBERS` usa `c = 0`; `REMOVE_CONSECUTIVE_CHARACTERS` usa un patrón literal que no cambia el texto. `ROUND_DOWN_REAL` es `IF(c > 0, Floor(c), Ceil(c))`, es decir, hacia cero. `CONVERT_TO_TIME` (`time(time#(c, 'hh:mm'))`, crea `[c_toTime]`) está descubierta y sin emular; `COMPARE_DATES` y `DATE_FROM_PARTS` necesitan más campos.

**`math` con otro campo o con un valor fijo:** las operaciones binarias (`ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MODULO`, `POW_NUMBERS`, `MIN_NUMBERS`, `MAX_NUMBERS`) usan `mode` (`WITH_VALUE` o `WITH_FIELD`), `constantValue` y `selectedColumn`, igual que `MULTIPLY`. Las unarias (`ABSOLUTE`, `NEGATE_NUMBERS`, `SQUARE_ROOT_NUMBERS`) solo `columnsToProcess`. Las 11 se verificaron en el tenant (hipótesis confirmadas a la primera).

**Formato de los números:** Qlik escribe los decimales con **14 cifras significativas** y sin `.0` (`sqrt(2)` sale `1.4142135623731`; DuckDB daba `1.4142135623730951`). El escritor del emulador lo reproduce con `printf('%.14g')`; a partir de 1e14 conserva el texto de DuckDB porque no se midió cómo escribe Qlik esos valores.

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
- **Ventanas (`window`)**: los tipos válidos son `FIRST`, `AVG`, `MAX`, `CONCATENATE`, `LAST`, `SUM`, `COUNT_DISTINCT`, `ROW_NUMBER`, `COUNT`, `MIN` y `RANK`. **`DENSE_RANK` no existe** (el servidor responde `BAD_REQUEST ... not one of the values accepted for Enum class`). Todas están emuladas y verificadas. Qlik las genera como `Window(agg(c), partición, 'ASC'|'DESC', orden[, 1, inicio, fin])`: `PRECEDING n` es `-n`, `CURRENT` es `0`, `FOLLOWING n` es `n`, `UNLIMITED` es `Unbounded()`, y sin rango la agregación abarca toda la partición. Dos rarezas medidas: `Window(Avg())` devuelve **8 cifras significativas** (`-246.66667`; lo confirmó la suma de 500 filas, no 5 decimales), y `Concat` junta los valores **ordenados por su texto**, no por el orden de la ventana. Las filas salen en el orden de origen.
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
| `python scripts/processor_battery.py [caso ...]` | batería de 129 casos (100 processors y 11 cadenas), emulador frente al tenant (escribe en el tenant; limpia lo que crea) |
| `dfemu translate script.qvs\|.pull.json [--run] [--compare [--apply]]` | traduce el script de Qlik a SQL de DuckDB; con `--run` lo ejecuta y con `--compare --apply` lo compara con la ejecución real en el tenant |

El espacio de escritura se configura con `DFEMU_SPACE_ID`, el flujo base con `DFEMU_BASE_APP` la CLI con `DFEMU_QLIK` (ver 10 bis) y, para usar otro contexto de la CLI sin activarlo, `DFEMU_QLIK_CONTEXT` (ver `02-guia-oauth.md`).

## 12. Pendiente

**Escenario de extremo a extremo (2026-11-24).** `scripts/e2e_ventas.py`: `clientes` (500 filas) y `cuentas` (760) → limpiar texto (`TRIM`, `UPPERCASE`, `PROPERCASE`), filtrar cuentas activas, `ROUND` del saldo a 1 decimal, `INNER_JOIN`, agregación por ciudad y tipo, `RANK` por tipo, `FORMAT_NUMBER`, orden y destino: 12 nodos, 30 filas, **coincide con el tenant** (contenido y primeras filas). Las dos fuentes se registran una vez desde el editor (`dfemu ui add "Conjuntos de datos" --tab Fuentes`, buscar el dataset en el catálogo y «Cargar en el flujo de datos») en el clon `emu_e2e_ventas`; luego el script empuja el grafo por API. Hallazgos que salieron de él: (1) `ROUND`, `CEIL` y `FLOOR` con paso dividen por el paso (ver arriba); (2) **`RANK` ordenando por un `SUM` de decimales falla al recargar** (`Internal error in WRank. Rank list is empty`) aunque el servidor dé `VALID`; ordenar por un `COUNT` o por un decimal sin agregar funciona, y también agregar y luego ventana. Ordenar por `SUM` no es un caso comparable (el emulador no falla); el flujo ordena por `n`.

**Escenario de normalización (2026-11-24, sin UI).** `python scripts/e2e_ventas.py --escenario normalizacion`: `fechas_sucias` y `numeros_sucios` (20 filas con formatos mezclados) → `CONVERT_TO_DATE` (auto) y `CONVERT_TO_NUMBER` → unión por `id` → orden. Las fuentes ya estaban registradas en el flujo `normalización` del espacio: copiarlo (el Bridge permite copiar cualquier flujo si la copia se llama `emu_*`) evita el editor. Tres comportamientos de Qlik que el emulador no tenía, medidos con las 20 filas y ya emulados (el emulador reproduce las 100 celdas del tenant): (1) **Qlik guarda cada valor distinto una sola vez**: dos textos que interpreta como el mismo número o la misma fecha salen con el primer texto leído (`1,200.50` sale como `1200.50` si antes hubo un `1200.50`; `09/09/2026` como `2026-09-09`; `2026-09-09T14:37:24` como `2026-09-09 14:37:24`), también en las columnas que solo pasan de largo. (2) **`CONVERT_TO_NUMBER` es estricto**: `num(num#([c], '#', '.', ','))` solo acepta un número bien formado (miles con coma en grupos de 3); `10,5`, `1.200,50`, `1 234,56`, `$1,234.56` y `NaN` dan vacío, `1,234` da `1234`, `+250.5` da `250.5`. (3) **Fechas automáticas** (`Date(Floor([c]))`): se reconocen `YYYY-MM-DD`, `M/D/YYYY`, con hora `YYYY-MM-DD hh:mm:ss` y con `T`; no `2026/09/09`, `09-09-2026`, `09-SEP-2026`, `15.07.2026` ni `M/D/YYYY hh:mm`.

**Escenario de calidad (2026-11-24, sin UI).** `python scripts/e2e_ventas.py --escenario calidad` reutiliza el clon de `normalizacion` (mismas fuentes, 20 filas): `fechas_sucias` → `CONVERT_TO_DATE` → `EXTRACT_DATE_PARTS` → `MODIFY_DATES` (+7) → `FORMAT_DATES` → `CUT`; `numeros_sucios` → `CONVERT_TO_NUMBER` → filtro `>= 0` con salida `REJECT` → `ROUND` / `ABSOLUTE` → `UNION`; `JOIN` por id. Una ejecución dio tres diferencias, ya corregidas, y la segunda coincide en las 12 columnas. (1) **`EXTRACT_DATE_PARTS` sobre una fecha convertida aplica el patrón al texto M/D/YYYY de la fecha** (con `M/d/yyyy` da 2026, 9, 9; con un patrón ISO daría vacío); el emulador lo hace y `_jfmt` entiende `M` y `d` sueltos. (2) **Las expresiones ven el texto de cada fila; la unificación de valores iguales la hace la recarga del CSV**, no el flujo: `CUT` sobre `09/09/2026` conserva `09/09/2026`, mientras que `fecha_raw` de esa fila sale `2026-09-09`. El emulador unifica ahora al escribir, no al leer la fuente (las 129 huellas locales no cambian). (3) **Con `ROUND` de precisión 0 y un `UNION` con otra rama que escribe la misma columna, el formato de `ROUND` alcanza a la otra rama**: `ABSOLUTE(-45.75)` sale `46`. Medido en un solo escenario: el emulador registra los decimales fijos por nombre de columna también con precisión 0. Las filas con `numero` vacío salen vacías en las dos ramas (el filtro las rechaza y `ABSOLUTE` de vacío es vacío). `UNCHANGED` en la respuesta del `PUT` significa que el grafo ya estaba subido y es válido.

**Estado (2026-11-24).** Lo verificado contra el tenant está en 9 quater (129 casos de batería, todos coincidentes). Para usar el emulador con flujos reales faltan, por orden de impacto:
- **Fuentes de base de datos.** El `.dfw` desidentificado no trae tipos ni datos: `dfemu coverage --stub` comprueba la forma del flujo con 20 filas enteras, pero con datos reales hay que dar una conexión `duckdb`/`sqlite`/`postgres` (`--connections`). Con `--stub`, 8 de los 11 flujos con conexión dan `no concluyente` por tipos y 3 no se pueden ni intentar (la fuente no trae tablas).
- **Variantes sin emular** (no están en la interfaz o no se pueden rellenar): `FORMAT_MONEY`, `NUMERIC_OPS`, `COMPARE_DATES`, `DATE_FROM_PARTS`, `FUZZY_MATCHING`, `EXTRACT_VALUES_BY_REGEX`; `FORMAT_DATES` con cualquier valor que no sea `YYYYMMDD_DASH`/`YYYYMMDD` (el servidor da 500), `MODIFY_DATES` contra otra columna, `CUT` solo `EQUALS` y `CONTAINS`.
- **`pivot` por API: medido y descartado** (2026-11-27). Se probo a inventar el `schemaEntityId` como se hace con `calculate-fields`: el `PUT` devuelve 500 envolviendo un `400 BAD_REQUEST` de Dataflow Apps. Control con el mismo grafo cambiando solo el processor: con `filter` da `VALID`, asi que el rechazo es del `pivot` y no del grafo. Sigue haciendo falta un `schemaEntityId` emitido por la interfaz.
- **`SUBSTRING` ya usa la configuracion real** (2026-11-27). Antes cortaba siempre `1, 5` ignorando el processor. Lo que genera Qlik (leido del script que devuelve el servidor, no supuesto): sin claves, `Mid(c, 1, 5)`; `FROM_INDEX i` empieza en `i + 1`; `FROM_N_BEFORE_END n` empieza en `Len(c) - (n - 1)` y envuelve en `Coalesce(EmptyIsNull(...), c)`; `TO_INDEX n` da largo `n` desde el inicio o `n - i + 1` desde indice; `TO_N_BEFORE_END n` da largo `Len(c) - n`; `FROM_BEGINNING` + `TO_END` no emite nada (el campo pasa igual). Casos `sub_index_index`, `sub_index_end`, `sub_n_before_end` y `sub_to_n_before`: los cuatro coinciden con el tenant (el de `FROM_N_BEFORE_END` fallo primero por un caracter y se corrigio con esa medicion).
- **`CUT` con `STARTS_WITH` y `ENDS_WITH` ya esta emulado y medido** (2026-11-27): el enum del servidor acepta ambos operadores (`VALID`) y los casos `cut_starts`/`cut_ends` coinciden con el tenant; el emulador corta el prefijo o el sufijo solo cuando coincide. Queda `shortcut:` solo por las variantes con regex.
- **Catalogo de datasets y fuente propia** (2026-11-27). `GET v1/data-sets/{id}` si existe y devuelve el objeto del catalogo: `name`, `qri` (`qdf:qix-datafiles:...`), `spaceId`, `dataAssetInfo` (con `dataStoreInfo.id/name/type`), `schema.dataFields[]` (nombre, `dataType.type`, `index`, `primaryKey`) y `operational` (`location` = id del archivo, `rowCount`, `size`, `status`). `POST v1/data-sets` valida con Bean Validation y pide `technicalName` y `dataAssetInfo`, asi que registrar un dataset es factible. Lo que sigue cerrado es el nodo fuente: `GET v1/dataflow-apps/{app}/datasources/{id}` devuelve la forma del datasource (`sourceId` = el `entityId` del nodo, `datasetId`, `qri`, `connections`, `tables[].fields[].id`), pero `POST v1/dataflow-apps/{app}/datasources` responde `ADF-500` con `{}`, con `{"datasetId"}` y con `{"datasetId", "sourceId"}`. Es el mismo muro que `pivot`, `map-fields` y `subflow`: el cuerpo real solo se puede copiar capturando la interfaz. Medido sobre el clon `emu_probe_src`, borrado despues.
- **`GET v1/dataflows/components/definitions?componentType=X&nodeType=processor`** (2026-11-27): el endpoint que usa la interfaz antes de crear un nodo. Devuelve la definicion exacta de cada processor — `type`, `properties.configuration` inicial y `handles` — sin inventar nada. Medido para `pivot` (`fieldToPivot`, `valueField`, `aggregation: ONLY`, `delimiter`), `map-fields`, `subflow` (`dataflowId`), `script`, `unpivot` y `join`. Es la forma correcta de descubrir la configuracion (mejor que provocar errores); expuesto como `dfemu_processor_definition` en el MCP.
- **`pivot` por API: el nodo se crea, pero necesita `schemaEntityId`** (2026-11-27, corregido). Con el cuerpo real (el de `processors.json` + handles con ids) el `PUT` **no** da 500: el nodo entra y el servidor responde `INVALID` con `VALUE_MISSING_ON_REQUIRED_FIELD` en `parameters.attributePath: /schemaEntityId` sobre el nodo pivot. Ese campo lo crea la interfaz al configurar y aplicar el nodo; no aparece en ningun nodo de un flujo sin pivots configurados, asi que para pivot sigue haciendo falta un arrastre en la interfaz (una vez) o copiar el `schemaEntityId` de un pivot ya configurado. El 500 de las pruebas anteriores venia de inventar ese campo, no de la forma del nodo.
- **`v1/items` se trunca a 100** y `Remote.list_dataflows` no pagina: en este tenant (52 flujos, >100 apps) un clon recien creado no aparece en el listado y `dfemu reload`/el MCP decian que no existia. La interfaz filtra por nombre (`v1/items?resourceType=app&limit=100&name=...`), y desde 2026-11-27 `Remote.find(name)` hace lo mismo antes de recorrer el listado.
- **Aristas en este build**: el grafo exportado usa aristas `{id, sourceHandle, targetHandle}` (sin `source`/`target`), y la interfaz no pinta `g.react-flow__edge`, asi que `dfemu ui add --on <arista>` no encuentra el punto medio. Alternativa medida: arrastrar la tarjeta al lienzo a mano y conectar; `dfemu flow capture` graba el `PUT` con el nodo resultante.
- **Editar el grafo por API desde el MCP, medido** (2026-11-27): sobre un clon `emu_mcp_probe` de `emu_e2e_calidad`, `dfemu_flow_add_node` inserta el nodo (5 nodos) y el servidor responde `INVALID` con `VALUE_MISSING_ON_REQUIRED_FIELD` mientras el processor nuevo no tiene columnas, que es lo esperado; `dfemu_flow_remove_node` del mismo nodo devuelve `VALID` y 4 nodos. El clon se borro despues. O sea: alta, baja y modificacion de nodos funcionan por API sin la interfaz, incluido el `PUT` con reintento de `POTENTIAL_STALE_EXPRESSION`.
- **Recarga de una app por API (`v1/reloads`)** (2026-11-27). `POST v1/reloads {"appId": ...}` responde el objeto de recarga (`id`, `status: QUEUED`, `creationTime`, `type`, `weight`) y `GET v1/reloads/{id}` pasa por `RELOADING` hasta `SUCCEEDED` o `FAILED`; en `FAILED` el campo `log` trae el error del motor (medido: `Cannot open file: 'lib://...GDDestino/emu_e2e_ventas.csv' (Connector error: Expecting a file path of format {folderId}/{fileName})`) y en `SUCCEEDED` la ultima linea es el recuento (`In total 60 rows stored.`). Medido en `emu_e2e_calidad` (`QUEUED / RELOADING / SUCCEEDED`) y en `emu_e2e_ventas`/`emu_e2e_normalizacion` (fallan por destino y por script, con el error en el log). El `appId` no se valida en el POST: pasar un nombre de flujo devuelve un id de recarga que luego da 404 al consultarlo, asi que `dfemu reload` resuelve primero el nombre a id (esta en `emulator/reload.py` y en el CLI).
- **`MODIFY_DATES`: las nueve unidades y el valor fijo estan medidas** (2026-11-27). El enum real de `timeUnit` es `[MONTH, MILLISECOND, HOUR, MICROSECOND, DAY, YEAR, MINUTE, SECOND, WEEK]` y el de `useWith` `[VALUE, FIELD]`, ambos sacados del error de deserializacion. Lo que emite Qlik, leido del script: `YEAR` → `AddYears([c], n)`, `MONTH` → `AddMonths([c], n)`, `WEEK` → `Date([c] + n * 7)`, `DAY` → `Date([c] + n)`, y las sub-dia `IF(Floor(Timestamp([c])) = Floor(Timestamp('00:00:00')), time([c] + (n / 24)), Timestamp([c] + (n / 24)))` con el divisor 24 / 1440 / 86400 / 86400000 / 86400000000 segun `HOUR`/`MINUTE`/`SECOND`/`MILLISECOND`/`MICROSECOND`. Casos `mod_year`, `mod_month`, `mod_week`, `mod_hour`, `mod_minute` y `fecha_sumar_dias` coinciden con el tenant. `useWith: FIELD` genera `Date([c] + [columna])`, pero no se puede medir con `clientes`: `cedula` desborda el rango de fechas y `cliente_id`/`telefono` son texto, asi que queda como shortcut.
- **`FORMAT_DATES`: `YYYYMMDD_DASH` y `YYYYMMDD` estan medidos** (2026-11-27). El campo `format` no valida contra un enum: `YYYYMMDD_SLASH`, `DDMMYYYY_DASH`, `DDMMYYYY_SLASH`, `MMDDYYYY_DASH`, `DD_MMM_YYYY`, `YYYY_MMM_DD`, `MONTH_NAME` y `YYYY_MM_DD` dan 500 (no un error de deserializacion), asi que solo se sabe que existe lo que responde. Qlik genera `Date([c], 'YYYY-MM-DD')` y `Date([c], 'YYYYMMDD')`; casos `fecha_formato` y `fecha_formato_num`, ambos coincidentes.
- **`PADDING` usa `size`, `paddingCharacter` y `paddingPosition`** (2026-11-27). Lo que genera Qlik es `Repeat(ch, size - Len([c])) & [c]` con `LEFT` y `[c] & Repeat(ch, size - Len([c]))` con `RIGHT` (sin `greatest`, asi que cuando el dato ya es mas largo el relleno queda en cero caracteres y no trunca). Nombres descartados midiendo (el servidor da `VALID` pero los ignora): `character`, `cushionValue`, `characterValue`, `position`, `length`, `targetLength`. Casos `pad_size8`, `pad_right`, `pad_short` (size 3 sobre ciudades mas largas: cubre la cuenta negativa) y `pad_left_x`: los cuatro coinciden con el tenant.
- **`MATCHES_PATTERN`: los cinco patrones con nombre estan medidos** (2026-11-27). El enum real, sacado del error `Cannot deserialize ... from String`, es `[OTHER, ANY_LITERAL_WITH_ALPHA_NUMERIC_CHARACTERS, ANY_WORD_CASE_INSENSITIVE, NUMBER, A_WORD_IN_LOWERCASE, A_WORD_IN_UPPERCASE]`, y el regex que emite Qlik (leido del script) es: `ANY_WORD_CASE_INSENSITIVE` `^[a-zA-Z]+$`, `ANY_LITERAL_WITH_ALPHA_NUMERIC_CHARACTERS` `^[a-zA-Z0-9]+$`, `NUMBER` `^[0-9]+$`, `A_WORD_IN_LOWERCASE` `^[a-z]+$`, `A_WORD_IN_UPPERCASE` `^[A-Z]+$`, todos con `IF(CountRegEx([c], regex), Dual('TRUE', -1), Dual('FALSE', 0)) AS [c_matching]`. Casos `pat_alnum`, `pat_numero`, `pat_mayus`, `pat_minus` y `str_patron`: coinciden con el tenant. `OTHER` da 500 con `otherPattern`, `customPattern`, `pattern`, `regex`, `otherValue`, `literalPattern` y `customRegex`, asi que el nombre de su campo solo se puede averiguar capturando lo que manda la interfaz.
- **`COMPARE_NUMBERS`: los seis operadores y el valor constante estan medidos** (2026-11-27). El enum real del servidor es `[LESS_THAN_OR_EQUAL, GREATER_THAN_OR_EQUAL, GREATER_THAN, LESS_THAN, NOT_EQUALS, EQUALS]` (lo devuelve el propio error `Cannot deserialize ... from String`: `LESS_OR_EQUAL` y `GREATER_OR_EQUAL` no existen, son `*_THAN_OR_EQUAL`). Lo que genera Qlik es `IF([c] <op> valor, Dual('TRUE',-1), Dual('FALSE',0))`, y el emulador lo replica con `CASE WHEN TRY_CAST(c AS DOUBLE) <op> valor THEN 'TRUE' ELSE 'FALSE' END`. Casos `cmp_gt`, `cmp_ne`, `cmp_le`, `cmp_ge`, `cmp_lt` y `cmp_eq` (comparando `cedula` contra 100): los seis coinciden con el tenant en contenido y en las 8 primeras filas. Lo que sigue sin medir es `comparisonType: OTHER_COLUMN` (comparar contra otra columna): su enum solo admite `[VALUE, OTHER_COLUMN]`, pero `OTHER_COLUMN` responde `VALUE_MISSING_ON_REQUIRED_FIELD` con cualquier nombre de campo que se pruebe (`column`, `comparisonColumn`, `otherColumn`, `columnName`, `compareColumn`, `columnToCompare`, `valuesColumn`, `field`) y con `constantValue` presente o ausente, asi que el nombre del campo solo se puede averiguar capturando lo que manda la interfaz.
- **`EXTRACT_VALUES_BY_REGEX` y `COMPARE_DATES` no existen en este servidor** (2026-11-27): el primero no es un valor de `StringsFunctionType` (`Cannot deserialize ... from String`), el segundo da 500. No son huecos del emulador sino nombres de la ayuda que el servidor rechaza.
- **`pivot`**: no queda ni el recurso de reutilizar un `schemaEntityId`. Escaneados los 52 flujos que ve la credencial (23 legibles; el resto da error de permiso), **ninguno tiene un nodo `pivot`**, asi que hoy no hay donante y el nodo solo se puede crear desde la interfaz. Tambien se midio que la API no documenta ninguna ruta de `data-entities`: el `entityId` de una fuente sigue naciendo en el editor.
- **`subflow`**: no medible por API en este tenant: ninguno de los 23 flujos legibles trae `subflows`, y sin un flujo que los tenga no hay forma de crear el nodo (la interfaz no ofrece recetas de tabla por API).
- **`map-fields`** (Asignar campos): esta en el catalogo porque se descubrio por la interfaz, pero su `configuration` (`mapFrom`, `mapTo`, `defaultValue`, `columnsToProcess`) no explica contra que columna de la entrada LOOKUP empareja y la ayuda de Qlik no lo documenta; no se emula por no adivinar la semantica.
- **Qlik Automate verificado contra el tenant** (2026-11-27): ciclo completo por API sobre la ruta vigente `workflows/automations` (la CLI ya antepone `/api`; `api/v1/automations` esta deprecada). La lista llega como array pelado (no envuelta en `data`). Ciclo medido: crear `emu_*` -> `state: available`; `enable`; `POST .../runs` exige `{"context": "api"}` (sin el: `The context field is required`); el run pasa de `not started` a `finished`; `GET .../runs` lo lista; `DELETE` lo borra y desaparece del listado.
- **Nodo `script` verificado de punta a punta** (2026-11-27): sobre el flujo `normalizacion` (unico con nodos `script` accesibles, junto con `Repaso Dataflow_Byron`) se creo el nodo en un clon `emu_*` reutilizando su `schemaEntityId`, el servidor dio `VALID` y genero el script de 38 lineas; ejecutado en la app oraculo y comparado con la traduccion local: **sin diferencias**. De ahi salio un hueco real del traductor: `Date(Floor([c]))`, que es justo lo que genera Qlik al convertir un campo, no se traducia; ahora usa el reconocimiento automatico de formatos (`_AUTO_DATES`).
- **`fork` y `union` ya estan medidos** (2026-11-27): caso `fork_union` de la bateria (`clientes` -> fork -> dos filtros disjuntos -> `union` con `unionAll` -> orden -> destino), 7 nodos, coincide con el tenant en contenido y en las 8 primeras filas.
- **`sample` ya esta medido** (2026-11-27): caso `sample_first` de la bateria (`SAMPLE_FIRST_ROWS` con 5 filas) coincide con el tenant en contenido y en las 8 primeras filas. `SAMPLE_RANDOM_ROWS` y `SAMPLE_N_RANDOM_ROWS` usan semilla fija en el emulador y aleatoria en Qlik, asi que no son comparables por contenido (solo por numero de filas).
- **`pivot`** y el **nodo `script`** (el emulador solo lo traduce).
- **Atajos con límite** (marcados `shortcut:` en el código): formato de fecha solo en-US, números de 1e14 o más, `MATCHES_PATTERN` con `OTHER` y `COMPARE_NUMBERS` contra otra columna, orden de empates en ventanas; `COUNT_DISTINCT` con rango (solo se midió sin rango).

- Modificar la receta dentro de un subflow (`PUT v1/dataflows/{id del subflow}`): no se probó; hoy el subflow se toma del flujo base (ver 5 bis).
- Import y export de `.dfw` con archivo: ver 10 quinquies. OAuth no era necesario (la API key sirve); falta obtener el id de la subida a `temp-contents` (viene en la cabecera `Location`, que la CLI no muestra) y la descarga del archivo exportado.
- Cliente OAuth `dfemu-prueba`: ya borrado en el tenant y el contexto `dfemu-oauth` ya no está en la CLI (2026-11-23). Si hace falta otro, la guía es `02-guia-oauth.md`.
- Comparar línea a línea el script de un clon con el original (se observó que difieren sin analizar por qué).
- Orquestación: ver "Pendiente de esta fase" en el apartado 10 ter (`usage` en tareas avanzadas, flujos reales).
- Limpieza de archivos escritos en carpetas de Google Drive (`GDDestino`): `dfemu cleanup` solo cubre `DataFiles` y no hay API de Qlik para listar o borrar en un conector de Drive; se borran a mano.
- Crear fuentes nuevas en un flujo: el `entityId` de cada nodo fuente es propio del flujo y no se encontró cómo registrar una (ver 9 ter).
