---
title: "Creating NL insights"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/NLInsights/create-nl-insights.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating NL insights

Add NL insights to your sheet to enhance and add depth to the data analytics content in your application. Insight Advisor provides natural language insights using a variety of available analysis types.

You need at least one dimension or one measure to create the chart. Combine dimensions and measures as needed. If you use an existing chart to generate the content of your NL insights, the dimensions and measures from that input chart are used and will be dynamically updated if you change the input chart.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag an empty NL insights chart to the sheet.
3. Click Add chart to use natural language insights from an existing chart in the NL insights visualization. Choose from any of the supported charts in the current sheet.

   Alternatively, click Add dimension or Add measure to add natural language insights from a dimension or measure into the chart.
4. In the properties panel, add or remove dimensions and measures from the chart.

   Information noteYou cannot add or remove dimensions and measures if you have chosen to use insights from an existing chart.

When you have created the NL insights visualization, you might want to adjust its appearance and other settings in the [properties](#glossary-0 "Glossary term") panel.  For information about how to style the visualization, see [*Styling NL insights*](#Styling).

## Styling NL insights

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
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, style the following text elements:

   - Analysis type: Set the font, font size, and color of the headers displaying the analysis types of the insights.
   - Style: Set the font, font size, and color of the narrative insights.
   - Structure: Set how the narrative insights in the chart should be presented. Choose bullet points or sentences.

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

## Adjusting the verbosity

You can control the verbosity of the generated insights. Verbosity can be full or brief. Full verbosity groups natural language insights by analysis type. Brief verbosity displays all natural language insights as a list.

Verbosity can be configured under Appearance > Presentation in the properties panel.

## Removing analysis types

You can remove unwanted analysis types from NL Insights under Appearance > Presentation in the properties panel.

## Changing the language of the natural language insights

You can change the language of the generated natural language insights under Appearance > Presentation in the properties panel in advanced edit mode.

Information noteNL insights has the same language supports as natural language insights. For information, see [*Supported languages*](../../Insights/insight-advisor-create-visualizations.htm#Supporte).

## Learn more

- [*NL insights*](nl-insights.htm)
