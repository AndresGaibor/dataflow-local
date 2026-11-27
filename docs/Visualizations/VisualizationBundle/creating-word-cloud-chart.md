---
title: "Creating word cloud charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-word-cloud-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating word cloud charts

The Word cloud chart (Word cloud) lets you visualize text data. Text values are displayed with their size based on a [measure](#glossary-0 "Glossary term") value. The measure can be anything you want to measure against, for example: times used, alphabetically, by importance, or by context. You can customize your chart with different shapes, fonts, layouts, and color schemes. It is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a word cloud on the [sheet](#glossary-1 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Legacy, drag a Word cloud object to the sheet.
3. Click the Add dimension button and select the dimension.
4. Click the Add measure button to select the measure of the chart.

Once a dimension and a measure have been selected, the word cloud chart displays automatically.

## Changing the appearance of the word cloud

You can customize your word cloud with one or more features.

### Changing the orientation

You can set the number of orientations with Appearance  > Design > Orientations in the [properties](#glossary-2 "Glossary term") panel. You can set an integer from 1 to 10.

- 1 will display all words in the same direction, set with Appearance  > Design > Start angle.
- 2 will display words in two orientations, Appearance  > Design > Start angle and Appearance  > Design > End angle.
- 3-10 will display words in the same number of orientations between Appearance  > Design > Start angle and Appearance  > Design > End angle.

Example:

A word cloud chart displaying food items in different orientations.

![A word cloud chart displaying food items in differnet sizes, orientation, and colours.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/w5_629x383.png "Click to view full size")

### Adjusting the start and end angles

You can adjust the starting point (angle) parameter of the word cloud under Appearance  > Design > Start angle, and the end point under Appearance  > Design > End angle in the properties panel. The angles can have positive or negative numbers.

### Changing font size

You can set maximum word font sizes under Appearance  > Design > Font max size and the minimum under Appearance  > Design > Font min size in the properties panel.

If you set a large font size, this can result in the larger words not being displayed in the chart as they do not fit.

### Changing scale

The word could chart scale can be either in linear or in log scale. Select scale Linear or Log under Appearance  > Design > Scale in the properties panel. Only positive values can be used for the log scale. Zero or negative values return nothing.

### Setting custom ranges

You can also specify a range of colors or select from a predefined color scheme.

Do the following:

1. Click Appearance > Design in the properties panel.
2. Ensure that the Enable color range is set to On (default).
3. Click the color palette beside From, and choose a color.
4. Click the color palette beside To, and choose a color.

You can set your own color range by clicking the easel symbol in the color palette, and selecting a color. You can also enter a color code string in the field next to the easel symbol. The colors should be valid CSS colors.

Do the following:

1. Click Appearance > Design in the properties panel.
2. Move the Enable custom range slide button to the left to turn the option off.
3. Select a color scheme under Scale color.
![A word cloud chart displaying food items in custom colors.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/w7_592x332.png)

A word cloud chart displaying food items in different sizes and colors.

### Formatting numbers

It is possible to format the measure value. Different formatting can be applied to the same value, for example as money, date, duration. The chart updates to reflect the changed number type.

Do the following:

1. Click Data > Measures in the properties panel and click a measure.
2. Select applicable number formatting form the Number formatting menu.
3. Enter details in the panel fields. These display when choosing an option other than Auto when further configuring the chart.

## Using the styling panel to further customize the appearance

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

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

- [How do I configure a Visualization Bundle Word cloud chart?](/lnk/How_configure_Visualization_Bundle_Word_cloud_chart)
