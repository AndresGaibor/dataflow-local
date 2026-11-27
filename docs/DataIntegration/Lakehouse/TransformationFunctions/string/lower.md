---
title: "LOWER"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/lower.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# LOWER

Converts the given string to lowercase letters.

## Syntax

```
LOWER(STRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters.

## Returns

Type: `string`

`STRING` in lowercase letters.

---

## Examples

| STRING | Output |
| --- | --- |
| A | a |
| ABC | abc |
| 123 | 123 |
| abc | abc |
| -=@#$ | -=@#$ |
| `null` | `null` |
