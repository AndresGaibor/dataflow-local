---
title: "GeoReduceGeometry Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoReduceGeometry.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---
# GeoReduceGeometry Script and chart function

GeoReduceGeometry() is used to reduce the number of vertices of a geometry, and to aggregate a number of areas into one area, but still displaying the boundary lines from the individual areas.

Syntax:

GeoReduceGeometry(field\_name[, value])

Return data type:  JSON

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |
| value | The amount of reduction to apply to the geometry. The range is from 0 to 1, with 0 representing no reduction and 1 representing maximal reduction of vertices.  **Note:** Using a value of 0.9 or higher with a complex data set can reduce the number of vertices to a level where the visual representation is inaccurate. |

GeoReduceGeometry() also performs a similar function to, GeoAggrGeometry() in that it aggregates a number of areas into one area. The difference being that individual boundary lines from the pre-aggregation data are displayed on the map if you use GeoReduceGeometry().

As GeoReduceGeometry() is an aggregating function, if you use it in the script a LOAD statement with a Group by clause is required.

Examples:

This example loads a KML file with area data, and then loads a table with the reduced and aggregated area data.

[MapSource]:
LOAD [world.Name],
[world.Point],
[world.Area]
FROM [lib://Downloads/world.kml]
(kml, Table is [World.shp/Features]);
Map:
LOAD world.Name,
GeoReduceGeometry(world.Area,0.5) as [ReducedArea]
resident MapSource Group By world.Name;

Drop Table MapSource;

## Learn more

- [*GeoAggrGeometry Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoAggrGeometry.htm)
- [*Loading your own map data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/load-map-data.htm)
