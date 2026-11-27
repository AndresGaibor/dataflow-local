---
title: "Changing the appearance of a visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/change-appearance-of-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Changing the appearance of a visualization

The Appearance section in the [properties](#glossary-0 "Glossary term") panel offers several options to set and modify the appearance of a visualization.

Many of the settings have Auto options that support an optimal presentation of the visualization, taking into account the number of [dimensions](#glossary-1 "Glossary term") and measures and the type of data used. Normally, you do not need to change these settings, unless you have a special reason for doing so, for example, when space is very limited.

Appearance can be affected by the sorting of the dimensions and measures. For more information, see [*Change the sorting of a visualization*](change-sorting-of-visualization.htm).

## General

Show titles: On by default in all visualizations except filter panes and text & image visualizations. Filter panes have the name of each dimension and in most cases do not need any additional title. The text & image visualization includes an editing toolbar with many options to format the text, and therefore the title [field](#glossary-2 "Glossary term") can be used for other purposes.

Title, Subtitle, and Footnote: Apart from the obvious use of title, subtitle, and footnote as text fields, you can use these fields to also display an expression, which provides additional information that complements the measure in the visualization. You could, for example, show the totals in the title field, so that the totals of the selected values are always available.

Example:

In the following image, the total sales are calculated and used in the title. When a selection is made, the total sales are updated accordingly.

![Pie chart for Total Sales.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CalculatedTitle.png)

The following string was used to add the Total Sales expression to the field Title:

='Total Sales: $'& Round(Sum(Sales)/1000000, 0.1) & 'M'.

Because the title field is primarily a text field, it is necessary to start the string with an equals sign (=), to signify that the strings contains an expression.

Because 'Total Sales: $' is a text string when it is used in an expression, the string must be surrounded by single quotation marks.

& is used to concatenate the string and the expression.

Round(Sum(Sales)/1000000, 0.1)  is the expression. The [aggregation](#glossary-3 "Glossary term") Sum(Sales) is divided by 1000000 and the function  Round (x,0.1) reduces the number of decimals to one.

& 'M', finally, concatenates the expression with the unit M for million.

For the title there are three options for adding an expression:

- Directly in the title field of a visualization. Start the string with an equals sign (=).
- Directly in the box Title under Appearance in the properties panel. Start the string with an equals sign (=).
- Through the expression editor in the box Title. Click ![Open Expression editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor. No equals sign is needed.

For the subtitle and footnote only the last two options are available.

Show details: Hide by default. When set to Show, users can click ![Info](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info.svg) when analyzing to view details such as descriptions measures and dimensions.

## Presentation and styling

Many of the presentation settings only apply to a certain visualization.

Presentation settings in visualizations

| Visualization | Description |
| --- | --- |
| Bar chart | Set the bars to be displayed grouped or stacked, vertically or horizontally. |
| Box plot | Select to show whisker ticks and grid lines. You can show the visualization vertically or horizontally. |
| Combo chart | Select whether to show labels for measures added as markers. You can select to show grid lines based on primary or secondary axis, and adjust spacing between them. |
| Distribution plot | Select to show point, background or both. You can show the visualization vertically or horizontally. |
| Funnel chart | Set the funnel mode. |
| Gauge | Set the gauge to be displayed as a radial or a bar. You can set range limits and use segments with limits. |
| Grid chart | Set the layout, symbol size, and symbol shapes. |
| Histogram | Select to show grid lines. |
| Line chart | Set the line chart to be displayed as a line or an area. |
| Org chart | Set the presentation mode. |
| Pie chart | Set the pie chart to be displayed as a pie or a donut. |
| Sankey chart | Set the node padding and node width. |
| Scatter plot | Turn on/off navigation. Set the size of the bubbles in a scatter plot. Set the compression resolution for large data sets in scatter plot. |
| Straight table | Set the totals to be displayed at the top, bottom, or not at all. |
| Treemap | Set the headers, labels, overlay labels, and leaf values. Select to show the data values. |

Example:

A bar chart with two dimensions is by default presented with the bars grouped.

![Bar chart with grouped bars.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartGrouped.png "Click to view full size")

Let us assume that you want to compare the total monthly quantity for these years. Then it would be a good idea to switch to a stacked bar chart.

In the properties panel, under Appearance > Presentation there is an option Stacked.

With stacked bars it is easier to compare the quantity between different months.

![Bar chart with stacked bars.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartStacked.png "Click to view full size")

Now it is quite easy to compare the quantities per month. There is a legend to display the years.

Under Colors and legend, Show legend is set to Auto, which means that the legend is displayed when there is enough space. In the properties panel, you can also set where to display the legend and whether to display the legend title.

There is only data for the first half of 2013 (red bars).

![Bar chart with stacked bars and a legend displayed.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartLegend.png "Click to view full size")

### Styling

Apply additional customization to the visualization by using the styling panel. The styling panel is available in the properties panel. Under Appearance > Presentation, click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.

For more information, see [*Applying custom styling to a visualization*](style-visualization.htm).

## Colors and legend

The Colors and legend section of the properties panel sets your color and legend options. Qlik Sense automatically colors visualizations as they are added to your [sheets](#glossary-4 "Glossary term"). As a best practice, it is recommended to add or change colors only when it serves as purpose in the visualization. Too many colors or indistinct color choices can make visualizations less clear.

You can manually set the colors and legends by deselecting the Auto option and selecting your color preferences. Qlik Sense enables you to color your visualizations by:

- Single color
- Multiple colors
- Dimension
- Measure
- Master items
- Expression

For more information on different visualization coloring options, see [*Coloring a visualization*](../Colors/color-a-visualization.htm). For examples of each of these methods of coloring visualizations and the settings used can be found, see [*Examples of visualization color settings*](../Colors/examples-visualization-colors.htm).

## X-axis and Y-axis

For both the y-axis and the y-axis, you have options for deciding what combination of labels and title to display, as well as their orientation and position. Sometimes it may feel unnecessary to have labels and/or a title, because the visualization is self-explanatory and then it would be good to be able to hide them. Furthermore, when you create a visualization that is very small, for example, three by three squares, the labels are automatically hidden.

Range: The measure axis (usually the y-axis) has an option to set the range of the axis. By default, the range is adjusted according to the highest positive or the lowest negative measure value, but if, for example, a single measure value is much larger than all the other values, you may want to set a range that is suitable for the lower values. In the properties panel, under Appearance > Y-axis <measure name>, there is a button for Range, which is set to Auto. Click the button to switch to Custom. Now you can set the range for Max, Min, or both. In a bar chart, the bars that are out of the range are cut diagonally to indicate that they are out range. In a line chart, only the parts that are within the range are visible.

Label orientation: You can change the orientation of data labels on the dimensions axis (usually the x-axis). In the properties panel, under Appearance > X-axis <dimension name>, there is a drop-down menu for label orientation. By default, this is set to Auto. If there is not enough room for a label to fully appear on the chart, it will be truncated with an ellipsis. The following options are available:

- Auto: Automatically selects one of the other options depending on the space available on the chart.
- Horizontal: Labels are arranged in a single horizontal line.
- Tilted: Labels are stacked horizontally at an angle.
- Layered: Labels are staggered across two horizontal lines.

Examples of layered and tilted labels

![Layered labels and tilted labels.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_Layered_Labels.png "Click to view full size")

## Learn more

- [*Properties panel*](../Sheets/navigating-sheets.htm#Properti)
- [How do I configure a label to include an expression?](/lnk/How_configure_label_include_expression)

Related learning:

- [How do I configure a label to include an expression?](/lnk/How_configure_label_include_expression)
