---
title: "Div Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/div.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Div Script and chart function

Div() returns the integer part of the arithmetic division of the first argument by the second argument. Both parameters are interpreted as real numbers, that is,
they do not have to be integers.

Syntax:

Div(integer\_number1, integer\_number2)

Return data type:  integer

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Div( 7,2 ) | Returns 3 |
| Div( 7.1,2.3 ) | Returns 3 |
| Div( 9,3 ) | Returns 3 |
| Div( -4,3 ) | Returns -1 |
| Div( 4,-3 ) | Returns -1 |
| Div( -4,-3 ) | Returns 1 |

## Learn more

- [*Mod Script and chart function*](mod.htm)
