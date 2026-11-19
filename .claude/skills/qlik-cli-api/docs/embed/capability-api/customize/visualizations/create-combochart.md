---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-combochart/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating combo charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create combo charts with the Visualization API.

## Creating a basic combo chart

In this example, you want to create a basic combo chart, containing one dimension
and two measures, and with a custom title. The chart applies custom sorting.

1. Create the chart.

   Create the container for the chart. The visualization type is `combochart`.

   ```javascript
   app.visualization.create(
     'combochart',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column. In this example, you will use a calculated
   dimension that does not include null values: `"qNullSuppression": true`.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "=If(Par<>3,TClubName)"
         ],
         "qFieldLabels": [
           "Tee club"
         ]
       },
       "qNullSuppression": true
     }
   ]
   ```

3. Define measures.

   Define the measures as columns. The first measure is to be presented as a bar
   on the primary axis: `"series": { "type": "bar","axis": 0}`. The second measure
   is to be presented as a line on the primary axis:
   `"series": { "type": "line", "axis": 0}`.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "=If(Par<>3,TClubName)"
         ],
         "qFieldLabels": [
           "Tee club"
         ]
       },
       "qNullSuppression": true
     },
     {
       "qDef": {
         "qLabel": "Avg",
         "qDef": "Avg(DrDist)",
         "series": {
           "type": "bar",
           "axis": 0
         }
       }
     },
     {
       "qDef": {
         "qLabel": "Max",
         "qDef": "Max(DrDist)",
         "series": {
           "type": "line",
           "axis": 0
         }
       }
     }
   ]
   ```

4. Define sorting for the dimension.

   You want to sort the dimension values based on an expression:
   `"qSortCriterias": [ { "qSortByExpression": -1`,
   `"qExpression": { "qv": "Max(DrDist)" } } ]`,  `"autoSort": false`.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
          "=If(Par<>3,TClubName)"
         ],
         "qFieldLabels": [
          "Tee club"
         ],
         "qSortCriterias": [
           {
             "qSortByExpression": -1,
             "qExpression": {
               "qv": "Max(DrDist)"
             }
           }
         ],
         "autoSort": false
       },
       "qNullSuppression": true
     },
     {
       "qDef": {
         "qLabel": "Avg",
         "qDef": "Avg(DrDist)",
         "series": {
           "type": "bar",
           "axis": 0
         }
       }
     },
     {
       "qDef": {
         "qLabel": "Max",
         "qDef": "Max(DrDist)",
         "series": {
           "type": "line",
           "axis": 0
          }
        }
      }
    ]
   ```

5. Define the title in the options.

   ```json
   {
     "showTitles": true,
     "title": "Off the tee"
   ```

Result

![Combo chart example](https://qlik.dev/_astro/on-the-fly-example-combochart-01-general.DVHRB5Ln.png)

### Complete code example: Sample combo chart

<details>

<summary>Visualization API</summary>

```javascript
const config = {
  host: '<TENANT_URL>', //for example, 'abc.us.example.com'
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};

require.config({
  baseUrl: `https://${config.host}/resources`,
  webIntegrationId: config.webIntegrationId
});

require(["js/qlik"], (qlik) => {
  qlik.on('error', (error) => console.error(error));
  const app = qlik.openApp('<APP_ID>', config);
  app.visualization.create(
    'combochart',
    [
      {
        "qDef": {
          "qFieldDefs": [
            "=If(Par<>3,TClubName)"
          ],
          "qFieldLabels": [
            "Tee club"
          ],
          "qSortCriterias": [
            {
              "qSortByExpression": -1,
              "qExpression": {
                "qv": "Max(DrDist)"
              }
            }
          ],
          "autoSort": false
        },
        "qNullSuppression": true
      },
      {
        "qDef": {
          "qLabel": "Avg",
          "qDef": "Avg(DrDist)",
          "series": {
            "type": "bar",
            "axis": 0
          }
        }
      },
      {
        "qDef": {
          "qLabel": "Max",
          "qDef": "Max(DrDist)",
          "series": {
            "type": "line",
            "axis": 0
          }
        }
      }
    ],
    {
      "showTitles": true,
      "title": "Off the tee"
    }
  ).then((vis)=>{
    vis.show("QV01");
  });
});
```

</details>

## Presentation and color settings

In this example, you want to change the way the combo chart is presented by adding
data points and changing the color used.

1. Show data points.
   Start by showing data points, which is defined in the options.

   ```json
   {
     {/*Show data points*/}
     "dataPoint": {
       "show": true
     }
   }
   ```

2. Define color settings.

   In this example, you want to define a single color to be used. The colors
   used are set in the color object. Disable automatic colors ("auto": false)
   and set that a single color will be used: `"mode": "primary"`. Then define the
   color in the `paletteColor` object:
   `"paletteColor": { "index": -1, "color": "#3a7391" }`.

   > **Note:** Color legends are automatically turned off when single color mode is used.

```json
{
  {/*Show data points*/}
  "dataPoint": {
    "show": true
  },
  {/*Single color: "#3a7391"*/}
  "color": {
    "auto": false,
    "mode": "primary",
    "paletteColor": {
      "index": -1,
      "color": "#3a7391"
    }
  }
}
```

Result

![Combo chart example with color modification](https://qlik.dev/_astro/on-the-fly-example-combochart-02-colors.BWgQ6oPR.png)

### Complete code example: Presentation and color settings

<details>

<summary>Visualization APZ</summary>

```javascript
const config = {
  host: '<TENANT_URL>', //for example, 'abc.us.example.com'
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};

