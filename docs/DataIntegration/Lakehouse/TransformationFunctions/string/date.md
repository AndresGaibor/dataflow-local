---
title: "DATE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/date.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# DATE

Casts a string value to a date.

## Syntax

```
DATE(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string |  |  |

## Returns

Returns a `date` value.

---

## Examples

| value | Output |
| --- | --- |
| "2022-02-01" | date "2022-02-01" |
| timestamp "2022-02-01 00:00:00" | date "2022-02-01" |
| timestamp "2022-01-01 00:30:00" | date "2022-01-01" |
