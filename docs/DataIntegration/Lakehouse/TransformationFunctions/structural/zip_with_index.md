---
title: "ZIP_WITH_INDEX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/zip_with_index.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# ZIP\_WITH\_INDEX

Combines multiple arrays by index into records

## Syntax

```
ZIP_WITH_INDEX(fieldNames, inputs1[, inputs2, ..., inputsN])
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| fieldNames | string | Optional comma separated field names | "" |
| inputs# | any |  |  |

## Examples

| fieldNames | inputs1 | inputs2 | inputs3 | Output |
| --- | --- | --- | --- | --- |
| null::string | array['a', 'b', 'c'] | array[1, 2] | array[false, true, false] | [{index: 0, field\_1: `a`, field\_2: 1, field\_3: false}, {index: 1, field\_1: `b`, field\_2: 2, field\_3: true}, {index: 2, field\_1: `c`, field\_2: null, field\_3: false}] |
