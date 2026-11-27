---
title: "VALUE_INDEX_IN_ROW"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/value_index_in_row.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# VALUE\_INDEX\_IN\_ROW

Calculates a continuous, 1-based positional index for each value in an array, treating the entire row as a single context. It assigns a unique index to each non-null element across the arrays within the row.

## Syntax

```
VALUE_INDEX_IN_ROW(array)
```

## Arguments

#### `array`

Type: any

An array of any value types.
