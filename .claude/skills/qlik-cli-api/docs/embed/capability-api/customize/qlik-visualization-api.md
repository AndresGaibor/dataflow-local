---
source: https://qlik.dev/embed/capability-api/customize/qlik-visualization-api/
last_updated: 2025-07-03T16:05:11+02:00
---

# Using the Visualization API

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Visualization API is the external interface to Qlik Sense visualizations.
You can create new visualizations on the fly based on a session object. These
visualizations are not persisted in the app. You can also fetch already
existing visualizations from an app using the Visualization API.

> **Note:** Embedded visualizations created with the Visualization API don't inherit all Qlik Sense capabilities, for example,
> the capability to create your own context menu.

To use the Visualization API in mashups, you should first create a mashup as
described in *Get started building mashups*. You do not need to place any
existing visualizations in your mashup, they will be created using the
Visualization API, but you need to create the HTML page, configure Qlik Sense
and connect to the Qlik Sense app.

## Examples of use

Learn how to create visualizations on the fly using the Visualization API.

### Creating basic visualizations

Learn how to create basic visualizations using the Visualization API.

#### Bar chart with custom title

This example creates a bar chart with one dimension, one measure, and a custom title.

```javascript
app.visualization.create(
  'barchart',
  [
    "NetScoreName",
    "=Count(NetScoreName)"
  ],
  {
    "showTitles": true,
    "title": "Net scores"
  }
).then((vis) => {
  vis.show("QV01");
});
```

#### Toolbar extension with three buttons

This example creates a visualization using the toolbar extension example,
enabling the buttons for Clear all, Back, and Forward.

```javascript
app.visualization.create('com-qliktech-toolbar', null,
  {"buttons":{"clear":true,"back":true,"forward":true}}
).then((vis) => {
  vis.show("QV05");
});
```

#### Bar chart with general properties

This example creates a bar chart with one dimension, one measure, and definitions
for title, subtitle, and footnote.

```javascript
app.visualization.create(
  'barchart',
  ["Case Owner Group", "=Avg([Case Duration Time])"],
  {
    "title": "My title",
    "subtitle": "My subtitle",
    "footnote": "My footnote"}
).then( ( visual ) => {
  visual.show( "QV01" );
  } );
```

### Creating visualizations with colors and legends

Learn how to create visualizations with definitions for colors and legends
using the Visualization API.

#### Creating a line chart with single color

This example creates a line chart with one dimension, one measure, and
definitions for single color.

```javascript
app.visualization.create(
  'linechart',
  ["Date", "=Avg([Case Duration Time])"],
  {
    "color": {"auto": false, "singleColor": 7}
  }
).then( ( linechart ) => {
  linechart.show( "QV02" );
} );
```

#### Creating a line chart with color by measure

This example creates a line chart with one dimension, one measure, and definition
for color by measure (sequential, classes).

```javascript
app.visualization.create(
  'linechart',
  ["Date", "=Avg([Case Duration Time])"],
  {
    "color": {
      "auto": false,
      "mode": "byMeasure",
      "measureScheme": "sc"
    }
  }
).then( ( visual ) => {
  visual.show( "QV04" );
} );
```

#### Creating a line chart with labels

This example creates a line chart with one dimension, one measure, and
definitions for labels placement for the dimension and measure.

```javascript
app.visualization.create(
  'linechart',
  ["Date", "=Avg([Case Duration Time])"],
  {
    "lineType": "area",
    "nullMode": "connect",
    "dataPoint": {
      "show": true,
      "showLabels": true
    }
  }
).then( ( visual ) => {
  visual.show( "QV01" );
} );
```
