---
title: "BinomDist Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/BinomDist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# BinomDist Script and chart function

BinomDist() returns the accumulated probability of the Binomial distribution.

Syntax:

BinomDist(value, trials, trial\_probability)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must be an integer not smaller than zero and not greater than the number of trials. |
| trials | A positive integer that states the number of trials. |
| trial\_probability | The success probability for each trial. It is always a number between 0 and 1. |

This function is related
to the BinomInv function in the following way:
If prob = BinomDIST(value, trials, trial\_probability), then BinomInv(prob, trials, trial\_probability) = value
