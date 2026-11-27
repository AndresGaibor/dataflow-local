---
title: "Frac Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/frac.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Frac Script and chart function

Frac() returns the fraction part of x.

The fraction is defined in such a way that Frac(x
) + Floor(x ) = x. In simple terms, this means that the fractional part of a positive number is the difference between the number (x) and the integer that precedes the fractional part.

For example: The fractional part of 11.43 = 11.43 - 11 = 0.43

For a negative number, say -1.4, Floor(-1.4) = -2, which produces the following result:

The fractional part of -1.4 = -1.4 - (-2) = -1.4 + 2 = 0.6

Syntax:

Frac(x)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| x | Number to return fraction for. |

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Frac( 11.43 ) | Returns 0.43 |
| Frac( -1.4 ) | Returns 0.6 |
| Extract the time component from the numeric representation of a timestamp, thus omitting the date.  Time(Frac(44518.663888889)) | Returns 3:56:00 PM |

## Learn more

- [*Floor Script and chart function*](floor.htm)
