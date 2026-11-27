---
title: "Table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Table/table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy"]
---

# Table

The table shows several fields simultaneously, where the content of each row is logically connected. Typically, a table consists of one [dimension](#glossary-0 "Glossary term") and several [measures](#glossary-1 "Glossary term").

Information note

The Straight table has replaced the Table as the default table visualization. Consider upgrading existing tables to straight tables for improved functionality and performance. For information about the straight table, see [*Straight table*](../StraightTable/sn-straight-table.htm).

![Table visualization](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Table.png)

You only make selections in the dimension columns. All dimension columns have a search icon ![Search](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) in the header.

## When to use the table chart

Use a table when you want to view detailed data and precise values rather than visualizations of values. Tables are good when you want to compare individual values. Drill-down group dimensions are very efficient in tables. Within a limited space, you can drill down to the next level of detail and analyze the updated measure values.

### Advantages

You can filter and sort the table in different ways. Many values can be included in a table, and when you drill down in a table, you make good use of the limited space on a [sheet](#glossary-2 "Glossary term"). A table is excellent when you want to see exact values rather than trends or patterns.

### Disadvantages

If the table contains many values, it is difficult to get an overview of how values are related. It is also hard to identify an irregularity within the table.

## Display limitations

### Number of rows and columns

In a table, you can have millions of rows and virtually any number of columns with dimensions and measures. But because huge tables are impractical and hard to manage, the limit for what is practical is far less than the theoretical maximum. In most cases, it is desirable to see all the columns without scrolling horizontally.

### Tables with content of mixed sizes

In a table you can have both columns where the content fits on one row within the cell, and columns containing wrapped multiline text. In some cases you will see a shift in alignment and number of rows when the multiline column is scrolled in and out of view. When the view only contains content that fits on one row, the table will adjust and show all content on single line rows, which means more rows are displayed.

We recommend that you disable multiline text wrapping in these cases to avoid confusion for the user.

### Mobile limitations

In the Qlik Analytics mobile app, the table is a natively rendered visualization. Natively rendered visualizations have better performance compared to visualizations rendered in WebView. If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

## Learn more

- [*Creating tables*](create-tables.htm)
- [Interpreting Tables](/lnk/Interpreting_tables)

Related learning:

- [Interpreting Tables](/lnk/Interpreting_tables)
