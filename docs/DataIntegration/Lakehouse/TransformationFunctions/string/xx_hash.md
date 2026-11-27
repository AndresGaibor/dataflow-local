---
title: "XX_HASH"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/xx_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# XX\_HASH

Hashes the input using xxHash.

## Syntax

```
XX_HASH(input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | string |  |  |

## Returns

Returns a `bigint` value.

---

## Examples

| input | Output |
| --- | --- |
| "Hello xxHash" | -8183063398697651807 |
