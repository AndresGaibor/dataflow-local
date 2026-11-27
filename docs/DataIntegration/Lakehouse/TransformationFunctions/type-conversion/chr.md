---
title: "CHR"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/type-conversion/chr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Type Conversion"]
---

# CHR

Returns the single character string corresponding to the given Unicode code point.

## Syntax

```
CHR(N)
```

## Arguments

#### `N`

Type: `bigint`

An integer representing a Unicode code point value.

## Returns

Type: `string`

The Unicode code point `N` as a single character string.

---

## Examples

| N | Output |
| --- | --- |
| 65 | A |
| 90 | Z |
| 48 | 0 |
| 57 | 9 |
| 32 | `''` |
| 97 | a |
| 122 | z |
| 33 | ! |
