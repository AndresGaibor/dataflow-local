---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-org-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating org charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The org chart is good for showing hierarchical structures, such as the
relations of an organization. Starts at the top and allows for navigation
through the hierarchy.

Learn more about the [org chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [org chart API specification](https://qlik.dev/apis/javascript/sn-org-chart/).

![Org chart example](https://qlik.dev/_astro/sn-org-chart.BjZ_Gsi-.png)

```js
const embeddable = window.stardust.embed(app, {
  context: { theme: 'light' },
  types: [
    {
      name: 'orgchart',
      load: () => Promise.resolve(window['sn-org-chart']);
    },
  ],
});

// Rendering an org chart
embed.render({
  type: 'orgchart',
  element: document.querySelector('.sn-org-chart'),
  fields: ['EmployeeID', 'ManagerID'],
});
```

## Dataset

The org chart expects the data sent in to be set up in a specific way. The
first dimension should contain the ID of the node, and the second dimension
should be the ID of the parent node. A node without an ID in the second
dimension will become a root node. A more thorough explanation of the expected
dataset structure can be found in the
[Org chart documentation](https://help.qlik.com/en-US/sense/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/org-chart.htm)
on Qlik Help.

## Options

- viewState - settings for the initial rendering of the org chart

## Requirements

Requires `@nebula.js/stardust` version `2.1.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-org-chart`. You can also load
through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-org-chart).

## More examples

### Title, subtitle and description

Each node can have a label, sublabel, and extra label. The label will replace
the node ID given in the first dimension in the visualization.

![Org chart with title, subtitle and description](https://qlik.dev/_astro/sn-org-chart-description.BU9sgEKt.png)

```js
// Rendering an org chart with title, subtitle and description
embed.render({
  type: "orgchart",
  element: document.querySelector(".sn-org-chart"),
  fields: ["EmployeeID", "ManagerID"],
  properties: {
    qHyperCubeDef: {
      qDimensions: [
        {
          qDef: {
            qFieldDefs: ["EmployeeID"],
          },
          qAttributeExpressions: [
            {
              qExpression: "Name",
              qAttribute: true,
              id: "labelExpression",
            },
            {
              qExpression: "Role",
              qAttribute: true,
              id: "subLabelExpression",
            },
            {
              qExpression: "Org",
              qAttribute: true,
              id: "extraLabelExpression",
            },
          ],
        },
      ],
      qInitialDataFetch: [
        {
          qWidth: 5,
          qHeight: 15,
        },
      ],
    },
  },
});
```

### Adding a measure

A measure can be added to the org chart. This will then be displayed in the
third row of the card, replacing the extra label. However, both the extra label
and the measure will be visible in the tooltip.

![Org chart with added measure](https://qlik.dev/_astro/sn-org-chart-measure.zubus5UV.png)

```js
// Rendering an org chart and adding a measure
embed.render({
  type: "orgchart",
  element: document.querySelector(".sn-org-chart"),
  fields: ["EmployeeID", "ManagerID", "=Sum([Direct Reports])"],
});
```

### Entire tree presentation mode

The default presentation mode is free, where nodes can be expanded
and collapsed to traverse the tree. It is also possible to set the presentation
mode to expandAll, which will show the whole tree at all times. It is still
possible to zoom and pan in the chart.

![Org chart showing the entire tree presentation mode](https://qlik.dev/_astro/sn-org-chart-entire-tree.Bj8tRrwd.png)

```js
// Rendering an org chart with entire tree presentation mode
embed.render({
  type: "orgchart",
  element: document.querySelector(".sn-org-chart"),
  fields: ["EmployeeID", "ManagerID"],
  properties: {
    navigationMode: "expandAll", // overrides default properties
  },
});
```

### Changing colors

The org chart can be customized by changing the background, font, and border
colors. These can be defined by a string, palette index or by expression. The
border can also be changed to no borders, just a thin all
around border, or just the top border.

![Org chart showing the custom colors and no border](https://qlik.dev/_astro/sn-org-chart-colors.Cc7XQ7gb.png)

```js
// Rendering an org chart with custom colors
embed.render({
  type: "orgchart",
  element: document.querySelector(".sn-org-chart"),
  fields: ["EmployeeID", "ManagerID"],
  properties: {
    style: {
      fontColor: {
        colorType: "colorPicker",
        color: {
          color: "#00ff00",
        },
      },
      backgroundColor: {
        colorType: "colorPicker",
        color: {
          index: 15,
        },
      },
      border: {
        top: false,
        fullBorder: false,
        colorType: "byExpression",
        colorExpression: {
          qStringExpression: {
            qExpr: "",
          },
        },
      },
    },
  },
});
```
