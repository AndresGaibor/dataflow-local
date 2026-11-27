---
title: "Text definition placeholders for native PixelPerfect charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-text-definition-placeholders.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report", "Creating native PixelPerfect charts"]
---

# Text definition placeholders for native PixelPerfect charts

As you configure a native PixelPerfect chart, specific placeholders can be added to values for text properties, such as for legends and labels.

Text definition placeholders

| Placeholder value | Output value | Further considerations |
| --- | --- | --- |
| {S} | Series name | - |
| {A} | Argument value for a series | - |
| {V} | Point values for the series | Relevant for Pie and Donut chart series. |

## Common uses

For PixelPerfect charts created with user-defined series, here are some examples of where these placeholders might be needed in the Chart Designer:

- Properties > Legend Text Pattern
- Properties > Label > Text Pattern

For PixelPerfect charts created with series templates, here are some examples of where these placeholders might be needed in the Chart Designer:

- Properties > Series Template > Legend Text Pattern
- Properties > Series Template > Label > Text Pattern

## Learn more

- [*Creating a PixelPerfect chart with user-defined series*](pixelperfect-native-chart-simple.htm)
- [*Creating a PixelPerfect chart with automated series splitting*](pixelperfect-native-chart-auto-split.htm)
