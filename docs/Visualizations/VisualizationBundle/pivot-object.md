---
title: "Pivot"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/pivot-object.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Pivot

The pivot table (Pivot) presents [dimensions](#glossary-0 "Glossary term") and [measures](#glossary-1 "Glossary term") as rows and columns in a table. In a pivot table you can analyze data by multiple measures and in multiple dimensions at the same time.

Information notePivot is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

Pivot table, with expansions

![Pivot object showing Sales, Quantity, and Margin % as measures for Customers. Customers is expanded into Product Group and Product type, showing measure results for these categories.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_pivotobject.png "Click to view full size")

## When to use the pivot table chart

Pivot tables are useful when you want to include several dimensions or measures in a single table, and then want to reorganize them to see different subtotals. The Qlik Visualization bundle pivot table offers several different layout and styling options than the pivot table visualization, including:

- Headers for all dimensions
- Header menu options for all dimensions
- Custom null representation
- Customizable column widths by pixel or percentage
- Adjust column widths using mouse
- Totals at top or bottom
- Chart exploration (allows users to customize data and arrangement on the fly during analysis)
- Measure grouping

## Limitations

Pivot tables have the following limitations:

- You cannot pivot data in your Visualization bundle pivot table when your sheet is in analysis mode as you can with the visualization pivot table.
- Measure groups are only displayed when all measures are in the Columns section and there are no dimensions in the Columns section.
- Measure groups are not supported when downloading the chart as data.

## Learn more

- [*Creating pivot tables (Pivot)*](creating-pivot-object.htm)
