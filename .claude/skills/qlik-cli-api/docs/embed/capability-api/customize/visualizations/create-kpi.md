---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-kpi/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating KPIs

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create KPIs with the Visualization API.

## Creating a basic KPI

In this example, you will create a basic KPI, containing a single measure. Measure
titles are displayed in the visualization by default.

1. Create the chart.

   Create the container for the chart. The visualization type is `kpi`.

   ```javascript
   app.visualization.create(
     'kpi',
     [],
     {}
   )
   ```

2. Define the measure.

   Define the measure as a column. Note that the number formatting is defined
   to display the value as a percentage.

   > **Note:** In a KPI visualization, you can have one or two measures and no dimensions.

   ```json
   [
     {
       "qDef": {
         "qLabel": "GIR %",
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
   ]
   ```

3. Style the text

   Since measure titles are displayed by default, `"showMeasureTitle": true` can
   be omitted. Visualization titles are therefore turned off by default, which
   means that `"showTitles": false` can also be omitted.

   In this example, you will select to center align the text and use large font size.

   ```json
   {
     "showTitles": false,
     "showMeasureTitle": true,
     "textAlign": "center",
     "fontSize": "L"
   }
   ```

Result

![KPI object example](https://qlik.dev/_astro/on-the-fly-example-kpi-01-large-font.DHID1rEn.png)

### Complete code example: Basic KPI

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
          'kpi',
          [
            {
              "qDef": {
                "qLabel": "GIR %",
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
          ],
          {
            "showTitles": false,
            "showMeasureTitle": true,
            "textAlign": "center",
            "fontSize": "L"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using two measures with different colors

In this example, you will add a second measure, where the second value
automatically becomes a complementary value and is shown with a smaller font
size. You will also apply different colors to the two measures.

1. Define the first measure.

   Define the measure as a column. The first measure is defined to display the
   current year value as a percentage.

   ```json
   {
     "qDef": {
       "qLabel": "GIR % current year",
       "qDef": "Avg({<[Date.autoCalendar.YearsAgo]={'3'}>}GIR)",
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

2. Define the second measure.

   Define the measure as a column. The second measure is to display the all time
   value as a percentage.

   ```json
   {
     "qDef": {
       "qLabel": "GIR % current year",
       "qDef": "Avg({<[Date.autoCalendar.YearsAgo]={'3'}>}GIR)",
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
       "qLabel": "All time",
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

3. Coloring the first measure.

   The first measure is to be displayed in the color #f05555, which is not in the
   default color palette. The following is added to the column definition for the
   first measure.

   ```json
   "conditionalColoring": {
     "paletteSingleColor": {
       "index": -1,
       "color": "#f05555"
     }
   }
   ```

4. Coloring the second measure.

   The second measure is to be displayed in the color #545352, defined in the
   default color palette as `"index": 14`. The following is added to the column
   definition for the second measure.

   ```json
   "conditionalColoring": {
     "paletteSingleColor": {
        "index": 14,
        "color": "#545352"
     }
   }
   ```

Result

![Example KPI object with multiple measures,
each with unique colors](https://qlik.dev/_astro/on-the-fly-example-kpi-02-measures-colors.C6k7RKYm.png)

### Complete code example: Two measures with different colors

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
          'kpi',
          [
            {
              "qDef": {
                "qLabel": "GIR % current year",
                "qDef": "Avg({<[Date.autoCalendar.YearsAgo]={'3'}>}GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                },
                "conditionalColoring": {
                  "paletteSingleColor": {
                    "index": -1,
                    "color": "#f05555"
                  }
                }
              }
            },
            {
              "qDef": {
                "qLabel": "All time",
                "qDef": "Avg(GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                },
                "conditionalColoring": {
                  "paletteSingleColor": {
                    "index": 14,
                    "color": "#545352"
                  }
                }
              }
            }
          ],
          {
            "showTitles": false,
            "showMeasureTitle": true,
            "textAlign": "center",
            "fontSize": "L"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using conditional colors and symbols

When you use conditional colors for your KPI visualization, you have the option
to use symbols to be displayed next to your measure value. In this example,
conditional coloring is used on the first measure. Two color segments are
defined where different colors are used for values greater than and less than
the defined limit.

You can also add symbols to the values. In this example, Arrow down is defined
as a symbol for values less than the limit and Arrow up is defined as a symbol for
values greater than the limit.

1. Enable conditional coloring.

   Conditional colors is defined in the `conditionalColoring` object. You will
   enable conditional coloring for the first measure:

   ```json
   "conditionalColoring": {
     "useConditionalColoring": true
   }
   ```

2. Define the color segment limit.

   Define the limit in the `segments` object to use two color segments. The
   limit is an expression: Avg(GIR).

   ```json
   "conditionalColoring": {
     "useConditionalColoring": true,
     "segments": {
       "limits": [
         {
           "value": {
             "qValueExpression": {
               "qExpr": "Avg(GIR)"
             }
           },
           "gradient": false
         }
       ]
     }
   }
   ```

3. Define segment colors and icons.

   The two color segments greater than and less than the limit specified in the previous
   step, are defined in the `paletteColors` object. You will define different
   colors and icons for the segments: Arrow down is defined as a symbol for values
   less than the limit and Arrow up is defined as a symbol for values greater
   than the limit.

   ```json
   "conditionalColoring": {
     "useConditionalColoring": true,
     "segments": {
       "limits": [
         {
           "value": {
             "qValueExpression": {
               "qExpr": "Avg(GIR)"
             }
           },
           "gradient": false
         }
       ],
       "paletteColors": [
         {
           "color": "#ae5798",
           "icon": "S",
           "index": -1
         },
         {
           "color": "#529a18",
           "icon": "R",
           "index": -1
         }
       ]
     }
   }
   ```

4. Coloring the second measure.

   Single color is used on the second measure. In this example, a shade of the
   color red (#f05555) is used:

   ```json
   "conditionalColoring": {
     "useConditionalColoring": false,
     "singleColor": 3,
     "paletteSingleColor": {
       "index": -1,
       "color": "#f05555"
     }
   }
   ```

Result

![Example KPI object with conditional color settings](https://qlik.dev/_astro/on-the-fly-example-kpi-03-conditional-colors.BuKAiZvq.png)

### Complete code example: Conditional colors and symbols

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
          'kpi',
          [
            {
              "qDef": {
                "qLabel": "GIR % current year",
                "qDef": "Avg({<[Date.autoCalendar.YearsAgo]={'3'}>}GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                },
                "conditionalColoring": {
                  "useConditionalColoring": true,
                  "segments": {
                    "limits": [
                      {
                        "value": {
                          "qValueExpression": {
                            "qExpr": "Avg(GIR)"
                          }
                        },
                        "gradient": false
                      }
                    ],
                    "paletteColors": [
                      {
                        "color": "#ae5798",
                        "icon": "S",
                        "index": -1
                      },
                      {
                        "color": "#529a18",
                        "icon": "R",
                        "index": -1
                      }
                    ]
                  }
                }
              }
            },
            {
              "qDef": {
                "qLabel": "All time",
                "qDef": "Avg(GIR)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0,
                  "qFmt": "0.0%",
                  "qDec": ".",
                  "qThou": ","
                },
                "conditionalColoring": {
                  "useConditionalColoring": false,
                  "singleColor": 3,
                  "paletteSingleColor": {
                    "index": -1,
                    "color": "#f05555"
                  }
                }
              }
            }
          ],
          {
            "showTitles": false,
            "showMeasureTitle": true,
            "textAlign": "center",
            "fontSize": "L"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
