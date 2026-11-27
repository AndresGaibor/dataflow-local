---
title: "IF_ELSE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/conditional/if_else.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Conditional"]
---

# IF\_ELSE

If there is a **true** Boolean value in the **condition** parameter, then return the second argument; in all other cases, return the third argument

## Syntax

```
IF_ELSE(condition, true_value, false_value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| condition | Boolean | If this is true, return the second argument, otherwise return the third argument. |  |
| true\_value | any | The value to return when the condition is true |  |
| false\_value | any | The value to return when the condition is not true |  |

## Examples

| condition | true\_value | false\_value | Output |
| --- | --- | --- | --- |
| true | 'foo' | 'bar' | `foo` |
| false | 'foo' | 'bar' | `bar` |
| null::Boolean | 'foo' | 'bar' | `bar` |
