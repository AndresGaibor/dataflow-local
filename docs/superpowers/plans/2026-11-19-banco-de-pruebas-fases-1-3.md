# Banco de pruebas, fases 1 a 3: puente seguro, calibración y oráculo de ejecución

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** que `dfemu` hable con Qlik Cloud de forma segura (descargar, validar, subir, ejecutar y comparar flujos contra el emulador local), y que el validador local coincida con el del servidor.

**Architecture:** `Bridge` es el único punto que invoca la CLI `qlik` y aplica la política de seguridad. `Remote` (operaciones de flujo), `calibrate` (validez), `oracle` (ejecución de scripts en el tenant) y `compare` (huellas de resultados) se apoyan en él. Las pruebas unitarias usan un `FakeRunner`; las pruebas contra el tenant son opcionales.

**Tech Stack:** Python 3.12, DuckDB, pytest, CLI `qlik` v4.0.0 (`qlik raw`, `qlik app script set|tables|eval`).

**Spec:** `docs/superpowers/specs/2026-11-19-banco-de-pruebas-design.md` (fases 1 a 3 del orden de entrega). Evidencia de la API: `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`. Las fases 4 a 6 (cobertura de processors, traductor de Qlik script, orquestación y CI) tendrán planes propios cuando estas fases entreguen resultados. Los subcomandos `push` y `run --remote` del diseño no se crean aparte: `validate --remote` y `compare --push` cubren sus casos.

## Global Constraints

- Todo acceso al tenant pasa por `Bridge` (`qlik raw ...`, `qlik app script set|tables|eval`); cada llamada con `stdin=subprocess.DEVNULL` y `timeout=60`.
- Espacio permitido para escribir: el de la variable de entorno `DFEMU_SPACE_ID` (en este documento, `000000000000000000000000`). Todo objeto creado se llama `emu_*`.
- Las escrituras son simulación por defecto; solo se ejecutan con `--apply`. Bitácora en `out/audit.jsonl`.
- Los flujos originales nunca se modifican. Un `STORE` fuera de `lib://Entrenamiento Dataflow:DataFiles/emu_*` nunca se ejecuta.
- Un grafo con nodos `subflow` no se sube (daña el clon).
- Contenido del tenant (flujos descargados, huellas) solo bajo `out/` (ignorado por git). Ninguna clave ni token en el repo.
- Pruebas contra el tenant: marcador `tenant`, solo con `DFEMU_TENANT=1`. Las demás no necesitan red. `python -m pytest -q` debe seguir pasando (35 pruebas actuales).
- El repo no tiene commits: los pasos de commit solo se ejecutan si el usuario ya autorizó commitear; si no, se omiten.

## Review Focus

Entradas o condiciones que el diseño implica y ninguna tarea cubriría sola, de más a menos probable:
1. Escritura con espacio de destino distinto del permitido, o con nombre sin `emu_` (cada tarea que escribe añade la prueba).
2. Un fallo a mitad de `validity_of` o de la ejecución del oráculo debe borrar igualmente el clon, el app y los archivos `emu_` creados.
3. Un script con `STORE` fuera de `DataFiles/emu_*`, o con un `STORE` que no se sabe interpretar.
4. Caracteres no ASCII (`μ` aparece en todos los scripts del tenant) en el cuerpo de la llamada y en el script.
5. La CLI devuelve código distinto de cero, texto que no es JSON o tarda demasiado.

## File Structure

- Create `emulator/bridge.py` (llamadas a `qlik` + política de seguridad), `emulator/remote.py` (operaciones de flujo), `emulator/calibrate.py` (batería de mutaciones), `emulator/oracle.py` (script a tenant), `emulator/compare.py` (huellas y diferencias).
- Modify `emulator/cli.py` (subcomandos), `emulator/dfw.py` y `emulator/runner.py` (calibración), `scripts/make_examples.py` (caso `i08`), `.gitignore` (nada nuevo: `out/` ya está).
- Tests: `tests/fakes.py`, `tests/test_bridge.py`, `tests/test_remote.py`, `tests/test_calibrate.py`, `tests/test_oracle.py`, `tests/test_compare.py`, `tests/test_tenant.py`, `tests/conftest.py` (marcador `tenant`).

---

