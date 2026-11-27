---
title: "QUERY_STRING_TO_RECORD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/query_string_to_record.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# QUERY\_STRING\_TO\_RECORD

Extracts data from the query string.

## Syntax

```
QUERY_STRING_TO_RECORD(mappings, value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| mappings | string | Field names |  |
| value | string |  |  |

## Examples

| mappings | value | Output |
| --- | --- | --- |
| "a,string" | "a=Hello" | {a: `Hello`} |
| "a,string |  |  |
| b,string" | "a=Hello&b=World" | {a: `Hello`, b: `World`} |
