---
title: "Creating waterfall charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WaterfallChart/create-waterfall-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating waterfall charts

The waterfall [chart](#glossary-0 "Glossary term") is suitable for illustrating how an initial value is affected by intermediate positive and negative values. The starting and the final values are represented by whole bars, and intermediate values by floating bars. You can also show subtotals in the chart.

You can create a waterfall chart on the [sheet](#glossary-1 "Glossary term") you are editing.

In a waterfall chart you need to use one [measure](#glossary-2 "Glossary term") for each bar in the chart. The order of the measures defines the order of the bars in the chart. For each measure, you need to define how it affects the previous value. You can add up to 15 measures in a waterfall chart.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty waterfall chart to the sheet.
3. Add the first measure.

   This is the first bar of the chart. By default, it will use the measure operation Add, and show a positive value.
4. Add a second measure.

   This is the second bar of the chart. If you want to show this measure as a negative contribution, change Measure operation to Subtract.
5. Continue to add measures, setting Measure operation to Add or Subtract in the properties panel depending on how you want them to contribute.
6. Add subtotals. There are two ways of adding subtotal bars to the chart:

   - If you have a data field containing subtotal data, add a measure with the subtotal data and select Subtotals as Measure operation.
   - If you don't have a data field containing subtotal data, you can add an automatically calculated subtotal by selecting the Subtotals check box of the measure before where you want the subtotal bar.

When you have created the waterfall chart, you may want to adjust its appearance and other settings in the properties panel. For information about styling, see [*Styling the waterfall chart*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Defining your measures

You can use the Measure operation option of each measure to set how it affects the previous value.

- Add

  The measure value adds to the previous bar. If this is the first measure, a whole bar is shown starting at 0.
- Subtract

  The measure value subtracts from the previous bar.

  Information noteIf the data already contains a negative sign, the result of subtraction will be a positive change.
- Subtotals

  The measure value is considered a subtotal.

  Tip noteIf you do not have sub-totals as a [field](#glossary-3 "Glossary term") you can add subtotals automatically by enabling Subtotals in the measure before you want the subtotal.

In the waterfall chart shown above, the first bar, Sales, is defined as Add. The second bar, Sales cost, is defined as Subtract, and the third bar, Sales margin, is defined as Subtotals.

## Styling the waterfall chart

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

   - Axis label: Style the labels on the axes.
   - Value label: Style the labels for the measure values.
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

- [*Waterfall chart*](waterfall-chart.htm)
- [*Visualizing positive and negative contributions to the result with a waterfall chart*](waterfall-example.htm)
- [Interpreting Waterfall Charts](/lnk/Interpreting_waterfall_charts)

Related learning:

- [Interpreting Waterfall Charts](/lnk/Interpreting_waterfall_charts)
