---
title: "TDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/TDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# TDist Script and chart function

TDist() returns the probability for the
student's t distribution where a numeric value is a calculated value of t for which the probability is to be computed.

Syntax:

TDist(value,
degrees\_freedom, tails)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must not be negative. |
| degrees\_freedom | A positive integer stating the number of degrees of freedom. |
| tails | Must be either 1 (one-tailed distribution) or 2 (two-tailed distribution). |

This function is related to the TInv function
in the following way:
If prob = TDIST(value, df ,2),
then TINV(prob, df) = value

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| TDIST(1, 30, 2) | Returns 0.3253 |

## Learn more

- [*TInv Script and chart function*](TInv.htm)
