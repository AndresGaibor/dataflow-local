# Control de Chrome y del editor de Data Flows

Cómo dejar a un agente controlando tu Chrome real (con tus sesiones iniciadas) y qué hay que saber para operar el editor de Qlik sin romperlo. Medido el 2026-11-24 en Windows 11, Chrome estable, Node 24.

Atajo: `python scripts/browser_setup.py` comprueba y hace todo lo automatizable; esta guía explica cada paso y los errores.

## 1. Instalación (una vez)

| Qué | Comando | Para qué |
|---|---|---|
| `playwright-cli` | `npm install -g @playwright/cli@latest` | Controla el navegador por línea de comandos; es lo que usan `dfemu flow` y los scripts |
| MCP `playwright` (opcional) | `claude mcp add --scope user playwright -- cmd /c npx -y @playwright/mcp@latest --browser chrome` | Herramientas `mcp__playwright__*` dentro de Claude Code. Abre **su propio** Chrome, sin tus sesiones |
| MCP `chrome-devtools` (opcional) | `claude mcp add --scope user chrome-devtools -- cmd /c npx -y chrome-devtools-mcp@latest --autoConnect` | DevTools (red, consola, rendimiento) sobre tu Chrome abierto |
| Skills (opcional) | `npx skills add microsoft/playwright-cli@playwright-cli -g -y` y `npx skills add chromedevtools/chrome-devtools-mcp@chrome-devtools -g -y` | Instrucciones de uso para el agente |

En macOS/Linux quite `cmd /c`. Los MCP y las skills nuevas solo se cargan al reiniciar Claude Code o con `/mcp`; `playwright-cli` funciona de inmediato desde la terminal. `python scripts/browser_setup.py --mcp` registra los dos MCP.

Solo se instalan skills de fuentes oficiales (Microsoft, Google): una skill es texto que el agente obedece.

## 2. Activar el CDP en tu Chrome

Es el único paso manual y es una decisión de seguridad tuya: da control total del navegador, con tus sesiones.

1. En Chrome abre `chrome://inspect/#remote-debugging`.
2. Marca **Allow remote debugging for this browser instance**.
3. Si Chrome muestra un aviso para confirmar la conexión del agente, acéptalo.

Comprobación: existe el archivo `DevToolsActivePort` en la carpeta de datos de Chrome (`%LOCALAPPDATA%\Google\Chrome\User Data` en Windows). Si falta, `attach` falla con `DevToolsActivePort file not found ... Make sure chrome is running with remote debugging enabled`.

Al terminar: desmarca la casilla y ejecuta `playwright-cli -s=chrome detach` (o `python scripts/browser_setup.py --detach`).

No hace falta lanzar Chrome con `--remote-debugging-port`: esa vía obliga a cerrar Chrome y abrirlo con un perfil aparte.

## 3. Conectar y comprobar

```bash
playwright-cli attach --cdp=chrome        # crea la sesión "chrome"
playwright-cli -s=chrome tab-list         # tus pestañas abiertas
```

Para Qlik: abre tu tenant en Chrome e inicia sesión. `dfemu flow` busca entre las pestañas una de `*.qlikcloud.com` y hace `fetch` desde ella con tus cookies; no necesita API key. Otra sesión: variable `DFEMU_BROWSER_SESSION`.

Reglas de trato con tu navegador:
- Trabajar en pestañas nuevas; no tocar las personales (correo, chats).
- No guardar en el repo nada de lo que se vea (URLs del tenant, ids, tokens, correos). El repositorio es público.
- Al abrir el editor de un flujo, no recargarlo: la pestaña es el espacio de trabajo y se pierde el estado (ver 5).

## 4. Dos formas de actuar, y cuándo usar cada una

| | API por `dfemu flow` | Interfaz con `playwright-cli run-code` |
|---|---|---|
| Coste | pocas líneas por llamada | una captura ≈ 1500 tokens; evitarlas con `run-code` que devuelve texto |
| Sirve para | leer grafo, insertar, configurar, borrar, restaurar | descubrir cómo crea la interfaz cada nodo, arrastrar, renombrar, conectar, ver la vista previa |
| Riesgo | el editor abierto no se entera del cambio | solo lo que el editor guarda solo |