require.config({
  baseUrl: `https://${config.host}/resources`,
  webIntegrationId: config.webIntegrationId
});
require(["js/qlik"], (qlik) => {
  qlik.on('error', (error) => console.error(error));
  const app = qlik.openApp('<APP_ID>', config);
  app.visualization.create(
    'combochart',
    [
      {
        "qDef": {
          "qFieldDefs": [
            "=If(Par<>3,TClubName)"
          ],
          "qFieldLabels": [
            "Tee club"
          ],
          "qSortCriterias": [
            {
              "qSortByExpression": -1,
              "qExpression": {
                "qv": "Max(DrDist)"
              }
            }
          ],
          "autoSort": false
        },
        "qNullSuppression": true
      },
      {
        "qDef": {
          "qLabel": "Avg",
          "qDef": "Avg(DrDist)",
          "series": {
            "type": "bar",
            "axis": 0
          }
        }
      },
      {
        "qDef": {
          "qLabel": "Max",
          "qDef": "Max(DrDist)",
          "series": {
            "type": "line",
            "axis": 0
          }
        }
      }
    ],
    {
      "showTitles": true,
      "title": "Off the tee",
      /*Show data points*/
      "dataPoint": {
        "show": true
      },
      /*Single color: "#3a7391"*/
      "color": {
        "auto": false,
        "mode": "primary",
        "paletteColor": {
          "index": -1,
          "color": "#3a7391"
        }
      }
    }
  ).then((vis)=>{
    vis.show("QV01");
  });
});
```

</details>

## Dimension and measure axis settings

In this example, you want to do some changes to how the dimension axis and the
measure axes are presented.

1. Dimension axis
   Dimension axis settings are set in the dimensionAxis object. This example
   displays labels only on the dimension axis.

   Set to display labels only on the dimension axis: `show: labels`.

   ```json
   /*Dimension axis: show labels only*/
   "dimensionAxis": {
     "show": "labels"
   }
   ```

2. Measure axis.

   Measure axis settings are set in the `measureAxes` object. This example
   uses narrow spacing and display labels only on the measure axis.

   Set to display labels only on the measure axis: `show: labels`. Then set
   narrow scaling: `spacing: 0.5`.

   The `measureAxes` object contain two measure axes: one for the primary and one
   for the secondary axis. Since both measures are displayed on the primary
   axis, changes done to the first axis apply for both measures.

   ```json
   /*Dimension axis: show labels only*/
   "dimensionAxis": {
     "show": "labels"
   },
   /*Measure axis: show labels only, narrow scale*/
   "measureAxes": [
     {
       "show": "labels",
       "dock": "near",
       "spacing": 0.5,
       "autoMinMax": true
     },
     {
     }
   ]
   ```

Result

![Combo chart example with dimension and measure modifiers](https://qlik.dev/_astro/on-the-fly-example-combochart-03-axis.mFJNVY-P.png)

### Complete code example: Dimension and measure axis settings

<details>

<summary>Visualization API</summary>

```javascript
const config = {
  host: '<TENANT_URL>', //for example, 'abc.us.example.com'
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};

