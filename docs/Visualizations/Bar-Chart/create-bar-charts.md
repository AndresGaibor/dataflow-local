---
title: "Creating bar charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/create-bar-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating bar charts

The bar chart is suitable for comparing multiple values. The [dimension](#glossary-0 "Glossary term") axis shows the category items that are compared, and the [measure](#glossary-1 "Glossary term") axis shows the value for each category item.

You can create a bar chart on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty bar chart to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Click Add measure and select a measure or create a measure from a field.

In a bar chart you need at least one measure.

You can include up to two dimensions and one measure, or one dimension and up to 15 measures in a bar chart. Each bar corresponds to a dimension, and the values of the measures determine the height or length of the bars.

You can also create a bar chart with no dimension and up to 15 measures. In this case, one bar is displayed for every measure. The value of the measure determines the height or length of a bar.

Creating a bar chart

| Dimensions | Measures | Result |
| --- | --- | --- |
| 1 dimension | 1 measure | A simple bar chart with one bar for each dimension value. |
| 2 dimensions | 1 measure | A grouped or a stacked bar chart with one bar for each value of the two dimensions. |
| No dimension | up to 15 measures | A simple bar chart with one bar for each measure. |
| 1 dimension | up to 15 measures | A grouped or a stacked bar chart with one bar for each value of each measure. With 1 dimension and 2 measures, you can switch to the butterfly chart configuration. See [*Changing the presentation format of the bar chart*](#Presentation). |

You can also change the chart's appearance in the advanced edit mode.
 For information about styling see [*Styling the bar chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Changing the presentation format of the bar chart

You have the following format options for your bar chart:

- Simple chart
- Grouped
- Stacked
- Butterfly

The simple chart and Grouped options are used by default, depending on the data you add to the chart. Additional options are available as applicable.

Each of the above formats can be presented in Horizontal or Vertical arrangement.

Presentation formats for bar chart

| Presentation format | Data required | Result |
| --- | --- | --- |
| Simple chart | Either of the following:   - 1 dimensions and 1 measure - 0 dimension and 1-15 measures | Data is presented in side-by-side fashion. As applicable, measures are differentiated by color. |
| Grouped | Either of the following:   - 2 dimensions and 1 measure - 1 dimension and 2-15 measures | Data is presented in groups in side-by-side fashion. Groups are differentiated by color. |
| Stacked | Either of the following:   - 2 dimensions and 1 measure - 1 dimension and 2-15 measures | Data is stacked together and differentiated by color. |
| Butterfly | 1 dimension and 2 measures | Data is presented in two separate, mirrored views along the same axis. |

Do the following:

1. Create a bar chart with one of the data requirements shown in the above table.
2. Open the properties panel and expand Appearance > Presentation.
3. Select the desired option (Grouped, Stacked, or Butterfly).
4. Select whether to display chart in a Horizontal or Vertical arrangement.

### Video - configuring a butterfly chart

This video shows an example of how you can create a butterfly chart.

### Considerations for Butterfly format

- Only for charts with one dimension and two measures.
- Only non-negative values are shown.
- If all values are negative, a disclaimer is shown in the center of the chart. If any value is negative, a disclaimer is shown in the footnote of the chart.
- The measure axis of the second measure is also used to show the negative part of a trend line for the first measure, or a reference line with a negative value.
- When defining a custom range for the X-axis, you can only set a maximum value. It is not possible to set a minimum value. This setting is configured under Appearance > X-axis.

## Styling the bar chart

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, font size, and color for the following text elements:

   - Axis title: Style the titles on the axes.
   - Axis label: Style the labels on the axes.
   - Value labels: Style the labels which display the measure value for each dimension value.

     When using the Stacked presentation option, this setting controls Segment labels (measure values for each dimension value) and Total labels (combines the measure values for each dimension value).
   - Legend title: Style the title of the legend.
   - Legend labels: Style the labels of the individual legend items.

### Customizing the background

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the origin must be added to the allowlist in your tenant's Content Security Policy. Add the origin with the img-src directive. This is done in the Administration activity center by an administrator.

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

### Customizing the bar segment outline and bar width

You can adjust the outline surrounding each bar segment in the chart, as well as the width of the bars.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Outline, set the thickness and color of the outlines.
4. Adjust the slider for Bar width to set the width of the bars.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Configuring a continuous or discrete scale

### Setting a continuous scale

A continuous scale allows you to plot time-based data in a view that accurately shows the distance in time between each data point.

You should set a continuous scale if your bar chart visualizes a time-based dimension with data that might not be measured over equal time intervals.

For more information about continuous scales, see [*Creating time-aware charts*](../time-aware-charts.htm).

Do the following:

1. In the properties panel, click the Appearance tab.
2. In the X-axis section, switch Continuous from Auto to Custom, and then check Use continuous scale. This explicitly sets the chart to use a continuous scale.

   The chart is compressed and the data points and labels are readjusted.
3. Adjust the bar width as follows:

   1. Set Period to reflect the time grain used in the chart dimension. You have the following options:

      - Auto: Automatically detect the period.
      - Seconds
      - Minutes
      - Hours
      - Days
      - Weeks
      - Months
      - Years
      - Number: Allows you to set a numeric period value rather than referencing time-based units.
      - None: The chart does not have a consistently measured period.
   2. Under Step size, set the number of time units, corresponding to your specified Period.
   3. In the ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling panel, under Chart, use the slider to adjust the Bar width. See [*Customizing the bar segment outline and bar width*](#BarWidth).

### Setting a discrete scale

Use a discrete scale when your bar chart uses a category-based dimension or a time-based dimension with data recorded at consistent time intervals.

Do the following:

- In the properties panel, under Appearance > X-axis, turn the Continuous setting to Custom and turn off Use continuous scale.

The chart is now explicitly set to use a discrete scale.

## Adding trend lines

You can add trend lines to the chart. Use trend lines to visualize how data changes over time.

For more information about trend lines, see [*Trend lines*](../../Measures/trend-lines.htm).

Do the following:

1. In the properties panel, expand the Data section.
2. Under Measures, expand the measure for which you are adding trend lines.
3. Under Trend lines, click Add trend line.
4. Define the Label and Type for the trend line.
5. Use the Colors slider to define Custom or Auto coloring.
6. Use the checkbox to toggle a Dashed appearance on or off.

## Showing or hiding dimensions and measures depending on a condition

You can show or hide a dimension or measure depending on if a condition is true or false. This is known as a show condition, and is entered as an expression. The dimension or measure is only shown if the expression is evaluated as true. If this field is empty, the dimension or measure is always shown. Expand the dimension or measure in the Data section of the properties panel and enter an expression under Show dimension if or Show measure if.

Information note

Custom tooltips are disabled for a bar chart if any of the dimensions in the chart are using a show condition.

Let's say you have a dataset with the fields City, Manager, and Sales, among others. You could configure your bar chart so that aggregated sales are displayed along a dimension called City. You can add a second dimension, Manager, but only organize the data by this dimension if there are more than three manager names associated with your sales data.

Do the following:

1. Drag a bar chart from the assets panel onto the sheet.
2. Add City as a dimension.
3. Add Manager as a second dimension from the properties panel.
4. Add Sum(Sales) as a measure.
5. In the properties panel, expand the dimension Manager. Under Show dimension if, add the following expression:

   Count(distinct Manager)>3

If your data only contains two manager names, the bar chart will not organize sales by manager, since the expression is evaluated as false. If the data contains three or more unique Manager values, sales will be organized by both City and Manager.

## Working with shapes

With shapes, you can add points and lines as separate items in the chart. Shapes allow you to enhance your dimension and measure data with special information that helps with analysis. For example, you could add a point to highlight a specific dimension value, or draw a line between the highest and lowest points for a key performance indicator.

### Adding a point

Do the following:

1. In the properties panel, expand Add-ons > Shapes.
2. Click Add shape, and select Point.
3. Optionally, define a Label for the point using text or an expression.
4. Under Dimension value, type the dimension value for which to add the point. You can also define the value with an expression.
5. In the Measure input drop down menu, select one of the following and define the value below the menu:

   - Measure value: Define the measure value for which to add the point, either as a simple value or an expression. For example, you could use a [set analysis](#glossary-3 "Glossary term") expression.
   - Measure index: Define the measure from which the measure value is extracted. This can be provided as a simple value or an expression. For example, use 0 for the first measure in the chart, 1 for the second measure in the chart, and so on.
6. Set the Symbol to use for the point. The default is Circle.
7. Adjust the Label position if needed. The label can be displayed above or below the point.
8. Set color and opacity using the following settings. You can also configure these elements to have no color.

   - Point color
   - Outline color
   - Label color
9. Use the Colored background check box to add a background for the label, if defined. When this option is turned on, the defined Label color is used for the background, and the label text switches to a color that best contrasts the background.
10. Use the sliders to adjust the Outline width and Data point size.

### Adding a line

You can add a line as a series of points. The line connects each point that you define for it.

Do the following:

1. In the properties panel, expand Add-ons > Shapes.
2. Click Add shape, and select Line.
3. Optionally, define a Label for the line using text or an expression. This does not appear in the chart but helps with identification when you have multiple lines and points.
4. By default, data points are not highlighted on the line. To highlight them, turn on Show data points at the bottom of the settings for the line. With this option turned on, more point settings are shown.
5. To add a point, click Add point.
6. Under Dimension value, type the dimension value for which to add the point. You can also define the value with an expression.
7. In the Measure input drop down menu, select one of the following and define the value below the menu:

   - Measure value: Define the measure value for which to add the point, either as a simple value or an expression. For example, you could use a [set analysis](#glossary-4 "Glossary term") expression.
   - Measure index: Define the measure from which the measure value is extracted. This can be provided as a simple value or an expression. For example, use 0 for the first measure in the chart, 1 for the second measure in the chart, and so on.
8. Adjust the point's appearance using the following settings. These settings become visible when Show data points is turned on.

   - Label: Set a textual label for the point.
   - Symbol: Set the shape of the point. The default is Circle.
   - Label position: Choose whether to show the label above or below the point.
   - Point color: Set the color of the point.
   - Outline color: Set the color of the point outline.
   - Label color: Set the color of the label text. If Colored background is turned on, this setting instead controls the background behind the label.
   - Outline width: Set the width of the point outline.
   - Data point size: Set the overall size of the point.
   - Colored background: Add a background for the label, if label text has been defined. When this option is turned on, the defined Label color is used for the background, and the label text switches to a color that best contrasts the background.
9. Add one or more points as needed, using the above steps.
10. Set the Line color, including opacity.
11. Use the slider to adjust the Line thickness.
12. Select the Line type, choosing between Solid or Dashed.
13. Use the Line curve drop down menu to select one of the following:

    - Linear: Each point is connected with straight lines.
    - Monotone: Each point is connected with curved lines.

## Learn more

- [*Bar chart*](bar-chart.htm#Bar)
- [*Comparing categories against a measure with a bar chart*](bar-chart-example.htm)
- [*Accumulating values over a dimension in a bar chart*](bar-chart-example2.htm)
- [Interpreting Bar Charts](/lnk/Interpreting_bar_charts)

Related learning:

- [Interpreting Bar Charts](/lnk/Interpreting_bar_charts)
