---
source: https://qlik.dev/embed/capability-api/customize/styling-visualizations/reference-lines/
last_updated: 2025-07-03T16:05:11+02:00
---

# Reference lines

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

A reference line is a line intersecting the chart area from a given point on the
measure axis. You can use a reference line to indicate a certain level of chart
data. The reference line is only drawn if it falls within the current range of
the measure axis. You can have several reference lines in the same chart.
Reference lines are available in the following visualization types:

- Bar chart
- Box plot
- Distribution plot
- Gauge
- Histogram
- Line chart
- Scatter plot
- Waterfall chart

You can either set the reference line value to an absolute numeric value, or
enter an arbitrary numeric expression. For more information, see the following examples.

## The refLine object

Reference lines are defined in the `refLine` object. You can have several reference
lines defined for the same visualization.

### Example: Empty refLine object

```javascript
"refLine": {
    "refLines": []
  }
```

The properties of the reference line are set in an array (refLines) and can
consist of the following properties:

<details>
<summary>show</summary>

Set to `true` to display the reference line in the visualization.

Default: `false`
</details>

<details>
<summary>label</summary>

Reference line label as a string.

You can also set a label property inside the `refLineExpr` object and this
defines the label of the value. It follows the following syntax when displayed
in the visualization: `refLines.label` (`refLines.refLineExpr.label`).

<Image src={ontheflyexamplereferencelinelabels} alt="reference line labels" />

</details>

<details>
<summary>paletteColor</summary>

Defines the reference line color. It can either be as an index number from the
color palette (0-15) or it can be a HEX color code. If the `paletteColor` property
is not defined, the color defaults to black. If you are using the `color` property
to define a color that is not in the color palette, the index property should be
`"index": -1`.

paletteColor properties

| Name   | Type    | Description                                                  |
|------- |---------|--------------------------------------------------------------|
| index  |Integer  |Index in the palette.<br></br>The default Qlik Sense color palette:<br></br><ul><li>-1: set to use custom color that is not in the palette.</li><li>0: No color</li><li>1: White, HEX: `#ffffff`</li><li>2: Light green, HEX: `#46c646`</li><li>3: Green, HEX: `#276e27`</li><li>4: Light blue, HEX: `#b6d7ea`</li><li>5: Blue, HEX: `#7db8da`</li><li>6: Dark blue, HEX: `#4477aa`</li><li>7: Purple, HEX: `#8e477d`</li><li>8: Yellow, HEX: `#ffcf02`</li><li>9: Orange, HEX: `#f8981d`</li><li>10: Red, HEX: `#f93f17`</li><li>11: Brown, HEX: `#633d0c`</li><li>12: Light gray, HEX: `#b0afae`</li><li>13: Gray, HEX: `#7b7a78`</li><li>14: Dark gray, HEX: `#545352`</li><li>15: Black, HEX: `#000000`</li></ul><br></br>Default: 6|
|color|String|Color as HEX string.<br></br>Mandatory if `"index": "-1"`.|

</details>

<details>
<summary>refLineExpr</summary>

Defines the actual value of the reference line

refLineExpr properties

|Name|Type|Description|
|--------------------------|---------------------------|-------------------------|
|value|-|Can be an absolute numeric value or an arbitrary numeric expression <br></br> Example: Absolute numeric value <br></br> ```"refLineExpr": {``` <br></br> ```"value": 2``` <br></br>```}``` <br></br> Example: Arbitrary numeric expression <br></br> ```"refLineExpr": {``` <br></br>```"value": {``` <br></br>```qValueExpression": {``` <br></br> ```"qExpr": "=Count(distinct ID)/Count(distinct [Date.autoCalendar.YearMonth])"``` <br></br>```}```<br></br>```}```<br></br>```}```|
|label|String Expression Container|Defines the label of the value as a string or as an expression.<br></br>You can also set a label property inside the `refLines` object and this defines the label of the reference line. It follows the following syntax when displayed in the visualization: refLines.label `(refLines.refLineExpr.label)`.|

