---
title: "Density layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/density-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Density layers

A density layer enables you to visualize the density of points in an area using a color ramp.

Each point influences a circular area, with the highest influence at the center and declining towards its outer perimeter. You can specify the influence radius of the points, change its color and scale it to suit your [visualization](#glossary-0 "Glossary term"). Density layers can be used to show hotspots of activity, population densities and more.

Map with density layer displaying number of global volcanic eruptions.

![Map with density layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DensityLayer.png "Click to view full size")

## Adding a density layer

Do the following:

1. From Layers in the [properties](#glossary-1 "Glossary term") panel, click Add layer and select Density layer.
2. In Dimensions, click Add and select a [field](#glossary-2 "Glossary term") containing point data to use as the [dimension](#glossary-3 "Glossary term").
3. If there are issues with the point locations, adjust the location settings in Locations in the properties panel.

   For more information, see [*Map chart*](Map.htm#Setting).
4. Optionally, in Options > General, after Max visible objects, set the maximum locations to display in the layer.

   The maximum number of values in a map layer is 50,000. By default, layers display a maximum of 4,000 values for point layers and 1,000 for other layers.

Once the layer is added, you can adjust settings for the layer in the properties panel. .
