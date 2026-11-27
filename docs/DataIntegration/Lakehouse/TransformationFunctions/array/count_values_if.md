---
title: "COUNT_VALUES_IF"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/count_values_if.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# COUNT\_VALUES\_IF

Returns the number of `true` values in a given array.

This can be used with conditional operators to count the number of array elements that fulfil a condition. For example, `COUNT_VALUES_IF(my_values[] > 3)` will return the number of elements that are greater than 3.

## Syntax

```
COUNT_VALUES_IF(input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | Boolean | The input array |  |

## Returns

the number of times `true` appeared in the input array. a primitive value is considered to be an array with one element.

---

## Examples

| input | Output |
| --- | --- |
| null::Boolean | 0 |
| array[true, false, true] | 2 |
