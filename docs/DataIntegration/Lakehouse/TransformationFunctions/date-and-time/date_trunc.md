---
title: "DATE_TRUNC"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/date_trunc.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# DATE\_TRUNC

Truncate a date to a given time unit.

## Syntax

```
DATE_TRUNC(unit, time)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| unit | string |  |  |
| time | timestamp |  |  |

## Returns

timestamp

---

## Examples

| unit | time | Output |
| --- | --- | --- |
| "millisecond" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-03 04:05:06.789" |
| "second" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-03 04:05:06" |
| "minute" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-03 04:05:00" |
| "hour" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-03 04:00:00" |
| "day" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-03 00:00:00" |
| "week" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-01 00:00:00" |
| "month" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-02-01 00:00:00" |
| "quarter" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-01-01 00:00:00" |
| "year" | timestamp "2021-02-03 04:05:06.789" | timestamp "2021-01-01 00:00:00" |
| "millisecond" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-31 23:59:59.999" |
| "second" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-31 23:59:59" |
| "minute" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-31 23:59:00" |
| "hour" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-31 23:00:00" |
| "day" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-31 00:00:00" |
| "week" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-27 00:00:00" |
| "month" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-12-01 00:00:00" |
| "quarter" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-10-01 00:00:00" |
| "year" | timestamp "2021-12-31 23:59:59.999" | timestamp "2021-01-01 00:00:00" |
| "test" | timestamp "2021-12-31 23:59:59.999" | null |
