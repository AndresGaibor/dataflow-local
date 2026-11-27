---
title: "Creating variance waterfall charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-variance-waterfall.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating variance waterfall charts

You can use the variance waterfall chart (Variance waterfall) to show the variance between two [measures](#glossary-0 "Glossary term") over the different values of a [dimension](#glossary-1 "Glossary term"). The variance waterfall chart is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a variance waterfall chart on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Legacy, drag a Variance waterfall object to the sheet.
3. Click the Add dimension button to select the bridge dimension.
4. Click the first Add measure button to select the measure to use as start value.
5. Click the second Add measure button to select the measure to use as end value.

The variance waterfall chart is now displayed with one bar for the start value measure and one bar for the end value measure. Between the measure bars you will see the variance for each value of the bridge dimension.

## Changing the appearance of the chart

You can customize the appearance of your chart.

### Labels

You can turn off value labels by setting Appearance > Presentation > Value labels to Off.

### Legend

You can customize the legend labels by setting Appearance > Presentation > Labels to Custom. You can set a custom text for the following legend labels:

- Start value (Start value)
- End value (End value)
- Positive variance (Positive label)
- Negative variance (Negative label)

You can also hide the legend by setting Appearance > Colors and legend > Show legend to Off or change the position of the legend with Appearance > Colors and legend > Legend position.

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

## Example of a variance waterfall chart

In this simple example we will show how quarterly sales numbers contribute to sales compared to budget.

### Dataset

The [dataset](#glossary-3 "Glossary term") we use contains sales numbers and budgeted sales for each quarter. You can paste it into a text file and load it in Qlik Sense.

```
Quarter,Sales,Budget
Q1,9,10
Q2,14,12
Q3,12,12
Q4,18,14
```

### Visualization

You can now create a variance waterfall chart.

- Add Quarter as dimension.
- Add Sum(Budget) as the first measure.
- Add Sum(Sales) as the second measure.

The variance waterfall chart is created. We have adjusted the labels and colors in the example.
You can clearly see that Q1 had sales below budget, but the year ended with sales over budget, and that Q4 was the largest contribution.

Variance waterfall chart showing spending over fiscal quarters

![A variance water showing spending over several fiscal quarters.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_variance_waterfall.png "Click to view full size")

Related learning:

- [How do I configure a Visualization Bundle Variance Waterfall chart?](/lnk/How_configure_Visualization_Bundle_Variance_Waterfall_chart)
