---
title: "MOD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/mod.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# MOD

Computes the modulus (remainder) of the first input divided by the second input.

## Syntax

```
MOD(N, M)
```

## Arguments

#### `N`

Type: `numeric`

A numeric value representing the dividend.

#### **`M`**

Type: `numeric`

A numeric value representing the divisor.

## Returns

Type: same as input

The remainder of `N` divided by `M`.

---

## Examples

| N | M | Output |
| --- | --- | --- |
| 1 | 1 | 0 |
| 1 | 0 | null |
| -1 | 1 | 0 |
| 0 | 0 | null |
| 3.3 | 1.1 | 1.0999999999999996 |
| 2.5 | 2.5 | 0.0 |
| 3.03 | 1.01 | 1.0099999999999998 |
| 0 | 2 | 0 |
| 9 | 2 | 1 |
