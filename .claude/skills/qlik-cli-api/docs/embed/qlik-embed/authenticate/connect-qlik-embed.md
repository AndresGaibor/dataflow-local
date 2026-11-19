---
source: https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/
last_updated: 2026-10-20T17:44:28+02:00
---

# Auth overview

## Introduction

qlik-embed supports multiple authentication strategies:

- Qlik Cloud
  - [OAuth2 SPA](https://qlik.dev/authenticate/oauth#single-page-and-native-oauth2-client-applications):
    the recommended method for embedding where your embedded solution
    leverages the same interactive Identity Provider as your Qlik Cloud tenant.
  - [OAuth2 Impersonation](https://qlik.dev/authenticate/oauth#machine-to-machine-oauth2-impersonation-client-applications):
    the recommended method for embedding where you handle auth on your backend,
    or do not wish for users to be redirected. To create users and assign them to custom groups
    from your backend, see
    [Manage users & groups with OAuth impersonation](https://qlik.dev/embed/qlik-embed/authenticate/manage-users-groups-impersonation/).
  - [OAuth2 Anonymous embed](https://qlik.dev/authenticate/oauth): the recommended method
    for embedding analytics into public web sites.
  - API keys: a method for using per-user API keys for access. **Not recommended** as
    less secure, and doesn't support browser WebSocket connections.
  - Interactive login: a method for using the current user session and a web integration
    to auth users. **Not recommended** as ineffective with browsers which block
    third-party cookies.
  - [No authentication](#no-authentication-noauth-for-analyticssnapshot-ui) (`noauth`):
    a method for embedding static Qlik objects (for example, with the `analytics/snapshot` UI)
    without connecting to a Qlik Cloud tenant or authenticating users.
- Qlik Sense Enterprise Client Managed
  - Interactive login: a method for using the current user session. Effective when
    the Qlik Sense deployment is on the same domain as the web app. Uses cookies.
  - Anonymous access: a method for public embedding without user login, using an
    anonymous virtual proxy. For a step-by-step setup guide, see
    [Embed analytics with anonymous access on Qlik Sense Enterprise client-managed](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-client-managed-anonymous-tutorial/).
- None: a method where you must handle authenticated requests using an
  [authorization proxy](https://qlik.dev/authenticate/jwt/jwt-proxy/), which you must deploy as an
  additional component.

If you use OAuth SPA, OAuth Impersonation, or Interactive login, users accessing
Qlik content via your web app will present to Qlik Sense with their own identity.
This means you can use the native access controls for access to apps, as well as
[section access](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Security/manage-security-with-section-access.htm)
for data reduction in the app.

## Add qlik-embed to your web application

Connecting to qlik-embed when you use the web components implementation requires
adding a `<script>` element in the `<head>` tag. The attributes of the script
element are a mix of standard and specific attributes relevant to the connection
you choose.

### Standard attributes, no auth

There are four attributes that must appear in `<script>` element for using
qlik-embed web components.

- `crossorigin`: tells the script element how to handle cross-origin
  requests. Setting the attribute to `anonymous` sets the script element to
  operate in `same-origin` mode.
- `type` is set to `application/javascript` so that the web
  components JavaScript file is used by the web application.
- `src` is the URI location for the qlik-embed web components
  library. Good practices include:
  - Using the full path to the minified source file
    at `https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js`.
  - Tagging either the major (or specific) version in the path. In the example
    `https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js`
    this is denoted by the `@1`, which will pick the latest release in major version
    1 (it will match the latest in `1.x.x`). You can view [version information
    on NPM](https://www.npmjs.com/package/@qlik/embed-web-components?activeTab=versions).
- `data-host` is the URI hostname of the Qlik Cloud tenant, client
  managed server, or the authorization proxy.

This provides no auth, and looks like:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="https://example.authproxy.hostname.com"
></script>
```

### No authentication (noauth) for analytics/snapshot UI

Use the `data-auth-type="noauth"` attribute if you want to embed static analytics snapshots offline, without connecting
to a Qlik Cloud tenant or authenticating users.
You can only use this authentication type with the `analytics/snapshot` UI, where you provide all the required data as a
JSON payload.

When using the `data-auth-type="noauth"` attribute, qlik-embed retrieves all required resource files from the Qlik CDN,
and does not fetch any data or resources from your Qlik Cloud tenant.

Your script should look like:

```html
<script
  crossorigin="anonymous"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-auth-type="noauth"
></script>
```

If you are using qlik-embed and qlik-api together (for example, in multi-host scenarios), you must set the default host
config to use `noauth` as shown in the following example.

```javascript
auth.setDefaultHostConfig({
  authType: "noauth"
});
```

### OAuth2 Single Page Application (SPA)

OAuth clients provide a way to authorize embedded content in your web
application without relying on cookies.

With [OAuth2 SPA](https://qlik.dev/authenticate/oauth#single-page-and-native-oauth2-client-applications),
your web app and Qlik Cloud tenant should leverage the same Identity Provider for
the best user experience. Users loading your web app are directed to the Identity Provider
when content is requested from Qlik Cloud, and authorize the web app against the
Qlik Cloud tenant hosting the Qlik Sense app.

Using a single-page application OAuth client with `qlik-embed` requires
the following attributes:

- `data-client-id`: OAuth client ID for the [OAuth SPA client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa)
  on the Qlik Cloud tenant hosting the content.
- `data-redirect-uri`: the callback location in the web app after authorization.
- `data-access-token-storage`: indicates to qlik-embed whether to place the
  token in `session` storage or `local` storage. Use `session` if you wish the browser
  to remove stored tokens at the end of the session, or `local` if you wish the
  token to persist outside of the session. `session` is appropriate for most use
  cases.

Your script should look like:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components"
  data-host="https://tenant.region.qlikcloud.com"
  data-client-id="<CLIENT_ID>"
  data-redirect-uri="https://your-web-application.example.com/oauth-callback.html"
  data-access-token-storage="session"
  data-auth-type="Oauth2"
></script>
```

By default, users will be prompted to authorize the web app to access Qlik resources.
However, you can configure the web app to automatically redirect the user to the Qlik
tenant by adding the `data-auto-redirect` attribute to the script element:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components"
  data-host="https://tenant.region.qlikcloud.com"
  data-client-id="<CLIENT_ID>"
  data-redirect-uri="https://your-web-application.example.com/oauth-callback.html"
  data-access-token-storage="session"
  data-auth-type="Oauth2"
  data-auto-redirect="true"
></script>
```

This will automatically redirect the user to the Qlik tenant for authorization
when the web app is loaded.

Using the `@qlik/embed-svelte` package in a Svelte application, configure OAuth2 SPA authentication globally in your `main.ts` entry point:

> **Note:** By default, users will be prompted to authorize the Svelte app to access Qlik resources.
> However, you can configure the Svelte app to automatically redirect the user to the Qlik
> tenant by adding the `autoRedirect` property to the `hostConfig` object.

```typescript
import { importRuntimeModule } from "@qlik/runtime-module-loader";
import type { HostConfig } from "@qlik/embed-runtime/auth";

const hostConfig: HostConfig = {
  host: "https://tenant.region.qlikcloud.com",
  clientId: "<CLIENT_ID>",
  redirectUri: "https://your-web-application.example.com/oauth-callback.html",
  autoRedirect: true,
};

// Set the default hostConfig for all embed components
importRuntimeModule("auth@v1", hostConfig).then((authModule) => {
  authModule.setDefaultHostConfig(hostConfig);
});
```

Then in your component, the `QlikEmbed` component will automatically use the global hostConfig:

```svelte
<script lang="ts">
  import QlikEmbed from "@qlik/embed-svelte";
</script>

<main>
  <QlikEmbed
    ui="analytics/chart"
    appId="<APP_ID>"
    objectId="<OBJECT_ID>"
  />
</main>
```

For complete setup instructions including the OAuth callback page, refer to the [Svelte quickstart](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-svelte-quickstart/).

#### Using a callback handler with data-redirect-uri

If your web app has a single page (path), then you can opt to redirect to the page
containing the embedded content. This path will need to be configured in the
Qlik Cloud tenant as the redirect URI, as well as placed into the script component
on the embedded page.

However, most web apps have multiple paths, and in this case you should deploy
a separate OAuth callback page, such as `/oauth-callback.html`. The purpose of this
page is to act as a catch all redirect when authorization is required, simplifying
whitelisting of callback URIs.

The `data-redirect-uri` will point back to the callback page rather than the page
containing the embedded content.
Qlik provides a standardized OAuth callback handler from [`@qlik/api`](https://qlik.dev/toolkits/qlik-api/authentication/), which works
seamlessly across all embedding frameworks.
This is the recommended approach regardless of which qlik-embed variant you're using.

You can create an HTML page and add this code, adapting the
`data-host` attribute in this code to match that of `data-host` in the
embedded page.

Your OAuth callback page should look like:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <script
      crossorigin="anonymous"
      type="application/javascript"
      data-host="https://tenant.region.qlikcloud.com"
      src="https://cdn.jsdelivr.net/npm/@qlik/api@2/oauth-callback.iife.js"
    ></script>
  </head>
</html>
```

Create an `oauth-callback.html` file in your project root with the OAuth callback handler script:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <script
      crossorigin="anonymous"
      type="application/javascript"
      data-host="https://tenant.region.qlikcloud.com"
      src="https://cdn.jsdelivr.net/npm/@qlik/api@2/oauth-callback.iife.js"
    ></script>
  </head>
</html>
```

Configure your Vite build to serve this file, and point your `redirectUri` to it.
For complete setup instructions including the OAuth callback page, refer to the [Svelte quickstart](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-svelte-quickstart/).

### OAuth2 anonymous embed

> **Limitations:**
>
> - Qlik Anonymous Access is available in the Europe (Stockholm) region (`se`) . It is not available in other regions, or in
>   Qlik Cloud Government.
> - [Visualization extensions](https://qlik.dev/embed/foundational-knowledge/visualizations/) are not supported when accessed via an
>   anonymous access link for an app, due to security and API restrictions for anonymous sessions.

You can use `qlik-embed` on a public website where anyone can see Qlik
Cloud content. To do this, create an **anonymous embed** OAuth2 client and obtain an
access code by sharing the analytics app with anyone with the link. Here
are the properties `qlik-embed` required to display content anonymously:

- `data-client-id`: the OAuth client ID for the
  [anonymous embed client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-anonymous)
  on the Qlik Cloud tenant hosting the content.
- `data-auth-type`: 'anonymous'.
- `data-access-code`: the access code from the shared app.

Your anonymous embed script should look like:

`embed:./snippets/qlik-embed/anonymous-config-example.html`

### Using API keys

Add a `data-api-key` attribute to the script element and set it to the API key
you are using to make a connection.

> **Do not use API keys in production:** The credential appears in plain text of the web application and provides
> full access to the Qlik Cloud tenant with the permissions of the creating user.
> Use a more secure authentication method in production environments.

> **Note:** API key authentication doesn't support WebSocket connections in browsers.

Your script should look like:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="https://tenant.region.qlikcloud.com"
  data-api-key="<some API key value>"
></script>
```

### Using Qlik Cloud interactive login

If your web application is not impacted by third-party cookie blocking by the
browser, you can [create a web integration Id](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
in your tenant.

Use the following attributes:

- `data-web-integration` set to the Id of the web integration.
- `data-cross-site-cookies` set to `true` to instruct
  Qlik to allow cross-site cookie requests for embedded content, or `false` if your
  Qlik content and web app are on the same domain.

Your script should look like:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="https://tenant.region.qlikcloud.com"
  data-web-integration-id="bee7e4b5c786af1033e6780d0bbe9727"
  data-cross-site-cookies="true"
></script>
```

### Connecting to Qlik Sense Enterprise Client-managed

#### Prerequisites

To connect a web application to Qlik Sense Enterprise using qlik-embed in a cross-domain setup, ensure the following
prerequisites are met:

1. **Browser Settings**: Browser must accept third-party cookies.
2. **Virtual Proxy Configuration**: Virtual Proxies (central or custom) must be correctly
   [set up](https://qlik.dev/embed/qlik-embed/authenticate/setting-up-qmc) to accept incoming connections.

#### Usage

Before using `qlik-embed` to connect to a Qlik Sense Enterprise client-managed site,
users must be authenticated. Authentication
mechanisms can vary and must be handled by the application connecting to Qlik Sense Enterprise
client-managed.

For a default setup, one simple method is to open a browser tab and log in to the Qlik Sense server that the application
needs to connect to. Once authenticated, qlik-embed can establish a connection and interact with the client-managed
edition of Qlik Sense Enterprise client-managed.

Use the following attributes in your `<script>` element to configure the connection:

- `data-auth-type`: Set this to `windowscookie`.
- `data-host`: Specify the HTTP address of the Qlik Sense server. If a virtual proxy is configured, include its path
  (for example: `https://senseserver.example.com` or `https://senseserver.example.com/virtualproxypath`).

Here's an example of a script for connecting `qlik-embed` to Qlik Sense client-managed:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-auth-type="windowscookie"
  data-host="https://senseserver.example.com"
></script>
```

## Next steps

After configuring your qlik-embed connection script, you can begin embedding Qlik analytics into your web application.
For a step-by-step guide, see the [qlik-embed
quick start tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart).
