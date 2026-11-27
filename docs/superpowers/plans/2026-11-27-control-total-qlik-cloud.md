# Control total de Qlik Cloud desde dfemu: documentación, Data Flow, Qlik script y Automate

**For agentic workers:** ejecutar fase a fase, en el orden de la sección 6. Cada tarea empieza
por la prueba que falla y termina con evidencia leída (no con "debería funcionar"). Las reglas de
`CLAUDE.md` mandan sobre este plan: medir en el tenant antes de afirmar, escribir solo `emu_*`,
`--apply` obligatorio, nada de `push` sin que el usuario lo pida.

**Estado:** propuesta para aprobación. Fecha: 2026-11-27.

## 1. Qué significa "100%" aquí

Cuatro ejes, cada uno medible. "Controlar" = poder leer, crear, modificar y borrar ese objeto sin
abrir la interfaz; CDP es el último recurso cuando la API no expone la ruta.

| Eje | Hoy | Objetivo medible |
|---|---|---|
| **Data Flow** | Lectura y edición completas (`flow` 9 comandos, `ui` 19); 129 casos de batería coincidentes | Crear un flujo desde cero (fuente propia + 12 processors + destino) por API, recargarlo y que coincida; 24/24 processors ejecutables en el emulador |
| **Qlik script** | Traductor parcial (~402 líneas) + `script_set` en `Bridge`; nodo `script` solo reutilizando uno existente | Inventario de constructs del corpus con estado (emulado / solo tenant) al 0% de desconocidas; nodo `script` creable desde cero; `dfemu script set/get` con tests |
| **Documentación** | 522 `.md` (DataFlow 30, Scripting 485) sin manifiesto, sin imágenes, sin Automate | Espejo reproducible desde sitemap, con `sha256` y `lastmod` por página, `docsync --check` = 0 faltantes, imágenes descargadas, `docs/Automate/` incluido |
| **Automate** | Nada en el repo; las rutas REST sí están vendorizadas en `.claude/skills/qlik-cli-api/` | CRUD + runs + enable/disable por API (o CDP en el editor de bloques), con las mismas reglas de seguridad que Data Flow |

## 2. Evidencia de partida (medida hoy, no supuesta)

- `help.qlik.com/sitemap.xml` responde 200: índice con 171 sitemaps y 6 familias en `en-US`;
  `sitemap_sense_November2026_en-US.xml` = **1.160 URLs** (donde viven Data Flow, Scripting y Automate).
  Una página suelta responde 200, así que el espejo se hace con HTTP, sin navegador.
- `docs/`: 522 `.md`, **0 imágenes**, y **368 referencias `_images/...` rotas**; no hay manifiesto
  ni script de descarga en el repo (se hicieron a mano).
- Catálogo local: 24 processors. La doc oficial lista 23 páginas; el extra es `map-fields`, que
  **no tiene ni una línea de código** en `emulator/` y **0 casos** medidos.
- Batería: 129 casos. Processors que nunca aparecen en ningún caso: `map-fields`, `sample`,
  `subflow`, `script`. Variantes declaradas no emuladas: `FORMAT_MONEY`, `NUMERIC_OPS`,
  `COMPARE_DATES`, `DATE_FROM_PARTS`, `FUZZY_MATCHING`, `EXTRACT_VALUES_BY_REGEX`.
- `pivot` no se puede crear por API (`schemaEntityId` lo pone la interfaz) y el emulador lo rechaza.
- Automate: `.claude/skills/qlik-cli-api/docs/apis/rest/workflows/automations.md` ya documenta
  `GET/POST/PUT/DELETE /api/v1/workflows/automations`, runs, enable/disable, copy, change-space,
  move, retry/stop y export del log. `/api/v1/automations` está deprecado a favor de `/workflows/`.
- CDP: `scripts/browser_setup.py` deja sesión `chrome` con playwright-cli y registra los MCP
  playwright/chrome-devtools. Lo único no automatizable es marcar la casilla de depuración remota.
