---
title: "ChiDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/ChiDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# ChiDist Script and chart function

`ChiDist()` returns the one-tailed probability
of the chi2 distribution. The chi2 distribution is associated with a chi2 test.

Syntax:

CHIDIST(value,
degrees\_freedom)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must not be negative. |
| degrees\_freedom | A positive integer stating the number of degrees of freedom. |

This function is related
to the ChiInv function in the following way:   
`If prob = CHIDIST(value,df),
then CHIINV(prob, df) = value`

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| CHIDIST( 8, 15) | Returns 0.9238 |

## Learn more

- [*ChiInv Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/ChiInv.htm)
