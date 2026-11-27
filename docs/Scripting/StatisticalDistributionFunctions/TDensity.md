---
title: "TDensity Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/TDensity.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---

# TDensity Script and chart function

TDensity() returns the value for the student's t density function where a numeric value is a calculated value of t for which the probability is to be computed.

Syntax:

TDensity(value, degrees\_freedom)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| value | The value at which you want to evaluate the distribution. The value must not be negative. |
| degrees\_freedom | A positive integer stating the number of degrees of freedom. |
