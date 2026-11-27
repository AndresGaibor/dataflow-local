---
title: "SPLIT_TO_RECORD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/split_to_record.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# SPLIT\_TO\_RECORD

Returns the given string split by the provided delimiter.

## Syntax

```
SPLIT_TO_RECORD(fieldNames, splitBy, filterEmptyValues, value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| fieldNames | string |  |  |
| splitBy | string |  | ',' |
| filterEmptyValues | boolean |  | false |
| value | string |  |  |

## Examples

| fieldNames | splitBy | filterEmptyValues | value | Output |
| --- | --- | --- | --- | --- |
| 'a,b,c' | ',' | false | '1,2,3,4' | {a: `1`, b: `2`, c: `3`} |
| 'a,b,c' | ',' | false | '1,2' | {a: `1`, b: `2`, c: ``} |
| 'a,b,c' | ',' | true | '1,,3' | {a: `1`, b: ``, c: `3`} |
