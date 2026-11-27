---
title: "Creating distribution plots"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DistPlot/create-distribution-plots.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating distribution plots

The distribution plot is suitable for comparing range and distribution for groups of numerical data. Data is plotted as value points along an axis.

You can create a distribution plot on the [sheet](#glossary-0 "Glossary term") you are editing.

In a distribution plot you need to use one or two [dimensions](#glossary-1 "Glossary term") and one [measure](#glossary-2 "Glossary term"). If you use a single dimension, you will receive a single line [visualization](#glossary-3 "Glossary term"). If you use two dimensions, you will get one line for each value of the second, or outer, dimension.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty distribution plot to the sheet.
3. Add the first dimension.

   This is the inner dimension, which defines the value points.
4. Add a second dimension.

   This is the outer dimension, which defines the groups of value points shown on the dimension axis.
5. Click Add measure and create a measure from a [field](#glossary-4 "Glossary term").

[*Viewing the distribution of measure values in a dimension with a distribution plot*](distribution-plot-example.htm)

When you have created the distribution plot, you might want to adjust its appearance and other settings in the properties panel.
 For information about styling, see [*Styling the distribution plot*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the distribution plot

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

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Learn more

- [*Distribution plot*](distribution-plot.htm)
- [*Viewing the distribution of measure values in a dimension with a distribution plot*](distribution-plot-example.htm)
- [Interpreting Distribution Plots](/lnk/Interpreting_distribution_plots)

Related learning:

- [Interpreting Distribution Plots](/lnk/Interpreting_distribution_plots)
