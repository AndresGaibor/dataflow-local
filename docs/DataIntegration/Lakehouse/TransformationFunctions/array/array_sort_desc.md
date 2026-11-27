---
title: "ARRAY_SORT_DESC"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_sort_desc.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_SORT\_DESC

Returns the values sorted in descending order.

## Syntax

```
ARRAY_SORT_DESC(array)
```

## Arguments

#### **`array`**

Type: any

An array of any value types.

## Returns

Type: same as input but in descending order.

---

## Examples

| array | Output |
| --- | --- |
| [2, 1, 3] | [3, 2, 1] |
| ["b", "a", "cd", "cc"] | ["cd", "cc", "b", "a"] |
| [0.5, 1.0, 0.75, 1.5] | [1.5, 1.0, 0.75, 0.5] |
| null::string | NULL |
| [true, false, true] | [true, true, false] |
| [date "2023-04-01", date "2023-04-01", date "2023-05-02"] | [date "2023-05-02", date "2023-04-01", date "2023-04-01"] |
| [timestamp "2023-01-02 11:00:00", timestamp "2023-01-01 09:00:00", timestamp "2023-01-01 10:00:00"] | [timestamp "2023-01-02 11:00:00", timestamp "2023-01-01 10:00:00", timestamp "2023-01-01 09:00:00"] |
