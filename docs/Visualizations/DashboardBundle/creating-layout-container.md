---
title: "Creating layout containers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/creating-layout-container.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating layout containers

Layout containers allow you to add [visualizations](#glossary-0 "Glossary term") in a limited space. You can also show or hide the visualizations inside the layout container based on conditions. Layout container is included as a part of the Dashboard bundle. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

You can create a container on the [sheet](#glossary-1 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag Layout container to the sheet.

You now have a layout container. You can start adding and configuring charts to your layout container.

## Adding charts to a layout container

Tip note

You can copy and paste charts in and out of the layout container, but you must use the right-click context menu.

Do the following:

1. Select a layout container.
2. Click Add under Content in the properties panel.

   Alternatively, click Add content in the layout container.
3. Select a visualization in Charts.
4. Click Add dimension and Add measure to add data to the chart.
5. To resize the chart, do one of the following:
   - Click and drag the corners or edge of the chart.
   - In properties, enter the width and height of the chart in percent.
6. To reposition the chart, do one of the following:

   - Click and drag the chart into position.
   - In properties, enter the x-axis and y-axis positions of the chart, in percent.

   To show grid lines for layout, in properties, under Presentation > Styling, turn on Show grid lines. You can also set the number of rows and columns in the grid, and snap visualizations to the grid lines.

   To keep charts within the borders of the layout container, under Presentation > Styling, turn on Keep charts within bounds.
7. To reorder the layers of visualizations in the layout container, right-click on the visualization in the layout container, select Reorder chat layers, and choose to bring the visualization forward or back. Alternatively, click and drag the visualizations in the properties panel.
8. To configure the chart with all properties available for that chart type, click Edit properties.
9. Repeat for any additional charts you want to add to the layout container.

### Adding show conditions

You can add show conditions on the tabs you have created.

Do the following:

1. Click on the chart you want to add a show condition to, under Content in the property panel.
2. Add a show condition for the [chart](#glossary-2 "Glossary term") in Show condition. Typically you would use an If() function.

   See [*if Script and chart function*](../../Scripting/ConditionalFunctions/if.htm).
3. Add another show condition to a different chart.

   The charts will now be shown or hidden depending on the result of the conditions you added. If the condition of a chart results in True, it is shown, and if it is False, it is hidden.

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
