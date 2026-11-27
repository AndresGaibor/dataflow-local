---
title: "CEIL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/ceil.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# CEIL

Rounds the given input up to the nearest integer.

This is an alias for the [`CEILING`](ceiling.htm) function.

## Syntax

```
CEIL(X)
```

## Arguments

#### **`X`**

Type: `numeric`

A numeric value.

## Returns

Type: same as input

`X` rounded up to the nearest integer.

---

## Examples

| X | Output |
| --- | --- |
| 0.13523523 | 1.0 |
| -1.1 | -1.0 |
| 1 | 1 |
| 1 + 1 | 2 |
| 0 | 0 |
| -1 | -1 |
| -1 - 5 | -6 |
