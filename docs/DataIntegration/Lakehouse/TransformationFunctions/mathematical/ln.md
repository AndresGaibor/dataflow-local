---
title: "LN"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/ln.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# LN

Computes the natural logarithm $$ln(x)$$ where $$x$$ is the given input.

## Syntax

```
LN(X)
```

## Arguments

#### **`X`**

Type: `numeric`

A numeric value.

## Returns

Type: `double`

The natural logarithm of `X`.

Note that if $$x \leq 0$$, then the function returns a null value.

---

## Examples

| X | Output |
| --- | --- |
| 1 | 0.0 |
| 0 | `null` |
| 2 | 0.6931471805599453 |
| 0.5 | -0.6931471805599453 |
| 4 \* 5 | 2.995732273553991 |