- `openspec` 2.1.0 está instalado pero **no inicializado** en el repo. Este plan se queda en
  `docs/superpowers/` (convención ya usada) para no tener dos fuentes de verdad; si se quiere
  seguimiento de deltas, `openspec init` es un añadido barato y reversible.

## 3. Reglas que no se negocian en ninguna fase

1. Se escribe en el tenant solo por `Bridge`, solo objetos `emu_*`, solo en el espacio de pruebas,
   y solo con `--apply`.
2. Sin credenciales en el repo ni en el chat; la API key se pide con `getpass`.
3. Una afirmación sobre Qlik se mide antes; se documenta en el apartado 9 quater.
4. La batería va por tandas de 6 a 12 casos y en segundo plano; si el sistema la corta, `cleanup`
   y no relanzar sin que se pida.
5. Sin `push` ni borrado de ramas remotas sin autorización explícita.

## 4. Fases y tareas

### Fase 0 — Cerrar lo suelto (medio día, sin tenant)

- **T0.1 CI con matriz.** `tests.yml`: matriz `3.11`/`3.12` + job `windows-latest` que corra
  `pytest` y `dfemu coverage` (el proyecto es Windows-first y hoy solo se prueba ubuntu/3.12).
- **T0.2 `dfemu --version`** leyendo la versión instalada; tag `v0.1.0`.
- **T0.3 Encoding.** `dfemu coverage` imprime `Uni�n` en consola Windows: forzar UTF-8 en stdout
  y añadir una prueba que escriba un nombre con acento y lo compare.
- **T0.4** Borrar `origin/ci/actions-v7` (obsoleta, ya en `main`) **con autorización**.

*Aceptación:* CI verde en las 5 combinaciones; `dfemu --version` devuelve `0.1.0`; la prueba de
encoding pasa en Windows.

### Fase 1 — Toda la documentación, reproducible (1-2 días, sin tenant)

- **T1.1 `scripts/docsync.py`.** Sitemap index → familia + versión + locale → descarga cada página,
  la convierte a `.md` con frontmatter (`source_url`, `product`, `version`, `lastmod`, `sha256`),
  descarga las `_images` referenciadas y escribe `docs/manifest.json`. Idempotente: si el `sha256`
  no cambió, no reescribe. `--check` compara sitemap contra disco y falla si falta algo.
  *Prueba primero:* un test con un sitemap y dos páginas falsas (una nueva, una igual, una borrada
  en origen) que verifique descarga, idempotencia y `--check`.
- **T1.2 Producto actual completo.** `sense_November2026_en-US` (1.160 páginas) a `docs/`, en
  carpetas por sección. *Decisión de empaquetado:* se commitea el `.md` (texto, ligero) y se ignora
  `docs/_images/` (regenerable), para no inflar el repo público.
- **T1.3 `docs/Automate/`.** Verificar que el espejo trae la sección de Qlik Automate y que las
  páginas de bloques/conectores están completas (es la base documental de la fase 4).
- **T1.4 API REST.** Regenerar el índice de endpoints vendorizados con el mismo manifiesto
  (`sha256` + fecha), para detectar cuándo Qlik añade o depreca rutas.

*Aceptación:* `python scripts/docsync.py --check` = 0 faltantes y 0 imágenes rotas; `docs/manifest.json`
con `sha256` por página; `docs/Automate/` presente; segunda ejecución no reescribe nada.

### Fase 2 — Data Flow: crear, no solo clonar (3-5 días, tenant por tandas)

- **T2.1 Fuentes nuevas por API.** Hoy `entityId` es propio de cada flujo y solo se reutilizan las
  del flujo base. Buscar el id global del dataset (catálogo/`data-assets`) y cómo lo transforma el
  flujo al registrar la fuente. *Aceptación:* flujo nuevo con una fuente del catálogo, recargado en
  tenant, coincidente con el emulador.
