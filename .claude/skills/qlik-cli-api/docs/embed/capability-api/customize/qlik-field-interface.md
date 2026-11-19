---
source: https://qlik.dev/embed/capability-api/customize/qlik-field-interface/
last_updated: 2025-07-08T16:09:30Z
---

# Get started with the Field API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.
>
> To help you migrate, you can find this same example built using [qlik-embed web components](https://qlik.dev/embed/qlik-embed/customize/qlik-embed-webcomponent-field-selection).

The `qlik.app.field` method is the entry point to the Field API. It returns a
`QField` object with methods and properties that can be used to manipulate the field.

[field method](https://qlik.dev/apis/javascript/capability/#definitions-qapp-entries-field)

You must first connect to the Qlik Sense app, and you do this with the
`qlik.openApp` method. You then use the `qlik.app.field` method to get a field
reference with methods that can be used to manipulate the field.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  //get a field reference and clear the field selection
  const lastNameField = app.field('LastName');
  lastNameField.clear();
});
```

## Examples of use

Learn what you can do with the Field API.

### Select values in a field

Use the `app.field.selectValues` method to select specific values in a field.

Example 1: Using standard syntax

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>' //only needed for SaaS editions
};
require(["js/qlik"], (qlik) => {
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  // select values - standard syntax
  app.field('LastName').selectValues([{qText: "Jones"},{qText: "Bush"},{qText:
  "Obama"}], true, true);
});
```

Example 2: Using simplified syntax

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  //select values - simplified syntax
  app.field('LastName').selectValues(["Jones"], true, true);
});
```

### Clear field selections

Use the `app.field.clear` method to clear a field selection.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  //get a field reference and clear the field selection
  const lastNameField = app.field('LastName');
  lastNameField.clear();
});
```

The `app.field.clearOther` method clears all fields except the selected one.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>' 
};
require(["js/qlik"], (qlik) => {
  // open the app
  const app = qlik.openApp('<APP_ID>', config);
  //clears all fields except the selected one
  app.field('LastName').clearOther(true);
});
```
