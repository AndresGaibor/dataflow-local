---
title: "Navigating the PixelPerfect designer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-designer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Getting started with PixelPerfect report templates"]
---

# Navigating the PixelPerfect designer

The PixelPerfect designer is where you construct PixelPerfect [report templates](#glossary-0 "Glossary term"). The designer is embedded within Qlik Sense applications. You access the designer by creating or editing a PixelPerfect template in the Templates tab in the Reporting section of your application.

The PixelPerfect designer

![An image of the PixelPerfect designer, showing all elements that need to be mentioned, such as the design surface, toolbar, toolbox panel (left side), and the right side panel (in this case, Properties are expanded)](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-designer.png "Click to view full size")

Information noteThe PixelPerfect designer is only available in English.

## Designer toolbar

The designer toolbar is located at the top of the PixelPerfect designer. In the toolbar, perform common actions on elements in your report template. For example, you can cut, copy, and paste objects in the template, delete objects or bands, and adjust the zoom for the design surface.

## Toolbox

The toolbox is the panel on the left side of the designer. From the toolbox, drag and drop report controls onto the design surface. Some controls need to be linked to data bindings when you add them from the toolbox. Others are used only for styling and formatting your report.

## Design surface

The design surface is shown in the center of the designer. This is where your template content is shown. It is a canvas where you add objects to define the structure and content of your report. The band structure of the template is shown on one side of the canvas.

For more information, see:

- [*Banded report authoring*](pixelperfect-banded-authoring.htm)
- [*Adding content to your PixelPerfect report template*](pixelperfect-add-content.htm)

## Side panel

The right-side panel is expandable and allows you to configure report data sources, properties, and other parameters. Click one of the following icons on the right edge of the designer to open these menus:

- ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties: Configure properties for the selected band or object. If nothing is selected, the global report properties are shown.
- ![Formula](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) Expressions: Configure expression-based properties for the selected band or object. If nothing is selected, the global expression properties for the report are shown.
- ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List: Add data bindings, reusable data entities from the Qlik Sense application. You can add different types of data bindings to suit a variety of content use cases: levels, images, tables (used only for native PixelPerfect visualizations), variables, and expressions.

  [*Data binding*](pixelperfect-data-binding.htm)
- ![Tree view](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg) Report Explorer: View the structure of the report as a hierarchical structure. You can reorganize objects and bands within the report structure by dragging and dropping.

  [*Using the Report Explorer*](pixelperfect-arrange-content.htm#ReportExp)

## Other interfaces in the designer

As you work in the PixelPerfect designer, you will interact with other interfaces. The following sections outline some notable examples.

### Chart Designer

The Chart Designer opens when you are creating a native PixelPerfect chart. With the Chart Designer, configure the data bindings used in the chart, the chart type, and choose how you want to present each data series you have added.

Open the Chart Designer by clicking Run Designer... within a ![Chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pixelperfect_chart.svg) Chart object you have added to the template from the toolbox.

For more information, see:

- [*Creating native PixelPerfect charts*](pixelperfect-native-chart.htm)
- [*Creating a PixelPerfect chart with user-defined series*](pixelperfect-native-chart-simple.htm)
- [*Creating a PixelPerfect chart with automated series splitting*](pixelperfect-native-chart-auto-split.htm)

### Expression Editor

The PixelPerfect Expression Editor opens whenever you edit an expression-based property. The Expression Editor offers extensive control over how properties are defined. You can use the Expression Editor to configure bookmarks, conditional formatting, and more.

Open the Expression Editor by selecting an item on the design surface, and clicking the ![Expression Editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) icon on the right side of the designer. Alternatively, click the bold f icon that pops up when you select the item.

For examples showing use of the Expression Editor, see:

- [*Example - Table of contents with level*](pixelperfect-toc-bookmarks.htm#Example)
- [*Example - Using a variable to display date of last application reload*](pixelperfect-variables-expressions.htm#Example)
- [*Add conditional formatting*](pixelperfect-highly-formatted-table.htm#Conditional)

### Filter Editor

You can use the Filter Editor to filter data in your PixelPerfect template. The Filter Editor is available for any report content for which you can configure the Filter String property.

For more information, see:

- [*Filtering data in your PixelPerfect report*](pixelperfect-filter-editor.htm)
- [*Example - Applying filtering to a table*](pixelperfect-example-filtered-table.htm)
