---
source: https://qlik.dev/embed/qlik-embed/customize/qlik-embed-bookmark-interface/
last_updated: 2026-03-18T16:49:43Z
---

# Working with Qlik Sense bookmarks

## Introduction

Bookmarks in Qlik Sense are a way to save selections for later use. You can create,
interact with, and delete bookmarks using qlik-embed.

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

You must connect to the Qlik Sense app before applying existing bookmarks
or creating new ones. You do this using the `qix.openAppSession` method.

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.js#L1-32`

## Examples of use

Learn what you can do with the Bookmark API.

### Create a new bookmark based on the current selection

Use the `createBookmark` method of the Qix Doc object object to create a bookmark based on the
current selection.

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.js#L34-62`

The JSON payload provided as a parameter to the `createBookmark` method contains these properties:

- `qType`: The type of object being created. In this case, a bookmark. Must be part of the `qInfo` object.
- `title`: The title is the value shown in the Qlik Sense user interface when users access bookmarks.
  Must be part of the `qMetaDef` object.
- `description`: A snippet of text for telling users what the bookmark is going to do.
  Must be part of the `qData` object.

### Remove a bookmark that you have applied

Use the `destroyBookmark` method to remove an existing bookmark.

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.js#L64-81`

## Full code example

Below is an example built using qlik-api and qlik-embed web components.

<details>
<summary>

### Style sheet: web-component-bookmark.css

</summary>

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.css`

</details>

<details>
<summary>

### JavaScript: web-component-bookmark.js

</summary>

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.js`

</details>

<details>
<summary>

### HTML: web-component-bookmark.html

</summary>

`embed:./snippets/qlik-embed/bookmark/web-component-bookmark.html`

</details>
