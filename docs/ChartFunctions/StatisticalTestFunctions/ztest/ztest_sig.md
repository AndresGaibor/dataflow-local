---
title: "ZTest_sig Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ztest/ztest_sig.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Z-test functions"]
---

# ZTest\_sig Script and chart function

ZTest\_sig() returns the aggregated z-test 2-tailed level of significance for a series of values.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

ZTest\_sig(value[, sigma])

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| value | The sample values to be evaluated. A population mean of 0 is assumed. If you want the test to be performed around another mean, subtract that mean from the sample values. |
| sigma | If known, the standard deviation can be stated in sigma. If sigma is omitted the actual sample standard deviation will be used. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Example:

ZTest\_sig(Value-TestValue)

## Learn more

- [*Examples of how to use z-test functions*](ztest-example.htm)
