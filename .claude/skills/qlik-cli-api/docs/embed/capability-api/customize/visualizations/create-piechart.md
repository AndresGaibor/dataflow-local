---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-piechart/
last_updated: 2025-07-03T16:05:11+02:00
---

# Creating pie charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create pie charts with the Visualization API.

## Creating a basic pie chart

In this example, you will create a basic pie chart, containing one dimension and
one measure, and switch the titles off.

1. Create the chart.

   Create the container for the chart. The visualization type is `piechart`.

   ```js
   app.visualization.create(
     'piechart',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     }
   ]
   ```

3. Define the measure.

   Define the measure as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     },
     "=Count(HoID)"
   ]
   ```

4. Switch off the titles.

   Since the dimension label by default is visible in the visualization, you
   will select to switch the titles off.

   ```json
   {
     "showTitles": false
   }
   ```

Result

![Example of pie chart](https://qlik.dev/_astro/on-the-fly-example-piechart-01-general.tH7Gb_fQ.png)

### Complete code example: Basic pie chart

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
          'piechart',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "GirResult"
                ],
                "qFieldLabels": [
                  "Greens in regulation"
                ]
              }
            },
            "=Count(HoID)"
          ],
          {
            "showTitles": false
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Creating a basic donut chart

In this example, you will create exactly the same chart as in *Creating a basic
pie chart*, but you will select to display it as a donut. This is done by simply
adding the donut definition in the options.

1. Define the dimension.

   Define the dimension as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     }
   ]
   ```

2. Define the measure.

   Define the measure as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     },
     "=Count(HoID)"
   ]
   ```

3. Switch off the titles.

   Since the dimension label by default is visible in the visualization, you
   will select to switch the titles off.

   ```json
   {
     "showTitles": false
   }
   ```

4. Display the chart as a donut.

   Since the dimension label by default is visible in the visualization, you
   will select to switch the titles off.

   ```json
   {
     "showTitles": false,
     "donut": {
       "showAsDonut": true
     }
   }
   ```

Result

![Example of pie chart in donut format](https://qlik.dev/_astro/on-the-fly-example-piechart-01-donut.zH9kw26F.png)

### Complete code example: Basic donut chart

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
          'piechart',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "GirResult"
                ],
                "qFieldLabels": [
                  "Greens in regulation"
                ]
              }
            },
            "=Count(HoID)"
          ],
          {
            "showTitles": false,
            "donut": {
              "showAsDonut": true
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Using custom value labels

In this example, you will change the value labels so that they display actual
values instead of percentage.

1. Change number formatting of measure.

   First, you will change the number formatting of the measure in the columns. Set
   `"qType": "F"` to indicate that a fixed number of decimals is used. Then set
   `"qnDec": 0` to indicate that no decimals are used.

   ```json
   {
     "qDef": {
       "qLabel": "Frequency",
       "qGrouping": "N",
       "qDef": "Count(HoID)",
       "qNumFormat": {
         "qType": "F",
         "qnDec": 0,
         "qUseThou": 0,
         "qFmt": "#,##0",
         "qDec": ".",
         "qThou": ","
       }
     }
   }
   ```

2. Define value label mode.

   You want to display the actual values instead of the share so inside the
   `dataPoint` object (in the options), set `"labelMode": "value"`.

   ```json
   {
     "showTitles": false,
     "donut": {
       "showAsDonut": true
     },
     "dataPoint": {
       "auto": false,
       "labelMode": "value"
     }
   }
   ```

Result

![Example of pie chart with custom value labels](https://qlik.dev/_astro/on-the-fly-example-piechart-02-number-format.CLoP5EYP.png)

### Complete code example: Custom value labels

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
          'piechart',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "GirResult"
                ],
                "qFieldLabels": [
                  "Greens in regulation"
                ]
              }
            },
            {
              "qDef": {
                "qLabel": "Frequency",
                "qGrouping": "N",
                "qDef": "Count(HoID)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 0,
                  "qUseThou": 0,
                  "qFmt": "#,##0",
                  "qDec": ".",
                  "qThou": ","
                }
              }
            }
          ],
          {
            "showTitles": false,
            "donut": {
              "showAsDonut": true
            },
            "dataPoint": {
              "auto": false,
              "labelMode": "value"
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Adding a radius measure

In this example, you will add a second measure to calculate the radius. The
measure added is the average Stableford points.

1. Create the chart.

   Create the container for the chart. The visualization type is `piechart`.

   ```js
   app.visualization.create(
     'piechart',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     }
   ]
   ```

3. Define the first measure.

   Define the first measure as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     },
     "=Count(HoID)"
   ]
   ```

4. Define the second measure.

   Define the second measure as a column.

   ```json
   [
     {
       "qDef": {
         "qFieldDefs": [
           "GirResult"
         ],
         "qFieldLabels": [
           "Greens in regulation"
         ]
       }
     },
     "=Count(HoID)",
     "=Avg(Stableford)"
   ]
   ```

5. Switch off the titles.

   Since the dimension label, by default, is visible in the visualization, you
   will select to switch the titles off.

   ```json
   {
     "showTitles": false
   }
   ```

Result

![Example of pie chart with radius measure
modification](https://qlik.dev/_astro/on-the-fly-example-piechart-01-radius.D_OEA-Td.png)

### Complete code example: Radius measure

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
          'piechart',
          [
            {
              "qDef": {
                "qFieldDefs": [
                  "GirResult"
                ],
                "qFieldLabels": [
                  "Greens in regulation"
                ]
              }
            },
            "=Count(HoID)",
            "=Avg(Stableford)"
          ],
          {
            "showTitles": false
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