Preferir la API; usar la interfaz cuando se pida o para aprender un procesador nuevo. **No mezclar escrituras por API con el editor abierto**: la pestaña no se actualiza y la siguiente acción de la interfaz puede pisar el cambio.

## 5. Medido sobre el editor (React Flow)

- **Guarda solo**: cada cambio de la interfaz aparece en `GET v1/dataflows/{id}` en segundos.
- **No recargar la página**: pierde el estado de la pestaña. Si hay que leer el resultado de una acción, se lee por API (solo lectura).
- **Nodos**: `.react-flow__node[data-id="<id del grafo>"]`. **Aristas**: `g.react-flow__edge[aria-label^="Edge from <prefijo del id del nodo origen>"]`; el `data-testid` lleva un id aleatorio, no sirve. El punto medio de la arista: `path.react-flow__edge-path` con `getPointAtLength(getTotalLength()/2)` y `getScreenCTM()`.
- **Pestañas de la paleta** (Fuentes, Procesadores, Destinos): `getByRole('tab')`. El clic de Playwright no las cambia; sí `el.click()` desde `evaluate`, el ratón con retardo entre `down` y `up`, o Enter. **Pulsar la pestaña ya activa pliega la paleta**: pulsar solo si `aria-selected` no es `true`.
- **Elementos de la paleta**: el texto lleva espacios de ancho cero (`U+200B`); comparar quitándolos y mirando hojas del DOM (`children.length === 0`, `textContent`; `innerText` no existe en SVG). Marcar el elemento con un atributo y borrar las marcas anteriores, o `getByText` encuentra varios.
- **Arrastrar y soltar**: `mouse.move` al elemento, `down`, `move` con `steps: 15` al destino, `up`. Soltar sobre una arista inserta el nodo entre sus dos extremos.
- **Borrar un nodo**: clic en su cabecera y `Delete`; la interfaz reconecta lo que llegaba con lo que salía y el flujo queda `VALID`.
- **Un nodo recién soltado** sale `INVALID` con `$state: UNCONFIGURED` hasta que se pulsa Aplicar en el panel de propiedades.
- **Errores típicos**: `strict mode violation ... resolved to N elements` (marcas acumuladas), `Cannot read properties of null (reading 'ownerSVGElement')` (arista no encontrada: prefijo de id mal o la paleta cambió el diseño), `locator.click: Timeout` en una pestaña (usar `evaluate(e => e.click())`), `playwright-cli: Daemon process exited with code 1` al conectar (la depuración remota no está activa).

## 6. Scripts del repositorio

| Script | Qué hace |
|---|---|
| `scripts/browser_setup.py` | Instala y comprueba todo; `--mcp`, `--detach` |
| `dfemu flow ...` | Control del flujo por API vía la pestaña de Qlik (documento 03) |
| `dfemu ui ...` | Control del editor abierto como comandos de texto (apartado 8) |
| `scripts/ui_probe.py FLUJO ORIGEN "Procesador" ...` | Arrastra cada procesador sobre la arista que sale de ORIGEN, lee lo que creó la interfaz (tipo, puertos, configuración inicial), lo borra desde la interfaz y vuelca `out/ui_probe.json` |

## 7. La paleta del editor (medido arrastrando cada elemento)

Tres pestañas a la izquierda. Los nombres son los de la interfaz en español.

- **Fuentes (3)**: Conjuntos de datos (*Buscar en el catálogo*), Conexiones (*Usar datos externos*), Entrada manual (*Tabla interna*).
- **Destinos (2)**: Archivos de datos (*Almacenar en la nube*), Conexiones (*Almacenar externamente*).
- **Procesadores (24)**: el catálogo completo, con tipo interno, puertos y configuración inicial, está en `emulator/processors.json`; `dfemu flow types` lo imprime.

