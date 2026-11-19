---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-pie-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating pie charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

A pie chart is a circular chart divided into more slices
that each represent a proportion of the whole.
Pie charts are most visually efficient when a small number (10 or fewer)
of slices is displayed.

Learn more about the [pie chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [pie chart API specification](https://qlik.dev/apis/javascript/sn-pie-chart/).

![pie chart example](https://qlik.dev/_astro/sn-pie-chart.DTCMA52i.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "pie-chart",
      load: () => Promise.resolve(window["sn-pie-chart"]),
    },
  ],
});
// Rendering a pie chart on the fly
nuked.render({
  element: document.querySelector(".pie"),
  type: "pie-chart",
  fields: ["Year", "=Avg(Price)"],

  // Overrides default properties
  properties: {
    title: "Price of Cars by Year",
    dataPoint: {
      labelMode: "none",
    },
  },
});
```

In a pie chart you need at least one dimension and one measure.
The dimension determines what kind of data is represented on the slices.
The measure determines the angle of each slice.
A second measure can be added, this one determines the radius of the slices.

Two types of pie chart views are available:
the traditional pie chart and the hollow-centered donut chart.

## Requirements

Requires `@nebula.js/stardust` version `1.2.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-pie-chart`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-pie-chart).

## Examples

The examples below show some possible configurations for the pie chart.

### One dimension, one measure, value labels

![pie chart example - value labels](https://qlik.dev/_astro/sn-pie-chart-value-labels.BT4hFrT5.png)

```js
nuked.render({
  element: document.querySelector(".pie"),
  type: "pie-chart",
  fields: ["Country", "=Avg(Price)"],

  // Overrides default properties
  properties: {
    title: "Price of Cars by Country",
    dataPoint: {
      labelMode: "value",
    },
  },
});
```

### One dimension, two measures, percentage labels

![pie chart example - two measures](https://qlik.dev/_astro/sn-pie-chart-2-meas.DlsnOB8M.png)

```js
nuked.render({
  element: document.querySelector(".pie"),
  type: "pie-chart",
  fields: ["Country", "=Avg(Price)", "=Avg(Horsepower)"],

  // Overrides default properties
  properties: {
    title: "Price and horsepower by country",
    dataPoint: {
      labelMode: "share",
    },
  },
});
```

### One dimension, one measure, donut chart view

![pie-chart example - donut view](https://qlik.dev/_astro/sn-pie-chart-donut-view-1-meas.AdF-XVaX.png)

```js
nuked.render({
  element: document.querySelector(".pie"),
  type: "pie-chart",
  fields: ["Country", "=Avg(Price)"],

  // Overrides default properties
  properties: {
    title: "Price by country",
    dataPoint: {
      labelMode: "share",
    },
    donut: {
      showAsDonut: true,
    },
  },
});
```

### One dimension, two measures, donut chart view

![pie chart example - donut two measures](https://qlik.dev/_astro/sn-pie-chart-donut-view-2-meas.D6QN6U6B.png)

```js
nuked.render({
  element: document.querySelector(".pie"),
  type: "pie-chart",
  fields: ["Country", "=Avg(Price)", "=Avg(Horsepower)"],

  // Overrides default properties
  properties: {
    title: "Price and horsepower by country",
    dataPoint: {
      labelMode: "share",
    },
    donut: {
      showAsDonut: true,
    },
  },
});
```