### Task 1: Bridge con política de seguridad

**Files:**
- Create: `emulator/bridge.py`, `tests/fakes.py`, `tests/test_bridge.py`, `tests/conftest.py`

**Interfaces:**
- Produces:
  - `SANDBOX_SPACE_ID = os.environ.get("DFEMU_SPACE_ID", "000000000000000000000000")`, `PREFIX = "emu_"`.
  - `class SafetyError(Exception)`, `class BridgeError(Exception)` (atributos `rc: int`, `stderr: str`), `class DryRun(Exception)` (atributos `method`, `path`, `body`).
  - `Runner = Callable[[list[str]], tuple[int, str, str]]` (argumentos tras `qlik`; devuelve rc, stdout, stderr). `qlik_runner(args: list[str]) -> tuple[int, str, str]` es el real.
  - `class Bridge(runner: Runner = qlik_runner, apply: bool = False, audit_path: str = "out/audit.jsonl")` con `get(path, query: dict | None = None) -> Any`, `post(path, body: dict | None = None) -> Any`, `put(path, body: dict) -> Any`, `delete(path) -> Any`, `script_set(app_id: str, script: str) -> None`, `cli_read(args: list[str]) -> str` (solo `["app","tables",...]` y `["app","eval",...]`).
  - `tests/fakes.py`: `FakeRunner(routes: dict[tuple[str, str], Any])`; clave `(MÉTODO, ruta)` para `qlik raw` y `("CLI", "app script set")`, `("CLI", "app tables")`, `("CLI", "app eval")` para los comandos de motor; el valor es JSON-able (stdout), o `(rc, stdout, stderr)`, o un callable `f(body) -> valor`. Atributo `calls: list[tuple[str, str, dict | None]]` (método, ruta, cuerpo leído del archivo temporal en el momento de la llamada, decodificado como UTF-8).
  - `tests/conftest.py`: marcador `tenant` que se omite salvo `DFEMU_TENANT=1`.

- [ ] **Step 1: Escribir las pruebas que fallan** en `tests/test_bridge.py`: `test_get_decodes_json`; `test_nonzero_exit_raises_bridgeerror` (el `stderr` viaja en la excepción); `test_non_json_stdout_raises_bridgeerror`; `test_dry_run_raises_dryrun_and_calls_nothing` (apply=False, POST `v1/dataflow-apps/X/actions/copy` válido: lanza `DryRun` y `calls` no contiene ningún POST); `test_copy_outside_sandbox_rejected` y `test_copy_name_without_prefix_rejected` (con `apply=True`, lanzan `SafetyError`); `test_put_dataflow_requires_emu_owner` (rutas: `GET v1/dataflows/DF` → `{"context":{"dataAppId":"A"}}`, `GET v1/apps/A` → atributos con nombre `fundamentos` y espacio permitido ⇒ `SafetyError`; con nombre `emu_x` ⇒ se ejecuta el PUT); `test_delete_app_requires_emu_in_sandbox`; `test_unknown_write_route_rejected` (POST `v1/spaces`); `test_validatescript_allowed_in_dry_run`; `test_audit_line_written` (`tmp_path`); `test_body_roundtrips_utf8` (cuerpo con `"μ"`); `test_script_set_requires_emu_app`; `test_cli_read_rejects_other_commands`; `test_qlik_runner_closes_stdin_and_sets_timeout` (con `monkeypatch` de `subprocess.run`: `stdin is subprocess.DEVNULL` y `timeout == 60`).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_bridge.py -q`. Expected: falla por import.
- [ ] **Step 3: Implementar `emulator/bridge.py`.** Reglas de autorización (todas se evalúan antes de ejecutar y también en simulación): POST `v1/apps` exige `body["attributes"]["spaceId"] == SANDBOX_SPACE_ID` y nombre con `PREFIX`; POST `v1/dataflow-apps/{id}/actions/copy` exige `body["spaceId"]` permitido y nombre con `PREFIX`; PUT `v1/dataflows/{id}` y POST `v1/reloads` y DELETE `v1/apps/{id}` y `script_set` exigen que el app dueño sea `emu_*` en el espacio permitido (se resuelve con `GET v1/apps/{id}`; para el flujo, `GET v1/dataflows/{id}` → `context.dataAppId`); POST `v1/data-files/actions/delete` exige que cada `id` de `body["delete"]` resuelva (`GET v1/data-files/{id}`) a un nombre `emu_*` en el espacio permitido; POST `v1/apps/validatescript` es lectura. Cualquier otra escritura: `SafetyError`. Con `apply=False`, tras autorizar se anota en la bitácora y se lanza `DryRun`. El cuerpo viaja en un archivo temporal UTF-8 con `--body-file`; las consultas como `--query k=v` repetidos.
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest tests/test_bridge.py -q`. Expected: todas pasan.
- [ ] **Step 5: Commit** (si hay autorización): `git add emulator/bridge.py tests/ && git commit -m "feat: bridge con politica de seguridad para Qlik Cloud"`.

