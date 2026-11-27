---
title: "SQRT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/sqrt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# SQRT

Computes the square root of the given input.

## Syntax

```
SQRT(X)
```

## Arguments

#### `X`

Type: `numeric`

A numeric value.

## Returns

Type: `double`

The square root of `X` as a `double`.

Note that if $$x \leq 0$$, then the function returns a null value.

---

## Examples

| X | Output |
| --- | --- |
| 1 | 1.0 |
| -1 | `null` |
| 0 | 0.0 |
| 10.5 | 3.24037034920393 |
