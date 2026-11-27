---
title: "ARRAY_SUM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_sum.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_SUM

This function calculates the sum of all non-null elements of the input.

If there are no non-null elements, the function returns **0**. The behavior is similar to the `SUM` aggregate function but operates on an array.

## Syntax

```
ARRAY_SUM(array)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| array | numeric | A numeric array |  |

## Returns

The sum of all non-null elements of the input. If there are no non-null elements, the function returns **0**. A primitive value input is considered to be an array with a single element.

---

## Examples

| array | Output |
| --- | --- |
| array[1, 0.2, 30] | 31.2 |
