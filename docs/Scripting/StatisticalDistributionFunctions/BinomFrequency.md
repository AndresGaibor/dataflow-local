---
title: "BinomFrequency Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/BinomFrequency.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# BinomFrequency Script and chart function

`BinomFrequency()` returns the Binomial probability distribution.

Syntax:

BinomFrequency(value, trials, trial\_probability)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| `value` | The value at which you want to evaluate the distribution. The value must be an integer not smaller than zero and not greater than the number of trials. |
| `trials` | A positive integer that states the number of trials |
| `trial_probability` | The success probability for each trial. It is always a number between 0 and 1. |
