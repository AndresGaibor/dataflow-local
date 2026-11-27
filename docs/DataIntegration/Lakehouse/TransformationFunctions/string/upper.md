---
title: "UPPER"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/upper.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# UPPER

Converts the string to uppercase letters.

## Syntax

```
UPPER(STRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters.

## Returns

Type: `string`

`STRING` in uppercase letters.

---

## Examples

"SELECT UPPER("a") = "A" AND UPPER("abc") = "ABC" AND UPPER("123") = "123" AND UPPER("abc") = "ABC" AND UPPER('-=@#$') = "-=@#$" AND UPPER(null) is null AND UPPER(CAST(null as varchar)) is null"

| STRING | Output |
| --- | --- |
| a | A |
| abc | ABC |
| 123 | 123 |
| abc | ABC |
| -=@#$ | -=@#$ |
| `null` | `null` |
