---
title: "Creating combo charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/ComboChart/create-combo-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating combo charts

The combo chart is suitable for comparing two sets of [measure](#glossary-0 "Glossary term") values that are usually hard to compare because of the differences in scale. It is basically a bar chart combined with a line chart.

You can create a combo chart on the [sheet](#glossary-1 "Glossary term") you are editing. In a combo chart, you need at least one [dimension](#glossary-2 "Glossary term") and one measure.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty combo chart to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Click Add measure and select a measure or create a measure from a field. Select to show the measure as a bar.
5. Add another measure by selecting Add under Height of line. Enter an expression, or master measure item, or a field with an aggregation function applied. By default a line will appear as the measure.
6. When you are done adding measures, configure each measure to display as bars, lines, or markers. For more information, see [*Configuring the presentation of measures*](#PresentationMeasures).

You can only have one dimension, but you can continue adding up to 15 measures. You can only have two measure axes though. This means, if you add three or more measures with a large difference in value range it can be hard to display all measures with a good distribution of values.

When you have created the combo chart, you might want to adjust its presentation.
For information about styling see [*Styling the combo chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the combo chart

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the labels shown on the chart depends on how you configure the measure values to be displayed, as well as other chart-specific settings and label display options. Configure a measure to be shown as Bars, Line, or Marker by expanding the measure under Data > Measures, and clicking  More properties. Configure additional chart and label options under Appearance > Presentation.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, expand the Bars section. This section appears if any of the measures are being displayed as bars.
5. Under Bar labels, style the labels for measure values configured as Bars. You can select the font, font size, and color.

   When using the Stacked presentation option, this setting controls Segment labels (measure values for each dimension value) and Total labels (combines the measure values for each dimension value).
6. Expand the Lines section of the Chart tab. This section appears if any of the measures are being displayed as lines.
7. Under Point labels, style the labels for measure values configured as Line. You can select the font, font size, and color.
8. On the Chart tab, expand the Markers section. This section appears if any of the measures are being displayed as markers.
9. Under Marker labels, style the labels for measure values configured as Marker. You can select the font, font size, and color.
10. On the Chart tab, set the font, font size, and color for the following text elements:

    - Axis title: Style the titles on the axes.
    - Axis label: Style the labels on the axes.
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

If your combo chart contains measure data represented as bars, you can adjust the outline surrounding each bar segment in the chart, as well as the width of the bars.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, expand the Bars section.
4. Under Outline, set the thickness and color of the outlines.
5. Adjust the slider for Bar width to set the width of the bars.

### Customizing the lines and data points

If your combo chart contains measure data represented as lines, you can customize the appearance of the lines and data points in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, expand the Lines section.
4. Under Data point size, adjust the slider to change the size of the data points in the chart.
5. Under Line options, adjust the line thickness, line type (solid or dashed), and line curve (linear or monotone).

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Configuring grid line spacing

You can change the placement of grid lines on the chart. Select whether to show grid lines based on the primary or secondary axis, and adjust the spacing. You can also turn off grid lines if desired.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Expand Appearance > Presentation.
3. Toggle Grid line spacing from Auto to Custom.
4. Use the drop down menu to select whether the grid lines are placed along the Primary axis or Secondary axis.

   Depending on the scale used by each axis, you might not notice any difference between these settings.
5. Use the second drop down menu to select the spacing, or choose No lines to remove grid lines.

## Configuring the presentation of measures

Optionally, you can change the presentation of measures between bars, lines, or markers. Additional options are also available.

Do the following:

1. In the properties panel, under Measures, select More Properties in a measure.
2. Choose the Presentation of the measure. You can:

   - Change the presentation of measures between bars, lines, or markers. For markers you can choose between several different shapes.
   - Select drop-down options to switch between the Primary axis or the Secondary axis.

     Tip noteThe primary axis is on the left side of the chart, and the secondary axis in on the right side. Right and left axes are reversed if Right-to-left is turned on in application settings (see [*Styling an application*](../../Apps/style-app.htm)).

### Adding bar and marker labels

If any measures in the chart are configured as bars or markers, you can show or hide their value labels. Bar and marker labels can be configured separately from one another.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Presentation, do one or both of the following:

   - Set Bar labels to Auto.
   - Set Marker labels to Auto.

### Adding segment and total labels

For combo charts with a specific configuration, you can add segment and total labels. Segment labels show values for each measure segment in a chart. Total labels show values for an entire set of measures arranged along a single axis.

You can add segment and total labels if all of the following apply:

- Two or more measures on the same axis are configured as bars.
- The combo chart uses the Stacked presentation option. This setting is located under Appearance > Presentation.

  Tip note

  The Stacked presentation option becomes available when two or more measures have the following settings under Data > More properties:

  - The measures are configured as Bars.
  - The measures appear on the same axis.

  For more information, see [*Configuring the presentation of measures*](#PresentationMeasures).
- Bar labels are set to Auto.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Presentation, set Bar Labels to Auto.
3. Do one or both of the following:

   - Set Segment labels to Auto.
   - Set Total labels to Auto.

### Changing line representation

If you have one or more lines on the same axis in the chart, you can customize them as follows:

- Under Appearance > Presentation in the properties panel, you can configure the line portion of a combo chart as an Area chart.
- If you have multiple lines in the chart, you can change whether and how their data is stacked. These properties are available under Appearance > Presentation:

  - Stacked area: Stack area values by adding them together.
  - Stack positive and negative values separately: When stacking areas, leaving this option unchecked will combine the area values as per their actual sign (positive or negative).

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

- [*Combo chart*](combo-chart.htm)
- [*Creating combo charts*](combo-chart-example.htm)
- [Interpreting Combo Charts](/lnk/Interpreting_combo_charts)

Related learning:

- [Interpreting Combo Charts](/lnk/Interpreting_combo_charts)
