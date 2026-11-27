---
title: "JSON_TO_RECORD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/json_to_record.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# JSON\_TO\_RECORD

Extracts data from JSON objects.

## Syntax

```
JSON_TO_RECORD(mappings, outputArray, value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| mappings | string | JSON to field mappings |  |
| outputArray | Boolean | If the string contains multiple JSON records use this to allow outputing all of them | true |
| value | string |  |  |

## Examples

| mappings | outputArray | value | Output |
| --- | --- | --- | --- |
| 'a,a,string' | true | '{ "a": "Hello" }' | {a: `Hello`} |
| 'a,a,number' | true | '{ "a": 1579540882000 }' | {a: 1579540882000} |
| 'a.value,a.value,string |  |  |  |
| b.value,b.value,string' | true | '{ "a": { "value": "Hello" }, "b" : { "value": "World" } }' | {a.value: `Hello`, b.value: `World`} |
| 'a.value,a.value,string |  |  |  |
| b.value,b.value,string /*this is a comment inside the mapping*/' | true | '{ "a": { "value": "Hello" }, "b" : { "value": "World" } }' | {a.value: `Hello`, b.value: `World`} |
| 'a.value,a.value,string |  |  |  |
| b.value,b.value,string' | true | '{ "a": null::string, "b" : { "value": "World" } }' | {a.value: null, b.value: `World`} |
