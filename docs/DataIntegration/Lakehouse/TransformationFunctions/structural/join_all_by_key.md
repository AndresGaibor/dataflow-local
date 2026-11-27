---
title: "JOIN_ALL_BY_KEY"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/join_all_by_key.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# JOIN\_ALL\_BY\_KEY

Combines multiple key value arrays into one by the keys.

## Syntax

```
JOIN_ALL_BY_KEY(fieldNames, inputs1[, inputs2, ..., inputsN])
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| fieldNames | string | Optional comma separated field names | "" |
| inputs# | any |  |  |

## Examples

| fieldNames | inputs1 | inputs2 | inputs3 | inputs4 | inputs5 | inputs6 | Output |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 'first,second,third' | array['a', 'b', 'c'] | array[1, 2, 3] | array['b', 'd', 'a'] | array[2, 4, 1] | array['c', 'b'] | array[false, true] | [{key: `a`, first: 1, second: 1, third: null}, {key: `b`, first: 2, second: 2, third: true}, {key: `c`, first: 3, second: null, third: false}, {key: `d`, first: null, second: 4, third: null}] |
