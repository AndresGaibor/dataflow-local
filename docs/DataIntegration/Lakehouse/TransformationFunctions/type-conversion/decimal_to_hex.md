---
title: "DECIMAL_TO_HEX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/type-conversion/decimal_to_hex.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Type Conversion"]
---

# DECIMAL\_TO\_HEX

Converts a signed 64-bit integer to its hexadecimal string representation

## Syntax

```
DECIMAL_TO_HEX(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | numeric | The number to convert |  |

## Returns

Returns a `string` value.

---

## Examples

| value | Output |
| --- | --- |
| 255 | `ff` |
| 2147483647 | `7fffffff` |
| 9223372036854775807 | `7fffffffffffffff` |
| -1 | `ffffffffffffffff` |
