---
title: "Z-test functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalTestFunctions/ztest/z_tests.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical test functions"]
---

# Z-test functions

Expand/Collapse all

# Z-test functions

A statistical examination of two population means. A two sample z-test examines whether two samples are different and is commonly used when two normal distributions have known variances and when an experiment uses a large sample size.

The z-test statistical test functions are grouped according the type of input data series that applies to the function.

If the function is used in the data load script, the values are iterated over a number of records as defined by a group by clause.

If the function is used in a chart expression, the values are iterated over the chart dimensions.

[*Examples of how to use z-test functions*](ztest-example.htm)

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

### One column format functions

The following functions apply to z-tests with simple input data series.

ztest\_conf

ZTest\_conf() returns the aggregated z value for a series of values.

[**ztest\_conf**](ztest_conf.htm) (value [, sigma [, sig ])

ztest\_dif

ZTest\_dif() returns the aggregated z-test mean difference for a series of values.

[**ztest\_dif**](ztest_dif.htm) (value [, sigma])

ztest\_sig

ZTest\_sig() returns the aggregated z-test 2-tailed level of significance for a series of values.

[**ztest\_sig**](ztest_sig.htm) (value [, sigma])

ztest\_sterr

ZTest\_sterr() returns the aggregated z-test standard error of the mean difference for a series of values.

[**ztest\_sterr**](ztest_sterr.htm) (value [, sigma])

ztest\_z

ZTest\_z() returns the aggregated z value for a series of values.

[**ztest\_z**](ztest_z.htm) (value [, sigma])

ztest\_lower

ZTest\_lower() returns the aggregated value for the lower end of the confidence interval
for two independent series of values.

[**ztest\_lower**](ztest_lower.htm) (grp, value [, sig [, eq\_var]])

ztest\_upper

ZTest\_upper() returns the aggregated value for the upper end of the confidence interval
for two independent series of values.

[**ztest\_upper**](ztest_upper.htm) (grp, value [, sig [, eq\_var]])

### Weighted two-column format functions

The following functions apply to z-tests where the input data series is given in weighted two-column format.

ztestw\_conf

ZTestw\_conf() returns the aggregated z confidence interval value for a series of values.

[**ztestw\_conf**](ztestw_conf.htm) (weight, value [, sigma [, sig]])

ztestw\_dif

ZTestw\_dif() returns the aggregated z-test mean difference for a series of values.

[**ztestw\_dif**](ztestw_dif.htm) (weight, value [, sigma])

ztestw\_lower

ZTestw\_lower() returns the aggregated value for the lower end of the confidence interval
for two independent series of values.

[**ztestw\_lower**](ztestw_lower.htm) (weight, value [, sigma])

ztestw\_sig

ZTestw\_sig() returns the aggregated z-test 2-tailed level of significance for a series of values.

[**ztestw\_sig**](ztestw_sig.htm) (weight, value [, sigma])

ztestw\_sterr

ZTestw\_sterr() returns the aggregated z-test standard error of the mean difference for a series of values.

[**ztestw\_sterr**](ztestw_sterr.htm) (weight, value [, sigma])

ztestw\_upper

ZTestw\_upper() returns the aggregated value for the upper end of the confidence interval
for two independent series of values.

[**ztestw\_upper**](ztestw_upper.htm) (weight, value [, sigma])

ztestw\_z

ZTestw\_z() returns the aggregated z value for a series of values.

[**ztestw\_z**](ztestw_z.htm) (weight, value [, sigma])
