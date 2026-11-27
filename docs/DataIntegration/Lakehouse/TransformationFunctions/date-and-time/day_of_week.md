---
title: "DAY_OF_WEEK"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/day_of_week.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# DAY\_OF\_WEEK

Returns the ISO day of the week from a timestamp.

Return values range from **1** to **7** :

| ISO Day of Week | Week Day |
| --- | --- |
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |
| 7 | Sunday |

## Syntax

```
DAY_OF_WEEK(timestamp)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| timestamp | timestamp |  |  |

## Returns

bigint

---

## Examples

| timestamp | Output |
| --- | --- |
| timestamp "2018-03-10 08:55:12.456" | 6 |