---

### Task 2: Descargar flujos (`Remote` lectura y `dfemu pull`)

**Files:**
- Create: `emulator/remote.py`, `tests/test_remote.py`
- Modify: `emulator/cli.py`

**Interfaces:**
- Consumes: `Bridge.get`.
- Produces:
  - `class FlowRef(NamedTuple)`: `name: str`, `app_id: str`, `space_id: str`.
  - `class Remote(bridge: Bridge)` con `list_dataflows(space_id: str | None = None) -> list[FlowRef]` (items con `resourceSubType == "dataflow-prep"`; `GET v1/items` con `resourceType=app` y `limit=100`; si `space_id`, filtra), `dataflow_id(app_id: str) -> str` (`GET v1/dataflow-apps/{app_id}` → `dataflowId`), `script_of(app_id: str) -> str` (`GET v1/apps/{app_id}/scripts/current` → `script`), `pull(app_id: str) -> dict` con claves `appId`, `dataflowId`, `dataflow` (cuerpo de `GET v1/dataflows/{dataflowId}`) y `script`.
  - `emulator.cli.make_bridge(apply: bool) -> Bridge` (función de módulo; las pruebas la sustituyen).
  - Subcomando `dfemu pull [APP_ID] [--all] [--all-spaces] --out RUTA` (por defecto `out/corpus`): escribe `<nombre saneado>.pull.json`; `--all` descarga los flujos del espacio permitido y `--all-spaces` los de todos.

- [ ] **Step 1: Pruebas que fallan** en `tests/test_remote.py`: `test_list_dataflows_filters_subtype_and_space` (items mezclados `dataflow-prep`/`None`; devuelve solo los de flujo y, con `space_id`, solo ese espacio); `test_pull_returns_graph_and_script` (aserciones sobre las cuatro claves); `test_cli_pull_writes_file` (con `cli.make_bridge` sustituido por un `Bridge(FakeRunner(...))`; `tmp_path` contiene `fundamentos.pull.json`); `test_cli_pull_all_defaults_to_sandbox` (con dos espacios en el listado solo se descargan los del permitido).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_remote.py -q`. Expected: FAIL (módulo inexistente).
- [ ] **Step 3: Implementar** `Remote` lectura y el subcomando `pull` (nombre saneado: caracteres no alfanuméricos a `_`; sin sobrescribir con distinto contenido: añade sufijo `_<app_id[:8]>` si el nombre ya existe).
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest tests/test_remote.py tests/test_bridge.py -q`. Expected: pasan.
- [ ] **Step 5: Prueba manual de solo lectura.** Run: `python -m emulator.cli pull $DFEMU_BASE_APP --out out/corpus`. Expected: crea `out/corpus/fundamentos.pull.json` cuyo `dataflow.graph.nodes` tiene 3 nodos y cuyo `script` contiene `LOAD DISTINCT`.
- [ ] **Step 6: Commit** (si hay autorización): `git add emulator/remote.py emulator/cli.py tests/test_remote.py && git commit -m "feat: descargar flujos del tenant con dfemu pull"`.

---

### Task 3: Subir y validar con el servidor (`Remote` escritura, `validate --remote`)

**Files:**
- Modify: `emulator/remote.py`, `emulator/cli.py`, `tests/test_remote.py`

