---
title: "Combin Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/combin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Combin Script and chart function

Combin() returns the number of combinations of q
elements that can be picked from a set of p items. As represented by the formula: Combin(p,q) = p! / q!(p-q)! The order in which the items are selected is insignificant.

Syntax:

Combin(p, q)

Return data type:  integer

Limitations:

Non-integer
items will be truncated.

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| How many combinations of 7 numbers can be picked from a total of 35 lottery numbers?  Combin( 35,7 ) | Returns 6,724,520 |

## Learn more

- [*Permut Script and chart function*](permut.htm)
