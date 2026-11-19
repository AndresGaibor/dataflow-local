---
title: "ChiDensity Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/ChiDensity.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Statistical distribution functions"]
---
# ChiDensity Script and chart function

`ChiDensity()` returns the one-tailed probability of the chi2 distribution. The chi2 density function is associated with a chi2 test.

Syntax:

ChiDensity(value, degrees\_freedom)

Return data type:  number

Arguments

| Argument | Description |
| --- | --- |
| `value` | The value at which you want to evaluate the distribution. The value must not be negative. |
| `degrees_freedom` | A positive integer stating the number of numerator degrees of freedom. |
