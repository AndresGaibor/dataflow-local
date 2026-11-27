---
title: "Grid chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/grid-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Grid chart

The grid chart (Grid chart) uses symbols of varying size sorted in a grid.

Information noteGrid chart is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

Grid charts must have two [dimensions](#glossary-0 "Glossary term") and one [measure](#glossary-1 "Glossary term"). The dimension values are the x and y axes. The measure is the metric that determines the size of the symbol in each crossing.

Grid chart with circles. Circle color is set by dimension (Quarter) and circle size is based on measure (Sum of Sales)

![Grid chart showing different coloured circles. Colours represent quarter, size of circle represents sales.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gridchart.png "Click to view full size")

## When to use the grid chart

A grid chart is useful when you need to quickly find measure values that stand out from other values. For example: you want to see which products sell well in some months, but poorly in others.

Grid charts do not work well when the measure has:

- Many duplicate values.
- Values that are numerically close to each other.

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

- The Number of axis values setting in the property panel has a limit of 55 per axis.
- Sometimes when you set dimension limits on a grid chart, chart labels will incorrectly display more items than requested.
- When coloring by dimension is used in this chart, a maximum of 100 unique dimension values and 100 unique colors can be plotted on the legend.

Related learning:

- [How do I configure a Visualization Bundle Grid Chart?](/lnk/How_configure_vizbundle_grid)
