---
title: "CAST"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/type-conversion/cast.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Type Conversion"]
---

# CAST

Casts the input expression to the specified type.

## Syntax

```
CAST(<expression> AS <type>)
```

## Example

#### SQL

In the the following example, the **nettotal** column, which is a double, is converted to a string to enable it to be concatenated with the dollar symbol:

```
'$' || CAST(nettotal AS STRING)
```

```
Query result
```

| orderid | nettotal | orderdate |
| --- | --- | --- |
| cU1QEyPKKc | $2018.37 | 2023-07-24T15:54:00Z |
| 6eI2KeIc2A | $1842.35 | 2023-07-24T15:54:00Z |
| yRQUXyRPTP | $1144.7 | 2023-07-24T15:54:00Z |
