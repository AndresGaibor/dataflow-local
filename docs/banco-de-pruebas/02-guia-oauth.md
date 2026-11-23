# Guía: cliente OAuth máquina a máquina para la CLI de Qlik

Documento vivo. Todo lo de aquí se hizo y verificó el 2026-11-23 sobre un tenant de Qlik Cloud en español. Los nombres de los campos son los de esa interfaz.

## Para qué sirve y qué no

La API key actual hace todo lo que usa el banco de pruebas, salvo `POST v1/dataflows/actions/import` y `/export`, que devuelven 403 con API key. Un cliente OAuth se creó para comprobar si con OAuth esas llamadas se habilitan.

- **No es necesario** para validar, emular, subir grafos, ejecutar scripts ni programar tareas.
- **Estado (2026-11-23):** el cliente se creó, entrega tokens y la CLI lo usa (`TenantAdmin`). **La conclusión fue que OAuth no hacía falta:** el 403 venía de usar la ruta equivocada (`v1/dataflows/...` en lugar de `v1/dataflow-apps/...`), y las rutas correctas responden igual con API key. Detalle en el apartado 10 quinquies del documento de hallazgos. Esta guía queda por si hace falta un cliente OAuth para otra cosa; si no, conviene borrar el cliente.
- Un cliente M2M actúa como un usuario bot con poder amplio sobre el tenant: se trata como una llave maestra.

## Requisitos

- Rol **Tenant Admin** para crear clientes OAuth. Con un rol menor no aparece el apartado OAuth, y la API responde `OAUTH-CLIENTS-27 "access forbidden. insufficient permissions"` al listarlos.
- La CLI de Qlik funcionando (ver `README.md`, `dfemu setup`, y el apartado 10 bis del documento de hallazgos para Windows).

## Paso 1: crear el cliente en la consola

Administración, **OAuth**, **Crear nuevo**. El asistente tiene cuatro pasos.

1. **Detalles:** tipo de cliente **Web**; un nombre que se reconozca (por ejemplo `dfemu-prueba`).
2. **Lista de elementos permitidos:** deja **vacías** la URL de redireccionamiento y los orígenes permitidos. La pantalla lo dice: la primera solo se usa en redirecciones del navegador y los segundos no se requieren cuando los tokens los usa un servidor o una CLI. Con ambos vacíos se puede continuar.
3. **Método de autenticación:** **Secreto de cliente**. Marca **Permitir máquina a máquina (M2M)**. **No** marques "Permitir la suplantación de usuarios M2M".
4. **Permisos:** busca `user_default` y ponlo en la opción que lo permita. Deja todo lo demás en "No establecido" (en especial `admin_classic`, que da acceso completo de administrador). El botón **Modificado** debe mostrar solo `user_default`. Pulsa el botón de crear.

Al crearlo aparecen el **Client ID** y el **Client secret** (64 caracteres). **El secreto solo se muestra una vez:** cópialo a un gestor de contraseñas.

## Paso 2: cambiar el consentimiento a "Trusted" (obligatorio)

En la lista de clientes OAuth, menú de tres puntos del cliente nuevo, **Cambiar método de consentimiento**, elige **De confianza** (Trusted) y confirma.

**Sin este paso todo da 401.** Es lo que nos pasó: Qlik responde `OAUTH-5: oauth client is not approved with trusted consent method`, y la CLI solo muestra un genérico "unexpected status code 401 ... the provided OAuth client credentials are probably not correct". El mensaje de la CLI despista: las credenciales estaban bien.

## Paso 3: comprobar las credenciales sin la CLI

Esta prueba muestra el error real de Qlik, que la CLI oculta (`Response body: ""`). Ejecútala tú en PowerShell: pide el secreto sin mostrarlo, no lo guarda y no imprime el token.

