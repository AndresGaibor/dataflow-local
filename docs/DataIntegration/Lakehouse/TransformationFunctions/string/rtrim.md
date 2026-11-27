---
title: "RTRIM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/rtrim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# RTRIM

Removes any trailing whitespace from a given string.

## Syntax

```
RTRIM(STRING)
```

## Arguments

#### **`STRING`**

Type: `string`

A sequence of characters.

## Returns

Type: `string`

`STRING` with any trailing whitespaces removed.

---

## Examples

| STRING | Output |
| --- | --- |
| `hey` | `hey` |
| `hey` | `hey` |
| `hey` | `hey` |
| `hey` | `hey` |
| `a b` | `a b` |