**Interfaces:**
- Consumes: `Bridge.post|put|delete|get` (Task 1), `Remote.dataflow_id|script_of` (Task 2).
- Produces:
  - `BASE_APP_ID` (variable de entorno `DFEMU_BASE_APP`; por omisión `00000000-0000-0000-0000-000000000001`, el flujo `fundamentos`, que solo se lee y se clona).
  - `class UnsupportedGraph(Exception)`; `class Clone(NamedTuple)`: `app_id`, `dataflow_id`, `name`; `class PushResult(NamedTuple)`: `validity: dict`, `script: str`.
  - `Remote.clone(base_app_id: str, name: str) -> Clone`; `Remote.push_graph(clone: Clone, graph: dict) -> PushResult`; `Remote.discard(app_id: str) -> None`; `Remote.validity_of(graph: dict, base_app_id: str = BASE_APP_ID) -> PushResult` (clona, sube, descarta siempre; nombre `emu_v_<8 hex>`).
  - Subcomando `dfemu validate --remote ARCHIVO.dfw [--apply]`: imprime estado y violaciones; sale con 1 si `INVALID`.

- [ ] **Step 1: Pruebas que fallan**: `test_push_graph_put_body_has_no_validity_and_new_graph`; `test_validity_of_discards_clone_when_put_fails` (el PUT devuelve rc≠0: se lanza `BridgeError` y existe un DELETE del app clonado); `test_validity_of_rejects_subflow_graph_without_any_call` (`calls == []`); `test_validity_of_dry_run_creates_nothing` (apply=False: `DryRun` y ningún POST/PUT); `test_cli_validate_remote_exit_code` (`INVALID` ⇒ 1, `VALID` ⇒ 0; en simulación imprime `[simulación] POST v1/dataflow-apps/...` y sale 0); `test_clone_outside_sandbox_impossible` (el `spaceId` enviado en el copy es `SANDBOX_SPACE_ID`).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_remote.py -q`. Expected: FAIL.
- [ ] **Step 3: Implementar.** `push_graph`: `GET v1/dataflows/{id}`, quitar `validity`, reemplazar `graph`, `PUT` del cuerpo completo (verificado: es la única forma aceptada), luego `script_of`. `UnsupportedGraph` si algún nodo tiene `component.type == "subflow"`, comprobado antes de cualquier llamada. La CLI captura `DryRun` y lo imprime.
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest tests/test_remote.py -q`. Expected: pasan.
- [ ] **Step 5: Prueba contra el tenant** (necesita `--apply`). Run: `python -m emulator.cli validate --remote samples/fundamentos_filtro_basico.dfw --apply`. Expected: `VALID`. Como `cleanup` llega en la Tarea 7, comprobar a mano que no quedó ningún clon: `qlik raw get v1/items --query resourceType=app,name=emu_v_ < /dev/null` devuelve una lista vacía.
- [ ] **Step 6: Commit** (si hay autorización): `git add emulator/remote.py emulator/cli.py tests/test_remote.py && git commit -m "feat: subir grafos y validar con el servidor"`.

---

### Task 4: Calibración del validador local frente al servidor

**Files:**
- Create: `emulator/calibrate.py`, `tests/test_calibrate.py`
- Modify: `emulator/cli.py`, `emulator/dfw.py`, `emulator/runner.py`, `scripts/make_examples.py`, `tests/test_validate.py`, `tests/test_run.py`

**Interfaces:**
- Consumes: `dfw.validate`, `Remote.validity_of`.
- Produces:
  - `MUTATIONS: dict[str, Callable[[dict], None]]` sobre un `.dfw` completo (muta una copia); nombres: `sin_aristas`, `target_sin_fileName`, `target_sin_extension`, `formato_xlsx`, `formato_invalido` (valor `"zzz"`), `sin_target`, `sin_source`, `processor_sin_configurar` (`$state: "UNCONFIGURED"`), `selectors_vacios`, `ids_duplicados`.
  - `class Row(NamedTuple)`: `name`, `local_valid: bool`, `remote: str`, `agree: bool`. `run_battery(base_dfw: dict, remote_status: Callable[[dict], str]) -> list[Row]` (`remote_status` recibe el grafo mutado y devuelve `VALID`/`INVALID`/`UNCHANGED`; solo `INVALID` cuenta como inválido); `format_rows(rows) -> str`; `disagreements(rows) -> list[Row]`.
  - Subcomando `dfemu calibrate [--base ARCHIVO.dfw] [--apply]` (por omisión `samples/fundamentos.dfw`): imprime la tabla; sale con 1 si hay discrepancias.

