---
title: "Chi2Test_df Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/chi2-tests/chi2test_df.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions", "Chi2-test functions"]
---

# Chi2Test\_df Script and chart function

Chi2Test\_df() returns the aggregated chi2-test df value (degrees of freedom) for one
or two series of values.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Information noteAll Qlik Sense chi2 -test functions have the same arguments.

Syntax:

Chi2Test\_df(col, row, actual\_value[, expected\_value])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| col, row | The specified column and row in the matrix of values being tested. |
| actual\_value | The observed value of the data at the specified col and row. |
| expected\_value | The expected value for the distribution at the specified col and row. |

Limitations:

Text
values, NULL values and missing values in the expression value will result
in the function returning NULL.

Examples:

Chi2Test\_df(
Grp, Grade, Count )

Chi2Test\_df(
Gender, Description, Observed, Expected )

## Learn more

- [*Examples of how to use chi2-test functions in charts*](chi2test-example.htm)
- [*Examples of how to use chi2-test functions in the data load script*](../../../Scripting/StatisticalTestFunctions/chi2Tests/chi2test-script-example.htm)
