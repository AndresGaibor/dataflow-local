---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/distributionplot/
last_updated: 2025-08-04T14:23:38+02:00
---

# Distribution plot

The distribution plot is suitable for comparing range and distribution for groups
of numerical data. Data is plotted as value points along an axis. You can choose
to display only the value points to see the distribution of values, a bounding
box to see the range of values, or a combination of both.

![Example of distribution plot](https://qlik.dev/_astro/on-the-fly-example-distributionplot-01-general.Bh4G5PKD.png)

## Number of columns (dimensions and measures)

In a distribution plot, you need to use one or two dimensions and one measure.
If you use a single dimension, you will receive a single line visualization, as
in the previous image. If you use two dimensions, you will get one line for each
value of the second, or outer, dimension, as in the example below.

```json
[
  {
    "qDef": {
      "qFieldDefs": [
        "=NetScoreName"
      ],
      "qFieldLabels": [
        "Net result"
      ]
    },
    "qNullSuppression": true
  },
  {
    "qDef": {
      "qFieldDefs": [
        "Date.autoCalendar.Year"
      ],
      "qFieldLabels": [
        "Year"
      ]
    },
    "qNullSuppression": true
  },
  {
    "qDef": {
      "qLabel": "Occurancies",
      "qDef": "Count(HoID)",
      "qNumFormat": {
        "qType": "F",
        "qnDec": 2,
        "qUseThou": 0
      }
    }
  }
]
```

![Example of distribution plot with multiple dimensions and measures](https://qlik.dev/_astro/on-the-fly-example-distributionplot-04-outer-dimension.OCQcSjap.png)

## Default settings for a distribution plot

Most native Qlik Sense chart types are automatically sorted on the dimension content:

- Numeric content is numerically sorted.
- Categorical content is alphabetically sorted.
