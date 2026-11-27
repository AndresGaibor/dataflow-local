---
title: "FROM_UNIXTIME"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/from_unixtime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# FROM\_UNIXTIME

Convert Epoch seconds to a timestamp.

Warning note

This function uses Epoch seconds as a value, to convert Epoch Milliseconds value divide the value by a thousand (value/1000)

## Syntax

```
FROM_UNIXTIME(unix_timestamp)
```

## Arguments

| value | Type | Description | Default Value |
| --- | --- | --- | --- |
| unix\_timestamp | numeric |  |  |

## Returns

timestamp

---

## Examples

| datetime | Output |
| --- | --- |
| 1641000600 | timestamp "2022-01-01 01:30:00" |
| 1520672112.456 | timestamp "2018-03-10 08:55:12.456" |
