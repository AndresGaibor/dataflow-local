---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-waterfall/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating waterfall charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create waterfall charts with the Visualization API.

## Creating a basic waterfall chart

In this example, you will create a basic waterfall chart containing three
measures, with a custom title and color legend switched off.

1. Create the chart.

   Create the container for the chart. The visualization type is `waterfallchart`.

   ```js
   app.visualization.create(
    'waterfallchart',
    [],
    {}
   )
   ```

2. Define the first measure.

   Define the first measure as a column. The first measure is using the measure
   operation Add: `"valueType": "NORMAL"`.

   ```json
   [
     {
       "qDef": {
         "qLabel": "Expected",
         "qDef": "Avg(ExpPutts)",
         "valueType": "NORMAL"
       }
     }
   ]
   ```

3. Define the second measure.

   Define the second measure as a column. It is using the measure operation
   Subtract: `"valueType": "INVERSE"`.

   ```json
   [
     {
       "qDef": {
         "qLabel": "Expected",
         "qDef": "Avg(ExpPutts)",
         "valueType": "NORMAL"
       }
     },
     {
       "qDef": {
         "qLabel": "Actual",
         "qDef": "Avg(Putts)",
         "valueType": "INVERSE"
       }
     }
   ]
   ```

4. Define the third measure.

   Define the third measure as a column. The first measure is using the measure
   operation Subtotals: `"valueType": "SUBTOTAL"`.

   ```json
   [
     {
       "qDef": {
         "qLabel": "Expected",
         "qDef": "Avg(ExpPutts)",
         "valueType": "NORMAL"
       }
     },
     {
       "qDef": {
         "qLabel": "Actual",
         "qDef": "Avg(Putts)",
         "valueType": "INVERSE"
       }
     },
     {
       "qDef": {
         "qLabel": "Shots gained or lost",
         "qDef": "Avg(ExpPutts-Putts)",
         "valueType": "SUBTOTAL"
       }
     }
   ]
   ```

5. Define the title.

   Then add a custom title and switch off the legend in the options.

   ```json
   {
     "showTitles": true,
     "title": "Shots gained or lost putting",
     "legend": {
       "show": false
     }
   }
   ```

Result

