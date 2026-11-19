---
source: https://qlik.dev/embed/qlik-embed/customize/qlik-embed-custom-dimensions-and-measures/
last_updated: 2026-07-08T14:18:07+02:00
---

# Create a chart on the fly with custom dimensions and measures

In [Create charts on the fly with analytics/chart](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-charts-on-the-fly-tutorial/),
you built a chart using field names and expression strings in the `dimensions` and `measures`
attributes.

That approach is suitable for simple charts:

```html
dimensions='["Region"]'
measures='["Sum(Sales)"]'
```

To define custom labels and other dimension or measure properties, pass complete `qDef` objects
as a single ordered array through the `dimensions` attribute.

Add dimension definitions first, followed by measure definitions. Do not pass complete measure
objects through the separate `measures` attribute.

In this tutorial, you'll render a bar chart with a custom dimension label and a custom
measure label.

## What you'll learn

- How to construct a field-based dimension using `qFieldDefs` and `qFieldLabels`.
- How to construct a measure using `qLabel` and the expression `qDef`.
- How to combine dimension and measure objects into the ordered array expected by
  `analytics/chart`.
- How to pass the array to `<qlik-embed>`.
- How to inspect an existing chart in Qlik Cloud and reuse its definitions.
- How to replace the field-based dimension with a calculated dimension.

## Prerequisites

- A Qlik Cloud tenant.
- A [SPA OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa/) configured for
  your web application. For a full walkthrough of authentication options, see the
  [qlik-embed auth overview](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/).
