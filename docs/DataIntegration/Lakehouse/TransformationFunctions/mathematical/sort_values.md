---
title: "SORT_VALUES"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/sort_values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# SORT\_VALUES

Returns the values sorted in numerical order.

## Syntax

```
SORT_VALUES(descending, input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| descending | Boolean |  | false |
| input | numeric |  |  |

## Returns

Returns the same as the input.

---

## Examples

| descending | input | Output |
| --- | --- | --- |
| false | null::double | null |
| false | array["b", "c", "a"] | [`a`, `b`, `c`] |
| true | array["b", "c", "a"] | [`c`, `b`, `a`] |
| false | null::double | null |
| false | array[4, 2, 14] | [2, 4, 14] |
| false | array[1000.1, 1.2, 0.1] | [0.1, 1.2, 1000.1] |
| true | array[4, 2, 14] | [14, 4, 2] |
