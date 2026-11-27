---
title: "Pivot table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/PivotTable/pivot-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Pivot table

The pivot table presents [dimensions](#glossary-0 "Glossary term") and [measures](#glossary-1 "Glossary term") as rows and columns in a table. In a pivot table you can analyze data by multiple measures and in multiple dimensions at the same time.

You can rearrange measures and dimensions by pivoting rows and columns.

Information noteWhen sorting pivot tables, NULL values are always displayed first.

## When to use the pivot table

The pivot table is useful when you want to include several dimensions or measures in a single table, and then want to reorganize them to see different subtotals.

### Advantages

The pivot table is very powerful when you want to analyze multiple dimensions and measures at once, and then reorganize them to get a different perspective on your data. You can expand the rows you are interested in while keeping the rows in the rest of the table collapsed.

### Disadvantages

The pivot table may seem a bit complicated, and does not give insights at a glance.+

## Pivoting your data in the table

When you want to rearrange your data, drag the items to a new column or row.

In the following pivot table, the dimension Customer has been dragged to the position after Product Group. The dimension Item Desc has been moved to the position before Product Group. As a consequence, the dimensions are now sorted by Item, primarily. Focus has shifted from Customer to Item Desc. You can find out the quantities and sales for each customer by clicking ![Plus icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg). This will expand a dimension.

![Pivot table with rearranged data.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotTableExample2.png)

By moving the dimension Customer from rows to columns, you retain focus on the dimension Item Desc, but you also get the distribution of items per customer. The move has made the pivot table more information dense.

![Pivot table with rearranged data.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotTableExample3.png)

### Measure grouping

As you may have noticed, Quantity and Sales are not presented as separate measures in the top column row. Next to the dimension Customer, you find an item called Values. When you use more than one measure, they are automatically grouped together forming a measure group, Values. This group can be added to the rows section or the columns section. The measure group cannot be edited or selected in the table. You cannot split up the measure item and use one measure as a row and another as a column.

You can use the properties panel to sort by the first measure in the group, see [Sort by first measure](#Sort).

## Learn more

- [*Creating pivot tables*](create-pivot-tables.htm)
- [*Comparing straight tables and pivot tables*](pivot-table-example.htm)
- [Interpreting Pivot Tables](/lnk/Interpreting_pivot_tables)

Related learning:

- [Interpreting Pivot Tables](/lnk/Interpreting_pivot_tables)
