---
title: "TRIM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/trim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# TRIM

Removes leading and trailing whitespace from the given input string.

## Syntax

```
TRIM(STRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters.

## Returns

Type: `string`

`STRING` with any leading or trailing whitespaces removed.

---

## Examples

| STRING | Output |
| --- | --- |
| `abc` | `abc` |
| `abc` | `abc` |
| `abc` | `abc |
| `abc a` | `abc a` |
| `ab c a` | `ab c a` |
| `ab c a 3` | `ab c a 3` |
|  | `''` |
| `null` | `null` |
