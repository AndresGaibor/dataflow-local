---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-funnel-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating funnel charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The funnel chart lets you add a sequential chart showing the connected stages
of a process. Each stage decreases and should contain a subset of
the previous stage. The decrease is gradual,
giving the chart an ever narrower funnel.

Learn more about the [funnel chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [funnel chart API specification](https://qlik.dev/apis/javascript/sn-funnel-chart/).

The example below shows the number of candidates during sequential stages
of a recruitment process. The chart is plotted in `width` mode, where the
quantity at each stage is proportional to the upper edge of the segment.

![funnel chart example](https://qlik.dev/_astro/sn-funnel-chart.9XfYPju1.png)

```js
// configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "funnel-chart",
      load: () => Promise.resolve(window["sn-funnel-chart"]),
    },
  ],
});

// Rendering a simple funnel chart
nuked.render({
  element: document.querySelector(".funnel"),
  type: "funnel-chart",
  fields: ["Hiring Stage", "=Sum(NumberOfCandidates)"],
  properties: {
    title: "Recruitment Process",
  },
});
```

Funnel chart can represent anything that is decreasing in size,
showing a process that starts at 100% and ends with a lower percentage.
The funnel chart is the opposite to a pyramid graph, which has
increasing stages instead of decreasing stages.

The chart requires one dimension and one measure.
Unlike bar charts, funnel chart segments are centered
to create a funnel shape.

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-funnel-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-funnel-chart).

## More examples

### Area mode

You can configure the funnel chart so that the area of each item is
proportional to the measure.

![funnel chart example - area](https://qlik.dev/_astro/sn-funnel-chart-area.CqFi6D5U.png)

```js
// Rendering a funnel chart in area mode
nuked.render({
  element: document.querySelector(".funnel"),
  type: "funnel-chart",
  fields: ["Hiring Stage", "=Sum(NumberOfCandidates)"],
  properties: {
    title: "Recruitment Process",
    funnel: {
      mode: "AREA",
    },
  },
});
```

### Height mode

The height of each item is proportional to the measure.

![funnel chart example - height](https://qlik.dev/_astro/sn-funnel-chart-height.tiQJlAjg.png)

```js
// Rendering a funnel chart in height mode
nuked.render({
  element: document.querySelector(".funnel"),
  type: "funnel-chart",
  fields: ["Hiring Stage", "=Sum(NumberOfCandidates)"],
  properties: {
    title: "Recruitment Process",
    funnel: {
      mode: "HEIGHT",
    },
  },
});
```

### Ordering mode

Only order matters, the items have the same height, ordered from top to bottom.

![funnel chart example - order](https://qlik.dev/_astro/sn-funnel-chart-order.t7HXnG_p.png)

```js
// Rendering a funnel chart in order mode
nuked.render({
  element: document.querySelector(".funnel"),
  type: "funnel-chart",
  fields: ["Hiring Stage", "=Sum(NumberOfCandidates)"],
  properties: {
    title: "Recruitment Process",
    funnel: {
      mode: "ORDER",
    },
  },
});
```

### More configurations

You can also remove the dimension title, show the actual number of
candidates instead of the percentage, or color the stages by measure.

![funnel chart example - customized](https://qlik.dev/_astro/sn-funnel-chart-customized.DM9dDw6C.png)

```js
// Rendering a funnel chart with customized look
nuked.render({
  element: document.querySelector(".funnel"),
  type: "funnel-chart",

  // Defines the fields in `properties`
  properties: {
    title: "Recruitment Process",

    // Hide dimension title
    showDimensionTitle: false,

    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: { qFieldDefs: ["Hiring Stage"] },

          // Color the dimension by `MedianRequestedSalary`
          qAttributeExpressions: [
            {
              qExpression: "Avg(MedianRequestedSalary)",
              id: "colorByAlternative",
            },
          ],
        },
      ],
      qMeasures: [
        {
          qDef: { qDef: "Sum(NumberOfCandidates)" },
        },
      ],
      qInterColumnSortOrder: [1, 0],
      qInitialDataFetch: [
        {
          qLeft: 0,
          qTop: 0,
          qWidth: 2,
          qHeight: 5000,
        },
      ],
    },

    // Show actual number of candidates instead of percentage
    dataPoint: {
      auto: false,
      labelMode: "value",
    },

    // Configure color
    color: {
      auto: false,
      byMeasureDef: {
        key: "Avg(MedianRequestedSalary)",
        type: "expression",
      },
      measureScheme: "dg",
      mode: "byMeasure",
      reverseScheme: true,
    },
  },
});
```
