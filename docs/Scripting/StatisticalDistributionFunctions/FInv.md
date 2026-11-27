---
title: "FInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/FInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# FInv Script and chart function

FInv() returns the inverse of the accumulated probability of the F distribution.

Syntax:

FInv(prob, degrees\_freedom1,
degrees\_freedom2)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the F-probability distribution and must be a number between 0 and 1. |
| degrees\_freedom | An integer stating the number of degrees of freedom. |

This function is related
to the FDist function in the following way:
If prob = FDIST(value, df1, df2),
then FINV(prob, df1, df2) = value

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| FINV( 0.0019369, 8, 6) | Returns 15.0000 |

## Learn more

- [*FDist Script and chart function*](FDist.htm)
