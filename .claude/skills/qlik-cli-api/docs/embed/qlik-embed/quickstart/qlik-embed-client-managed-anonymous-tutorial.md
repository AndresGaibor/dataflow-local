---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-client-managed-anonymous-tutorial/
last_updated: 2026-10-02T14:35:27+02:00
---

# Embed analytics with anonymous access on Qlik Sense Enterprise client-managed

## What you'll learn

- How anonymous access works on Qlik Sense Enterprise client-managed.
- How to configure a virtual proxy in the Qlik Management Console (QMC) for anonymous access.
- How to configure `qlik-embed` to connect to an anonymous virtual proxy.
- How to handle cross-domain embedding without user login.
- Common mistakes and how to avoid them.

## How anonymous access works on client-managed

Anonymous access on Qlik Sense Enterprise client-managed is session-based. When a browser
requests content through an anonymous-enabled virtual proxy, Qlik Sense creates an anonymous
session and issues a session cookie, without requiring a login prompt. This is different from
Qlik Cloud anonymous access, which uses OAuth2 and is only available on cloud tenants.

> **Do not use data-auth-type='anonymous':** The `data-auth-type="anonymous"` attribute is a Qlik Cloud-only setting that uses OAuth2.
> It does not work with Qlik Sense Enterprise client-managed. Omit `data-auth-type` from
> your script tag or set it to `windowscookie` when targeting a client-managed deployment.

## Prerequisites

- Qlik Sense Enterprise for Windows with Analyzer Capacity, or Qlik Analytics Platform
  (QAP). Named User licenses do not support anonymous sessions.
- Administrator access to the QMC.
- A published Qlik Sense app that anonymous users can access.
- HTTPS on both the Qlik Sense server and the embedding site (required for `SameSite=None`
  cookies used in cross-domain scenarios).
- A trusted HTTPS certificate (browser security restrictions commonly cause issues
  loading cross-site content with untrusted or expired certificates).

## Architecture overview

An anonymous embed setup has three components:

1. **An anonymous virtual proxy** configured in the QMC. All anonymous browser requests
   pass through this virtual proxy, which grants a session without requiring credentials.
2. **A Qlik Sense app** published so that anonymous users can open it.
3. **An embedding site** that loads `qlik-embed` and points it to the anonymous
   virtual proxy.

If your embedding site is on a different domain from your Qlik Sense server (cross-domain),
you must also configure CORS headers and `SameSite=None` cookies on the virtual proxy, and
optionally use a reverse proxy.

## Choose your hosting approach

You can host the HTML page that contains your `qlik-embed` components in two ways:

- **Standalone web server**: a separate web server (for example, Nginx, Apache, or a Node.js
  application server) that serves your embedding site independently of Qlik Sense. This is
  the recommended approach for most deployments.
- **Qlik Sense extension server**: upload your HTML, JavaScript, and CSS files as a Qlik
  Sense extension, which makes them available at a path under the Qlik Sense server itself.
  Because the embedding page is served from the same origin as Qlik Sense, you do not need
  CORS headers or `SameSite=None` cookies. This pattern is supported and works well for
  simple or proof-of-concept pages with no backend logic.

> **Extension server has no backend support:** If your embedding site needs server-side logic (token generation, session management,
> external API calls), use a dedicated web server instead. The extension server is not
> designed for backend applications.

## Step 1: Create an anonymous virtual proxy in the QMC

Create a dedicated virtual proxy for anonymous access. Do not modify your existing default
virtual proxy, as this would affect all authenticated users.

1. Open the QMC and go to **Virtual proxies**.

2. Select **Create new**.

3. Fill in the following required fields:

   - **Description**: for example, `Anonymous embed proxy`.
   - **Prefix**: the path segment that identifies this proxy, for example `anonym`. Browsers
     will reach Qlik Sense through `https://<your-server>/anonym`.
   - **Session cookie header name**: for example, `X-Qlik-Session-Anonym`.

4. Under **Authentication**, set **Anonymous access mode** to **Allow anonymous
   users** (sometimes shown as **Always anonymous**). This tells Qlik Sense to grant a
   session without prompting for credentials.

5. Select **Advanced** to open the advanced settings panel.

6. Add the anonymous access load balancing condition. In the **Load balancing** section,
   set the node condition to:

   ```text
   user.isAnonymous()
   ```

   This routes anonymous sessions to the correct engine node.

7. Under **Advanced**, locate **Additional response headers** and add the following headers:

   ```text
   Access-Control-Allow-Credentials: true
   Access-Control-Expose-Headers: Qlik-Csrf-Token
   ```

8. Under **Advanced**, add the hostname of your embedding site to the **Host allow list**,
   for example `external-site.com`, including the port if applicable.

9. Set the **SameSite** cookie attribute to **None**, and also set the **Secure** flag
   (both are required for cross-domain cookie exchange).
   Both settings together require HTTPS on both your embedding site and the Qlik Sense server.

10. Select **Apply**.

