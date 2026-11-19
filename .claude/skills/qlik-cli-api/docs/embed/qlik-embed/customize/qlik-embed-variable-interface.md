---
source: https://qlik.dev/embed/qlik-embed/customize/qlik-embed-variable-interface/
last_updated: 2026-03-18T16:49:43Z
---

# Working with Qlik Sense variables

## Introduction

Variables are a powerful feature in Qlik Sense that allow you to store and reuse
values across your app. This guide shows you how to use qlik-embed to create,
interact with, and delete variables in Qlik Sense.

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
| `QLIK_OAUTH_CLIENT_ID` | The clientId of the OAuth SPA you configured.                                             |
| `QLIK_REDIRECT_URI`    | The Redirect URL for the OAuth2 client to provide an access token.                        |
| `QLIK_APP_ID`          | The unique identifier of the application.                                                 |
| `QLIK_OBJECT_ID`       | The unique identifier of the sheet.                                                       |

This example loads these values from `process.env`, which you can set in a `.env` file
and reference when running the example with node.js 20+ using `node --env-file=.env server.js`.

You must connect to the Qlik Sense app before manipulating fields or selection.
You do this with the `qix.openAppSession` method.

`embed:./snippets/qlik-embed/customize/web-component-variable.js#L1-31`

## Examples of use

Learn what you can do with the Variable API.

### Create a new variable

Use the `createVariableEx` method of a Qix Doc object to create a new variable.

`embed:./snippets/qlik-embed/customize/web-component-variable.js#L67-81`

### List variables

Use the `qVariableList.qItems` property from the layout of an app Session object.

`embed:./snippets/qlik-embed/customize/web-component-variable.js#L33-54`

### Delete variables

Use the `app.destroyVariableById` method of a Qix Doc object to delete a variable identified by Id.

`embed:./snippets/qlik-embed/customize/web-component-variable.js#L83-88`

## Full code example

Below is an example built using qlik-api and qlik-embed web components.

<details>
<summary>

### Style sheet: web-component-variable.css

</summary>

`embed:./snippets/qlik-embed/customize/web-component-variable.css`

</details>

<details>
<summary>

### JavaScript: web-component-variable.js

</summary>

`embed:./snippets/qlik-embed/customize/web-component-variable.js`

</details>

<details>
<summary>

### HTML: web-component-variable.html

</summary>

`embed:./snippets/qlik-embed/customize/web-component-variable.html`

</details>
