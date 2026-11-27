---
title: "Creating grid charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-grid-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating grid charts

The grid chart (Grid chart) uses symbols of varying size sorted in a grid. The grid chart is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a grid chart on the [sheet](#glossary-0 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a Grid chart object to the sheet.
3. Click the Add Dimension button to select the x axis value of the chart.
4. Click the second Add Dimension button to select the y axis value of the chart.
5. Click the Add Measure button to select the metric being weighed.

The grid chart is now displayed with the dimensions and measures you selected.

## Sorting

Grid chart elements are automatically sorted alphabetically or numerically from smallest to largest on the x axis. You can change the sort order of either axes in the property panel.

Do the following:

1. In the property panel, go to Appearance>Sorting.
2. Click on a dimension.
3. Toggle Sorting from Auto to Custom.
4. You can choose any of these options:
   - Sort by expression: Ascending or Descending.
   - Sort numerically: Ascending or Descending.
   - Sort alphabetically: Ascending or Descending.

## Changing the appearance of the chart

You can customize the appearance of your grid chart.

Grid chart with stars. Star color and size is set by measure (Gross Sales).

![Grid chart with stars. Colour is set by measure to a gradient.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gridchart_stars.png "Click to view full size")

### Customizing the symbols

You can change the shape and size of the symbols from the Appearance>Presentation tab in the property panel:

- Use the Symbol size slider to change size.
- Use the Symbol dropdown to change symbol type.

### Placing labels on symbols

You can place the individual values of symbols directly onto the chart. From the Appearance> Presentation tab, toggle the Labels from Off to Auto.

### Using a grid chart as a heat map

You can change the layout of a grid chart to a heat map from the Appearance>Presentation tab in the property panel. From the Layout dropdown menu, choose:

- Standard: The chart will show individual symbols.
- Heatmap: The chart will display data in a grid with a legend ordered by color.

For a visual demo about using a grid chart as a heatmap chart, see [Creating a heatmap using a grid chart](https://share.vidyard.com/watch/pznWdVxeT4KgnACi6tZkcD).

### Changing the color scheme

You can change the color scheme of the symbols from the Colors and legend tab. Set Colors to Custom. From the dropdown menu, choose:

- Single color: You can choose any color.
- By dimension: Under Color scheme, you can change how many different colors are used.
- By measure: Under Color scheme, you can alter the color gradient. Click the Reverse colors check box to flip the gradient order. The colors used are based on your application theme.
- By expression: You can have a color code in the expression. Or, deselect the The expression is a color code check box, and you can alter the color gradient. Click the Reverse colors check box to flip the gradient order. The colors used are based on your application theme.

### Changing the range limits

You can customize the limits of the ranges if you color by measure or expression. The full range is defined by the value of the dimensions. Go to Appearance > Colors and legend > Range in the [properties](#glossary-1 "Glossary term") panel:

- Min: Defines the lower limit of the range.
- Max: Defines the upper limit of the range.

### Changing the scale of the axes

You can customize the presentation of the x and y axes. Go to Appearance > X-axis: [dimension] or Appearance > Y-axis: [dimension] in the properties panel. You can set:

- Labels and title: Select what labels and title to display.
- Label orientation: Select how to display the labels. The following options are available:

  - Auto: Automatically selects one of the other options depending on the space available on the chart.
  - Horizontal: Labels are arranged in a single horizontal line.
  - Tilted: Labels are stacked horizontally at an angle.
  - Layered: Labels are staggered across two horizontal lines.

  To view examples of label orientation, see [*X-axis and Y-axis*](../change-appearance-of-visualization.htm#X-axis).
- Position: Select where to display the dimension axis.
- Number of axis values:

  - Auto: The number of visible bars is determined by the number of dimensions and measures used.
  - Max: The number of visible bars is set to maximum.
  - Custom: When custom is selected, you can directly set the upper limit to the number of visible bars using Maximum number, or by entering an expression. Click Expression to open the Expression editor.
- Show grid lines: Select whether to display grid lines.

## Using the styling panel to further customize the appearance

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
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, font size, and color for the following text elements:

   - Axis title: Style the titles on the axes.
   - Axis label: Style the labels on the axes.
   - Value label: Style the labels which display the measure value for each dimension value.
   - Legend title: Style the title of the legend. The legend is only available for the Heatmap configuration.
   - Legend labels: Style the labels of the individual legend items. The legend is only available for the Heatmap configuration.

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

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

Related learning:

- [How do I configure a Visualization Bundle Grid Chart?](/lnk/How_configure_vizbundle_grid)