- [ ] **Step 1: Pruebas que fallan** en `tests/test_calibrate.py` (sin red): `test_mutations_do_not_touch_base` (el `.dfw` base queda igual tras `run_battery`); `test_battery_covers_all_names` (conjunto de nombres exacto); `test_agree_logic` (con un `remote_status` que siempre devuelve `INVALID`, las filas cuyo veredicto local es inválido concuerdan y las demás no); `test_unchanged_counts_as_valid`. En `tests/test_validate.py`: `test_xlsx_target_is_valid_locally` (`dfw.validate` de `fundamentos.dfw` con formato `xlsx` no devuelve errores de formato, según el servidor). En `tests/test_run.py`: `test_xlsx_target_not_executable` (`runner.run` lanza `Unsupported`, porque el emulador no escribe xlsx).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_calibrate.py tests/test_validate.py tests/test_run.py -q`. Expected: FAIL.
- [ ] **Step 3: Implementar** `calibrate.py`, el subcomando, y los dos cambios ya evidenciados: añadir `xlsx` a `TARGET_FORMATS` en `emulator/dfw.py` y hacer que `runner._write` lance `Unsupported("target xlsx: validado pero no ejecutable en el emulador")`. En `scripts/make_examples.py` cambiar `_bad_target_fmt` para que use un formato que el servidor rechace (se fija en el paso 5; mientras tanto `"zzz"`), y regenerar con `python scripts/make_examples.py`.
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest -q`. Expected: todas pasan (las 35 anteriores más las nuevas).
- [ ] **Step 5: Calibrar contra el tenant** (necesita `--apply`). Run: `python -m emulator.cli calibrate --apply`. Expected: una tabla con 10 filas. El servidor es el juez: por cada fila con `agree == False`, ajustar la regla de `emulator/dfw.py` hasta coincidir y añadir una prueba unitaria en `tests/test_validate.py` con la mutación y el veredicto del servidor. Si el servidor da `VALID` para `formato_invalido`, eliminar la regla de formato de `dfw.py` y cambiar `i08` por otra mutación inválida que el servidor confirme. Repetir hasta `disagreements == []`. Anotar la tabla final en `docs/banco-de-pruebas/01-hallazgos-api-qlik.md` §6.
- [ ] **Step 6: Commit** (si hay autorización): `git add emulator/ scripts/make_examples.py tests/ docs/ && git commit -m "feat: calibrar el validador local contra el servidor"`.

---

### Task 5: Oráculo de ejecución en el tenant

**Files:**
- Create: `emulator/oracle.py`, `tests/test_oracle.py`
- Modify: `emulator/remote.py` (borrado de archivos `emu_`)

**Interfaces:**
- Consumes: `Bridge` (Task 1), `Remote.script_of` (Task 2).
- Produces:
  - `class OracleError(Exception)`; `DATAFILES_PREFIX = "lib://Entrenamiento Dataflow:DataFiles/"`.
  - `class Retargeted(NamedTuple)`: `script: str`, `files: dict[str, str]` (nombre original sin extensión → archivo `emu_<tag>_<n>.csv`), `tables: dict[str, str]` (mismo origen → tabla `emu_out_<n>`).
  - `retarget(script: str, tag: str) -> Retargeted`: reemplaza cada `STORE <tabla> INTO [lib://...] (<fmt>);` por un `STORE` a `DATAFILES_PREFIX + "emu_<tag>_<n>.csv"` con formato `(txt)`, y añade al final `QUALIFY *;` y, por cada archivo, `[emu_out_<n>]: LOAD * FROM [<ruta>] (txt, utf8, embedded labels, delimiter is ',', msq);`. Un `STORE` que no encaja con el patrón lanza `OracleError`.
  - `assert_safe(script: str) -> None`: todo `INTO [...]` debe empezar por `DATAFILES_PREFIX + "emu_"`; si no, `OracleError`.
  - `parse_tables(text: str) -> dict[str, tuple[int, list[str]]]`: interpreta la salida de `qlik app tables` (`NAME ROW COUNT RAM FIELDS`) y devuelve tabla → (filas, campos).
  - `TableFp = {"rows": int, "columns": {col: {"count": int, "distinct": int, "sum": float | None}}}`; `run_script(bridge: Bridge, script: str, tag: str, timeout: int = 180) -> dict[str, TableFp]` (clave: nombre original sin extensión).
  - `Remote.discard_files(names: list[str]) -> None` (busca `GET v1/data-files` por nombre en la conexión `DataFiles` del espacio permitido y llama a `POST v1/data-files/actions/delete`).

