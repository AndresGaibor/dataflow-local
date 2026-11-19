---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-grid-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating grid charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The grid chart uses symbols of varying size sorted in a grid
to visualize a measure across two dimensions.
The measure is the metric that determines the size of
the symbol in each crossing.

Learn more about the [grid chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [grid chart API specification](https://qlik.dev/apis/javascript/sn-grid-chart/).

![grid chart example](https://qlik.dev/_astro/sn-grid-chart.B7KM4IxO.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sn-grid-chart",
      load: () => Promise.resolve(window["sn-grid-chart"]),
    },
  ],
});

// Rendering a simple grid chart
nuked.render({
  element: document.querySelector(".grid"),
  type: "sn-grid-chart",
  fields: ["Country", "Year", "=Sum(Population)"],
  properties: {
    title: "The historical populations of some European countries",
  },
});
```

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-grid-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-grid-chart).

## More examples

### Change symbol size and shape

The size and shape of the symbols can be modified.

![grid chart example - symbol](https://qlik.dev/_astro/sn-grid-chart-symbol.C_PbqSJ1.png)

```js
// Rendering a grid chart with customized symbols
nuked.render({
  element: document.querySelector(".grid"),
  type: "sn-grid-chart",
  // fields: ['Country', 'Year', '=Sum(Population)'],
  properties: {
    title: "The historical populations of some European countries",
    dataPoint: {
      rangeBubbleSizes: [0.25, 0.85],
      symbol: "star",
    },
  },
});
```

### Customize the look of the chart

You can color the symbol by measure and add a legend to show more
information about the measure. The axis titles can be hidden
and the gridlines can be shown to further improve the look.

![grid chart example - coloring](https://qlik.dev/_astro/sn-grid-chart-color.Drds01X9.png)

```js
// Rendering a customized grid chart
nuked.render({
  element: document.querySelector(".grid"),
  type: "sn-grid-chart",

  // Define all `fields` in `properties`
  properties: {
    title: "The historical populations of some European countries",
    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: { qFieldDefs: ["Country"] },
        },
        {
          qDef: { qFieldDefs: ["Year"] },

          qAttributeExpressions: [
            {
              qExpression: "Sum(Population)",
              id: "colorByAlternative",
            },
          ],
        },
      ],
      qMeasures: [
        {
          qDef: {
            qDef: "Sum(Population)",
          },
        },
      ],
      qMode: "T",
      qAlwaysFullyExpanded: true,
    },
    color: {
      auto: false,
      mode: "byMeasure",
      measureScheme: "dg",
      reverseScheme: true,
    },
    legend: {
      show: true,
      dock: "auto",
      showTitle: true,
    },
    xAxis: {
      show: "label",
      dock: "near",
      gridLines: true,
    },
    yAxis: {
      show: "label",
      dock: "near",
      gridLines: true,
    },
  },
});
```
