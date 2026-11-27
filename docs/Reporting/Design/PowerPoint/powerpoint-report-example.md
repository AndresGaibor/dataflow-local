---
title: "Example - Creating a PowerPoint report"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PowerPoint/powerpoint-report-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing PowerPoint report templates"]
---

# Example - Creating a PowerPoint report

Expand/Collapse all

# Example - Creating a PowerPoint report

In this example, you will build a PowerPoint-based report to analyze sales by year, region, and customer.

Example result

![PowerPoint report result slide with page object, chart, expression, and table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-preview-page-2.png "Click to view full size")

## Before you start

Requirements

Before you begin, ensure:

- Your Qlik Cloud subscription has capacity for the Qlik Reporting Service.
- You or your admin installs the Qlik add-in for Microsoft PowerPoint.

  [*Deploying and installing Qlik add-ins for Microsoft Office*](../../Install/reporting-install-add-ins.htm)
- You have activated the Qlik add-in for Microsoft PowerPoint after it is installed.

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

1. Open Microsoft PowerPoint and create a new PPTX file. This will be your template file.
2. Click the Qlik add-in icon in the ribbon bar under the Home tab.

   Open the Qlik add-in by clicking the Qlik icon in the ribbon bar

   ![Ribbon bar in Microsoft PowerPoint showing the Qlik add-in icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_PowerPointAddIn_QlikIconInRibbon.png "Click to view full size")
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

## Add a title slide containing a variable

On the default title slide, add some text to the title box—for example, add a title such as Sales Report.

You can add variables from the analytics application to the report. Variables store values that can change dynamically. Add a variable that has been added to the application, storing today's date. It can be added on the title slide to indicate when the report was created.

Do the following:

1. Select the description box on the title slide. This is where the variable will be inserted.
2. In the add-in, click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar.

   The Variables and expressions section opens.
3. Click Add variable.

   A list of available variables appears.
4. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to vTodayDate.

   Selecting the variable to use

   ![Selecting the variable to use](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-add-in-excel-select-variable.png "Click to view full size")

After adding the variable tag, you can style and format the title slide as desired.

Variable added to title slide

![Title PowerPoint slide with styling and variable added](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-variable-added.png "Click to view full size")

## Add a page object

With page objects, you can automate the creation of filtered slides, cycling report data for each dimension value. A page creates one or more new slides for each dimension value.

Tip noteFor more information about pages, see [*Defining pages in PowerPoint report templates*](powerpoint-report-pages.htm).

Add a page object to generate a separate slide for each year.

Do the following:

1. Create a new slide.
2. In the add-in, click the ![Levels and pages](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_layer_outline.svg) icon on the top toolbar.

   The Levels and pages section opens.
3. Click Add page.
4. Expand Fields.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Date.autoCalendar.Year.

   Selecting the field to use for the page object

   ![Selecting the field to use for the PowerPoint page object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-select-page.png "Click to view full size")
6. Under Select fields to add (optional), check the box for Date.autoCalendar.Year.
7. Click Add.

The page object is inserted and the corresponding field tag is added as the title. Note that the page tag itself is not visible as text so the field tag denotes which dimension value each slide is for.

Template with page object added

![PowerPoint template slide with page object and year field tag](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-page-defined.png "Click to view full size")

## Add an expression

Next, you can add more content to the slide where the page object is inserted. All content defined by the page object will be repeated for each year value.

Add an expression to provide high-level information about total sales.

Do the following:

1. On slide 2, reduce the size of the <Date.autoCalendar.Year> title so that it occupies half of its current length.
2. Copy and paste the <Date.autoCalendar.Year> title and place the copy to the right of the original. Delete its contents.
3. With the new blank box selected, type:

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

Template with expression inserted in a title box on the slide.

![PowerPoint template slide with Total Sales expression in title box](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-expression.png "Click to view full size")

## Add a chart image

Do the following:

1. On slide 2, delete the content box below the title boxes.
2. In the add-in, click the ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) icon on the top toolbar.

   The Charts section opens.
3. Click Add chart.

   A list of available sheets appears.
4. Expand the Dashboard sheet.
5. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Top 5 Customers chart.
6. Resize the chart, making it take up half of the area under the titles.

   Template with chart image added.

   ![PowerPoint template slide with Top 5 Customers chart image](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-chart-image.png "Click to view full size")

## Add a table

Do the following:

1. In the add-in, click the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) icon on the top toolbar.

   The Tables section opens.
2. Click Add table.

   A list of available sheets appears.
3. Expand the Dashboard sheet.
4. Click ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to the Sales per Region chart, and select Individual columns.
5. Under Select columns to add, check All.
6. Click Add.

   All columns from the source chart are added as individual columns in a PowerPoint table.
7. Move and resize the table so it takes up the remaining space below the titles.

   Template with chart image added.

   ![PowerPoint template slide with Sales per Region table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-table.png "Click to view full size")

## Preview the report

Before finishing the report, you can set formatting and styling as desired.

When ready, preview the report as a PowerPoint file to ensure it looks as expected.

Do the following:

1. In the add-in, click the ![Preview](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) icon on the top toolbar.

   The Preview section opens.
2. Click Preview as PowerPoint (.pptx).

Title slide in PowerPoint, containing application variable

![PowerPoint report title slide with variable value](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-preview-page-1.png "Click to view full size")

PowerPoint report slide containing page object, chart image, expression, and table.

![PowerPoint report content slide with page object, chart, expression, and table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Reporting/ui_example-add-in-ppt-preview-page-2.png "Click to view full size")

## Next steps

The next step is to upload the template to the application.

After uploading the template, you could:

- Configure a distribution list and report task, and set the report up to generate on a schedule.

  [*Configuring report generation*](../../Generate/configure-task-based.htm)
- Enable the template for on-demand reporting.

  [*Working with on-demand reporting*](../../OnDemand/reports-on-demand.htm)

## Learn more

- [*Designing PowerPoint report templates*](powerpoint-report-template.htm)
- [*Designing report templates with Qlik add-ins for Microsoft Office*](../OfficeCommon/reporting-add-ins.htm)
- [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm)
- [*In-application reporting with Qlik Cloud Analytics*](../../InAppGeneral/cloud-in-app-reports-intro.htm)
