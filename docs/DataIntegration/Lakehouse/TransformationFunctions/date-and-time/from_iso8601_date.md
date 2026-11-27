---
title: "FROM_ISO8601_DATE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/from_iso8601_date.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# FROM\_ISO8601\_DATE

Parses the ISO 8601 formatted string into a date.

## Syntax

```
FROM_ISO8601_DATE(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string |  |  |

## Returns

date

---

## Examples

| value | Output |
| --- | --- |
| "2006-04-06" | date "2006-04-06" |
| "2006-4-6" | date "2006-04-06" |
| "2006-03" | date "2006-03-01" |
| "2006-3" | date "2006-03-01" |
| "2006" | date "2006-01-01" |
| "2006-121" | date "2006-05-01" |
| "2006-009" | date "2006-01-09" |
| "2009-W41-7" | date "2009-10-11" |
| "2009-W41" | date "2009-10-05" |
| "2009-W1-1" | date "2008-12-29" |
| "06-12-12" | date "0006-12-12" |
| "6-12-12" | date "0006-12-12" |
| "6" | date "0006-01-01" |
