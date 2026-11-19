---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-bar-chart/
last_updated: 2026-03-18T16:49:43Z
---

# Creating bar charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The bar chart is suitable for comparing multiple values. The dimension
axis shows the category items that are compared, and the measure axis
shows the value for each category item.

Learn more about the [bar chart](https://qlik.dev/embed/foundational-knowledge/visualizations/barchart),
or review the [bar chart API specification](https://qlik.dev/apis/javascript/sn-bar-chart/).

![bar chart example](https://qlik.dev/_astro/sn-bar-chart.i-mBLsNv.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "barchart",
      load: () => Promise.resolve(window["sn-bar-chart"]),
    },
  ],
});

// Rendering a bar chart on the fly
nuked.render({
  type: "barchart",
  element: document.querySelector(".bars"),
  fields: ["Dim1", "=Sum(Expression1)"],
  options: {
    direction: "ltr",
    freeResize: true,
    viewState: {
      scrollPosition: 25,
    },
  },
  properties: {
    color: { mode: "byDimension" }, // overrides default properties
  },
});
```

## Options

- direction - ltr/rtl
- freeResize - in conjunction with snapshotData on layout,
  lets the chart ignore size set on snapshotData
- viewState - settings for the initial rendering of the table
  - viewState.scrollPosition - pixel position of the scroll

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-bar-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-bar-chart).

## More examples

You can make more complex comparisons of data by using grouped or stacked bars.
This requires using two dimensions and one measure.
The [Grouped bar chart](#grouped-bar-chart) and
[Stacked bar chart](#stacked-bar-chart)
use the same two dimensions and the same measure.

You can change the orientation of a bar chart by following
this [Horizontal bar chart](#horizontal-bar-chart) example.

### Grouped bar chart

Grouped bars: with grouped bars, you can compare
two or more items in the same categorical group.

![bar chart grouped example](https://qlik.dev/_astro/sn-bar-chart-grouped.DUbg9ALM.png)

```js
// Rendering a bar chart on the fly
nuked.render({
  type: "barchart",
  element: document.querySelector(".bars"),
  fields: ["Product Group", "=Sum(Sales)", "=Sum(Margin)"],
  // overrides default properties
  properties: {
    barGrouping: {
      grouping: "grouped",
    },
    dataPoint: {
      showLabels: true,
      showSegmentLabels: false,
      showTotalLabels: true,
    },
  },
});
```

### Stacked bar chart

Stacked bars: with stacked bars it is easier to compare
the total quantity between different months.
Stacked bars combine bars of different groups on top of each other
and the total height of the resulting bar represents the combined result.

![bar chart stacked example](https://qlik.dev/_astro/sn-bar-chart-stacked.DUeCJrzS.png)

```js
// Rendering a bar chart on the fly
nuked.render({
  type: "barchart",
  element: document.querySelector(".bars"),
  fields: ["Product Group", "=Sum(Sales)", "=Sum(Margin)"],
  // overrides default properties
  properties: {
    barGrouping: {
      grouping: "stacked",
    },
    dataPoint: {
      showLabels: true,
      showSegmentLabels: true,
      showTotalLabels: true,
    },
  },
});
```

### Horizontal bar chart

The bar chart can be displayed horizontally or vertically
by setting `orientation` property to `horizontal` or `vertical`,
as a horizontal bar chart example below:

![bar chart horizontal example](https://qlik.dev/_astro/sn-bar-chart-horizontal.DqThNSm5.png)

```js
// Rendering a bar chart on the fly
nuked.render({
  type: "barchart",
  element: document.querySelector(".bars"),
  fields: ["Product Group", "=Sum(Sales)", "=Sum(Margin)"],
  // overrides default properties
  properties: {
    barGrouping: {
      grouping: "grouped",
    },
    dataPoint: {
      showLabels: true,
      showSegmentLabels: false,
      showTotalLabels: true,
    },
    orientation: "horizontal",
  },
});
```
