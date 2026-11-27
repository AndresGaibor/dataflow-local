---
title: "Tab container"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Container/container-object.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# Tab container

The tab container is an object that lets you add [visualizations](#glossary-0 "Glossary term") in a limited space. You can also show or hide the visualizations inside the tab container based on conditions.

![A tab container.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Container-rev.png)

## When to use the tab container

The tab container is useful when you want to quickly switch between different visualizations on a dashboard with limited space. You can also use a tab container to show different visualizations based on:

- Which user is accessing the chart.
- The value of a variable.

## Creating a tab container

You can create a tab container on the [sheet](#glossary-1 "Glossary term") you are editing.

Do the following:

1. From the assets panel, open Charts and under Dashboard objects, drag a tab container to the sheet.
2. Click Add under Content in the properties panel.
3. Select a master visualization in Master items, or create a new visualization in Charts.

   Alternatively: you can add content to your tab container by dragging available visualizations from your sheet, or from your Master items, directly on the tab container.
4. Drag the charts in the property panel to set the tab order.

You now have a container with a tab for each visualization you added. You can switch between tabs to show different visualizations.

Information note

It is not recommended to convert an existing ShowHide Container or Tabbed container into a Tab container.
Containers created by converting these objects cannot be monitored in activity centers or downloaded as an image or PDF. Instead, it is recommended to create a new container.

## Adding show conditions

You can add show conditions on the tabs you have created.

Do the following:

1. Click on the chart you want to add a show condition to, under Content in the property panel.
2. Add a show condition for the [chart](#glossary-2 "Glossary term") in Show condition. Typically you would use an If() function.

   See [*if Script and chart function*](../../Scripting/ConditionalFunctions/if.htm).
3. Add another show condition to a different chart.

   The charts will now be shown or hidden depending on the result of the conditions you added. If the condition of a chart results in True, it is shown, and if it is False, it is hidden.

## Changing the tab orientation

Tabs can be orientated vertically or horizontally.

Do the following:

1. Go to Appearance > Presentation in the property panel.
2. Under Orientation, select the position of tabs in the tab container.

## Changing the default active tab

By default, the first tab is displayed when you view a tab container.
You can change this in the property panel.

Do the following:

1. Go to Appearance > Presentation in the property panel.
2. Use the Default tab dropdown to select which chart displays when users view a sheet. The dropdown lists the available charts in the same order they are arranged in the container.
3. If you want to see the new default tab setting take effect, close and re-open your browser.

## Styling the tab container

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

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
4. On the Tab tab, set the font, font size, and color for the following text elements:

   - Label: Style the labels on the axes.

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

### Customizing the border

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Under Border, set the border outline and corner radius.

### Adding a shadow

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Under Shadow, set the shadow size and color.

### Setting tab width

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Click Tabs.
4. Under Width, set the width to be in percentage or pixels.
5. Under Min/Max, set the maximum and minimum sizes of the tabs.

### Setting the selected tab indicator color

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Click Tabs.
4. Under Indicator, select to use a single color or color by expression.
5. If using a single color, select a color.
6. If using an expression, enter an expression.

### Styling icons

If you turn on Show icons, you can style the icons.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Click Tabs.
4. Under Icon, set the size, color, and position of chart icons.

### Customizing tab background colors

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. Click Tabs.
4. Under Background color, select the colors for tabs, selected tabs, and when tabs are being hovered over. You can color by a single selected color or by expression.

## Creating a bookmark with a tab container

By default, if you create a [bookmark](#glossary-3 "Glossary term") that contains a tab container with [selections](#glossary-4 "Glossary term"), the first tab will be active when the bookmark is selected. To save a different default active tab for the tab container, you can toggle on Save layout when creating the bookmark with that tab open.
If you set that bookmark as the default bookmark by right-clicking and selecting Set as default bookmark in the bookmark list, the sheet will open to the selections and tab that were active when the bookmark was created.

Do the following:

1. Click ![Bookmark](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) in the toolbar.
2. Click Create new bookmark.

   Change the name and description, if desired.
3. If you want a tab other than the default tab to be the active tab, toggle on Save layout with that tab open. This will override the Default tab setting in the property panel.
4. Click Save.

## Display limitations

- You cannot use a master visualization that has a tab container inside another container.
- You cannot add the same master visualization twice in a tab container.
- You cannot create a chart inside a tab container by dropping measures or dimensions on the container.
- You cannot add a tab container, trellis container, or layout container inside a tab container.
- The visualization exploration menu is not available for charts that are located inside a tab container, layout container, or legacy container object.
- With the Show hover menu setting turned on and the hover menu visible, you may not be able to see arrows for switching between tabs.

## Learn more

- [*Creating tab containers*](create-containers.htm)
