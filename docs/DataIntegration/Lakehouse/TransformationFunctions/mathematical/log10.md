---
title: "LOG10"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/log10.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# LOG10

Returns the base 10 logarithm of x.

## Syntax

```
LOG10(input)
```

## Arguments

| Name | Type | Mandatory |
| --- | --- | --- |
| input | numeric | true |

## Returns

Returns a `double` value.

---

## Examples

| input | output |
| --- | --- |
| 100 | 2.0 |
| 0.5 | -0.30102999566398114 |
| 1 | 0.0 |
| 0 | "-Infinity" |
| -2 | nan() |
