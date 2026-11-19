---
source: https://qlik.dev/embed/capability-api/customize/qlik-selectionstate-interface/
last_updated: 2026-06-29T09:07:47+02:00
---

# Get started with the Selection API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Selection API is the external interface to Qlik Sense selection state data
and it allows developers to work with selection state data returned from the
Qlik associative engine without having deeper knowledge of internal constructs.

The `qlik.app.selectionState` method is the entry point to the Selection API. It
creates a `QSelectionState` object that encapsulates the selection state.

```javascript
const config = {
  host: '<TENANT_URL>',
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require(["js/qlik"], (qlik) => {
  //open apps -- inserted here --
  const app = qlik.openApp('<APP_ID>', config);

  const selState = app.selectionState( );
  const listener = () => {
    alert('Back count:' + selState.backCount);
    selState.OnData.unbind( listener );
  };
  selState.OnData.bind( listener );
```

[selectionState method](https://qlik.dev/apis/javascript/capability/#definitions-qapp-entries-selectionstate)

## Examples of use

Learn what you can do with the Selection API.

### Example based on AngularJS

Main script:

```javascript
 $scope.selState = app.selectionState( );
```

AngularJS template:

```html
<button type="button" class="btn btn-default btn-xs" 
ng-click="selState.clearAll()" aria-label="Clear">
  <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
</button>

<li ng-repeat="sel in selState.selections">{{sel.fieldName}}: {{sel.qSelected}}
  <button type="button" class="btn btn-default btn-xs" 
  ng-click="sel.field.clear()" aria-label="Lock">
    <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
  </button>
</li>
```
