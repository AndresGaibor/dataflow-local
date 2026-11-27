---
title: "TTest1_lower Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/ttest1_lower.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "T-test functions"]
---

# TTest1\_lower Script and chart function

TTest1\_lower() returns the aggregated value for the lower end of the confidence interval for a series of values.

This function applies to one-sample student's t-tests.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

TTest1\_lower (value [,
sig])

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| value | The samples to be evaluated. If a field name for the sample values is not provided in the load script, the field will automatically be named Value. |
| sig | The two-tailed level of significance can be specified in sig. If omitted, sig is set to 0.025, resulting in a 95% confidence interval. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Examples:

TTest1\_lower( Value )

TTest1\_lower( Value, 0.005 )

## Learn more

- [*Creating a typical t-test report*](ttest_t_example.htm)
