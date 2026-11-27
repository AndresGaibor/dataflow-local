---
title: "Creating line charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/LineChart/create-line-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating line charts

The line chart is used to show trends over time. The [dimension](#glossary-0 "Glossary term") is always on the x-axis, and the [measures](#glossary-1 "Glossary term") are always on the y-axis.

You can create a line chart on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty line chart to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Click Add measure and select a measure or create a measure from a field.

In a line chart you need at least one dimension and one measure.

You can include up to two dimensions and one measure, or one dimension and up to 15 measures in a line chart.

Creating a line chart

| Dimensions | Measures | Result |
| --- | --- | --- |
| 1 dimension | 1 measure | A simple line chart with a single line. |
| 2 dimensions | 1 measure | A line chart with the first dimension on the X-axis, and a line for each value of the second dimension. |
| 1 dimension | up to 15 measures | A line chart with one line for each measure. |

When you have created the line chart, you may want to adjust its appearance and other settings in the properties panel. For information about styling, see [*Styling the line chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the line chart

You have a number of styling options available in the properties panel.
Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to style the text, background, data point size, and lines at the chart level (for the entire chart). The styling panel contains various sections under the General and Chart tabs. You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel. Any customization you apply here overrides the styling set in the application theme.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, font size, and color for the following text elements:

   - Axis title: Style the titles on the axes.
   - Axis label: Style the labels on the axes.
   - Value label: Style the labels for the measure values that are configured as Lines.
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

### Customizing the data points at the chart level

You can set the size of the data points. The settings defined here apply to all measures in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Data point size, adjust the slider to change the size of the data points in the chart.

### Customizing the measure lines at the chart level

You can customize the appearance of the lines in the chart. The settings defined here apply to all measures in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. Switch to the Chart tab of the styling panel.
4. In the Line options section, adjust the line thickness, line type (solid or dashed), and line curve (linear or monotone).

### Styling each measure individually

Each measure line in the chart can be styled with separate settings. For each measure, you can customize the data point size, line thickness, line type, and line curve.

Do the following:

1. In the properties panel, expand the Data section.
2. Click the measure you want to customize.
3. Under Styling, click Add.
4. Adjust the data point size, line thickness, line type (solid or dashed), and line curve (linear or monotone).

Repeat these steps for each individual measure you need to customize separately from the application theme or chart-level style settings.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Showing or hiding dimensions and measures depending on a condition

You can show or hide a dimension or measure depending on if a condition is true or false. This is known as a show condition, and is entered as an expression. The dimension or measure is only shown if the expression is evaluated as true. If this field is empty, the dimension or measure is always shown. Expand the dimension or measure in the Data section of the properties panel and enter an expression under Show dimension if or Show measure if.

Information noteCustom tooltips are disabled for a line chart if any of the dimensions in the chart are using a show condition.

Information noteTime series forecasting is not available if any of the dimensions or measures in the line chart use a show condition.

Let's say you have a dataset with the fields Sales, Quarter, Year, and Order Number, among others. You could configure your chart so that sales are displayed along a time-based dimension for yearly aggregations. You can add a second dimension for quarterly aggregations but only organize the data by this dimension if the total number of orders received by your company has reached a target goal of 100,000.

Do the following:

1. Drag a line chart from the assets panel onto the sheet.
2. Add Quarter as a dimension.
3. Add Year as a second dimension from the properties panel.

   Each distinct year in the data model becomes a separate line in the chart.
4. Add Sum(Sales) as a measure.
5. In the properties panel, expand the dimension Manager. Under Show dimension if, add the following expression:

   Count([Order Number])>100000

If your data contains 50,000 order records, the chart will not organize sales by quarter, since the expression is evaluated as false. If the data contains 100,000 or more order records, sales will be organized by both Year and Quarter.

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

## Adding images within the chart

You can add images to align with dimensions in the chart. Images can be added onto measure values or anywhere on the measure axis. Images can be dynamically sized based on expressions.

Do the following:

1. In the properties panel, expand Add-ons > Images.
2. Click Add image.
3. Select a Source. You have the following options:

   - Media library: Click ![Select an image](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg), select an image, and click Insert. You can also upload new images to the media library, and then use them.
   - URL: Enter a URL or expression to define the URL.

     Information note

     To add an image from a URL, the origin must be added to the allowlist in your tenant's Content Security Policy. Add the origin with the img-src directive. This is done in the Administration activity center by an administrator.

     For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).
4. Under Dimension value, specify the dimension value where the image will appear.

   For charts with multiple dimensions, you must use a value from the Group dimension.
5. Under Measure input, select an option for where on the measure axis to insert the image:

   - Measure index: Specify the number of the measure onto which to place the image. Use 0 for the first measure, 1 for the second, and so on.
   - Measure value: Specify a value or expression defining the location for the image on the measure axis. This can be anywhere on the axis and does not need to correspond to the actual value of a measure.

   For charts with multiple dimensions, Measure index is not available and you can only specify a measure value.
6. Under Size, select Simple or Custom.

   With Simple, you define the size using a single slider.
7. With Custom, you can specify a Width and Height (rectangle) or Radius (circle). Expressions are supported. For example, images could be dynamically sized depending on a measure value.
8. Under Shape, select Rectangle or Circle.
9. Set the Opacity using the slider.
10. Adjust the Position of the image.

## Learn more

- [*Line chart*](line-chart.htm)
- [*Time series forecasting with the line chart*](timeseries-forecast.htm)
- [*Adding trend and reference lines to visualizations*](../add-trend-and-reference-lines.htm)
- [Interpreting Line Charts](/lnk/Interpreting_line_charts)
- [How do I forecast based upon time series data in Qlik Cloud?](/lnk/How_forecast_timeseries_data_qlikcloud)

Related learning:

- [Interpreting Line Charts](/lnk/Interpreting_line_charts)
- [How do I forecast based upon time series data in Qlik Cloud?](/lnk/How_forecast_timeseries_data_qlikcloud)
