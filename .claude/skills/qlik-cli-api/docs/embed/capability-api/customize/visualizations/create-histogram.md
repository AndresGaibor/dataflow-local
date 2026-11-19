---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-histogram/
last_updated: 2025-10-31T14:06:52+01:00
---

# Creating histogram charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create histograms with the Visualization API.

## Creating a basic histogram

In this example, you will create a basic histogram, containing a single
dimension and a custom title.

1. Create the chart

   Create the container for the chart. The visualization type is histogram.

   Visualization API

   ```javascript
   app.visualization.create(
     'histogram',
      [],
      {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column.

   > **Note:** You can only apply a single dimension to a histogram. The dimension
   > must be a numerical field. Histograms do not need a measure, as the frequency
   > of the binned data is automatically calculated.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "DrDist"
         ],
         "qFieldLabels": [
           "Drive distance"
         ]
       }
     }
   ]
   ```

3. Define the title in the options.

   ```json
   {
     "title": "Driving distance"
   }
   ```

Result

![Histogram example](https://qlik.dev/_astro/on-the-fly-example-histogram-01-general.Cjb44Y4D.png)

### Complete code example: Basic histogram

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
          'histogram',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "DrDist"
                ],
                "qFieldLabels": [
                  "Drive distance"
                ]
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Driving distance"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Setting maximum number of bars

In this example, you will set the maximum number of bars that you want to divide
the data into. You will select to display a maximum of 6 bars (or bins). You
achieve this by configuring the `bins` object in the options.

1. Disable auto-bins.

   In the `bins` object, enable custom bars by setting `"auto": false`.

   ```json
   "bins": {
     "auto": false
   }
   ```

2. Define the maximum number of bars.

   To use the maximum number of bars feature, set `"binMode": "maxCount"` and
   then define the maximum number: `"binCount": 6`.

   ```json
   "bins": {
     "auto": false,
     "binMode": "maxCount",
   "binCount": 6
   }
   ```

Result

![Histogram chart example with bar maximum](https://qlik.dev/_astro/on-the-fly-example-histogram-02-bars.05smBs6X.png)

### Complete code example: Setting maximum number of bars

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
          'histogram',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "DrDist"
                ],
                "qFieldLabels": [
                  "Drive distance"
                ]
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Driving distance",
            "bins": {
              "auto": false,
              "binMode": "maxCount",
              "binCount": 6
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Setting bar width on the x-axis

In this example, you will define how wide each bar should be, based on the
values on the x-axis, and which offset the bars are using by configuring the
`bins` object in the options.

1. Disable auto-bins.

   Make sure that custom bars are enabled ("auto": false).

   ```json
   "bins": {
     "auto": false
   }
   ```

2. Define the bar width.

   To use the bar width feature, set `"binMode": "size"`. Set the width of each
   bar `"binSize": 10` and then set the offset: `"offset": 5`.

   In this example, you have set the bar width to 10 and the offset is 5. That
   means the first bar is 5 to 15, the second bar is 15 to 25, and so forth.

   ```json
   "bins": {
     "auto": false,
     "binMode": "size",
     "binSize": 10,
     "offset": 5
   }
   ```

Result

![Histogram chart example with set bar width](https://qlik.dev/_astro/on-the-fly-example-histogram-03-bar-width.34MvZVcT.png)

### Complete code example: Setting bar width on the x-axis

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
          'histogram',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "DrDist"
                ],
                "qFieldLabels": [
                  "Drive distance"
                ]
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Driving distance",
            "bins": {
              "auto": false,
              "binMode": "size",
              "binSize": 10,
              "offset": 5
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Presentation, colors and axis settings

In this example, you will define some settings for how the histogram is
presented. All these settings are defined in the options.

1. Grid line spacing

   The spacing between the grid lines are set in the gridlines object. To use
   narrow grid line spacing, set `"auto": false` and then set `"spacing": 3`,
   where 3 means narrow.

   ```json
   "gridlines": {
     "auto": false,
     "spacing": 3
   }
   ```

2. Y-axis settings

   This example shows labels only on the Y-axis (measure axis), uses narrow
   scale, and has a custom value range defined. These settings are set in the
   `measureAxis` object.

   To show labels only, set `"show": "labels"`. Then set narrow scale:
   `"spacing": 0.5` where 0.5 means narrow. Finally, set `"autoMinMax": false`,
   `"minMax": "min"`, and `"min": 100` to define the custom range.

   ```json
   "measureAxis": {
     "show": "labels",
     "dock": "near",
     "spacing": 0.5,
     "autoMinMax": false,
     "minMax": "min",
     "min": 100
   }
   ```

3. X-axis settings

   To show labels only on the X-axis (dimension axis):

   ```json
   "dimensionAxis": {
     "show": "labels"
   }
   ```

4. Value labels on data points

   To show values labels on data points:

   ```json
   "dataPoint": {
    "showLabels": true
   }
   ```

5. Bar colors

   The bar color is defined in the color object. In this example, you will
   define a color that is not part of the default color palette.

   ```json
   "color": {
     "bar": {
       "paletteColor": {
         "index": -1,
         "color": "#d47dbe"
       }
     }
   }
   ```

Result

![Histogram chart example modified colour
and label settings](https://qlik.dev/_astro/on-the-fly-example-histogram-04-color-spacing.aeDWAnba.png)

### Complete code example: Presentation, colors and axis settings

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
          'histogram',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "DrDist"
                ],
                "qFieldLabels": [
                  "Drive distance"
                ]
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Driving distance",
            "bins": {
              "auto": false,
              "binMode": "size",
              "binSize": 10,
              "offset": 5
            },
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "measureAxis": {
              "show": "labels",
              "spacing": 0.5,
              "autoMinMax": false,
              "minMax": "min",
              "min": 100
            },
            "dimensionAxis": {
              "show": "labels"
            },
            "dataPoint": {
              "showLabels": true
            },
            "color": {
              "bar": {
                "paletteColor": {
                  "index": -1,
                  "color": "#d47dbe"
                }
              }
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
