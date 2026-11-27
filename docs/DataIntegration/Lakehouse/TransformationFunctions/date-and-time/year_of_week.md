---
title: "YEAR_OF_WEEK"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/year_of_week.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# YEAR\_OF\_WEEK

Returns the year of [ISO week](https://en.wikipedia.org/wiki/ISO_week_date) from timestamp.

## Syntax

```
YEAR_OF_WEEK(timestamp)
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
| timestamp "2018-03-10 08:55:12.456" | 2018 |
