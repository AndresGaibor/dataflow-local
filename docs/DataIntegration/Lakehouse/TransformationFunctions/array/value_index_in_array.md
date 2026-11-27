---
title: "VALUE_INDEX_IN_ARRAY"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/value_index_in_array.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# VALUE\_INDEX\_IN\_ARRAY

Calculates a 1-based positional index for each non-null value within a sub-array, resetting the index with each new sub-array. This is particularly useful for maintaining context-specific indexes within nested array structures.

## Syntax

```
VALUE_INDEX_IN_ARRAY(array)
```

## Arguments

#### `array`

Type: any

An array of any value types.
