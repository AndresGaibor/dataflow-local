---
title: "Adding images to the report template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-add-images.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Adding images to the report template

You can insert images into your PixelPerfect report template. Add images of content from the Qlik Sense application, which use the latest application data at time of report generation.

You can also add images from external sources such as your computer or a web URL. See [*Adding external images to the report template*](pixelperfect-add-external-images.htm).

## Adding Qlik Sense charts as images

You can add images of charts in the Qlik Sense application. You first need to add a data binding for the image that you want to use, then add it to the template with a Picture Box.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Hover your cursor over Images, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
3. Navigate through the sheets to find the image you want to add. You can use the search bar to search for specific charts or sheets. You can preview an object by clicking ![Right arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) next to it. Click View in Qlik Sense app when previewing a chart to open the sheet where the chart is located.
4. To add a chart image as a data binding, click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to it.

   You are brought back to the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Double-click the Images node in the menu to expand it.
5. After adding the image as a data binding, you can edit it to customize the zoom and description. See [*Adjusting zoom level of image bindings*](#Modifying).
6. Drag the image data binding you added onto the report design surface. It is added as a Picture Box.

## Adjusting zoom level of image bindings

After you add an image binding, you can modify it to set a custom zoom level. You can also edit the description and generate previews as you customize.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Double-click Images to expand it.
3. Hover over an item, and click the pencil icon.
4. Optionally, add a Description. Changes to the description are auto-saved.
5. Adjust the Zoom as needed. As you modify the zoom, click Image preview to check the appearance of the image.

   Information noteTo preview what the image zoom will look like, you first need to add the binding to the template.
6. Click Save to confirm the changes to the zoom level.

## Example - Adding a Qlik Sense object as an image

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

In this example, we add a Qlik Sense image to the default Detail1 band. You can add images to other bands as well.

Do the following:

1. Create a new PixelPerfect template.

   [*Creating a template*](pixelperfect-report-get-started.htm#CreateTemplate)
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_report-pixelperfect-gen-field-list.png "Click to view full size")
3. In the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, hover your cursor over Images, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. From the available sheets, expand Dashboard.
5. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Sales per Region pie chart. This creates the data binding.

   You are brought back to the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Double-click the Images node in the menu.
6. Drag the Sales per Region data binding onto the Detail1 band in the design surface.
7. Resize and reposition the Picture Box and the Detail1 band as desired.

   Picture Box with a Qlik Sense chart added as an image

   ![PixelPerfect report template with a chart image placeholder added to it. The 'Field List' menu is also open in the right side of the screen, showing the data binding used to create the chart image, under 'Images' node](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_report-pixelperfect-sense-image.png "Click to view full size")
8. In the top right corner, click Save template.
9. Click Preview report. Download the report and open it.

Report preview

![Report preview showing the generated chart image, which is a pie chart from the source Qlik Sense app](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sense-image_preview.png "Click to view full size")
