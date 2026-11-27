---
title: "Fmod Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/fmod.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Fmod Script and chart function

fmod() is a generalized modulo function that returns the remainder part of the integer division of the first argument (the dividend) by the second argument (the divisor). The result is a real number. Both arguments are interpreted as real
numbers, that is, they do not have to be integers.

Syntax:

fmod(a, b)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| a | Dividend |
| b | Divisor |

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| fmod( 7,2 ) | Returns 1 |
| fmod( 7.5,2 ) | Returns 1.5 |
| fmod( 9,3 ) | Returns 0 |
| fmod( -4,3 ) | Returns -1 |
| fmod( 4,-3 ) | Returns 1 |
| fmod( -4,-3 ) | Returns -1 |

## Learn more

- [*Div Script and chart function*](div.htm)
