---
title: "ARRAY_SORT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_sort.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_SORT

Returns the values in the array in ascending order.

## Syntax

```
ARRAY_SORT(array)
```

## Arguments

#### **`array`**

Type: any

An array of any value types.

## Returns

Type: same as input but in ascending order.

---

## Examples

| array | Output |
| --- | --- |
| [2, 1, 3] | [1, 2, 3] |
| ["b", "a", "cd", "cc"] | ["a", "b", "cc", "cd"] |
| [0.5, 1.0, 0.75, 1.5] | [0.5, 0.75, 1.0, 1.5] |
| null::string | null |
| [true, false, true] | [false, true, true] |
| [date "2023-04-01", date "2023-04-01", date "2023-05-02"] | [date "2023-04-01", date "2023-04-01", date "2023-05-02"] |
| [timestamp "2023-01-02 11:00:00", timestamp "2023-01-01 09:00:00", timestamp "2023-01-01 10:00:00"] | [timestamp "2023-01-01 09:00:00", timestamp "2023-01-01 10:00:00", timestamp "2023-01-02 11:00:00"] |