| Interfaz | Tipo | Puertos (entrada → salida) |
|---|---|---|
| Filtro | `filter` | DEFAULT → DEFAULT, REJECT |
| Seleccionar campos | `field-selector` | DEFAULT → DEFAULT |
| Unir | `join` | DEFAULT + LOOKUP → DEFAULT |
| Asignar campos | `map-fields` | DEFAULT + LOOKUP → DEFAULT |
| Unión | `union` | DEFAULT + 9 OPTIONAL → DEFAULT |
| Bifurcación | `fork` | DEFAULT → DEFAULT + OPTIONAL_1..9 |
| Agregar | `aggregate` | DEFAULT → DEFAULT |
| Ordenar | `sort` | DEFAULT → DEFAULT |
| Eliminar campos | `field-remover` | DEFAULT → DEFAULT |
| Cadenas de texto | `strings` | DEFAULT → DEFAULT |
| Fechas | `date` | DEFAULT → DEFAULT |
| Números | `numbers` | DEFAULT → DEFAULT |
| Matemáticas | `math` | DEFAULT → DEFAULT |
| Concatenar campos | `field-concatenator` | DEFAULT → DEFAULT |
| Dividir campos | `split-field` | DEFAULT → DEFAULT |
| Limpiar | `data-cleansing` | DEFAULT → DEFAULT |
| Hash | `masking` | DEFAULT → DEFAULT |
| Muestra | `sample` | DEFAULT → DEFAULT |
| Pivotar | `pivot` | DEFAULT → DEFAULT |
| Despivotar | `unpivot` | DEFAULT → DEFAULT |
| Ventana | `window` | DEFAULT → DEFAULT |
| Receta de tabla | `subflow` | DEFAULT → DEFAULT |
| Calcular campos | `calculate-fields` | DEFAULT → DEFAULT |
| Script de Qlik | `script` | 10 OPTIONAL → DEFAULT + OPTIONAL_1..9 |

Observaciones:
- Al soltar, solo salen `VALID` sin configurar: Bifurcación, Eliminar campos, Muestra y Receta de tabla (más Unión, que sale `CONFIGURED`). El resto sale `INVALID` hasta rellenar sus campos.
- Hash es `masking` con `type: HASH_DATA`; Cadenas de texto, Fechas, Números, Matemáticas, Limpiar y Dividir campos son un mismo componente con `type` que elige la función y un objeto `xxxConfiguration` propio (así se descubre cada variante: crearla por la interfaz y leer el nodo por API).
- **Pivotar, Despivotar y Script de Qlik se crean sin pasos extra desde la interfaz** (la receta anterior decía que `pivot` y `script` exigían un `schemaEntityId` y no se podían crear por API; por la interfaz sí).
- **Receta de tabla crea un subflow nuevo en el tenant** (otro flujo `Subflow ... of <flujo>`). Borrar el nodo desde la interfaz **no borra ese subflow**: queda huérfano. Usarla con moderación.
- **Menú del nodo (tres puntos)**: Agregar destino, Agregar procesador, Eliminar. Es más fiable que la tecla Suprimir, que no borró la Bifurcación.
- **Eliminar un nodo reconecta** lo de DEFAULT a DEFAULT, salvo en nodos con muchas entradas (el `script` dejó el flujo `INVALID` con `NODE_TOPOLOGY_NOT_FULFILLED`: faltaba la arista entre los vecinos).
- **Conectar o reconectar**: arrastrar de un puerto de salida al de entrada, `.react-flow__handle[data-handleid="<id del puerto>"]` (los ids de los puertos están en `handles` del nodo). Con `mouse.move`, `down`, `move` con `steps: 15`, `up`; la arista nueva aparece en segundos y el flujo vuelve a `VALID`.

## 8. `dfemu ui`: el editor como comandos

`dfemu ui ...` (emulator/uictl.py) maneja el editor abierto en tu Chrome con salida de texto: nada de capturas, nada de recargar. Un nodo se nombra por el prefijo de su id (8 caracteres) o por su título exacto. Cada acción es un `playwright-cli run-code`; todas verificadas contra el tenant el 2026-11-24.

