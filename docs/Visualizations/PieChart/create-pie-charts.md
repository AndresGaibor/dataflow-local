---
title: "Creating pie charts and donut charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/PieChart/create-pie-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating pie charts and donut charts

The pie chart and the donut chart display the relation between values as well as the relation of a single value to the total. You can use a pie chart when you have a single data series with only positive values. You can use a donut chart when you have a single data series that includes negative values.

You can create a pie or donut chart on the [sheet](#glossary-0 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty pie chart to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Click Add measure and select a measure or create a measure from a field.
5. In the properties panel, expand the Appearance section.
6. Under Appearance > Presentation, select Pie or Donut.

The following settings are used by default in pie and donut charts.

- The top 10 sectors are presented in descending size order, clockwise.
- Colors are presented by dimension.
- Value labels are presented in percent.

After you have created the pie chart, you may want to add a radius measure or adjust its appearance and other settings in the properties panel.
 For information about styling, see [*Styling the pie chart or donut chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the pie chart or donut chart

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

   - Dimension label: Style the label for the dimension shown in the chart.
   - Dimension value label: Style the individual dimension values.
   - Value label: Style the labels which display the measure value (displayed as a value or relative percentage) for each dimension value.
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

### Customizing the outline and shape

You can customize the outline surrounding the chart, as well as the shape and thickness of the slices.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab of the styling panel, under Outline, set the thickness and color of the outlines of the slices.
4. Under Corner radius, set the roundness of the corners of the slices.
5. If the chart is configured as a donut chart, under Inner radius, set the size of the hole at the center of the chart.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Showing the legend

By default, the legend and dimension name are not displayed in pie charts. You can display the legend if needed.

Do the following:

1. In edit mode, select the pie chart.
2. In the properties panel, go to Appearance > Colors and legend.
3. Turn on Show legend.

## Learn more

- [*Pie chart and donut chart*](pie-chart.htm)
- [Interpreting Pie Charts](/lnk/Interpreting_pie_charts)

Related learning:

- [Interpreting Pie Charts](/lnk/Interpreting_pie_charts)
