---
title: "LEAST"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/comparison/least.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Comparison"]
---

# LEAST

This function returns the smallest of the provided values.

## Syntax

```
LEAST(VALUE1 [, VALUE2, ..., VALUEN])
```

## Arguments

#### **`VALUE`**

Type: `double`, `bigint`, `string`, `timestamp`, `date`, `array`

A value of any of the above types, provided that all values are of the same type.

## Returns

Type: same as input

The smallest of the provided values.

When the input values are arrays, the smallest element between all the arrays is returned.

If any of the input values are `null`, the result is `null` as well.