![Example of a waterfall chart](https://qlik.dev/_astro/on-the-fly-example-waterfallchart-01-general-noLegend.KdMG9JMW.png)

### Complete code example: Waterfall chart

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
          'waterfallchart',
          [
            {
              "qDef": {
                "qLabel": "Expected",
                "qDef": "Avg(ExpPutts)",
                "valueType": "NORMAL"
              }
            },
            {
              "qDef": {
                "qLabel": "Actual",
                "qDef": "Avg(Putts)",
                "valueType": "INVERSE"
              }
            },
            {
              "qDef": {
                "qLabel": "Shots gained or lost",
                "qDef": "Avg(ExpPutts-Putts)",
                "valueType": "SUBTOTAL"
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Shots gained or lost putting",
            "legend": {
              "show": false
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Defining number formatting and grid line spacing

In this example, the number formatting is changed to always display two decimals
and the grid line spacing has been set to narrow.

1. Set the number formatting.

   Change the number formatting for all three measures in the columns:

   ```json
   "qNumFormat": {
     "qType": "F",
     "qnDec": 2,
     "qUseThou": 0,
     "qFmt": "#,##0.00",
     "qDec": ".",
     "qThou": ","
   }
   ```

2. Set the grid line spacing.

   Then specify the grid line spacing in the options: `"gridlines": { "auto":`
   `false, "spacing": 3 }`, where 3 means narrow.

   ```json
   {
     "showTitles": true,
     "title": "Shots gained or lost putting",
     "gridlines": {
       "auto": false,
       "spacing": 3
     },
     "legend": {
       "show": false
     }
   }
   ```

Result

Example waterfall chart with modified number formats and grid spacing

![Example of a waterfall chart with modified
number formats and grid spacing](https://qlik.dev/_astro/on-the-fly-example-waterfallchart-02-numformat-gridlines.DSDBnsnf.png)

### Complete code example: Waterfall chart with modified number formats and grid spacing

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
          'waterfallchart',
          [
            {
              "qDef": {
                "qLabel": "Expected",
                "qDef": "Avg(ExpPutts)",
                "valueType": "NORMAL",
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
                "qLabel": "Actual",
                "qDef": "Avg(Putts)",
                "valueType": "INVERSE",
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
                "qLabel": "Shots gained or lost",
                "qDef": "Avg(ExpPutts-Putts)",
                "valueType": "SUBTOTAL",
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
            "title": "Shots gained or lost putting",
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "legend": {
              "show": false,
              "dock": "auto"
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using custom colors

You can set the presentation color for the different measure operations:
Positive value color, Negative value color, and Subtotal color.

The following colors are being used in this example:

- Positive value color: `#91c26a`
- Negative value color: `#f8981d`
- Subtotal color: `#52a2cc`

1. Define the colors.

   The colors are defined in the color object. Switch off auto coloring:
   `"auto": false`. Then add a definition for the positive value color:
   `"positiveValue": { "paletteColor": { "index": -1, "color": "#91c26a" }`.
   Add the definition for the negative value color: `"negativeValue":`
   `{ "paletteColor": { "index": 9, "color": "#f8981d" } }`. Finally, define the
   subtotal color: `"subtotal": { "paletteColor": { "index": -1, "color":`
   `"#52a2cc" } }`.

   ```json
   "color": {
     "auto": false,
     "positiveValue": {
       "paletteColor": {
         "index": -1,
         "color": "#91c26a"
       }
     },
     "negativeValue": {
       "paletteColor": {
         "index": 9,
         "color": "#f8981d"
       }
     },
     "subtotal": {
       "paletteColor": {
         "index": -1,
         "color": "#52a2cc"
       }
     }
   }
   ```

Result

![Example of a waterfall chart with custom color
modification](https://qlik.dev/_astro/on-the-fly-example-waterfallchart-03-coloring.Dw-Tz-Mt.png)

### Complete code example: Waterfall chart with custom color modification

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
          'waterfallchart',
          [
            {
              "qDef": {
                "qLabel": "Expected",
                "qDef": "Avg(ExpPutts)",
                "valueType": "NORMAL",
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
                "qLabel": "Actual",
                "qDef": "Avg(Putts)",
                "valueType": "INVERSE",
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
                "qLabel": "Shots gained or lost",
                "qDef": "Avg(ExpPutts-Putts)",
                "valueType": "SUBTOTAL",
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
            "title": "Shots gained or lost putting",
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "color": {
              "auto": false,
              "positiveValue": {
                "paletteColor": {
                  "index": -1,
                  "color": "#91c26a"
                }
              },
              "negativeValue": {
                "paletteColor": {
                  "index": 9,
                  "color": "#f8981d"
                }
              },
              "subtotal": {
                "paletteColor": {
                  "index": -1,
                  "color": "#52a2cc"
                }
             }
            },
            "legend": {
              "show": false,
              "dock": "auto"
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Dimension and measure axis settings

In this example, you will make changes to how the X and Y axes are presented.

1. Configure X axis settings.

   X-axis settings are set in the `dimensionAxis` object.

   Set to display labels only on the X-axis: `"show": "labels"`. State that the
   labels should always be horizontally displayed: `"label": "horizontal"`, and
   positioned at the top of the visualization: `"dock": "far"`.

   ```json
   "dimensionAxis": {
     "show": "labels",
     "label": "horizontal",
     "dock": "far"
   }
   ```

2. Configure Y axis settings.

   Y-axis settings are set in the `measureAxis` object.

   For the Y-axis, also set to display labels only: `"show": "labels"`. Then set
   narrow scaling of the axis: `"spacing": 0.5`, where 0.5 means narrow. Disable
   auto range to define a custom value range for the Y-axis: `"autoMinMax":`
   `false`. Then set the range mode: `"minMax": "minMax"`, and define the
   minimum and maximum values: `"min": -0.5, "max": 2`.

   ```json
   "measureAxis": {
     "show": "labels",
     "spacing": 0.5,
     "autoMinMax": false,
     "minMax": "minMax",
     "min": -0.5,
     "max": 2
   }
   ```

Result

Note that the label of the third measure has been changed to SGLP in the
following example.

![Example of a waterfall chart waterfall chart
with custom dimension and axis settings](https://qlik.dev/_astro/on-the-fly-example-waterfallchart-04-axis-settings.DUwamRJH.png)

### Complete code example: Waterfall chart with custom dimension and axis settings

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
          'waterfallchart',
          [
            {
              "qDef": {
                "qLabel": "Expected",
                "qDef": "Avg(ExpPutts)",
                "valueType": "NORMAL",
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
                "qLabel": "Actual",
                "qDef": "Avg(Putts)",
                "valueType": "INVERSE",
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
                "qLabel": "SGLP",
                "qDef": "Avg(ExpPutts-Putts)",
                "valueType": "SUBTOTAL",
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
            "title": "Shots gained or lost putting",
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "color": {
              "auto": false,
              "positiveValue": {
                "paletteColor": {
                  "index": -1,
                  "color": "#91c26a"
                }
              },
              "negativeValue": {
                "paletteColor": {
                  "index": 9,
                  "color": "#f8981d"
                }
              },
              "subtotal": {
                "paletteColor": {
                  "index": -1,
                  "color": "#52a2cc"
                }
              }
            },
            "legend": {
              "show": false,
              "dock": "auto"
            },
            "measureAxis": {
              "show": "labels",
              "spacing": 0.5,
              "autoMinMax": false,
              "minMax": "minMax",
              "min": -0.5,
              "max": 2
            },
            "dimensionAxis": {
              "show": "labels",
              "label": "horizontal",
              "dock": "far"
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
