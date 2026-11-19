---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-linechart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating line charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create line charts with the Visualization API.

## Create a basic line chart

In this example, you will create a basic line chart, containing one dimension
and one measure, with a custom title.

1. Create the chart.

   Create the container for the chart. The visualization type is `linechart`.

   ```javascript
   app.visualization.create(
     'linechart',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column. Note the Dual function used in the
   dimension definition:
   `"qFieldDefs": [ "=Dual([Date.autoCalendar.Date],ID)" ]`.
   It is used to separate values that belong to separate ranges (ID) but has the
   same date `([Date.autoCalendar.Date])`.

   For more information about the Dual function, see [Dual - script and chart function](https://help.qlik.com/en-US/sense/August2022/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Dual.htm)
   on Qlik Help.

   ```json
   [
     {
       "qDef": {
         "qGrouping": "N",
         "qFieldDefs": [
           "=Dual([Date.autoCalendar.Date],ID)"
         ],
         "qFieldLabels": [
           "Date"
         ]
       },
       "qNullSuppression": true
     }
   ]
   ```

3. Define the measure.

   Define the measure as a column.

   ```json
   [
     {
       "qDef": {
         "qGrouping": "N",
         "qFieldDefs": [
           "=Dual([Date.autoCalendar.Date],ID)"
         ],
         "qFieldLabels": [
           "Date"
         ]
       },
       "qNullSuppression": true
     },
     {
       "qDef": {
         "qLabel": "Pts",
         "qGrouping": "N",
         "qDef": "Avg(Stableford)",
         "qNumFormat": {
           "qType": "U",
           "qnDec": 10,
           "qUseThou": 0
         }
       }
     }
   ]
   ```

4. Define the title.

   Define the title in the options.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point trend"
   }
   ```

Result

