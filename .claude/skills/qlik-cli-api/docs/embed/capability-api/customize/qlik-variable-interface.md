---
source: https://qlik.dev/embed/capability-api/customize/qlik-variable-interface/
last_updated: 2025-07-03T16:05:11+02:00
---

# Get started with the Variable API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) rather than this framework.
>
> Review the tutorial [embedding Qlik Analytics using qlik-embed web components](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart).
>
> To help you migrate, [use this example](https://qlik.dev/embed/qlik-embed/customize/qlik-embed-variable-interface)
> built using qlik-embed web components.

> **Third-party cookies:** This tutorial leverages cookies for auth, which are blocked by some browser vendors.
> Please use an OAuth solution where possible, which doesn't leverage cookies.

The Variable API is the external interface to Qlik Sense variables.

You must first connect to the Qlik Sense app, and you do this with the
`qlik.openApp` method. You can then use the `qlik.app.variable.get` method to
get an existing variable.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //get an existing variable
  app.variable.get('yTgsRI').then((model) => {
    myvar = model;
  });
});
```

## Examples of use

Learn what you can do with the Variable API.

### Create a new variable

Use the `qlik.app.variable.create` method to create a new variable.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //create a new variable
  app.variable.create({
    qName : 'myvar',
    qDefinition : 'Month'
  });
});
```

### Create a session variable

You can also create a variable that only exists in the session. To do so, use
the `qlik.app.variable.createSessionVariable` method.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //create a new session variable
  app.variable.createSessionVariable({
    qName : 'myvar',
    qDefinition : 'Month'
  });
});
```

### Get the variable content

Use the `qlik.app.variable.getContent` method to get the variable content.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //get the variable content
  app.variable.getContent('MYVAR',function ( reply ){
    alert( JSON.stringify( reply ) );
  });
});
```

### Set a numeric value

Use the `qlik.app.variable.setNumValue` method to set a numeric variable value.

> **Note:** The `setNumValue` method replaces the deprecated `setContent` method.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //set numeric value
  app.variable.setNumValue('MYVAR',5);
});
```

### Set a string value

Use the `qlik.app.variable.setStringValue` method to assign a string value.

> **Note:** The `setStringValue` method replaces the deprecated `setContent` method.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open the app
  const app = qlik.openApp('<APP_ID>', config);
  //set string value
  app.variable.setStringValue('MYVAR','=(1+1)');
});
```
