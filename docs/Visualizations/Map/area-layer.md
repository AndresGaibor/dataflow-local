---
title: "Area layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/area-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Area layers

An area layer presents areas on your map, such as countries or states. With polygon geometry loaded into a [field](#glossary-0 "Glossary term"), it can present any custom area.

With an area layer, each [dimension](#glossary-1 "Glossary term") value corresponds to a presented area. By using colors with your area layer, you can present different [measure](#glossary-2 "Glossary term") values for the areas. In the [properties](#glossary-3 "Glossary term") panel, under Appearance > Colors and legend, switch Colors to Custom where the options By measure and By expression are available.

Map with area layer displaying Australian states and territories colored by population.

![Map with area layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AreaLayerMap.png "Click to view full size")

## Adding an area layer

Do the following:

1. From Layers in the properties panel, click Add layer and select Area layer.
2. In Dimensions, click Add and select a field containing area data to use as the dimension.
3. If there are issues with the point locations, adjust the location settings in Locations in the properties panel.

   [*Map chart*](Map.htm#Setting)
4. Optionally, in Options > General, after Max visible objects, set the maximum locations to display in the layer.

   The maximum number of values in a map layer is 50,000. By default, layers display a maximum of 4,000 values for point layers and 1,000 for other layers.

Once the layer is added, you can adjust settings for the layer in the properties panel.
