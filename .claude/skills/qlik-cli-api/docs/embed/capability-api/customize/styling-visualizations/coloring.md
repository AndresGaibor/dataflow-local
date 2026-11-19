---
source: https://qlik.dev/embed/capability-api/customize/styling-visualizations/coloring/
last_updated: 2025-10-31T14:06:52+01:00
---

# Add color to your visualizations

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Qlik Sense automatically colors visualizations as they are added to your web pages.
You can manually set the colors in your visualizations to meet your requirements
or preferences.

## Overview

Not all Qlik Sense visualizations support the same coloring options.
Additionally, some visualization types have specific behaviors or limitations
when using certain coloring methods. Color methods supported by visualizations
and their limitations are determined primarily by the kinds of data the
visualizations displays. For example, visualizations that only support displaying
measures cannot be colored by dimension or through using master dimensions.

The following table outlines color method support by visualization type.

Supported color methods

| Visualization type | Single color        | Multicolor             | By dimension           | By measure           | By expression           |   |
| ------------------ | ------------------- | ---------------------- | ---------------------- | -------------------- | ----------------------- | - |
| Mode               | `"mode": "primary"` | `"mode": "byMultiple"` | `"mode":"byDimension"` | `"mode":"byMeasure"` | `"mode":"byExpression"` |   |
| Bar chart          | ✔                   | ✔                      | ✔                      | ✔                    | ✔                       |   |
| Box plot           | ✔                   | -                      | -                      | -                    | -                       |   |
| Combo chart        | ✔                   | ✔                      | ✔                      | ✔                    | ✔                       | ✔ |
| Distribution plot  | ✔                   | -                      | -                      | -                    | -                       |   |
| Gauge              | ✔                   | -                      | -                      | -                    | -                       |   |
| Histogram          | ✔                   | -                      | -                      | -                    | -                       |   |
| KPI                | ✔                   | ✔                      | -                      | -                    | -                       |   |
| Line chart         | ✔                   | ✔                      | ✔                      | ✔                    | ✔                       | ✔ |
| List box           | -                   | -                      | -                      | -                    | -                       |   |
| Pie chart          | ✔                   | ✔                      | ✔                      | ✔                    | ✔                       | ✔ |
| Pivot table        | -                   | -                      | -                      | -                    | ✔                       |   |
| Scatter plot       | ✔                   | -                      | ✔                      | ✔                    | ✔                       |   |
| Table              | -                   | -                      | -                      | -                    | ✔                       |   |
| Treemap            | ✔                   | ✔                      | ✔                      | ✔                    | ✔                       | ✔ |
| Waterfall chart    | ✔                   | -                      | -                      | -                    | -                       |   |

### Coloring limitations and behaviors

Different visualizations have different behaviors with the methods of setting
color in visualizations. This section outlines specific considerations when
coloring different visualizations.

#### Line charts

Line charts do not support coloring by measure if they have two or more dimensions.

## The color object

Most color options for visualizations are set in the color `object` in the options.
You activate custom coloring by setting `"auto": false` which turns off auto-coloring.

If `"auto": true`, no other properties need to be defined in the `color` object.

The following parameters can be set in the color object:

<details>
<summary>auto (boolean)</summary>

When `"auto": true`, color settings are based on the visualization used and the
number of dimensions and measures, that is, the settings are not fixed, but are
dependent on the data input.
</details>

<details>
<summary>mode (string)</summary>

The mode property sets the coloring mode for the visualization when auto-coloring
has been switched off (`"auto": false`). Can be one of:

- `primary`: a single color (by default blue) is used for all items in the chart.
In visualizations that do not benefit from multiple colors (bar charts with one
dimension and scatter plots), single color is the default setting.

- `byDimension`: coloring is based upon the amount of dimension values.
Details are set in the byDimensionDef property.

  <Aside type="note">
    `byDimension` can only be used in conjunction with an attribute dimension
    on the dimension to color by, as shown in the following example.
  </Aside>

