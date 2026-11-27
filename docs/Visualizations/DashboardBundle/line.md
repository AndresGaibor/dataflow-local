---
title: "Line"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/line.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# Line

Add lines to your sheets with the Line control.

Information noteLine is included as a part of the Dashboard bundle. Dashboard bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

With Line controls, you can add vertical and horizontal lines to your sheets. They can be dotted or solid.

Line in a sheet dividing visualizations

![Line dividing a sheet horizontally, with three bar charts above the line and 2 map charts below the line.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineObject.png "Click to view full size")

## When to use the Line control

The Line control is useful for helping to group or divide sheet objects, as well as decorating sheets to help improve visual appeal.

## Creating lines

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag Line to the sheet.
3. Adjust the Line on the grid.
4. In the properties panel, in Presentation under Orientation, select Vertical or Horizontal.
5. Under Alignment, select:

   1. Leading: Line is placed to the left (vertical orientation) or top (horizontal orientation) of Line on the grid.
   2. Center: Line is placed in the center of Line on the grid.
   3. Trailing: Line is placed to the right or bottom of Line on the grid.
6. Under Stroke, set the following line styling options.
   - Color: Select the color of the line.
   - Width: Set the width of the line.
   - Dash: Set whether the line is solid or dashed. If the line is dashed, the following options are available:
     - Dash length: Set the length of dashes in the line.
     - Dash spacing: Set the gap between dashes in the line.
7. Optionally, to add a title, subtitle, or footnote, under General, select Show titles.

## Styling Line controls

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General tab. You can reset your styles by clicking ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section.

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

### Limitations

Line has the following limitations:

- You cannot connect the lines in separate Line controls together. If you want to have intersecting lines in your sheet, consider using a background image with the lines on the sheet instead.
