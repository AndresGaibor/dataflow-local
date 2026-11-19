---
title: "TInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/TInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# TInv Script and chart function

`TInv()` returns the `t` value of the student's
`t` distribution as a function of the probability and the degrees of freedom.

Syntax:

TINV(prob, degrees\_freedom)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| prob | A two-tailed probability associated with the t-distribution. It must be a number between 0 and 1. |
| degrees\_freedom | An integer stating the number of degrees of freedom. |

Limitations:

All arguments must be numeric,
else NULL will be returned.

This function is related to the TDist
function in the following way:   
`If prob = TDIST(value, df ,2),
then TINV(prob, df) = value`.

Examples and results:

| Example | Result |
| --- | --- |
| TINV(0.3253086, 30 ) | Returns 1.0000 |

## Learn more

- [*TDist Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/TDist.htm)
