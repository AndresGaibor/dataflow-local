---
title: "SUBTRACT_TIME_ZONE_OFFSET"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/subtract_time_zone_offset.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# SUBTRACT\_TIME\_ZONE\_OFFSET

Subtracts a timezone offset from a date.

The timezone offset can be any standard format accepted by Java's `ZoneId.of` method (America/New\_York, +02:00, etc.)

## Syntax

```
SUBTRACT_TIME_ZONE_OFFSET(time, zone)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| time | timestamp |  |  |
| zone | string |  |  |

## Returns

timestamp

---

## Examples

| time | zone | Output |
| --- | --- | --- |
| timestamp "2018-03-10 08:55:12.456" | "+02:00" | timestamp "2018-03-10 06:55:12.456" |
| timestamp "2018-03-10 08:55:12.456" | "America/New\_York" | timestamp "2018-03-10 13:55:12.456" |
| timestamp "2018-03-10 08:55:12.456" | '' | null |
| timestamp "2018-03-10 08:55:12.456" | "Invalid Zone Id" | null |
