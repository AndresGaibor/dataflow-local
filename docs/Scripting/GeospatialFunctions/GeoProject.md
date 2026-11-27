---
title: "GeoProject Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoProject.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---

# GeoProject Script and chart function

GeoProject() is used in scripts and chart expressions to apply a projection to a geometry.

Syntax:

GeoProject(type, field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| type | Projection type used in transforming the geometry of the map. This can take one of two values: 'unit', (default), which results in a 1:1 projection, or 'mercator', which uses the web Mercator projection. |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

Tip noteDo not use the Group by clause in the data load editor with this and other non-aggregating geospatial functions, because this will cause an error on load.

Example:

Script examples

| Example | Result |
| --- | --- |
| In a Load statement: GeoProject('mercator',Area) as GetProject | The Mercator projection is applied to the geometry loaded as Area, and the result is stored as GetProject. |

[*Loading your own map data*](../../Visualizations/Map/load-map-data.htm)
