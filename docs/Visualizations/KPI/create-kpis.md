---
title: "Creating KPIs"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/KPI/create-kpis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating KPIs

The KPI [visualization](#glossary-0 "Glossary term") can show one or two [measure](#glossary-1 "Glossary term") values, and is used to track performance.

You can create a KPI visualization on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty KPI chart to the sheet.
3. Click Add measure and select a measure or create a measure from a field.

In a KPI visualization, you can have one or two measures and no [dimensions](#glossary-3 "Glossary term"). With two measures, the second value automatically becomes a complementary value and is shown with a smaller font size. You can easily switch their order by dragging the measures in the [properties](#glossary-4 "Glossary term") panel under Measures.

When you have created the KPI visualization, you might want to adjust its appearance and other settings in the properties panel.
 For information about styling, see [*Styling the KPI*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

The following settings are used by default in a KPI visualization:

- Centered alignment.
- Black text color.
- No background color.
- Fluid layout behavior.
- Medium font size.
- No titles.
- Measure label displayed.
- Conditional colors and symbols are turned off.
- No link to sheet.

Tip noteIf you double-click or drag a measure from the assets panel, a KPI visualization is added on the sheet using the measure.

## Styling the KPI

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

In a KPI, you can style the text in the following components of the chart:

- Title area: Includes the chart title, subtitle, and footnote.
- Chart area: Includes measure titles and measure values.

#### Styling the title, subtitle, and footnote

You can customize the text displayed in the title area of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote

#### Styling the chart text

The data displayed in a KPI chart consists of text. The appearance of this text can be customized separately from the title area.

You can set the text alignment for the chart. Choose between left-aligned, centered, or right-aligned text.

You can also select between several layout behavior options. The layout behavior defines how the size of the text adapts given the configured font size, chart size, and text length. The following options are available:

- Responsive: You can adjust the font size, with additional text size adjustments applied based on chart size and text length. Adjustments are made to fit all text content into the KPI.
- Fluid (default): You can adjust the font size, with additional text size adjustments applied based on chart size only. This re-scaling of the text is independent of text length. If the text is too long, an ellipsis is inserted at the end.
- Fixed: You can adjust the font size, but it does not automatically adapt to chart size or text length. It remains at the same size regardless of changes to these components.

Additionally, you can show or hide each of the measure titles in the KPI, and set the font size for the chart text.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. Navigate to the Chart tab.
4. Under Alignment, set the text alignment. Choose between left, centered, or right alignment.
5. Under Layout behavior, adjust how text size adapts to chart size and text length. The appearance of each setting depends on the Font size you set for the chart.
6. Under Show, select whether to show or hide each KPI title in the chart.
7. Under Font size, adjust the size of the text that displays the measure titles and values.

For further customization settings, you can set the Styling mode to Advanced options to style each measure title and measure value individually.

Do the following:

1. In the Chart tab of the styling panel, under Styling mode, turn on Advanced options.
2. Under First measure title, configure the following settings:

   - Set Show title on or off to display or hide the measure title.
   - Style the text. Choose the font, emphasis style, font size, and color.
3. Under First measure value, set the font, emphasis style, and font size.
4. Repeat the steps above to customize the Second measure title and Second measure value.

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

## Using conditional colors and symbols

You can set your KPI visualization to display in different colors, and with different symbols, depending on the value of the selected measure. Conditional colors and symbols can be configured in the properties panel.

You can do this by adding multiple range limits to the KPI, creating subsections that indicate performance. For example, you can set your KPI so that it displays in:

- Green with a check mark symbol when performance is strong.
- Yellow with a caution symbol when performance falls below expectations.
- Red with an X symbol when performance is low.

You can also set range limits with expressions, rather than defining a single value.

For more information, see [Using conditional colors in KPIs](https://share.vidyard.com/watch/ZCtp8zxuuHtRU8sYCSh5Mr).

Do the following:

1. Select a KPI visualization and open the properties panel.
2. Select Appearance and expand Color.
3. If necessary, turn off Library colors and turn on Conditional colors.
4. Click Add limit to create a new limit. Multiple limits can be added to a single KPI chart.
5. Specify a value for the limit, or enter an expression using the expression editor.
6. On the Value color bar, click the range area of the KPI you would like to modify.
7. Under Colors, select a preset color or use a custom color. Toggle, if needed, to Symbols to choose the symbol displayed when your KPI falls within the specified limit.

## Linking to another sheet

You can link from the KPI visualization to a sheet in the application. When making data analysis and clicking the visualization, you can click a second time to go to a predefined sheet. The sheet is opened in a new tab. When hovering over ![Info](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info.svg), the name of the sheet is displayed. The icon is only displayed when Show title is selected, under Presentation.

## Showing the hover menu

By default, the hover menu is not displayed on KPI visualizations. You can enable the hover menu if needed.

Do the following:

1. In edit mode, select the KPI visualization.
2. In the properties panel, go to Appearance > General.
3. Turn on Show hover menu.

## Learn more

- [*KPI*](KPI.htm)
- [Interpreting KPIs](/lnk/Interpreting_KPIs)

Related learning:

- [Interpreting KPIs](/lnk/Interpreting_KPIs)
