---
title: "WKT_SPATIAL_INTERSECT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/spatial/wkt_spatial_intersect.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Spatial"]
---

# WKT\_SPATIAL\_INTERSECT

Checks if the WKT formatted spatial objects intersect.

## Syntax

```
WKT_SPATIAL_INTERSECT(first, second)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| first | string | A WKT formatted spatial object |  |
| second | string | A WKT formatted spatial object |  |

## Examples

| first | second | Output |
| --- | --- | --- |
| "POLYGON((-10 30, -40 40, -10 -20, 40 20, 0 0, -10 30))" | "POINT(10 0)" | true |
| "POLYGON((-10 30, -40 40, -10 -20, 40 20, 0 0, -10 30))" | "POINT(16 0)" | false |
