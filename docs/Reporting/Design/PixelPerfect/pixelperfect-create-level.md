---
title: "Using a level to loop over application data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-create-level.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Using a level to loop over application data

You can loop and repeat the creation of report elements using data from the Qlik Sense application.

For an overview of levels, see [*Working with levels*](pixelperfect-work-with-levels.htm).

## High-level workflow

This is the recommended workflow for using levels in your PixelPerfect report. It covers some of the most common and simple ways to work with levels in the designer.

### Part 1: Add data bindings

First, you need to add the data binding that will be used to cycle the generation of unique report elements. For example, if you want a separate section in the report for each region, you need to add a Region field as a data binding. Data bindings are added in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.

This workflow assumes you already have content, in the applicable areas in the template, for which you want to create a level.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Levels.
3. Expand the sections to find the item you want to use. You can select a field from Fields, or an entire chart from any of the sheet sections.
4. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to an item to add it as a data binding.

### Part 2: Connect the data binding to the band

Next, you need to connect the level data binding to a band.

You cannot bind a level to the default Detail1 band, so you will need to create a new DetailReport band for content where you plan on using a level.

Do the following:

1. Create a new DetailReport band. See [*Creating a new band*](pixelperfect-banded-authoring.htm#Create).
2. Select the new band, if not already selected.
3. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
4. Under Detail Report Tasks > Data Member, select the item to use as the level.

## Refreshing source data for data bindings

You can refresh the source application data used for charts that have been added as level data bindings. This is helpful when:

- Dimensions and measures have been added to or removed from the source chart since you created the data binding.
- The definitions of dimensions and measures have been changed in the source chart since you created the data binding.

Refreshing data binding sources allows you to keep the same objects in your ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu without having to create new ones as chart configurations change.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Double-click Levels to expand it.
3. Hover your cursor over the item that you want to refresh.
4. Click the refresh (Update fields) icon.

   Refreshing a level data binding in the Field List menu

   ![Clicking the 'Update fields' icon to refresh a level data binding](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-pixelperfect-refresh-level-binding.png "Click to view full size")
5. Continue with your template development according to your use case. This may involve re-configuring existing content or adding new content. After refreshing the data binding, newly added chart columns will now be available for use from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.

## Example - Looping chart images over a dimension

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

### Part 1: Add data bindings

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Levels.
4. Expand Fields, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Region chart.

   The data binding is added.
5. You are brought back to the main ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Click the plus icon next to Images.
6. Expand the Dashboard sheet, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Top 5 Customers chart.

   The data binding is added.

   Field List menu showing newly created level and image data bindings

   ![The 'Field List' menu showing the newly created data bindings added for use: a 'Region' level and a 'Top 5 Customers' image.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-level-field-list.png "Click to view full size")

### Part 2: Add band and content

Do the following:

1. On the design surface, right-click the Detail1 band and select Insert Band > DetailReport.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and double-click Levels to expand it.
3. For Region, expand the level object and drag the Region field within it onto the DetailReport1 band.

   Position the label at the top of the band.
4. In the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, expand Images and drag Top 5 Customers onto the DetailReport1 band. Place it below the Region label.

You can customize and style the content as desired.

### Part 3: Bind the level to the band

Do the following:

1. Click the DetailReport1 band.
2. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
3. Under Detail Report Tasks > Data Member, select the Region field.

   Report template with content and DetailReport1 band bound to level

   ![Report template with Detail1 band selected, and its properties opened on the right side panel. The properties show that the data binding has been connected to the band under 'Data Member'](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-level-empty.png "Click to view full size")
4. In the top right corner, click Save template.
5. Click Preview report. Download the report and open it.

Report preview

![Generated report showing several sections, one for each region, with a chart under each region heading](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-level-preview.png "Click to view full size")
