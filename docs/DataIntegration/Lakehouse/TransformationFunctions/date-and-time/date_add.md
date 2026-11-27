---
title: "DATE_ADD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/date_add.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# DATE\_ADD

Adds an interval of a specified unit to a given timestamp. Subtraction can be performed by using a negative interval value.

## Syntax

```
DATE_ADD(UNIT, VALUE, TIMESTAMP)
```

## Arguments

#### **`UNIT`**

Type: `string`

The unit of time to add.

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

#### **`VALUE`**

Type: `bigint`

The integer value of the `UNIT` to add to `TIMESTAMP`.

Can be positive (for times in the future) or negative (for times in the past).

#### **`TIMESTAMP`**

Type: `timestamp`

The timestamp to be modified.

## Returns

Type: `timestamp`

The `TIMESTAMP` with an `INTERVAL` of the given `NUMBER` added to it.

---

## Examples

| UNIT | VALUE | TIMESTAMP | Output |
| --- | --- | --- | --- |
| day | 1 | `2001-08-22 03:04:05.321` | `2001-08-23 03:04:05.321` |
| year | 5 | `2001-08-22 03:04:05.321` | `2006-08-22 03:04:05.321` |
| second | 30 | `2001-08-22 03:04:05.321` | `2001-08-22 03:04:35.321` |
| quarter | 1 | `2001-08-22 03:04:05.321` | `2001-11-22 03:04:05.321` |
| quarter | -1 | `2001-08-22 03:04:05.321` | `2001-05-22 03:04:05.321` |
| quarter | 0 | `2001-08-22 03:04:05.321` | `2001-08-22 03:04:05.321` |
| year | 1 | `null` | `null` |