![Example of line chart](https://qlik.dev/_astro/on-the-fly-example-linechart-01-general.Ce3qI-Rn.png)

### Complete code example: Basic line chart

- <details>
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
          'linechart',
          [
            {
              "qDef": {
                "qGrouping": "N",
                "qFieldDefs": [
                  "=Dual([Date.autoCalendar.Date],ID)"
                ],
                "qFieldLabels": [
                  "Date"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "Pts",
                "qGrouping": "N",
                "qDef": "Avg(Stableford)",
                "qNumFormat": {
                  "qType": "U",
                  "qnDec": 10,
                  "qUseThou": 0
                }
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Stableford point trend"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Number formatting and presentation

In this example, the number formatting has changed, show data points is enabled,
grid line spacing is narrow, and missing values are shown as connections.

1. Change number formatting

   You will change the number formatting of the measure to show two decimals.
   Set `"qType": "F"` to indicate that a fixed number of decimals is used. Then
   set `"qnDec": 2` to indicate that two decimals is used.

```json
{
   "qDef": {
     "qLabel": "Pts",
     "qGrouping": "N",
     "qDef": "Avg(Stableford)",
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

1. Show data points

   In the options, enable data points:
   `"dataPoint": { "show": true, "showLabels": false }`. Value labels are not
   shown on the data points in this example.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point trend",
     "dataPoint": {
       "show": true,
       "showLabels": false
     }
   }
   ```

2. Narrow grid line spacing

   Next, set grid line spacing to narrow:
   `"gridLine": { "auto": false, "spacing": 3 }`, where 3 means narrow.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point trend",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     }
   }
   ```

3. Connect missing values

   Finally, define that missing values should be shown as connections:
   `"nullMode": "connect"`.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point trend",
     "nullMode": "connect",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     }
   }
   ```

Result

![Example of line chart with modified number
formats and presentation settings](https://qlik.dev/_astro/on-the-fly-example-linechart-02-numberformat-datapoints.CRN_8ruB.png)

### Complete code example: Number formatting and presentation

- <details>
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
          'linechart',
          [
            {
              "qDef": {
                "qGrouping": "N",
                "qFieldDefs": [
                  "=Dual([Date.autoCalendar.Date],ID)"
                ],
                "qFieldLabels": [
                  "Date"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "Pts",
                "qGrouping": "N",
                "qDef": "Avg(Stableford)",
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
            "title": "Stableford point trend",
            "nullMode": "connect",
            "dataPoint": {
              "show": true,
              "showLabels": false
            },
            "gridLine": {
              "auto": false,
              "spacing": 3
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Area chart with two measures and numerous settings

In this example, you will display the chart as an area chart. You will also add a
second measure and some presentation settings are defined.

1. Add a second measure.

   Define the second measure as a column.

   ```json
   {
     "qDef": {
       "qLabel": "Putts",
       "qGrouping": "N",
       "qDef": "Avg(Putts)",
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

2. Define area chart.
   In this example, you want to present the chart as an area chart. This is
   defined in the options: `"lineType": "area"`.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point and putt average relation",
     "lineType": "area",
     "nullMode": "connect",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     }
   }
   ```

3. Define the scroll alignment.

   Define the scroll alignment to be at the end: `"scrollStartPos": 1`.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point and putt average relation",
     "lineType": "area",
     "scrollStartPos": 1,
     "nullMode": "connect",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     }
   }

   ```

4. Define the dimension axis.

   Axis settings are set in the `dimensionAxis` and `measureAxis` objects.
   On the dimension axis, set to display labels only that are tilted:
   `"dimensionAxis": {"continuousAuto": true, "show": "labels", "label": "tilted"}`.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point and putt average relation",
     "lineType": "area",
     "scrollStartPos": 1,
     "nullMode": "connect",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     },
     "dimensionAxis": {
       "continuousAuto": true,
       "show": "labels",
       "label": "tilted"
     }
   }
   ```

5. Define the measure axis.

   On the measure axis, also set to display labels only and then set the measure
   axis scale to
   `narrow: "measureAxis": { "show": "labels", "dock": "near", "spacing": 0.5 }`.

   ```json
   {
     "showTitles": true,
     "title": "Stableford point and putt average relation",
     "lineType": "area",
     "scrollStartPos": 1,
     "nullMode": "connect",
     "dataPoint": {
       "show": true,
       "showLabels": false
     },
     "gridLine": {
       "auto": false,
       "spacing": 3
     },
     "dimensionAxis": {
       "continuousAuto": true,
       "show": "labels",
       "label": "tilted"
     },
     "measureAxis": {
       "show": "labels",
       "dock": "near",
       "spacing": 0.5
     } 
   }
   ```

Result

![Area chart example with multiple overlapping
measures and presentations](https://qlik.dev/_astro/on-the-fly-example-linechart-03-area-two-measures.s6j_TcsP.png)

### Complete code example: Area chart with two measures and numerous settings

- <details>
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
          'linechart',
          [
            {
              "qDef": {
                "qGrouping": "N",
                "qFieldDefs": [
                  "=Dual([Date.autoCalendar.Date],ID)"
                ],
                "qFieldLabels": [
                  "Date"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "Pts",
                "qGrouping": "N",
                "qDef": "Avg(Stableford)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0.00",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            },
            {
              "qDef": {
                "qLabel": "Putts",
                "qGrouping": "N",
                "qDef": "Avg(Putts)",
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
            "title": "Stableford point and putt average relation",
            "lineType": "area",
            "scrollStartPos": 1,
            "nullMode": "connect",
            "dataPoint": {
              "show": true,
              "showLabels": false
            },
            "gridLine": {
              "auto": false,
              "spacing": 3
            },
            "dimensionAxis": {
              "continuousAuto": true,
              "show": "labels",
              "label": "tilted"
            },
            "measureAxis": {
              "show": "labels",
              "dock": "near",
              "spacing": 0.5
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Creating a time-aware line chart

In this example, you will create a time-aware line chart, containing one
dimension and one measure.

1. Define the dimension.

   Define the dimension as a column.

   ```json
   {
     "qDef": {
       "qGrouping": "N",
       "qFieldDefs": [
         "Date.autoCalendar.Date"
       ],
       "qFieldLabels": [
         "Date"
       ]
     }
   }
   ```

2. Define the measure.

   Define the measure as a column.

   ```json
   {
     "qDef": {
       "qGrouping": "N",
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
       "autoSort": true
     }
   }
   ```

3. Set the title.

   Define a title in the options: `"title": "Strokes gained putting"`.

   ```json
   {
     "showTitles": true,
     "title": "Strokes gained putting"
   }

   ```

4. Set labels on the dimension axis.

   You want to show labels only on the dimension axis. You will also set
   `"continuousAuto": false` to indicate that you want to customize the scaling
   of the dimensional axis. This is then done by setting
   `"preferContinuousAxis": true`, which means that the scale along the
   dimensional axis is continuous if supported by the data.

   ```json
   {
     "showTitles": true,
     "title": "Strokes gained putting",
     "dimensionAxis": {
       "continuousAuto": false,
       "show": "labels"
     },
     "preferContinuousAxis": true
   }
   ```

5. Set labels on the measure axis.

   You want to show labels only on the measure axis:
   `"measureAxis": { "show": "labels" }`.

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

Example of time-aware line chart

![Example of time-aware line chart](https://qlik.dev/_astro/on-the-fly-example-linechart-04-time-aware-chart.CJuMw8jB.png)

### Complete code example: Time-aware line chart

- <details>
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
          'linechart',
          [
            {
              "qDef": {
                "qGrouping": "N",
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
                "autoSort": true
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
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
