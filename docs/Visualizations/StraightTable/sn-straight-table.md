---
title: "Straight table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Straight table

The Straight table shows several fields simultaneously, where the content of each row is logically connected. A table can consist of as many dimensions and measures as needed.

Application creators can add many fields simultaneously, customize the table at the column level, add alternative dimensions and measures, set column width, apply pagination, and turn on chart exploration.

The straight table offers flexible, accessible, and responsive data analysis, including the following features:

- Ease of use

  One-click interactive sorting and ability to drag and drop columns to reorder them without affecting chart defaults or sorting preferences.
- Accessibility and flexible configuration

  The straight table offers comprehensive keyboard navigation. It also has configurable settings for row-level pagination, screen reader support, and enhanced readability. Enhancements can be switched off if needed to add more mouse shortcuts into column headers. To learn more, see [*Managing accessibility settings*](sn-straight-table-appearance.htm#Accessibility).
- Performance

  The straight table optimizes performance for large data volumes.
- Unique features

  - Chart exploration allows users that do not have edit rights to customize the original straight table when they are in analysis mode. These users can add or remove columns, change sort order, re-arrange columns, and make selections. They can then share, download, subscribe, or bookmark the new table layout. The changes made in chart exploration mode by a user are not seen by other users analyzing the sheet.
  - Straight tables can also show subtotal rows for dimensions to summarize grouped values directly in the table.

Information noteThe straight table replaces the table as the default table visualization. For help with configuring existing instances of the table visualization, see [*Table*](../Table/table.htm).

## When to use the straight table

Use a straight table when you want to view detailed data and precise values rather than visualizations of values. Tables are good when you want to compare individual values. Drill-down group dimensions are very efficient in tables. Within a limited space, you can drill down to the next level of detail and analyze the updated measure values. Use this table when you want users to be able to create custom tables in analysis mode.

### Advantages

You can filter and sort the table in different ways. Many values can be included in a table, and when you drill down in a table, you make good use of the limited space on the sheet. A table is excellent when you want to see exact values rather than trends or patterns. Tables are an easy way to export data into other programs.

### Disadvantages

If the straight table contains many values, it is difficult to get an overview of how values are related. It is also hard to identify an irregularity within the table.

## Best practices for optimizing tables

If a table has too many dimensions and measures, it may load slowly. As a best practice, add the majority of your fields and expressions as Alternative columns. This encourages users to add only the fields they need using chart exploration.

You can also increase performance by ensuring a table has 10 columns or less.

Tables that extract fields from a single data source will perform better than tables that contain fields from multiple data sources.

## Selecting active fields from cyclic dimensions in straight tables

If a straight table uses a cyclic dimension, analyzers can select the active field from the cyclic dimension.

Do one of the following, depending on chart accessibility settings:

- Click ![Cyclic group](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cyclic_group_outline.svg) next to the column name, and select the dimension.
- Click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) on a cyclic dimension column, and then click ![Cycle](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) <Dimension name> and select a dimension from the cyclic dimension.

## Using chart exploration

Chart exploration mode is a great way to quickly remove or add data, and then share it, download it, or bookmark the new table state. It is available in the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu under ![Controls](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Chart exploration. Your application creator needs to turn this setting on for you to use it.

You use chart exploration in analysis mode. Add or remove columns from a table, re-sort columns, change column width, and apply selections. You cannot change the size or layout of the entire table on the sheet in chart exploration mode.

Tip note

The following actions are available in the panel header:

- ![Unselect all](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cleanse_outline.svg): Remove all currently selected columns from the table.
- ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reset_outline.svg): Reset all unsaved changes you made during analysis in the current session, including added or removed columns, sorting, column reordering, and more.
- ![Close exploration](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg): Close the panel.

If you customize a table using chart exploration mode, other users cannot see your changes, unless you save them as a public bookmark. This means that several users can alter the same table, at the same time. Your changes will remain visible to you until your session ends. When this occurs, the table will return to its default state, as set by the person who created the straight table. If you want to save your table layout, create a bookmark. For more information, see [*Creating bookmarks*](../../Bookmarks/create-bookmark.htm).

