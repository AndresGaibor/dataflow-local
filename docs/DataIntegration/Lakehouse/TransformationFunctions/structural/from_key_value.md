---
title: "FROM_KEY_VALUE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/from_key_value.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# FROM\_KEY\_VALUE

Maps a list of key values to a record with fields for each key.

## Syntax

```
FROM_KEY_VALUE(keys, key, value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| keys | string |  |  |
| key | string |  |  |
| value | any |  |  |

## Examples

| keys | key | value | Output |
| --- | --- | --- | --- |
| 'foo, hello' | array['foo', 'hello'] | array['bar', 'world'] | {foo: `bar`, hello: `world`} |
| 'foo, hello' | array['foo', 'hoo'] | array['bar', 'zoo'] | {foo: `bar`, hello: null} |
