---
title: "Adding sparklines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-sparklines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Adding sparklines

A sparkline is a simple visualization, usually styled in the form of a line, that is helpful for analyzing trends for a single metric. You can add sparklines to your PixelPerfect report using the Sparkline object.

A sparkline generally consists of a field (equivalent to a dimension) and a value member (equivalent to a measure).

Sparkline

![Sample report showing sparklines created with PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sparkline.png "Click to view full size")

## Requirements

The data you use for a sparkline has to be added as a table data binding. These data bindings are added under Tables in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.

The source data for the sparkline should ideally contain a single [dimension](#glossary-0 "Glossary term") and a single [measure](#glossary-1 "Glossary term"). To use sparklines to visualize more complex, multi-dimensional data, it is recommended that you apply a level to the band where you add the sparkline. In this case, the level should be an additional dimension along which you want to cycle the generation of multiple filtered sparklines.

## Creating sparklines

This is the recommended workflow for adding sparklines in your report.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Tables.
3. From the available sheets, select the Qlik Sense [chart](#glossary-2 "Glossary term") you want to add as a table. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to it.

   The data binding is added.
4. From the toolbox panel on the left side of the designer, drag a Sparkline onto the design surface.
5. Click the gear icon that appears next to the sparkline. In the pop-up menu, for Data Member, select the table data binding you created earlier.
6. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer, and expand Data.
7. For Value Member, select the variable metric you want to visualize (for example, sales).

## Refreshing source data for data bindings

Over time, the configuration of the source chart might change, requiring action in your PixelPerfect report template. You can refresh the source application data in data bindings that define your sparkline. This is helpful when:

- Dimensions and measures have been added to or removed from the source chart since you created the data binding.
- The definitions of dimensions and measures have been changed in the source chart since you created the data binding.

Refreshing data binding sources allows you to keep the same objects in your ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu without having to create new ones as chart configurations change.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Double-click Tables to expand it.
3. Hover your cursor over the item that you want to refresh.
4. Click the refresh (Update columns) icon.

   Refreshing a table data binding in the Field List menu

   ![Clicking the 'Update columns' icon to refresh a table data binding](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-pixelperfect-refresh-table-binding.png "Click to view full size")
5. Continue with your template development according to your use case. This may involve re-configuring existing content or adding new content. After refreshing the data binding, newly added chart columns will now be available for use from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.

## Example - Sparklines with a level

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

We will create sparklines with monthly sales by region.

### Part 1: Add data bindings

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Levels.
4. Expand Fields, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to Region.

   The data binding is added.
5. You are brought back to the main ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Click the plus icon next to Tables.
6. Expand the Sales Table sheet, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Regional Sales over Time chart.

   The data binding is added.

### Part 2: Add DetailReport band and connect it with data binding

You need to create a DetailReport band to use a level.

Do the following:

1. Right-click the Detail1 band, and then click Insert Band > DetailReport.
2. To bind the DetailReport1 band to the level, select the band and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu. Under Detail Report Tasks > Data Member, select the Region level.

### Part 3: Add a label and sparkline

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and double-click Levels to expand it.
2. For Region, expand the level object and drag the Region field within it onto the DetailReport1 band.

   Position the label at the top of the band, centered horizontally.
3. From the toolbox panel on the left side of the designer, drag a Sparkline onto the DetailReport1 band, below the Region label.
4. Resize the sparkline so that it occupies all horizontal space on the band, and its shape is a narrow rectangle.
5. Resize the DetailReport1 band so there is a small space at the bottom of the sparkline.

   Region label and empty sparkline added to template

   ![Report template showing a title label for the 'Region' level added to a band, and below it the empty Sparkline object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sparkline-blank.png "Click to view full size")
6. Select the sparkline and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.
7. Expand Appearance > View.
8. Check Highlight Max Point and Highlight Min Point.
9. For Color, expand the drop down menu. Paste the following hex code in the # field: 0d00ff. Click OK.
10. For Max Point Color, expand the drop down menu. Paste the following hex code in the # field: 0dff00. Click OK.
11. For Min Point Color, expand the drop down menu. Paste the following hex code in the # field: ff0000. Click OK.
12. In the top right corner, click Save template.
13. Click Preview report. Download the report and open it.

Report preview with sparklines

![Generated report with a series of sparklines - one for each region. The sparklines contain color-coded points showing the minimum and maximum vales for the calculated performance metric](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sparkline-preview.png "Click to view full size")
