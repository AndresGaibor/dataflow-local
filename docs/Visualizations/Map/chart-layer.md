---
title: "Chart layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/chart-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Chart layers

A chart layer enables you to display small pie charts or bar charts over locations in your map. It uses one [dimension](#glossary-0 "Glossary term") to identify the locations and a second dimension to create the pie or bar charts.

You can label the charts and use an expression to control their size. The info bubble displays useful information about the contents of the selected chart.

Map with chart layer displaying source of funds in European Union countries as pie charts. The size of each pie chart shows average absorption rate of funds.

![Map with density layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ChartLayer.png "Click to view full size")

## Adding a chart layer

Do the following:

1. From Layers in the properties panel, click Add layer and select Chart layer.
2. In Dimensions, under Location, click Add and select a field containing point data to use as the locations on your map. Click Add and select a field containing data to use as the dimension on your charts.
3. In Measures, click Add and select a field containing data to use as the measure on your charts.
4. If there are issues with the point locations, adjust the location settings in Location in the [properties](#glossary-1 "Glossary term") panel.

   [*Map chart*](Map.htm#Setting)[*Map chart*](Map.htm#Setting)
5. Optionally, in Options > General, after Max visible objects, set the maximum locations to display in the layer.

   The maximum number of values in a map layer is 50,000. By default, layers display a maximum of 4,000 values for point layers and 1,000 for other layers.

Once the layer is added, you can adjust settings for the layer in the properties panel.