- [ ] **Step 1: Pruebas que fallan** en `tests/test_oracle.py`: `test_retarget_rewrites_every_store` (con el script real de `fundamentos`, que cabe en un literal: no queda ningún `GDDestino` y hay un `QUALIFY *;` y un `LOAD`); `test_assert_safe_rejects_original_store` y `test_assert_safe_accepts_retargeted`; `test_retarget_unknown_store_raises` (`STORE a, b FROM t INTO [x]` sin paréntesis de formato); `test_retarget_keeps_non_ascii` (el `μ` del bloque `SET NumericalAbbreviation` sobrevive); `test_parse_tables_sample` (con el texto exacto `"NAME          ROW COUNT     RAM     FIELDS\nSalida        3             16      id, valor\nTotal RAM     -             175     -"` devuelve `{"Salida": (3, ["id", "valor"])}`); `test_run_script_cleans_up_when_reload_fails` (con `FakeRunner`: el reload termina `FAILED` ⇒ `OracleError` con el final del log y existen DELETE del app y borrado de archivos); `test_run_script_rejects_validatescript_errors` (no se llega a recargar); `test_run_script_fingerprint` (`FakeRunner` devuelve `app tables` y `app eval --json` con `qMatrix`; `Sum` con `qNum` `"NaN"` pasa a `None`).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_oracle.py -q`. Expected: FAIL.
- [ ] **Step 3: Implementar `oracle.py`.** Flujo de `run_script`: `retarget` + `assert_safe`; crear app `emu_oracle_<tag>` en el espacio permitido; `Bridge.script_set`; `POST v1/apps/validatescript` (si hay `Errors`, `OracleError`); `POST v1/reloads` y sondear `GET v1/reloads/{id}` cada 2 s hasta `SUCCEEDED`/`FAILED` o `timeout`; huellas con `Bridge.cli_read(["app","tables","--app",id])` y, por cada campo, `["app","eval","--app",id,"Count([c])","Count(distinct [c])","Sum([c])","--json"]` (campos calificados `emu_out_<n>.<col>`; el resultado se indexa por la columna sin prefijo); `finally`: `Remote.discard(app_id)` y `Remote.discard_files(...)`.
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest tests/test_oracle.py tests/test_bridge.py tests/test_remote.py -q`. Expected: pasan.
- [ ] **Step 5: Commit** (si hay autorización): `git add emulator/oracle.py emulator/remote.py tests/test_oracle.py && git commit -m "feat: oraculo de ejecucion en el tenant"`.

---

### Task 6: Comparador y `dfemu compare`

**Files:**
- Create: `emulator/compare.py`, `tests/test_compare.py`, `tests/test_tenant.py`
- Modify: `emulator/cli.py`

**Interfaces:**
- Consumes: `runner.run`, `oracle.run_script`, `Remote.script_of|validity_of`, `TableFp`.
- Produces:
  - `local_fingerprint(dest: str) -> TableFp` (DuckDB sobre `.csv` o `.parquet`; `sum` solo para columnas numéricas, `None` en las demás).
  - `stem_of(dest: str) -> str` (nombre de archivo sin extensión ni `.qvd`).
  - `compare(local: dict[str, TableFp], remote: dict[str, TableFp], rel_tol: float = 1e-9) -> list[str]` (mensajes legibles: tabla ausente en un lado, filas distintas, columna ausente, `count`/`distinct`/`sum` distintos; vacío = coinciden).
  - Subcomando `dfemu compare ARCHIVO.dfw (--app APP_ID | --push) [--data data/practica] [--out out] [--apply]`: ejecuta el emulador, obtiene el script (de `--app`, o subiendo el grafo con `--push` a un clon), lo ejecuta con el oráculo y lista las diferencias; sale con 1 si hay.

