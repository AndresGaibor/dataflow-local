---
title: "COALESCE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/conditional/coalesce.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Conditional"]
---

# COALESCE

Returns the first value in a given list that is not `null`.

## Syntax

```
COALESCE(VALUE1, VALUE2[, ...])
```

## Arguments

#### `VALUE`

Type: any

A list of values of any type.

## Returns

Type: same as input

The first `VALUE` that is not `null`.
