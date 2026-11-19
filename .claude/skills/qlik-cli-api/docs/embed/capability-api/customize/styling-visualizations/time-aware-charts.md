---
source: https://qlik.dev/embed/capability-api/customize/styling-visualizations/time-aware-charts/
last_updated: 2025-07-03T16:05:11+02:00
---

# Time-aware charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Time-aware charts are visualizations that use a continuous scale to provide a
complete and accurate view of time-based data. That is, when you enable
continuous scaling on the x-axis in a chart with date fields, data points are
separated from each other by a distance relative to their associated time.
As well, the axis labels are evenly separated whether or not there is data for
that point and the chart view is compressed to avoid scrolling.

A continuous scale is most commonly used with date fields such as:

- Second
- Minute
- Hour
- Week
- Month
- YearMonth
- Quarter
- YearQuarter
- Year
- Date
- Timestamp

## Time-aware bar charts

Create a time-aware bar chart, containing one dimension and one measure.
The visualization type is `barchart`.

Define the dimension and the measure as columns. Note the number formatting
applied to the measure.

```javascript
{
  "qDef": {
    "qFieldDefs": [
      "Date.autoCalendar.Date"
    ],
    "qFieldLabels": [
      "Date"
    ]
  }
},
{
  "qDef": {
    "qLabel": "Strokes gained putting",
    "qDef": "Sum(ExpPutts-Putts)",
    "qNumFormat": {
      "qType": "F",
      "qnDec": 2,
      "qUseThou": 0,
      "qFmt": "#,##0.00",
      "qDec": ".",
      "qThou": ","
    }
  }
}
```

Define a title in the options: `"title": "Strokes gained putting"`. In the
`dimensionAxis` object, set `"continuousAuto": false`. Then set
`"preferContinuousAxis": true`.

```javascript
{
  "showTitles": true,
  "title": "Strokes gained putting",
  "dimensionAxis": {
    "continuousAuto": false,
    "show": "labels"
  },
  "preferContinuousAxis": true,
  "measureAxis": {
    "show": "labels"
  }
}
```

Result

