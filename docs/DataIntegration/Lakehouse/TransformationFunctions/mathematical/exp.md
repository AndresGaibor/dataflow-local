---
title: "EXP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/exp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# EXP

Computes $$e^x$$ where $$e$$​ is Euler's number and $$x$$​ is the given input.

## Syntax

```
EXP(X)
```

## Arguments

#### **`X`**

Type: `numeric`

A numeric value.

## Returns

Type: `double`

Euler’s number raised to the power of `X`.

---

## Example

| X | Output |
| --- | --- |
| 1 | 2.7182818284590455 |
| 2 | 7.38905609893065 |
| 1 + 1 | 7.38905609893065 |
| 1.5 | 4.4816890703380645 |
| -1 | 0.36787944117144233 |
| -1.5 | 0.22313016014842982 |
