---
title: "Adding charts as images in your HTML template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-chart-images.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template"]
---

# Adding charts as images in your HTML template

You can add a chart as an image to the HTML report template. The chart will use the data from the application's most recent reload.

A chart image is added as an img element in the HTML template code. The image is also added as an object in the objects panel, which you can return to at any time for editing and reuse.

When selecting a chart, refresh the list of available charts from the Qlik Sense application by clicking ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the image.
2. In the HTML designer, click ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) in the objects panel.

   Charts menu in the objects panel within the HTML designer

   !['Charts' tab in HTML designer, from which you can modify existing charts you have added, or add a new chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-image-objects-panel.png "Click to view full size")
3. Click Add chart. A list of available sheets appears.
4. Expand the sheet containing the chart you want to add. You can search the chart's name to refine the list of sheets if needed.
5. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon to add the chart.

   To make sure you are adding the correct chart, you can preview it before adding. To preview a chart, click ![Right arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) next to it, or click the chart name.

   Selecting a chart to add as an image

   ![Selecting the chart to add as an image to the HTML report](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-image-select-chart.png "Click to view full size")
6. The chart is added to the template as an img element. In the objects panel, provide a unique Name to the image so you can identify it later.

   Template design surface with newly added img element highlighted

   ![Chart image element added to report template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-image-resulting-tags.png "Click to view full size")
7. After adding the image, you can adjust the following:

   - Adjust the Zoom in the objects menu. This can help with readability of chart text, and to highlight certain aspects of the chart.
   - Add up to one Filter to the object individually. This is done in the objects menu and allows you to customize the data used in the chart without affecting the data used in other template objects. Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).
   - Change the dimensions of the image with the width and height attributes in the img elements. This is done in the design surface.
8. You can re-use the image object at any time. Open ![Chart object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_chart_object_outline.svg) in the objects panel, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to open the object. Click Add image to add the image again.
