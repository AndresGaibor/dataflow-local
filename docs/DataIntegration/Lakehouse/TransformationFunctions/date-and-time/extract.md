---
title: "EXTRACT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/extract.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# EXTRACT

Extracts a unit of time as a field from the given timestamp.

## Syntax

```
EXTRACT(FIELD FROM X)
```

## Arguments

#### `FIELD`

Type: `identifier`

The unit of time to extract.

The following fields are supported:

| Field | Description |
| --- | --- |
| `YEAR` | year |
| `QUARTER` | quarter |
| `MONTH` | month |
| `WEEK` | week |
| `DAY` | day |
| `DAY_OF_MONTH` | day |
| `DAY_OF_WEEK` | day of week |
| `DOW` | day of week |
| `DAY_OF_YEAR` | day of year |
| `DOY` | day of year |
| `YEAR_OF_WEEK` | year of week |
| `YOW` | year of week |
| `HOUR` | hour |
| `MINUTE` | minute |
| `SECOND` | second |

#### `X`

Type: `timestamp`

The time to extract `FIELD` from.

## Returns

Type: `bigint`

The `FIELD` extracted from `X`.

---

## Examples

| Field | X | Output |
| --- | --- | --- |
| year | `2012-02-22 00:00:00` | 2012 |
| month | `2012-02-22 00:00:00` | 02 |
| day | `2012-02-22 00:00:00` | 22 |
| hour | `2012-02-22 00:00:00` | 01 |
| minute | `2012-02-22 01:02:00` | 02 |
| second | `2012-02-22 01:00:32` | 21 |
| dow | `2012-02-22 01:00:32` | 3 |
| dow | `null` | `null` |
