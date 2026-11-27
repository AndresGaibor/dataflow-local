---
title: "The in-application lineage summary view"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/chart-lineage-consumer-view.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with lineage and impact analysis in Analytics", "Analyzing lineage in Analytics"]
---

# The in-application lineage summary view

Analytics consumers and casual business users can access a consumer summary view of field-level dependencies directly from an analytics chart in a tabular view that lists dependencies for the field used in the chart.

Lineage summary view

![Lineage summary view opens to show details and dependencies](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineageSummary_Dependencies.png "Click to view full size")

While the more detailed lineage graph is available, casual analytics users can access summary information for associated objects that include: applications, links, datasets, tables, fields, dimensions, and measures. You can easily get an explanation of where the data came from within a chart with the lineage summary view.

This view lists details and dependencies for measures and dimensions in the chart. These include the Expression that calculates the measure or dimension, the fields that are being used in the expression, and the data sources where the fields came from.

## Activating the view for consumers

Application developers can change chart settings for the lineage consumer summary view to be visible. These settings may not be on by default.

Do the following:

1. Open a sheet in edit mode, and open the properties panel.
2. Change one or both of these settings:

   - Under Appearance>General>turn on Show details.
   - Under Appearance>General>turn on Show expressions.

## Opening the lineage summary view

Do the following:

1. Right-click the visualization or click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
   Click ![Information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) Show details.
2. Click Show dependencies.

   The lineage summary view opens. Explore the items under the Dimension, Measure, Fields, and Sources sections. Expand expressions to view the underlying calculations.
3. For more details, select ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an item and open the applicable lineage link. The lineage graph opens, where you can view more information.

   For more information about the lineage graph, see [*Analyzing lineage in Analytics*](../Catalog/lineage.htm).

## Example: Viewing field dependencies and expressions in charts with lineage summary

For a walk-through of lineage analysis, see [Field-level lineage use cases](https://share.vidyard.com/watch/17bg3fny5xLck5eF6XJEKP).

As a casual business user, you are analyzing a line chart COGS per Month in an application and want to review the expression used to calculate the measure (Cost of Goods Sold) COGS per Month and which Fields and Sources are used in the chart. You make sure that Show details and Show expressions are turned on for the chart under the Appearance > General section of [properties](#glossary-0 "Glossary term"), then select switch to sheet analysis mode. Click Show dependencies.

Lineage summary view for a line chart: View expressions, fields, and sources

![Summary lineage view lists expressions and dependent fields and sources](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_Lineage_ViewDetails.png "Click to view full size")

The lineage summary view lists the measures and the dimensions that are represented in the chart. The expressions that create the measures and dimensions can also be viewed in a dropdown when you expand ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) these fields. You see that the measure is created by the expression: Sum (UnitCost\*Quantity). The fields (Quantity, UnitCost) in the expression are listed as field dependencies. You can select ![icon more actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view lineage for the two fields but in this case there is only one relay back to its ultimate source Dataset.xlsx, which is also listed as a source dependency in the lineage summary.

## Additional examples

For more examples related to the in-application lineage summary, and lineage generally, see [*Example use cases for analyzing lineage*](../Catalog/lineage.htm#Examples).

## Security and permissions

Access is always provided to dimensions and expressions. Links to lineage and dataset names display only when the user has access.

## Limitations

- The lineage summary view is not supported in Button and Map charts.
- The lineage summary view is not available in mobile mode.
