---
title: "GammaDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/GammaDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# GammaDist Script and chart function

GammaDist() returns the accumulated probability of the Gamma distribution.

Syntax:

GammaDist(value, k, θ)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must not be negative. |
| k | A positive number defining the shape parameter. |
| θ | A positive number defining the scale parameter. |

This function is related
to the GammaINV function in the following way:
If prob = GammaDist(value, k, θ), then GammaInv(prob, k, θ) = value
