---
source: https://qlik.dev/embed/capability-api/customize/visualizations/create-distributionplot/
last_updated: 2025-10-31T14:06:52+01:00
---

# Creating distribution plot charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

This section describes how to create distribution plots with the Visualization
API.

## Creating a basic distribution plot

In this example, you will create a basic distribution plot, containing one
dimension and two measures, with a custom title and horizontal orientation.

1. Create the chart.

   Create the container for the chart. The visualization type is `distributionplot`.

   ```js
   app.visualization.create(
     'distributionplot',
     [],
     {}
   )
   ```

2. Define the dimension.

   Define the dimension as a column.

   ```js
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
     }
   ]
   ```

3. Define the measures.

   Define the measures as columns.

   ```js
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

4. Define the title in the options.

   Next, define the title and the orientation in the options.

   ```json
   {
     "showTitles": true,
     "title": "Net score result per hole"
   }
   ```

Result

![Example of distribution plot](https://qlik.dev/_astro/on-the-fly-example-distributionplot-01-general.Bh4G5PKD.png)

### Complete code example: Basic distribution plot

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
          'distributionplot',
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
          ],
          {
            "showTitles": true,
            "title": "Net score result per hole"
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Presentation and color settings

In the example, you will change the way the distribution plot is presented by
adding narrow grid line spacing and customizing the colors. All these changes
are set in the options.

1. Add narrow grid line spacing.

   Changes to the grid line spacing is set in the `gridlines` object. Disable auto
   grid lines and set spacing to 3 which means narrow.

   ```json
   "gridlines": {
     "auto": false,
     "spacing": 3
   }
   ```

2. Add custom colors to the chart.

   You can set the presentation colors of the distribution plot: box color and
   point color. They are defined in the color object and each array consists of
   a `paletteColor` definition where you set the actual color as an index number
   in the palette or as a HEX string color.

   This example use colors that are not in the default palette, defined by
   "index": −1. The box color is a lighter shade of blue (`"color": "#68b5de"`)
   while the point color is a darker shade of blue (`"color": "#3a7391"`).

   ```json
   "color": {
     "box": {
       "paletteColor": {
         "index": -1,
         "color": "#68b5de"
       }
     },
     "point": {
       "auto": false,
       "paletteColor": {
         "index": -1,
         "color": "#3a7391"
       }
     }
   }
   ```

Result

Example of distribution plot with color settings

![Example of distribution plot with color
settings](https://qlik.dev/_astro/on-the-fly-example-distributionplot-02-presentation-color.Bl3PVuPu.png)

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
          'distributionplot',
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
          ],
          {
            "showTitles": true,
            "title": "Net score result per hole",
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "color": {
              "box": {
                "paletteColor": {
                  "index": -1,
                  "color": "#68b5de"
                }
              },
              "point": {
                "auto": false,
                "paletteColor": {
                  "index": -1,
                  "color": "#3a7391"
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

## Dimension and measure axis settings

In this example, you will define how the measure axis is presented. This is set
in the `measureAxis` object. If more than one dimension is used, the dimension
axis settings are defined in the dimensionAxis object. This example display
labels only on the measure axis . The axis also has narrow spacing and a custom
range. The visualization consists of only one dimension so no dimension axis
settings are needed.

1. Set the labels and spacing.

   Set to display labels only on the measure axis: `"show": "labels"`.

   Define that narrow spacing should be used: `"spacing": 0.5`.

   ```json
   "measureAxis": {
     "show": "labels",
     "dock": "near",
     "spacing": 0.5
   }
   ```

2. Customize the range.

   Enable custom range by setting `"autoMinMax": false`. Set the mode to display
   `"minMax": "minMax"` and then define the minimum and maximum values (0 and 1100).

   ```json
   "measureAxis": {
     "show": "labels",
     "dock": "near",
     "spacing": 0.5,
     "autoMinMax": false,
     "minMax": "minMax",
     "min": 0,
     "max": 1100
   }
   ```

Result

![Example of distribution plot with
dimension and measure axis settings](https://qlik.dev/_astro/on-the-fly-example-distributionplot-03-axis.qNnAENrt.png)

### Complete code example: Dimension and measure axis settings

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
          'distributionplot',
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
          ],
          {
            "showTitles": true,
            "title": "Net score result per hole",
            "gridlines": {
              "auto": false,
              "spacing": 3
            },
            "color": {
              "box": {
                "paletteColor": {
                  "index": -1,
                  "color": "#68b5de"
                }
              },
              "point": {
                "auto": false,
                "paletteColor": {
                  "index": -1,
                  "color": "#3a7391"
                }
              }
            },
            "measureAxis": {
              "show": "labels",
              "dock": "near",
              "spacing": 0.5,
              "autoMinMax": false,
              "minMax": "minMax",
              "min": 0,
              "max": 1100
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>

## Multiple lines using inner and outer dimensions

In this example, you will add a second dimension which gives you one line for
each value of the second (or outer) dimension.

1. Add the outer dimension as a column.

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

2. Define the dimension axis.

   Since you now have two dimensions, you can configure the dimension axis. This
   example show labels only for the outer dimension.

   ```json
   "dimensionAxis": {
     "show": "labels"
   }
   ```

3. Add sorting.

   For distribution plots, sorting is done in the sorting object inside the
   options. This example is sorted alphabetically in descending order.

   ```json
   "sorting": {
     "autoSort": false,
     "sortCriteria": {
       "sortByAscii": -1,
       "sortByLoadOrder": 1
     }
   }
   ```

Result

![Example of distribution plot with
dimension and measure axis settings](https://qlik.dev/_astro/on-the-fly-example-distributionplot-04-outer-dimension.OCQcSjap.png)

### Complete code example: Multiple lines using inner and outer dimensions

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
          'distributionplot',
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
                "qLabel": "Occurancies",
                "qDef": "Count(HoID)",
                "qNumFormat": {
                  "qType": "F",
                  "qnDec": 2,
                  "qUseThou": 0
                }
              }
            }
          ],
          {
            "showTitles": true,
            "title": "Net score result per hole and year",
            "gridlines": {
              "auto": true,
              "spacing": 2
            },
            "color": {
              "box": {
                "paletteColor": {
                  "index": -1,
                  "color": "#68b5de"
                }
              },
              "point": {
                "paletteColor": {
                  "index": -1,
                  "color": "#3a7391"
                }
              }
            },
            "measureAxis": {
              "show": "labels",
              "dock": "near",
              "spacing": 1,
              "autoMinMax": true
            },
            "dimensionAxis": {
              "show": "labels"
            },
            "sorting": {
              "autoSort": false,
              "sortCriteria": {
                "sortByAscii": -1,
                "sortByLoadOrder": 1
              }
            }
          }
        ).then((vis)=>{
          vis.show("QV01");
        });
      });
      ```
    </details>
