---
title: "Creating box plots"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/BoxPlot/create-box-plots.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating box plots

The box plot is suitable for comparing range and distribution for groups of numerical data, illustrated by a box with whiskers, and a center line in the middle. The whiskers represent high and low reference values for excluding outlier values.

You can create a box plot on the [sheet](#glossary-0 "Glossary term") you are editing.

In a box plot you need to use one or two [dimensions](#glossary-1 "Glossary term"), and one [measure](#glossary-2 "Glossary term"). If you use a single dimension, you will receive a single box [visualization](#glossary-3 "Glossary term"). If you use two dimensions, you will get one box for each value of the second, or outer, dimension.

By default, the Standard (Tukey) preset is used.

Information noteYou cannot use calculated dimensions in a box plot.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty box plot to the sheet.
3. Add the first dimension.

   This is the inner dimension, which defines a box.
4. Add a second dimension.

   This is the outer dimension, which defines the boxes shown on the dimension axis.
5. Click Add measure and create a measure from a [field](#glossary-4 "Glossary term"). The measure does not have to contain an aggregation.

When you have created the box plot, you may want to adjust its appearance and other settings in the [properties](#glossary-5 "Glossary term") panel.
For information about styling, see [*Styling the box plot*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the box plot

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

## Changing the definition of the box plot

You can use one of the three presets, found under Box plot elements in the properties panel, to define your box plot.

- Standard (Tukey)

  This preset is based on the original box plot definition by J. Tukey. The center line represents the median (second quartile), and the box start and end points represent the first and third quartiles. Whisker length can be set to 1, 1.5 or 2 inter-quartile ranges. An inter-quartile range represents the difference between the first and third quartiles.
- Percentile-based

  This preset is also defined with the box start and end points representing the first and third quartiles, and the center line representing the median, but the whisker length is adjusted by setting a percentile based whisker position.
- Standard deviation

  This preset is based on standard deviations, with the center line representing the average value, and the box start and end points representing one standard deviation variance. You can set the whisker length to a multiple of standard deviations.

You can also define a custom box plot where you set the value of each box plot element using an expression.

## Learn more

- [*Box plot*](box-plot.htm)
- [*Visualizing range and distribution of numerical data with a box plot*](box-plot-example.htm)
- [Interpreting Box Plots](/lnk/Interpreting_box_plots)

Related learning:

- [Interpreting Box Plots](/lnk/Interpreting_box_plots)
