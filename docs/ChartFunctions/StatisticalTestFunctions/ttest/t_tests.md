---
title: "T-test functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ttest/t_tests.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions"]
---

# T-test functions

Expand/Collapse all

# T-test functions

T-test functions are used for statistical examination of two population means. A two-sample t-test examines whether two samples are different and is commonly used when two normal distributions have unknown variances and when an experiment uses a small sample size.

In the following sections, the t-test statistical test functions are grouped according to the sample student test that applies to each type of function.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

[*Creating a typical t-test report*](ttest_t_example.htm)

### Two independent samples t-tests

The following functions apply to two independent samples student's t-tests.

ttest\_conf

TTest\_conf returns the aggregated t-test confidence interval value for two independent samples.

[**ttest\_conf**](ttest_conf.htm) (
grp, value [, sig[, eq\_var]])

ttest\_df

TTest\_df() returns the aggregated student's t-test value (degrees of freedom)
for two independent series of values.

[**ttest\_df**](ttest_df.htm) (grp, value [, eq\_var)

ttest\_dif

TTest\_dif() is a numeric function that returns the aggregated student's t-test mean difference for two independent series of values.

[**ttest\_dif**](ttest_dif.htm) (grp, value)

ttest\_lower

TTest\_lower() returns the aggregated value for the lower end of the confidence interval
for two independent series of values.

[**ttest\_lower**](ttest_lower.htm) (grp, value [, sig[, eq\_var]])

ttest\_sig

TTest\_sig() returns the aggregated student's t-test 2-tailed level of significance for two independent series of values.

[**ttest\_sig**](ttest_sig.htm) (grp, value [, eq\_var])

ttest\_sterr

TTest\_sterr() returns the aggregated student's t-test standard error of the mean difference for two independent series of values.

[**ttest\_sterr**](ttest_sterr.htm) (grp, value [, eq\_var])

ttest\_t

TTest\_t() returns the aggregated t value for two independent series of values.

[**ttest\_t**](ttest_t.htm) (grp, value
[, eq\_var])

ttest\_upper

TTest\_upper() returns the aggregated value for the upper end of the confidence interval
for two independent series of values.

[**ttest\_upper**](ttest_upper.htm) (grp, value [, sig [, eq\_var]])

### Two independent weighted samples t-tests

The following functions apply to two independent samples student's t-tests where the input data series is given in weighted two-column format.

ttestw\_conf

TTestw\_conf() returns the aggregated t value for two independent series of values.

[**ttestw\_conf**](ttestw_conf.htm) (weight, grp, value [, sig[, eq\_var]])

ttestw\_df

TTestw\_df() returns the aggregated student's t-test df value (degrees of freedom) for two independent series of values.

[**ttestw\_df**](ttestw_df.htm) (weight, grp,
value [, eq\_var])

ttestw\_dif

TTestw\_dif() returns the aggregated student's t-test mean difference for two independent
series of values.

[**ttestw\_dif**](ttestw_dif.htm) (
weight, grp, value)

ttestw\_lower

TTestw\_lower() returns the aggregated value for the lower end of the confidence interval for two independent series of values.

[**ttestw\_lower**](ttestw_lower.htm) (weight, grp,
value [, sig[, eq\_var]])

ttestw\_sig

TTestw\_sig() returns the aggregated student's t-test 2-tailed level of significance
for two independent series of values.

[**ttestw\_sig**](ttestw_sig.htm) (
weight, grp, value [, eq\_var])

ttestw\_sterr

TTestw\_sterr() returns the aggregated student's t-test standard error of the mean difference
for two independent series of values.

[**ttestw\_sterr**](ttestw_sterr.htm) (weight, grp,
value [, eq\_var])

ttestw\_t

TTestw\_t() returns the aggregated t value for two independent series of values.

[**ttestw\_t**](ttestw_t.htm) (weight, grp,
value [, eq\_var])

ttestw\_upper

TTestw\_upper() returns the aggregated value for the upper end of the confidence interval
for two independent series of values.

[**ttestw\_upper**](ttestw_upper.htm) (weight, grp,
value [, sig [, eq\_var]])

### One sample t-tests

The following functions apply to one-sample student's t-tests.

ttest1\_conf

TTest1\_conf() returns the aggregated confidence interval value for a series of values.

[**ttest1\_conf**](ttest1_conf.htm) (value [,
sig])

ttest1\_df

TTest1\_df() returns the aggregated student's t-test df value (degrees of freedom)
for a series of values.

[**ttest1\_df**](ttest1_df.htm) (value)

ttest1\_dif

TTest1\_dif() returns the aggregated student's t-test mean difference for a series of values.

[**ttest1\_dif**](ttest1_dif.htm) (value)

ttest1\_lower

TTest1\_lower() returns the aggregated value for the lower end of the confidence interval for a series of values.

[**ttest1\_lower**](ttest1_lower.htm) (value [,
sig])

ttest1\_sig

TTest1\_sig() returns the aggregated student's t-test 2-tailed level of significance
for a series of values.

[**ttest1\_sig**](ttest1_sig.htm) (value)

ttest1\_sterr

TTest1\_sterr() returns the aggregated student's t-test standard error of the mean difference for a series of values.

[**ttest1\_sterr**](ttest1_sterr.htm) (value)

ttest1\_t

TTest1\_t() returns the aggregated t value for a series of values.

[**ttest1\_t**](ttest1_t.htm) (value)

ttest1\_upper

TTest1\_upper() returns the aggregated value for the upper end of the confidence interval for a series of values.

[**ttest1\_upper**](ttest1_upper.htm) (value [,
sig])

### One weighted sample t-tests

The following functions apply to one-sample student's t-tests where the input data series is given in weighted two-column format.

ttest1w\_conf

TTest1w\_conf() is a numeric function that returns the aggregated confidence interval value for a series of values.

[**ttest1w\_conf**](ttest1w_conf.htm) (weight, value [, sig])

ttest1w\_df

TTest1w\_df() returns the aggregated student's t-test df value (degrees of freedom)
for a series of values.

[**ttest1w\_df**](ttest1w_df.htm) (weight, value)

ttest1w\_dif

TTest1w\_dif() returns the aggregated student's t-test mean difference for a series of values.

[**ttest1w\_dif**](ttest1w_dif.htm) (weight, value)

ttest1w\_lower

TTest1w\_lower() returns the aggregated value for the lower end of the confidence interval for a series of values.

[**ttest1w\_lower**](ttest1w_lower.htm) (weight, value [, sig])

ttest1w\_sig

TTest1w\_sig() returns the aggregated student's t-test 2-tailed level of significance
for a series of values.

[**ttest1w\_sig**](ttest1w_sig.htm) (weight, value)

ttest1w\_sterr

TTest1w\_sterr() returns the aggregated student's t-test standard error of the mean difference for a series of values.

[**ttest1w\_sterr**](ttest1w_sterr.htm) (weight, value)

ttest1w\_t

TTest1w\_t() returns the aggregated t value for a series of values.

[**ttest1w\_t**](ttest1w_t.htm) (
weight, value)

ttest1w\_upper

TTest1w\_upper() returns the aggregated value for the upper end of the confidence interval
for a series of values.

[**ttest1w\_upper**](ttest1w_upper.htm) (weight, value [, sig])
