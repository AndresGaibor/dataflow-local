---
title: "Measures"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/measures.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Measures

Measures are calculations used in visualizations, typically represented on the y-axis of a bar chart or a column in a table. Measures are created from an expression composed of aggregation functions, such as Sum or Max, combined with one or several fields.

A measure must have a name, and may also be supplied with descriptive data such as description and tags.

Example:

You can, for example, create a bar chart to visualize the cost of each type, by adding the Product Type [dimension](#glossary-0 "Glossary term") to the [chart](#glossary-1 "Glossary term"), and the measure Cost, which is made from the expression Sum(Cost), that is the result of the calculation of the [aggregation](#glossary-2 "Glossary term") function Sum over the [field](#glossary-3 "Glossary term") Cost. The results are grouped by the Product Type dimension.

Bar chart with the dimension Product Type and the measure Cost.

![Bar chart.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChart2.png "Click to view full size")

## Creating measures

When you load data into an application, all data is loaded as fields. When you add a measure to a chart or create a master measure, these fields can be used in aggregations to perform specific calculations.

The process of creating a measure depends on whether you want to customize or standardize a particular calculation. Follow these guidelines:

- To simply add a calculation to a chart, enter the measure expression when configuring the chart. No additional configuration is needed.
- Create a master measure in the application if you want to:

  - Create a standalone entity in the application that is easily recognized as a useful calculation.
  - Enhance and expand the definitions of a calculation. For example, you can define colors and label expressions so they are added whenever the measure is used, rather than configuring these properties separately in each instance.
  - Allow a centralized definition of a measure, so a change in the central definition will propagate through the application to all objects where the measure is referenced.
  - Allow re-use of the measure across the application, including by others.

  After creating the master measure, it can be added to any applicable charts as you configure them.

  [*Reusing measures with master measures*](create-master-measure.htm)

## Learn more

- [*Fields*](../DataSource/fields.htm)
- [*Data grouping with dimensions*](../Dimensions/dimensions.htm)
- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
- [*Reusing assets with master items*](../Assets/work-with-master-items.htm)
- [*Creating a master measure from the data model viewer*](create-master-measure-data-model-viewer.htm)
- [What is a measure?](/lnk/What_is_measure)
- [Understanding dimensions and measures](/lnk/Understand_Dimensions_Measures_QS)

Related learning:

- [What is a measure?](/lnk/What_is_measure)
- [Understanding dimensions and measures](/lnk/Understand_Dimensions_Measures_QS)
