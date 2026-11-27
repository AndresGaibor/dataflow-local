---
title: "ZTestw_conf Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ztest/ztestw_conf.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Z-test functions"]
---

# ZTestw\_conf Script and chart function

ZTestw\_conf() returns the aggregated z confidence interval value for a series of values.

This function applies to z-tests where the input data series is given in weighted two-column format.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

ZTest\_conf(weight, value[, sigma[, sig]])

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| value | The sample values to be evaluated. A population mean of 0 is assumed. If you want the test to be performed around another mean, subtract that mean from the sample values. |
| weight | Each sample value in value can be counted one or more times according to a corresponding weight value in weight. |
| sigma | If known, the standard deviation can be stated in sigma. If sigma is omitted the actual sample standard deviation will be used. |
| sig | The two-tailed level of significance can be specified in sig. If omitted, sig is set to 0.025, resulting in a 95% confidence interval. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Example:

ZTestw\_conf( Weight, Value-TestValue)

## Learn more

- [*Examples of how to use z-test functions*](ztest-example.htm)
