---
title: "SPLIT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/split.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# SPLIT

Splits a string by the given delimiter.

## Syntax

```
SPLIT(STRING, DELIMITER)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters to split.

#### **`DELIMITER`**

Type: `string`

A sequence of one or more characters for specifying the boundary between separate, independent regions in plain text.

## Returns

Type: `array`

Splits `STRING` on `DELIMITER` and returns an array.

---

## Examples

| STRING | DELIMITER | Output |
| --- | --- | --- |
| abc | b | `['a','c']` |
| abc | d | `['abc']` |
| abcdefg | cde | `['ab','fb']` |
| 1234567 | 345 | `['12','67']` |
| 1234567 | 0 | `['1234567']` |
| 1234567 | `null` | `null` |
| `null` | 0 | `null` |
