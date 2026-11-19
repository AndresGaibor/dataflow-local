---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-map/
last_updated: 2025-07-08T16:09:30Z
---

# Creating map charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Maps enable you to view your data geographically. Maps have many ways to present your data.
You can add multiple layers to your map to display different types of information on the same map.
You can set a custom scope for locations so that if two locations have the same name,
you display the locations and their data correctly.
You can add custom base maps to your map and use non-WGS-84 coordinates.

Learn more about the [map chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [GitHub repository](https://github.com/qlik-oss/sn-map).

![map example](https://qlik.dev/_astro/sn-map.BY0XIT1l.png)

## Layers

- Point layer: A point layer overlays individual locations on a map, representing them with shapes.
- Geodata layer: A geodata layer enables you to display a custom base map for your map visualization.

More details can be found in the `docs` folder of the `sn-map`
repository: [https://github.com/qlik-oss/sn-map](https://github.com/qlik-oss/sn-map)

## Requirements

Requires `@nebula.js/stardust` version `2.3.0` or later.

## Installing

If you use npm: npm install `@nebula.js/sn-map`

## Usage

```js
import { embed } from '@nebula.js/stardust';
import map from '@nebula.js/sn-map';

// 'app' is an enigma app model
const nuked = embed(app, {
  types: [
    {
      // register the map
      name: 'map',
      load: () => Promise.resolve(map),
    },
  ],
});

// Rendering a map on the fly
// Best way is to make a sn-map extension in the client and copy the properties
// You will need add the serverUrl and serverKey to the options
nuked.render({
  type: 'map',
  element,
  options: {
    configuration: { serverUrl: ...,  serverKey: ... }
  },
  properties: {
    ...
  },
});
```

## Options

- configuration
  - serverUrl - host URL for map server.
  - serverKey - key for map server.

## Examples

### Map with a point layer

![map example - point layer](https://qlik.dev/_astro/sn-map-point-layer.DAPDOhDK.png)

```js
nuked.render({
  type: 'map',
  element,
  options: {
    configuration: {
      serverUrl: ... ,
      serverKey: ... ,
    },
  },
  properties: {
    gaLayers: [
      {
        type: 'PointLayer',
        qHyperCubeDef: {
          qDimensions: [
            {
              qDef: {
                qFieldDefs: [
                  'id'
                ],
              },
              qAttributeExpressions: [
                {
                  qExpression: 'latitude',
                  id: 'locationOrLatitude'
                },
                {
                  qExpression: 'longitude',
                  id: 'longitude'
                }
              ],
            }
          ],
          qMeasures: [],
          qInitialDataFetch: [
            {
              qLeft: 0,
              qTop: 0,
              qWidth: 1,
              qHeight: 10000
            }
          ],
        },
        size: {
          radiusMin: 4,
          radiusMax: 12,
        },
        color: {
          mode: 'primary',
          paletteColor: {
            index: 9,
            color: '#f8981d'
          },
        },
        locationOrLatitude: {
          key: 'latitude',
          type: 'expression'
        },
        isLatLong: true,
        id: 'tWTdanX'
      }
    ],
    mapSettings: {
      showScaleBar: true,
    },
  },
});
```

### Map with a wms geodata layer

![map example - web map service layer](https://qlik.dev/_astro/sn-map-wms-layer.CahkGLPX.png)

```js
nuked.render({
  type: "map",
  element,
  properties: {
    gaLayers: [
      {
        type: "GeodataLayer",
        dataType: "tms",
        wms: {
          url: "https://nowcoast.noaa.gov/arcgis/services/nowcoast/analysis_meteohydro_sfc_qpe_time/MapServer/WmsServer",
          version: "1.1.0",
          hasWmsLoaded: true,
          selectedCrs: "EPSG:3857",
          selectedFormat: "PNG",
          capabilities: {
            layers: [
              {
                name: "1",
                title: "Image",
                selected: true,
              },
              {
                name: "2",
                title: "Image Footprints with Time Attributes",
                selected: true,
              },
              {
                name: "3",
                title: "Boundary",
                selected: true,
              },
            ],
            transparent: true,
          },
        },
        id: "bKgjAA",
      },
    ],
    mapSettings: {
      showScaleBar: true,
    },
  },
});
```
