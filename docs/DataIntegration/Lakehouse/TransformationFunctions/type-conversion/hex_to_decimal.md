---
title: "HEX_TO_DECIMAL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/type-conversion/hex_to_decimal.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Type Conversion"]
---

# HEX\_TO\_DECIMAL

Converts a hexadecimal string value to the corresponding signed 64-bit integer.

## Syntax

```
HEX_TO_DECIMAL(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string | The hexadecimal string value to convert |  |

## Returns

Returns a `bigint` value.

---

## Examples

| value | Output |
| --- | --- |
| "###" | null |
| "ff" | 255 |
| "0xff" | 255 |
