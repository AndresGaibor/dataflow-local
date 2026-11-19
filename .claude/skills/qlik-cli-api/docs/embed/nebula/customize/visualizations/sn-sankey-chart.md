---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-sankey-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating sankey charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Sankey chart (Sankey chart) lets you add a specific
type of flow chart to the sheet you are editing.
The chart visually emphasizes major transfers or flows
within defined system boundaries. The width of the chart
arrows is shown proportionally to the flow quantity.
The Sankey chart is included in the Visualization bundle.

- A minimum of two dimensions and one measure is required.
  You can use up to five dimensions, but only one measure.
- The dimensions do not need to be of equal size on each side of the diagram.
- You can use the dimension values to set the color of the flows in the chart.
- Link colors can be based on source or target anchor.

Learn more about the [sankey chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [sankey chart API specification](https://qlik.dev/apis/javascript/sn-sankey-chart/).

![sankey chart example](https://qlik.dev/_astro/sn-sankey-chart.DzJHuxr1.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "sankeychart",
      load: () => Promise.resolve(window["sn-sankey-chart"]),
    },
  ],
});

// Rendering a Sankey chart on the fly
nuked.render({
  type: "sankeychart",
  element: document.querySelector(".sankey"),
  fields: [
    "Region",
    "Product Group",
    "Product Type",
    "Product Line",
    "=Sum(Margin)",
  ],

  // overrides default properties
  properties: {
    node: {
      padding: 0.2,
      width: 0.3,
    },
    link: {
      opacity: 0.5,
      shadow: false,
      color: 3,
      colorBy: "custom",
    },
  },
});
```

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-sankey-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-sankey-chart).

## More examples

### Node and link colors

You can change the node colors of each dimension value.
The color should be a valid CSS color.

The colors of chart links are based on either the source or target anchors.
To apply the source or target anchor color to chart links
either use the string `='SOURCE'` or `='TARGET'`.
You can also select a separate color by entering a color code string.
The color should be a valid CSS color.

![sankey chart with customized node and link colors example ](https://qlik.dev/_astro/sn-sankey-chart-node-link-color.C0YbQ13m.png)

```js
nuked.render({
  element: document.querySelector(".object"),
  type: "sankeyChart",
  properties: {
    node: {
      padding: 0.1,
      width: 0.7,
    },
    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: {
            qFieldDefs: ["Region"],
          },
          qAttributeExpressions: [
            {
              qExpression:
                "if(Sum(total<Region> Margin) > 4500000, '#53ac94', '#ac536b')",
            },
          ],
        },
        {
          qDef: {
            qFieldDefs: ["Product Group"],
          },
          qAttributeExpressions: [
            {
              qExpression: "'#28bad7'",
            },
          ],
        },
      ],
      qMeasures: [
        {
          qDef: {
            qDef: "Sum(Margin)",
          },
          qAttributeExpressions: [
            {
              qExpression: "if(Sum(Margin) > 300000, '#53ac94', '#ac536b')",
            },
          ],
        },
      ],
      qInitialDataFetch: [
        {
          qLeft: 0,
          qTop: 0,
          qWidth: 6,
          qHeight: 1000,
        },
      ],
    },
  },
});
```

### Links colored based on their source

![sankey chart links colored based on their source example ](https://qlik.dev/_astro/sn-sankey-chart-link-source.BZ69Gyrl.png)

```js
nuked.render({
  element: document.querySelector(".object"),
  type: "sankeyChart",
  fields: ["Product Group", "Product Type"],
  properties: {
    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: {
            qFieldDefs: ["Region"],
          },
          qAttributeExpressions: [
            {
              qExpression:
                "if(Sum(total<Region> Margin) > 4500000, '#53ac94', '#ac536b')",
            },
          ],
        },
      ],
      qMeasures: [
        {
          qDef: {
            qDef: "Sum(Margin)",
          },
          qAttributeExpressions: [
            {
              qExpression: "='SOURCE'",
            },
          ],
        },
      ],
      qInitialDataFetch: [
        {
          qLeft: 0,
          qTop: 0,
          qWidth: 6,
          qHeight: 1000,
        },
      ],
    },
  },
});
```
