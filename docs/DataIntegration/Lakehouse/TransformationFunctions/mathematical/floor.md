---
title: "FLOOR"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/floor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# FLOOR

Rounds the given input down to the nearest integer.

## Syntax

```
FLOOR(X)
```

## Arguments

#### **`X`**

Type: `numeric`

A numeric value.

## Returns

Type: same as input

`X` rounded down to the nearest integer.

---

## Examples

| X | Output |
| --- | --- |
| 0.13523523 | 0.0 |
| -0.1 | -1.0 |
| -1.1 | -2.0 |
| 1 | 1 |
| 1 + 1 | 2 |
| 0 | 0 |
| -1 | -1 |
| -1 - 5 | -6 |
