---
source: https://qlik.dev/embed/qlik-embed/customize/interact-with-ref-api/
last_updated: 2026-01-19T14:21:00Z
---

# Interacting with Qlik Sense apps via qlik-embed and refApi

If you're embedding Qlik Sense into your own web app, and you want to control the
Qlik app (selections, navigation, metadata) from your own frontend logic without using
[qlik-api](https://qlik.dev/toolkits/qlik-api/), then you can use the `refApi`.

The `refApi` provides access to the underlying connection to the Qlik Sense engine,
and as a result you can use most methods documented in the [Qlik Sense Engine API specification](https://qlik.dev/apis/json-rpc/qix/).

## When to use refApi vs qlik-api

Use the `refApi` when you need to go beyond just displaying a visualization and want
to interact directly with the embedded Qlik Sense app, for example, to make
selections, fetch field values, or list bookmarks.

Use [qlik-api](https://qlik.dev/toolkits/qlik-api/) if you need to work at a broader level, such
as calling REST APIs for automation, managing users, or accessing multiple apps
or tenants.
You can use it alongside qlik-embed on the same page and with the same
authentication pattern, as shown in [Using qlik-embed with multiple tenants](https://qlik.dev/embed/qlik-embed/authenticate/multi-environments/).

## Access the refApi

You first need a page with a qlik-embed object connected to a Qlik Sense app. This
example uses OAuth2 SPA, and an `analytics/chart` object, but you can use other auth
patterns and UIs. It includes a placeholder script module after the chart, which
provides access to the `refApi` and document model.

If you're new to host configurations, review the [qlik-embed authentication guide](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/),
and for locating Qlik Sense app and object IDs, refer to the [find embedded IDs guide](https://qlik.dev/embed/foundational-knowledge/find-ids/).

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>qlik-embed</title>

    <script
      crossorigin="anonymous"
      type="application/javascript"
      src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
      data-host="<QLIK_TENANT_URL>"
      data-client-id="<QLIK_OAUTH2_CLIENT_ID>"
      data-redirect-uri="<WEB_APP_CALLBACK_URI>"
      data-auth-type="Oauth2"
    ></script>
  </head>
  <body>
    <h1>My Chart</h1>

    <qlik-embed
      id="chart"
      ui="analytics/chart"
      app-id="<APP_ID>"
      object-id="<CHART_ID>"
    ></qlik-embed>

    <script type="module">
      const refApi = await document.getElementById("chart").getRefApi();
      const doc = await refApi.getDoc();
      // add your logic here
    </script>
  </body>
</html>
```

This code accesses the `refApi` and returns access to the loaded Qlik Sense app via the `doc` object.

Using this handle, you can perform most tasks in Qlik Sense, such as:

- List, make, clear, and navigate selections and bookmarks in your Qlik Sense app.
- Return app metadata, such as app name, app description, and last reload time.
- Create, edit, update, and delete bookmarks, charts, sheets, and more, depending on the user's
  access level.

You have full access to the document model and can call engine functions
documented in the [Qlik Sense Engine API specification](https://qlik.dev/apis/json-rpc/qix/).

## Examples

To use these examples, update the relevant HTML if user controls are provided.
Then, add the JavaScript sample to the script module in the
`// add your logic here` section.

### Make a selection in a field

To select values in a field, use the `getField` and `selectValues` methods.
The following example selects the `Albany` and `Atlanta` values in a `City` field:

```javascript
// Add into script module
const field = await doc.getField("City");
const result = await field.selectValues([
  {
    qText: "Albany",
  },
  {
    qText: "Atlanta",
  },
]);
```

This code selects these values in your app.
For a more consistent user experience, use [clear all selections](https://qlik.dev/apis/json-rpc/qix/doc/#clearall)
or [clear selections in this field](https://qlik.dev/apis/json-rpc/qix/field/#clear) before making new selections.

### Add selection navigation buttons

To add some selection controls in your app using your own components, use components
such as these buttons:

```html
<!-- Add these buttons to your HTML -->
<button id="undoBtn">Undo selections</button>
<button id="redoBtn">Redo selections</button>
<button id="clearBtn">Clear selections</button>
```

Then, add this to your script module:

```javascript
document.getElementById("undoBtn").onclick = async () => {
  const undoSelect = await doc.back();
};
document.getElementById("redoBtn").onclick = async () => {
  const redoSelect = await doc.forward();
};
document.getElementById("clearBtn").onclick = async () => {
  const clearSelect = await doc.clearAll();
};
```

### List bookmarks in the app

To return and display a list of bookmarks from the current Qlik Sense app, create
a component to display the list:

```html
<!-- Add this dropdown to your HTML -->
<label for="bookmarkDropdown">Apply bookmark:</label>
<select id="bookmarkDropdown">
  <option value="">Select a bookmark...</option>
</select>
```

Then, add this to your script module:

```javascript
async function populateBookmarks() {
  const bookmarkList = await doc.getBookmarkList();
  const dropdown = document.getElementById("bookmarkDropdown");
  // Clear existing options except the first
  dropdown.length = 1;
  bookmarkList.forEach((bm) => {
    const option = document.createElement("option");
    option.value = bm.qInfo.qId;
    option.textContent = bm.qMeta.title;
    dropdown.appendChild(option);
  });
}

document.getElementById("bookmarkDropdown").onchange = async (e) => {
  const bookmarkId = e.target.value;
  if (bookmarkId) {
    await doc.applyBookmark(bookmarkId);
  }
};

// Call this after doc is ready
populateBookmarks();
```

You can use a similar approach for sheets, as shown in the [get sheets from an app example](https://qlik.dev/embed/qlik-embed/examples/sheetlist-dropdown-example/).

### Display the app name and last reload time

To return app metadata, add HTML to present the response:

```html
<!-- Add these elements to your HTML -->
<div>
  <strong>App name:</strong> <span id="appName"></span><br>
  <strong>Last reload:</strong> <span id="lastReload"></span>
</div>
```

Add this to your module:

```javascript
document.getElementById("appName").textContent = doc.layout.qTitle;
document.getElementById("lastReload").textContent = doc.layout.qLastReloadTime;
```

This will display the app's name and the last reload time in your page.