- **T2.2 `pivot` creable.** Mismo patrón que `script-node`: reutilizar el `schemaEntityId` de un
  flujo que ya tenga `pivot` y crear el nodo. *Aceptación:* nodo `pivot` nuevo, `VALID`, recarga OK
  y resultado coincidente.
- **T2.3 `script` desde cero por CDP.** Capturar con CDP la petición que crea el nodo `script`
  desde la interfaz (ruta y cuerpo), documentarla y reproducirla sin navegador si es posible.
- **T2.4 Receta dentro de subflow.** `PUT v1/dataflows/{subflow}` (nunca probado): modificar una
  regla del subflow clonado y verificar que el flujo la usa.
- **T2.5 Import/export `.dfw` con archivo.** Cerrar los dos cabos: id de la subida a `temp-contents`
  (cabecera `Location`, que la CLI no muestra — CDP o una llamada HTTP directa) y descarga del
  exportado. *Aceptación:* round-trip export → import → grafo idéntico.
- **T2.6 Tareas.** `usage` de tareas avanzadas y un flujo real completo (no `emu_`) en simulación.
- **T2.7 Limpieza en Google Drive.** No hay API de Qlik: documentar como manual o resolverlo por CDP
  en el conector; no dejar `emu_` huérfanos en el espacio.

*Aceptación de la fase:* `dfemu flow` crea un flujo de 12 nodos con fuente propia y destino por API,
recarga y coincide; `add/set/rm/restore` cubiertos por tests; cada hallazgo nuevo en 9 quater.

### Fase 3 — Qlik script de punta a punta (3-4 días)

- **T3.1 `dfemu script set|get|validate`.** Exponer `Bridge.script_set` (ya existe y lo usa el
  oráculo) como comando con tests, sin `--verbose` y sin imprimir token.
- **T3.2 Nodo `script` operativo.** Con T2.3: crear el nodo desde cero, guardar el script que genera
  Qlik y verificarlo con `translate --compare`.
- **T3.3 Inventario de constructs.** Extraer del corpus (`out/corpus/*.pull.json`, `samples/`) todas
  las sentencias y funciones usadas, con estado por construct: `emulado`, `traducido sin ejecutar`,
  `solo tenant`. Sale como tabla en `docs/banco-de-pruebas/`.
- **T3.4 Cerrar los huecos conocidos**, uno por caso medido: `LIB CONNECT`, `xlsx`/`qvd`,
  `CONCATENATE`, `Match`, `SubField`, `Window`, varios `STORE`, joins entre campos comunes de distinto
  tipo, `Sum`/`Avg` con parte de valores nulos.
- **T3.5 `translate --compare` sin tenant** en CI, con snapshots de los scripts ya verificados.

*Aceptación:* 0 constructs "desconocidas" sobre el corpus; cada una emulada o marcada; la tabla de
cobertura queda publicada en el README.

### Fase 4 — Qlik Automate (3-5 días)

- **T4.1 `dfemu automate ls|show|new|set|rm|enable|disable|copy|run|runs`** sobre
  `/api/v1/workflows/automations` (con caída al `/api/v1/automations` deprecado si hiciera falta),
  pasando por `Bridge`: prefijo `emu_`, `--apply`, bitácora y simulación por defecto.
- **T4.2 Estructura de bloques.** Crear una automatización vacía por API y leer el JSON; si los
  bloques no se pueden definir por API, capturarlos por CDP del editor y guardarlos como plantilla.
- **T4.3 Runs.** Lanzar, seguir estado, `retry`/`stop` y export del log de depuración.
- **T4.4 Conexiones.** `automation-connections` / `automation-connectors`: listar y reutilizar;
  crear solo si el scope lo permite.
- **T4.5 Alcance explícito.** No se emula el motor de Automate; queda documentado como "solo tenant".

*Aceptación:* automatización `emu_*` con 3 bloques creada, habilitada, ejecutada y con su run leído
sin abrir la interfaz; borrada sin dejar restos.

