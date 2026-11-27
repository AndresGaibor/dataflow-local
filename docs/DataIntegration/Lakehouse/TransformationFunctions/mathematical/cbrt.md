---
title: "CBRT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/cbrt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# CBRT

Computes the cube root of the given input.

## Syntax

```
CBRT(X)
```

## Arguments

#### **`X`**

Type: `numeric`

A numeric value.

## Returns

Type: `double`

The cube root of `X`.

---

## Examples

| X | Output |
| --- | --- |
| 1 | 1 |
| 1 + 1 | 1.2599210498948732 |
| 0 | 0 |
| 1.1 | 1.0322801154563672 |
| -1 | -1 |
| -1.1 | -1.0322801154563672 |
| -1 - 5 | -1.8171205928321397 |
| 0.1 | 0.4641588833612779 |
| -0.1 | -0.4641588833612779 |
