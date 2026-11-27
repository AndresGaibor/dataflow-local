---
title: "Example - Creating a tabular report"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Excel/tabular-report-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing tabular report templates"]
---

# Example - Creating a tabular report

Expand/Collapse all

# Example - Creating a tabular report

In this example, you will build an Excel-based report to analyze sales by product, year, and region.

Example result

![Excel report example result, summary sheet with pivot table and metrics](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-preview-page-1.png "Click to view full size")

## Before you start

Requirements

Before you begin, ensure:

- Your Qlik Cloud subscription has capacity for the Qlik Reporting Service.
- You or your admin installs the Qlik add-in for Microsoft Excel.

  [*Deploying and installing Qlik add-ins for Microsoft Office*](../../Install/reporting-install-add-ins.htm)
- You have activated the Qlik add-in for Microsoft Excel after it is installed.

  [*Activating add-ins*](../OfficeCommon/add-in-get-started.htm#Activati)
- You have the required permissions for working with in-application reporting.

  [*Qlik Reporting Service permissions*](../../reporting-permissions.htm)

  If you cannot create or manage reports, contact your administrator and consult [*Setting permissions for metered reporting features*](../../../Admin/mc-permissions-reporting.htm).

Upload example sources

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

## Create a new template

Tip noteFor more information about getting started with the add-in, see [*Getting started with using Qlik add-ins for Microsoft Office*](../OfficeCommon/add-in-get-started.htm).

### Get started

Do the following:

1. Open Microsoft Excel and create a new XLSX file. This will be your template file.
2. Click the Qlik add-in icon in the ribbon bar under the Home tab.

   Open the Qlik add-in by clicking the Qlik icon in the ribbon bar

   ![Ribbon bar in Microsoft Excel showing the Qlik add-in icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_QlikIconInRibbon.png "Click to view full size")
3. Log in to the add-in using your Qlik Cloud credentials.

   [*Connecting to the tenant and logging in*](../OfficeCommon/add-in-get-started.htm#Connecti)

### Connect to the application

Do the following:

1. Select the Space where you have uploaded the application.
2. Under App, select the application.
3. Click Save.

   Connecting to the uploaded application in the template

   ![Add-in pane 'Home' tab, selecting source application to connect to.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-add-in-application-select.png "Click to view full size")

The template is now connected to the application.

## Add a level and a page

With levels and pages, you can automate the creation of filtered worksheets, cycling report data for each dimension or chart value:

- A level creates a new section for each dimension or chart value.
- A page create a new worksheet for each dimension or chart value.

Tip noteFor more information about levels and pages, see [*Working with levels and pages in tabular report templates*](add-in-excel-levels-pages.htm).

### Add a level

Add a level object to generate a separate section on the same worksheet for each unique value of a dimension or chart. In this case, create a new section for each region.

Do the following:

1. In the worksheet, select cell A3 to put it in focus.
2. In the add-in, click the ![Levels and pages](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_layer_outline.svg) icon on the top toolbar.

   The Levels and pages section opens.
3. Click Add level.
4. Expand Fields.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Region.

   Selecting the field to use as a level

   ![Selecting the field 'Region' to use it as a level](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-select-level.png "Click to view full size")
6. Under Select fields to add (optional), check the box for Region.

   This will insert a field tag with the level tags, creating section headers for each value.
7. Click Add.

After creating the level, add 3 rows under the <Region> field tag. This is where the report data will be added.

### Add a page

Add a page object to generate separate worksheets for each unique value of a dimension or chart. In this case, create a new worksheet for each year.

Do the following:

1. In the add-in, click the ![Levels and pages](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_layer_outline.svg) icon on the top toolbar.

   The Levels and pages section opens.
2. Click Add page.
3. Expand Fields.
4. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Date.autoCalendar.Year.

   Selecting the field to use

   ![Selecting the field to use as a page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-select-page.png "Click to view full size")
5. Under Select fields to add (optional), leave Date.autoCalendar.Year unchecked.
6. Click Add.

The worksheet title is updated with the name of the field used for the page object.

Template with level and page added

![Excel template with level and page objects defined](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-page-defined.png "Click to view full size")

## Add a chart image

Now that you have defined a level and page, add a chart image.

Do the following:

1. In the worksheet, select cell A5 to put it in focus.
2. In the add-in, click the ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) icon on the top toolbar.

   The Charts section opens.
3. Click Add chart.

   A list of available sheets appears.
4. Expand the Dashboard sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Top 5 Customers chart.

   Selecting the source chart to add as an image

   ![Selecting the source chart to add as an image](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-chart-image.png "Click to view full size")
6. Resize the chart image to your preferences, and then resize the height of the row so it matches the size of the chart image.

Tip noteFor more information about adding chart images, see [*Adding charts as images to report templates with Qlik add-ins for Microsoft Office*](../OfficeCommon/add-in-chart-images.htm).

## Add tabular data

Next, add a table based on a chart in the source application.

### Part 1: Add the source table

Do the following:

1. In the worksheet, select cell A6 to put it in focus.
2. In the add-in, click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar.

   The Tables section opens.
3. Click Add table.

   A list of available sheets appears.
4. Expand the Sales Tables sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Sales By Product Group chart, and select Individual columns.

   Selecting the source chart to add as an image

   ![Selecting the source chart table to add as tabular data](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-select-table-data.png "Click to view full size")
6. Under Select columns to add, check All.
7. Click Add.

   All columns from the source chart are added as individual columns in the worksheet.

### Part 2: Adjust the formatting

You can customize the table by applying native Excel formatting, such as:

- Resizing column widths
- Changing fonts, text size, and adding cell-specific styling
- Customizing number formatting

If you want to customize formatting in the table, you need to turn off Keep source formats for the table object you just created.

Do the following:

1. With the table object selected in the add-in window, uncheck Keep source formats under Table settings.

   Now you can change the formatting by applying changes to the cell contents of the table.
2. By default, the table object has fixed-text column headers inserted above it. These are not part of the table object.

   Under Table settings for the object, set Display headers to Show above tag cell. This ensures table headers are not duplicated.
3. Style the fixed-text headers by making the font size slightly larger than the tag cells.

Tip noteFor full details about customizing tabular formatting properties, see [*Formatting properties for tabular data in Excel report templates*](add-in-excel-tabular-properties.htm).

Template after adding chart image and table, and applying some custom formatting

![Template after adding chart image and table, and applying some custom formatting](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-table.png "Click to view full size")

## Add a native Excel pivot table

Next, add an Excel PivotTable to summarize the application's data at a high level.

Information note

Excel-native pivot tables connected to Qlik application data are not supported when placed inside a level. You can, however, place the Excel pivot table inside a worksheet with a page.

Tip note

For further details, see [*Working with native Excel tables*](add-in-excel-native-tables.htm).

### Part 1: Insert the source tabular data

Do the following:

1. Create a new worksheet and title it PivotTable source.
2. In the add-in, click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar.

   The Tables section opens.
3. Click Add table.

   A list of available sheets appears.
4. Expand the Sales Tables sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Sales Details 2021-2023 chart, and select Individual columns.
6. Under Select columns to add, check All.
7. Click Add.

   All columns from the source chart are added as individual columns in the worksheet.

### Part 2: Convert the tabular data to an Excel table

Do the following:

1. Select the following in the worksheet:

   - Header row
   - The row with tags
   - One additional blank row
   - All desired columns

   Selecting the required area to create a native Excel table

   ![Selected Excel range for creating a native table for pivot source](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-excel-pivottable-step1.png "Click to view full size")
2. Convert the selected area to an Excel table. The exact procedure depends on your Excel version. For example, select a cell in the table, and click Insert > Table in the ribbon.

   For exact steps, refer to [the official Microsoft documentation](https://support.microsoft.com/en-us/office/create-and-format-tables-e81aa349-b006-4f8a-9806-5af9df0ac664).
3. Select cell A3 in the Excel table. In the add-in window, under Tags, click Add tag: <deleterow>.

A <deleterow> tag is inserted in cell A3.

Native Excel table created with <deleterow> tag inserted in final row

![Native Excel table with deleterow tag inserted in final row](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-excel-pivottable-step2.png "Click to view full size")

### Part 3: Convert the Excel table to an Excel pivot table

Do the following:

1. Transform the Excel table you just created into a native Excel PivotTable. The exact steps may depend on your Excel version. For example, click Insert > PivotTable in the ribbon.

   For exact steps, refer to [the official Microsoft documentation](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576).
2. When prompted, select the option to add the new PivotTable on a new worksheet.
3. In the PivotTable field list, configure the pivot table as follows:

   - Rows:

     - Region
     - Product Group
     - Sales Rep Name
   - Columns:

     - Year
   - Values:

     - Sum of Sales
4. Change the labels in the pivot table according to preference.

PivotTable created on new sheet in template

![PivotTable created on a new worksheet in the template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-excel-pivottable-step3.png "Click to view full size")

## Add a variable

You can add variables from the analytics application to the report. Variables store values that can change dynamically. You can add a variable that has been added to the application, storing today's date.

### Part 1: Add the variable

Do the following:

1. In the worksheet where you added the PivotTable, rename the worksheet Summary.
2. In the worksheet, select a blank cell in the middle of row 1, about halfway across the entire content width.
3. In the add-in, click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar.

   The Variables and expressions section opens.
4. Click Add variable.

   A list of available variables appears.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to vTodayDate .

   Selecting the variable to use

   ![Selecting the variable to use](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-add-in-excel-select-variable.png "Click to view full size")

### Part 2: Format the variable as a banner

Do the following:

1. In the worksheet, merge and center two groups of cells in row 1, with the right group being the one that contains the variable.
2. In the cell for the left group, type the following:

   ```
    Report generated on:
   ```
3. By default, in tabular reports, dates are formatted as serial numbers. You can format the date according to your preferences. The exact procedure depends on your Excel version. An example:

   1. Select the <vTodayDate> tag in the template.
   2. Right-click the cell, and select Format cells.
   3. Select Date, and then choose the date format you would like to display.
   4. Click OK.

After adding the banner, you can customize it with native Excel formatting. For example, you can adjust text styling, add cell background colors, and add borders.

Banner in the report, using a variable to display when the report is generated

![Banner in the report, using a variable to display when the report is generated](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-variable.png "Click to view full size")

## Add an expression

You can add expressions to the report with Qlik-native calculations based on the application data. For example, you can add a cell showing high-level metrics, such as total sales, without creating a table.

### Part 1: Add the expression

Do the following:

1. In the worksheet, select a cell in the middle of row 2, about halfway across the entire content width.
2. Click ![Left-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_left.svg) to return to the Variables and expressions section menu.
3. Click Add expression.
4. Type a Name for the expression, for example: TotalSales.
5. Under Expression, type sum(Sales).

   Configuring the expression in the add-in

   ![Configuring the expression in the add-in](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-add-in-excel-configure-expression.png "Click to view full size")
6. Click Create.

### Part 2: Format the expression with a title cell

1. In the worksheet, merge and center two groups of cells in row 2, with the right group being the one that contains the expression.
2. In the cell for the left group, type the following:

   ```
    Total Sales:
   ```
3. Customize the number formatting for the TotalSales expression. The exact procedure depends on your Excel version. An example:

   1. Select the <TotalSales> expression tag in the template.
   2. Right-click the cell, and select Format cells.
   3. Select Currency, and click OK.

After adding the title and expression, you can customize it with native Excel formatting. For example, you can center their text, adjust text styling, add cell background colors, and add borders.

Expression for total sales added with the add-in and styled using native Excel formatting

![Expression total sales added with the add-in](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-expression.png "Click to view full size")

## Preview the report

Before finishing the report, you can set formatting and styling as desired.

When ready, preview the report as an Excel file to ensure it looks as expected.

Do the following:

1. In the add-in, click the ![Preview](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) icon on the top toolbar.

   The Preview section opens.
2. Click Preview as Excel (.xlsx).

Summary sheet in report, with a native Excel PivotTable, variable, and expression

![Final Excel report summary sheet with pivot table, variable, and expression](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-preview-page-1.png "Click to view full size")

Summary sheet in report, with level, page, chart image, and table.

![Final Excel report sheet with level, page, chart image, and table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-excel-preview-page-2.png "Click to view full size")

## Next steps

The next step is to upload the template to the application.

After uploading the template, you could:

- Configure a distribution list and report task, and set the report up to generate on a schedule.

  [*Configuring report generation*](../../Generate/configure-task-based.htm)
- Enable the template for on-demand reporting.

  [*Working with on-demand reporting*](../../OnDemand/reports-on-demand.htm)

## Learn more

- [*Designing tabular report templates*](design-tabular-report-templates.htm)
- [*Designing report templates with Qlik add-ins for Microsoft Office*](../OfficeCommon/reporting-add-ins.htm)
- [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm)
- [*In-application reporting with Qlik Cloud Analytics*](../../InAppGeneral/cloud-in-app-reports-intro.htm)
