---
title: "Adding tabular data to report templates with Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/OfficeCommon/add-in-tabular-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Adding content to report templates with Qlik add-ins for Microsoft Office"]
---

# Adding tabular data to report templates with Qlik add-ins for Microsoft Office

You can add a chart from the analytics application in tabular format to your Excel, PowerPoint, or Word report template. You can add the content as entire tables or individual columns.

Tables tab in an add-in, allowing you to add a new table or re-visit a table that you have already added

![Using the add-in to manage tabular data objects](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_TablesTab.png "Click to view full size")

## Applies to

This content applies to the following types of Qlik Cloud report templates:

- Excel

  [*Qlik add-in for Microsoft Excel*](reporting-add-ins.htm#Excel)
- PowerPoint

  [*Qlik add-in for Microsoft PowerPoint*](reporting-add-ins.htm#PowerPoint)
- Word

  [*Qlik add-in for Microsoft Word*](reporting-add-ins.htm#Word)

## Behavior

### Supported charts

- Charts with straight type hypercubes can be used as tabular data in reports.
- When you add a chart as a table, the underlying fields representing the chart's data are added as columns to the report.
- Whether you add a chart as a single table tag or as single column tags, the underlying report object you create is usually a table.

### Excel templates

When you add a chart as tabular data in an Excel template, each column in the source table is generated as a separate column in the spreadsheet within the report output.

Because Excel is designed primarily for tabular data, there are a number of additional options and considerations for adding tabular data. See:

- [*Formatting properties for tabular data in Excel report templates*](../Excel/add-in-excel-tabular-properties.htm)
- [*Removing rows with the Deleterow tag*](../Excel/add-in-excel-deleterow.htm)
- [*Working with native Excel tables*](../Excel/add-in-excel-native-tables.htm)

### PowerPoint templates

When you add a chart as tabular data in a PowerPoint template, it is helpful to be aware of how many rows will be generated in the final output. If many rows are included, the generated content could spill outside of the bounds of the slide on which you place it.

### Word templates

In Word templates, when you are adding the object as a single tag and need to use custom Word formatting, you need to insert the tag within an existing single-cell table. This allows you to format the table using the native Word table design features. For more information, see [*Adding an entire chart*](#Adding3) and [*Keep source formats setting at the table level*](../Word/word-tabular-properties.htm#Keep).

Depending on how many columns are in the table you add to the Word template, the output may or may not be formatted as a Word table. If the table is a single column, it will be generated as a series of consecutive paragraph lines.

## Adding an entire chart

You can add an entire chart in tabular form with a single tag. The chart data is inserted in the report as a straight table.

Do the following:

1. Tip note

   For Word templates only:

   For more control over formatting in the resulting table, first create a one-column, one-row table in the Word document. Place your cursor inside the table cell so that the report object is inserted into the table.

   For more information, see [*Keep source formats setting at the table level*](../Word/word-tabular-properties.htm#Keep).
2. Click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar of the add-in. The Tables section appears.
3. Click Add table.

   This shows the list of objects that can be added as a table.
4. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the chart you want to add. You can preview the chart directly in the add-in before adding it by clicking the chart's name.

   Tip noteWhen selecting a chart, refresh the list of available tables from the Qlik Sense application by clicking ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).
5. In the drop down menu, select Table. This inserts the Qlik Sense entity as a single table tag into the selected area.

   Adding a Qlik Sense chart as an entire table

   ![Selecting a chart from a Qlik Sense app to insert with a single entity tag](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_EntireTable.png "Click to view full size")
6. The settings page for the table appears. You can adjust:

   - Name: It is recommended to provide a unique name to the table so you can identify it in the add-in if you later need to change its settings.
   - Description (optional): Add a description to the object if desired.
   - Filter: Add up to one filter to the object individually. This allows you to customize the data used in the table without affecting the data used in other template objects. Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).
7. After adding the table object, you can change its properties and customize formatting using the native features of your Microsoft Office application. This is slightly different depending on template type. See:

   - Excel: [*Formatting properties for entire tables*](../Excel/add-in-excel-tabular-properties.htm#Formatti)
   - PowerPoint: [*Formatting properties for entire tables*](../PowerPoint/powerpoint-tabular-properties.htm#Formatti)
   - Word: [*Formatting properties for entire tables*](../Word/word-tabular-properties.htm#Formatti)

Revisit any table you have added at any point for modifications to its configuration, to locate it in the Excel, PowerPoint, or Word file, or to add another instance of it. Click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon in the add-in to open the Tables landing page, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to navigate to the area where it is inserted. Adjust any settings as needed in the add-in.

## Adding a chart by column

A chart can also be added in tabular form as a set of single columns. This allows increased control over formatting within the report template, with the native text formatting options in Excel, PowerPoint, or Word.

The chart data is inserted in the report as a straight table.

Do the following:

1. Click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar of the add-in. The Tables section appears.
2. Click Add table.

   This shows the list of objects that can be added as a table.
3. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the chart you want to add one or columns from. You can preview the chart directly in the add-in before adding it by clicking the chart's name.

   Tip noteWhen selecting a chart, refresh the list of available tables from the Qlik Sense application by clicking ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).
4. In the drop down menu, select Individual columns. The list of available columns appears.

   Adding a Qlik Sense chart by columns

   ![Adding a Qlik Sense chart to template as a series of individual columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_TableByColumn.png "Click to view full size")
5. Select the columns you want to add, or click All to insert all columns from the chart.
6. Click Add. The columns are inserted into the template at the selected area.

   Two columns from a Qlik Sense application, added individually into an Excel report template.

   ![Result of adding individual columns from a chart as tabular data](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_TableColumnsCells.png "Click to view full size")
7. The settings page for the table appears. You can adjust:

   - Name: It is recommended to provide a unique name to the table so you can identify it in the add-in if you later need to change its settings.
   - Description (optional): Add a description to the object if desired.
   - Filter: Add up to one filter to the object individually. This allows you to customize the data used in the table without affecting the data used in other template objects. The filter is applied to all columns from the same source table.

     Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).
8. Adjust any other parameters as needed.

Each column selected is added to the template as a single column tag. The set of columns is still considered a single object.

Header cells with the field names are automatically inserted above each column tag. This allows you to customize the headers separately. These headers can be removed if you prefer to use the header formatting options within the add-in. See:

- Excel: [*Column header settings*](../Excel/add-in-excel-tabular-properties.htm#Header2)
- PowerPoint: [*Column header settings*](../PowerPoint/powerpoint-tabular-properties.htm#Header2)
- Word: [*Column header settings*](../Word/word-tabular-properties.htm#Header2)

Revisit any table you have added at any point for modifications to its configuration, to locate it in the Excel, PowerPoint, or Word file, or to add another instance of it. Click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon in the add-in to open the Tables landing page, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to navigate to the cell where it is inserted. Adjust any settings as needed in the add-in.

## Adding more columns from a chart

### Into a chart added by column

After adding some columns of a table individually, you can add more at any time.

Do the following:

1. Select the column tag of the column directly to the left of where you need to add another column.

   In the add-in, the chart table settings menu appears.
2. Under Columns, click the column you want to add to expand it.
3. Click Add column tag.

   The tag of the selected column is added to the right of the selected column.

Adjust any parameters as needed.

### From a chart added as entire table

You can also add more columns to the template from a chart that was added as an entire table. When you do this with a column, the new column you add becomes a new, separate table object with a single column. You can then add more columns to that object.

Do the following:

1. Select the table tag.

   In the add-in, the chart table settings menu appears.
2. Click Expand columns.
3. Select an area outside of where the table tag's columns will end.
4. Click Add column tag.

## Learn more

- [*Formatting properties for tabular data in Excel report templates*](../Excel/add-in-excel-tabular-properties.htm)
- [*Formatting properties for tabular data in PowerPoint report templates*](../PowerPoint/powerpoint-tabular-properties.htm)
- [*Formatting properties for tabular data in Word report templates*](../Word/word-tabular-properties.htm)
