---
title: "ARRAY_DISTINCT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_distinct.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_DISTINCT

Returns all the distinct elements in the array.

## Syntax

```
ARRAY_DISTINCT(input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | any | The values to transform |  |

## Returns

an array of distinct values from the input. this function will maintain the order of the input. a primitive input will be considered an array with a single value and will return an array containing that value.

---

## Examples

| input | Output |
| --- | --- |
| array[1, 2, 3, 4, 4, 1] | [1, 2, 3, 4] |
