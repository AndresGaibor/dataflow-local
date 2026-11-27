---
title: "Creating visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/create-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations"]
---

# Creating visualizations

You create [visualizations](#glossary-0 "Glossary term") on a [sheet](#glossary-1 "Glossary term") by clicking ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to the right or bottom of the grid.

For instructions on creating specific types of visualizations, see the subsequent pages in this section.

Do the following:

1. Drag the visualization from the assets panel onto the sheet, or double-click the visualization.
2. Drag and drop fields or master items from Assets under Fields and Master items. Alternatively, click Add and then select them from the list.

   If you want to build a dimension or measure using an expression, add them under Data in the properties panel.
3. Optionally, to add filters:

   1. Click Add under Filters.
   2. Select the filter type and set any additional filter parameters.

   For more information about filters, see [*Applying filters to visualizations*](../Sheets/visualization-filters.htm).
4. Optionally, to change how the chart is sorted, in Sorting drag the fields into the desired sort order and optionally change how the fields are sorted.
5. Adjust the presentation of the visualization in the properties panel.

   For more information, see [*Changing the appearance of a visualization*](change-appearance-of-visualization.htm).

Tip noteYou can also add a visualization by copying visualizations. This is useful if you want to use existing visualization settings in another visualization type. For more information, see [*Copying a visualization from an existing visualization*](copy-visualization.htm)

Custom objects are added in a similar manner. You start creating a visualization by dragging a visualization extension onto the sheet. For more information, see [*Creating a visualization using a custom object*](create-visualization-extensions.htm).

You can use tab containers to save space on your dashboard, by quickly switching between tabs with different visualizations. For more information, see [*Tab container*](Container/container-object.htm).

The types of data you have in your tables and fields impacts whether they can be used as [dimensions](#glossary-2 "Glossary term") or [measures](#glossary-3 "Glossary term").

- Dimensions determine how the data in a visualization is grouped. For example: total sales per country or number of products per supplier. For more information, see [*Data grouping with dimensions*](../Dimensions/dimensions.htm).
- Measures are calculations used in visualizations, typically represented on the y-axis of a bar chart or a column in a table. Measures are created from an expression composed of aggregation functions, such as Sum or Max, combined with one or several fields. For more information, see [*Measures*](../Measures/measures.htm).

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
- [How do I create visualizations?](/lnk/How_do_I_create_visualizations)
- [How do I use the chart suggestions toggle?](/lnk/How_use_chart_suggestions)
- [How do I configure charts using the simplified authoring interface?](/lnk/How_configure_charts_simplified_authoring)
