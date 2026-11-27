---
title: "STRPOS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/strpos.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# STRPOS

Returns the starting position of the first instance of a given substring within a string.

## Syntax

```
STRPOS(STRING, SUBSTRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters to search.

#### **`SUBSTRING`**

Type: `string`

The substring to search for.

## Returns

Type: `bigint`

Returns the starting position of the first instance of `SUBSTRING` in `STRING`.

Positions start from `1`. If no instance is found, `0` is returned.

---

## Examples

| STRING | SUBSTRING | Output |
| --- | --- | --- |
| All happy families are alike | all | 0 |
| All happy families are alike | All | 1 |
| All happy families are alike | are | 20 |
| All happy families are alike | `''` | 1 |
| `''` | `''` | 1 |
| `''` | word | 0 |
| `null` | word | `null` |
