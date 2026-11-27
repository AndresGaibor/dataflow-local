---
title: "Example - Creating a Word report"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Word/word-report-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing Word report templates"]
---

# Example - Creating a Word report

Expand/Collapse all

# Example - Creating a Word report

In this example, you will build a Word-based report to analyze sales by year, region, and customer.

Word report result.

![Generated Word report result, page 2](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-preview2.png "Click to view full size")

## Before you start

Requirements

Before you begin, ensure:

- Your Qlik Cloud subscription has capacity for the Qlik Reporting Service.
- You or your admin installs the Qlik add-in for Microsoft Word.

  [*Deploying and installing Qlik add-ins for Microsoft Office*](../../Install/reporting-install-add-ins.htm)
- You have activated the Qlik add-in for Microsoft Word after it is installed.

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

1. Open Microsoft Word and create a new DOCX file. This will be your template file.
2. Click the Qlik add-in icon in the ribbon bar under the Home tab.

   Open the Qlik add-in by clicking the Qlik icon in the ribbon bar

   ![Ribbon bar in Microsoft Word showing the Qlik add-in icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_WordAddIn_QlikIconInRibbon.png "Click to view full size")
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

## Setting up the report

Do the following:

- Add a title to the report—for example, Sales Report. Format the title as desired.

## Add a level

With levels, you can automate the creation of filtered sections, cycling report data for each dimension or chart value. A level creates a new section for each dimension or chart value.

Tip noteFor more information about levels, see [*Adding levels to Word report templates*](word-report-levels.htm).

Add a page object to generate a separate section for each year.

Do the following:

1. Add new lines below the title you created earlier.
2. In the add-in, click the ![Levels and pages](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_layer_outline.svg) icon on the top toolbar.

   The Levels and pages section opens.
3. Click Add level.
4. Expand Fields.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Date.autoCalendar.Year.

   Selecting the field to use for the level

   ![Selecting the field to use for the level object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-select-level.png "Click to view full size")
6. Under Select fields to add (optional), check the box for Date.autoCalendar.Year.
7. Click Add.

## Add expressions

Add expressions to provide high-level information about sales. You can reuse the same expression, placing it once at the top of the report (for all-time total sales), and once inside the level (for total sales per year).

Do the following:

1. Place your cursor above the opening <Date.autoCalendar.Year\_Level> tag of the level.
2. Press Enter to create a few new lines.
3. Type the following:

   ```
    Total Sales:
   ```
4. In the add-in, click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar.

   The Variables and expressions section opens.
5. Click Add expression.
6. Under Name, type TotalSales.
7. Under Expression, add the following:

   ```
   Money(Sum(Sales))
   ```
8. Click Create.
9. Under Select fields to add (optional), check the box for Date.autoCalendar.Year.
10. Click Add.
11. Add a few new lines between the <Date.autoCalendar.Year\_Level> and <Date.autoCalendar.Year> tags.
12. Type the following:

    ```
     Total Sales:
    ```
13. In the add-in, click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar.

    The Variables and expressions section opens.
14. Next to the TotalSales expression you just created, click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg).
15. Click Add expression tag.

Template with expressions inserted.

![Word template with Total Sales expressions inserted](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-expressions.png "Click to view full size")

## Add a chart image

Do the following:

1. Add a few new lines below the second Total Sales: <TotalSales> line.
2. In the add-in, click the ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) icon on the top toolbar.

   The Charts section opens.
3. Click Add chart.

   A list of available sheets appears.
4. Expand the Dashboard sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Top 5 Customers chart.
6. Resize the chart as desired.

   Template with chart image added.

   ![Word template with Top 5 Customers chart image added](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-chart-image.png "Click to view full size")

## Add a table

Do the following:

1. Place your cursor below the chart image you just inserted.
2. In the add-in, click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar.

   The Tables section opens.
3. Click Add table.

   A list of available sheets appears.
4. Expand the Dashboard sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Sales per Region chart, and select Individual columns.
6. Under Select columns to add, check All.
7. Click Add.

   All columns from the source chart are added as individual columns in a Word table.
8. Move and resize the table so it takes up the remaining space below the titles.

   Template with chart image added.

   ![Word template with Sales per Region table added below chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-table.png "Click to view full size")

## Add a variable in the document header

You can add variables from the analytics application to the report. Variables store values that can change dynamically. Add a variable that has been added to the application, storing today's date. It can be added to the document header so that each page contains the date of report generation.

Do the following:

1. Double-click the top of document canvas to select the document header. This is where the variable will be inserted.
2. In the add-in, click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar.

   The Variables and expressions section opens.
3. Click Add variable.

   A list of available variables appears.
4. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to vTodayDate .

   Selecting the variable to use

   ![Selecting the variable to use](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-add-in-excel-select-variable.png "Click to view full size")

## Preview the report

Use the Word-native features to finalize the document presentation. For example, you can:

- Set formatting, styling, and spacing as desired.
- Add auto-generated page numbers in the footer.
- Add a table of contents at the top of the document (formatting field tags with header styles ensures these items will be captured in the table of contents).

  [Microsoft documentation: Inserting a table of contents](https://support.microsoft.com/en-us/office/insert-a-table-of-contents-882e8564-0edb-435e-84b5-1d8552ccf0c0)
- Insert a page break within the level tag to break each cycle of the level into its own page.

Page 1 of Word report template ready to preview, containing table of contents

![Word template ready to preview, page 1 with table of contents](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-ready-to-preview1.png "Click to view full size")

Page 2 of Word report template ready to preview, containing tags and chart images.

![Word template ready to preview, page 2 with tags and chart image](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-ready-to-preview2.png "Click to view full size")

When ready, preview the report as a Word file to ensure it looks as expected.

Do the following:

1. In the add-in, click the ![Preview](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) icon on the top toolbar.

   The Preview section opens.
2. Click Preview as Word (.docx).

Page 1 of Word report result.

![Generated Word report result, page 1](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-preview1.png "Click to view full size")

Page 2 of Word report result.

![Generated Word report result, page 2](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-word-preview2.png "Click to view full size")

## Next steps

The next step is to upload the template to the application.

After uploading the template, you could:

- Configure a distribution list and report task, and set the report up to generate on a schedule.

  [*Configuring report generation*](../../Generate/configure-task-based.htm)
- Enable the template for on-demand reporting.

  [*Working with on-demand reporting*](../../OnDemand/reports-on-demand.htm)

## Learn more

- [*Designing Word report templates*](word-report-template.htm)
- [*Designing report templates with Qlik add-ins for Microsoft Office*](../OfficeCommon/reporting-add-ins.htm)
- [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm)
- [*In-application reporting with Qlik Cloud Analytics*](../../InAppGeneral/cloud-in-app-reports-intro.htm)
