---
title: "TRIM_CHARS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/trim_chars.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# TRIM\_CHARS

Returns the given string without leading or trailing characters.

## Syntax

```
TRIM_CHARS(characters, input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| characters | string |  |  |
| input | string |  |  |

## Returns

Returns a `string` value.

---

## Examples

| characters | input | Output |
| --- | --- | --- |
| "-=" | "-==–Hello World—=—" | `Hello World` |
| "-" | '' | `` |
| "-" | "———–" | `` |
| "-" | "x———–" | `x` |
| "-" | "———–x" | `x` |
| "-" | "——x—–" | `x` |
| "-" | "x———–x" | `x-----------x` |
