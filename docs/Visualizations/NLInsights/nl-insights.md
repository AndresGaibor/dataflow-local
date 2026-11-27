---
title: "NL insights"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/NLInsights/nl-insights.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# NL insights

The NL insights visualization displays natural language insights and information about selected [dimensions](#glossary-0 "Glossary term") and [measures](#glossary-1 "Glossary term").

NL insights uses Insight Advisor to generate natural language information about the dimensions and measure added to the chart. The chart updates the insights as [selections](#glossary-2 "Glossary term") are made in the application.

Native NL insights object displaying natural language insights with full verbosity

![Native NL insights object, with custom styling applied](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_nl-insights.png "Click to view full size")

NL insights is a native chart type replacing the deprecated NL Insights control from the Dashboard bundle.

By default, NL insights generates insights for all analysis types supported for the selected fields. The classification of fields in your application logical model determines which fields are available as dimensions or measures. For more information on defining fields, see [*Defining fields and groups in Insight Advisor*](../../BusinessLogic/business-logic-fields-groups.htm).

## When to use NL insights

Use NL insights when you want to include a narrative or analytical summary of your data. For example, on a [sheet](#glossary-3 "Glossary term") focused on sales, you might want narratives summarizing key ranking, correlation, and comparison analyses for sales to complement your other [visualizations](#glossary-4 "Glossary term").

It is also helpful to pair NL insights with another [chart](#glossary-5 "Glossary term") containing the same dimensions and measures. This provides additional context and information for the chart. To do this, configure the NL insights object to use an input chart that has already been created on the current sheet. The dimensions and measures from that input chart are used to generate the natural language insights, and the NL insights will update based on changes you make in the input chart.

NL insights with natural language insights generated directly from input bar chart

![Native NL insights object, shown alongside bar chart. The NL insights chart is linked to the bar chart and uses the same dimensions and measures to generate the narrative insights](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_nl-insights_using_existing_chart.png "Click to view full size")

## Migrating from the Dashboard bundle to native object

NL Insights extension objects from the Dashboard bundle must be migrated to native charts if they appear on a public (base) sheet or published (community) sheet. To do this, follow the applicable steps to make the sheet private, then publish and/or make it public again.

### Personal and shared spaces

Do the following:

1. Open the application overview, or open ![Sheets](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sheet2.svg) Sheets from sheet view.
2. Right-click the public sheet and select Make private.
3. Open the private sheet and ensure the chart has been migrated.
4. Under your private sheets, right-click the sheet and select Make public.

### Managed spaces

#### Public sheets

Do the following:

1. Open the application overview, or open ![Sheets](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sheet2.svg) Sheets from sheet view.
2. Right-click the public sheet and select Duplicate.
3. Open the duplicated private sheet and ensure the chart has been migrated.
4. Right-click the sheet and select Publish.

   This publishes the sheet to the Community, under My sheets.

If you instead need the sheet to be re-added as a public sheet, you will need to open the source application in the personal or shared space, then make the sheet private and then public again. Finally, re-publish the application to the managed space.

#### Published sheets

Do the following:

1. Open the application overview, or open ![Sheets](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sheet2.svg) Sheets from sheet view.
2. Right-click the published sheet and select Unpublish.
3. Open the private sheet and ensure the chart has been migrated.
4. Right-click the sheet and select Publish.

## Creating NL insights

You need at least one dimension or one measure to create the chart. Combine dimensions and measures as needed. If you use an existing chart to generate the content of your NL insights, the dimensions and measures from that input chart are used and will be dynamically updated if you change the input chart.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag an empty NL insights chart to the sheet.
3. Click Add chart to use natural language insights from an existing chart in the NL insights visualization. Choose from any of the supported charts in the current sheet.

   Alternatively, click Add dimension or Add measure to add natural language insights from a dimension or measure into the chart.
4. In the properties panel, add or remove dimensions and measures from the chart.

   Information noteYou cannot add or remove dimensions and measures if you have chosen to use insights from an existing chart.

When you have created the NL insights visualization, you might want to adjust its appearance and other settings in the [properties](#glossary-6 "Glossary term") panel.  For information about how to style the visualization, see [*Styling NL insights*](#Styling).

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

## Considerations

The analysis types and number of narrative insights generated in the NL insights chart depend on the volume and variety of data that belongs to the fields selected. A limited number of analysis types and insights might be displayed in the following scenarios:

- The selected items use the same underlying field with aggregations or selections.
- The selected items include only measures and no dimensions.
- The selected items are mostly unrelated.

## Limitations

The NL insights object has the following the limitations:

- You cannot use the following chart types for direct input into the NL insights chart:

  - Animator
  - Button
  - Container
  - Date picker
  - Filter pane
  - Text & image
  - Video player
- The NL insights chart does not provide natural language insights for the following analysis types (even if it uses an input chart generated from these analysis types):

  - Anomaly (spike)
  - Anomaly (trend)
  - Clustering (k-means)
  - Overview
  - Period changes
  - Process control (rolling mean)
  - Year to date
- Expressions with modifiers, either applied directly to the chart or via an input chart, might not provide correct values in natural language insights.
- The number format accompanying an expression is only applied to narrative statements generated using that expression. Additional narratives that are generated might not adhere to the expression's number format.
- When using an existing chart as the input for an NL insights object, certain actions taken on the input chart will not result in the natural language insights being updated automatically. Specifically, switching to alternative measures or dimensions, or customizations made through chart exploration in analysis mode, do not update natural language insights unless those changes are applied and made available for all users.
- Changing the number format of a measure might not always result in this formatting being changed in all available insights.
- The NL insights chart is not available for consumption by anonymous (non-authenticated) users through the sharing of an application with a Qlik Anonymous Access subscription. This means that the chart cannot be embedded into external content for anonymous consumption. In applications that are shared anonymously via a public link, the chart does not appear.

## Learn more

- [*Creating NL insights*](create-nl-insights.htm)
