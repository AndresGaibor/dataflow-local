---
title: "ST_DISTANCE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/spatial/st_distance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Spatial"]
---

# ST\_DISTANCE

Calculates the two-dimensional cartesian minimum distance between two WKT formatted geometries in the units of the inputs.

## Syntax

```
ST_DISTANCE(first, second)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| first | string | A WKT formatted spatial object |  |
| second | string | A WKT formatted spatial object |  |

## Returns

Returns a `double` value.

---

## Examples

| first | second | Output |
| --- | --- | --- |
| "POINT (152.352298 -24.875975)" | "POINT (151.960336 -24.993289)" | 0.409141520796879 |
| "POLYGON((-10 30, -40 40, -10 -20, 40 20, 0 0, -10 30))" | "POINT(16 0)" | 0.6246950475544248 |
