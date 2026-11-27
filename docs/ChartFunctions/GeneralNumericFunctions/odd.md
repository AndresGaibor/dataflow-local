---
title: "Odd Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/odd.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Odd Script and chart function

Odd() returns True (-1), if integer\_number is an odd
integer or zero. It returns False (0), if integer\_number is an even integer, and NULL if integer\_number is not
an integer.

Syntax:

Odd(integer\_number)

Return data type:  Boolean

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Odd( 3 ) | Returns -1, True |
| Odd( 2 \* 10 ) | Returns 0, False |
| Odd( 3.14 ) | Returns NULL |

## Learn more

- [*Even Script and chart function*](even.htm)
