---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart/
last_updated: 2026-05-06T12:24:45+02:00
---

# Get started with qlik-embed web components

Embed your first Qlik visualization in minutes using qlik-embed web components and OAuth2
single-page application authentication.

## Prerequisites

- A Qlik Cloud tenant with at least one Analytics app and visualization
- A text editor or IDE (VS Code, Notepad++, etc.)
- An [OAuth2 SPA client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa/) with:
  - Scope: `user_default`
  - Redirect URI: `http://localhost:8080/oauth-callback.html` (or your local dev URL)
  - Allowed origin: `http://localhost:8080`

## Step 1: Create your HTML file

Create a new file named `index.html`. For a minimal setup, start with basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Qlik Embed Quick Start</title>
</head>
<body>
  <h1>Embedded Qlik Visualization</h1>
  <div id="visualization"></div>
</body>
</html>
```

Or use the [complete example](#full-code) at the end of this guide, which includes styling and both embed types.

## Step 2: Add the qlik-embed script

In the `<head>` section of your HTML file, add the qlik-embed script tag.
This initializes the qlik-embed library and configures your OAuth authentication:

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="<QLIK_TENANT_URL>"
  data-client-id="<QLIK_OAUTH2_CLIENT_ID>"
  data-redirect-uri="<WEB_APP_CALLBACK_URI>"
  data-access-token-storage="session"
></script>
```

Replace placeholders:

- `<QLIK_TENANT_URL>`: Your Qlik Cloud tenant URL (for example, `https://your-tenant.us.qlikcloud.com`)
- `<QLIK_OAUTH2_CLIENT_ID>`: Your [OAuth client ID](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa/)
- `<WEB_APP_CALLBACK_URI>`: Your callback page URL (for example, `http://localhost:8080/oauth-callback.html`)

## Step 3: Create the OAuth callback page

Create a new file named `oauth-callback.html` in the same directory as `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <script
      crossorigin="anonymous"
      type="application/javascript"
      data-host="<QLIK_TENANT_URL>"
      src="https://cdn.jsdelivr.net/npm/@qlik/api@2/oauth-callback.iife.js"
    ></script>
  </head>
</html>
```

Replace `<QLIK_TENANT_URL>` with your Qlik Cloud tenant URL (must match `data-host` in Step 2).

## Step 4: Embed visualizations

In the `<body>` of `index.html`, add qlik-embed components. You can embed a single chart or multiple embeds.

**Option A: Single chart**

```html
<qlik-embed
  ui="analytics/chart"
  app-id="<APP_ID>"
  object-id="<OBJECT_ID>"
></qlik-embed>
```

**Option B: Full Qlik Sense interface**

```html
<qlik-embed
  ui="classic/app"
  app-id="<APP_ID>"
></qlik-embed>
```

Replace placeholders:

- `<APP_ID>`: Your [app ID](https://qlik.dev/embed/foundational-knowledge/find-ids/)
- `<OBJECT_ID>`: Your visualization ID (for `analytics/chart` only)

> **Note:** The `analytics/chart` UI renders nebula.js visualizations only. Use `classic/app` for the full Qlik Sense experience. See [UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/) for all options.

## Step 5: Run your application

1. Start a local web server. If you have Python installed:

```bash
python -m http.server 8080
```

Or with Node.js:

```bash
npx http-server -p 8080
```

2. Open your browser to `http://localhost:8080`.

3. Click the **Authorize** button. The browser redirects you to Qlik Cloud login.

4. Log in with your credentials.

After authentication, you're redirected back and your embedded visualization loads.

> **Note:** If your server runs on a different port, update your OAuth client configuration and the `data-redirect-uri` in your HTML to match.

## Troubleshooting

- **OAuth errors**: Verify `data-redirect-uri` matches your OAuth client configuration and
  `oauth-callback.html` is in the same directory
- **Visualization not showing**: Verify `app-id` and `object-id` are correct and you have permissions in Qlik Cloud
- **"Tenant not found"**: Check your `data-host` URL matches your Qlik Cloud tenant

## Next steps

Now that you have a working embed:

- [Explore other UI types](https://qlik.dev/embed/qlik-embed/parameters/) (`analytics/sheet`, `analytics/selections`, and more)
- [Add interactivity with the ref API](https://qlik.dev/embed/qlik-embed/customize/interact-with-ref-api/)
- [Deploy to production](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/)
- View the [complete working example](#full-code)

## Full code

<details>
  <summary>index.html</summary>

  `embed:./snippets/qlik-embed/quickstart-webcomponent-complete.html`
</details>

<details>
  <summary>oauth-callback.html</summary>

  `embed:./snippets/qlik-embed/oauth-callback-page-example.html`
</details>
