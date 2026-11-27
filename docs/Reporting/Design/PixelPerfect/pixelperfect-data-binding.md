---
title: "Data binding"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-data-binding.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Defining report structure and data"]
---

# Data binding

You use the assets from your Qlik Sense application as the data sources for your report. In your PixelPerfect [report template](#glossary-0 "Glossary term"), add data bindings for the application data and images you want to use in the report. Then, connect these data bindings to objects in your template. Data bindings are added in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu in the PixelPerfect designer.

Data bindings in the Field List

![Image showing the 'Field List' menu expanded in the right side panel of the designer. The 'Field List' menu shows several example data bindings that have been added, such as levels and tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-field-list-data-bindings.png "Click to view full size")

## What is a data binding?

A data binding is a reusable entity that you create in your report template, which contains the data from the application that you then use in your report content. When you add a data binding, the data source to which it refers becomes usable in your template.

A data binding can be reused across multiple objects and bands in your report. For example, you could add a table data binding for a specific pie chart in the application. This data binding could be connected to different objects in the application – for example, it could be used in a native PixelPerfect bar chart and a Cross Tab.

## Types of data bindings

Data bindings are added in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu that is available on the right side panel in the designer. From this menu, you can add the following types of data bindings.

### Levels

Add a field or chart in the application as a level data binding. Level data bindings are often used to bind to bands, looping the creation of distinct content filtered for each value in a dimension.

For more information about using levels to loop over dimensions, see:

- [*Working with levels*](pixelperfect-work-with-levels.htm)
- [*Using a level to loop over application data*](pixelperfect-create-level.htm)

You can also add a level data binding and connect it directly to an object in the template. For example, you want to add a label and use it as a title for a section containing looped charts.

Level data bindings are a key element of highly formatted PixelPerfect tables. For more information, see [*Creating highly formatted tables*](pixelperfect-highly-formatted-table.htm).

### Images

Add images of your Qlik Sense [visualizations](#glossary-1 "Glossary term") directly onto your report.

For more information, see [*Adding images to the report template*](pixelperfect-add-images.htm).

### Tables

Add the source table for a [visualization](#glossary-2 "Glossary term") as a table data binding. The visualization does not have to be a table. Some Qlik Sense chart types – for example, treemap – cannot be added as table data bindings.

Table data bindings cannot be dragged and dropped directly from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Instead, they are mainly used to create the following:

- Native PixelPerfect charts

  [*Creating native PixelPerfect charts*](pixelperfect-native-chart.htm)
- Cross Tabs

  [*Summarizing data with a Cross Tab*](pixelperfect-cross-tab.htm)
- Sparklines

  [*Adding sparklines*](pixelperfect-sparklines.htm)

### Variables

Add variables from the Qlik Sense application as variable data bindings. Variables created in the script, as well as those created when editing sheets, can be used.

For more information, see [*Working with variables and expressions in your PixelPerfect template*](pixelperfect-variables-expressions.htm).

### Expressions

Add calculated expressions, that are evaluated using the Qlik engine, as expression data bindings. For example, you could add an expression such as sum(Sales) as a data binding so that it can be used in native PixelPerfect labels with other natural language, or you could reference it in conditional formatting.

For more information, see [*Working with variables and expressions in your PixelPerfect template*](pixelperfect-variables-expressions.htm).

## Adding a data binding

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to the type of data binding you want to add. For details about each type and how it is used, see [*Types of data bindings*](#Types).
3. When applicable, expand the sheet containing the item you want to add, or search for items.
4. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the item.

   The data binding is added.

## How to use data bindings

After you create a data binding, it is not automatically added to your report content. Instead, it is simply now available for use in the report content. To use a data binding in report content, it needs to be connected to an object or band in the template.

Depending on the type, you can use data bindings in the following ways:

- If available, drag and drop the data binding directly from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu onto the canvas.
- Add an object from the toolbox panel on the left side of the designer, and then connect it to the data binding. This process varies from object to object. The process usually involves selecting a Data Member and/or similar properties for the object.
- You can sometimes reference the data binding in the Expression Editor.

For full details, refer to [*Visualizing application data in your report*](pixelperfect-visualize-data.htm) and related topics.

## Refreshing data bindings

You can refresh the source application data used in:

- Data binding objects for charts added as levels. These are added under ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List > Levels.
- Data binding objects for the source tables used in native PixelPerfect charts, Cross Tabs, and sparklines. These are added under ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List > Tables.

This is helpful when:

- Dimensions and measures have been added to or removed from the source chart since you created the data binding.
- The definitions of dimensions and measures have been changed in the source chart since you created the data binding.

Refreshing data binding sources allows you to keep the same objects in your ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu without having to create new ones as chart configurations change.

Do the following:

1. Before you begin, remove all instances of any removed or updated columns and fields from your template. This is not required if your chart updates are only adding new columns or fields.

   This may involve any of the following:

   - Remove reference to the removed field or column in the properties for the [report band](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-banded-authoring.htm).
   - For chart levels, sparklines, and Cross Tabs, remove reference to any deleted fields by using the [Expression Editor](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-designer.htm#Expression) after selecting the level.
   - For native PixelPerfect charts, remove reference to any deleted columns in the object properties. This is done in the [Chart Designer](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-designer.htm#Chart).
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
3. Double-click Levels or Tables to expand it.
4. Hover your cursor over the item that you want to refresh.
5. Click the refresh (Update fields or Update columns) icon.

   Refreshing a level data binding in the Field List menu

   ![Clicking the 'Update fields' icon to refresh a level data binding](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-pixelperfect-refresh-level-binding.png "Click to view full size")

   Refreshing a table data binding in the Field List menu

   ![Clicking the 'Update columns' icon to refresh a table data binding](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-pixelperfect-refresh-table-binding.png "Click to view full size")

   If chart elements changed during the refresh, a notice appears listing each change. Changes can include columns and fields that were added, updated, or removed.
6. Continue with your template development according to your use case. This may involve re-configuring existing content or adding new content. After refreshing the data binding, newly added chart columns will now be available for use from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.
