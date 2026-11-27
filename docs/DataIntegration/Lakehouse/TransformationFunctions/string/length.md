---
title: "LENGTH"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/length.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# LENGTH

Returns the length of a given string.

## Syntax

```
LENGTH(STRING)
```

## Arguments

#### `STRING`

Type: `string`

A sequence of characters.

## Returns

Type: `bigint`

The length of `STRING` in characters.

---

## Examples

| STRING | Output |
| --- | --- |
| 1 | 1 |
| abcdefg | 7 |
| 12345 | 5 |
| `null` | `null` |
| `''` | 0 |
| -=^%$ | 5 |
