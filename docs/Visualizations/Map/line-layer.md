---
title: "Line layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/line-layer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Line layers

A line layer enables you to display lines between points on your map.

For example, you can use a line layer to show aircraft flights between cities. With a line layer, you can use two fields containing point data to define the start points and end points for lines in the layer. Alternatively, you can use a [field](#glossary-0 "Glossary term") containing line geometry in either GeoJSON LineString or MultiLineString format. You can customize the width and curvature of lines in the line layer and add directional arrows to your lines.

Map with line layer displaying departing flights between airports in Europe.

![Map with line layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineLayer.png "Click to view full size")

## Adding a line layer

Line layers display lines using either start and end points, where two fields are used to determine where lines start and end, or using line geometries in GeoJSONLineString or MultiLineString format.

If you are using a start and end point line layer, the [dimension](#glossary-1 "Glossary term") you select for your line layer should represent the fields selected as the start and end points in your Location settings. For example, if you wanted to visualize where your shipments are being sent, you could set Shipments as the dimension and then use Distribution Center Location and Shipping Destination as the start point and end point in Location.

Alternatively, you can add two dimensions to the line layer and use these as the start and end points. This is useful if you want to display lines between all locations in the first dimensions to all locations in the second dimension, which has an association to the first dimension.

### Adding a line layer with start and end points

Do the following:

1. From Layers in the [properties](#glossary-2 "Glossary term") panel, click Add layer and select Line layer.
2. In Dimensions, click Add and select a field to use as the dimension.
3. If your dimension contains start point data, add a field containing end point data. Do one of the following:

   - Drag and drop a field containing end point data onto the map, select Use in <layer name>, and select Add <field name> as a second dimension.
   - In Data, click Add and select a field containing end point data.
4. If your dimension does not contain start or end point data, in Location, add the fields containing the start point data and end point data as location fields.
5. If there are issues with the start and end point locations, adjust the location settings in Location in the properties panel.

   Line layers using start point field and end point fields each have separate location settings in Location.

   For more information, see [*Map chart*](Map.htm#Setting).
6. Optionally, in Options > General, after Max visible objects, set the maximum locations to display in the layer.

   The maximum number of values in a map layer is 50,000. By default, layers display a maximum of 4,000 values for point layers and 1,000 for other layers.

Once the layer is added, you can adjust settings for the layer in the properties panel.

### Adding a line layer with line geometries

Do the following:

1. From Layers in the advanced properties, click Add layer and select Line layer. In Dimensions, click Add and select a field to use as the dimension.
2. In Location, select Line geometry and then select a field in Line geometry field.

   By default, your dimension is selected as the Line geometry field.

Once the layer is added, you can adjust settings for the layer in the properties panel.
