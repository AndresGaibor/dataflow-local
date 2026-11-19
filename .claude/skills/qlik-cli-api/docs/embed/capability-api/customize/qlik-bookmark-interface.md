---
source: https://qlik.dev/embed/capability-api/customize/qlik-bookmark-interface/
last_updated: 2025-07-03T16:05:11+02:00
---

# Get started with the Bookmark API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.
>
> To help you migrate, you can find this same example built using [qlik-embed web components](https://qlik.dev/embed/qlik-embed/customize/qlik-embed-bookmark-interface).

The Bookmark API contains methods to work with bookmarks on the Qlik Sense app
you are connected to.

You must connect to the Qlik Sense app before applying existing, or creating
new bookmarks. You do this with the `qlik.openApp` method.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require.config({
  baseUrl: `https://${config.host}/resources`,
  webIntegrationId: config.webIntegrationId
});
require(["js/qlik"], (qlik) =>{
  qlik.on('error', (error) => console.error(error));
  
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);
  //apply a bookmark
  app.bookmark.apply('pPvpTN');
});
```

## Examples of use

Learn what you can do with the Bookmark API.

### Create a new bookmark based on current selection

Use the `qlik.app.bookmark.create` method to create a bookmark based on the
current selection.

```javascript
require(["js/qlik"], (qlik) => {
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);
  //create a bookmark
  app.bookmark.create('Test','Test bookmark','fmcJkH');
}
```

### Apply an existing bookmark

Use the `qlik.app.bookmark.apply` method to apply an existing bookmark.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) =>{
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);
  //apply a bookmark
  app.bookmark.apply('pPvpTN');
});
```

### Remove a bookmark that you have applied

Use the `qlik.app.bookmark.remove` method to remove an existing bookmark.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);
  //remove a bookmark
  app.bookmark.remove('pPvpTN');
});
```
