---
source: https://qlik.dev/embed/qlik-embed/customize/qlik-embed-webcomponent-field-selection/
last_updated: 2026-03-18T16:49:43Z
---

# Working with Qlik Sense selections

## Introduction

Qlik Sense allows users to make selections on field values in an app, which can
be used to filter data in visualizations. You can use qlik-embed to manage selections
in your Qlik Sense app.

A [complete example](#full-code-example) is available at the end of this guide.

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
| `QLIK_REDIRECT_URI`    | The Redirect URL for the OAuth2 client to provide an access token.                        |
| `QLIK_OAUTH_CLIENT_ID` | The clientId of the OAuth SPA you configured.                                             |
| `QLIK_APP_ID`          | The unique identifier of the application.                                                 |
| `QLIK_SHEET_ID`        | The unique identifier of the sheet.                                                       |

This example loads these values from `process.env`, which you can set in a `.env` file
and reference when running the example with node.js 20+ using `node --env-file=.env server.js`.

You must connect to the Qlik Sense app before manipulating fields or selection.
You do this with the `qix.openAppSession` method.

`embed:./snippets/qlik-embed/customize/web-component-field-selection.js#L1-29`

## Examples of use

Learn what you can do with the Field and Selection APIs.

### Select values in a field

Use the `app.field.select` method to select specific values in a field.

`embed:./snippets/qlik-embed/customize/web-component-field-selection.js#L52-63`

### Clear field selections

Use the `app.field.clear` method to clear a field selection.

`embed:./snippets/qlik-embed/customize/web-component-field-selection.js#L65-76`

## Full code example

Below is an example built using qlik-api and qlik-embed web components.

<details>
<summary>

### Style sheet: web-component-field-selection.css

</summary>

`embed:./snippets/qlik-embed/customize/web-component-field-selection.css`

</details>

<details>
<summary>

### JavaScript: web-component-field-selection.js

</summary>

`embed:./snippets/qlik-embed/customize/web-component-field-selection.js`

</details>

<details>
<summary>

### HTML: web-component-field-selection.html

</summary>

`embed:./snippets/qlik-embed/customize/web-component-field-selection.html`

</details>
