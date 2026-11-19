---
source: https://qlik.dev/embed/capability-api/customize/qlik-table-interface/
last_updated: 2026-10-26T15:10:16Z
---

# Get started with the Table API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Table API allows developers to work with tabular data returned from the Qlik
associative engine without having deeper knowledge of internal constructs, like
for example, a Hypercube.

The `qlik.app.createTable` method is the entry point to the Table API. It
creates a table object that wraps the hypercube. A table object of type `QTable`
is returned. It is initially empty but will eventually contain data. The table
object will be updated when selection state changes. Notification is sent when
data is available and will be triggered after each update. To receive
notification, bind a listener on `OnData` of a QTable instance.

[createTable method](https://qlik.dev/apis/javascript/capability/#definitions-qapp-entries-createtable)

Initialization using the hypercube of the current visualization:

```javascript
const table = qlik.table( this );

const listener = () => {
  const rowCount = table.rowCount;
  const colCount = table.colCount;
  table.OnData.unbind( listener );  // unregister the listener when notification
  // is no longer needed.
};
table.OnData.bind( listener ); // bind the listener
```

Your main script, based on using AngularJS:

```javascript
if ( !this.$scope.table ) => {
  this.$scope.table = qlik.table( this );
```

In your AngularJS template:

```html
<tr ng-repeat="row in table.rows">
<td ng-repeat="cell in row.cells"> {{cell.qText}} </td>;
</tr>
```

## Examples of use

Learn what you can do with the Table API.

### Export the hypercube

Example 1:

This example creates a button that exports the entire hypercube data when pressed.

```javascript
const qTable = qlik.table(this);

const $exportButton = $( document.createElement('button'));
$exportButton.html('Export');
$exportButton.bind('click', ( ) => {
  qTable.exportData({download: true});
});
$element.append($exportButton);
```

Example 2:

This example is using AngularJS in a visualization extension

Main script:

```javascript
...
paint: ( ) => {
  //set up scope.table
  if ( !this.$scope.table ) {
    this.$scope.table = qlik.table( this );
  }
}
...
```

Angular template:

```html
<button ng-click="table.exportData({download:true})">Create Excel file</button>
```

### Get more hypercube data

This example gets more data for your hypercube and is based on using AngularJS
in a visualization extension.

Main script:

```javascript
...
paint: ( ) => {
  //set up scope.table
  if ( !this.$scope.table ) {
    this.$scope.table = qlik.table( this );
  }
}
...
```

Angular template:

```html
<button ng-if="data.rowcount>data.rows.length" ng-click="data.getMoreData()">More</button>
```
