---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-pivottable/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating pivot tables

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create pivot tables with the Visualization API.

## Creating a basic pivot table

In this example, you will create a basic pivot table, containing two dimensions
(Year and Quarter) and three measures. The measures have basic number formatting
applied and a title is added to the pivot table.

1. Create the chart.

   Create the container for the chart. The visualization type is pivot-table.

   ```js
   app.visualization.create(
     'pivot-table',
     [],
     {}
   )
   ```

2. Define the first dimension.

   Define the dimension Year as a column. Note that the dimension does not
   include null values: `"qNullSuppression": true`.

   ```json
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
   }
   ```

3. Define the second dimension.

   Define the dimension `Quarter` as a column. Note that the dimension does not
   include null values: `"qNullSuppression": true`.

   ```json
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
       "qFieldDefs": [
         "Date.autoCalendar.Quarter"
       ],
       "qFieldLabels": [
         "Quarter"
       ]
     },
     "qNullSuppression": true
   }
   ```

4. Define the first measure.

   Define the measure as a column and label it `FIR%`. Apply custom number
   formatting since the measure should be displayed in percent.

   ```json
   {
     "qDef": {
       "qLabel": "FIR%",
       "qDef": "Avg(FwHit)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     }
   }
   ```

5. Define the second measure.

   Define the measure as a column and label it `GIR%`. Apply custom number
   formatting since the measure should be displayed in percent.

   ```json
   {
     "qDef": {
       "qLabel": "FIR%",
       "qDef": "Avg(FwHit)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     }
   },
   {
     "qDef": {
       "qLabel": "GIR%",
       "qDef": "Avg(GIR)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     }
   }
   ```

6. Define the third measure.

   Define the measure as a column and label it `Putt avg`. Apply custom number
   formatting since the measure should be displayed with two decimals.

   ```json
   {
     "qDef": {
       "qLabel": "FIR%",
       "qDef": "Avg(FwHit)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     }
   },
   {
     "qDef": {
       "qLabel": "GIR%",
       "qDef": "Avg(GIR)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     }
   },
   {
     "qDef": {
       "qLabel": "Putt avg",
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

7. Define the title.

   The title is defined in the options.

   ```json
   {
     "showTitles": true,
     "title": "Golf statistics"
   }
   ```

Result

![Example of pivot table](https://qlik.dev/_astro/on-the-fly-example-pivottable-01-general-collapsed.MijgfrWY.png)

The image below shows the same example with year 2013 expanded.

![Example of pivot table with a measure
category expanded](https://qlik.dev/_astro/on-the-fly-example-pivottable-01-general-expanded.C8uSBy4N.png)

### Complete code example: Basic pivot table

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
          'pivot-table',
          [
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
                "qFieldDefs": [
                  "Date.autoCalendar.Quarter"
                ],
                "qFieldLabels": [
                  "Quarter"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "FIR%",
                "qDef": "Avg(FwHit)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            },
            {
              "qDef": {
                "qLabel": "GIR%",
                "qDef": "Avg(GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            },
            {
              "qDef": {
                "qLabel": "Putt avg",
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
            "title": "Golf statistics"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Adding totals row

In this example, you will add a totals row to the pivot table. This is enabled
in the `qOtherTotalSpec` object of the first dimension.

1. Add the totals row.

   Add the totals row in the column definition of the first dimension (Year):
   `"qOtherTotalSpec": { "qTotalMode": "TOTAL_EXPR" }`. This means that the total
   of the dimension values is returned.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "Date.autoCalendar.Year"
       ],
       "qFieldLabels": [
         "Year"
       ]
     },
     "qNullSuppression": true,
     "qOtherTotalSpec": {
       "qTotalMode": "TOTAL_EXPR"
     }
   },
   ```

