---
title: "BetaDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/BetaDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# BetaDist Script and chart function

`BetaDist()` returns the accumulated probability of the Beta distribution.

Syntax:

BetaDist(value, alpha, beta)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| `value` | The value at which you want to evaluate the distribution. The value must be between 0 and 1. |
| `alpha` | A positive number defining the first shape parameter. It is the exponent of the random variable |
| `beta` | A positive number defining the second shape parameter. It is the exponent that controls the shape of the distribution. |

This function is related
to the `BetaInv` function in the following way:   
`If prob = BetaDist(value, alpha, beta), then BetaInv(prob, alpha, beta) = value`
