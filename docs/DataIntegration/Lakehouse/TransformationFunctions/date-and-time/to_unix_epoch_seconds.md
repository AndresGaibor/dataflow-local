---
title: "TO_UNIX_EPOCH_SECONDS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/to_unix_epoch_seconds.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# TO\_UNIX\_EPOCH\_SECONDS

Convert a date to its Epoch (Unix) seconds representation.

## Syntax

```
TO_UNIX_EPOCH_SECONDS(date)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| date | timestamp |  |  |

## Returns

bigint

---

## Examples

| date | Output |
| --- | --- |
| timestamp "2018-03-10 08:55:12.456" | 1520672112 |
