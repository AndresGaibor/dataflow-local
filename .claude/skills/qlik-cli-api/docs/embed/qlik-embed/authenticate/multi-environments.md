---
source: https://qlik.dev/embed/qlik-embed/authenticate/multi-environments/
last_updated: 2025-12-08T16:58:54+01:00
---

# Using qlik-embed with multiple tenants

## Introduction

It is possible to connect different qlik-embed objects to different backend
environments. For example, two different charts on the same embedding can connect
to two different Qlik Cloud tenants.

## Configure tenant-specific authentication with import maps

Instead of using the `<script>` tag with the different data-attributes, this example uses native [import maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
and `qlik-embed`'s companion library [@qlik/api](https://github.com/qlik-oss/qlik-api-ts/blob/main/README.md) to
configure authentication.

Start by adding a `<script>` tag defining the import map:

```html
<script type="importmap">
  {
    "imports": {
      "@qlik/embed-web-components": "https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js",
      "@qlik/api": "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.js"
    }
  }
</script>
```

Then add another `<script>` tag that does the actual authentication configuration:

```html
<script type="module">
  // this imports the <qlik-embed /> web-component using the import map
  import "@qlik/embed-web-components"
  // this imports the auth module used by qlik-embed
  import { auth } from "@qlik/api";

  // define the auth config for the "first" tenant

  auth.registerHostConfig("first", { // this string will be used as a reference later.
    host: "https://first-tenant.us.qlikcloud.com",
    authType: "oauth2",
    clientId: "<client-id>",
    redirectUri: "https://your-web-application.example.com/oauth-callback.html",
    accessTokenStorage: "session",
  });

  // define the auth config for the "second" tenant

  auth.registerHostConfig("second", { // this string will be used as a reference later.
    host: "https://second-tenant.us.qlikcloud.com",
    authType: "oauth2",
    clientId: "<client-id>",
    redirectUri: "https://your-web-application.example.com/oauth-callback.html",
    accessTokenStorage: "session",
  });

</script>
```

## Embed objects using tenant-specific configurations

Once host configs are registered, you can reference them from
`<qlik-embed>` elements using the `host-config` attribute. For example:

```html
<!-- This chart will authenticate and connect to first-tenant.us.qlikcloud.com -->
<qlik-embed ui="analytics/chart" app-id="<app-id>" object-id="<obj-id>" host-config="first" />

<!-- This chart will authenticate and connect to second-tenant.us.qlikcloud.com -->
<qlik-embed ui="analytics/chart" app-id="<app-id>" object-id="<obj-id>" host-config="second" />
```

These two qlik-embed objects will authenticate against their respective tenants and
render the objects next to each other on the same web page.

## Handling authentication or connectivity errors

If an error occurs, the `<qlik-embed>` object displays an error icon in place of the
expected visualization. Hovering over the icon reveals a tooltip with details about
the error. This information can help you diagnose issues such as authentication failures,
misconfigurations, or connectivity problems. For more details, you can also look in the
browser's dev tools and console for error messages.
