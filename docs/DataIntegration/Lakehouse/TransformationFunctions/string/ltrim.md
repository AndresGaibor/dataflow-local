---
title: "LTRIM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/ltrim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# LTRIM

Removes any leading whitespace from a given string.

## Syntax

```
LTRIM(STRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters.

## Returns

Type: `string`

`STRING` with any leading whitespaces removed.

---

## Examples

| STRING | Output |
| --- | --- |
| `hey` | `hey` |
| `hey` | `hey` |
| `hey` | `hey` |
| `hey` | `hey` |
| `a b` | `a b` |
| `a b` | `a b` |
