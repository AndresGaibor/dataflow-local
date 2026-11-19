---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-line-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating line charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The line chart is a common, widely used visualization.
It is often used to show trends over time.

When the number of dimension values exceeds the width of the visualization,
a mini chart with a scroll bar is displayed. You can scroll by using
the scroll bar in the mini chart, or, depending on your device, by using
the scroll wheel or by swiping with two fingers.

Learn more about the [line chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [line chart API specification](https://qlik.dev/apis/javascript/sn-line-chart/).

![line chart example](https://qlik.dev/_astro/sn-line-chart.PrFK1lYz.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "line-chart",
      load: () => Promise.resolve(window["sn-line-chart"]),
    },
  ],
});
// Rendering a line chart on the fly
nuked.render({
  element: document.querySelector(".lines"),
  type: "line-chart",
  fields: ["Date.autoCalendar.YearMonth", "=Avg(Gold)", "=Avg(Bitcoin)"],

  // Overrides default properties
  properties: {
    title: "Price of Gold and Bitcoin",
    dataPoint: {
      show: true,
      showLabels: true,
    },
    gridLine: {
      auto: false,
    },
    dimensionAxis: {
      show: "all",
      dock: "near",
    },
    measureAxis: {
      spacing: 0.5,
      dock: "near",
      show: "all",
      logarithmic: true,
    },
  },
});
```

In a line chart you need at least one dimension and one measure.
With one dimension, you can include up to 15 measures.
You can also have two dimensions and one measure.

| Dimensions | Measures | Results                                                                                              |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------- |
| 1          | 1        | A simple line chart with a single line                                                               |
| 1          | 2-15     | A line chart with one line for each measure.                                                         |
| 2          | 1        | A line chart with the first dimension on the axis, and a line for each value of the second dimension |

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-line-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-line-chart).

## More examples

### One dimension, two measures, area styling

![line chart example - area](https://qlik.dev/_astro/sn-line-chart-area.Cxbw5vBJ.png)

```js
nuked.render({
  element: document.querySelector(".lines"),
  type: "line-chart",
  fields: ["Date.autoCalendar.YearMonth", "=Avg(Gold)", "=Avg(Bitcoin)"],

  // Overrides default properties
  properties: {
    lineType: "area",
  },
});
```

### One dimension, two measures, vertical orientation

![line chart example - vertical](https://qlik.dev/_astro/sn-line-chart-vertical.BLqsucoC.png)

```js
nuked.render({
  element: document.querySelector(".lines"),
  type: "line-chart",
  fields: [
    "Date.autoCalendar.Quarter",
    "Date.autoCalendar.Year",
    "=Avg(Bitcoin)",
  ],

  // Overrides default properties
  properties: {
    orientation: "vertical",
    dimensionAxis: {
      continuousAuto: false,
      dock: "near",
    },
    dataPoint: {
      show: true,
      showLabels: true,
    },
    preferContinuousAxis: false,
  },
});
```

### Two dimensions, one measure

![line chart example - 2 dimensions](https://qlik.dev/_astro/sn-line-chart-2d.Bf_9PQtT.png)

```js
nuked.render({
  element: document.querySelector(".lines"),
  type: "line-chart",
  // Two dimensions, one measure
  fields: [
    "Date.autoCalendar.Quarter",
    "Date.autoCalendar.Year",
    "=Avg(Bitcoin)",
  ],
  properties: {
    measureAxis: {
      dock: "near",
      show: "all",
      logarithmic: true,
    },
    dataPoint: {
      show: true,
      showLabels: true,
    },
  },
});
```

### One dimension, two measures, two reference lines

![line chart example - reference lines](https://qlik.dev/_astro/sn-line-chart-ref-lines.ja3gOHna.png)

```js
nuked.render({
      element: document.querySelector('.lines'),
      type: 'line-chart',
      fields: ['Date.autoCalendar.YearMonth', '=Avg(Gold)', '=Avg(Bitcoin)'],

      // Overrides default properties
      properties: {
        refLine: {
          refLines: [
            {
              label: '',
              paletteColor: {
                color: 'green',
              },
              refLineExpr: {
                value: 52500,
              },
              show: true,
            },
            {
              label: '',
              paletteColor: {
                color: 'red',
              },
              refLineExpr: {
                value: 3570,
              },
              show: true,
            },
          ],
        },
        measureAxis: {
          dock: 'near',
          show: 'all',
          logarithmic: true,
        },
        dataPoint: {
          show: true,
        },
      },
    });
  });
```
