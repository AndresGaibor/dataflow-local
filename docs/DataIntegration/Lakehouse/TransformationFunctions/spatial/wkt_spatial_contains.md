---
title: "WKT_SPATIAL_CONTAINS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/spatial/wkt_spatial_contains.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Spatial"]
---

# WKT\_SPATIAL\_CONTAINS

Checks if the first WKT formatted spatial object contains the second.

## Syntax

```
WKT_SPATIAL_CONTAINS(first, second)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| first | string | The WKT formatted spatial object which should be contained by the second argument |  |
| second | string | The WKT formatted spatial object which should contain the first object |  |

## Examples

| first | second | Output |
| --- | --- | --- |
| "POLYGON((-10 30, -40 40, -10 -20, 40 20, 0 0, -10 30))" | "POINT(10 0)" | true |
| "POLYGON((-10 30, -40 40, -10 -20, 40 20, 0 0, -10 30))" | "POINT(15 0)" | false |