| Comando | Qué hace | Verificado |
|---|---|---|
| `ui state` | validez, nodos con posición `@x,y` y aristas | sí |
| `ui select N` / `ui panel` | selecciona el nodo y lista los controles del panel de propiedades (`rol \| etiqueta \| valor`) | sí |
| `ui options ETIQUETA` | lista las opciones de un desplegable del panel (separadas por `\|`) | sí |
| `ui fill ETIQUETA VALOR` | rellena un control del panel; en listas desplegables varios valores separados por `\|` | sí (input y listas) |
| `ui apply` / `ui cancel` | pulsa Aplicar / Cancelar | sí |
| `ui rename N TEXTO` | cambia el título con el lápiz del nodo (falla si no queda) | sí, guardado en el servidor |
| `ui move N DX DY` | arrastra el nodo | sí |
| `ui add "Paleta" --on ORIGEN` | arrastra el procesador de la paleta sobre la arista que sale de ORIGEN (o `--x --y` a un punto) | sí |
| `ui connect FLUJO ORIGEN DESTINO [--out REJECT] [--to LOOKUP]` | une puertos arrastrando (los ids de puerto se leen por API) | sí |
| `ui unlink ORIGEN DESTINO` | borra la arista (clic y Suprimir) | sí |
| `ui rm N` | elimina el nodo desde su menú | sí, reconecta |
| `ui undo` / `ui redo` | botones Deshacer y Rehacer de la barra (Ctrl+Y no rehace) | sí |
| `ui layout` / `ui fit` | Organizar el flujo / Ajuste de zoom | sí (layout) |
| `ui script [N]` | texto del script de Qlik que genera el flujo hasta el nodo (conmutador Script, lo deja como estaba) | sí |
| `ui preview N [--rows K]` | vista previa de datos: encabezado y K filas (consulta datos del tenant: usar poco, y no guardar la salida, lleva datos reales) | sí |

Receta típica para configurar un procesador nuevo: `ui add "Ordenar" --on <origen>`, `ui select "Ordenar 1"`, `ui panel`, `ui fill "Campo" ciudad`, `ui fill "Criterio de ordenación" Descendente`, `ui apply`, y comprobar con `dfemu flow show` (por API, solo lectura). Medido: el nodo quedó `sortFields: [{fieldPath: ciudad, sortOrder: DESCENDING}]` y el flujo `VALID`.

Trampas del editor, ya resueltas en el código: la pestaña de la paleta activa se pliega si se pulsa; el lápiz de renombrar solo existe con el nodo seleccionado (esperar 800 ms); Suprimir no siempre borra un nodo (usar su menú); en las etiquetas del panel, `aria-label` no siempre existe (se usa también `label` y `placeholder`); tras un `layout` el lienzo se aleja y los nodos cambian de coordenadas (las acciones buscan el nodo en cada llamada, no guardan posiciones).

Pruebas: `tests/test_uictl.py` pasa cada acción por `node --check`, porque un `\n` mal escapado en el JavaScript ya rompió una acción.

## Arrastrar de la paleta: son eventos HTML5, no del ratón

El arrastre de «Conjuntos de datos» (y de los procesadores) **no** responde a `mouse.down/move/up` ni a
`page.dragAndDrop`: la fila es un `div[draggable=true]` que escucha `dragstart`/`dragover`/`drop`. Lo que sí
funciona es lanzarlos con un `DataTransfer` desde la página:

```js
const dt = new DataTransfer();
fire(src, 'dragstart', ...); fire(pane, 'dragenter', ...); fire(pane, 'dragover', ...);
fire(pane, 'drop', ...); fire(src, 'dragend', ...);   // abre el diálogo «Catálogo de datos»
```

Está en `dfemu ui dataset NOMBRE`: lanza el arrastre, escribe en «Buscar datos», marca la fila y pulsa el botón
de confirmación. Medido hasta hoy: el diálogo se abre y el filtro deja la fila del dataset a la vista, pero la
casilla de la tabla no habilita el botón «Cargar en el flujo de datos» con un clic sintético — ese último gesto
sigue pendiente. Para el mismo resultado sin interfaz, `dfemu_flow_add_source` (o `dfemu flow add-source`)
registra la fuente por API con el cuerpo que capturó el grabador y deja el flujo `VALID`.
