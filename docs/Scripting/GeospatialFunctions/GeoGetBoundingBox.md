---
title: "GeoGetBoundingBox Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoGetBoundingBox.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---
# GeoGetBoundingBox Script and chart function

GeoGetBoundingBox() is used in scripts and chart expressions to calculate the smallest geospatial bounding box that contains all coordinates of a geometry.

A geospatial bounding box, created by the function GeoBoundingBox() is represented as a list of four values: left, right, top, bottom.

Syntax:

GeoGetBoundingBox(field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

> **Tip:** Do not use the Group by clause in the data load editor with this and other non-aggregating geospatial functions, because this will cause an error on load.

## Learn more

- [*GeoBoundingBox Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoBoundingBox.htm)
- [*Loading your own map data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/load-map-data.htm)
