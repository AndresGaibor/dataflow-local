---
title: "TO_BIGINT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/type-conversion/to_bigint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Type Conversion"]
---

# TO\_BIGINT

Convert any numeric value to a 64-bit signed integer. This truncates any existing fractional part.

## Syntax

```
TO_BIGINT(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | numeric | The numeric value to convert |  |

## Returns

Returns a `bigint` value.

---

## Examples

| value | Output |
| --- | --- |
| 3 | 3 |
| 3.5 | 3 |
| -3.5 | -3 |
| 3 | 3 |
