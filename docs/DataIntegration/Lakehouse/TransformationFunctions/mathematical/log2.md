---
title: "LOG2"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/log2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# LOG2

Returns the base 2 logarithm of x.

## Syntax

```
LOG2(input)
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
| 2 | 1.0 |
| 16.0 | 4.0 |
| 0.5 | -1.0 |
| 15 | 3.9068905956085187 |
| 0 | '-Infinity' |
| -2 | nan() |
