---
source: https://qlik.dev/embed/nebula/customize/visualizations/sn-word-cloud/
last_updated: 2025-07-08T16:09:30Z
---

# Creating Word clouds

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

The Word cloud provides a visual way to represent
text data, where each unique field value is shown once.
The relative size of these words (field values) can
be based on a measure value. Various customization
options like different shapes,fonts, layouts,
and color schemes are available.
It is included in the Visualization bundle.

Learn more about the [word cloud chart](https://qlik.dev/embed/foundational-knowledge/visualizations),
or review the [word cloud chart API specification](https://qlik.dev/apis/javascript/sn-word-cloud/).

![word cloud example](https://qlik.dev/_astro/sn-word-cloud.Cu2LfRrB.png)

```js
// Configure nucleus
const nuked = window.stardust.embed(app, {
  context: { theme: "light" },
  types: [
    {
      name: "qlik-word-cloud",
      load: () => Promise.resolve(window["sn-word-cloud"]),
    },
  ],
});

// Rendering a Sankey chart on the fly
nuked.render({
  type: "qlik-word-cloud",
  element: document.querySelector(".wordCloud"),
  fields: [
    "Product Type",
    "=Sum(Sales)",
  ],
});
```

## Requirements

Requires `@nebula.js/stardust` version `2.0.0` or later.

## Installing

If you use npm: `npm install @nebula.js/sn-word-cloud`.
You can also load through the script tag directly from
[https://unpkg.com](https://unpkg.com/@nebula.js/sn-word-cloud).
