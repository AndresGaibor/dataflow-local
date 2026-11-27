---
title: "BetaInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/BetaInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# BetaInv Script and chart function

BetaINV() returns the inverse of the accumulated probability of the Beta distribution.

Syntax:

BetaInv(prob, alpha, beta)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the Beta-probability distribution. It must be a number between 0 and 1. |
| alpha | A positive number defining the first shape parameter. It is the exponent of the random variable |
| beta | A positive number defining the second shape parameter. It is the exponent that controls the shape of the distribution. |

This function is related
to the BetaDist function in the following way:
If prob = BetaDist(value, alpha, beta), then BetaInv(prob, alpha, beta) = value
