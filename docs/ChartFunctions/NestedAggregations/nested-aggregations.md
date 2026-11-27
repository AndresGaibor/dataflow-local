---
title: "Nested aggregations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/NestedAggregations/nested-aggregations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---

# Nested aggregations

You may come across situations where you need to apply an [aggregation](#glossary-0 "Glossary term") to the result of another aggregation. This is referred to as nesting aggregations.

You cannot nest aggregations in most chart expressions. You can, however, nest aggregations if you use the TOTAL qualifier in the inner aggregation function.

Information note No more than 100 levels of nesting is allowed.

## Nested aggregations with the TOTAL qualifier

Example:

You want to calculate the sum of the [field](#glossary-1 "Glossary term") Sales, but only include transactions with an OrderDate equal to the last year. The last year can be obtained via the aggregation function Max(TOTAL
Year(OrderDate)).

The following aggregation would return the desired result:

Sum(If(Year(OrderDate)=Max(TOTAL Year(OrderDate)), Sales))

Qlik Sense requires the inclusion of the TOTAL
qualifier this type of nesting. It is necessary for the desired comparison. This type of nesting need is quite common and is a good practice.

## Learn more

- [*Aggr - chart function*](../aggr.htm)
