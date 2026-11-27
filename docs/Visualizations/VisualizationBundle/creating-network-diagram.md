---
title: "Creating network charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-network-diagram.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating network charts

The network chart (Network chart) lets you draw a network of connected nodes and edges from a data set to a [sheet](#glossary-0 "Glossary term"). A network chart shows how information flows, how components interact, and where components exist in the network. The network chart is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

This example of a network chart illustrates how different airports are connected worldwide based on base data set. It uses the example data set from [Formatting your data](#Formatti). Prepare by saving the example data set in a text file, creating a new application and loading the example data set.

Do the following:

1. In the assets panel, open Charts.
2. Under Legacy, drag a Network chart object to the sheet.
3. Click the top Add dimension button and select ID as the node identifier.
4. Click the second Add dimension button and select Name as the node label.
5. Click the third Add dimension button and select LinkTo as the parent node.
6. Click Data in the properties panel. Click the Add button under Node group and select Group as the group dimension.
7. Under Measure, click the Add button under Tooltip, and select Volume > Sum(NodeVolume).
8. Click the Add button under Node size, and select Volume > Sum(NodeVolume).
9. Click the Add button under Edge size, and select Volume > Sum(Volume).

   The chart displays:

   ![A chart with four dimensions and three measures in a dynamic edge type, with dot nodes, and visible curve values.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_networkchart.png)

## Changing the appearance of the chart

You can customize your chart with one or more features.

### Configuring edge type

You can configure the shape of the curve between chart nodes under Settings > Edge Type in the [properties](#glossary-1 "Glossary term") panel. Select the shape option of the chart curves from the menu.

Examples:

A chart with dynamic edge type (curves).

![A chart with dynamic edge type (curves). ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/b2_335x227.png "Click to view full size")

The same chart with curved CW edges.

![The same chart with curved CW edges.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/bild7_337x292.png "Click to view full size")

### Toggling edge value

The edge value represents value of the curves between chart nodes and their width. This option hides the numerical value of each curve. To hide the value move the slide button under Settings > Display edge value in the properties panel to the left to turn the option off.

### Configuring edge label

The edge label value is the numerical value of each chart curve. You can change the position of these or hide the labels.

- Hide edge label value: This option hides the edge label of the network chart. Toggle the slide button under Settings > Display edge value in the properties panel.

- Edge label position: This option decides where on each chart curve the edge value displays, for example: above or below. Select applicable option from the menu.

### Configuring node shape

You can customize the shape of the nodes, for example: dot, square, diamond, or triangle. Go to Settings > Node shape in the properties panel, and select the node shape from the menu.

### Toggling shadow option

This option lets you turn off the shadow effects behind chart curves and nodes (used to highlight background). Toggle the slide button under Settings > Display shadow in the properties panel.

### Sorting

Sorting is set to Auto with the system choosing the sorting order as the default (under Sorting > chosen dimension or measure in the properties panel) for all dimensions and measures. You can change them individually by expression.

Do the following:

1. Open the dimension or measure menu under Sorting in the properties panel.
2. Move Sorting slide button to the left to turn the option from Auto to Custom.
3. Click the Sort by expression check box.
4. Enter an order string under Expression and press Enter. You can also change the color using an expression in the Expression editor (![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg)).
5. Choose start order by selecting Ascending or Descending for the menu below.

### Number formatting

It is possible to format the measure value. Different formatting can be applied to the same value, for example: money, data,or duration. The chart updates to reflect the changed number type.

Do the following:

1. Click Data > Measures in the properties panel and click chosen measure.
2. Select applicable number formatting form the Number formatting menu.
3. Enter details in the panel fields. These display when choosing an option other than Auto when to configuring the chart.

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

- [How do I configure a Visualization Bundle Network chart?](/lnk/How_configure_Visualization_Bundle_Network_chart)
