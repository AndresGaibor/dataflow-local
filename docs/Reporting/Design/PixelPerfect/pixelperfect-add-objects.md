---
title: "Adding objects to your PixelPerfect report template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-add-objects.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template"]
---

# Adding objects to your PixelPerfect report template

Add non-data-bound (not connected to a data binding you created) and data-bound objects to your template to fill it with content. At a high level, objects can be used to populate reports with data, style reports, and fulfill functional formatting needs.

## Adding non-data-bound objects

Non-data-bound objects can be added to your report template to enhance its appearance and to achieve functional needs.

These objects are usually added by dragging them from the toolbox panel on the left side of the designer onto the design surface. Here are some common examples of objects to use:

- ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label: Text-based element that can contain custom fixed text. A label can also be connected to a data binding. Labels can be added in the toolbox or from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. For an example of adding custom fixed text, see [*Example - Adding a label with custom fixed text*](#Example).
- ![Select image](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) Picture Box: Image-based element that can contain an external image or a data-bound chart image from your Qlik Sense application. For more information about adding an external image, see [*Adding external images to the report template*](pixelperfect-add-external-images.htm).
- ![Line](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_line_outline.svg) Line: Used for adding lines to divide content for improved readability, or to draw shapes manually.
- ![Shapes](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_shapes_outline.svg) Shape: Add shapes to your report to achieve styling needs. Configure the shape and other parameters in the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.
- ![List](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg) Table of Contents: Add an interactive table of contents in the header or footer of the report. For more information, see [*Adding a table of contents*](pixelperfect-toc-bookmarks.htm).
- ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_info_outline.svg) Page Info: Insert the page number and other information.
- ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_break_outline.svg) Page Break: Add a manual page break to force content to be split onto a new page at a specific point.

### Example - Adding a label with custom fixed text

Adding a label with custom fixed text is helpful for manually inserting titles and other content into your report.

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label onto the design surface.
2. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer, if not already open.
3. Under Label Tasks > Text, insert the text you want to use.

Tip noteAlternatively, double-click the label after adding it, and type the text.

You can customize the label's appearance using the other settings in the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.

## Adding data-bound objects

Before you can link objects in the template to specific sets of your application data, you need to create data bindings in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. For more information, see [*Data binding*](pixelperfect-data-binding.htm).

After you have created the required data bindings, you can add data-bound objects to the template. This can generally be done in two ways:

- Dragging certain data bindings directly onto the design surface from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. A default object is added and the data binding is used to populate it with data when reports are generated.
- Dragging an object from the toolbox onto the design surface, and then connecting it with a data binding. Not all objects available in the toolbox can be data-bound.

For more information, see [*Visualizing application data in your report*](pixelperfect-visualize-data.htm) and related topics.
