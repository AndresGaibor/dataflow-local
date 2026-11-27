---
title: "GeoBoundingBox Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoBoundingBox.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---

# GeoBoundingBox Script and chart function

GeoBoundingBox() is used to aggregate a geometry into an area and calculate the smallest bounding box that contains all coordinates.

A GeoBoundingBox is represented as a list of four values: left, right, top, bottom.

Syntax:

GeoBoundingBox(field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

GeoBoundingBox() aggregates a set of geometries and returns four coordinates for the smallest rectangle that contains all the coordinates of that aggregated geometry.

To visualize the result on a map, transfer the resulting string of four coordinates into a polygon format, tag the transferred [field](#glossary-0 "Glossary term") with a geopolygon format, and drag and drop that field into the map object. The rectangular boxes .will then be displayed in the map [visualization](#glossary-1 "Glossary term").

[*Loading your own map data*](../../Visualizations/Map/load-map-data.htm)
