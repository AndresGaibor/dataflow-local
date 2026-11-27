---
title: "KPI"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/KPI/KPI.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# KPI

The KPI [visualization](#glossary-0 "Glossary term") can show one or two [measure](#glossary-1 "Glossary term") values, and is used to track performance.

A KPI visualization with two measure values, using conditional colors and symbols.

![KPI visualization.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_KPI.png "Click to view full size")

## When to use the KPI

Use KPIs to get an overview of performance values that are central to an organization. Use color coding and symbols to indicate how the figures relate to the expected results.

### Advantages

KPIs give a quick understanding of the performance within an area.

### Disadvantages

The KPI is somewhat limited when it comes to graphical components. You can use symbols to help illustrate the performance, but if you want a more conspicuous component, consider using a gauge.

## Mobile limitations

In the Qlik Analytics mobile app, the KPI is a natively rendered visualization. Natively rendered visualizations have better performance compared to visualizations rendered in WebView. If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

## Learn more

- [*Creating KPIs*](create-kpis.htm)
- [Interpreting KPIs](/lnk/Interpreting_KPIs)

Related learning:

- [Interpreting KPIs](/lnk/Interpreting_KPIs)