- [ ] **Step 1: Pruebas que fallan** en `tests/test_compare.py`: `test_local_fingerprint_csv` (CSV pequeño en `tmp_path`: `rows`, `count`, `distinct`, `sum` y `None` para texto); `test_compare_equal_is_empty`; `test_compare_reports_each_difference` (una prueba por tipo: tabla ausente, filas, columna ausente, `sum` fuera de tolerancia); `test_compare_sum_within_tolerance`; `test_stem_of_qvd_parquet` (`a.qvd.parquet` → `a`); `test_cli_compare_exit_code` (con `Bridge` falso que devuelve huellas distintas ⇒ 1). En `tests/test_tenant.py` (marcador `tenant`): `test_compare_fundamentos_against_tenant` (ejecuta `compare samples/fundamentos.dfw --app $DFEMU_BASE_APP --apply` y espera 0 diferencias).
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_compare.py -q`. Expected: FAIL.
- [ ] **Step 3: Implementar** `compare.py` y el subcomando. Emparejar tablas por `stem_of`; si dos destinos comparten nombre, error explícito (no se compara). Con `--push`, el clon se descarta siempre; el original de `--app` solo se lee.
- [ ] **Step 4: Ejecutar.** Run: `python -m pytest -q`. Expected: pasan (las pruebas `tenant` se omiten).
- [ ] **Step 5: Prueba de aceptación contra el tenant.** Run: `DFEMU_TENANT=1 python -m pytest tests/test_tenant.py -q`. Expected: pasa; la salida del tenant y la del emulador coinciden en `clientes` (mismas filas y columnas). Si hay diferencias, tratarlas como hallazgos: anotarlas en `docs/banco-de-pruebas/01-hallazgos-api-qlik.md` y corregir el emulador o el comparador según de quién sea el error.
- [ ] **Step 6: Commit** (si hay autorización): `git add emulator/compare.py emulator/cli.py tests/ && git commit -m "feat: comparar resultados del emulador con el tenant"`.

---

### Task 7: Limpieza y cierre de la fase

**Files:**
- Modify: `emulator/cli.py`, `tests/test_remote.py`, `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`, `docs/superpowers/specs/2026-11-19-banco-de-pruebas-design.md`

**Interfaces:**
- Consumes: `Remote.list_dataflows`, `Bridge`.
- Produces:
  - `Remote.list_emu() -> tuple[list[FlowRef], list[str]]` (apps `emu_*` del espacio permitido y nombres de archivos `emu_*` de `DataFiles`).
  - Subcomando `dfemu cleanup [--apply]`: lista lo que borraría; con `--apply` lo borra. Nunca toca objetos sin prefijo `emu_` ni de otro espacio.

- [ ] **Step 1: Pruebas que fallan**: `test_list_emu_ignores_non_emu_and_other_spaces`; `test_cleanup_dry_run_deletes_nothing`; `test_cleanup_apply_deletes_only_emu`.
- [ ] **Step 2: Ejecutar y ver el fallo.** Run: `python -m pytest tests/test_remote.py -q`. Expected: FAIL.
- [ ] **Step 3: Implementar** `list_emu` y `cleanup` (reutiliza `discard` y `discard_files`).
- [ ] **Step 4: Ejecutar todo.** Run: `python -m pytest -q`. Expected: todas pasan.
- [ ] **Step 5: Limpiar el tenant** (necesita `--apply`). Run: `python -m emulator.cli cleanup --apply`. Expected: se borran `emu_probe` y `emu_probe_out.csv` y cualquier `emu_*` residual; una segunda ejecución no lista nada.
- [ ] **Step 6: Actualizar la documentación**: en `docs/banco-de-pruebas/01-hallazgos-api-qlik.md`, §10 (objetos creados) y §11 (pendiente), y marcar en el diseño las fases 1 a 3 como hechas. Anotar los comandos de `dfemu` (`pull`, `validate --remote`, `calibrate`, `compare`, `cleanup`) y el uso de `--apply`.
- [ ] **Step 7: Commit** (si hay autorización): `git add emulator/ tests/ docs/ && git commit -m "feat: limpieza de objetos emu_ y cierre de fases 1 a 3"`.
