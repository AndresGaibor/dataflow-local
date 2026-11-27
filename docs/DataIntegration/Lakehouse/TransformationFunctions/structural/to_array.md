---
title: "TO_ARRAY"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/to_array.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# TO\_ARRAY

Outputs all the values from all the inputs as an array.

## Syntax

```
TO_ARRAY(inputs1[, inputs2, ..., inputsN])
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| inputs# | any |  |  |

## Returns

Returns the same as the input.

## Examples

| inputs1 | inputs2 | Output |
| --- | --- | --- |
| array["a", "c"] | "b" | [`a`, `c`, `b`] |
