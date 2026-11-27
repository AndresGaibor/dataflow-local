---
title: "FORMAT_DATETIME"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/format_datetime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# FORMAT\_DATETIME

Converts a datetime value into a string.

## Syntax

```
FORMAT_DATETIME(datetime, format)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| datetime | timestamp | A datetime value. |  |
| format | string | A format string that is compatible with JodaTime’s pattern: http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html |  |

## Examples

| datetime | format | Output |
| --- | --- | --- |
| timestamp '2017-09-25 22:11:00' | 'yyyy/MM/dd HH:mm:ss.SSS' | `2017/09/25 22:11:00.000` |
| timestamp '2018-03-10 08:12:45' | 'yyyy/MM/dd' | `2018/03/10` |
| timestamp '2019-10-20 08:55:12.450' | 'HH:mm:ss.SS' | `08:55:12.45` |
| timestamp '2018-03-10 08:55:12.450' | 'E' | `Sat` |
