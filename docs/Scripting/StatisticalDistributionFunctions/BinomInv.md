---
title: "BinomInv Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/BinomInv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# BinomInv Script and chart function

BinomInv() returns the inverse of the accumulated probability of the Binomial distribution.

Syntax:

BinomInv(prob, trials, trial\_probability)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| prob | A probability associated with the Binomial-probability distribution. It must be a number between 0 and 1. |
| trials | A positive integer that states the number of trials. |
| trial\_probability | The success probability for each trial. It is always a number between 0 and 1. |

This function is related
to the BinomDist function in the following way:
If prob = BinomDist(value, trials, trial\_probability), then BinomInv(prob, trials, trial\_probability) = value