### Fase 5 — Emulador al 100% de la paleta (2-3 días, tenant por tandas)

- **T5.1 `map-fields`.** Sin código: descubrir su configuración (CDP si la API da `500`) y decidir
  emular o marcar.
- **T5.2 Casos para `sample`, `subflow`, `script`.**
- **T5.3 Las 6 variantes** declaradas: `FORMAT_MONEY`, `NUMERIC_OPS`, `COMPARE_DATES`,
  `DATE_FROM_PARTS`, `FUZZY_MATCHING`, `EXTRACT_VALUES_BY_REGEX`.
- **T5.4 Levantar los `shortcut:`** por impacto: `CUT` (`STARTS_WITH`/`ENDS_WITH`/regex),
  `MODIFY_DATES`/`FORMAT_DATES` (más unidades y formatos), `FORMAT_NUMBER` `CUSTOM`,
  parámetros de `PADDING`/`SUBSTRING`/`MATCHES_PATTERN`/`COMPARE_NUMBERS`, empates en ventanas,
  `COUNT_DISTINCT` con rango, locale distinto de en-US.
- **T5.5 `pivot` ejecutable** (cierra T2.2).
- **T5.6 Fuentes de BD con tipos.** Aceptar `--connections` reales para que `coverage` deje de dar
  `no concluyente` en 8 de 11 flujos.

*Aceptación:* cada processor tiene ≥1 caso medido; `dfemu coverage` no reporta ningún processor sin
caso; toda restricción que quede, marcada `shortcut:` y listada en el apartado 12.

### Fase 6 — Cierre y publicación del estado

- **T6.1** README con la tabla de cobertura generada (no escrita a mano).
- **T6.2** `docs/banco-de-pruebas/05-cobertura.md` con la foto final y las limitaciones que queden.
- **T6.3** Tag de release, `CHANGELOG` y CI publicando la tabla.

## 5. Lo único que te voy a pedir

Todo lo demás lo resuelvo yo (incluido CDP: cuando la API no expone la ruta, la capturo del
navegador y la documento).

1. **Marcar "Permitir depuración remota" en Chrome** (paso 2 de `04-control-de-chrome.md`). Es una
   casilla que no se puede automatizar y sin ella no hay CDP; con CDP se desbloquean `pivot`,
   nodo `script`, fuentes y el editor de bloques de Automate.
2. **API key con scopes de Automate** (`automations`, `admin.automations`, rol `AutomationCreator`)
   si la actual (`AnalyticsAdmin`) no alcanza; y la autorización para escribir en el tenant durante
   las tandas de medición.
3. **Aprobación de `push` y de borrado de ramas remotas** cuando toque.

## 6. Orden y coste

`F0 → F1 → F3.3 → F2 → F3 → F5 → F4 → F6`. F0, F1 y F3.3 no necesitan tenant ni dinero; el resto
sí (baterías por tandas de 6-12 casos, en segundo plano).

El orden pone delante lo gratis y lo que desbloquea lo demás: la documentación de la fase 1 es la
base para Automate, y el inventario de constructs (F3.3) dice qué merece la pena traducir antes de
tocar código.

## 7. Riesgos y cómo se manejan

| Riesgo | Manejo |
|---|---|
| La credencial actual da 403 en `import`/`export` | Se intenta con API key; si no, cliente OAuth (`02-guia-oauth.md`), ya probado una vez |
| Scopes de Automate ausentes | Se pide la clave una sola vez, con la lista exacta de scopes |
| Espejo de docs infla el repo público | Se commitea `.md`; `_images/` se ignora y se regenera con `docsync` |
| Coste del tenant | Casos nuevos por tandas, 20 filas, y limpieza obligatoria al cerrar cada tanda |
| `pivot` sigue sin poder crearse | Queda como limitación documentada; el emulador lo ejecuta igual si T2.2 no sale |
| Pérdida de contexto entre sesiones | El estado vive en `docs/banco-de-pruebas/` y en esta lista de tareas, no en la conversación |
