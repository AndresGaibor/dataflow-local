---
source: https://qlik.dev/embed/capability-api/customize/backend-api-reference/
last_updated: 2025-07-08T16:09:30Z
---

# Backend API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Backend API consists of a number of methods, and is used for communicating
with the Qlik associative engine. It provides Helper functions for Qlik
associative engine calls and access to Qlik associative engine data. In short
terms, the Backend API is a wrapper around selected Qlik Engine JSON API methods
but with the difference that the Backend API is aware of the context, that is
the current WebSocket connection and the Qlik Sense app.

For more information, see the [Qlik Sense Engine API documentation](https://qlik.dev/apis/json-rpc/qix).

## Get started

The Backend API is available for extension developers as `this.backendApi`.

```javascript
this.backendApi.eachDataRow(function(rownum, row) {
    .....
});
```

### Examples of use

Learn how to use the Backend API in your visualization extensions.

### Selections

The following Backend API methods are available when you are working with
selections in the generic object that is behind your extension.

- `selectValues`
- `selectRange`
- `clearSelections`
- `hasSelections`

Use the `selectValues` method to select values in this object. The call triggers
a repaint of the object.

```javascript
$element.find('li').on('click', function() {
    if(this.hasAttribute("data-value")) {
        var value = parseInt(this.getAttribute("data-value"), 10), dim = 0;
        self.backendApi.selectValues(dim, [value], true);
    }
});
```

The `selectRange` method selects values in this object using ranges.

```javascript
var range = {
    "qMeasureIx": 1,
    "qRange": {
        "qMin": 10,
        "qMax": 100,
        "qMinInclEq": true,
        "qMaxInclEq": true
    }
};
self.backendApi.selectRange( [range], false);
```

The `hasSelections` method can be used to find out if there are unconfirmed
selections for this object.

```javascript
this.backendApi.hasSelections();
```

If there are unconfirmed selections for this object, you can use the
`clearSelections` method to clear them.

```javascript
this.backendApi.clearSelections();
```

### Search

You can use the following Backend API methods when working with search in list objects.

- `search`
- `acceptSearch`
- `abortSearch`

Use the `search` method to search for a term in a list object. This results in an
updated layout which contains only the matching records.

```javascript
this.backendApi.search("A");
```

The `acceptSearch` method accepts the search result and makes it selected in
the field.

```javascript
this.backendApi.acceptSearch(false);
```

Use the `abortSearch` method if the search is to be aborted. This clears the
existing search and returns the object to the state it was in prior to the search.

```javascript
this.backendApi.abortSearch();
```
