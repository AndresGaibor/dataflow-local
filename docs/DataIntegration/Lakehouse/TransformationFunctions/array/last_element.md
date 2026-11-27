---
title: "LAST_ELEMENT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/last_element.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# LAST\_ELEMENT

Returns the last element in the array.

## Syntax

```
LAST_ELEMENT(input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | any |  |  |

## Examples

| input | Output |
| --- | --- |
| null::string | null |
| array["a", "b", "c"] | `c` |
