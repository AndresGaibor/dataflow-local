---
title: "POWER"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/power.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# POWER

Raises the first input to the power of the second input.

## Syntax

```
POWER(X, P)
```

## Arguments

#### `X`

Type: `numeric`

A numeric value.

#### **`P`**

Type: `numeric`

A numeric value.

## Returns

Type: `double`

`X` raised to the power of `P`.

---

## Examples

| X | P | Output |
| --- | --- | --- |
| 1 | 1 | 1.0 |
| 2 | 2 | 4.0 |
| -1 | 2 | 1.0 |
| -2 | -2 | 0.25 |
| 0.5 | 0.5 | 0.7071067811865476 |
| 0.5 | 0 | 1.0 |
| 0 | 0 | 1.0 |
