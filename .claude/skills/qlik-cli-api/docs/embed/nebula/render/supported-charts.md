---
source: https://qlik.dev/embed/nebula/render/supported-charts/
last_updated: 2026-06-02T18:15:45+01:00
---

# Supported Charts

## Nebula charts supported by Insight Advisor and Insight Advisor APIs

Charts rendered in Qlik Sense are listed in the following table. Many of these
charts are available as an embeddable nebula.js chart. Insight Advisor inside
the Qlik Sense client uses a subset of these visualizations to render insights.

Insight Advisor APIs will return the associated hypercube properties that can be
created in any engine session and rendered using any visualization library of
choice. However, the plug and play support provided by nebula.js is only a
subset of these visualizations.

The support matrix of these charts both within
nebula.js and through the API response is outlined here. If you're instead interested
in embedding support, explore [visualization types](https://qlik.dev/embed/foundational-knowledge/visualizations).

Legend: ✔ supported ⛔ not supported

| Qlik Sense visualization name | Nebula visualization name | Nebula support | Insight Advisor support (Inside Qlik Sense client) | Insight Advisor API support (using nebula.js) |
| ----------------------------- | ------------------------- | -------------- | -------------------------------------------------- | --------------------------------------------- |
| barchart                      | sn-bar-chart              | ✔              | ✔                                                  | ✔                                             |
| boxplot                       | sn-boxplot                | ✔              | ✔                                                  | ✔                                             |
| bulletchart                   | sn-bullet-chart           | ✔              | ✔                                                  | ✔                                             |
| action-button                 | sn-action-button          | ✔              | ⛔                                                  | ⛔                                             |
| combochart                    | sn-combo-chart            | ✔              | ✔                                                  | ✔                                             |
| distributionplot              | sn-distplot               | ✔              | ✔                                                  | ✔                                             |
| gauge                         |                           | ⛔              | ✔                                                  | ✔                                             |
| sn-grid-chart                 | sn-grid-chart             | ✔              | ✔                                                  | ✔                                             |
| histogram                     | sn-histogram              | ✔              | ⛔                                                  | ⛔                                             |
| kpi                           | sn-kpi                    | ✔              | ✔                                                  | ✔                                             |
| linechart                     | sn-line-chart             | ✔              | ✔                                                  | ✔                                             |
| map                           | sn-map                    | Experimental1  | ✔                                                  | ⛔                                             |
| mekkochart                    | sn-mekko-chart            | ✔              | ✔                                                  | ✔                                             |
| sn-nav-menu                   | sn-nav-menu               | ✔              | ⛔                                                  | ⛔                                             |
| sn-org-chart                  | sn-org-chart              | ✔              | ⛔                                                  | ⛔                                             |
| piechart                      | sn-pie-chart              | ✔              | ✔                                                  | ✔                                             |
| pivot-table                   | sn-pivot-table            | ✔1             | ✔                                                  | ✔                                             |
| scatterplot                   | sn-scatter-plot           | ✔              | ✔                                                  | ✔                                             |
| table                         | sn-table                  | ✔1             | ✔                                                  | ✔                                             |
| treemap                       | sn-treemap                | ✔              | ✔                                                  | ✔                                             |
| sn-video-player               | sn-video-player           | ✔              | ⛔                                                  | ⛔                                             |
| waterfallchart                | sn-waterfall              | ✔              |                                                    | ✔                                             |
| qlik-funnel-chart             | sn-funnel-chart           | ✔              | ✔                                                  | ✔                                             |
| qlik-multi-kpi                |                           | ⛔              | ✔                                                  | ⛔                                             |
| qlik-radar-chart              |                           | ⛔              | ✔                                                  | ⛔                                             |
| qlik-sankey-chart-ext         | sn-sankey-chart           | ✔              | ✔                                                  | ✔                                             |
| qlik-variance-waterfall       |                           | ⛔              | ✔                                                  | ⛔                                             |
| qlik-word-cloud               |                           | ⛔              | ✔                                                  | ⛔                                             |

1. Not all of the charts listed are a one-to-one match with the object created
   inside Qlik Sense. Specifically, these charts are not the same when rendered using
   Nebula.

> **Notes:**
>
> - Charts marked as `Experimental` are not yet supported by Qlik.
> - Support for the API and compatibility with nebula.js is outlined based
>   on the charts in the table. While customers can render any engine object
>   hypercube using their own frameworks, support for compatibility is based upon nebula.js.

## Chart conversion

Converting a visualization to a different registered type:

```js
const viz = await n.render({
  element: document.querySelector(".object"),
  type: "barchart",
  fields: ["title", "=avg(rating)"],
});
viz.convertTo("piechart");
```

You first render a bar chart, then pie chart is the registered type to convert to.
For more information about `convertTo`, see the [API reference](https://qlik.dev/apis/javascript/nebula-js/#definitions-viz-entries-convertto).

You can find an example using charts conversion in [the nebula.js repository on GitHub](https://github.com/qlik-oss/nebula.js/tree/master/examples/chart-conversion).
