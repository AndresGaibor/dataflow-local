# Banco de pruebas de Data Flows y Qlik script — diseño

Estado: **borrador para aprobación**. Evidencia técnica en `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`.

## 1. Intención y por qué

El usuario quiere que este repo sea su **banco de pruebas** para Data Flows y Qlik script, y a la vez la herramienta con la que **automatiza** su ciclo completo contra Qlik Cloud real: descargar flujos, validarlos, modificarlos y subirlos, de forma segura. Hoy el repo es un emulador local (DuckDB) que valida y ejecuta `.dfw`, pero no habla con Qlik, no ejecuta Qlik script y cubre solo un subconjunto de processors. Sin un juez real, no se sabe si el emulador acierta.

## 2. Objetivos, no objetivos y antiobjetivos

**Objetivos**
- Cada processor documentado en `docs/DataFlow/` tiene emulación local y al menos un caso comparado contra Qlik real.
- Cada construcción de Qlik script que aparezca en el corpus (flujos reales y scripts propios) se ejecuta localmente o queda marcada como "solo en tenant".
- Un comando por acción del ciclo: descargar, validar (local y servidor), subir, ejecutar, comparar, limpiar. Con códigos de salida y reportes JSON aptos para CI.
- "100%" se mide: porcentaje del corpus en el que emulador y Qlik coinciden, y cobertura de processors y funciones. Nunca "cubre todo el lenguaje".

**No objetivos**
- No es un motor Qlik completo: lo que el emulador no pueda traducir se ejecuta en el tenant.
- No reemplaza la interfaz de Qlik, ni toca producción.

**Antiobjetivos (fallo aunque funcione)**
- Sobrescribir una salida o modificar un flujo original.
- Operar fuera de "Entrenamiento Dataflow".
- Dejar claves en el repo.

## 3. Restricciones verificadas

- Credencial actual: API key de `AnalyticsAdmin`. `v1/dataflows/actions/import|export` dan 403.
- La CLI debe ejecutarse con `< /dev/null` (si no, se cuelga).
- Subir grafos con subflows daña el clon; hay que descartarlo.
- El clon de un flujo escribe en el mismo destino (Google Drive) que el original.
- No se pueden descargar archivos de salida; se leen cargándolos en un app y consultando con `qlik app eval`.
- El script de Qlik fusiona nodos: la comparación es de resultados, no de texto.

## 4. Enfoques considerados

| | Idea | Costo / riesgo |
|---|---|---|
| A | Emulador como centro; el tenant solo compara | El script nunca se cubre; esfuerzo sin techo |
| **B** | **Tenant como juez, emulador como acelerador local** | Depende de red para validar; cubre el script por partes |
| C | Todo a script; ejecutar siempre en el tenant | Hay que replicar el generador de Qlik; sin pruebas locales rápidas |

**Elegido: B** (recomendado por el asistente; el usuario continuó sin objetar). Razón: es la única que alcanza "100%" donde importa, porque el motor real decide y el emulador da velocidad. El diseño del puente se apoya en los endpoints ya verificados.

## 5. Arquitectura (Python, sobre lo que ya existe)

Se mantiene `emulator/` (validar, ejecutar) y se añade, sin rehacer lo existente:

1. **`bridge`**: cliente del tenant sobre `qlik raw` (stdin cerrado, tiempo límite, reintentos). Es el único punto que habla con Qlik. Incluye la **capa de seguridad**: lista de espacios permitidos (solo "Entrenamiento Dataflow"), prefijo `emu_` obligatorio al crear, solo borra objetos `emu_`, modo simulación por defecto (muestra la llamada y no la ejecuta hasta `--apply`), bitácora de cada escritura, y rechazo de cualquier ejecución cuyo `STORE` apunte fuera de `DataFiles/emu_*`.
2. **`pull`**: descarga un flujo (`GET v1/dataflows`) a `.dfw` y guarda su script y su `validity`. Crea el corpus de los 47 flujos.
3. **`push`**: clona un flujo base con nombre `emu_*`, reemplaza el grafo (`PUT`), devuelve `validity` y el script generado. Un clon por subida; si hay subflows o falla el `PUT`, descarta el clon.
4. **Oráculo de validez**: la `validity` del servidor sobre una batería de mutaciones; calibra `emulator/dfw.py` (enums, comprobación de fuentes). Meta: cero discrepancias en la batería.
5. **Oráculo de ejecución**: toma el script de Qlik, redirige los `STORE` a `DataFiles/emu_*`, agrega el `LOAD` del resultado, ejecuta (`POST v1/reloads`) y lee tablas y filas con `qlik app tables|eval`.
6. **Comparador**: resultado del emulador frente al del tenant (filas, tipos, agregados por columna, filas completas si son pocas) con un informe de diferencias.
7. **Traductor de Qlik script a SQL (DuckDB)**: por construcciones y guiado por el corpus; lo no soportado se marca y se ejecuta solo en el tenant. Lo existente (`qexpr`, 12 funciones) es el punto de partida.
8. **CLI `dfemu`** con subcomandos `pull`, `validate [--remote]`, `push`, `run [--local|--remote]`, `compare`, `calibrate`, `cleanup`, y reporte JSON.

## 6. Orden de entrega

1. `bridge` con seguridad, `pull` y validación remota. **Hecho** (2026-11-19).
2. Oráculo de validez y calibración de `emulator/dfw.py`. **Hecho** (2026-11-19).
3. `push` y oráculo de ejecución con comparador sobre los flujos simples (`fundamentos*`). **Hecho** (2026-11-19): `dfemu compare` sin diferencias contra el tenant.
4. Cobertura de processors del emulador, guiada por diferencias (pivot, unpivot, math, strings, window, date...). **Parcial** (2026-11-19): `dfemu coverage` mide el corpus y se cerraron las variantes reales que faltaban (`strings.UPPERCASE`, `REPLACE_ON_VALUE` con `STARTS_WITH`, `REPLACE_CELL_WITH_VALUE` con `EQUALS`). `pivot`, `unpivot`, `map-fields` y `clear-cells` siguen sin emulación porque ningún flujo real trae su configuración.
5. Traductor de Qlik script por construcciones, medido contra el corpus. Pendiente.
6. Orquestación (programación de tareas `DATAFLOW_PREP`, encadenado), CI y empaquetado. **Parcial** (2026-11-19): CI con GitHub Actions ejecuta la suite local en cada push; la orquestación sigue pendiente.

Cada fase deja pruebas en `tests/` y actualiza `docs/banco-de-pruebas/`.

## 7. Decisiones tomadas por el asistente (a revisar)

- Lenguaje Python y DuckDB (lo que ya usa el repo).
- Todo acceso al tenant pasa por `qlik raw` (credencial ya configurada, sin manejar claves).
- La suite de pruebas contra el tenant es opcional (se activa con una variable de entorno); las pruebas locales no necesitan red.
- Los reportes se guardan en `out/` (ya ignorado por git).

## 8. Lo que queda al constructor y preguntas abiertas

- Cómo subir grafos con subflows sin dañar el clon (probar un campo `subflows` en el `PUT`).
- Cómo cambiar el destino de un flujo clonado de forma robusta antes de ejecutarlo.
- Si una credencial OAuth habilita import/export de `.dfw`.
- Límite de velocidad de la API para la batería de mutaciones.
- Política de limpieza de objetos `emu_`: implementada a demanda con `dfemu cleanup [--apply]`; borra solo apps y archivos `emu_*` del espacio permitido.
