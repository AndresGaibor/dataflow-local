---
title: "GammaInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/GammaInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# GammaInv Script and chart function

`GammaInv()` returns the inverse of the accumulated probability of the Gamma distribution.

Syntax:

GammaInv(prob, k, θ)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| `prob` | A probability associated with the Gamma-probability distribution. It must be a number between 0 and 1. |
| `k` | A positive number defining the shape parameter. |
| `θ` | A positive number defining the scale parameter. |

This function is related
to the `GammaDist` function in the following way:   
`If prob = GammaDist(value, k, θ), then GammaInv(prob, k, θ) = value`