For a straight table customized through chart exploration or the exploration panel, a bookmark with Save layout restores column visibility and order for both dimensions and measures. Columns added to the table after you create the bookmark are included exploration panel in the restored layout when you apply the bookmark, but will be inactive.

The chart exploration panel is not shown in the resulting table that you have shared or downloaded.

For information about configuring chart exploration as an application creator, see [*Activating chart exploration in a straight table*](sn-straight-table-chart-exploration.htm).

Chart exploration of a straight table. The table has three columns: Customer, Region, City.

![Straight table in view mode, with chart exploration turned on.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_straighttable_chart-exploration.png "Click to view full size")

Chart exploration of the same table as above, but with two measures added to the table: Sales and Cost. The background colors are the result of an expression.

![Straight table in view mode, with chart exploration turned on.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_straighttable_chartexploration_edits.png "Click to view full size")

## Downloading a straight table

This section outlines details about downloading straight tables using special features that are unique to the straight table.

Straight tables can also be downloaded as standard images and PDFs, similar to other charts. For more information, see [*Downloading visualizations*](../../Download/downloading-visualization.htm#DownloadChart).

Information note

When downloading data from a table or pivot table, column- and cell-specific styling is not preserved. Dynamic colors, background colors, and images are not supported in chart data downloads.

### Downloading a straight table as data

When you download a straight table as data, you can choose to include the following in the downloaded Excel file:

- Titles, subtitles, and footnotes
- Column totals
- Current selections

Do the following:

1. In the hover menu, click ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg)Download.

   You can also click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download.
2. Select Data.
3. Under Export options, select the additional content you would like to include. Depending on the configuration of your chart, one or more of the following options might be available:
   - Titles: Include titles, subtitles, and footnotes.
   - Column totals: Include the row displaying totals at the top or bottom of the table.
   - Current selections: Include a list of selections applied in the application at the time when you download the table. A separate row is added for each field that has selections.
4. Click Download.

### Downloading a straight table as a multi-page PDF

You can download a straight table as a PDF document that spans multiple pages.

Information noteWhen you export a straight table as a PDF with Pages set to All, row height is adjusted to single lines. Therefore, the resulting PDF could have different image dimensions than the application sheet, and multi-line rows will be condensed to single lines.

Do the following:

1. In the hover menu, click ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download.

   You can also click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download.
2. Select PDF.
3. Select an Orientation.
4. Under Pages, select All.
5. Set the Scale.
6. Click Download.

## Limitations

### Chart exploration limitations

#### Chart exploration for straight tables added to containers

Chart exploration is not available if the table is embedded inside any of the following objects:

- An existing container object that has not been replaced with a tab container. The tab container became the native container object on November 5, 2024.

  Chart exploration is also not available in existing instances of the deprecated ShowHide container and Tabbed container objects. However, converting these objects to tab containers is not recommended. Instead, create a new tab container from scratch in order to access chart exploration in straight tables.

  For information about the tab container, see [*Tab container*](../Container/container-object.htm).
- Trellis container

  [*Trellis container*](../VisualizationBundle/trellis-container.htm)

#### Chart exploration for straight tables embedded in web pages

Chart exploration is not available for straight tables that are embedded in web pages.

### Number of rows displayed

If pagination is turned on, you can only display 100 rows at a time. If pagination is turned off, you can display up to 250 000 rows at a time. If your table has more than 250 000 rows, pagination will be applied.

Because huge tables are impractical and hard to manage, the limit for what is practical is far less than the theoretical maximum. In most cases, it is desirable to see all the columns without scrolling horizontally.

### Accessibility

The straight table is only fully accessible with certain settings activated. For more information, see [*Managing accessibility settings*](sn-straight-table-appearance.htm#Accessibility).

For more information on keyboard navigation, see [*Keyboard navigation and shortcuts in apps*](../../UserInterface/keyboard-navigation-and-shortcuts.htm).

## Learn more

- [*Creating straight tables*](create-sn-straight-tables.htm)
