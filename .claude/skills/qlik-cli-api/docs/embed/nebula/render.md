---
source: https://qlik.dev/embed/nebula/render/
last_updated: 2026-06-02T18:15:45+01:00
---

# Overview - Rendering Qlik visualizations

nebula.js lets you embed and render Qlik Sense visualizations in your own web applications.
Using the `embed` function from `@nebula.js/stardust`, you can render charts from an existing
Qlik app, control their appearance and behavior, and expose the Qlik selection model directly
in your own UI.

This section covers the key areas of working with nebula.js visualizations:

- [Configuration](https://qlik.dev/embed/nebula/render/configuration/) -
  Set up the `Configuration` object to control themes, language, device type, and interaction
  constraints. Learn how to register chart types from npm or load them on the fly from a CDN.
- [Supported Charts](https://qlik.dev/embed/nebula/render/supported-charts/) -
  A reference matrix of which Qlik Sense charts are available in nebula.js, and which are
  supported by Insight Advisor and the Insight Advisor APIs.
- [Rendering](https://qlik.dev/embed/nebula/render/embedding-visualizations/) -
  Render existing app objects by ID, or create visualizations on the fly by specifying a type,
  fields, and initial properties.
- [Current app selections](https://qlik.dev/embed/nebula/render/app-selections/) -
  Mount a selections bar to surface the active selections from one or more connected apps.
- [Field selections](https://qlik.dev/embed/nebula/render/field-selections/) -
  Render a listbox for a specific field, allowing users to browse values and make selections
  outside of a chart.
- [Applying themes](https://qlik.dev/embed/nebula/render/applying-themes/) -
  Register and apply Qlik Sense themes to control colors, fonts, and palettes across all
  embedded charts. Includes guidance on CSS overrides for elements outside the chart boundary.