![time aware bar chart](https://qlik.dev/_astro/on-the-fly-example-barchart-08-time-aware.BUbeCTee.png)

Code examples

<details>
<summary>Visualization API</summary>

```javascript
app.visualization.create(
  'barchart',
  [
    {
      "qDef": {
        "qFieldDefs": [
          "Date.autoCalendar.Date"
        ],
        "qFieldLabels": [
          "Date"
        ]
      }
    },
    {
      "qDef": {
        "qLabel": "Strokes gained putting",
        "qDef": "Sum(ExpPutts-Putts)",
        "qNumFormat": {
          "qType": "F",
          "qnDec": 2,
          "qUseThou": 0,
          "qFmt": "#,##0.00",
          "qDec": ".",
          "qThou": ","
        }
      }
    }
  ],
  {
    "showTitles": true,
    "title": "Strokes gained putting",
    "dimensionAxis": {
      "continuousAuto": false,
      "show": "labels"
    },
    "preferContinuousAxis": true,
    "measureAxis": {
      "show": "labels"
    }
  }
).then(function(vis){
  vis.show("QV01");
});
```

</details>

## Time-aware combo charts

Create a time-aware combo chart, containing one dimension and one measure.
The visualization type is `combochart`.

Define the dimension and the measure as columns. This example
displays the measure as a marker on the primary axis:
`"series": { "type":"marker", "axis": 0,`.
The marker type is a filled square: `"marker": "rect", "markerFill": true }`.

Also note the number formatting applied to the measure.

```json
{
  "qDef": {
    "qFieldDefs": [
      "Date.autoCalendar.Date"
    ],
    "qFieldLabels": [
      "Date"
    ]
  }
},
{
  "qDef": {
    "qLabel": "Strokes gained putting",
    "qDef": "Sum(ExpPutts-Putts)",
    "qNumFormat": {
      "qType": "F",
      "qnDec": 2,
      "qUseThou": 0,
      "qFmt": "#,##0.00",
      "qDec": ".",
      "qThou": ","
    },
    "series": {
      "type": "marker",
      "axis": 0,
      "marker": "rect",
      "markerFill": true
    }
  }
}
```

Define a title in the options: `"title": "Strokes gained putting"`. In the
`dimensionAxis` object, set `"continuousAuto": false`. Then set
`"preferContinuousAxis": true`.

```json
{
  "showTitles": true,
  "title": "Strokes gained putting",
  "dimensionAxis": {
    "continuousAuto": false,
    "show": "labels"
  },
  "preferContinuousAxis": true,
  "measureAxis": {
    "show": "labels"
  }
}
```

Result

![time aware combo chart](https://qlik.dev/_astro/on-the-fly-example-combochart-05-time-aware.CfUyMG0n.png)

Code examples

<details>
<summary>Visualization API</summary>

```javascript
app.visualization.create(
  'combochart',
  [
    {
      "qDef": {
        "qFieldDefs": [
          "Date.autoCalendar.Date"
        ],
        "qFieldLabels": [
          "Date"
        ]
      }
    },
    {
      "qDef": {
        "qLabel": "Strokes gained putting",
        "qDef": "Sum(ExpPutts-Putts)",
        "qNumFormat": {
          "qType": "F",
          "qnDec": 2,
          "qUseThou": 0,
          "qFmt": "#,##0.00",
          "qDec": ".",
          "qThou": ","
        },
        "series": {
          "type": "marker",
          "axis": 0,
          "marker": "rect",
          "markerFill": true
        }
      }
    }
  ],
  {
    "showTitles": true,
    "title": "Strokes gained putting",
    "dimensionAxis": {
      "continuousAuto": false,
      "show": "labels"
    },
    "preferContinuousAxis": true,
    "measureAxes": [
      {
        "show": "labels"
      },
      {
        "show": "all"
      }
    ]
  }
).then(function(vis){
  vis.show("QV01");
});
```

</details>

## Time-aware line charts

Create a time-aware line chart, containing one dimension and one measure. The
visualization type is `linechart`.

Define the dimension and the measure as columns. Note the number formatting
applied to the measure.

```json
{
  "qDef": {
    "qFieldDefs": [
      "Date.autoCalendar.Date"
    ],
    "qFieldLabels": [
      "Date"
    ]
  }
},
{
  "qDef": {
    "qLabel": "Strokes gained putting",
    "qDef": "Sum(ExpPutts-Putts)",
    "qNumFormat": {
      "qType": "F",
      "qnDec": 2,
      "qUseThou": 0,
      "qFmt": "#,##0.00",
      "qDec": ".",
      "qThou": ","
    }
  }
}
```

Define a title in the options: `"title": "Strokes gained putting"`. In the
`dimensionAxis` object, set `"continuousAuto": false`. Then set
`"preferContinuousAxis": true`.

Result

![time aware line
chart](https://qlik.dev/_astro/on-the-fly-example-linechart-04-time-aware-chart.CJuMw8jB.png)

Code examples

<details>
<summary>Visualization API</summary>

```javascript
app.visualization.create(
  'linechart',
  [
    {
      "qDef": {
        "qFieldDefs": [
          "Date.autoCalendar.Date"
        ],
        "qFieldLabels": [
          "Date"
        ]
      }
    },
    {
      "qDef": {
        "qLabel": "Strokes gained putting",
        "qDef": "Sum(ExpPutts-Putts)",
        "qNumFormat": {
          "qType": "F",
          "qnDec": 2,
          "qUseThou": 0,
          "qFmt": "#,##0.00",
          "qDec": ".",
          "qThou": ","
        }
      }
    }
  ],
  {
    "showTitles": true,
    "title": "Strokes gained putting",
    "dimensionAxis": {
      "continuousAuto": false,
      "show": "labels"
    },
    "preferContinuousAxis": true,
    "measureAxis": {
      "show": "labels"
    }
  }
).then(function(vis){
  vis.show("QV01");
});
```

</details>
