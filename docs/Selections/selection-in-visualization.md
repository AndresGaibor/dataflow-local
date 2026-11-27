---
title: "Types of selections in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/selection-in-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring data with visualizations"]
---

# Types of selections in visualizations

When you analyze your data, you have different ways of making selections. The following selections are available:

- [*Click selection*](click-selection.htm)
- [*Draw selection*](draw-selection.htm)
- [*Range selection*](range-selection.htm)
- [*Lasso selection*](lasso-selection.htm)
- [*Legend selection*](legend-selection.htm)
- [*Label selection*](label-selection.htm)

## Available selections by visualization type

The charts and tables have different selection patterns. Some selection types are particularly useful for certain visualizations. The following table displays which kinds of selections that are supported in the visualizations.

Selections that are supported in the visualizations

| Visualizations | Click selection | Draw selection | Range selection | Lasso selection | Legend selection | Label selection |
| --- | --- | --- | --- | --- | --- | --- |
| Bar chart | Yes | Yes | Yes | Yes | Yes | Yes |
| Box plot | Yes | Yes | Yes | Yes | No | Yes |
| Combo chart | Yes | Yes | Yes | Yes | Yes | Yes |
| Distribution plot | Yes | Yes | Yes | Yes | Yes | Yes |
| Filter pane | Yes | Yes | No | No | No | No |
| Gauge | No | No | No | No | No | No |
| Histogram | Yes | Yes | Yes | Yes | No | No |
| KPI | No | No | No | No | No | No |
| Line chart | Yes | Yes | Yes | Yes | Yes | Yes |
| Map | Yes | Yes | No | Yes | Yes | No |
| Pie chart | Yes | Yes | No | Yes | Yes | Yes |
| Pivot table | Yes | Yes | No | No | No | No |
| Scatter plot | Yes | Yes | Yes | Yes | No | No |
| Straight table | Yes | Yes | No | No | No | No |
| Table | Yes | Yes | No | No | No | No |
| Text & image | No | No | No | No | No | No |
| Treemap | Yes | Yes | No | Yes | No | No |
| Waterfall chart | No | No | No | No | No | No |
| Write table | Yes | Yes | No | No | No | No |

## Limitations

- You cannot make selections in Gauge, KPI, Waterfall chart, and Text & image visualizations.
- Legend selection is not available in a visualization when coloring by expression.
- Range selection is only available on the dimension axis for stacked bar charts or combo charts, and box plots.
- You cannot select a measure by name.
