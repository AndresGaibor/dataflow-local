# Handoff: control de Qlik Cloud desde dfemu

**Fecha:** 2026-11-28. **Rama:** `main`, último commit `3b4a79b`. **CI:** run `46115671928` en verde
(py3.11 y py3.12 × ubuntu y windows).
Para quien siga: leer antes `CLAUDE.md` (reglas) y `01-hallazgos-api-qlik.md` (lo ya medido).

## 1. Estado medido, no supuesto

| Comprobación | Comando | Resultado de la última corrida |
|---|---|---|
| Suite local | `python -m pytest -q` | **582 pasan, 1 omitida** (63 s) |
| Cobertura publicada | `python scripts/test_coverage.py --check` | **82,7 % medido = 82,7 % en README** |
| Documentación espejo | `python scripts/docsync.py --check` | **2964/2964 páginas, 0 imágenes rotas** |
| Cobertura de processors | `python scripts/processor_coverage.py` | 24 en catálogo, 157 casos, **20 con caso, 4 sin caso** |
| MCP | `grep -c '"dfemu_' emulator/mcp.py` | **42 herramientas** |

Las cuatro sin caso son las que quedan de trabajo real: `map-fields`, `pivot`, `script`, `subflow`
(el script lo imprime el comando con el motivo de cada una).

## 2. Qué queda terminado (con cómo comprobarlo)

- **Documentación reproducible.** `scripts/docsync.py` baja de help.qlik.com con manifiesto `sha256`
  e imágenes, incluido `docs/Automate/`; `--check` da 0 faltantes. No volver a bajarla a mano.
- **Data Flow creable desde cero por API.** `Remote.create()` hace `POST v1/dataflow-apps` y deja
  app + dataflow vacío; con fuente y destino el flujo queda `VALID` y recarga `SUCCEEDED`. Dos claves
  medidas que costaron varias sesiones: la **clave del bloque `connections` lleva el prefijo del
  espacio** (`Entrenamiento Dataflow:DataFiles`), y el conector se elige por `dataStoreType` + `spaceId`
  del dataset. Fuente por API: `POST v1/dataflow-apps/{app}/datasources` con el cuerpo capturado de
  la interfaz (`dfemu flow add-source`).
- **`datasources` y `subflow` por API** dejan el flujo `VALID` (el `subflow` ya existía; crear uno
  nuevo sigue en la lista de pendientes).
- **Qlik script de punta a punta:** `dfemu script get|set|translate`, y el nodo `script` se reutiliza
  de una copia con `dfemu script-node` (no se puede crear desde cero: ver §3).
- **Automate:** `emulator/automate.py` sobre `workflows/automations` con `ls/show/new/set/rm/enable/
  disable/copy/run/runs`, todo con las reglas del `Bridge` (simula sin `--apply`, solo objetos
  `emu_*`). **14 pruebas** lo cubren. Le falta documentación en el banco de pruebas: no hay apartado
  propio en `docs/banco-de-pruebas/`.
- **MCP:** publica 42 herramientas, resources, prompts y `notifications/progress`; `dfemu_compare`,
  `dfemu_coverage`, `dfemu_docs_check` y `automation_run` ya esperan estado final.
- **`dfemu ui`** (ver §4): localiza controles por nombre accesible y ejecuta recetas en una sola
  sesión de página.

## 3. Lo que falta, en orden

### 3.1 `pivot` y `script`: conseguir el `schemaEntityId` (bloqueante principal)

Con los campos puestos por API el flujo se queda en un solo error, y es este:

```
a21699df  VALUE_MISSING_ON_REQUIRED_FIELD   parameters.attributePath = /schemaEntityId
```

Lo medido, para no repetir:

- Va en `component.properties.schemaEntityId` (no dentro de `configuration`).
- **Cualquier valor inventado devuelve `500 INTERNAL_SERVER_ERROR`** (probado con un `uuid4`, con el
  id de un campo del esquema y con el id de un nodo). No es un `500` por forma del cuerpo: es porque
  la entidad no existe.
