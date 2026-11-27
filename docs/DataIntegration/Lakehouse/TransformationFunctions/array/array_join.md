---
title: "ARRAY_JOIN"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_join.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_JOIN

Concatenates the elements of the given array using the specified delimiter.

## Syntax

```
ARRAY_JOIN(X, DELIMITER)
```

## Arguments

#### **`X`**

Type: `array`

An array of any value type.

#### **`DELIMITER`**

Type: `string`

The delimiter used to join the values within the array.

## Returns

Type: `string`

The values of the array `X` joined with `DELIMITER`.

---

## Examples

| X | DELIMITER | Output |
| --- | --- | --- |
| `[a, b, c]` | , | a,b,c |
| `[5.5]` | , | 5.5 |
| `[hello, NULL, world]` |  | hello world |
| `[brave, NULL, world]` | new | brave new world |
| `[3,6,1,2]` | , | 3,6,1,2 |
| `[5.5]` | `NULL` | `NULL` |
