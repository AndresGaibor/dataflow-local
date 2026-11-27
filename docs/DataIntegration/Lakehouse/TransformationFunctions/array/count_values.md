---
title: "COUNT_VALUES"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/count_values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# COUNT\_VALUES

Returns the number of non-null items in a given array.

## Syntax

```
COUNT_VALUES(input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | any | The input array |  |

## Returns

The number of non-null items in the input array. If the input is a primitive value, **0** will be returned if null, and otherwise **1 1** will be returned.

---

## Examples

| input | Output |
| --- | --- |
| null::string | 0 |
| array["a", "b", "c"] | 3 |
| array[1, 2, 3, 4] | 4 |
