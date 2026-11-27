---
title: "TRUNCATE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/truncate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# TRUNCATE

Truncates the given input to a given number of decimal places.

## Syntax

```
TRUNCATE(X [, N])
```

## Arguments

#### `X`

Type: `numeric`

A numeric value.

#### `N`

Type: `integer`

Default: `0`

The number of decimal places to keep. This can be negative to truncate `N` digits left of the decimal point.

If omitted, the precision defaults to 0 and `X` is rounded to the nearest integer.

## Returns

Type: `double`

`X` truncated to `PRECISION` decimal places.

---

## Examples

| X | Precision | Output |
| --- | --- | --- |
| 2.365 |  | 2.0 |
| 1.456249 | 3 | 1.456 |
| 42.01934 | 2 | 42.01 |
| 1.1 |  | 1.0 |
| -1.1 |  | -1.0 |
| -1.9 |  | -1.0 |
| 0 |  | 0.0 |
| 0.5 |  | 0.0 |
| 12.333 | -1 | 10.0 |
| 12.333 | 0 | 12.0 |
| 12.333 | 1 | 12.3 |
