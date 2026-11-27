---
title: "SIGN"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/sign.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# SIGN

Returns the signum function of the given input, that is:

- 0 if the argument is 0
- 1 if the argument is greater than 0
- -1 if the argument is less than 0

## Syntax

```
SIGN(X)
```

## Arguments

#### `X`

Type: `numeric`

A numeric value.

## Returns

Type: same as input

A value 1, 0, or -1 indicating the sign of `X`.

---

## Examples

| X | Output |
| --- | --- |
| 1 | 1 |
| -1 | -1 |
| 0 | 0 |
| 1.1 | 1.0 |
| -1.35 | -1.0 |
| 3 | 1 |