```json
{
  "qDef": {
    "qFieldDefs": [
      "NetScoreName"
    ]
  },
  "qAttributeDimensions": [
    {
      "qDef": "NetScoreName",
      "id": "colorByAlternative",
      "label": "Year"
    }
  ]
}
```

- `byExpression`: coloring is based on an expression, which in most cases is a
color code. Details are set in the expressionIsColor, expressionLabel
and colorExpression properties.

- `byMeasure`: coloring is based on the measure value. Details are set in
the byMeasureDef property.

- `byMultiple`: can be used when more than one measure is used. By default,
12 colors are used for the dimensions. The colors are reused when there are
more than 12 dimension values.

</details>

<details>
<summary>useBaseColors(string)</summary>

Only applicable when `"mode": "primary"` or `"mode": "byMultiple"` has been defined.

Use colors encoded in master items. Should only be defined when a master
dimension or master measure used in the visualization has a color assigned to it.

One of:

- `off`
- `measure`: use colors encoded in master measure.
- `dimension`: use colors encoded in master dimension.

Default: off

</details>

<details>
<summary>paletteColor(object)</summary>

The `paletteColor` object is used to define the color when you color by single
color (`"mode": "primary"`). It has the following properties:

paletteColor properties

| Name  | Type    | Description                                                 |
|-------|---------|-------------------------------------------------------------|
| index | Integer | Index in the palette. The default Qlik Sense color palette: |
|       |         | -1: set to use custom color that is not in the palette.     |
|       |         | 0: No color                                                 |
|       |         | 1: White, HEX: `#ffffff`                                    |
|       |         | 2: Light green, HEX: `#46c646`                              |
|       |         | 3: Green, HEX: `#276e27`                                    |
|       |         | 4: Light blue, HEX: `#b6d7ea`                               |
|       |         | 5: Blue, HEX: `#7db8da`                                     |
|       |         | 6: Dark blue, HEX: `#4477aa`                                |
|       |         | 7: Purple, HEX: `#8e477d`                                   |
|       |         | 8: Yellow, HEX: `#ffcf02`                                   |
|       |         | 9: Orange, HEX: `#f8981d`                                   |
|       |         | 10: Red, HEX: `#f93f17`                                     |
|       |         | 11: Brown, HEX: `#633d0c`                                   |
|       |         | 12: Light gray, HEX: `#b0afae`                              |
|       |         | 13: Gray, HEX: `#7b7a78`                                    |
|       |         | 14: Dark gray, HEX: `#545352`                               |
|       |         | 15: Black, HEX: `#000000`                                   |
|       |         |                                                             |
|       |         | Default: 6                                                  |
| Color | String  | Color as HEX string.                                        |
|       |         | Mandatory if `"index": "-1"`.                                 |

</details>

<details>
<summary>persistent (boolean)</summary>

Set to true to use persistent colors on data points between selection states.
Only applicable when using one dimension and when `"mode": "byDimension"` or
when `"mode": "byMultiple"`.

Default: `false`
</details>

<details>
<summary>expressionColor (boolean)</summary>

Set to true to define whether the result of the expression is a valid CSS3 color.

Only applicable when `"mode": "byExpression"`.

Default: `true`
</details>

<details>
<summary>expressionLabel (string)</summary>

Defines the label on tool tips when using a coloring expression. Only applicable
when `"mode": "byExpression"` and only used if `"expressionIsColor": false`.
</details>

<details>
<summary>colorExpression (ValueExpressionContainer)</summary>

Sets the color expression to be used when `"mode": "byExpression"` is defined.

Supported formats:

- RGB
- ARGB
- HSL

</details>

<details>
<summary>measureScheme (string)</summary>

Color scheme when `"mode": "byMeasure"`. Can be one of:

- `sg`: (sequential gradient) the transition between the different color groups
is made using different shades of colors. High measure values have darker hues

- `sc`: (sequential classes) the transition between the different color groups
is made using distinctly different colors.

