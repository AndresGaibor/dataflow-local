---
title: "Creating funnel charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-funnel-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating funnel charts

The Funnel chart (Funnel chart) lets you add a sequential chart showing the connected stages of a process. Each stage will decrease and should contain a subset of the previous stage. The decrease is gradual, giving the chart an ever narrower funnel.  The Funnel chart is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a funnel chart on the [sheet](#glossary-0 "Glossary term") you are editing.

- The dimension decides how it should be grouped in segments. By default, dimension values are displayed in descending order by measure value.
- The measure is the value that decides the size of each segment.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a Funnel chart object to the sheet.
3. Click the top Add dimension button and select the target dimension (usually target market) of the chart.
4. Click the Add measure button to select the measure (what is to be measured) of the chart. Once dimensions (dimension label) and measure (value label) have been selected the funnel chart displays automatically (in color) in the chart field.
5. Click Done to revert to the main display field.
6. Click applicable region under Region. The chart field will update displaying chosen parameters and details.

Dimension, [measure](#glossary-1 "Glossary term") and region details will continue to display in the chart [field](#glossary-2 "Glossary term") even when reverting to Edit mode.

## Changing the appearance of the chart

You can customize your chart with one or more features.

### Funnel mode

You can set the shape of the funnel with Appearance > Presentation > Funnel Mode.

#### Area

The area of each item is proportionate to the measure. Only the height of the individual segment is affected - not the overall chart or contents.

![Funnel chart shaped in default funnel mode.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/areany50_307x301.png "Click to view full size")

#### Height

The height of each item is proportionate to the measure. Only the height of the individual segment is affected - not the overall chart or contents.

![Funnel chart shaped by measure height.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/heightny50_309x321.png "Click to view full size")

#### Width

The width of the upper edge is proportionate to the maximum value of the measure. The top segment is always 100% and the following segments are relative in size to the first. The lowest segment is rectangular. This affects the shape of the funnel and each segment has its individual slope.

![Funnel chart shaped by measure width.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/funnelny51_298x302.png "Click to view full size")

#### Ordering

The measure only orders the segments with largest value at the top. The ordering is fixed so the shape of the funnel is not affected.

![Funnel chart shaped with largest value on top.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/orderingny50_303x306.png "Click to view full size")

### Colors

You can choose how to color the funnel chart by changing the Appearance > Colors setting from Auto to Custom.

#### Single color

You can use a single color for the entire funnel chart by selecting Single color in Colors.

![Funnel chart with a single color.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/singleny50_297x304.png "Click to view full size")

#### Color by dimension

You can also color your entire funnel chart by [dimension](#glossary-3 "Glossary term") by selecting By dimension in Colors. There are two gradient color schemes available:

- 12 colors
- 100 colors

You can also select to keep persistent colors with Persistent colors.

#### Color by measure

You can color your funnel chart by measure by selecting By measure in Colors. The measure of the chart is selected as default, but you can change it under Select measure. This measure must be unlinked before a new can be selected. You can also change the measure using an expression in the Expression editor (![Expression](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg)).

You can choose between four color schemes. It is also possible to reverse the colors.

- Sequential gradient
- Sequential classes
- Diverging gradient
- Diverging classes

You can also set a color range for your chart based on your measure by setting Range to Custom. Set the range in Range > Min and Range > Max. You can use a number or an expression that evaluates as a number.

#### Color by expression

You can color your funnel chart by measure by selecting By expression in Colors. You can color it in two ways.

- The expression evaluates as a valid CSS color to color the chart. The expression is a color code should be checked.
- The chart is colored by the expression value according to a color scheme. The expression is a color code should be unchecked.

  You can also set the range of the colors.

### Sorting

Funnel chart elements are automatically sorted from largest to smallest. You can change the sort order in the [properties](#glossary-4 "Glossary term") panel. Go to Sorting, and drag your dimensions and measurements into the desired order.

### Styling and formatting

The position and order of labels for dimension and measure values can be displayed in different ways. You can for example hide the dimension value or display [measures](#glossary-5 "Glossary term") as values or as a percentage.

Additionally, you configure the title label to display for the dimension under Data in the properties panel. Change the styling of these text elements in the styling panel. See [*Using the styling panel to further customize the appearance*](#Using).

#### Dimension label

You can choose if you want to show the dimension title label or not with Appearance > Presentation > Dimension title

#### Value labels

You can choose how to show value labels for each segment by setting Appearance > Presentation > Value labels to Custom.

- None hides the value labels.
- Share displays the values as percentage.
- Values displays the actual measure values.

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

   - Dimension title: Style the text of the dimension title that is displayed above the visualization.
   - Dimension value label: Style the text of the labels displaying the individual dimension values.
   - Value Label: Style the text of the measure value labels.

     Use the Auto contrast color setting to automatically override the selected value label color with a color that better contrasts the funnel colors.

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

- [How do I configure a Visualization Bundle Funnel chart?](/lnk/How_configure_Visualization_Bundle_Funnel_chart)
