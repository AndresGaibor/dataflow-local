---
title: "Creating bullet charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/BulletChart/create-bullet-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating bullet charts

The bullet chart (Bullet chart) displays a gauge with extended options. Bullet charts can be used to visualize and compare performance of a [measure](#glossary-0 "Glossary term") to a target value and to a qualitative scale, such as poor, average, and good.

You can create a bullet chart on the [sheet](#glossary-1 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty bullet chart to the sheet.
3. Click Add dimension to select the dimension that define how many gauges are shown.
4. Click the Add measure button to select the value measure of the chart that defines the length of the bar.

   Once the measure is selected the bullet chart is displayed with default settings. Each gauge is displayed with an individual range. If you want to use a common range, you can set it with Appearance>Y-axis>Common range.
5. To add a target value, click Target under the measure. You can define a fixed value or use a measure with target values.
6. To add performance ranges, set Use segments under the measure to On.

   Click Add limit to set a range limit for the segments. You can adjust the color of each segment by clicking on it.

   You can define a fixed limit value or an expression.

The bullet chart is now displayed with the [dimension](#glossary-2 "Glossary term") and measure you selected.

When you have created the bullet chart, you might want to adjust its appearance and other settings in the properties panel. For information about styling, see [*Styling the bullet chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the bullet chart

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

     Click the checkbox for Auto contrast color to automatically override the selected color with the default color for the application's theme. This only applies to value labels inside the bars or inside white rectangles outside the bars.

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

## Setting a target value

In the [properties](#glossary-3 "Glossary term"), you can add a target value which is displayed as a marker line.
If the measure contains sales numbers, this could be budgeted sales for example.

You can define a fixed value or use a measure with target values.

## Setting performance ranges

In the properties panel, you can add performance ranges. Set Use segments under the measure to On.

You need to add the limits for the ranges you want to use for showing indicators with Add limit. You can set a limit value in three ways.

- Use the slider.
- Type a value in the text box.
- Set an expression that returns the limit value.

## Changing the color scheme

You can change color scheme of the value bar and the target by setting Appearance > Colors > Colors to Custom.
You can set single colors or use an expression.

Tip noteIt's a good idea to use a bar color that is visually dominant to the range colors.

When you have added the limits, you can select the color and the symbol of the indicator for each defined range.

## Adding a custom tooltip

You can add measures, charts, and images as tooltips.
To add custom tooltips, select Appearance>Tooltip>Custom.

- If you want to add a measure as a tooltip, you can add it from a field using From a field. You can also use an expression to add a measure. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor. The existing expression is displayed by default. You can add a title and description to the tooltip. You can change the label of the tooltip using Label as well as its formatting using Number formatting.
- If you want to add a chart as a tooltip, select a master visualization from the list of Master items.

  - Set the size of the tooltip container. Qlik Sense fits the chart into the container.
    - Small. Sets the width and height of the container to 140 pixels.
    - Medium. Sets the width and height of the container to 200 pixels.
    - Large. Sets the width and height of the container to 340 pixels.

    Tip noteAfter you add the chart, you can edit it by clicking Edit master item. See [*Editing a master visualization*](../../Assets/edit-master-visualization.htm).
- If you want to add an image as a tooltip, choose whether to add an image from your Media library or from a URL.

  - Set the size of the tooltip container. Qlik Sense fits the image into the container.
    - Small. Sets the width and height of the container to 50 pixels.
    - Medium. Sets the width and height of the container to 200 pixels.
    - Large. Sets the width and height of the container to 340 pixels.
    - Original. Qlik Sense fits the image into the container. If the image is larger than 340 pixels, it is scaled down.
  - Media library: Appears when you choose Media library for Type. Click to select an image from your media library.
  - URL: Appears when you choose URL for Type. Enter a URL. Your Qlik Sense administrator must allowlist external URLs in the Content Security Policy.

## Setting the scale of the axis

If you use a dimension to show several gauges, you can select how to show the scale of the axis with Appearance>Y-axis>Common range

- If you want each dimension gauge to use the same scale, enable Common range. If the range measure depends on the dimension value, the range bars will have different lengths.

  This is useful when you want to be able to compare the actual values.

  You can also set a common axis for all gauges with Appearance>Y-axis>Common range.
- If you want each range bar to be equally long, disable Common range.

  This is useful when you want to be able to compare the relative performance of each dimension value.

## Changing the orientation of the labels

To change the orientation of the chart's labels, the chart's presentation must be vertical. This can be set in the advanced edit mode properties panel with Appearance > Presentation > Vertical. Label orientation can then be selected with Appearance > X-axis > Label orientation. The following orientations are available:

- Auto: Automatically selects one of the other options depending on the space available on the chart.
- Horizontal: Labels are arranged in a single horizontal line.
- Tilted: Labels are stacked horizontally at an angle.
- Layered: Labels are staggered across two horizontal lines.

To view examples of label orientation, see [*X-axis and Y-axis*](../change-appearance-of-visualization.htm#X-axis).

## Learn more

- [*Bullet chart*](bullet-chart.htm)
