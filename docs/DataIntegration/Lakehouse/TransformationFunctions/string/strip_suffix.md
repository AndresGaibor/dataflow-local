---
title: "STRIP_SUFFIX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/strip_suffix.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# STRIP\_SUFFIX

Remove the given suffix from the end of the string.

## Syntax

```
STRIP_SUFFIX(input, suffix)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | string |  |  |
| suffix | string |  |  |

## Returns

Returns a `string` value.

---

## Examples

| input | suffix | Output |
| --- | --- | --- |
| "((foo))" | ")" | `((foo)` |
| "foo" | ")" | `foo` |