- The [app ID](https://qlik.dev/embed/foundational-knowledge/find-ids/) of a Qlik Sense app whose data model
  contains `Region` and `Sales` fields, or equivalent fields that you can substitute in the
  examples.
- Basic familiarity with HTML, JavaScript, and JSON.

> **Tip:** Replace values in angle brackets (`<PLACEHOLDER>`) with your own values. Field names such as
> `Region` and `Sales` are examples: substitute fields that exist in your app.

## Step 1: Set up the page

Add the qlik-embed script to the page's `<head>`. Replace the placeholder values with your
tenant URL, OAuth client ID, and callback URL.

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="<QLIK_TENANT_URL>"
  data-client-id="<QLIK_OAUTH2_CLIENT_ID>"
  data-redirect-uri="<QLIK_CALLBACK_URI>"
  data-access-token-storage="session"
></script>
```

For information about creating the OAuth client and callback page, see the
[qlik-embed authentication overview](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/).

Add a container and the `<qlik-embed>` component to the page body:

```html
<div class="chart-container">
  <qlik-embed
    id="chart"
    ui="analytics/chart"
    app-id="<QLIK_APP_ID>"
    type="barchart"
  ></qlik-embed>
</div>
```

Add CSS to give the chart a visible height:

```html
<style>
  .chart-container {
    width: 100%;
    height: 500px;
  }

  .chart-container qlik-embed {
    display: block;
    width: 100%;
    height: 100%;
  }
</style>
```

`barchart` is the
[Viz on the fly ID](https://qlik.dev/embed/foundational-knowledge/visualizations/) for a bar chart.

## Step 2: Construct the dimension definition

A field-based dimension groups chart data by the values of a field in the app's data model.

The following definition groups data by `Region` and displays the label `Sales region`:

```json
{
  "qDef": {
    "qFieldDefs": ["Region"],
    "qFieldLabels": ["Sales region"]
  }
}
```

The definition uses the following properties:

- `qFieldDefs` contains the fields or expressions used by the dimension.
- `qFieldLabels` contains labels corresponding to the entries in `qFieldDefs`.

Use a field name that exists in the selected app's data model. The Engine API schema defines
the object structure, not the fields available in a particular app.

For the complete property definitions, see:

- [NxDimension](https://qlik.dev/apis/json-rpc/qix/schemas/#nxdimension)
- [NxInlineDimensionDef](https://qlik.dev/apis/json-rpc/qix/schemas/#nxinlinedimensiondef)

## Step 3: Construct the measure definition

A measure calculates a value for each dimension group.

The following measure calculates total sales and displays the label `Total sales`:

```json
{
  "qDef": {
    "qLabel": "Total sales",
    "qDef": "Sum(Sales)"
  }
}
```

The measure uses the following properties:

- `qLabel` contains the display label.
- The inner `qDef` contains the Qlik expression to evaluate.

> **Note:** The name `qDef` appears at two nesting levels:
>
> - The outer `qDef` is an object containing the measure definition.
> - The inner `qDef` is the string containing the measure expression.
>
> In this example, `measure.qDef` is an object and `measure.qDef.qDef` is the
> `Sum(Sales)` expression.

For the complete property definitions, see:

- [NxMeasure](https://qlik.dev/apis/json-rpc/qix/schemas/#nxmeasure)
- [NxInlineMeasureDef](https://qlik.dev/apis/json-rpc/qix/schemas/#nxinlinemeasuredef)

## Step 4: Assemble the fields array

Place the dimension and measure definitions in one ordered array.

Add dimensions first, followed by measures:

```js
const fields = [
  {
    qDef: {
      qFieldDefs: ["Region"],
      qFieldLabels: ["Sales region"]
    }
  },
  {
    qDef: {
      qLabel: "Total sales",
      qDef: "Sum(Sales)"
    }
  }
];
```

Although the component attribute is named `dimensions`, the array can contain complete
dimension and measure definitions.

> **Warning:** Do not place a complete measure object in the separate `measures` attribute. The
> `analytics/chart` adapter treats entries in that attribute as expression strings.
>
> Use the `measures` attribute for simple expressions such as `measures='["Sum(Sales)"]'`.
>
> When using complete objects, add the measure objects after the dimension objects in the array
> passed through `dimensions`.
>
> Also avoid setting a `properties` attribute that defines its own `qHyperCubeDef` on the same
> element. It does not cleanly override the `dimensions` array: `properties.qHyperCubeDef.qDimensions`
> is prepended in front of whatever `dimensions` defines, so the chart renders both sets of
> dimensions concatenated into one hypercube instead of either one you designed.

## Step 5: Pass the array to qlik-embed

Serialize the mixed array with `JSON.stringify()` and assign it to the component's
`dimensions` attribute:

```html
<script>
  const fields = [
    {
      qDef: {
        qFieldDefs: ["Region"],
        qFieldLabels: ["Sales region"]
      }
    },
    {
      qDef: {
        qLabel: "Total sales",
        qDef: "Sum(Sales)"
      }
    }
  ];

  customElements.whenDefined("qlik-embed").then(() => {
    const chart = document.getElementById("chart");
    chart.setAttribute("dimensions", JSON.stringify(fields));
  });
</script>
```

There is no separate `measures` attribute in this example.

> **Other ways to pass the array:** In static HTML, you can serialize the mixed array directly in the `dimensions` attribute:
>
> ```html
> <qlik-embed
>   ui="analytics/chart"
>   app-id="<QLIK_APP_ID>"
>   type="barchart"
>   dimensions='[{"qDef":{"qFieldDefs":["Region"],"qFieldLabels":["Sales region"]}},{"qDef":{"qLabel":"Total sales","qDef":"Sum(Sales)"}}]'
> ></qlik-embed>
> ```
>
> When using the raw web component in a framework template, bind `JSON.stringify(fields)` to the
> `dimensions` attribute. For example, Vue uses:
>
> ```vue
> <qlik-embed
>   ui="analytics/chart"
>   :app-id="appId"
>   type="barchart"
>   :dimensions="JSON.stringify(fields)"
> ></qlik-embed>
> ```
>
> The `:dimensions` binding is Vue-specific syntax. It is not valid in plain HTML.

## Step 6: Check the result

Open the page in your browser. After authentication completes, the page renders a bar chart
that shows total sales for each region.

You should see:

- one bar for each value in the `Region` field
- **Sales region** as the dimension label
- **Total sales** as the measure label
- bar values calculated using `Sum(Sales)`

![Bar chart showing total sales by sales region](https://qlik.dev/_astro/qlik-embed-chart-custom-dimensions-measures.DD5DyFoU.png)

The custom labels confirm that qlik-embed used the complete dimension and measure definitions,
rather than only the underlying `Region` field and `Sum(Sales)` expression.

## Adapt the example

### Use a calculated dimension

The main example uses the `Region` field as a field-based dimension.

When the grouping value must be derived from an expression, replace the dimension definition at
the beginning of the `fields` array.

For example, the following definition groups sales by the month of `OrderDate`:

```json
{
  "qDef": {
    "qFieldDefs": ["=Month(OrderDate)"],
    "qFieldLabels": ["Order month"]
  }
}
```

The adapted array is:

```js
const fields = [
  {
    qDef: {
      qFieldDefs: ["=Month(OrderDate)"],
      qFieldLabels: ["Order month"]
    }
  },
  {
    qDef: {
      qLabel: "Total sales",
      qDef: "Sum(Sales)"
    }
  }
];
```

A calculated dimension expression belongs in `qFieldDefs`. A measure expression belongs in the
measure's inner `qDef`.

### Reuse definitions from an existing chart

If you already have a chart configured in Qlik Cloud, you can use its properties as a starting
point.

1. In a Qlik Sense app, create or open a chart and configure its dimensions, measures, and labels.
2. Add `/options/developer` to the end of the sheet URL. For the full workflow, see
   [Find the chart ID in developer mode](https://qlik.dev/embed/foundational-knowledge/find-ids/#find-the-chart-id-in-developer-mode).
3. Open the chart's ellipses menu and select **Developer**.
4. In the **Developer** dialog, expand **Properties**.
5. Locate `qHyperCubeDef.qDimensions` and `qHyperCubeDef.qMeasures`.
6. Copy the required dimension definitions into the beginning of your `fields` array.
7. Copy the required measure definitions after the dimensions.
8. Remove properties that are not needed by your embedded chart.

> **Warning:** The **Developer** dialog displays the chart's full `properties` object, with `qHyperCubeDef`
> nested inside it. Do not copy `qHyperCubeDef` as a whole into a `properties` attribute on the
> `<qlik-embed>` element. Extract only the individual entries from `qDimensions` and `qMeasures`
> into the `fields` array passed through `dimensions`, as shown in this tutorial.

The resulting array should follow this order:

```js
const fields = [
  dimensionDefinition,
  measureDefinition,
  additionalMeasureDefinition
];
```

## Troubleshooting

<details>
  <summary>
    The browser console reports that `startsWith` is not a function
  </summary>

  A complete measure object was probably passed through the separate `measures` attribute.

  This fails:

  ```html
  measures='[{"qDef":{"qLabel":"Total sales","qDef":"Sum(Sales)"}}]'
  ```

  Add the complete measure object to the mixed array passed through `dimensions` instead.
</details>

<details>
  <summary>
    The chart does not render
  </summary>

  Verify that:

  - the mixed array is serialized with `JSON.stringify()` before assigning it to the raw web
    component
  - the serialized `dimensions` value contains valid JSON
  - dimension objects appear before measure objects
  - the field names exist in the selected app
  - measure and calculated-dimension expressions use valid Qlik syntax
  - the app ID points to the app containing the fields
  - no `properties` attribute with its own `qHyperCubeDef` is set on the same element: this
    concatenates with `dimensions` and `measures` instead of replacing them, and the resulting
    extra dimension can make the chart render something unexpected instead of failing outright

  If a calculated dimension or measure expression is the suspected cause, isolate the problem by
  building the expression up in stages. For example, replace the expression with `="hello"`, confirm
  the chart renders, then try `=[FieldName]`, then add the full expression back one piece at a time
  until it breaks. This narrows down exactly where the syntax is invalid.
</details>

<details>
  <summary>
    Custom labels are not applied
  </summary>

  Verify that:

  - dimension properties are inside the dimension's `qDef`
  - the measure label and expression are inside the measure's `qDef`
  - the measure expression is assigned to the inner `qDef`
</details>

## Migrate from visualization.create()

The Capability API `columns` argument and the array used in this tutorial follow the same
general ordering: dimensions first, followed by measures.

For example, a `visualization.create()` call such as:

```js
app.visualization.create("barchart", [
  dimensionDefinition,
  measureDefinition
]);
```

maps to:

```js
const fields = [
  dimensionDefinition,
  measureDefinition
];

chart.setAttribute("dimensions", JSON.stringify(fields));
```

With qlik-embed, supply the app through `app-id` and the visualization type through `type`.
The component renders declaratively while it remains in the page. There is no direct equivalent
to the Capability API's `.show()` and `.close()` methods.

This is not necessarily a one-to-one migration. Review visualization-specific options.

## Next steps

- Review the
  [simpler charts-on-the-fly tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-charts-on-the-fly-tutorial/)
  to create charts using field-name and expression strings.
- Explore the
  [supported visualization types](https://qlik.dev/embed/foundational-knowledge/visualizations/).
- Explore the available [qlik-embed UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/).

## Full code

<details>
  <summary>
    Full HTML code for the chart
  </summary>

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Sales by region</title>

      <script
        crossorigin="anonymous"
        type="application/javascript"
        src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
        data-host="<QLIK_TENANT_URL>"
        data-client-id="<QLIK_OAUTH2_CLIENT_ID>"
        data-redirect-uri="<QLIK_CALLBACK_URI>"
        data-access-token-storage="session"
      ></script>

      <style>
        .chart-container {
          width: 100%;
          height: 500px;
        }

        .chart-container qlik-embed {
          display: block;
          width: 100%;
          height: 100%;
        }
      </style>
    </head>

    <body>
      <div class="chart-container">
        <qlik-embed
          id="chart"
          ui="analytics/chart"
          app-id="<QLIK_APP_ID>"
          type="barchart"
        ></qlik-embed>
      </div>

      <script>
        const fields = [
          {
            qDef: {
              qFieldDefs: ["Region"],
              qFieldLabels: ["Sales region"]
            }
          },
          {
            qDef: {
              qLabel: "Total sales",
              qDef: "Sum(Sales)"
            }
          }
        ];

        customElements.whenDefined("qlik-embed").then(() => {
          const chart = document.getElementById("chart");
          chart.setAttribute("dimensions", JSON.stringify(fields));
        });
      </script>
    </body>
  </html>
  ```
</details>
