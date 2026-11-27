---
title: "MakeGeoPoint Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/MakeGeoPoint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Geospatial functions"]
---

# MakeGeoPoint Script and chart function

MakeGeoPoint() is used to validate geographic data in JSON and set the appropriate tags on the field. MakeGeoPoint() confirms the data is an array with two numbers.

Syntax:

MakeGeoPoint(geo\_data)

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| geo\_data | The source of geographic data. This can be constructed with other geospatial functions, string literals, JSON functions, KML data, or other sources.  geo\_data is validated and only returns valid data of that type. Any invalid data returns a NULL value instead. |

Tip noteDo not use the Group by clause in the data load editor with this and other non-aggregating geospatial functions, because this will cause an error on load.

[*Loading your own map data*](../../Visualizations/Map/load-map-data.htm)