- El esquema del nodo **sí** se puede leer por API: `GET v1/dataflows/{df}/actions/schema?handleId={salida del nodo anterior}`
  → `{"schema":[{"id","name","details"}]}`, con ids v5 estables por columna (p. ej. `ciudad` →
  `52482077-ce5f-54d7-95e9-057b256bf5a9`). Ese `handleId` es el de **salida** del nodo previo; el de
  entrada del pivot también responde.
- `POST .../actions/schema` no existe como tal: **403** con la API key y **también 403 desde la
  página** con el `qlik-csrf-token` real capturado de una petición del SPA. Descartado por las dos
  vías; no insistir ahí.
- Ningún flujo accesible del tenant tiene un nodo `pivot` ni `script` configurado, así que no hay
  donante que copiar.

Conclusión: **el id nace en la interfaz**, al confirmar el panel del nodo. El trabajo pendiente es
terminar de rellenar ese panel.

### 3.2 Dónde se atasca el panel del Pivotar (y por dónde seguir)

El panel flota sobre el lienzo (x≈841) y se abre con *hover* + clic en el nodo (`dfemu ui steps`, paso
`abrir`). Controles medidos:

| Control | Cómo se localiza | Estado |
|---|---|---|
| Campo que pivotar | `data-testid^="pivot.attributeFieldName"` | **atascado** |
| Campo de valores | `data-testid^="pivot.valueFieldName"` | **atascado** |
| Función de agregación | `data-testid^="pivot.contains.type"`, lista `role=option` | **funciona** (`fill` deja «Suma») |

Las dos primeras **no son listas de opciones**: son grupos de casillas
(`div._optionGroup` → `label._optionCheckbox` → `span._optionLabel`), el `input[type=checkbox]` no
está deshabilitado y aun así:

- `press` de ratón sobre la fila (probado en el borde izquierdo, en el centro y en el derecho): cierra
  el menú y **no** marca.
- `input.click()`, `label.click()`, y `checked=true` + `input`/`change` sintéticos: la casilla queda
  marcada en el DOM y React la revierte; el combobox sigue mostrando «Seleccione un campo».
- Teclado: `Enter` abre (`aria-expanded=true`), pero `ArrowDown` no mueve el foco ni
  `aria-activedescendant`, y en ese estado el popup no expone ningún elemento con rol.

Siguiente intento recomendado, en este orden:

1. **Eventos de puntero por CDP** (`Input.dispatchMouseEvent` con `pointerdown`/`pointerup` reales
   sobre el centro de la `label`), en lugar del `click` sintético: si el SPA cierra el menú en un
   `pointerdown` de captura, ese orden es el que hay que reproducir.
2. **Llamar al handler de React**: leer la fibra del `label` (`__reactProps$…` / `onClick`) y
   invocarla con el evento del propio elemento. Es la vía que esquiva el hit-testing.
3. Si ninguna de las dos: capturar con `dfemu flow capture cdp --only actions` el `PUT` que manda la
   interfaz cuando se configura el pivot a mano (basta una vez, la acción es manual del usuario) y
   pasar el cuerpo por `dfemu flow capture adopt --save`. Con ese `PUT` el `schemaEntityId` queda
   documentado y se convierte en herramienta y caso de batería.

Cuando funcione: añadir el paso `marcar` (casilla por texto) al motor de `ui steps`, un caso a
`scripts/processor_battery_cases.json` para `pivot`, y borrar el clon `emu_ui_piv`.

### 3.3 Resto

- `map-fields`: sigue sin semántica documentada; exige la entrada `LOOKUP` conectada (`feed`/`REQ_IN`).
- `subflow`: crear uno nuevo (hoy solo se clona).
- `script` desde cero: depende de §3.1 (mismo `$state: UNCONFIGURED`).
- Apartado de Automate en `docs/banco-de-pruebas/` (lo hay en código y pruebas, no en el banco).
- Batería en tandas de 6–12 casos y en segundo plano cuando toque medir contra el tenant.

## 4. El motor `dfemu ui` (lo nuevo de esta sesión)

