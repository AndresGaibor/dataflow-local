---
title: "Chi2-test functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/chi2-tests/chi2_tests.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions"]
---

# Chi2-test functions

Expand/Collapse all

# Chi2-test functions

Generally used in the study of qualitative variables. One can compare observed frequencies in a one-way frequency table with expected frequencies, or study the connection between two variables in a contingency table.Chi-squared test functions are used to determine whether there is a statistically significant difference between the expected frequencies and the observed frequencies in one or more groups. Often a histogram is used, and the different bins are compared to an expected distribution.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

Chi2Test\_chi2

Chi2Test\_chi2() returns the aggregated chi2-test value for one or two series of values.

[**chi2test\_chi2**](chi2test_chi2.htm)(col, row, actual\_value[, expected\_value])

Chi2Test\_df

Chi2Test\_df() returns the aggregated chi2-test df value (degrees of freedom) for one
or two series of values.

[**chi2test\_df**](chi2test_df.htm)(col, row, actual\_value[, expected\_value])

Chi2Test\_p

Chi2Test\_p() returns the aggregated chi2-test p value (significance) for one or two series of values.

[**chi2test\_p**](chi2test_p.htm)(col, row, actual\_value[, expected\_value])

## Learn more

- [*T-test functions*](../ttest/t_tests.htm)
- [*Z-test functions*](../ztest/z_tests.htm)
