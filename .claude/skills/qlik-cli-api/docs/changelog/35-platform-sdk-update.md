---
source: https://qlik.dev/changelog/35-platform-sdk-update/
last_updated: 2025-03-11T11:54:24Z
---

# Tools and SDKs Update

Here are the latest maintenance releases for the tools and SDKs.
Those releases includes a number of bug fixes and security patches.

## Python SDK v0.12.0

- fix: add event listener to the RPC session

```python
from qlik_sdk import Auth, AuthType, Config

# custom function that should be called
def opened_listener():
    print("session opened")

# register function for event "opened"
rpc_session.on("opened", opened_listener)

with rpc_session.open() as rpc_client:
...     # opened_listener function is called when "opened" event is received in session
```

- fix: readonly and allOf fields are now handled

- fix: render param string enums for typings

- fix: set type for the session property

- fix: various improvements in the generated code-structure

## Typescript SDK v0.17.0

- feat: adding themes resource

```js
const themes = new Themes({...});

const zipStream = fs.readFileSync(path.join(__dirname, 'assets/red-theme-extension.zip'));

// upload theme
const theme = await themes.create({ name: `red-theme-test-sdk-ts-${Date.now()}` }, zipStream);
```

- fix: readonly and allOf fields are now handled
- fix: improved typings for nested object types
- fix: bumping all dependencies security patch releases

## qlik-cli v2.18.0

- feat: new resource added oauth-token

```bash
qlik oauth-token ls          # List OAuth tokens
qlik oauth-token rm <token>  # Revoke an OAuth token by ID
```

- fix: properly handle deprecated operations and commands
