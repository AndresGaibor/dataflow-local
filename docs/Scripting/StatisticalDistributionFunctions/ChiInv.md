---
title: "ChiInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/ChiInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# ChiInv Script and chart function

`ChiInv()` returns the inverse of the one-tailed
probability of the chi2 distribution.

Syntax:

CHIINV(prob,
degrees\_freedom)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the chi2 distribution. It must be a number between 0 and 1. |
| degrees\_freedom | An integer stating the number of degrees of freedom. |

This function is related
to the ChiDist
function in the following way:   
`If prob = CHIDIST(value,df),
then CHIINV(prob, df) = value`

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| CHIINV(0.9237827, 15 ) | Returns 8.0000 |

## Learn more

- [*ChiDist Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/ChiDist.htm)