11. Link the new virtual proxy to the correct proxy: go to **Proxies**, open the proxy
    service (typically the central node), and select **Associate items** to link the new
    anonymous virtual proxy.

> **Same-domain embedding:** If your embedding page is served from the same domain as your Qlik Sense server, you
> do not need to configure CORS headers or `SameSite=None`. The browser treats the
> requests as same-origin and shares cookies automatically.

## Step 2: Publish the app for anonymous access

Anonymous users can only open apps that are published to a stream they have access to.
Ensure the stream has read access for anonymous users.

1. In the QMC, go to **Streams**.

2. Open or create the stream that holds the app you want to embed.

3. Under **Security rules**, add a rule that grants anonymous users read access. For example:

   ```text
   ((user.IsAnonymous()=true))
   ```

   with the **Read** action selected.

4. Publish the target app to that stream.

## Step 3: Configure qlik-embed on your embedding site

Add the `qlik-embed` script tag to the `<head>` of your embedding page. Point `data-host`
and `data-login-uri` to the anonymous virtual proxy URL you created in step 1.

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="https://<your-qlik-server>/anonym"
  data-login-uri="https://<your-qlik-server>/anonym"
  data-cross-site-cookies="true"
></script>
```

Replace `<your-qlik-server>` with your Qlik Sense server hostname, and `anonym` with
the prefix you chose in step 1.

- **`data-host`**: the base URL of the Qlik Sense server, including the virtual proxy prefix.
- **`data-login-uri`**: the URL `qlik-embed` calls to establish a session. For anonymous
  access, this must point to the anonymous virtual proxy so that Qlik Sense issues an
  anonymous session cookie rather than redirecting to a login page.
- **`data-cross-site-cookies="true"`**: required when the embedding page and the Qlik Sense
  server are on different domains. This tells `qlik-embed` to handle cross-site cookie
  exchange. Omit this attribute if embedding from the same domain.

> **data-auth-type is not required:** Do not set `data-auth-type` when connecting to an anonymous virtual proxy. The default
> cookie-based session handling in `qlik-embed` works correctly with the anonymous session
> that the virtual proxy creates. Setting `data-auth-type="anonymous"` will fail because
> that value requires a Qlik Cloud OAuth2 configuration.

## Step 4: Add an embedded visualization

In the `<body>` of your page, add a `qlik-embed` web component. Replace `<APP-ID>` and
`<OBJECT-ID>` with the IDs from your Qlik Sense app.

```html
<qlik-embed
  ui="analytics/chart"
  app-id="<APP-ID>"
  object-id="<OBJECT-ID>"
></qlik-embed>
```

For more information about UIs and parameters, see
[UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/).

## Security considerations

When using a reverse proxy in front of Qlik Sense, configure the reverse proxy to strip
any `X-Qlik-User` headers from incoming client requests before forwarding them to Qlik
Sense. This prevents clients from injecting a user identity, which would bypass the
anonymous session mechanism.

For header-based authentication setups where you inject a shared static identity (for
example, `UserDirectory=PUBLIC;UserId=anonymous`), the reverse proxy is the enforcement
point. If the proxy does not strip client-supplied headers, any user can impersonate that
identity.

## Troubleshooting

<details>
  <summary>The component does not render and the browser shows a CORS error</summary>

  - Confirm the embedding site is listed in the **Host allow list** on the virtual proxy.
  - Check that `SameSite=None` and `Secure` are set on the virtual proxy cookies. Without
    these, browsers will block cross-site cookies.
</details>

<details>
  <summary>The component does not render and the browser shows a 401 or session error</summary>

  - Confirm the virtual proxy is configured with **Anonymous access mode** set to
    **Allow anonymous users**.
  - Confirm you have linked the virtual proxy to the proxy service in the QMC.
  - Verify the app is published to a stream that anonymous users can read.
  - Check the Qlik Sense log files for session creation failures.
</details>

<details>
  <summary>Anonymous users see a login prompt</summary>

  - Check that `data-login-uri` points to the anonymous virtual proxy and not to a
    virtual proxy that requires authentication. If `data-login-uri` is missing or wrong,
    `qlik-embed` will follow the Qlik Sense login redirect, which leads to a login page.
</details>

<details>
  <summary>Content loads correctly when testing locally but fails after deployment</summary>

  - Verify HTTPS is configured on both your embedding site and the Qlik Sense server.
    `SameSite=None` cookies require a secure context. HTTP sites cannot receive these
    cookies from an HTTPS Qlik Sense server.
  - Update the **Host allow list** to include the production hostname of your embedding site,
    including the port if applicable, not just the local development hostname.
</details>

## Next steps

- [UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/): explore all available `qlik-embed`
  components and their configuration options.
- [Configure Qlik Sense Enterprise client-managed](https://qlik.dev/embed/qlik-embed/authenticate/setting-up-qmc/):
  review cross-domain setup requirements for authenticated sessions.
- [Auth overview](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/):
  compare all available authentication options for `qlik-embed`.
