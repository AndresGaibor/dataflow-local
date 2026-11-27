---
title: "ARRAY_MIN"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array_min.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Array"]
---

# ARRAY\_MIN

Returns the minimum value of the given input array.

## Syntax

```
ARRAY_MIN(X)
```

## Arguments

#### **`X`**

Type: `array`

An array of any comparable value type.

## Returns

Type: same as input

The minimum value of `X`.

---

## Examples

| X | Output |
| --- | --- |
| [1,2,3,1,2,3] | 1 |
| [1,1,1,1,1,1,1] | 1 |
| [0,1,0,1,0,1] | 0 |
| [NULL,1,0,1,0,1] | NULL |
| [a,b,a,c,c,c] | a |
| [NULL] | NULL |
| [a,b,c,z] | a |
| [true, false] | false |
