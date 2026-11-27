---
title: "NormDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/NormDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# NormDist Script and chart function

NormDist() returns the cumulative normal
distribution for the specified mean and standard deviation. If mean = 0
and standard\_dev = 1, the function returns the standard normal distribution.

Syntax:

NORMDIST(value, [mean], [standard\_dev], [cumulative])

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. |
| mean | Optional value stating the arithmetic mean for the distribution.  If you do not state this argument, the default value is 0. |
| standard\_dev | Optional positive value stating the standard deviation of the distribution.  If you do not state this argument, the default value is 1. |
| cumulative | You can optionally select to use a standard normal distribution or a cumulative distribution.  0 = standard normal distribution  1 = cumulative distribution (default) |

This function is related to the NormInv function in
the following way:
If prob = NORMDIST(value, m,
sd), then NORMINV(prob, m, sd) = value

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| NORMDIST( 0.5, 0, 1) | Returns 0.6915 |

## Learn more

- [*NormInv Script and chart function*](NormInv.htm)