```powershell
$sec = Read-Host "Client secret" -AsSecureString
$plain = [System.Net.NetworkCredential]::new("", $sec).Password
"Longitud del secreto recibido: $($plain.Length)"
$body = @{ grant_type = "client_credentials"; client_id = "<CLIENT_ID>"; client_secret = $plain } | ConvertTo-Json
try {
  Invoke-RestMethod -Method Post -Uri "https://<TENANT>.<REGION>.qlikcloud.com/oauth/token" -ContentType "application/json" -Body $body | Select-Object token_type, expires_in, scope
} catch {
  "HTTP $([int]$_.Exception.Response.StatusCode)"; $_.ErrorDetails.Message
}
Remove-Variable plain, sec, body
```

Cómo leer el resultado:

| Salida | Significado |
|---|---|
| `token_type bearer`, `expires_in 21600`, `scope user_default` | Credenciales y consentimiento correctos (el token dura 6 horas) |
| `Longitud del secreto recibido: 0` | El secreto no se pegó; repetir el pegado |
| `OAUTH-5 ... trusted consent method` | Falta el paso 2 |
| `invalid_client` u otro 401 | ID o secreto equivocado, o la casilla M2M no está marcada en el cliente |

## Paso 4: crear el contexto en la CLI

Hazlo en tu propia terminal (no con `!` desde Claude), para que el secreto no pase por la conversación. La CLI pregunta la URL del tenant, `O` para OAuth, el Client ID y el Client Secret.

```powershell
$q = "C:\ProgramData\chocolatey\lib\qlik-cli\tools\qlik.exe"   # o el de .tools\qlik del repo
& $q context init dfemu-oauth
& $q context use <CONTEXTO_DE_SIEMPRE>
```

**Trampa:** `qlik context init` deja el contexto nuevo como **activo**, y si el alta falla lo deja activo de todos modos. Mientras sea el activo, `dfemu` y cualquier comando de la CLI usan esas credenciales, y fallan si son inválidas. Por eso el segundo comando: `context use` devuelve el contexto de siempre. Para ver cuál está activo: `qlik context ls` (marca `*`).

Otros mensajes:

- `context already exists with name 'dfemu-oauth'`: el contexto ya existe, quizá con credenciales viejas. Bórralo con `qlik context rm dfemu-oauth` o usa otro nombre.
- Con el contexto roto activo, un comando de `dfemu` falla con el 401 de arriba. Se arregla con `context use`.

## Paso 5: usar el contexto OAuth sin activarlo

El puente de `dfemu` lee la variable de entorno `DFEMU_QLIK_CONTEXT`. Si está definida, añade `--context <nombre>` a cada llamada a la CLI; si no, usa el contexto activo como siempre.

```powershell
$env:DFEMU_QLIK_CONTEXT = "dfemu-oauth"   # solo para esta sesión de PowerShell
python -m emulator.cli cleanup            # ejemplo: ahora usa OAuth
Remove-Item Env:DFEMU_QLIK_CONTEXT        # vuelve al contexto activo
```

Así no hace falta cambiar el contexto activo para probar.

## Seguridad

- El secreto va solo al prompt de la CLI o a un gestor de contraseñas. No lo pegues en el chat, en archivos del repo ni en la línea de comandos (queda en el historial de PowerShell).
- La CLI guarda el contexto en su propia carpeta de usuario (`.qlik`), normalmente en texto plano: cuida ese perfil y no la copies a ningún sitio.
- Un cliente M2M puede más que una API key. Cuando termine la prueba, bórralo en Administración, OAuth, o genera un secreto nuevo si lo vas a conservar.
- Si se filtra el secreto: genera uno nuevo en el menú del cliente, ejecuta `qlik context rm` y vuelve al paso 4.

## Resumen de lo que falló y por qué

| Síntoma | Causa | Arreglo |
|---|---|---|
| CLI: `401 ... credentials are probably not correct` | Cliente sin consentimiento "De confianza" (`OAUTH-5`) | Paso 2 |
| `dfemu` falla con ese 401 después del `init` | `context init` activó el contexto nuevo | `qlik context use <contexto de siempre>` |
| `context already exists` | Se repitió el `init` con el mismo nombre | `qlik context rm` o otro nombre |
| `OAUTH-CLIENTS-27 insufficient permissions` | La API key no es de Tenant Admin | Crear el cliente con un administrador |
| No se ve el motivo del 401 | La CLI no muestra el cuerpo de la respuesta | Prueba del paso 3 |
