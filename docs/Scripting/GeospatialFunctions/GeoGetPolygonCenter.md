---
title: "GeoGetPolygonCenter Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoGetPolygonCenter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---
# GeoGetPolygonCenter Script and chart function

GeoGetPolygonCenter() is used in scripts and chart expressions to calculate and return the center point of a geometry.

In some cases, the requirement is to plot a dot instead of color fill on a map. If the existing geospatial data is only available in the form of area geometry (for example, a boundary), use GeoGetPolygonCenter() to retrieve a pair of longitude and latitude for the center of area.

Syntax:

GeoGetPolygonCenter(field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

> **Tip:** Do not use the Group by clause in the data load editor with this and other non-aggregating geospatial functions, because this will cause an error on load.

[*Loading your own map data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/load-map-data.htm)
