---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-bullet-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating bullet charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The bullet chart displays a gauge with extended options.
Bullet charts can be used to visualize and compare performance of
a measure to a target value and to a qualitative scale,
such as poor, average, and good.

Learn more about the [bullet chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [bullet chart API specification](https://qlik.dev/apis/javascript/sn-bullet-chart/).

In the example below, the sales in different quarters are compared
using a bullet chart.

![bullet chart example](https://qlik.dev/_astro/sn-bullet-chart.CtIM8dpa.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "bullet-chart",
      load: () => Promise.resolve(window["sn-bullet-chart"]),
    },
  ],
});

// Rendering a simple bullet chart
nuked.render({
  element: document.querySelector(".bullet"),
  type: "bullet-chart",
  fields: ["Quarter", "=Sum(Sales)"],
  properties: {
    title: "Sales by Quarters",
  },
});
```

You can create a bullet chart with one dimension and one measure,
or no dimension and multiple measures.

| Dimensions | Measures | Results                                                                                   |
| ---------- | -------- | ----------------------------------------------------------------------------------------- |
| 1          | 1        | A bullet chart with columns corresponding to different values in the dimension            |
| 0          | n        | A bullet chart with columns corresponding to the measures, aggregated over the dimension. |

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-bullet-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-bullet-chart).

## More examples

### Horizontal bullet chart with common range

Sometime it is easier for the eyes to perceive the information from a
bullet chart if it is horizontal and its measure has a common range.

![bullet chart example - horizontal, with common range](https://qlik.dev/_astro/sn-bullet-chart-horizontal.BUHwt_Ps.png)

```js
// Render a bullet chart horizontally, and with common range
nuked.render({
  element: document.querySelector(".bullet"),
  type: "bullet-chart",
  fields: ["Quarter", "=Sum(Sales)"],
  properties: {
    title: "Sales by Quarters",
    orientation: "horizontal",
    measureAxis: {
      commonRange: true,
      dock: "near",
    },
  },
});
```

### Adding target

By adding targets, you can compare not only the sales between
different quarters but also the sale of each quarter to its sale target.

![bullet chart example - with targets](https://qlik.dev/_astro/sn-bullet-chart-with-targets.CP4F1Mm0.png)

```js
// Rendering a bullet chart with targets
nuked.render({
  element: document.querySelector(".bullet"),
  type: "bullet-chart",
  fields: ["Quarter"],

  // Define `qMeasures` in `properties` instead of in `fields`
  properties: {
    title: "Sales by Quarters",
    qHyperCubeDef: {
      qMeasures: [
        {
          qDef: {
            qDef: "Sum(Sales)",
            target: "Sum([Sale targets])",
          },
          qSortBy: {
            qSortByNumeric: -1,
          },
          qAttributeExpressions: [
            {
              qExpression: "Sum([Sale targets])",
              id: "bullet-target",
            },
          ],
        },
      ],
      qInitialDataFetch: [
        {
          qLeft: 0,
          qTop: 0,
          qWidth: 15,
          qHeight: 500,
        },
      ],
    },

    // Horizontal, with common range
    orientation: "horizontal",
    measureAxis: {
      commonRange: true,
      dock: "near",
    },
  },
});
```

### Add color segments

You can also add color segments to the chart to show poor/normal/good
performance. Here two limits
are added, splitting the range into three segments: red (lower than
90% of the target), yellow (within 90-110% of the target),
and green (higher than 110% of the target).

![bullet chart example - with segments](https://qlik.dev/_astro/sn-bullet-chart-segments.DmbyaGDn.png)

```js
// Rendering a bullet chart with segments
nuked.render({
  element: document.querySelector(".bullet"),
  type: "bullet-chart",

  // Define all `fields` in `properties`
  properties: {
    title: "Sales by Quarters",

    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: {
            qFieldDefs: ["Quarter"],
            qSortCriterias: [{ qSortByAscii: 1 }],
          },
        },
      ],
      qMeasures: [
        {
          qDef: {
            qDef: "Sum(Sales)",
            target: "Sum([Sale targets])",
            conditionalColoring: {
              segments: {
                limits: [
                  {
                    value: {
                      qValueExpression: {
                        qExpr: "Sum([Sale targets])*0.9",
                      },
                    },
                  },
                  {
                    value: {
                      qValueExpression: {
                        qExpr: "Sum([Sale targets])*1.1",
                      },
                    },
                  },
                ],
                paletteColors: [
                  {
                    color: "#7c4345",
                  },
                  {
                    color: "#e0db4d",
                  },
                  {
                    color: "#53ad55",
                  },
                ],
              },
            },
          },
          qSortBy: {
            qSortByNumeric: -1,
          },
          qAttributeExpressions: [
            {
              id: "bullet-target",
              qExpression: "Sum([Sale targets])",
            },

            {
              id: "bullet-segment",
              qExpression: "Sum([Sale targets])*0.9",
            },
            {
              id: "bullet-segment",
              qExpression: "Sum([Sale targets])*1.1",
            },
          ],
        },
      ],
      qInitialDataFetch: [
        {
          qLeft: 0,
          qTop: 0,
          qWidth: 15,
          qHeight: 500,
        },
      ],
      qInterColumnSortOrder: [0, 1],
    },

    // Horizontal, with common range
    orientation: "horizontal",
    measureAxis: {
      commonRange: true,
      dock: "near",
    },
  },
});
```

### Multiple measures, no dimension

The bullet chart can also be defined with no dimension and multiple measures.
Each bar represents corresponding measure aggregate over the dimension.

![bullet chart example - no dimension](https://qlik.dev/_astro/sn-bullet-chart-no-dimension.Dz3ItzDY.png)

```js
// Rendering a bullet chart with three measures and no dimension
nuked.render({
  element: document.querySelector(".bullet"),
  type: "bullet-chart",
  fields: ["=Sum(Coffee)", "=Sum(Tea)", "=Sum(Sales)"],
  properties: {
    title: "Sales of Coffee, Tea, and Total",
  },
});
```
