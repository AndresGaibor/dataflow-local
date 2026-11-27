---
title: "STRIP_PREFIX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/strip_prefix.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# STRIP\_PREFIX

Remove the given prefix from the beginning of the string.

## Syntax

```
STRIP_PREFIX(input, prefix)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | string |  |  |
| prefix | string |  |  |

## Returns

Returns a `string` value.

---

## Examples

| input | prefix | Output |
| --- | --- | --- |
| "((foo))" | "(" | `(foo))` |
| "foo" | "(" | `foo` |
