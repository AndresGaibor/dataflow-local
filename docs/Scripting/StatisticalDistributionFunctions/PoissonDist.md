---
title: "PoissonDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/PoissonDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# PoissonDist Script and chart function

`PoissonDist()` returns the accumulated probability of the Poisson distribution.

Syntax:

PoissonDist(value, mean)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| `value` | The value at which you want to evaluate the distribution. The value must not be negative. |
| `mean` | A positive number defining the average outcome. |

This function is related
to the `PoissonInv` function in the following way:   
`If prob = PoissonDist(value, mean), then PoissonInv(prob, mean) = value`
