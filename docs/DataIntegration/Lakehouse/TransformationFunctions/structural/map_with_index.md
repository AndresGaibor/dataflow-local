---
title: "MAP_WITH_INDEX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/map_with_index.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# MAP\_WITH\_INDEX

Outputs an index and a value field. Index contains a zero based index, and value contains the value in the input field.

## Syntax

```
MAP_WITH_INDEX(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | any | The value to convert to a record |  |

## Examples

| value | Output |
| --- | --- |
| array['a', 'b', 'c'] | [{index: 0, value: `a`}, {index: 1, value: `b`}, {index: 2, value: `c`}] |
