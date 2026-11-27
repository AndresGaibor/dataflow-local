---
title: "EXTRACT_TIMESTAMP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/extract_timestamp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# EXTRACT\_TIMESTAMP

Convert a date or timestamp string to a date or timestamp, autodetecting the date format.

## Syntax

```
EXTRACT_TIMESTAMP(datetime)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| datetime | string | Convert a date or timestamp string to a date or timestamp, autodetecting the date format. |  |

## Returns

timestamp

---

## Examples

| datetime | Output |
| --- | --- |
| "2017-09-25 22:11:00" | timestamp "2017-09-25 22:11:00" |
| "2017-09-25T22:11:12Z" | timestamp "2017-09-25 22:11:12" |
| "2017-09-25T22:11:12.1Z" | timestamp "2017-09-25 22:11:12.100" |
| "2017-09-25T22:11:12.12Z" | timestamp "2017-09-25 22:11:12.120" |
| "2017-09-25T22:11:12.123Z" | timestamp "2017-09-25 22:11:12.123" |
| "2018-03-19" | timestamp "2018-03-19 00:00:00" |
| "2018\_Mar\_21\_17:59:05.689" | timestamp "2018-03-21 17:59:05.689" |
| "2018\_Mar\_21" | timestamp "2018-03-21 00:00:00" |
| "2018\_Mar\_21\_00:59:05.689 America/Los\_Angeles" | timestamp "2018-03-21 07:59:05.689" |
| "March 21, 2018 00:59:05.689 America/Los\_Angeles" | timestamp "2018-03-21 07:59:05.689" |
| "03/21/2020 00:59:05.689" | timestamp "2020-03-21 00:59:05.689" |
| "03/11/2020 00:59:05.689 America/Los\_Angeles" | timestamp "2020-03-11 07:59:05.689" |
| "03/11/2020 00:59:05.689 America/Los\_Angeles" | timestamp "2020-03-11 07:59:05.689" |
| "21/11/2020 00:59:05.689 America/Los\_Angeles" | timestamp "2020-11-21 08:59:05.689" |
| "https://www.zillow.com/homedetails/33-Rohde-Ave-St-Augustine-FL-32084/2099072901\_zpid/" | timestamp "2099-07-29 01:00:00" |
