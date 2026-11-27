---
title: "DATE_DIFF"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/date_diff.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# DATE\_DIFF

Computes the difference between two timestamps.

## Syntax

```
DATE_DIFF(UNIT, TIMESTAMP1, TIMESTAMP2)
```

## Arguments

#### **`UNIT`**

Type: `string`

The unit of time to return.

It can be one of the following:

- `year`
- `quarter`
- `month`
- `week`
- `day`
- `hour`
- `minute`
- `second`
- `millisecond`

#### **`TIMESTAMP1`**

Type: `timestamp`

The time to subtract from `TIMESTAMP2`.

#### **`TIMESTAMP2`**

Type: `timestamp`

The time `TIMESTAMP1` is subtracted from.

## Returns

Type: `bigint`

`TIME2 - TIME1` expressed in terms of `UNIT`.

---

## Examples

| UNIT | TIMESTAMP1 | TIMESTAMP2 | Output |
| --- | --- | --- | --- |
| day | `2001-08-22 03:04:05.321` | `2001-08-23 03:04:05.321` | 1 |
| year | `2001-08-22 03:04:05.321` | `2006-08-22 03:04:05.321` | 5 |
| year | `2006-08-22 03:04:05.321'` | `2001-08-22 03:04:05.321` | -5 |
| second | `2001-08-22 03:04:05.321` | `2001-08-22 03:04:35.321` | 30 |
| quarter | `2001-08-22 03:04:05.321` | `2001-11-22 03:04:05.321` | 1 |
| quarter | `2001-08-22 03:04:05.321` | `2001-08-22 03:04:05.321` | 0 |
| year | `2001-08-22 03:04:05.321` | `null` | `null` |
