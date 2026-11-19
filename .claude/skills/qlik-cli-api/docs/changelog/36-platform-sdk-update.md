---
source: https://qlik.dev/changelog/36-platform-sdk-update/
last_updated: 2025-03-11T11:54:24Z
---

# Platform SDKs Update-February 2023

## Typescript SDK (v0.19.1)

### New APIs (Questions, Audits, App Scripts)

- feat: added support for the [Questions API](https://qlik.dev/apis/rest/natural-language).

```ts
  // Ask question regarding the reloaded data
  const question = 'What is the count of Prime?';
  const answer = await qlik.questions.ask({ text: question, app: { id: app.attributes.id } });
```

- feat: added support for the [Audits API](https://qlik.dev/apis/rest/audits).

```ts
  // Get the list of event sources
  const sources = await qlik.audits.getSources();
```

- feat added support for listing app script versions

```ts
  // saves a script with version called `v1`
  const script = 'Load RecNo() as N autogenerate(100);';
  await app.createScript({
    script,
    versionMessage: 'v1',
  });
  // retrieves all versions of the app script
  const { scripts } = await app.getScriptVersions();
```

### Features

- feat: Added support for registering an event listener for object `changed` and `closed` events.

  If an object handle is invalidated for instance when the data model has changed,
  then the handle will be part of a change array in the response for the method
  that caused the change.

  It is now possible to register a listener for an object,
  where `onChanged` is a custom defined function.

  `hypercube.on('changed', onChanged);`

  Handles can also be closed in a session if they are no longer valid.
  This can happen if for instance you have a handle for a field and the data model is changed/reloaded.

  `field.on('closed', onClosed);`

### Improvements

- fix: improvements for handling fetch depending on environment

  The global.fetch function is assumed to be available, and if not now an error will be returned.
  If it is not available then it can be added:

  1. For ES6-Modules and `node-fetch` you can use
     `global.fetch = (args) => import('node-fetch').then(({default: fetch}) => fetch(args));`
  2. For CommonJS and `cross-fetch` you can use `global.fetch = require('cross-fetch');`

- fix: Handling of websocket close errors.
  If an error code is set when the websocket is closed, the SDK will now return
  an error containing the code and reason for being closed.

  ```ts
  // in case of an socket error the err will contain a `closeCode` and a `closeMsg`
  session.on('socket-error', (data) => {
      err = data;
  });
  ```

### ⚠️ Breaking change

Operations on sub-resources ex: get_reloads_log were previously generated as class static methods
and required you to have the resource Id as parameter - now fixed.

```ts
public async getReloadsLog(reloadId: string): Promise<ArrayBuffer> {...}
// previously requiring appId
public async getReloadsLog(appId: string, reloadId: string): Promise<ArrayBuffer> {...}
```

This change affects the following resources: `Apps`, `Automations`, `Collections`,
`Extensions`, `Spaces`, `Themes` and `Webhooks`.

## Python SDK (v0.13.0)

### New APIs and Maintenance Fixes

- feat: adding support for the [Oauth-Tokens API](https://qlik.dev/apis/rest/oauth-tokens)

```py
config = Config(
  host=self.base_url, auth_type=AuthType.APIKey, api_key=self.api_key
)
oauth_tokens = OauthTokens(config=config)
# fetch all tokens for user with <userId>
tokens = oauth_tokens.get_oauth_tokens(userId="<userId>")
# loop through tokens and revoke them
for token in tokens:
    oauth_tokens.delete(token.id)
```

- feat: added support for the [Questions API](https://qlik.dev/apis/rest/natural-language)

```py
  # ask a question about the data
  answer = q.questions.ask(
    QueryCreate(
      app=QlikApp(id=app.attributes.id),
      text="What is the total sum of Prime?",
    )
  )
```

- feat: added support for [Apps Scripts API](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fv1%2Fapps%2F-appId%2Fscripts-post)

```py
  # create a script
  app.create_script(ScriptVersion(script="Load RecNo() as N autogenerate(200);", versionMessage="v1"))
  # list the script versions in the app
  scriptMetaList = app.get_script_versions()
  # get a specific version of a script
  scriptObject = app.get_script_by_version(scriptMetaList.scripts[0].scriptId)
  # get the current script version (latest version)
  currentScriptObject = app.get_script_by_version("current")
```

- fix: Operations on sub-resources ex: get_reloads_log were previously generated
  as class static methods and required you to have the resource Id as parameter is now fixed.
- fix: clear all listeners on session and handles closed events
- fix: raise engine connection close error
- fix: pagination users
