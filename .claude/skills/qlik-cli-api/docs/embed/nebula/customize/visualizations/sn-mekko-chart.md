---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-mekko-chart/
last_updated: 2025-07-08T16:09:30Z
---

# Creating mekko charts

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

A basic mekko chart supernova aimed to be used in [nebula.js](https://github.com/qlik-oss/nebula.js).

Learn more about the [mekko chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [mekko chart API specification](https://qlik.dev/apis/javascript/sn-mekko-chart/).

![mekko chart example](https://qlik.dev/_astro/sn-mekko-chart.B75lxvz5.png)

```js

import { embed } from '@nebula.js/stardust';
import mekko from '@nebula.js/sn-mekko-chart';

// 'app' is an enigma app model
const embeddable = embed(app, {
  types: [{ // register the mekko chart
    name: 'mekko',
    load: () => Promise.resolve(mekko);
  }]
});

embeddable.render({
  element,
  type: 'mekko',
  fields: ['Region', 'Fiscal Year', '=Sum(Sales)'],
});
```

## Requirements

Requires `@nebula.js/stardust` version `>=1.7.0`.

## Installing

If you use npm: `npm install @nebula.js/sn-mekko-chart`. You can also load through the script tag directly from any of
the CDNs that supports NPM packages, for example: [unpkg](https://unpkg.com/@nebula.js/sn-mekko-chart).

## More examples

### Color by dimension

In this example the first dimension (Region) is used to color each cell.

![mekko chart color by first dimension example](https://qlik.dev/_astro/sn-mekko-chart-color-by-dim.CYJvPdkC.png)

```js
embeddable.render({
  element,
  type: "mekko",
  fields: ["Region", "Fiscal Year", "=Sum(Sales)"],
  properties: {
    cellColor: {
      mode: "byDimension",
      byDimension: { type: "index", typeValue: 0 },
    },
  },
});
```
