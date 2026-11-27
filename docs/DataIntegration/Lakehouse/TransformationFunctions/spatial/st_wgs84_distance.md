---
title: "ST_WGS84_DISTANCE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/spatial/st_wgs84_distance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Spatial"]
---

# ST\_WGS84\_DISTANCE

Calculates the distance between two WKT formatted points in meters in the WGS84 projection.

## Syntax

```
ST_WGS84_DISTANCE(first, second)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| first | string | A WKT formatted Longitude Latitude point |  |
| second | string | A WKT formatted Longitude Latitude point |  |

## Returns

Returns a `double` value.

---

## Examples

| first | second | Output |
| --- | --- | --- |
| "POINT (152.352298 -24.875975)" | "POINT (151.960336 -24.993289)" | 41667.7298657432 |