require.config({
  baseUrl: `https://${config.host}/resources`,
  webIntegrationId: config.webIntegrationId
});
require(["js/qlik"], (qlik) => {
  qlik.on('error', (error) => console.error(error));
  const app = qlik.openApp('<APP_ID>', config);
  app.visualization.create(
    'combochart',
    [
      {
        "qDef": {
          "qFieldDefs": [
            "=If(Par<>3,TClubName)"
          ],
          "qFieldLabels": [
            "Tee club"
          ],
          "qSortCriterias": [
            {
              "qSortByExpression": -1,
              "qExpression": {
                "qv": "Max(DrDist)"
              }
            }
          ],
          "autoSort": false
        },
        "qNullSuppression": true
      },
      {
        "qDef": {
          "qLabel": "Avg",
          "qDef": "Avg(DrDist)",
          "series": {
            "type": "bar",
            "axis": 0
          }
        }
      },
      {
        "qDef": {
          "qLabel": "Max",
          "qDef": "Max(DrDist)",
          "series": {
            "type": "line",
            "axis": 0
          }
        }
      }
    ],
    {
      "showTitles": true,
      "title": "Off the tee",
      "dataPoint": {
        "show": true
      },
      "color": {
        "auto": false,
        "mode": "primary",
        "paletteColor": {
          "index": -1,
          "color": "#3a7391"
        }
      },
      "dimensionAxis": {
        "continuousAuto": true,
        "show": "labels"
      },
      "measureAxes": [
        {
          "show": "labels",
          "dock": "near",
          "spacing": 0.5,
          "autoMinMax": true
        },
        {
          "show": "all",
          "dock": "far"
        }
      ]
    }
  ).then((vis)=>{
    vis.show("QV01");
  });
});
```

</details>

## Stacked bars, line on secondary axis and dimension limits

In this example, you will create a combo chart containing one dimension and
three measures, where the first two measures are displayed as stacked bars on
the primary axis and the third measure is displayed as a line on the secondary axis.

1. Define the dimension and dimension limit.

   Define the dimension as a column. This example uses the same dimension as in the
   previous examples but with some alterations.

   Now you want to display only the top five results based on the first measure.
   So you set `qOtherMode: OTHER_COUNTED` and then define
   `qOtherCounted: {"qv": "5"}`. You do not want to show an others value, so set
   `qSuppressOther: true`.

   > **Note:** If `qSuppressOther` is not defined, the last value in the
   > visualization (colored gray) summarizes all the remaining values and the
   > value counts as 1 in that setting. In this example, the third value would be `Others`.
   > Since you want to show the top (highest) five values, set
   > `qOtherSortMode: OTHER_SORT_DESCENDING` to sort the values in descending order.

   ```json
   "qOtherTotalSpec": {
           "qOtherMode": "OTHER_COUNTED",
           "qOtherCounted": {
           "qv": "5"
           },
        "qSuppressOther": true,
        "qOtherSortMode": "OTHER_SORT_DESCENDING"
      }
   ```

2. Define the first measure.

   Define the measures as columns.

   The first measure is displayed as a bar on the primary axis:
   `"series": { "type": "bar", "axis": 0 }`. Note the custom numeric formatting
   defined in `qNumFormat`.

   ```json
   {
     "qDef": {
       "qLabel": "Typical",
       "qDef": "Median(DrDist)",
       "qNumFormat": {
          "qType": "F",
          "qFmt": "#,##0 m"
       },
       "numFormatFromTemplate": false,
       "series": {
         "type": "bar",
         "axis": 0
       }
     }
   }
   ```

3. Define the second measure.

   The second measure is also displayed as a bar on primary axis:
   `"series": { "type": "bar", "axis": 0 }`. Note the custom numeric formatting
   defined in `qNumFormat`.\`

   ```json
   {
     "qDef": {
       "qLabel": "Max",
       "qDef": "Max(DrDist)-Median(DrDist)",
       "qNumFormat": {
         "qType": "F",
         "qFmt": "+#,##0"
       },
       "numFormatFromTemplate": false,
       "series": {
         "type": "bar",
         "axis": 0
       }
     }
   }
   ```

4. Define the third measure.

   The third measure is displayed as a line on the secondary axis:
   `"series": { "type": "line", "axis": 1 }`. Note the custom numeric formatting
   defined in `qNumFormat`.

   ```json
   {
     "qDef": {
       "qLabel": "FIR%",
       "qDef": "Avg(FwHit)",
       "qNumFormat": {
         "qType": "F",
         "qFmt": "0.0%"
       },
       "numFormatFromTemplate": true,
       "series": {
         "type": "line",
         "axis": 1
       }
     }
   }
   ```

5. Define some general settings.

   Group the first two measures as stacked bars:
   `"barGrouping": { "grouping": "stacked" }`.

   Add a title to the visualization: `"title": "Off the tee - top 5 clubs"`. Then
   you want to show data points on the line: `"dataPoint": { "show": true }`.

   The dimension axis should show labels only:
   `"dimensionAxis": { "show": "labels", "dock": "near" }`.

6. Define the measure axes.

   The measureAxes object contain two measure axes: one for the primary and one
   for the secondary axis. Since this example display measures on both the
   primary and secondary axis, changes done to the first axis apply for the
   first and second measure, and changes done to the second axis apply for the
   third measure.

   Set to display labels only on the both measure axes: `"show": "labels"`.
   Then set narrow spacing: `"spacing": 0.5` for the primary axis and medium
   spacing: `"spacing": 1` for the secondary axis. On the secondary axis, set
   a custom range where you define both the minimum value and the maximum value:
   `"autoMinMax": false`, `"minMax": "minMax"`, `"min": 0.2, "max": 1`.

   ```json
   "measureAxes": [
     {
       "show": "labels",
       "dock": "near",
       "spacing": 0.5,
       "autoMinMax": true
     },
     {
       "show": "labels",
       "dock": "far",
       "spacing": 1,
       "autoMinMax": false,
       "minMax": "minMax",
       "min": 0.2,
       "max": 1
     }
   ]
   ```

Result

![Combo chart example with stacked bars](https://qlik.dev/_astro/on-the-fly-example-combochart-04-three-measures-dimlimits.Bv_9nCVH.png)

### Complete code example: Stacked bars, line on secondary axis and dimension limits

<details>

<summary>Visualization API</summary>

    ```javascript
    const config = {
      host: '<TENANT_URL>', //for example, 'abc.us.example.com'
      prefix: '/',
      port: 443,
      isSecure: true,
      webIntegrationId: '<WEB_INTEGRATION_ID>'
    };

    require.config({
      baseUrl: `https://${config.host}/resources`,
      webIntegrationId: config.webIntegrationId
    });
    require(["js/qlik"], (qlik) => {
      qlik.on('error', (error) => console.error(error));
      const app = qlik.openApp('<APP_ID>', config);
      app.visualization.create(
        'combochart',
        [
          {
            "qDef": {
              "qFieldDefs": [
                "=If(Par<>3,TClubName)"
              ],
              "qFieldLabels": [
                "Tee club"
              ],
              "qSortCriterias": [
                {
                  "qSortByExpression": -1,
                  "qExpression": {
                    "qv": "Max(DrDist)"
                  }
                }
              ],
              "autoSort": false
            },
            "qNullSuppression": true,
            "qOtherTotalSpec": {
              "qOtherMode": "OTHER_COUNTED",
              "qOtherCounted": {
                "qv": "5"
              },
              "qSuppressOther": true,
              "qOtherSortMode": "OTHER_SORT_DESCENDING"
            }
          },
          {
            "qDef": {
              "qLabel": "Typical",
              "qDef": "Median(DrDist)",
              "qNumFormat": {
                "qType": "F",
                "qFmt": "#,##0 m"
              },
              "numFormatFromTemplate": false,
              "series": {
                "type": "bar",
                "axis": 0
              }
            }
          },
          {
            "qDef": {
              "qLabel": "Max",
              "qDef": "Max(DrDist)-Median(DrDist)",
              "qNumFormat": {
                "qType": "F",
                "qFmt": "+#,##0"
              },
              "numFormatFromTemplate": false,
              "series": {
                "type": "bar",
                "axis": 0
              }
            }
          },
          {
            "qDef": {
              "qLabel": "FIR%",
              "qDef": "Avg(FwHit)",
              "qNumFormat": {
                "qType": "F",
                "qFmt": "0.0%"
              },
              "numFormatFromTemplate": true,
              "series": {
                "type": "line",
                "axis": 1
              }
            }
          }
        ],
        {
          "showTitles": true,
          "title": "Off the tee - top 5 clubs",
          "barGrouping": {
            "grouping": "stacked"
          },
          "dataPoint": {
            "show": true
          },
          "color": {
            "auto": true
          },
          "legend": {
            "show": false
          },
          "dimensionAxis": {
            "show": "labels",
            "dock": "near"
          },
          "measureAxes": [
            {
              "show": "labels",
              "dock": "near",
              "spacing": 0.5,
              "autoMinMax": true
            },
            {
              "show": "labels",
              "dock": "far",
              "spacing": 1,
              "autoMinMax": false,
              "minMax": "minMax",
              "min": 0.2,
              "max": 1
            }
         ]
        }
      ).then((vis)=>{
        vis.show("QV01");
      });
    });
    ```

  </details>
