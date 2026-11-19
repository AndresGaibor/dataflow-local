---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-kpi/
last_updated: 2025-07-08T16:09:30Z
---

# Creating KPI charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The KPI visualization can show one or two measure values,
and is used to track performance.

Learn more about the [KPI chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [KPI chart API specification](https://qlik.dev/apis/javascript/sn-kpi/).

![Kpi example](https://qlik.dev/_astro/sn-kpi.Dy340fVb.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "kpi",
      load: () => Promise.resolve(window["sn-kpi"]),
    },
  ],
});

nuked.render({
  type: "kpi",
  element: document.querySelector(".kpi"),
  fields: ["=Sum(Expression1)"],
  options: {
    freeResize: true,
  },
});
```

## Options

- freeResize - in conjunction with snapshotData on layout,
  lets the chart ignore size set on snapshotData
