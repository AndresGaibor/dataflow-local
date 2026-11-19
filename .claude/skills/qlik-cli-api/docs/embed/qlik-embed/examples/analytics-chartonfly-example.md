---
source: https://qlik.dev/embed/qlik-embed/examples/analytics-chartonfly-example/
last_updated: 2026-07-08T14:18:07+02:00
---

# analytics/chart on the fly

The `analytics/chart` UI for qlik-embed accepts additional properties to
create a chart on the fly. This is a visualization that doesn't
exist in the source Qlik Sense app, and is instead generated for the current
session when you supply the chart type, dimensions, and measures.

For a step-by-step tutorial that includes interactive controls to change the
chart type, dimension, and measure at runtime, see
[Create charts on the fly with analytics/chart](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-charts-on-the-fly-tutorial/).

> **Note:** Supports visualizations that work with the `analytics/chart` UI only.
> Review [the visualization support table](https://qlik.dev/embed/foundational-knowledge/visualizations/) for compatibility information.

Here's an example of a chart on the fly definition using qlik-embed web components.

> **Tip:** When defining arrays or objects in HTML attributes, use either single quotes around the
> attribute and standard double quotes inside, or encode double quotes as `&amp;quot;` for valid
> static HTML. This example uses single quotes for readability.

```html
<qlik-embed
  ui="analytics/chart"
  app-id="<appid>"
  type="barchart"
  dimensions='["[CategoryName]", "[Product Name]"]'
  measures='["=Sum(Sales)", "=Sum([Cost of Goods Sold])", "=Sum([GrossMargin])"]'
  properties='{orientation: "horizontal"}'
  state-name="name_of_the_state"
  theme="breeze"
></qlik-embed>
```

To create a chart on the fly, supply values for these properties:

- `app-id`: A unique identifier for a Qlik Analytics application.
- `type`: The Viz on the fly ID for the visualization type to render. See the
  [visualization support table](https://qlik.dev/embed/foundational-knowledge/visualizations/)
  for all available IDs and their `analytics/chart` compatibility.

Depending on chart type, add:

- `dimensions`: A JSON array of field names or master dimension titles, each
  wrapped in square brackets for Qlik script compatibility:
  `'["[FieldName]", "[Another Field]"]'`.
- `measures`: A JSON array of expressions, each prefixed with `=`:
  `'["=Sum(Sales)", "=Avg(Sales)"]'`. Master measures cannot be referenced by
  name—write the expression inline instead.

For a custom dimension or measure label, a calculated
dimension, `dimensions` and `measures` can also take full property objects instead
of plain strings. For more information, see
[Create a chart on the fly with custom dimensions and measures](https://qlik.dev/embed/qlik-embed/customize/qlik-embed-custom-dimensions-and-measures/).

You can also add additional properties:

- `state-name`: A string for the name of the alternate state to apply to the chart (must
  exist in the app).
- `properties`: An object setting specific properties to control the presentation
  of the rendered object.

Want to explore more qlik-embed? Explore all [qlik-embed UIs and params](https://qlik.dev/embed/qlik-embed/parameters/).