- `dg`: (diverging gradient) used when working with data that is ordered from
low to high, for instance, to show the relationship between different areas on
a map. Low and high values have dark colors, mid-range colors are light.

- `dc`: (diverging classes) can be seen as two sequential classes combined, with
the mid-range shared. The two extremes, high and low, are emphasized with dark
colors with contrasting hues, and the mid-range critical values are emphasized
with light colors.

Default: `sg`

</details>

<details>
<summary>useMeasureGradient (boolean)</summary>

Set to true if you want to apply the colors defined for library measures when
used. Only applicable if `"mode": "byMeasure"`.

Default: `true`

</details>

<details>
<summary>dimensionScheme (string)</summary>

Color scheme when `"mode": "byDimension"` or `"mode": "byMultiple"`. Can be one of:

- `12`: 12 colors where all can be distinguished by people with vision deficiency.

- `100`: 100 colors where not all can be distinguished by people with vision deficiency

Default: `12`

</details>

<details>
<summary>useDimColVal (boolean)</summary>

Set to true if you want to apply the colors defined for library dimensions when
used. Only applicable if `"mode": "byDimension"`.

Default: `true`

</details>

<details>
<summary>reverseScheme (boolean)</summary>

Set to true to reverse the color scheme.

</details>

<details>
<summary>autoMinMax (boolean)</summary>

Set to false to define custom color range. Custom color range is only
applicable when coloring is by measure (`"mode": "byMeasure"`) or by expression
(`"mode": "byExpression"`).

When coloring is by expression, `"expressionIsColor": "false"` must be set for
a custom color range to work.

Default: `true`

</details>

<details>
<summary>measureMin (ValueExpressionContainer)</summary>

Set the min value for the color range.

Only applicable if `autoMinMax: false`. Can be used in conjunction with `measureMax`
or on its own.

</details>

<details>
<summary>measureMax (ValueExpressionContainer)</summary>

Set the max value for the color range.

Only applicable if `autoMinMax: false`. Can be used in conjunction with `measureMin`
or on its own.

</details>

<details>
<summary>byDimensionDef (object)</summary>

byDimensionDef properties

|Name|Type|Description|
|-------------------------|----------------------------|-------------------------|
|label|String|Dimension label.|
|key|String|Field or expression that defines the dimension.|
|type|String|-|

</details>

<details>
<summary>byMeasureDef (object)</summary>

byMeasureDef properties

|Name|Type|Description|
|-------------------------|----------------------------|-------------------------|
|label|String|Measure label.|
|key|String|Field or expression that defines the measure.|
|type|String|-|

</details>

## Color by single color

When you color by single color, one color is used for all objects in the chart.
Coloring by a single color is best used for visualizations, such as bar or line
charts, with a single dimension and measure.

You color by single color by setting `"mode": "primary"`. You then define the color
in the paletteColor object, see paletteColor (object).

### Example: Single custom color

```json
"color": {
  "auto": false,
  "mode": "primary",
  "useBaseColors": "off",
  "paletteColor": {
    "index": -1,
    "color": "#61a729"
  }
}
```

