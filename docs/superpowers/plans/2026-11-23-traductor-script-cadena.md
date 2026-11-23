# Traductor de script: cadena de tablas, joins y agregaciones — plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (ejecucion nativa, una sola sesion). Los pasos usan `- [ ]`.

**Goal:** que `dfemu translate` traduzca a SQL de DuckDB los scripts que Qlik genera para flujos con `RESIDENT`, `LEFT/INNER/OUTER JOIN` y `GROUP BY`, y que `--run` los ejecute localmente.

**Architecture:** `emulator/script.py` pasa de "un LOAD por script" a un catalogo de tablas con nombre. Cada sentencia `[T]: LOAD ... (FROM csv | RESIDENT [X]) [WHERE] [GROUP BY]` crea una vista `T`; `JOIN([T]) LOAD ...` reemplaza `T` por el join; `DROP` se ignora; el resultado es la tabla del `STORE` (o la ultima si no hay). La salida sigue siendo UN SQL (`WITH ... SELECT`), asi `run` y `cli` no cambian.

**Tech Stack:** Python 3.12, DuckDB, pytest (ya instalados).

**Spec:** `docs/superpowers/specs/2026-11-19-banco-de-pruebas-design.md` (fase 5, "Quedan `RESIDENT`, joins, agregaciones y expresiones").

## Global Constraints

- Todo lo no reconocido se marca "no traducible" con motivo; nunca se adivina (principio del repo: el servidor es el juez).
- Los textos se recortan al leer CSV (ya implementado en `_reader`).
- Sin dependencias nuevas; las pruebas locales no usan red ni tenant.
- Los atajos con limite conocido llevan comentario `shortcut: <limite>, <cuando mejorar>`.

## Review Focus

- Join sin campos en comun: Qlik hace producto cartesiano; aqui se marca no traducible.
- Join con campos en comun de distinto tipo (texto vs numero): se compara tal cual; documentar.
- `GROUP BY` con campos de salida que no son clave ni agregacion: no traducible.
- `Sum` sobre solo nulos: la documentacion de Qlik no dice si da 0 o NULL; se deja NULL (SQL) y se marca sin verificar.
- Nombres de tabla con espacios y acentos (`[Unir 1]`, `[Seleccionar campos 1]`).

## Datos de partida (corpus real, `out/corpus_all/*.pull.json`)

Forma observada: `[Unir 1]: NOCONCATENATE LOAD ... FROM [lib://...csv] WHERE ...;`, `LEFT JOIN([Unir 1]) LOAD ... FROM ...;`, `[T2]: NOCONCATENATE LOAD ..., Upper([x]) AS [x] RESIDENT [Unir 1]; DROP TABLE [Unir 1];`, `... Sum([a]) AS [b] ... GROUP BY [k1], [k2];`. Funciones vistas: Sum, Avg, Count(DISTINCT), Upper, Trim, Year, Month, IsNull, Coalesce, If, Match, SubField, Num.

## Task 1: Cadena de tablas con RESIDENT y campos con alias

**Files:** Modify `emulator/script.py` (`translate`); Test `tests/test_script.py`.

**Interfaces:** Produces `translate(text, data_dir) -> (sql | None, reasons)` (firma intacta); internamente `_tables: dict[str, str]` nombre -> SQL de la subconsulta.

- [ ] Test `test_translate_resident_chain`: script con `[A]: LOAD ... FROM csv WHERE ...; [B]: NOCONCATENATE LOAD [x] AS [y], [z] RESIDENT [A]; DROP TABLE [A]; STORE [B] INTO ...;` sobre un CSV de 3 filas; `run(sql)` devuelve las columnas `y, z` y solo las filas filtradas.
- [ ] Test `test_translate_unknown_resident_is_reported`: `RESIDENT [Nope]` => `sql is None` y un motivo que contiene `Nope`.
- [ ] Ejecutar: deben fallar (hoy `RESIDENT` => "LOAD sin FROM").
- [ ] Implementar: refactor de `translate` en `_load_statement(st) -> (name, select_sql)` y ensamblado `WITH "A" AS (...), "B" AS (...) SELECT * FROM "<destino>"`; destino = tabla del primer `STORE`, si no la ultima. Mantener los tests existentes (un LOAD sin nombre sigue funcionando).
- [ ] Ejecutar `python -m pytest tests/test_script.py -q`: todo verde.
- [ ] Commit.

## Task 2: JOIN (LEFT / INNER / OUTER) por campos en comun

**Files:** Modify `emulator/script.py`; Test `tests/test_script.py`.

**Interfaces:** Consumes `_load_statement` y `_tables` de la Task 1. Produces `_join(kind, left_sql, right_sql) -> sql` (claves = columnas en comun, usando `USING`).

- [ ] Tests con dos CSV: `test_translate_left_join` (fila sin pareja queda con NULL), `test_translate_inner_join` (fila sin pareja se descarta), `test_translate_join_without_common_fields_is_reported`.
- [ ] Ejecutar: fallan.
- [ ] Implementar la sentencia `(LEFT|INNER|RIGHT|OUTER) JOIN([T]) [// comentario] LOAD ... FROM csv [WHERE]`: reemplaza `_tables[T]` por `SELECT * FROM T <kind> JOIN (<load>) USING (<comunes>)`; las comunes se calculan con `DESCRIBE` de ambos lados. `OUTER` => `FULL`. Sin comunes => motivo "join sin campos en comun".
- [ ] Ejecutar `python -m pytest tests/test_script.py -q`: verde.
- [ ] Commit.

## Task 3: Expresiones y GROUP BY

**Files:** Modify `emulator/script.py` (`_field`, nueva `_expr`); Test `tests/test_script.py`.

**Interfaces:** Produces `_expr(item: str) -> str | None` (SQL o None si no soportada).

- [ ] Tests parametrizados por funcion: `Upper`, `Trim`, `Year`, `Month`, `IsNull`, `Coalesce`, `If(cond, a, b)` => cada uno con su `AS [alias]` y el valor esperado ejecutando `run`.
- [ ] Tests de agregacion: `Sum`, `Avg`, `Count(DISTINCT [x])` con `GROUP BY [k]`; `test_group_by_with_free_field_is_reported`.
- [ ] Ejecutar: fallan.
- [ ] Implementar `_expr` con tabla `{funcion Qlik: plantilla DuckDB}` y parentesis balanceados (reusar `_split_top`); la sentencia con `GROUP BY` exige que todo campo no agregado este en la lista de claves. Lo no reconocido => motivo `expresion no soportada: ...`.
- [ ] Ejecutar `python -m pytest -q`: toda la suite verde.
- [ ] Commit.

## Task 4: Medicion contra el corpus y documentacion

**Files:** Modify `docs/banco-de-pruebas/01-hallazgos-api-qlik.md` (seccion de `translate`, tabla de pendientes), `docs/superpowers/specs/2026-11-19-banco-de-pruebas-design.md` (fase 5).

- [ ] Correr `translate` sobre `out/corpus_all/*.pull.json` y anotar cuantos pasan de 3 a N y los motivos que quedan (esperado: `LIB CONNECT`/`SELECT` de BigQuery y Postgres, que no se pueden ejecutar sin conexion).
- [ ] Actualizar fase 5 y "Pendiente" con los numeros reales. Commit.

## Fuera de alcance (a pedir aparte)

- Verificar contra el tenant (`dfemu compare`): crea objetos `emu_` y requiere `--apply`.
- `Window`/`WRank`, `SubField`, `IndexRegEx`, `Match`: aparecen una o dos veces; se agregan cuando un flujo los necesite.
- Orquestacion (fase 6) y subflows en `PUT`.
