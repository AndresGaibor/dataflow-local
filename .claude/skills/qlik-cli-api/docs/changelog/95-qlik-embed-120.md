---
source: https://qlik.dev/changelog/95-qlik-embed-120/
last_updated: 2024-08-01T13:17:48+01:00
---

# qlik-embed adds charts on the fly and new context naming

## charts on the fly

qlik-embed 1.2.0 adds the popular charts on the fly feature to the `analytics/chart`
ui. This allows you to generate charts from data in a Qlik Sense app, without
the chart existing in the app. You pass a definition, and the chart is created as
requested by your web app.

Here's an example using qlik-embed web components:

```html
<qlik-embed
  id="visualization"
  ui="analytics/chart"
  app-id="<appid>"
  type="barchart"
  dimensions='["Dimension1"]'
  measures='["Measure1", "=Sum(Expression2)", "=Avg(Expression2)"]'
  properties='{ orientation: "horizontal", barGrouping: { grouping: "stacked" } }'
></qlik-embed>
```

> Note: charts on the fly works only with charts available in the `analytics/chart`
> ui in qlik-embed. Please consult the
> [chart compatibility table](https://qlik.dev/embed/foundational-knowledge/visualizations/#chart-types-and-properties)
> for a list of compatible charts. Use the *Viz on the fly ID* for the type property.

## Update for using context property

Previously an html attribute to the `<qlik-embed />` tag could include `:json` or `:number`
to indicate which type the string in the attribute should be parsed to. In some environments
the `:` is not allowed as a html parameter so it is now possible to also use `___`
(triple underscore) as a delimiter.

This means you can now set context like this:
`<qlik-embed context___json='{ theme: "Breeze" }' ... />` and it will be parsed as json.
