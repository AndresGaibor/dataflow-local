---
title: "LOG"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/log.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# LOG

Return the logarithm of x to the given base.

## Syntax

```
LOG(base, input)
```

## Arguments

| Name | Type |
| --- | --- |
| base | numeric |
| input | numeric |

## Returns

`Double`

---

## Examples

| base | input | Output |
| --- | --- | --- |
| 2 | 2 | 1.0 |
| 0.5 | 1 | 0.0 |
| 5 | 0.04 | -2.0 |
| 10 | 0 | "-Infinity" |
| 1 | 10 | "Infinity" |
| 10 | -2 | nan() |
