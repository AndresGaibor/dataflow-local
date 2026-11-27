---
title: "Creating navigation menus"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Navigation-menu/create-navigation-menu.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating navigation menus

The navigation menu offers an alternative method of navigating between sheets and sheet groups in an application.

You can format and color the text in the menu. The background image has sizing and positioning options.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a navigation menu on to the sheet.

## Styling the navigation menu

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
4. On the Menu tab, set the font, font size, and color for the following text elements:

   - Labels: Style the labels of the individual items (and their icons, if used).

### Customizing the background

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-0 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.
4. On the Menu tab of the styling panel, select a default color for the menu items, a highlight color, and a hover color.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Tip noteIf the Separate items setting is turned on, the border and shadow are applied to each menu item rather than the entire chart. For information about Separate items, see [*Separating items in navigation menus*](#SeparateItems).

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.
7. On the Menu tab, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
8. Select a color for the border.
9. Adjust the Corner radius to control the roundness of the border.
10. Under Shadow in the Menu tab, select a shadow size and color. Select None to remove the shadow.

## Setting navigation menus as drawer menus

You can make your navigation menu a drawer menu. When set as a drawer menu, the navigation menu acts as a button that opens a menu over the whole application listing sheets. You can optionally add a menu icon (![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg)) to the navigation menu.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, turn on Drawer menu.
3. Optionally select Show drawer icon.
4. Adjust Drawer panel position to configure whether the panel opens on the left or right side of the page.

### Styling drawer menus

You can style your drawer button and panel.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. Click Menu.
4. Under Drawer button, optionally customize the colors and add a background image.
5. Under Drawer panel, optionally customer the color and background image used by the panel.

## Setting orientation and layout

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, under Orientation, select Vertical or Horizontal.
3. Under Layout, select Fill or Minimal.
4. Under Position, select the position of the menu items in the navigation menu.
5. If you selected Horizontal or Minimal, optionally select Same item width to make all tabs have the same size.

## Separating items in navigation menus

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, turn on Separate items.

With the Separate items setting turned off, choose whether to show a divider between items with Use divider. When using a divider, you can set its color.

## Showing large items

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, select Show large items.

## Showing item icons

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, select Show item icons.

## Turning on the hover menu

The hover menu is turned off by default in navigation menus. You can turn it on in the properties panel.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > General, select Show hover menu.

## Working with sheet title expressions

The navigation menu can display sheet names entered using a sheet title expression. The order of priority is as follows:

- If a Title expression is applied to the sheet, the navigation menu displays the output of this expression.
- If there is no Title expression applied to the sheet, the navigation menu displays the Title of the sheet.

For more information about sheet titles and title expressions, see [*Changing the title and description of a sheet*](../../Sheets/styling-sheets.htm#TitleDesc).
