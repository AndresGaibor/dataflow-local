---
title: "Converting a visualization to another kind of visualization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/convert-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Converting a visualization to another kind of visualization

You can convert from one [visualization](#glossary-0 "Glossary term") type to another by dragging a [chart](#glossary-1 "Glossary term") from the assets panel on the left-hand side onto the visualization that you want to convert.

All properties that the original visualization has are transferred to the new type. The new visualization uses the dimensions, measures, and settings that are applicable to that visualization type. If a visualization requires an additional primary dimension or measure, the first listed alternative dimension or measure is used by default. If no alternative dimensions or measures exist and one is required the new visualization, you will be prompted to add one.

All [properties](#glossary-2 "Glossary term") from the original visualization are saved, even if they are not available or visible in the new visualization. This means that properties can become available again if you decide to convert to yet another visualization type where those properties are used.

Do the following:

1. While editing a sheet, drag a new chart from the assets panel onto the visualization that you want to convert.

   The shortcut menu opens.
2. Select the conversion option.

The new visualization is displayed, using the data from the original visualization.

Information noteWhen you convert to a new visualization type, some of the settings from the original visualization may not be optimal for the new visualization, for example, the sorting order. Therefore, you may need to make some changes in the properties panel, so that the new visualization is displayed as you want.

Information note

It is not recommended to convert an existing ShowHide Container or Tabbed container into a Tab container.
Containers created by converting these objects cannot be monitored in activity centers or downloaded as an image or PDF.

It is recommended to create a new container. For more information, see [*Converting a visualization to another kind of visualization*](#Creating).
