---
title: "Qlik Cloud Help"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/element_at.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: ""
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

ELEMENT\_AT

Retrieves the element of an array at a given index.

## Syntax

```
ELEMENT_AT(ARRAY(E), INDEX)
```

## Arguments

#### `ARRAY(E)`

Type: `array`

A array of values of any type.

#### `INDEX`

Type: `integer`

An integer indicating the index of the element to retrieve.

If `INDEX > 0`, this function provides the same functionality as the SQL-standard subscript operator (`[]`).

If `INDEX < 0`, this function accesses elements from the last to the first.

Note that if the `ARRAY` contains any `null` values, they are ignored in the indexing of the array.

## Returns

Type: same as input

The element of `ARRAY` at the given `INDEX`.

Note that if the `INDEX` is **0**, then the function returns `null`.

---

## Examples

| ARRAY | INDEX | Output |
| --- | --- | --- |
| `[5,2,3,1,2,3]` | 1 | 5 |
| `[5,2,3,1,2,3]` | 4 | 1 |
| `[5,2,3,1,2,3]` | 10 | `NULL` |
| `[5,2,3,1,6,3]` | -2 | 6 |
| `[a,2,p,34]` | 3 | p |
