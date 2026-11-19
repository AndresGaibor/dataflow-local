---
source: https://qlik.dev/embed/capability-api/customize/qlik-interface-interface/
last_updated: 2025-07-08T16:09:30Z
---

# Using the Root API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Root API is the external interface to Qlik Sense and is available as the
`qlik` namespace. It provides methods opening apps, get a reference to the
current app, set the specific language, and registering callbacks for error
handling. The Root API also holds methods for listing available apps and
extensions, and registering extensions that you build on the fly (using the
Visualization API).

The Root API is available for mashup developers as the `qlik` namespace.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>' //only needed for SaaS editions
};
require(["js/qlik"], (qlik) =>{
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
});
```

## Examples of use

Learn what you can do with the Root API.

### Open an app and access the App API

You must connect to the Qlik Sense app containing the objects you want to
display on your web page. You do this with the `qlik.openApp` method.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) =>{
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  // insert Qlik objects into the page.
  app.getObject(document.getElementById('LB01'), 'uPyZavD');
});
```

You can also have multiple apps open at the same time.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
const app = qlik.openApp('<APP_ID>', config);
const app2 = qlik.openApp('<APP_ID>', config);
```

In return, you get an app JavaScript object with app methods.
See [App API](https://qlik.dev/apis/javascript/capability/#entries-js/qlik-entries-openapp).

### Set a specific language

You can set a specific language for the Qlik Sense session. It should be defined
before the app is opened, meaning the qlik.setLanguage method should be called
before the `qlik.openApp` method is called.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) =>{
  //set the language to something else than default language
  qlik.setLanguage('es-EN')
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);
  // insert Qlik Sense objects into the page
  app.getObject(document.getElementById('LB01'), 'uPyZavD');
});
```
