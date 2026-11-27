---
title: "Geospatial functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/geospatial-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Geospatial functions

Expand/Collapse all

# Geospatial functions

These functions are used to handle geospatial data in map [visualizations](#glossary-0 "Glossary term"). Qlik Sense follows GeoJSON specifications for geospatial data and supports the following:

- Point
- Linestring
- Polygon
- Multipolygon

For more information on GeoJSON specifications, see:

[GeoJSON.org](http://geojson.org/)

[*Map chart*](../../Visualizations/Map/Map.htm)

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

There are two categories of geospatial functions: aggregation and non-aggregation.

Aggregation functions take a geometry set (points or areas) as input, and return a single geometry. For example, multiple areas can be merged together, and a single boundary for the aggregation can be drawn on the map.

Non-aggregation function take a sinlge geometry and return one geometry. For example, for the function GeoGetPolygonCenter(), if the boundary geometry of one area is set as input, the point geometry (longitude and latitude) for the center of that area is returned.

The following are aggregation functions:

GeoAggrGeometry

GeoAggrGeometry() is used to aggregate a number of areas into a larger area, for example aggregating a number of sub-regions to a region.

[**GeoAggrGeometry**](GeoAggrGeometry.htm)(field\_name)

GeoBoundingBox

GeoBoundingBox() is used to aggregate a geometry into an area and calculate the smallest bounding box that contains all coordinates.

[**GeoBoundingBox**](GeoBoundingBox.htm)(field\_name)

GeoCountVertex

GeoCountVertex() is used to find the number of vertices a polygon geometry contains.

[**GeoCountVertex**](GeoCountVertex.htm)(field\_name)

GeoInvProjectGeometry

GeoInvProjectGeometry() is used to aggregate a geometry into an area and apply the inverse of a projection.

[**GeoInvProjectGeometry**](GeoInvProjectGeometry.htm)(type, field\_name)

GeoProjectGeometry

GeoProjectGeometry() is used to aggregate a geometry into an area and apply a projection.

[**GeoProjectGeometry**](GeoProjectGeometry.htm)(type, field\_name)

GeoReduceGeometry

GeoReduceGeometry() is used to reduce the number of vertices of a geometry, and to aggregate a number of areas into one area, but still displaying the boundary lines from the individual areas.

[**GeoReduceGeometry**](GeoReduceGeometry.htm)(geometry)

The following are non-aggregation functions:

GeoGetBoundingBox

GeoGetBoundingBox() is used in scripts and chart expressions to calculate the smallest geospatial bounding box that contains all coordinates of a geometry.

[**GeoGetBoundingBox**](GeoGetBoundingBox.htm)(geometry)

GeoGetPolygonCenter

GeoGetPolygonCenter() is used in scripts and chart expressions to calculate and return the center point of a geometry.

[**GeoGetPolygonCenter**](GeoGetPolygonCenter.htm)(geometry)

GeoMakePoint

GeoMakePoint() is used in scripts and chart expressions to create and tag a point with latitude and longitude.

[**GeoMakePoint**](GeoMakePoint.htm)(lat\_field\_name, lon\_field\_name)

GeoProject

GeoProject() is used in scripts and chart expressions to apply a projection to a geometry.

[**GeoProject**](GeoProject.htm)(geo\_data)

MakeGeoLine

MakeGeoLine() is used to validate geographic data in JSON and set the appropriate tags on the field. MakeGeoLine() confirms the data is an array with points.

[**MakeGeoLine**](MakeGeoLine.htm)(geo\_data)

MakeGeoPolygon

MakeGeoPolygon() is used to validate geographic data in JSON and set the appropriate tags on the field. MakeGeoPolygon() confirms the data is an array with lines.

[**MakeGeoPolygon**](MakeGeoPolygon.htm)(geo\_data)

MakeGeoPoint

MakeGeoPoint() is used to validate geographic data in JSON and set the appropriate tags on the field. MakeGeoPoint() confirms the data is an array with two numbers.

[**MakeGeoPoint**](MakeGeoPoint.htm)(geo\_data)

MakeGeoRegion

MakeGeoRegion() is used to validate geographic data in JSON and set the appropriate tags on the field. MakeGeoRegion() confirms the data is an array with polygons.

[**MakeGeoRegion**](MakeGeoRegion.htm)(geo\_data)
