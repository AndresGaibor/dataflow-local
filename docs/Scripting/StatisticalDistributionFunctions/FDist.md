---
title: "FDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/FDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# FDist Script and chart function

FDist() returns the accumulated probability of the F distribution.

Syntax:

FDist(value,
degrees\_freedom1, degrees\_freedom2)

Return data type:  number

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must not be negative. |
| degrees\_freedom1 | A positive integer stating the number of numerator degrees of freedom. |
| degrees\_freedom2 | A positive integer stating the number of denominator degrees of freedom. |

This function is related
to the FInv
function in the following way:
If prob = FDIST(value, df1, df2),
then FINV(prob, df1, df2) = value

Limitations:

All arguments must be numeric,
else NULL will be returned.

Examples and results:

| Example | Result |
| --- | --- |
| FDIST(15, 8, 6) | Returns 0.0019 |

## Learn more

- [*FInv Script and chart function*](FInv.htm)
