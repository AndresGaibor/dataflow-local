---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-gauge/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating gauges

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create gauges with the Visualization API.

## Creating a basic radial gauge

In this example, you will create a basic radial gauge, containing one measure,
with the titles switched off and a custom range.

1. Create the chart
   Create the container for the chart. The visualization type is gauge.

   ```javascript
   app.visualization.create(
     'gauge',
     [],
     {}
   )
   ```

2. Define the measure.

   Define the measure as a column. Note that the value of the measure is to be
   displayed in percent.

   > **Note:** In a gauge, you can only have one measure and no dimensions.

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

3. Disable the title in the options.

   Since the label of the measure by default is visible in the gauge
   visualization, you can switch off the titles.

   ```json
   {
     "showTitles": false
   }
   ```

4. Set the range limit.

   Set a maximum range limit value of the measure to be equal to 100 percent, that
   is, "max": 1.

   ```json
   "measureAxis": {
     "min": 0,
     "max": 1
   }
   ```

5. Define the gauge type.

   Since radial gauges are the default gauge type, "gaugetype": "radial" can be
   omitted from the definition, but it is being kept in this example.

   Result

   ![Gauge object example](https://qlik.dev/_astro/on-the-fly-example-gauge-01-general.D_JZr876.png)

### Complete code example: Basic radial gauge

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
          'gauge',
          [
            {
              "qDef": {
                "qLabel": "Fairway hits",
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
          ],
          {
            "showTitles": false,
            "measureAxis": {
              "min": 0,
              "max": 1
            },
            "gaugetype": "radial"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Presentation and color settings

In this example, you will change the way the gauge is presented by adding
gradient color segments and reducing the arc size. All these changes are set in
the options.

1. Add color segments.

   Enable the usage of segments: `"useSegments": true`. Changes to the color
   segments are then set in the `segmentInfo` object.

   In this example, you will split the gauge into three color segments:
   0 - 0.25, 0.25 - 0.5, and 0.5 - 1.

   To achieve this, first set the measure axis value range.

   ```json
   "measureAxis": {
     "min": 0,
     "max": 1
   }
   ```

   Then add two segment limits to split the range into three segments. Note that
   the color segments are defined to be gradient.

   ```json
   "segmentInfo": {
     "limits": [
       {
         "value": 0.25,
         "gradient": true
       },
       {
         "value": 0.5,
         "gradient": true
       }
     ]
   }
   ```

2. Define the colors for the segments.

   Define the colors to be used for the three segments by adding a
   `paletteColors` object inside the `segmentInfo` object. Add a color for the
   first segment, that is, for values between measure axis minimum and the first
   segment limit. Then add a color for the second segment, that is, for values
   between the first and the second limit. Finally, add a color for the third
   segment, which are for values between the second segment limit and the
   measure axis maximum.

   ```json
   "paletteColors": [
      /*color for the first segment*/
      {
        "color": "#ff7373",
        "index": -1
      },
      /*color for the second segment*/
      {
        "color": "#fab761",
        "index": -1
      },
      /*color for the third segment*/
      {
        "color": "#91c26a",
        "index": -1
      }
   ]
   ```

Result

![Example of gauge object with color gradient settings](https://qlik.dev/_astro/on-the-fly-example-gauge-02-segment-color.CUPKG431.png)

### Complete code example: Presentation and color settings

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
          'gauge',
          [
            {
              "qDef": {
                "qLabel": "Fairway hits",
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
          ],
          {
            "showTitles": false,
            "measureAxis": {
              "min": 0,
              "max": 1
            },
            "gaugetype": "radial",
            "useSegments": true,
            "segmentInfo": {
              "limits": [
                {
                  "value": 0.25,
                  "gradient": true
                },
                {
                  "value": 0.5,
                  "gradient": true
                }
              ],
              "paletteColors": [
                {
                  "color": "#ff7373",
                  "index": -1
                },
                {
                  "color": "#fab761",
                  "index": -1
                },
                {
                  "color": "#91c26a",
                  "index": -1
                }
              ]
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Horizontal and vertical bars

In this example, you want the gauge visualizations to be displayed as a vertical
bar.

1. Change the gauge type.

   To display the gauge as a bar, set `"gaugetype"` in the options.

   ```json
   {
     "gaugetype": "bar"
   }
   ```

2. Set vertical orientation.

   Bars are by default presented with horizontal orientation. In this example,
   you will set vertical orientation. First, turn off auto orientation:
   `"autoOrientation": false` and then set `"orientation": "vertical"`.

   ```json
   {
     "gaugetype": "bar",
     "autoOrientation": false,
     "orientation": "vertical"
   }
   ```

Result

![Example of gauge object with vertical orientation](https://qlik.dev/_astro/on-the-fly-example-gauge-03-vertical-bar.CI6Dz5-6.png)

### Complete code example: Horizontal and vertical bars

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
          'gauge',
          [
            {
              "qDef": {
                "qLabel": "Fairway hits",
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
          ],
          {
            "showTitles": false,
            "measureAxis": {
              "min": 0,
              "max": 1
            },
            "gaugetype": "bar",
            "autoOrientation": false,
            "orientation": "vertical",
            "useSegments": true,
            "segmentInfo": {
              "limits": [
                {
                  "value": 0.25,
                  "gradient": true
                },
                {
                  "value": 0.5,
                  "gradient": true
                }
              ],
              "paletteColors": [
                {
                  "color": "#ff7373",
                  "index": -1
                },
                {
                  "color": "#fab761",
                  "index": -1
                },
                {
                  "color": "#91c26a",
                  "index": -1
                }
              ]
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
