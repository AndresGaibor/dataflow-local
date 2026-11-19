---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-sheet/
last_updated: 2026-03-18T16:49:43Z
---

# Embed a Qlik Sense sheet using qlik-embed web components

## Overview

In this tutorial, you'll learn how to embed a sheet from a Qlik Sense app
using qlik-embed, rather than the Capability API or iframe. While embedding
a sheet is simpler using Capability API, this example demonstrates
additional capability provided with the qlik-api.

A sheet in a Qlik Sense app is a container for one-to-many
visualizations, and the sheet's layout is accessible metadata in JSON that you
can read to recreate the sheet programmatically. The benefit of this approach is
that the layout of the sheet is created dynamically in the client and propagated
to your web application without using an iframe.

## Prerequisites

To use the example page in this guide, ensure that you have the following:

- An existing app ID and sheet ID to embed. This example uses [this demo app](https://github.com/qlik-oss/nebula.js-examples/blob/main/data/apps/the_movies.qvf)
  that you can download and use.
- A [SPA OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa/) configured.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `VARIABLE_NAME` or `<VARIABLE_NAME>`. Here is a list of
variables that appear in the sample code.

| Variable               | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `QLIK_TENANT_URL`      | The domain for the tenant you are accessing. Equivalent to `tenant.region.qlikcloud.com`. |
| `QLIK_OAUTH_CLIENT_ID` | The clientId of the OAuth SPA you configured.                                             |
| `QLIK_REDIRECT_URI`    | The Redirect URL for the OAuth2 client to provide an access token.                        |
| `QLIK_APP_ID`          | The unique identifier of the application.                                                 |
| `QLIK_SHEET_ID`        | The unique identifier of the sheet.                                                       |

This example loads these values from `process.env`, which you can set in a `.env` file
and reference when running the example with node.js 20+ using `node --env-file=.env server.js`.

## Sequence

The code example in this tutorial provides a basic, fully functional web page that executes
the following sequence:

1. Handles logging in to Qlik.
2. Loads the qlik-embed web components and qlik-api resources.
3. Connects to the app.
4. Retrieves the sheet layout.
5. Sets a target div with a CSS grid that matches the sheet's layout.
6. Iterates over each object within the sheet layout, creating a div for each and
   setting it with the same grid position as in the layout. This process also
   sets the `id` of each div to the `objectId` of the Qlik object.
7. Iterates over each div and injects each Qlik object whose `objectId` matches
   the corresponding `id`.

## Full example code

Below is an example built using qlik-api and qlik-embed web components.

<details>
<summary>

### Style sheet: web-component-sheet.css

</summary>

`embed:./snippets/qlik-embed/web-component-sheet.css`

</details>

<details>
<summary>

### JavaScript: web-component-sheet.js

</summary>

`embed:./snippets/qlik-embed/web-component-sheet.js`

</details>

<details>
<summary>

### HTML: web-component-sheet.html

</summary>

`embed:./snippets/qlik-embed/web-component-sheet.html`

</details>
