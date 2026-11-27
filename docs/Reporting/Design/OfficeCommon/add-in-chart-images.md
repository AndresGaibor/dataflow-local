---
title: "Adding charts as images to report templates with Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/OfficeCommon/add-in-chart-images.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Adding content to report templates with Qlik add-ins for Microsoft Office"]
---

# Adding charts as images to report templates with Qlik add-ins for Microsoft Office

You can add a chart as an image to your Excel, PowerPoint, or Word report template. When the report output is generated, an image of the chart is placed in the selected cell. The chart will use the data from the application's most recent reload.

## Applies to

This content applies to the following types of Qlik Cloud report templates:

- Excel

  [*Qlik add-in for Microsoft Excel*](reporting-add-ins.htm#Excel)
- PowerPoint

  [*Qlik add-in for Microsoft PowerPoint*](reporting-add-ins.htm#PowerPoint)
- Word

  [*Qlik add-in for Microsoft Word*](reporting-add-ins.htm#Word)

## Adding a chart image

When you add a chart image to the template, it is added as a placeholder image, representing a snapshot of what the chart looks like during your current session. This might include [selections](#glossary-1 "Glossary term") made in the application.

The selections in the chart snapshot are not included in the report output. When reports are generated, data reduction is instead controlled by:

- Report filters
- Cycles
- Section access
- For on-demand reporting, the application user's current selections

Do the following:

1. Click the ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) icon on the top toolbar of the add-in.
2. Click Add chart. A list of available sheets appears.

   Charts tab in a Qlik add-in, allowing you to add a new chart or re-visit a chart that you have already added

   !['Charts' tab in an add-in, from which you can add/modify existing charts you have added, or add a new chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_AddChartImage.png "Click to view full size")
3. Expand the sheet containing the chart you want to add. You can search the chart's name to refine the list of sheets if needed.
4. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon to add the chart.

   You can preview the chart directly in the add-in before adding it by clicking the chart's name.

   Select a chart you want to add to the template as an image

   ![Select the chart to add to the template from the available charts listed by app sheet](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ChooseChartImage.png "Click to view full size")
5. The chart is added, and the settings page for the image appears. You can adjust:

   - Name: It is recommended to provide a unique name to the image so you can identify it in the add-in if you later need to change its settings.
   - Description (optional): Add a description to the object if desired.
   - Zoom: Use the Zoom setting in the add-in as needed. You can also change the size of the image as you normally do with images in the Microsoft Office application you are using.
   - Filter: Add up to one filter to the object individually. This allows you to customize the data used in the chart without affecting the data used in other template objects. Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).

   Chart image placeholder added to template

   ![Chart image added to report template in reporting add-in](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ChartImageAdded.png "Click to view full size")

Revisit any chart you have added at any point for modifications to its configuration, to locate it in the workbook, or to add another instance of it to the Excel, PowerPoint, or Word file. Click the ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) icon in the add-in to open the Charts landing page, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to navigate to the area where it is inserted. Adjust any settings as needed in the add-in.

## Limitations

For Word reports, there are limitations for chart images that are inserted as [floating images](https://www.microsoft.com/en-us/microsoft-365/blog/2011/05/19/understanding-images-part-1-the-basics/). For more information, see [*Word reporting*](../../Reporting-service-specifications-limitations.htm#LimitsWord).
