---
title: "Creating a PixelPerfect chart with user-defined series"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-native-chart-simple.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report", "Creating native PixelPerfect charts"]
---

# Creating a PixelPerfect chart with user-defined series

You can create a native PixelPerfect chart with manually added series. This method is simpler than using a series template.

Native PixelPerfect stacked bar chart

![Example report showing a native PixelPerfect chart, in this case a stacked bar chart with sales and margin calculations for various products](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-example.png "Click to view full size")

## Requirements

Before you start creating a native PixelPerfect chart, you need to have a chart in your Qlik Sense application with a source table that adapts well to what you want to visualize. In the Qlik Sense chart, select the appropriate dimensions and measures to filter the data sufficiently from the application's data model.

The data you use for a native PixelPerfect chart has to be added as a table data binding. To create this type of data binding, use the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu and add an item under Tables.

## Creating a simple PixelPerfect chart

This is the general workflow for creating a native PixelPerfect chart. Parts of it might not apply to every chart available. Each of the charts is different, serving a range of visualization needs ranging from simple to complex. Depending on what you need to visualize, some additional configurations might also be required.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Tables.
3. From the available sheets, select the Qlik Sense chart you want to add as a table. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to it.

   The data binding is added.
4. From the toolbox panel on the left side of the designer, drag a ![Chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pixelperfect_chart.svg) Chart onto the design surface.
5. Select the blank chart and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
6. Under Chart Tasks > Data Member in the menu, select the table you added as a data binding.
7. Inside the chart, click Run Designer....
8. In the left panel in the Chart Designer, hover over Series and click the plus icon.
9. In the menu, select a chart type. For a list of available charts, see [*Available chart types*](#Available).

   The Properties for the new series are shown on the right side.
10. Under Name, add a name for the series. This is recommended, for example, if your chart requires more than one series.
11. For Argument Data Member, use the drop down menu to select a field containing independent categories that group the data.

    Tip noteIn this context, selecting the Argument Data Member is similar to selecting a [dimension](#glossary-0 "Glossary term") in Qlik Sense.
12. Expand Value Data Members. For Value, select a field containing the variable metrics you want to visualize. For certain advanced chart types (for example, Candle Stick chart), you might need to select more than one Value field.

    Tip noteIn this context, selecting the Value is similar to selecting a [measure](#glossary-1 "Glossary term") in Qlik Sense.
13. If needed, add additional series. In the left panel in the Chart Designer, hover over Series and click the plus icon. Complete the remaining configuration steps as outlined above.

## Additional tips for configuring the chart

The above workflow shows you how to create a simple native chart and connect it to Qlik Sense data sources. Here are some extra tips to help you make the most out of native PixelPerfect charts.

### Labels and legends

You might need to configure labels and legends so that they appear correctly.

#### Changing the text

You can change the text shown in the labels and legend. You can do this by entering specific placeholders in the following properties:

- Labels: Open the Properties for the series, and add a placeholder to Label > Text Pattern.
- Legend: Open the Properties for the series, and add a placeholder to Legend Text Pattern.

The placeholders instruct PixelPerfect to generate dynamic text with commonly needed values. For example, to use the name of the series, enter {S}. To enter the name of specific field values, enter {A}.

For a full list of placeholders you can use, see [*Text definition placeholders for native PixelPerfect charts*](pixelperfect-text-definition-placeholders.htm).

#### Turning labels and legends off

If your chart has a lot of data, it is often preferred to turn labels off (they are turned on by default). To turn off labels in a series, change the Labels Visibility setting in the Properties to False.

To turn the legend off, you need to return to the chart's global Properties in the Chart Designer. In the left-side panel, click Chart. In the Properties menu on the right side, expand Legend and set Visibility to False.

### Charts with more than one series

Some native PixelPerfect charts will require you to add more than one series to the chart to visualize all the data. Common examples are grouped or stacked bar charts, stacked line charts, and nested pie charts. You might also need to add multiple series if you want to create a chart that, in Qlik Sense, would require more than one dimension or measure.

For example, to create a stacked bar chart with one independent grouping (Product Group) and two variable metrics (Sales and Margin), you would need to create two series:

- Sales, with an Argument Data Member of Product Group and a Value of Sales
- Margin, with an Argument Data Member of Product Group and a Value of Margin

### Editing a chart with a user-defined series

Some additional steps are required to edit an existing PixelPerfect chart that is configured with a user-defined series. When you open the Chart Designer, the Properties that are initially shown are the global properties for the chart. To edit the elements that are defined in the visualization, you need to first select the series in the left-side panel.

Do the following:

1. In the Chart Designer, double-click Series in the left-side panel.
2. Select the series you want to edit.
3. Edit the Properties on the right side.

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

The following charts are shown as options when creating a PixelPerfect chart with manual series splitting.

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

## Example - Creating a simple native bar chart

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

In this example, we walk through a simple example of adding a native PixelPerfect bar chart to a report template.

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Tables.
4. Expand the Dashboard sheet, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Sales per Region chart.

   The data binding is added.
5. From the toolbox panel on the left side of the designer, drag a ![Chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pixelperfect_chart.svg) Chart onto the Detail1 band.

   Blank chart added to template. The image also shows the data source that will be used to bind to the chart.

   ![Report template with a blank Chart object added, along with the 'Field List' menu expanded on the right side panel showing the data binding we will use to connect to the chart](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-user-defined-blank.png "Click to view full size")
6. Select the blank chart and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer.
7. Under Chart Tasks > Data Member in the menu, select the Sales per Region table.
8. Inside the chart, click Run Designer....
9. In the left panel in the Chart Designer, hover over Series and click the plus icon. In the menu, select Bar to create a bar chart series.

   The Properties for the new series are shown on the right side.
10. For Argument Data Member, use the drop down menu to select Region.

    Tip noteIn this context, selecting the Argument Data Member is similar to selecting a [dimension](#glossary-2 "Glossary term") in Qlik Sense.
11. Expand Value Data Members. For Value, select Sales.
12. In this case, we want to remove the labels and legend. Do both of the following:

    - In the Properties for the series, change the Labels Visibility setting to False.
    - In the Properties for the entire chart (select Chart in the left panel), expand Legend and set Visibility to False.

    Chart Designer with the bar chart series configured to use Qlik Sense data sources

    ![Chart Designer with placeholder chart at center, and properties used to configure it on the right panel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-series-data.png "Click to view full size")
13. Add a title to the chart. In the left panel in the Chart Designer, hover over Titles and click the plus icon. Select a title position using the popup menu.
14. In the Properties for the title, enter Sales By Region for the Text property.
15. Click OK to exit the Chart Designer.
16. Increase the size of the chart and the Detail1 band.
17. In the top right corner, click Save template.
18. Click Preview report. Download the report and open it.

Chart preview

![Generated report showing a chart created by manually adding one data series. In this case, the charts shows a bar chart with sales values for each region](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-native-chart-user-defined-preview.png "Click to view full size")

## Learn more

- [*Text definition placeholders for native PixelPerfect charts*](pixelperfect-text-definition-placeholders.htm)
