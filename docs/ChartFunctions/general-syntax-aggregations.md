---
title: "General syntax for aggregations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/general-syntax-aggregations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions"]
---

# General syntax for aggregations

The following general syntax structure can be used for aggregations, with many optional parameters:

aggrexpression
::= ( fieldref | operator1
aggrexpression | aggrexpression
operator2 aggrexpression | functioninaggr | ( aggrexpression
)
)

fieldref is a [field](#glossary-0 "Glossary term") name.

functionaggr ::= functionname (
parameters2 )

Expressions and functions can thus be nested freely, as long as fieldref is always enclosed by exactly one [aggregation](#glossary-1 "Glossary term") function and provided the expression returns an interpretable
value, Qlik Sense does not give any error messages.

## Learn more

- [*Operators*](../Scripting/Operators/operators.htm)
