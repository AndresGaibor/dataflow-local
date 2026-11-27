---
title: "GET_RANGE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/get_range.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# GET\_RANGE

Returns range of numbers between start and end (inclusive).

## Syntax

```
GET_RANGE(maxLimit, first, last)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| maxLimit | int |  | 10000000 |
| first | numeric |  |  |
| last | numeric |  |  |

## Returns

Returns a `bigint` value.

---

## Examples

| maxLimit | first | last | Output |
| --- | --- | --- | --- |
| 10000000 | 0 | 0 | [0] |
| 10000000 | 0 | 2 | [0, 1, 2] |
| 10000000 | 5 | 2 | [5, 4, 3, 2] |
| 10000000 | 1.5 | 3.5 | [2, 3] |
| 10000000 | 5.2 | 3.5 | [5, 4] |
| 10000000 | array[0, 5] | array[2, 7] | [0, 1, 2, 5, 6, 7] |