2. Add the label.

   Next, add a label for the totals row: `"qTotalLabel": { "qv": "Totals" }`.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "Date.autoCalendar.Year"
       ],
       "qFieldLabels": [
         "Year"
       ]
     },
     "qNullSuppression": true,
     "qOtherTotalSpec": {
       "qTotalMode": "TOTAL_EXPR"
     },
     "qTotalLabel": {
       "qv": "Totals"
     }
   },
   ```

Result

![Example of pivot table with totals row](https://qlik.dev/_astro/on-the-fly-example-pivottable-02-totals.3DrSokAc.png)

### Complete code example: Pivot table with totals row

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
          'pivot-table',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "Date.autoCalendar.Year"
                ],
                "qFieldLabels": [
                  "Year"
                ]
              },
              "qNullSuppression": true,
              "qOtherTotalSpec": {
                "qTotalMode": "TOTAL_EXPR"
              },
              "qTotalLabel": {
                "qv": "Totals"
              }
            },
            {
              "qDef": {
                "qFieldDefs": [
                  "Date.autoCalendar.Quarter"
                ],
                "qFieldLabels": [
                  "Quarter"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "FIR%",
                "qDef": "Avg(FwHit)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            },
            {
              "qDef": {
                "qLabel": "GIR%",
                "qDef": "Avg(GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            },
            {
              "qDef": {
                "qLabel": "Putt avg",
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
            "title": "Golf statistics"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using background color and text color

In this example, you will use expressions to color the cell backgrounds and the
text in your pivot table. This enables you to use expressions to define both the
colors used and the conditional values upon which the colors are applied in a
visualization.

Background colors and text colors are defined in the `qAttributeExpressions`
object inside the applicable measure definition in the columns. The
qAttributeExpressions object consists of two arrays, where the first array is
for defining the background color and the second array is for defining the text color.

1. Set a background color for the first measure.

   You will add a background color to the first measure: `"qAttributeExpressions":`
   `[{ "qExpression": "If(Avg(FwHit)>0.667, RGB(145, 194, 106))" }, {} ]`. This will
   color the cell green for values that are greater than 66.7%.

   ```json
   {
     "qDef": {
       "qLabel": "FIR%",
       "qDef": "Avg(FwHit)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     },
     "qAttributeExpressions": [
       {
         "qExpression": "If(Avg(FwHit)>0.667, RGB(145, 194, 106))"
       },
       {}
     ]
   },
   ```

2. Set a text color for the second measure.

   Next, you will add a text color to the second measure:
   `"qAttributeExpressions":[ {}, { "qExpression":`
   `"If(Avg(GIR)<0.1,RGB(255, 115, 115))" } ]`. This will color the text red for
   values that are below 10%.

   ```json
   {
     "qDef": {
       "qLabel": "GIR%",
       "qDef": "Avg(GIR)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "0.0%",
         "qDec": ".",
         "qThou": ","
       }
     },
     "qAttributeExpressions": [
       {},
       {
         "qExpression": "If(Avg(GIR)<0.1,RGB(255, 115, 115))"
       }
     ]
   },
   ```

Result

![Example of pivot table with with background
and text color modifiers](https://qlik.dev/_astro/on-the-fly-example-pivottable-03-coloring.hGjEXQex.png)

### Complete code example: Background color and text color

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
          'pivot-table',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "Date.autoCalendar.Year"
                ],
                "qFieldLabels": [
                  "Year"
                ]
              },
              "qNullSuppression": true,
              "qOtherTotalSpec": {
                "qTotalMode": "TOTAL_EXPR"
              },
              "qTotalLabel": {
                "qv": "Totals"
              }
            },
            {
              "qDef": {
                "qFieldDefs": [
                  "Date.autoCalendar.Quarter"
                ],
                "qFieldLabels": [
                  "Quarter"
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "FIR%",
                "qDef": "Avg(FwHit)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              },
              "qAttributeExpressions": [
                {
                  "qExpression": "If(Avg(FwHit)>0.667, RGB(145, 194, 106))"
                },
                {}
              ]
            },
            {
              "qDef": {
                "qLabel": "GIR%",
                "qDef": "Avg(GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                }
              },
              "qAttributeExpressions": [
                {},
                {
                  "qExpression": "If(Avg(GIR)<0.1,RGB(255, 115, 115))"
                }
              ]
            },
            {
              "qDef": {
                "qLabel": "Putt avg",
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
            "title": "Golf statistics"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
