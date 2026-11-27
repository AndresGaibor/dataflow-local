---
title: "Configuring sorting in your write table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/sort.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Configuring sorting in your write table

You can adjust the sorting of a Write table in several ways:

- Column sorting: Adjust the order of the dimensions and measures from left to right.
- Row sorting: Adjust the sorting priority order of the rows.
- Internal sorting: Use the internal sorting order of dimensions and measures.
- Interactive sorting: During analysis, you can click on a column header to sort the table.

Information noteSorting in write tables is only available for dimension and measure columns. It is not available for editable columns.

## Column sorting

By default, the order in which columns are sorted is set by the order in which dimensions and measures are added to the table. If you add the measure Sales first, it is presented first (leftmost) in the table. The next dimension or measure that is added is presented in the second column, and so on. The column sorting order can be changed in the properties panel, under Columns.

## Row sorting

By default, rows are sorted by the first added dimension or measure, numeric values ascending, text values ascending. A small arrow under the column header shows by which column the table is sorted.

You can change the row sorting in the properties panel, under Sorting. Drag the dimensions and measures to change the sorting priority order. In many cases, sorting is not only affected by the first dimension or measure in Sorting, but also the following ones.

## Internal sorting

Each dimension and measure has a default (Auto) internal sorting order, which can be changed. Under Sorting, click the item you want to change and click the button to switch to Custom sorting. Changes made to the internal sorting of an item may not have any effect if the sorting is in conflict with an item with higher priority.

## Interactive sorting

During analysis, you can set which column to sort on by clicking the column header. Clicking the column header opens a menu in which sorting can be changed. You can select Sort ascending or Sort descending.

Interactive sorting is session-based and is not saved. If you want your changes to the sorting to be persistent, you need to make the changes in the properties panel.
