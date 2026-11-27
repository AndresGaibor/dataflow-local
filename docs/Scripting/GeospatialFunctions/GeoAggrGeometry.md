---
title: "GeoAggrGeometry Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoAggrGeometry.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---

# GeoAggrGeometry Script and chart function

GeoAggrGeometry() is used to aggregate a number of areas into a larger area, for example aggregating a number of sub-regions to a region.

Syntax:

GeoAggrGeometry(field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

Typically, GeoAggrGeometry() can be used to combine geospatial boundary data. For example, you might have postcode areas for suburbs in a city and sales revenues for each area.
If a sales person’s territory covers several postcode areas, it might be useful to present total sales by sales territory, rather than individual areas, and show the results on a color-filled map.

GeoAggrGeometry() can calculate the aggregation of the individual suburb geometries and generate the merged territory geometry in the data model.
If then, the sales territory boundaries are adjusted, when the data is reloaded the new merged boundaries and revenues are reflected in the map.

As GeoAggrGeometry() is an aggregating function, if you use it in the script a LOAD statement with a Group by clause is required.

Tip noteThe boundary lines of maps created using GeoAggrGeometry() are those of the merged areas. If you want to display the individual boundary lines of the pre-aggregated areas, use GeoReduceGeometry().

Examples:

This example loads a KML file with area data, and then loads a table with the aggregated area data.

[MapSource]:
LOAD [world.Name],
[world.Point],
[world.Area]
FROM [lib://Downloads/world.kml]
(kml, Table is [World.shp/Features]);
Map:
LOAD world.Name,
GeoAggrGeometry(world.Area) as [AggrArea]
resident MapSource Group By world.Name;

Drop Table MapSource;

## Learn more

- [*GeoReduceGeometry Script and chart function*](GeoReduceGeometry.htm)
- [*Loading your own map data*](../../Visualizations/Map/load-map-data.htm)
