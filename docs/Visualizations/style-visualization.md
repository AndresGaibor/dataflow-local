---
title: "Applying custom styling to a visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/style-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Changing the appearance of a visualization"]
---

# Applying custom styling to a visualization

By default, the styling properties of a visualization are determined by the application theme. You can override the application theme for individual visualizations by using the styling panel. In the styling panel, you can also style individual charts with properties that are not available in the application theme.

The styling panel is available in the properties panel.
Under Appearance > Presentation, click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling. The properties available to customize depend on the chart type.

Examples of styling properties you can customize include, but are not limited to:

- Chart title, subtitle, and footnote
- Background color and image
- Measure, dimension, and axis labels

For a list of customizable properties available for each chart type, see the corresponding chart-specific help topic.

## Copying and pasting visualization styling

If you have applied custom styling to a visualization, you can copy its styling properties and paste them onto another visualization. With this option, you can quickly align the styling of your visualizations without editing them in the properties panel or adding a custom theme.

You can copy and paste styles between different chart types. The entire style definition is applied to the chart. Therefore, if a chart contains properties that do not apply to the chart receiving the styling, these properties are still transferred to the receiving chart.

Do the following:

1. In sheet edit mode, right-click a chart or open the options menu by selecting the ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button next to it.
2. Click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy style.
3. Right-click the chart onto which you want to paste the styling, or open its options menu.
4. Click ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) Paste style.

### Limitations

- You cannot copy and paste the styling of a master visualization.
- You cannot copy and paste the styling of a map.
- You cannot copy and paste the styling of a button.

## Application themes

If you are looking to change the styling for all visualizations in the application, it might be easier to change the application theme. For increased control over specific styling aspects of all application visualizations, consider developing a custom theme and applying it to the application.

For more information about styling an application, see [*Styling an application*](../Apps/style-app.htm).

## Learn more

- [*Changing the appearance of a visualization*](change-appearance-of-visualization.htm)
