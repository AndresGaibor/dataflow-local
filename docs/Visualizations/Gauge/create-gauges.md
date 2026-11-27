---
title: "Creating gauges"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Gauge/create-gauges.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating gauges

The gauge shows a single [measure](#glossary-0 "Glossary term") value and visualizes how to interpret that value.

You can create a gauge on the [sheet](#glossary-1 "Glossary term") you are editing. In a gauge you can only have one measure and no [dimensions](#glossary-2 "Glossary term").

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty gauge to the sheet.
3. Click Add measure and select a measure or create a measure from a field.

When you have created the gauge, you may want to adjust its appearance and other settings in the [properties](#glossary-3 "Glossary term") panel.

The following settings are used by default in a gauge:

- A radial gauge.
- A single (blue) color.
- Range limits: min (0), max (100).
- No segments.
- Label and title are displayed in medium scale.

For example, you can change the radial gauge to a bar, and use a color gradient.

![Bar gauge with a color gradient.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Gauge2.png)

## Styling the gauge

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the labels and other titles on the chart depends on how it has been configured outside of the styling panel. For a gauge, these display options can be configured in other areas the Appearance section.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font and font color for the following text elements:

   - Axis title: Style the title for measure displayed in the gauge.
   - Axis label: Style the labels for gauge's range limits.
   - Value label: Style the label displaying the measure value.

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

## Showing the hover menu

By default, the hover menu is not displayed on gauge visualizations. You can enable the hover menu if needed.

Do the following:

1. In edit mode, select the gauge.
2. In the properties panel, go to Appearance > General.
3. Turn on Show hover menu.

## Learn more

- [*Gauge*](gauge.htm)
- [Interpreting Gauges](/lnk/Interpreting_gauges)

Related learning:

- [Interpreting Gauges](/lnk/Interpreting_gauges)
