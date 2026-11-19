---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-scatterplot/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating scatter plots

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create scatter plots with the Visualization API.

## Basic scatter plot with number formatting

In this example, you will create a basic scatter plot, containing one dimension
and two measures. The measures have basic number formatting applied and a title
is added to the scatter plot.

1. Create the chart.

   Create the container for the chart. The visualization type is `scatterplot`.

   ```js
   app.visualization.create(
     'scatterplot',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=[Date.autoCalendar.YearQuarter]"
       ],
       "qFieldLabels": [
         "Year & Qtr"
       ]
     },
     "qNullSuppression": true
   }
   ```

3. Define the first measure.

   Define the first measure as a column.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=[Date.autoCalendar.YearQuarter]"
       ],
       "qFieldLabels": [
         "Year & Qtr"
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
   }
   ```

4. Define the second measure.

   Define the second measure as a column.

   ```json
   {
     "qDef": {
       "qFieldDefs": [
         "=[Date.autoCalendar.YearQuarter]"
       ],
       "qFieldLabels": [
         "Year & Qtr"
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
   }
   ```

5. Define the title.

   Then define the title in the options.

   ```json
   {
     "showTitles": true,
     "title": "Fairways hit vs. Greens hit relation"
   }
   ```

Result

![Example of a scatter plot chart](https://qlik.dev/_astro/on-the-fly-example-scatterplot-01-general.2xWJ9qnE.png)

### Complete code example: Basic scatter plot chart

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
          'scatterplot',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=[Date.autoCalendar.YearQuarter]"
                ],
                "qFieldLabels": [
                  "Year and Qtr"
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
           }    
          ],
          {
            "showTitles": true,
            "title": "Fairways hit vs. Greens hit relation"
          }
          ).then((vis)=>{
            vis.show("QV01");
        });
      });
      ```
    </details>

## Using calculated bubble size

In this example, you will add a third measure to the scatter plot, which is used
to calculate the bubble size.

1. Define the third measure.

   Define the third measure as a column.

   ```json
   {
     "qDef": {
       "qLabel": "Holes played",
       "qDef": "Count(HoID)"
     }
   }
   ```

2. Define the bubble size range.

   The bubble size range is defined in the `dataPoint` object in the options:
   `"dataPoint": { "rangeBubbleSizes": [ 1, 11 ] }`.

   > **Note:** `rangeBubbleSizes` is an array of integers where the first index is
   > the from-size, and the second is the to-size. From-size should always be
   > smaller than the to-size. 1 is the minimum value and 20 is the maximum value.

   ```json
   {
     "showTitles": true,
     "title": "Fairways hit vs. Greens hit relation",
     "dataPoint": {
       "rangeBubbleSizes": [
         1,
         11
       ]
     }
   }
   ```

Result

![Example of a scatter plot chart with bubble
size modified by data](https://qlik.dev/_astro/on-the-fly-example-scatterplot-02-BubbleSize.Cwv8F7W5.png)

### Complete code example: Scatter plot chart with bubble size modified by data

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
          'scatterplot',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=[Date.autoCalendar.YearQuarter]"
                ],
                "qFieldLabels": [
                  "Year and Qtr"
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
                "qLabel": "Holes played",
                "qDef": "Count(HoID)"
              }
            }  
          ],
          {
            "showTitles": true,
            "title": "Fairways hit vs. Greens hit relation",
            "dataPoint": {
              "rangeBubbleSizes": [
                1,
                11
              ]
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Customizing the bubble colors

In this example, you will customize the color of the bubbles by an expression,
where three different colors are applied depending on the return value of the expression.

1. Enable custom colors.

   The bubble color is defined in the color object. You will enable custom coloring
   `"auto": false` and set `"mode": "byExpression"`. Then define the expression to
   be used for coloring: `"colorExpression": "If(Avg(Stableford)>2,rgb(82, 162, 204),`
   `If(Avg(Stableford)<1.65,rgb(248, 152, 29),rgb(128, 128, 128)))"`. Since the
   expression includes an actual color code, set `"expressionIsColor": true`.

   ```json
   "color": {
     "auto": false,
     "mode": "byExpression"
   }

   ```

2. Define the color expression.

   You then define the expression to be used for coloring: `"colorExpression":`
   `"If(Avg(Stableford)>2,rgb(82, 162, 204),If(Avg(Stableford)<1.65,rgb(248,`
   `152, 29),rgb(128, 128, 128)))"`.
   Since the expression includes an actual color code,
   `"expressionIsColor": true`.

   ```json
   "color": {
     "auto": false,
     "mode": "byExpression",
     "expressionIsColor": true,
     "colorExpression": "If(Avg(Stableford)>2,rgb(82, 162, 204),
     If(Avg(Stableford)<1.65,rgb(248, 152, 29),rgb(128, 128, 128)))"
   }
   ```

3. Add an attribute expression on the first measure.

   Since color expressions must be added as attribute expressions on the first
   measure, you define this inside the first measure definition in the columns:
   `"qAttributeExpressions": [ { "qExpression": "If(Avg(Stableford)>2,rgb(82,`
   `162, 204),   If(Avg(Stableford)<1.65,rgb(248, 152, 29),rgb(128, 128,`
   `128)))", "id": "colorByExpression" } ]`.

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
         "qExpression": "If(Avg(Stableford)&gt;2,rgb(82, 162, 204),
         If(Avg(Stableford)&lt;1.65,rgb(248, 152, 29),rgb(128, 128, 128)))",
         "id": "colorByExpression"
       }
     ]
   },
   ```

Result

![Example of a scatter plot chart with colour and
attribute modifiers](https://qlik.dev/_astro/on-the-fly-example-scatterplot-03-Coloring.CXGIMdbY.png)

### Complete code example: Scatter plot chart with colour and attribute modifiers

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
          'scatterplot',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "=[Date.autoCalendar.YearQuarter]"
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
                  "qExpression": "If(Avg(Stableford)>2,rgb(82, 162, 204), If(Avg(Stableford)<1.65,rgb(248, 152, 29),rgb(128, 128, 128)))",
                  "id": "colorByExpression"
                }
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
              }
            },
            {
              "qDef": {
                "qLabel": "Holes played",
                "qDef": "Count(HoID)"
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Fairways hit vs. Greens hit relation",
            "showDetails": false,
            "navigation": false,
            "dataPoint": {
              "bubbleSizes": 5,
              "rangeBubbleSizes": [
                1,
                11
              ]
            },
            "labels": {
              "mode": 0
            },
            "compressionResolution": 5,
            "gridLine": {
              "auto": false,
              "spacing": 3
            },
            "color": {
              "auto": false,
              "mode": "byExpression",
              "useBaseColors": "off",
              "expressionIsColor": true,
              "colorExpression": "If(Avg(Stableford)>2,rgb(82, 162, 204),If(Avg(Stableford)<1.65,rgb(248, 152, 29),rgb(128, 128, 128)))"
            },
            "xAxis": {
              "show": "labels"
             },
            "yAxis": {
              "show": "labels"
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
