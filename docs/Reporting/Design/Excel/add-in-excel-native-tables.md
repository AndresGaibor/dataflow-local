---
title: "Working with native Excel tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Excel/add-in-excel-native-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing tabular report templates"]
---

# Working with native Excel tables

When you need to create certain types of content in your [report template](#glossary-0 "Glossary term"), it is often easier and more beneficial to use Microsoft Excel's native table features. This includes creating pivot tables, calculated columns, and calculated row totals.

It is recommended to convert your template content to native Excel tables if you want to do any of the following:

- Have easier access to native Excel data filtering and sorting
- Create a pivot table in your Excel report
- Add calculated columns which rely on native Excel computations
- Add calculated row totals which rely on native Excel computations

In some cases, you can accomplish these outcomes without converting content to native Excel tables. However, using this functionality is easier and is therefore the recommended workflow.

## Applies to

This content applies to designing [tabular report](#glossary-1 "Glossary term") templates using the Qlik add-in for Microsoft Excel. See [*Qlik add-in for Microsoft Excel*](../OfficeCommon/reporting-add-ins.htm#Excel).

## Creating native Excel pivot tables

A Qlik Sense pivot table can be added as a single table tag. You can recognize it from the add-in user interface because you cannot add it as individual columns. However, if you simply insert the Qlik Sense pivot table as a single-tag item with no other modifications, the chart will be exported as a straight table, not a native Excel pivot table.

Instead, complete the following steps to use Qlik Sense tabular data to create a native Excel pivot table:

1. Create or select a chart in your application to use as the source straight table. Insert it as a set of columns. See [*Adding a chart by column*](../OfficeCommon/add-in-tabular-data.htm#Adding2).
2. Transform the chart table into a native Excel straight table.
3. Transform this native Excel straight table into a native Excel pivot table.

See below for details on each process.

### Step 1: Insert the source data as a straight table

Design or select a chart in your Qlik Sense application with the columns you need to use to create the native Excel pivot table. This can be any Qlik Sense chart that has an underlying straight-table data structure (all supported visualizations except pivot table). If you are starting from scratch, a Straight table might be the easiest input object to help visualize what you would like to add.

A native Excel pivot table performs aggregations on its own. Therefore, to include calculated expressions from the application in your Excel pivot table, add the non-aggregated fields from the Qlik Sense application as dimensions rather than measures.

Create a Qlik Sense visualization and add all desired columns as dimensions

![Source table in Qlik Sense app to be used as input for native PivotTable](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotSourceSense.png "Click to view full size")

Next, add the chart to the report template as a set of individual columns. See [*Adding a chart by column*](../OfficeCommon/add-in-tabular-data.htm#Adding2) for instructions.

Add the Qlik Sense visualization as a table of individual columns in the template

![Source table added to template as straight table consisting of individual columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotSourceTable.png "Click to view full size")

### Step 2: Convert the tabular data to a native Excel straight table

When you have added the source Qlik Sense chart to the template, convert it to a native Excel straight table. Visit [the official Microsoft documentation](https://support.microsoft.com/en-us/office/create-and-format-tables-e81aa349-b006-4f8a-9806-5af9df0ac664)for additional instructions. The following procedure is customized to provide details specific to your Qlik Excel template.

Do the following:

1. In Excel, highlight the area required to generate the native Excel table. This includes the header row, the row with tags, one additional row below these rows, and all desired columns. Convert the selection into a native Excel straight table.

   Highlight the necessary components of the source table and convert them into a native Excel straight table

   ![ Columns and rows selected in source table, showing necessary selections to create the native straight table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotSourceExcelTable.png "Click to view full size")
2. With the native Excel straight table created, insert a <deleterow> tag below the row which has the column tags. This ensures the selected row is deleted in report output. For more information, see [*Removing rows with the Deleterow tag*](add-in-excel-deleterow.htm).

   Insert a <deleterow> tag in native Excel table

   ![Newly created Excel native straight table, with deleterow tag in the necessary location](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotExcelDeleteRow.png "Click to view full size")

### Step 3: Convert the native Excel straight table to a native Excel pivot table

Finally, transform the Excel straight table into an Excel PivotTable.

Visit [the official Microsoft documentation](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576). for additional instructions. The following procedure is customized to provide details specific to your Qlik Excel template.

Information note

Excel-native pivot tables connected to Qlik application data are not supported when placed inside a level. You can, however, place the Excel pivot table inside a worksheet with a page.

1. Select a cell within your native Excel straight table, and use the options in the Excel ribbon bar to convert it into a PivotTable.

   Transform the native Excel straight table into a native Excel PivotTable

   ![Native Excel straight table selected, with necessary buttons user needs to select to convert it to a native pivot table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotCreate_rev.png "Click to view full size")
2. Configure your pivot table with your desired configuration, using the Microsoft Excel features. If you need to have calculated expressions (measures) in your output, this is the step in which you would apply those aggregations.

   Prepare the native Excel pivot table using your desired configurations

   ![Configuration settings for native Excel PivotTable](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotConfig_rev.png "Click to view full size")

If you preview the report, the native Excel pivot table is generated correctly.

Report output showing intended rendering of native Excel pivot table

![Report output with native PivotTable rendered correctly](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddin_NativePivotExported.png "Click to view full size")

## Adding calculated columns

You can use Excel formulas to add calculated columns that do not exist in your original Qlik Sense application. Use this functionality with both dimensions and measures defined in the source application.

Do the following:

1. Use the add-in to insert a Qlik Sense chart by column.

   Qlik Sense chart added to Microsoft Excel in tabular form

   ![Ribbon bar in Microsoft Excel showing the Qlik add-in icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SourceTableCalcColumn.png "Click to view full size")
2. In Excel, highlight the area required to generate the native Excel table. This includes the header row, the row with tags, one additional row below these rows, and all desired columns. Convert the selection into a native Excel straight table.

   Highlight the necessary components of the source table and convert them into a native Excel straight table

   ![Columns and rows selected in source table, showing necessary selections to create the native straight table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CalcColumnNative.png "Click to view full size")
3. To add a calculated column to the right of the rightmost column in your Excel table, click the cell to the right of the rightmost column tag, and type =, followed by your custom formula.

   Expression written for a new calculated column in the Excel table

   ![Add the calculated column expression in the column cell where the column tags would typically be](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CalcColumnCreate.png "Click to view full size")
4. A new column is added to the Excel table. Note that it could have an invalid value in the template, but if configured correctly, it will generate the correct information in the output.

   You can rename the column, and format it as needed.

   Calculated column added to native Excel table

   ![Calculated column in Excel table after being added](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CalcColumnRename.png "Click to view full size")

If you preview the report, you will see that the Excel table includes the new column, with the native formula being propagated in all rows.

Report output including calculated column Revenue

![Report output showing that calculated column was rendered correctly](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CalcColumnOutput.png "Click to view full size")

## Adding calculated totals

You can add a row that displays totals in your table by using native Excel features. Select the table, click on Table Design on the right, and select the Total Row checkbox.

Do the following:

1. Use the add-in to insert a Qlik Sense chart by column.

   Qlik Sense chart added to Microsoft Excel in tabular form

   ![Source straight table chart from Qlik Sense app, added to the template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SourceTableCalcColumn.png "Click to view full size")
2. In Excel, highlight the area required to generate the native Excel table. This includes the header row, the row with tags, one additional row below these rows, and all desired columns. Convert the selection into a native Excel straight table.

   Highlight the necessary components of the source table and convert them into a native Excel straight table

   ![Columns and rows selected in source table, showing necessary selections to create the native straight table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CalcColumnNative.png "Click to view full size")
3. With the native Excel straight table created, insert a <deleterow> tag below the row which has the column tags. This ensures the selected row is deleted in report output. For more information, see [*Removing rows with the Deleterow tag*](add-in-excel-deleterow.htm).
4. Click anywhere inside the table, and then click the Table Design tab in the Excel toolbar. Select the Total Row checkbox.

   Add a Total Row to the Excel table using the native Excel features

   ![Enable the option in the Excel toolbar to create a Total Row for the Excel native table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_TotalsEnable.png "Click to view full size")
5. In the new Total row, click the cell for the column you want to have a total row for, and use the drop down to select any of the available built-in table summary functions.

   List of summary functions in the drop down list

   ![Drop down menu to select a summary function for the Total Row](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_Totals_SummaryFunctions.png "Click to view full size")

Tip noteAlternatively, you can also manually insert an Excel formula into a Total row. Be sure to include at least two rows from a column in the source table. This allows the add-in to expand the range to include all needed rows.

## Learn more

- [*Example - Creating a tabular report*](tabular-report-example.htm)