![coloring by single color](https://qlik.dev/_astro/on-the-fly-example-coloring-by-single-color.B8VYbYmR.png)

## Color by multiple colors

When you have multiple measures in a visualization, you can set
`"mode": "byMultiple"` to color each measure with a different color. Qlik Sense
offers a 12-color and a 100-color palette to apply to the visualization in the
`dimensionScheme` property.

- `12`: 12 colors where all can be distinguished by people with vision deficiency.

- `100`: 100 colors where not all can be distinguished by people with vision deficiency

By default, 12 colors is selected as the color scheme dimensions.

### Example: Color by multiple colors

```json

"color": {
  "auto": false,
  "mode": "byMultiple",
  "dimensionScheme": "100"
}
```

![coloring by multiple
colors](https://qlik.dev/_astro/on-the-fly-example-coloring-by-multiple-colors.B8QBEI9i.png)

## Color by dimension

When you color a visualization by a dimension, all values in the visualization
are colored by the corresponding values in the dimension field selected. You
set `"mode": "byDimension"` to color by dimension. You define the dimension to
color by in the `byDimDef` object. Qlik Sense offers a 12-color and a
100-color palette to apply to the visualization in the `dimensionScheme` property.

- `12`: 12 colors where all can be distinguished by people with vision deficiency.

- `100`: 100 colors where not all can be distinguished by people with vision deficiency

By default, 12 colors is selected as the color scheme dimensions.

You can set `"persistent": true` which means that colors persist between
selection states. If `"persistent": false`, colors will be changed and reassigned
for different dimension values as selections are made in the visualization.

`byDimension` can only be used in conjunction with an attribute on the dimension
to color by, as shown in the example below.

### Example: Color by dimension

Columns: color by alternative added as "qAttributeDimensions" on the dimension
to color by

```json
{
  "qDef": {
    "qFieldDefs": [
      "FirResult"
    ],
    "qFieldLabels": [
      "Driving accuracy"
    ]
  },
  "qNullSuppression": true,
  "qAttributeDimensions": [
    {
      "qDef": "FirResult",
      "id": "colorByAlternative"
    }
  ]
}
```

Options: color object

```json
"color": {
  "auto": false,
  "mode": "byDimension",
  "persistent": true,
  "dimensionScheme": "12",
  "byDimDef": {
    "label": "Driving accuracy",
    "key": "FirResult",
    "type": "expression"
  }
}
```

![coloring by dimension](https://qlik.dev/_astro/on-the-fly-example-coloring-by-dimension.BHAl8qM_.png)

## Color by measure

When you color a visualization by a measure, all values in the visualization
are colored by a gradient or class based on the values in the selected measure.
Coloring by measure is useful when you want to clearly see objects colored by
their corresponding measure value.

You set `"mode": "byMeasure"` to color by measure. You then have four available
color schemes that you define in the `measureScheme` property.

- `sg`: (sequential gradient) the transition between the different color groups is
  made using different shades of colors. High measure values have darker hues.

- `sc`: (sequential classes) the transition between the different color groups is
  made using distinctly different colors.

- `dg`: (diverging gradient) used when working with data that is ordered from low
  to high, for instance, to show the relationship between different areas on a map.
  Low and high values have dark colors, mid-range colors are light.

- `dc`: (diverging classes) can be seen as two sequential classes combined, with
  the mid-range shared. The two extremes, high and low, are emphasized with dark
  colors with contrasting hues, and the mid-range critical values are emphasized
  with light colors.

You can reverse the color scheme by setting `"reverseScheme": true` which
switches which colors are used for low values and which colors are used for
high values in the selected color scheme.

You can define a custom measure value range by setting `"autoMinMax": false`. You
then define `measureMin` and/or `measureMax` depending on how you want to set the
range.

Measure range properties

| Name       | Type                       | Description                                                                                                                                                                                                                                                                                                 |
| ---------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| autoMinMax | Boolean                    | Set to false to define custom color range. Custom color range is only applicable when coloring is by measure (`"mode": "byMeasure"`) or by expression (`"mode": "byExpression"`).  When coloring is by expression,`"expressionIsColor": "false"` must be set for custom color range to work.Default: `true` |
| measureMin | Value Expression Container | Set the min value for the color range.Only applicable if `autoMinMax: false`. Can be used in conjunction with `measureMax` or by its own.                                                                                                                                                                   |
| measureMax | Value Expression Container | Set the max value for the color range. Only applicable if `autoMinMax: false`. Can be used in conjunction with `measureMin` or by its own.                                                                                                                                                                  |

### Example: Color by measure

```json
"color": {
  "auto": false,
  "mode": "byMeasure",
  "measureScheme": "dc",
  "reverseScheme": true,
  "autoMinMax": true,
  "byMeasureDef": {
    "label": "Pts",
    "key": "Avg(Stableford)",
    "type": "expression"
  },
  "altLabel": "Pts"
}
```

![coloring by measure](https://qlik.dev/_astro/on-the-fly-example-coloring-by-measure.Og3YFSBl.png)

## Color by expression

Coloring by expression applies colors to a visualization based on a user-defined
expression. This enables you to use expressions to define both the colors used
and the values upon which the colors are applied in a visualization. You could,
for example, use an expression to set conditional colors in a chart.

Supported formats for color expressions are: RGB, ARGB, and HSL.

You set `"mode": "byExpression"` to color by expression. Details are then defined
in the `expressionIsColor`, `expressionLabel`, and `colorExpression` properties.

`byExpression` can only be used in conjunction with an attribute expression on the
first measure, as shown in the example below.

### Example: Color by expression

Columns: color expression added as "qAttributeExpressions" on first measure

```json
{
  "qDef": {
    "qLabel": "Frequency",
    "qDef": "Count(NetScoreName)"
  },
  "qAttributeExpressions": [
    {
      "qExpression": "If(NetScoreDiff<0,RGB(82, 162, 204),\nIf(NetScoreDiff>0,RGB(248, 152, 29),RGB(145, 194, 106)))",
      "id": "colorByExpression"
    }
  ]
}
```

Options: color object

```json
"color": {
  "auto": false,
  "mode": "byExpression",
  "expressionIsColor": true,
  "expressionLabel": "",
  "colorExpression": "If(NetScoreDiff<0,RGB(82, 162, 204),\nIf(NetScoreDiff>0,RGB(248, 152, 29),RGB(145, 194, 106)))"
}
```

![coloring by expression](https://qlik.dev/_astro/on-the-fly-example-coloring-by-expression.C4p-DEY1.png)

## Color by expression in tables and pivot tables

Expressions can be used to color table and pivot table backgrounds and text.
This enables you to use expressions to define both the colors used and the
conditional values upon which the colors are applied in a visualization. You
could, for example, use expressions to change text and background colors
depending on the values within different table cells.

### Cell background color in straight tables

Cell background color is applied as an attribute expression on the applicable
column measure with `"id": "cellBackgroundColor"`.

```json
"qAttributeExpressions": [
  {
    "qExpression": "If(Avg(FwHit)>0.7,RGB(145, 194, 106))",
    "id": "cellBackgroundColor"
  }
]
```

### Text color in straight tables

Text color is applied as an attribute expression on the applicable column
measure with `"id": "cellForegroundColor"`.

```json
"qAttributeExpressions": [
  {
    "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115))",
    "id": "cellForegroundColor"
  }
]
```

### Using both background color and text color in a straight table column

When defining both background color and text color for a measure, you include two
definitions in the attribute expression.

```json
"qAttributeExpressions": [
  {
    "qExpression": "If(Avg(FwHit)>0.7,RGB(145, 194, 106))",
    "id": "cellBackgroundColor"
  },
  {
    "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115))",
    "id": "cellForegroundColor"
  }
]
```

![cell text coloring
straight table](https://qlik.dev/_astro/on-the-fly-example-coloring-cell-text-straight-table.C16HBTnj.png)

### Cell background color and text color in pivot tables

The `qAttributeExpressions` property behaves differently in pivot tables compared
to in straight tables. For pivot tables, it consists of two arrays, where the
first array is for defining the background color and the second array is for
defining the text color. There is therefore no need to define `"id": "cellBackgroundColor"`
or `"id": "cellForeroundColor"` for pivot tables.

```json
"qAttributeExpressions": [
  {
    "qExpression": "If(Avg(FwHit)>0.667, RGB(145, 194, 106))"
  },
  {
    "qExpression": "If(Avg(FwHit)<0.5, RGB(255, 115, 115))"
  }
]
```

![cell background color
pivot table](https://qlik.dev/_astro/on-the-fly-example-coloring-cell-text-pivot-table.DmcCM4t0.png)
