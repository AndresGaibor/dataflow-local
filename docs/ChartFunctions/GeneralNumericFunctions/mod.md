---
title: "Mod Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/mod.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Mod Script and chart function

Mod() is a mathematical modulo function that returns the non-negative remainder of an integer division. The first argument is the dividend, the second argument is the divisor, Both arguments must be integer values.

Syntax:

Mod(integer\_number1, integer\_number2)

Return data type:  integer

Limitations:

integer\_number2 must be greater than 0.

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Mod( 7,2 ) | Returns 1 |
| Mod( 7.5,2 ) | Returns NULL |
| Mod( 9,3 ) | Returns 0 |
| Mod( -4,3 ) | Returns 2 |
| Mod( 4,-3 ) | Returns NULL |
| Mod( -4,-3 ) | Returns NULL |

## Learn more

- [*Div Script and chart function*](div.htm)
