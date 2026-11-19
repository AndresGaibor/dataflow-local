---
source: https://qlik.dev/changelog/212-override-properties-json/
last_updated: 2026-05-19T11:15:23+02:00
---

# qlik-embed property overrides for \`analytics/chart\`

> **Updated on May 19, 2026:** This feature is now available after an initial delay.

The new `override-properties___json` attribute on `<qlik-embed>` lets you modify how a chart
renders within a specific embed instance without altering the underlying object stored in the
Qlik app. It is the modern declarative equivalent of the
[Capability API `setOptions()` method](https://help.qlik.com/en-US/sense-developer/May2025/Subsystems/APIs/Content/Sense_ClientAPIs/CapabilityAPIs/VisualizationAPI/setOptions-method.htm).

Supported on `analytics/chart` with `preview="true"`.

```html
<qlik-embed
  ui="analytics/chart"
  app-id="<APP_ID>"
  object-id="<OBJECT_ID>"
  preview="true"
  override-properties___json="{title:'New title'}"
></qlik-embed>
```

In this example, the chart's title will be overridden with "New title" when rendered
in preview mode.

For the full property schema reference, patch behavior, and details on discovering overridable
properties per chart type, see [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/).
