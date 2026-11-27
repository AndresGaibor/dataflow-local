---
title: "P&L pivot chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/pl-pivot-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy"]
---

# P&L pivot chart

You can use the P&L pivot chart to create a pivot table with a layout for profit and loss reporting. You can color cells according to performance and style the chart with custom fonts and alternating row colors. You can also download the chart to Excel including formatting.

Information noteP&L pivot is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

![A P&L pivot chart showing many dimensions and measures.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_pl_pivot.png)

P&L pivot chart dimensions and measures

| Dimensions | Measures | Result |
| --- | --- | --- |
| 1 [dimension](#glossary-0 "Glossary term") | up to 9 measures | A table with one row for each dimension value and one column for each [measure](#glossary-1 "Glossary term"). |
| 2 dimensions | up to 8 measures | A pivot table with one row for each value of the first dimension and one column for each measure pivoted using the second dimension. |

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

- There is a limitation for data transfer between Qlik Engine and P&L pivot. This limits each request for data to 10000 elements, for example, 1000 rows and 10 columns. P&L pivot can make automatic requests for more data using pagination.

  You can set the limit of how much data to request with Pagination > Max pagination loops. The default value is 20000 elements (20k cells) and the maximum value is 40000 elements.

  You can also modify the error message displayed to the user when the data limit is exceeded. The recommended workaround when the data limit is exceeded is to apply filters to the data to limit the data transfer.
- It is not possible to convert a P&L pivot chart to another visualization or convert another visualization to a P&L pivot chart.

Related learning:

- [How do I configure a Visualization Bundle P and L pivot chart?](/lnk/How_configure_Visualization_Bundle_P_L_pivot_chart)
