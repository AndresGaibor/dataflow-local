---
title: "TTest1w_t Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/ttest1w_t.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "T-test functions"]
---

# TTest1w\_t Script and chart function

TTest1w\_t() returns the aggregated t value for a series of values.

This function applies to one-sample student's t-tests where the input data series is given in weighted two-column format.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Syntax:

TTest1w\_t (
weight, value)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The samples to be evaluated. If a field name for the sample values is not provided in the load script, the field will automatically be named Value. |
| weight | Each value in value can be counted one or more times according to a corresponding weight value in weight. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Example:

TTest1w\_t( Weight, Value )

## Learn more

- [*Creating a typical t-test report*](ttest_t_example.htm)
