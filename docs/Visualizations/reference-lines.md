---
title: "Reference lines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/reference-lines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Reference lines

A reference line is a line intersecting the [chart](#glossary-0 "Glossary term") area from a given point on the [measure](#glossary-1 "Glossary term") axis.

For information about how to create reference lines, see [*Adding reference lines to visualizations*](add-trend-and-reference-lines.htm#AddRefLine).

You can use a reference line to indicate a certain level of chart data. The reference line is only drawn if it falls within the current range of the measure axis. You can have several reference lines in the same chart.

Bar chart Top 5 customers with a reference line at 5M.

![Bar chart with a reference line.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ReferenceLine.png "Click to view full size")

Reference lines are available in the following visualization types:

- Bar chart
- Box plot
- Combo chart
- Distribution plot
- Gauge
- Histogram
- Line chart
- Scatter plot
- Waterfall chart

## Reference line expression

You can either set the reference line expression to an absolute numeric value, or enter an arbitrary numeric expression.

## Dimensional reference lines

You can also add reference lines along the [dimension](#glossary-2 "Glossary term") axis. Both continuous and discrete axes are supported. It is possible to enter text values for discrete dimensional axes, and numerical values or expressions for continuous axes. On a time axis it is possible to enter an expression that gives a time-based result like a date or a month.

Line chart average sales per month, with a reference line at 3.5k and a dimensional reference line in September.

![Line chart with reference and dimensional reference lines.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ReferenceLine2.png.png "Click to view full size")

Dimensional reference lines are available in the following visualization types:

- Bar chart
- Combo chart
- Line chart

## Learn more

- [*Adding trend and reference lines to visualizations*](add-trend-and-reference-lines.htm)
- [How to create a dimension reference line](/lnk/How_create_dimension_reference_line)

Related learning:

- [How to create a dimension reference line](/lnk/How_create_dimension_reference_line)
