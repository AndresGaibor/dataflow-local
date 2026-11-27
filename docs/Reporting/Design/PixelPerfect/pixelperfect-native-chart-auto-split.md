---
title: "Creating a PixelPerfect chart with automated series splitting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-native-chart-auto-split.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report", "Creating native PixelPerfect charts"]
---

# Creating a PixelPerfect chart with automated series splitting

With series templates, you can create native PixelPerfect charts where the application data is automatically split into different series. This method is useful when you do not need to manually split the series yourself.

## Requirements

Before you start creating a native PixelPerfect chart, you need to have a chart in your Qlik Sense application with a source table that adapts well to what you want to visualize. In the Qlik Sense chart, select the appropriate dimensions and measures to filter the data sufficiently from the application's data model.

The data you use for a native PixelPerfect chart has to be added as a table data binding. To create this type of data binding, use the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu and add an item under Tables.

## Creating an auto-split PixelPerfect chart

This process is similar to creating a chart with a user-defined series, but there are key differences. Notably, you use the same types of data bindings, but these are connected using a series template rather than by adding a series manually.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Tables.
3. From the available sheets, select the Qlik Sense chart you want to add as a table. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to it.

   The data binding is added.
4. From the toolbox panel on the left side of the designer, drag a ![Chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pixelperfect_chart.svg) Chart onto the design surface.
5. Select the blank chart and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
6. Under Chart Tasks > Data Member in the menu, select the table you added as a data binding.
7. Inside the chart, click Run Designer....

   The Properties for the chart are shown on the right side.
8. Select a field for Series Data Member. This sets the primary grouping for the chart. PixelPerfect automatically creates a new series for each distinct value in the field.
9. Expand Series Template.
10. To choose a chart type, select a value for View. The default is Bar. For a list of available charts, see [*Available chart types*](#Available).
11. For Argument Data Member, use the drop down menu to select a field containing the secondary data groupings.
12. Expand Value Data Members. For Value, select a field containing the variable metrics you want to visualize. For certain advanced chart types (for example, Candle Stick chart), you might need to select more than one Value field.

    Tip noteIn this context, selecting the Value is similar to selecting a [measure](#glossary-0 "Glossary term") in Qlik Sense.
13. When using a series template, it is often required to add summary functions to fulfill the aggregations specified in the chart. You need to set the summary options. Depending on the type of data you are using for your groupings, this might be labeled as one of the following:

    - Qualitative Summary Options
    - Numeric Summary Options
    - Date-Time Summary Options

    Expand the section.
14. Expand Summary Function.
15. Select a Function to use (for example, SUM).
16. Select an Argument. This is usually the variable metric your chart is meant to visualize (for example, sales).

## Additional tips for configuring the chart

The above workflow shows you how to create a native chart with automatically generated series, and connect it to Qlik Sense data sources. Here are some extra tips to help you make the most out of these charts.

### Labels and legends

You might need to configure labels and legends so that they appear correctly.

#### Changing the text

You can change the text shown in the labels and legend. You can do this by entering specific placeholders for the following properties:

- Labels: Open the Properties for the series, and add a placeholder to Label > Text Pattern.
- Legend: Open the Properties for the series, and add a placeholder to Legend Text Pattern.

The placeholders instruct PixelPerfect to generate dynamic text with commonly needed values. For a chart with autogenerated series, the following are commonly used placeholders:

- {S}
- {A}

For a full list of placeholders you can use, see [*Text definition placeholders for native PixelPerfect charts*](pixelperfect-text-definition-placeholders.htm).

#### Turning labels and legends off

If your chart has a lot of data, it is often preferred to turn labels off (they are turned on by default). To turn off labels for the chart, change the Labels Visibility setting in the Properties to False.

With auto-generated series, the chart legend can play a key role to help distinguish each series in the chart. However, if you want to turn the legend off, expand Legend and set Visibility to False.

## Refreshing source data for data bindings

Over time, the configuration of the source chart might change, requiring action in your PixelPerfect report template. You can refresh the source application data in data bindings that define your native PixelPerfect chart. This is helpful when:

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

## Available chart types

The following charts are shown as options when creating an auto-split PixelPerfect chart.

Available native PixelPerfect charts

- Bar
- Bar Stacked
- Bar Stacked 100%
- Side by Side Bar Stacked
- Side By Side Bar Stacked 100%
- Waterfall
- Point
- Line
- Line Stacked
- Line Stacked 100%
- Step Line
- Spline
- Scatter Line
- Swift Plot
- Pie
- Doughnut
- Nested Doughnut
- Funnel
- Area
- Area Stacked
- Area Stacked 100%
- Step Area
- Spline Area
- Spline Area Stacked
- Spline Area Stacked 100%
- Range Bar
- Side By Side Range Bar
- Range Area
- Polar Point
- Polar Line
- Polar Area
- Stock Series
- Candle Stick

## Example - Creating a multi-bar chart with auto-split series

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

This example shows you how to create a bar chart with automatically generated series for each value in a specific dimension.

### Part 1: Add data binding and chart

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Tables.
4. Expand the Sales Tables sheet, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Sales Details 2021-2023 chart.

   The data binding is added.
5. From the toolbox panel on the left side of the designer, drag a ![Chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pixelperfect_chart.svg) Chart onto the Detail1 band.

   Blank chart added to template. The image also shows the data source that will be used to bind to the chart.

   ![Report template with a blank Chart object added, along with the 'Field List' menu expanded on the right side panel showing the data binding we will use to connect to the chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-auto-split-blank.png "Click to view full size")

### Part 2: Connect the chart to data binding

Do the following:

1. Select the blank chart and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
2. Under Chart Tasks > Data Member in the menu, select the Sales Details 2021-2023 table.
3. Inside the chart, click Run Designer....

   The Properties for the chart are shown on the right side.
4. In the left panel in the Chart Designer, hover over Series and click the plus icon. In the menu, select Bar to create a bar chart series.

   The Properties for the new series are shown on the right side.
5. For Series Data Member, select the Year field.
6. Expand Series Template if not already expanded.
7. For View, leave the chart type as Bar.
8. For Argument Data Member, select Region field.
9. Expand Value Data Members. For Value, select the Sales field.
10. Next ,define the summary function to use. Expand Qualitative Summary Options.
11. Expand Summary Function.
12. For Function, select SUM.
13. For Argument, select the Sales field.

### Part 3: Refine the appearance

Finally, we want to hide the labels and arrange the data in descending order along the total sales for each dimension.

Do the following:

1. Still in the Properties in Chart Designer, set Labels Visibility to False.
2. Set Series Points Sorting to Descending.
3. Set Series Points Sorting Key to Value.
4. Add a title to the chart. In the left panel in the Chart Designer, hover over Titles and click the plus icon. Select a title position using the popup menu.
5. In the Properties for the title, enter Yearly Sales By Region for the Text property.
6. Click OK to exit the Chart Designer.
7. Increase the size of the chart and the Detail1 band.
8. In the top right corner, click Save template.
9. Click Preview report. Download the report and open it.

Generated report showing a chart created using automated series splitting

![Generated report showing a chart created using automated series splitting. In this case, the charts shows a bar chart with different series for each year in the data, also broken down by region values](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-auto-split-preview.png "Click to view full size")

## Learn more

- [*Text definition placeholders for native PixelPerfect charts*](pixelperfect-text-definition-placeholders.htm)
