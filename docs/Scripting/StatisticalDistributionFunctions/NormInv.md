---
title: "NormInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/NormInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# NormInv Script and chart function

`NormInv()` returns the inverse of the normal
cumulative distribution for the specified mean and standard deviation.

Syntax:

NORMINV(prob,
mean, standard\_dev)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the normal distribution. It must be a number between 0 and 1. |
| mean | A value stating the arithmetic mean for the distribution. |
| standard\_dev | A positive value stating the standard deviation of the distribution. |

This function
is related to the NormDist function in
the following way:   
`If prob = NORMDIST(value, m,
sd), then NORMINV(prob, m, sd) = value`

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| NORMINV( 0.6914625, 0, 1 ) | Returns 0.5000 |

## Learn more

- [*NormDist Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/NormDist.htm)
