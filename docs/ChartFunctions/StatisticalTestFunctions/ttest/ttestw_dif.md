---
title: "TTestw_dif Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/ttestw_dif.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "T-test functions"]
---

# TTestw\_dif Script and chart function

TTestw\_dif() returns the aggregated student's t-test mean difference for two independent
series of values.

This function applies to two independent samples student's t-tests where the input data series is given in weighted two-column format.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

TTestw\_dif (weight, grp, value)

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| weight | Each value in value can be counted one or more times according to a corresponding weight value in weight. |
| grp | The field containing the names of each of the two sample groups. If a field name for the group is not provided in the load script, the field will automatically be given the name Type. |
| value | The sample values to be evaluated. The sample values must be logically grouped as specified by exactly two values in group. If a field name for the sample values is not provided in the load script, the field will automatically be named Value. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Examples:

TTestw\_dif( Weight, Group, Value )

TTestw\_dif( Weight, Group, Value, false )

## Learn more

- [*Creating a typical t-test report*](ttest_t_example.htm)
