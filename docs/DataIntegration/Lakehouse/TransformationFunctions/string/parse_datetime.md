---
title: "PARSE_DATETIME"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/parse_datetime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# PARSE\_DATETIME

Parses a string into a timestamp with time zone using format.

## Syntax

```
PARSE_DATETIME(input, format)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| input | string |  |  |
| format | string |  |  |

## Returns

Returns a `timestamp` value.

---

## Examples

| input | format | Output |
| --- | --- | --- |
| "2017-09-25 22:11:00" | "yyyy-MM-dd HH:mm:ss" | timestamp "2017-09-25 22:11:00" |
| "2018-03-19" | "yyyy-MM-dd" | timestamp "2018-03-19 00:00:00" |
| "2018\_Mar\_21" | "yyyy\_MMM\_dd" | timestamp "2018-03-21 00:00:00" |
| "2018\_Mar\_21\_17:59:05.689" | "yyyy\_MMM\_dd\_HH:mm:ss.SSS" | timestamp "2018-03-21 17:59:05.689" |
| "2012/02/22 12:34:56" | "Y/MM/d HH:mm:ss" | timestamp "2012-02-22 12:34:56" |
| "01-06-2021" | "dd-MM-YYYY" | timestamp "2021-06-01 00:00:00" |
| "01-06-2021" | "MM-dd-YYYY" | timestamp "2021-01-06 00:00:00" |
| "2021-05-13 19:02:57.415006+01:00" | "YYYY-MM-dd HH:mm:ss.SSSSSSZ" | timestamp "2021-05-13 18:02:57.415" |
