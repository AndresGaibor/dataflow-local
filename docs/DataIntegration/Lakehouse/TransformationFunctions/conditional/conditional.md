---
title: "Conditional functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/conditional/conditional.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions"]
---

# Conditional functions

Conditional functions evaluate one or more conditions and return results based on whether those conditions are true or false.

The following functions are available in Qlik Open Lakehouse:

| Function | Description |
| --- | --- |
| [COALESCE](coalesce.htm) | Returns the first input that is not null. If an input is an array, the whole array is returned. Empty arrays are not selected and are considered to be equivalent to a null value. |
| [IF\_ELSE](if_else.htm) | If there is a `true` Boolean value in the `condition` parameter, then return the second argument. In all other cases, return the third argument |
| [NULL\_IF](null_if.htm) | If there is a `true` Boolean value in the `condition` parameter, then return null. Otherwise, return the second argument |