</details>

## Using an absolute numeric value

This example defines a reference line by an absolute numeric value. Set the
absolute numeric value of reference line:
`"refLineExpr": { "value": 2, "label":"2" }`. Then set `"show": true` to enable
the reference line. Define the color of the reference line:
`"paletteColor": { "index": 7, "color": "#8e477d" }`. Note how the label property
is empty.

```javascript
"refLine": {
  "refLines": [
    {
      "show": true,
      "label": "",
      "paletteColor": {
        "index": 7,
        "color": "#8e477d"
      },
      "refLineExpr": {
        "value": 2,
        "label": "2"
      }
    }
  ]
}
```

Result

![reference line
absolute numeric value](https://qlik.dev/_astro/on-the-fly-example-reference-line-absolute-numeric-value.BHH5jv3R.png)

## Using an arbitrary numeric expression

You can use an arbitrary numeric expression as a reference line. This means that
the value property includes a value expression instead of a number:
`"value": { "qValueExpression": { "qExpr": "=Count(distinct ID)/Count(distinct`
`[Date.autoCalendar.YearMonth])" } }`.

Note how the `label` property now has a value.

```javascript
"refLine": {
  "refLines": [
    {
      "show": true,
      "label": "Avg",
      "paletteColor": {
        "index": 7,
        "color": "#8e477d"
      },
      "refLineExpr": {
        "value": {
          "qValueExpression": {
            "qExpr": "=Count(distinct ID)/Count(distinct [Date.autoCalendar.YearMonth])"
          }
        },
        "label": {
          "qStringExpression": {
            "qExpr": "=Count(distinct ID)/Count(distinct [Date.autoCalendar.YearMonth])"
          }
        }
      }
    }
  ]
}
```

![reference line arbitrary numeric expression](https://qlik.dev/_astro/on-the-fly-example-reference-line-arbitrary-numeric-expression.Cfi0Bjra.png)

## Defining multiple reference lines

You can use multiple reference lines in your visualization. You can select to
keep them in the code but to hide them from being shown in the visualization
by setting "show": false, as demonstrated on the last reference line in the
following example.

```javascript
"refLine": {
  "refLines": [
    {
      "show": true,
      "label": "Pars this year",
      "paletteColor": {
        "index": -1,
        "color": "#91c26a"
      },
      "refLineExpr": {
        "value": {
          "qValueExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Pars'}>}NetScoreName)"
          }
        },
        "label": {
          "qStringExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Pars'}>}NetScoreName)"
          }
        }
      }
    },
    {
      "show": true,
      "label": "Birdies this year",
      "paletteColor": {
        "index": -1,
        "color": "#52a2cc"
      },
      "refLineExpr": {
        "value": {
          "qValueExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Birdies'}>}NetScoreName)"
          }
        },
        "label": {
          "qStringExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Birdies'}>}NetScoreName)"
          }
        }
      }
    },
    {
      "show": true,
      "label": "Boogies this year",
      "paletteColor": {
        "index": 9,
        "color": "#f8981d"
      },
      "refLineExpr": {
        "value": {
          "qValueExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Boogies'}>}NetScoreName)"
          }
        },
        "label": {
          "qStringExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'Boogies'}>}NetScoreName)"
          }
        }
      }
    },
    {
      "show": false,
      "label": "Double Boogies this year",
      "paletteColor": {
        "index": 9,
        "color": "#f8981d"
      },
      "refLineExpr": {
        "value": {
          "qValueExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'2 Boogies'}>}NetScoreName)"
          }
        },
        "label": {
          "qStringExpression": {
            "qExpr": "=Count({<[Date.autoCalendar.YearsAgo]={'0'},NetScoreName={'2 Boogies'}>}NetScoreName)"
          }
        }
      }
    }
  ]
}
```

Result

![reference line
multiple lines](https://qlik.dev/_astro/on-the-fly-example-reference-line-multiple-lines.C2YlRh8t.png)
