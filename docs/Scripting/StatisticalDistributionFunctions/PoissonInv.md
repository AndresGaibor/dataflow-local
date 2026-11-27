---
title: "PoissonInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/PoissonInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# PoissonInv Script and chart function

PoissonInv() returns the inverse of the accumulated probability of the Poisson distribution.

Syntax:

PoissonInv(prob, mean)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the Poisson-probability distribution. It must be a number between 0 and 1. |
| mean | A positive number defining the average outcome. |

This function is related
to the PoissonDIST function in the following way:
If prob = PoissonDist(value, mean), then PoissonInv(prob, mean) = value
