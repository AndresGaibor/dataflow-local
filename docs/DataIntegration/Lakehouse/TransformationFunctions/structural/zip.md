---
title: "ZIP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/zip.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# ZIP

Merges the given arrays, element-wise, into a single array of rows.

## Syntax

```
ZIP(ARRAY1, ARRAY2 [, ...])
```

## **Arguments**

#### `ARRAY`

Type: `array`

A array of values of any type.

## Returns

Type: `array`

The given arrays merged element-wise into a single array of rows.

The M-th element of the N-th argument will be the N-th field of the M-th output element. If the arguments have an uneven length, missing values are filled with `NULL`.
