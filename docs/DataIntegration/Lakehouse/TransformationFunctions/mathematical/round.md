---
title: "ROUND"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/round.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# ROUND

Rounds the given input to a given number of decimal places.

## Syntax

```
ROUND(X [, D])
```

## Arguments

#### `X`

Type: `numeric`

A numeric value.

#### `D`

Type: `bigint`

Default: `0`

(Optional) The number of decimal places to keep.

If omitted, the precision defaults to 0 and `X` is rounded to the nearest integer.

## Returns

Type: same as input `X`

`X` rounded to `D` decimal places.

---

## Examples

| X | D | Output |
| --- | --- | --- |
| 1.1 |  | 1.0 |
| -1.1 |  | -1.0 |
| 1.9 |  | 2.0 |
| -1.9 |  | -2.0 |
| 1 |  | 1 |
| 1 | 5 | 1 |
| 1.23 | 1 | 1.2 |
| 1 + 1 |  | 2 |
| 0 |  | 0 |
| -1 |  | -1 |
