---
title: "Creating sankey charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-sankey-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating sankey charts

The Sankey chart (Sankey chart) lets you add a specific type of flow chart to the [sheet](#glossary-0 "Glossary term") you are editing. The chart visually emphasizes major transfers or flows within defined system boundaries. The width of the chart arrows is shown proportionally to the flow quantity. The Sankey chart is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a sankey chart on the sheet you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a Sankey chart object to the sheet.
3. Click the top Add dimension button and select the source dimension for the flow of the chart (appears to the left).
4. Click the second Add dimension button to select the target dimension for the flow of the chart (appears to the right).
5. Click the Add measure button to select the measure of the chart.

Once dimensions and [measure](#glossary-1 "Glossary term") have been selected the sankey chart diagram displays automatically (in color) in the chart field.

## Adding additional dimensions

You can add up to five dimensions to your chart in property panel under Data > Dimensions. The chart updates to reflect the added dimensions. The dimensions are displayed from left to right, with the first entered dimension always being the source dimension. The target dimension is always displayed to the to the right. When you add more dimensions, they are added to the right in the order they are entered.

A chart with three dimensions: the source dimension (Origin), the target dimension (Decision) and one additional (Destination).

![Sankey chart with three dimensions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/2018-11-20 11_33_01-Microsoft Edge_691x383.png "Click to view full size")

## Sorting

Sankey chart elements are automatically sorted from largest to smallest flow. You can change the sort order in the property pane.

Do the following:

1. Click Sorting under Appearance in the property panel.
2. Toggle Sorting from Auto to Custom.
3. You can toggle Sort numerically:
   - Toggle on: Sort numerically by Ascending or Descending.
   - Toggle off: Drag your dimensions and measurements into the desired order.

## Changing the styling and appearance

You can customize your chart with one or more features. Your chart automatically updates.

### Link colors

The colors of chart links are based on either the source or target anchors. To apply the source or target anchor color to chart links either use the string ='SOURCE' or ='TARGET'. You can also select a separate color by entering a color code string. The color should be a valid CSS color.

Do the following:

1. Click Presentation under Appearance in the property panel.
2. Enter the applicable string under Link color.
3. Press Enter and the chart updates.

You can also change the link colors using an expression in the Expression editor (![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg)). It is also possible to color a link that has its intensity based on the Margin % of the dimension values it represents.

Example:

Enter the string =rgb(round(Avg ([Margin %])\*255), 100, 100) where Margin % is a value between 0-1 and the link will display as red in the chart.

### Link opacity

You can adjust link opacity by moving the slide button of the link opacity slider under Appearance > Link opacity in the property panel. Also, setting opacity to 1 (furthest right) allows the setting to drop a shadow, giving links a more individually distinct appearance.

### Node colors

You can change the node colors of each dimension value. The color should be a valid CSScolor.

Do the following:

1. Select applicable dimension under Data > Dimensions in the property panel.
2. Enter the color code string under Node color and press Enter. The chart will update.

   For example: To use the color Aqua (#00ffff) set the color code string to ='#00ffff'. You can also set the node colors using an expression in the Expression editor (![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg)).

   ![Region dimension values colored by an expression.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/2018-11-20 11_39_03-Microsoft Edge_651x328.png)

### Node padding and width

You can set both the vertical distance between nodes ("node padding") and the horizontal width of chart nodes ("node width").

Do the following:

1. Click Presentation under Appearance in the property panel.
2. Move applicable slide button of the Node padding and/or Node width sliders to adjust node settings.

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

   - Node title: Style the text of the header for each node in the chart.
   - Node label: Style the text of the labels displaying the individual values of the nodes.

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
