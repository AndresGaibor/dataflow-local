---
title: "Visualization support for coloring methods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/color-method-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Changing the appearance of a visualization", "Coloring a visualization"]
---

# Visualization support for coloring methods

Not all Qlik Sense [visualizations](#glossary-0 "Glossary term") support the same coloring options. Additionally, some visualization types have specific behaviors or limitations when using certain coloring methods.

Color methods supported by visualizations and their limitations are determined primarily by the kinds of data the visualizations displays. For example, visualizations that only support displaying [measures](#glossary-1 "Glossary term") cannot be colored by [dimension](#glossary-2 "Glossary term") or through using master dimensions.

## Color method support by visualization

The following table outlines color method support by visualization type.

Color methods that are supported in the visualization

| Visualizations | Single | Multicolor | Master measure | Master dimension | Dimension | Measure | Expression |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bar chart | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Box plot | Yes | - | - | - | - | - | - |
| Combo chart | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Distribution plot | Yes | - | - | - | - | - | - |
| Filter pane | - | - | - | - | - | - | - |
| Gauge | Yes | Yes | Yes | - | - |  | - |
| Histogram | Yes | - | - | - | - | - | - |
| KPI | Yes | Yes | - | - | - | - | - |
| Line chart | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Map | Yes | - | - | Yes | Yes | Yes | Yes |
| Pie chart | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Pivot table | - | - | - | - | - | - | Yes |
| Scatter plot | Yes | - | - | Yes | Yes | Yes | Yes |
| Table | - | - | - | - | - | - | Yes |
| Text & image | - | - | - | - | - | - | - |
| Treemap | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

## Visualization coloring limitations and behaviors

Different visualizations have different behaviors with the methods of setting color in visualizations. This section outlines specific considerations when coloring different visualizations.

Line chart

Line charts do not support coloring by measure if they have two or more dimensions.

Map

Colors assigned to master dimensions that contain geopoint data or area data (polygons of geopoints) cannot be used to color a map.

Pie chart

Pie charts do not use [master item](#glossary-3 "Glossary term") colors when Auto is selected under Colors and legend.
