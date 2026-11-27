---
title: "RANDOM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/mathematical/random.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Mathematical"]
---

# RANDOM

Returns a pseudo-random value in the range 0.0 <= x < 1.0.

## Syntax

```
RANDOM()
```

## Returns

type: `double`

A pseudo-random value in the range 0.0 <= x < 1.0

The value will not change between different runs of the same task, i.e. if the result of this function makes the task fail, it will consistently fail.
