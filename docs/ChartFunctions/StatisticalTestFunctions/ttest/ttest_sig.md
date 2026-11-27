---
title: "TTest_sig Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/ttest_sig.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "T-test functions"]
---

# TTest\_sig Script and chart function

TTest\_sig() returns the aggregated student's t-test 2-tailed level of significance for two independent series of values.

This function applies to independent samples student's t-tests.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

TTest\_sig (grp, value [, eq\_var])

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| value | The sample values to be evaluated. The sample values must be logically grouped as specified by exactly two values in group. If a field name for the sample values is not provided in the load script, the field will automatically be named Value. |
| grp | The field containing the names of each of the two sample groups. If a field name for the group is not provided in the load script, the field will automatically be given the name Type. |
| eq\_var | If eq\_var is specified as False (0), separate variances of the two samples will be assumed. If eq\_var is specified as True (1), equal variances between the samples will be assumed. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Examples:

TTest\_sig( Group, Value )

TTest\_sig( Group, Value, false )

## Learn more

- [*Creating a typical t-test report*](ttest_t_example.htm)
