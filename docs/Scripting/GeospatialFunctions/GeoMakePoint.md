---
title: "GeoMakePoint Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoMakePoint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---
# GeoMakePoint Script and chart function

GeoMakePoint() is used in scripts and chart expressions to create and tag a point with latitude and longitude. GeoMakePoint returns points in the order of longitude and latitude.

Syntax:

GeoMakePoint(lat\_field\_name, lon\_field\_name)

Return data type:  string, formatted [longitude, latitude]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| lat\_field\_name | A [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/GeoMakePoint.htm#glossary-0 "Glossary term") or expression referring to a field representing the latitude of the point. |
| lon\_field\_name | A field or expression referring to a field representing the longitude of the point. |

> **Tip:** Do not use the Group by clause in the data load editor with this and other non-aggregating geospatial functions, because this will cause an error on load.

[*Loading your own map data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/load-map-data.htm)
