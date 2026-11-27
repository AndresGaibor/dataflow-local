---
title: "Drill-down layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/drill-down-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Drill-down layers

When creating a map that has multiple points of data located in a wide geographical area, you can use drill-down [dimensions](#glossary-0 "Glossary term") to display your layers in a selection hierarchy.

This enables you to use different layers at different levels within your map, ensuring only the most relevant information is being displayed.

As you make [selections](#glossary-1 "Glossary term") in a drill-down layer, the dimension used for locations changes to the next dimension in the drill-down dimension. The drill-down happens across layers that use the same drill-down dimension. If you have an area and point layer that use the same drill-down dimension, you can set which layer displays with which dimension from the drill-down dimension.

Information noteIf selections cause the current drill-down dimension field to have only one possible value, the next field in the list is used instead.

Drill-down dimensions used for drill-down layers should have the fields in order of highest geographical area to smallest geographical area.

For information on creating drill-down dimensions, see [*Creating a drill-down dimension*](../../Dimensions/create-drill-down-dimension.htm).

Do the following:

1. From Layers in the properties panel, click Add layer.
2. Select Point layer, Area layer, Line layer, Density layer, or Chart layer.
3. Click Dimensions, click Add and select your drill-down dimension.
4. In your layer, click Options.
5. Click Layer display.
6. After Visible drill-down levels, select which dimensions to display in the layer.
