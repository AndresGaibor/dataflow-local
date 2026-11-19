---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-table/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating tables

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create tables with the Visualization API.

## Creating a basic table

In this example, you will create a basic table, containing one dimension and four
measures. The measures have basic number formatting applied and the dimension is
sorted by load order. No options are defined for the table.

1. Create the chart.

   Create the container for the chart. The visualization type is `table`.

   ```js
   app.visualization.create(
    'table',
    [],
    {}
   )
   ```

2. Define the first dimension.

   You start by adding the dimension. Note the sort order definition in the
   `qSortCriterias` object and that null values have been suppressed.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=If(Par&gt;3,TClubName)"
       ],
       "qFieldLabels": [
         "Tee club"
       ],
       "qSortCriterias": [
         {
           "qSortByLoadOrder": 1
         }
       ]
     },
     "qNullSuppression": true
   }
   ```

3. Define the first measure.

   You then add the first measure.

   ```json
   {
     "qDef": {
       "qLabel": "#",
       "qDef": "Count(HoID)"
     }
   }
   ```

4. Define the second measure.

   Next, you add the second measure and apply custom number formatting to it as
   you want it to be shown in percent.

   ```json
   {
     "qDef": {
       "qLabel": "#",
       "qDef": "Count(HoID)"
     }
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
   }
   ```

5. Define the third measure.

   Add the third measure and apply custom number formatting to it. This time,
   you want to show the measure value as numbers with an addition to indicate
   that the number is in meters.

   ```json
   {
     "qDef": {
       "qLabel": "#",
       "qDef": "Count(HoID)"
     }
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
       "qLabel": "Avg",
       "qDef": "Avg(DrDist)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "#,##0.00 m",
         "qDec": ".",
         "qThou": ","
       },
       "numFormatFromTemplate": false
     }
   }
   ```

6. Define the fourth measure.

   Finally, you will add the fourth measure. You apply custom number formatting to
   it as well, and just as for the third measure, you want to show the measure
   value as numbers with an addition to indicate that the number is in meters.

   ```json
   {
     "qDef": {
       "qLabel": "#",
       "qDef": "Count(HoID)"
     }
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
       "qLabel": "Avg",
       "qDef": "Avg(DrDist)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "#,##0.00 m",
         "qDec": ".",
         "qThou": ","
       },
       "numFormatFromTemplate": false
     }
   },
   {
     "qDef": {
       "qLabel": "Max",
       "qDef": "Max(DrDist)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 2,
         "qUseThou": 0,
         "qFmt": "#,##0 m",
         "qDec": ".",
         "qThou": ","
       },
       "numFormatFromTemplate": false
     }
   }
   ```

Result

![Example of a standard table](https://qlik.dev/_astro/on-the-fly-example-table-01-general.pKU9OQjg.png)

### Complete code example: Basic standard table

- <details>
      <summary>Visualization API</summary>

      ```js
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
          'table',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=If(Par>3,TClubName)"
                ],
                "qFieldLabels": [
                  "Tee club"
                ],
                "qSortCriterias": [
                  {
                    "qSortByLoadOrder": 1
                  }
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "#",
                "qDef": "Count(HoID)"
              }
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
                "qLabel": "Avg",
                "qDef": "Avg(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0.00 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            },
            {
              "qDef": {
                "qLabel": "Max",
                "qDef": "Max(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            }
          ],
          {
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using background color and text color

In this example, you will use expressions to color the cell backgrounds and the
text in tables. This enables you to use expressions to define both the colors
used and the conditional values upon which the colors are applied in a visualization.

Background colors and text colors are defined in the `qAttributeExpressions`
object inside the applicable measure definition in the columns.

Note that the definition of `qAttributeExpressions` for straight tables is
different from the definition for pivot tables.

1. Set the text color for the first measure.

   Add a text color condition to the first measure: `"qAttributeExpressions":`
   `[ { "qExpression": "If(Count(HoID)<10,RGB(255, 115, 115))", "id":`
   `"cellForegroundColor" } ]`. Text color is defined with `"id": "cellForegroundColor"`.

   ```json
   {
     "qDef": {
       "qLabel": "#",
       "qDef": "Count(HoID)"
     },
     "qAttributeExpressions": [
       {
         "qExpression": "If(Count(HoID)<10,RGB(255, 115, 115))",
         "id": "cellForegroundColor"
       }
     ]
   },
   ```

2. Set the background color for the second measure.

   Next, you will add a background color condition to the second measure:
   `"qAttributeExpressions": [ { "qExpression": "If(Avg(FwHit)<0.5,RGB(255,`
   `115, 115),If(Avg(FwHit)>0.7,RGB(145, 194, 106)))", "id":`
   `"cellBackgroundColor" } ]`. Background color is defined with `"id": "cellBackgroundColor"`.

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
         "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115),If(Avg(FwHit)>0.7,`
         `RGB(145, 194, 106)))",`
         "id": "cellBackgroundColor"
       }
     ]
   }
   ```

3. Define the title.

   In this example, you will also add a title, which is defined in the options.

   ```json
   {
     "showTitles": true,
     "title": "Off the tee (Par 4s and Par 5s)"
   }
   ```

Result

![Example of a table object with text and background
color modifiers](https://qlik.dev/_astro/on-the-fly-example-table-02-bgcolor.COdtrndP.png)

### Complete code example: Table object with text and background color modifiers

- <details>
      <summary>Visualization API</summary>

      ```js
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
          'table',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=If(Par>3,TClubName)"
                ],
                "qFieldLabels": [
                  "Tee club"
                ],
                "qSortCriterias": [
                  {
                    "qSortByLoadOrder": 1
                  }
                ]
              },
              "qNullSuppression": true
            },
            {
              "qDef": {
                "qLabel": "#",
                "qDef": "Count(HoID)"
              },
              "qAttributeExpressions": [
                {
                  "qExpression": "If(Count(HoID)<10,RGB(255, 115, 115))",
                  "id": "cellForegroundColor"
                }
              ]
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
                  "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115),If(Avg(FwHit)>0.7,RGB(145, 194, 106)))",
                  "id": "cellBackgroundColor"
                }
              ]
            },
            {
              "qDef": {
                "qLabel": "Avg",
                "qDef": "Avg(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0.00 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            },
            {
              "qDef": {
                "qLabel": "Max",
                "qDef": "Max(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Off the tee (Par 4s and Par 5s)"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Applying dimension limits

In this example, you want to display all items where the value of the first
measure is greater than 5.

1. Define the mode.

   Start by defining the mode. Since you want to limit the dimension values to an
   absolute value, set `"qOtherMode": "OTHER_ABS_LIMITED"`.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=If(Par>3,TClubName)"
       ],
       "qFieldLabels": [
         "Tee club"
       ],
       "qSortCriterias": [
         {
           "qSortByLoadOrder": 1
         }
       ]
     },
     "qNullSuppression": true,
     "qOtherTotalSpec": {
       "qOtherMode": "OTHER_ABS_LIMITED"
     }
   },
   ```

2. Define the limit value.

   Next, you will define the actual value: `"qOtherLimit": {"qv": "5"}`. Set
   `"qOtherLimitMode": "OTHER_GT_LIMIT"` to include only the values greater than
   what you defined in `qOtherLimit`.

   > **Note:** `"qOtherLimit": {"qv": "5"}` means that only the items with a value greater than 5 will be displayed.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=If(Par>3,TClubName)"
       ],
       "qFieldLabels": [
         "Tee club"
       ],
       "qSortCriterias": [
         {
           "qSortByLoadOrder": 1
         }
       ]
     },
     "qNullSuppression": true,
     "qOtherTotalSpec": {
       "qOtherMode": "OTHER_ABS_LIMITED",
       "qOtherLimit": {
         "qv": "5"
       },
       "qOtherLimitMode": "OTHER_GT_LIMIT"
     }
   },
   ```

3. Additional settings.

   You want to define the sort order of the dimension values to sort descending:
   `"qOtherSortMode": "OTHER_SORT_DESCENDING"`. You do not want any totals to be
   displayed and therefore set: `"qTotalMode": "TOTAL_OFF"`.

   Finally, set the label of the Others group: `"qOtherLabel": { "qv": "Other`
   `clubs" }`.

   Note that the label is not set inside the `qOtherTotalSpec` object.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=If(Par>3,TClubName)"
       ],
       "qFieldLabels": [
         "Tee club"
       ],
       "qSortCriterias": [
         {
           "qSortByLoadOrder": 1
         }
       ]
     },
     "qNullSuppression": true,
     "qOtherTotalSpec": {
       "qOtherMode": "OTHER_ABS_LIMITED",
       "qOtherLimit": {
         "qv": "5"
       },
       "qOtherLimitMode": "OTHER_GT_LIMIT",
       "qOtherSortMode": "OTHER_SORT_DESCENDING",
       "qTotalMode": "TOTAL_OFF"
     },
     "qOtherLabel": {
       "qv": "Other clubs"
     }
   },
   ```

Result

![Example of a table object with dimension limits](https://qlik.dev/_astro/on-the-fly-example-table-03-dimension-limit.lsFJOGoB.png)

### Complete code example: Table object with dimension limits

- <details>
      <summary>Visualization API</summary>

      ```js
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
          'table',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=If(Par>3,TClubName)"
                ],
                "qFieldLabels": [
                  "Tee club"
                ],
                "qSortCriterias": [
                  {
                    "qSortByLoadOrder": 1
                  }
                ],
                "othersLabel": "Other clubs"
              },
              "qNullSuppression": true,
              "qOtherTotalSpec": {
                "qOtherMode": "OTHER_ABS_LIMITED",
                "qOtherLimit": {
                  "qv": "5"
                },
                "qOtherLimitMode": "OTHER_GT_LIMIT",
                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                "qTotalMode": "TOTAL_OFF"
              },
              "qOtherLabel": {
                "qv": "Other clubs"
              }
            },
            {
              "qDef": {
                "qLabel": "#",
                "qDef": "Count(HoID)"
              },
              "qAttributeExpressions": [
                {
                  "qExpression": "If(Count(HoID)<10,RGB(255, 115, 115))",
                  "id": "cellForegroundColor"
                }
              ]
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
                  "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115),If(Avg(FwHit)>0.7,RGB(145, 194, 106)))",
                  "id": "cellBackgroundColor"
                }
              ]
            },
            {
              "qDef": {
                "qLabel": "Avg",
                "qDef": "Avg(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0.00 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            },
            {
              "qDef": {
                "qLabel": "Max",
                "qDef": "Max(DrDist)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "#,##0 m",
                  "qDec": ".",
                  "qThou": ","
                },
                "numFormatFromTemplate": false
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Off the tee (Par 4s and Par 5s)"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
