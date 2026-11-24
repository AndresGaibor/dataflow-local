# Control de flujos por agentes (`dfemu flow`)

Objetivo: que un agente lea y edite un flujo del tenant gastando poco contexto. Medido el 2026-11-24 contra el tenant.

## Cómo funciona

- **Transporte**: la sesión de Chrome ya iniciada en Qlik Cloud, a través de `playwright-cli`. No hace falta API key ni la CLI `qlik` (en esta máquina `qlik.exe` lo bloquea la política de control de aplicaciones). Cada llamada es un `fetch` same-origin desde la pestaña de Qlik; las escrituras llevan la cabecera `qlik-csrf-token` (se obtiene con `GET /api/v1/csrf-token`).
- **Requisitos** (una vez): `npm i -g @playwright/cli`, activar `chrome://inspect/#remote-debugging` y `playwright-cli attach --cdp=chrome` (crea la sesión `chrome`; otra con `DFEMU_BROWSER_SESSION`). Debe haber una pestaña de `*.qlikcloud.com` abierta. Al terminar, desmarcar la depuración remota y `playwright-cli -s=chrome detach`.
- **Política de escritura**: solo flujos `emu_*` del espacio de pruebas, o los nombres que el usuario liste en `allow_flows` de `dfemu.local.json` (ignorado por git). Sin `--apply` simula. Cada escritura se anota en `out/audit.jsonl` y guarda antes una copia en `out/backups/`.

## Comandos

| Comando | Para qué | Coste típico |
|---|---|---|
| `dfemu flow ls` | id y nombre de los flujos | 1 línea por flujo |
| `dfemu flow types` | los 24 procesadores: tipo, nombre en la interfaz y puertos (`emulator/processors.json`) | 24 líneas |
| `dfemu flow show F [--full]` | nodos (8 primeros caracteres del id, tipo, etiqueta, configuración truncada) y aristas (`a>b`, `a~>b` si sale por REJECT) | ~1 línea por nodo |
| `dfemu flow node F N` | JSON completo de un nodo | solo ese nodo |
| `dfemu flow add F TIPO --after N [--label L] [--cfg JSON] [--apply]` | inserta un procesador tras N (TIPO o el nombre de la paleta; sin `--cfg` queda con la configuración inicial de la interfaz) | resumen del flujo |
| `dfemu flow set F N --cfg JSON [--label L] [--apply]` | mezcla configuración (diccionarios se fusionan, listas se reemplazan) | resumen |
| `dfemu flow rm F N [--apply]` | quita el nodo y reconecta lo que llegaba con lo que salía | resumen |
| `dfemu flow backup F` / `restore F ARCHIVO [--apply]` | copia y vuelta atrás | ruta |

`F` es el id de la app, el id del flujo o el nombre exacto. `N` es un prefijo del id o la etiqueta. Tras escribir imprime el estado (`VALID`/`INVALID`) y las violaciones (`! nodo código`). El `PUT` se repite mientras solo quede `POTENTIAL_STALE_EXPRESSION` (receta de `calculate-fields`).

Regla para agentes: `show` primero, `node` solo del nodo que importa, nunca volcar el JSON completo del flujo ni capturas de pantalla si la API alcanza.

## Medido

- **Editar por la interfaz es caro y frágil**: cada paso es un clic con coordenadas y una captura (~1500 tokens). Con la CLI, añadir un nodo `sort`, `calculate-fields` y cambiar un filtro costó 3 llamadas de pocas líneas.
- **El editor guarda solo**: un cambio hecho en la interfaz aparece de inmediato en `GET v1/dataflows/{id}` (el nodo, ya `VALID`). Si se edita por API con el editor abierto, la pestaña no se refresca sola.
- **Arrastrar un procesador de la paleta sobre una arista lo inserta entre los dos nodos** (el nodo nuevo sale "No configurado" hasta pulsar Aplicar). Con ratón: `mousemove` a la paleta, `mousedown`, varios `mousemove` y `mouseup` sobre la arista.
- **Las aristas solo nombran handles**: `reactflow__edge-{nodo}{handleOrigen}-{nodo}{handleDestino}`. Insertar un nodo es mover `sourceHandle` de las aristas de salida al nodo nuevo y añadir una arista nueva.
- **Puertos por tipo**: ver la tabla de `04-control-de-chrome.md` (apartado 7) y `dfemu flow types`.
- **Configuraciones verificadas** (el servidor las dio por `VALID` sin pasos extra):
  - `filter`: `{"logicalOpType":"ALL","filters":[{"columnName":"c","function":"EMPTY","operator":"CONTAINS","compareWith":"VALUE","value":"x","columnToCompareWith":""}]}`
  - `sort`: `{"sortFields":[{"fieldPath":"c","sortOrder":"ASCENDING"}]}`
  - `calculate-fields`: `{"calculateFields":[{"newColumnName":"n","expressionStatement":"[a] & ' ' & [b]","anchorColumn":"","rightOfAnchor":false,"fieldReferences":[]}]}`
  - `$state: CONFIGURED` se añade solo si hay configuración.
- **Restaurar funciona**: `restore` con la copia anterior devolvió el flujo exacto (mismos nodos y aristas, `VALID`).

## No cubierto

- No ejecuta flujos: el destino de `fundamentos` escribe en Google Drive y la regla del proyecto solo permite ejecutar cuando todo `STORE` va a un archivo `emu_*`.
- Sin vista previa de datos (la da la interfaz, no la API).
- `flow add` de `Unir`, `Unión`, `Bifurcación`, `Script de Qlik` y los demás con puertos extra crea el nodo con los puertos de la interfaz, pero solo se ha verificado contra el tenant con `filter`, `sort` y `calculate-fields`; los nodos con entradas múltiples quedan sin conectar a sus otras entradas (se conectan por la interfaz).
