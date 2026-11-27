---
title: "Filtering data in your PixelPerfect report"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-filter-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Filtering data in your PixelPerfect report

You can use the Filter Editor to filter data in your PixelPerfect template. The Filter Editor is available for any report content for which you can configure the Filter String property.

## Filtering content

Do the following:

1. Select a report item for which the Filter String property is configurable—for example, a DetailReport band or native PixelPerfect chart.
2. Open the Filter Editor. Where this action is performed depends on the content you are filtering:

   - For a DetailReport band: open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right-side panel.
   - For a native PixelPerfect chart: Click Run Designer..., create a series, and then modify the Filter String property in its properties.
3. In the Filter Editor, configure you filter using groups and conditions. For more information, see [*Using the Filter Editor*](#FilterEditor).

### Using the Filter Editor

Use the graphical interface in the Filter Editor to configure your filter. There are two main components to a filter: groups and conditions. Groups allow you to combine and nest conditions together.

There is always a default group that cannot be deleted. By default, this is set to an And condition, but can be changed to any of the other operators.

Click the plus icon next to the first And group to add groups and conditions. A condition needs to have a subject (field), an operator, and most often, a value.

Switch to Advanced Mode to view and edit the input expression that defines the filter.

PixelPerfect Filter Editor with filter added

![Filter Editor with condition added in the graphical user interface: Sales Is greater than 5000000](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-example-filter-editor.png "Click to view full size")

## Example

For an example of using the Filter Editor to create a filtered table with PixelPerfect, see [*Example - Applying filtering to a table*](pixelperfect-example-filtered-table.htm).

## Limitations

Filters you create with the Filter Editor cannot be reused.
