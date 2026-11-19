---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/gauge/
last_updated: 2025-08-04T14:23:38+02:00
---

# Gauge

The gauge is designed to show a single measure value and visualize how to
interpret that value.

The gauge is often used to present KPIs, for example, on an executive dashboard,
and together with segmenting and color coding, it is an effective way of
illustrating a performance result.

![Example of gauge object](https://qlik.dev/_astro/on-the-fly-example-gauge-04-golf-segment-color.P89-LAJF.png)

## Default settings for a gauge

The following settings are used by default in a gauge:

- A radial gauge
- A single (blue) color
- Range limits: min (0), max (100)
- No segments
- Label and title are displayed

## Number of columns (dimensions and measures)

In a gauge, you can only have one measure and no dimensions.

## Gauge types

Gauges can be displayed as a radial or as a bar. This is defined by the
`gaugetype` property.

```js
"gaugetype": "radial"; // default
```

![Example of radial gauge
object](https://qlik.dev/_astro/on-the-fly-example-gauge-04-golf-segment-color.P89-LAJF.png)

```js
"gaugetype": "bar";
```

![Example of vertical bar gauge
object](https://qlik.dev/_astro/on-the-fly-example-gauge-03-vertical-bar.CI6Dz5-6.png)

## Measure axis

### Range limits

The default range limits are in most cases not usable:
chances are your measure value is outside of the default limits,
as indicated by an arrow at the max end or the min end.

```js
"measureAxis": {
    "min": 0,
    "max": 100,
}, // default
```

![Radial gauge with default range limits](https://qlik.dev/_astro/on-the-fly-example-gauge-range-limits-default.By2WA8E2.png)

You should specify the range limits using relevant values or expressions
to support the interpretation of the value.

```js
"measureAxis": {
    "min": 0,
    "max": {
        "qValueExpression": {
            "qExpr": "Sum ([Sales Amount])*1.1",
        },
    },
},
```

![Radial gauge with customized limits](https://qlik.dev/_astro/on-the-fly-example-gauge-range-limits-customized.2K4S2tFw.png)

### Labels and title

By default, both labels and tile of the measure axis are shown.

```js
"measureAxis": {
    "show": "all", // default
},
```

![Radial gauge with labels and title shown](https://qlik.dev/_astro/on-the-fly-example-gauge-axis-labels-title-shown.CVZIyKMR.png)

But you can show only labels (`"labels"`), only title (`"title"`),
or none of them (`"none"`).

```js
"measureAxis": {
    "show": "none",
},
```

![Radial gauge with labels and title hidden](https://qlik.dev/_astro/on-the-fly-example-gauge-axis-labels-title-hide.CfYawQYn.png)

### Spacing

The distance between ticks can be configured with
the `"spacing"` properties, with `1` being medium (default),
`0.5` being narrow and `2` being wide.

```js
"measureAxis": {
    "spacing": 1, // default
},
```

![Radial gauge with medium axis spacing](https://qlik.dev/_astro/on-the-fly-example-gauge-axis-medium.BXapcu7b.png)

```js
"measureAxis": {
    "spacing": 0.5, // narrow
},
```

![Radial gauge with narrow axis spacing](https://qlik.dev/_astro/on-the-fly-example-gauge-axis-narrow.BByINYYl.png)

## Bar gauge orientation

If `autoOrientation` is true, the bar is oriented along the longer side of the chart.

```js
"autoOrientation": true; // default
```

![Bar gauge with auto orientation](https://qlik.dev/_astro/on-the-fly-example-gauge-orientation-auto.BauozuGQ.png)

If `autoOrientation` is false, the orientation is dictated by the `orientation` property.

```js
"autoOrientation": false;
"orientation": "vertical",
```

![Bar gauge with vertical orientation](https://qlik.dev/_astro/on-the-fly-example-gauge-orientation-vertical.Db5D4SZf.png)

## Coloring

There are several options to color a gauge, depending on your needs.

### Progress

The simplest way to color a gauge is to only color the progress,
that is the part of the gauge representing the value of interest.

By default, the master measure's color is used.
For it to work, you need to specify the ID of the master measure
you want to get the color from.

```js
"useSegments": false, // default
"color": { "useBaseColors": "measure" }, // default
"qHyperCubeDef": {
    "qMeasures": [{ "qLibraryId": "id-of-the-qMeasureInfo-in-your-app" }],
    "qInitialDataFetch": [{ "qWidth": 1, "qHeight": 1 }],
},
```

![Radial gauge with progress color from library](https://qlik.dev/_astro/on-the-fly-example-gauge-color-progress-library.BYS24gYR.png)

Progress color can also be specified explicitly in `"paletteProgressColor"`

```js
"useSegments": false, // default
"color": { "useBaseColors": "off" },
"paletteProgressColor": { "color": "#aa347a" },
```

![Radial gauge with explicit progress color](https://qlik.dev/_astro/on-the-fly-example-gauge-color-progress-explicit.DySo71RM.png)

### Segments

A gauge can also be colored with multiple segments,
enabling visualizing additional information.

Similar to progress color, segments colors can be taken from a master measure,
or can be specified explicitly. The first option is to use the segments from
a master measure. The master measure has been configured (not shown here) with
segments colors with red at the lowest 50% range, and green at the
highest 50% range, and with gradient (that is gradual changing color).

```js
"useSegments": true,
"color": { "useBaseColors": "measure" }, // default
"qHyperCubeDef": {
  "qMeasures": [{ "qLibraryId": "id-of-the-qMeasureInfo-in-your-app" }],
  "qInitialDataFetch": [{ "qWidth": 1, "qHeight": 1 }],
},
```

![Radial gauge with segments color from library](https://qlik.dev/_astro/on-the-fly-example-gauge-color-segments-library.B98SprLJ.png)

Segments colors can also be specified explicitly in `"segmentInfo"`.
Note: in the example below, expressions are used for the limits,
but limits can simply be numbers (for example `"value": 100`).

```js
"useSegments": true,
"color": { "useBaseColors": "off" },
"segmentInfo": {
    "limits": [
        { "value": { "qValueExpression": { "qExpr": "Sum ([Sales Amount])*0.8" } }, "gradient": false },
        { "value": { "qValueExpression": { "qExpr": "Sum ([Sales Amount])*1.2" } }, "gradient": false },
    ],
    "paletteColors": [{ "color": "#ff3834" }, { "color": "yellow" }, { "color": "#20aa1a" }],
},
```

![Radial gauge with explicit segments colors](https://qlik.dev/_astro/on-the-fly-example-gauge-color-segments-explicit.BS-pChHI.png)

## Reference lines

Reference lines, configured in the `refLine` property,
provide additional information to
help interpret the gauge value.

Below is an example of having two reference lines
to help put the gauge value in context.

```js
"refLine": {
    "refLines": [
        {
            "show": true, // default
            "label": "Last year sales",
            "showLabel": true, // default
            "refLineExpr": { "value": 91000000, "label": "91000000" },
            "showValue": true, // default
            "paletteColor": { "color": "#cc3c5b" },
            "style": { "lineThickness": 2, "lineType": "8 4" },
        },
        {
            "label": "Expectation",
            "refLineExpr": { "value": 101000000, "label": "101000000" },
            "paletteColor": { "color": "#49bd2b" },
            "style": { "lineThickness": 2, "lineType": "8 4" },
        },
    ],
},
```

![Bar gauge with reference lines](https://qlik.dev/_astro/on-the-fly-example-gauge-ref-lines.D-K9v0rx.png)
