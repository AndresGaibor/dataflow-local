---
title: "Permut Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/permut.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Permut Script and chart function

Permut() returns the number of permutations of q elements that can be selected from a set of p items. As represented by the formula: Permut(p,q) = (p)! / (p - q)! The order in which the items are selected is significant.

Syntax:

Permut(p, q)

Return data type:  integer

Limitations:

Non-integer arguments will be truncated.

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| In how many ways could the gold, silver and bronze medals be distributed after a 100 m final with 8 participants?  Permut( 8,3 ) | Returns 336 |

## Learn more

- [*Combin Script and chart function*](combin.htm)
