---
title: "QUARTER"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/quarter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Date & Time"]
---

# QUARTER

Returns the quarter of the year from a timestamp.

Values range from **1** to **4**.

## Syntax

```
QUARTER(timestamp)
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
| timestamp "2018-03-10 08:55:12.456" | 1 |
