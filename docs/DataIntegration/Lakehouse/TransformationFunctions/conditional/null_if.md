---
title: "NULL_IF"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/conditional/null_if.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Conditional"]
---

# NULL\_IF

If there is a **true** Boolean value in the **condition** parameter, then return null; otherwise, return the second argument

## Syntax

```
NULL_IF(condition, value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| condition | Boolean | If this is true, return null. Otherwise, return the second argument |  |
| value | any | This will be returned as-is if the first argument does not contain true. |  |

## Examples

| condition | value | Output |
| --- | --- | --- |
| true | "foo" | null |
| false | "foo" | `foo` |
| null::Boolean | "foo" | `foo` |