```bash
export DFEMU_BROWSER_SESSION=cdp2          # sesión de playwright-cli atada al Chrome del usuario
dfemu ui state                              # validez, nodos @x,y, aristas
dfemu ui panel                              # controles del panel: rol | etiqueta | valor
dfemu ui fill "Campo que pivotar" ciudad --node Pivotar
dfemu ui click "Ejecutar y aplicar" --wait 12000
dfemu ui steps out/receta_pivot.json        # receta: abrir / fill / click / wait
```

Hechos que cambiaron el diseño (no volver a tropezar):

- **Los comboboxes del panel no tienen `aria-label`**: su etiqueta es el `<span id>` de
  `aria-labelledby`. Antes el panel se veía como tres combos vacíos e irrellenables.
- **El panel se cierra al soltar la pestaña**: dos procesos de `playwright-cli` seguidos no ven el
  mismo panel. Por eso `fill`/`click` son azúcar sobre `ui steps` y `--node` antepone `abrir`.
- Un paso que no deja el valor pedido se reporta `<- sin efecto` y el comando **falla** (no se da por
  bueno el clic).
- `data-testid` del pivot: `pivot.attributeFieldName}` (sí, con llave pegada), `pivot.valueFieldName`,
  `pivot.contains.type`; se aceptan por prefijo y se descartan los `.menuTrigger`.

## 5. Entorno y trampas

- **Chrome por CDP**: `http://[::1]:9222`, perfil aparte en `C:/tmp/chrome-dfm`, sesión de
  playwright-cli `cdp2`. Navegar con `MSYS2_ARG_CONV_EXCL='*' playwright-cli -s=cdp2 goto "$URL"`
  (Git Bash corrompe las rutas con `/`).
- **JS ad hoc**: `playwright-cli -s=cdp2 --raw run-code --filename=out/x.js`, devolviendo
  `async page => {…}`. `/tmp` no existe para Windows: escribir siempre en `out/` (ignorado por git).
- **La CLI no está en el PATH** en esta máquina: usar
  `python -c "from emulator.cli import main; main(['flow','show','emu_ui_piv'])"`.
  `python -m emulator.flowctl` **no** ejecuta nada (no hay guard `__main__`); `python -m emulator`
  tampoco existe.
- **Heredocs y `\n`**: en Git Bash un `python - <<EOF` con `\\n` dentro de cadenas corrompe el archivo
  (ya rompió `mcp.py` y `flowctl.py`). Usar las herramientas de edición.
- **El tenant**: vivos `emu_e2e_ventas`, `emu_e2e_calidad`, `emu_e2e_normalizacion` y el clon de
  trabajo **`emu_ui_piv`** (app `a3390b14-f5d7-4fa9-8e60-4d07cfbb4069`, dataflow `0cf07ee4…`, con el
  nodo `Pivotar` `a21699df`). Al cerrar §3, borrarlo (`dfemu cleanup --apply` o `git`-free `DELETE`
  vía `Remote.discard`). Su nombre de dataflow interno es «fundamentos»: no confundir al buscar.
- **Reglas del repo** (`CLAUDE.md`): solo objetos `emu_*`, solo con `--apply`, nunca imprimir
  credenciales ni el host, y `push` solo cuando el usuario lo pida (en esta sesión está autorizado
  `push origin main`).

## 6. Primeros comandos para retomar

```bash
cd /c/Users/USUARIO_BISOLUTION1/code/dataflow-local
python -m pytest -q                                    # debe seguir en 582/1
python scripts/docsync.py --check                      # debe seguir en 2964/2964
python scripts/processor_coverage.py                   # los 4 sin caso, con motivo
export DFEMU_BROWSER_SESSION=cdp2
python -c "from emulator.cli import main; main(['flow','show','emu_ui_piv'])"
python -c "from emulator.cli import main; main(['ui','steps','out/receta_pivot.json'])"
```

`out/receta_pivot.json` ya existe con los tres `fill` y el «Ejecutar y aplicar»: el único paso que
falla hoy es el de las casillas de §3.2.
