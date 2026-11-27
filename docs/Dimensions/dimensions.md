---
title: "Data grouping with dimensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/dimensions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Data grouping with dimensions

Dimensions determine how the data in a visualization is grouped. For example: total sales per country or number of products per supplier. You typically find a dimension as the slices in a pie chart or on the x-axis of a bar chart with vertical bars.

Dimensions are created from fields in the data model tables.

Example:

Product Type is a [field](#glossary-0 "Glossary term") in the Product table that is loaded into the application. The values of this field are the different types that products are grouped into.

You can, for example, create a bar chart to visualize the cost of each type, by adding the Product Type dimension to the chart. To complete the [visualization](#glossary-1 "Glossary term"), you must add a [measure](#glossary-2 "Glossary term") (in this case Cost), which is grouped by the Product Type dimension.

Bar chart with the dimension Product Type and measure Cost.

![Bar chart.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChart2.png "Click to view full size")

You can also create different types of master dimensions:

- [*Drill-down groups*](drill-down-groups.htm)
- [*Cyclic dimensions*](cyclic-dimension.htm)

## Creating dimensions

When you load data into an application, all data is loaded as fields. At the same time, Qlik Sense identifies the fields from the data model that can be used as dimensions. These are shown to you as you populate visualizations with data or create master items.

The process of creating a dimension depends on whether you want to customize how data is grouped. Follow these guidelines:

- To simply use a certain field to group data in your visualization, add the field as a dimension when you create the visualization. No additional configuration is needed.
- Create a master dimension in the application if you want to:

  - Create a standalone entity in the application that is easily recognized as a useful way to group data.
  - Enhance and expand how the dimension fields group data. For example, you can create a drill-down or cyclic dimension for specific behavior, or set a specific color for the dimension.
  - Allow re-use of the dimension across the application, including by others.

  After creating the master dimension, it can be added to any applicable charts as you configure them.

  [*Reusing dimensions with master dimensions*](create-master-dimension.htm)

## Learn more

- [*Fields*](../DataSource/fields.htm)
- [*Measures*](../Measures/measures.htm)
- [*Reusing dimensions with master dimensions*](create-master-dimension.htm)
- [*Creating a master dimension from the data model viewer*](create-master-dimension-from-data-model-viewer.htm)
- [*Deleting a master dimension or master measure*](../Assets/delete-master-dimension-measure.htm)
- [What is a dimension?](/lnk/What_is_dimension)
- [Understanding dimensions and measures](/lnk/Understand_Dimensions_Measures_QS)

Related learning:

- [What is a dimension?](/lnk/What_is_dimension)
- [Understanding dimensions and measures](/lnk/Understand_Dimensions_Measures_QS)
