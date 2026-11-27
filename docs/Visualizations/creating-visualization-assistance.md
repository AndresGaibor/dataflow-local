---
title: "Creating visualizations using Insight Advisor chart suggestions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/creating-visualization-assistance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations"]
---

# Creating visualizations using Insight Advisor chart suggestions

Qlik Sense offers a wide range of [visualizations](#glossary-0 "Glossary term") to use with your data. Deciding on the correct [chart](#glossary-1 "Glossary term") type can be challenging when creating your first Qlik Sense application.

Insight Advisor chart suggestions enable you to select data [field](#glossary-3 "Glossary term")s and let Insight Advisor choose the [dimensions](#glossary-4 "Glossary term"), [measures](#glossary-5 "Glossary term"), and visualization types. As you add or remove fields, the suggested visualization adjusts itself based on your changes. You can customize a suggested visualization with a focused set of [properties](#glossary-6 "Glossary term").

If you started a visualization, enabling Chart suggestions will change your visualization to a suggested visualization.

Warning noteIf you enable Chart suggestions and then disable them, you will lose changes made to your visualization. You can restore your old visualization by undoing the changes. However, if you navigate away from Sheet view or make changes in the assets panel, you will not be able to undo and restore your visualization. For more information, see [*Undoing and redoing actions*](../UserInterface/undo-redo.htm).

## Creating a new visualization using chart suggestions

Do the following:

1. Click ![Edit object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. From ![Database](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_outline.svg) Fields, drag and drop a field into your sheet.

   Fields suggested as dimensions are added as tables or histograms. Fields suggested as measures are added as KPIs.

   To add fields as filter panes hold the shift key when you drag and drop the field.
3. Add additional fields by doing one of the following:

   - Drag and drop a field onto the visualization created from the first field, or on Suggest on the right-hand side.

     Qlik Sense determines if the field should be used as a dimension or as a measure, and which measure [aggregation](#glossary-7 "Glossary term") to use.
   - Click Add on the properties panel and select a field.
   - Drag and drop a field on Drop item here under Dimensions or Measures.

   The visualization will change as fields are added to it.
4. Optionally, remove unwanted fields.
5. Click ![Edit object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Done.

## Changing an existing visualization using chart suggestions

You change an existing visualization by adding fields or removing unwanted fields. Enabling Chart suggestions in the properties panel on the right-hand side changes the selected visualization to a chart suggestion based on the fields of the visualization. You can change the suggestions made by Qlik Sense. For example you can:

- Drag fields between Dimensions and Measures to change how a field is used. Moving a field to Dimensions removes its aggregation. Moving a field to Measures assigns it an aggregation.
- Choose a different aggregation for a field used as a measure. Your aggregation choice will be used whenever you use this field as a measure, while Chart suggestions is enabled.
- Use Change chart type to choose a different type of chart from the one suggested.

## Adjusting the settings when using chart suggestions

You can adjust the settings in the properties panel for Data and Appearance. The properties panel for visualizations created with chart suggestions contains a focused set of properties settings. Disabling Chart suggestions brings back access to all available properties.

## Limitations when using chart suggestions

- You cannot enable Chart suggestions for a master visualization.
- You cannot enable Chart suggestions for filter panes, histograms or maps.
- Charts with Chart suggestions enabled are not supported in Qlik NPrinting reports. To include charts created using chart suggestions in Qlik NPrinting reports, disable Chart suggestions.
- You can only change the aggregation of a measure when its label is the default label.
- You cannot drag a master dimension to Measures. You cannot drag a master measure to Dimensions.
- You can only drag a field from Measures to Dimensions if its expression is simple. For more information on how to use expressions in visualizations see [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm).

Related learning:

- [Using Insights to Create Visualizations](/lnk/Use-Insights-Create-Visualizations_QS)
- [How do I use the chart suggestions toggle?](/lnk/How_use_chart_suggestions)
