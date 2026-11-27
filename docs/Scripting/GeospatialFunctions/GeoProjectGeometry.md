---
title: "GeoProjectGeometry Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoProjectGeometry.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---

# GeoProjectGeometry Script and chart function

GeoProjectGeometry() is used to aggregate a geometry into an area and apply a projection.

Syntax:

GeoProjectGeometry(type, field\_name)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| type | Projection type used in transforming the geometry of the map. This can take one of two values: 'unit', (default), which results in a 1:1 projection, or 'mercator', which uses the web Mercator projection. |
| field\_name | A field or expression referring to a field containing the geometry to be represented. This could be either a point (or set of points) giving longitude and latitude, or an area. |

Example:

| Example | Result |
| --- | --- |
| In a Load statement: GeoProjectGeometry('mercator',AreaPolygon) as ProjectGeometry | The geometry loaded as AreaPolygon is transformed using the Mercator projection and stored as ProjectGeometry for use in [visualizations](#glossary-0 "Glossary term"). |

## Learn more

- [*Loading your own map data*](../../Visualizations/Map/load-map-data.htm)
