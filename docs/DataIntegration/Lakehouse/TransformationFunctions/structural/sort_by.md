---
title: "SORT_BY"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/sort_by.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# SORT\_BY

Sorts the values array by the sortKeys array.

## Syntax

```
SORT_BY(values, sortKeys)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| values | any |  |  |
| sortKeys | any |  |  |

## Examples

| values | sortKeys | Output |
| --- | --- | --- |
| array["a", "b"] | array["c", "d"] | [`a`, `b`] |
| array["a", "b"] | array["d", "c"] | [`b`, `a`] |
| array["a", "b"] | array[1, 2] | [`a`, `b`] |
| array["a", "b"] | array[2, 1] | [`b`, `a`] |
| array["a", "b"] | array[false, true] | [`a`, `b`] |
| array["a", "b"] | array[true, false] | [`b`, `a`] |
| array["a", "b"] | "c" | `a` |
