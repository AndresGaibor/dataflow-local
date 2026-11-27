---
title: "LINEST_R2 Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_r2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# LINEST\_R2 Script function

LINEST\_R2() returns
the aggregated r2
value (coefficient of determination) of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by clause.

Syntax:

LINEST\_R2 (y\_value, x\_value[, y0 [, x0 ]])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| y\_value | The expression or field containing the range of y-values to be measured. |
| x\_value | The expression or field containing the range of x-values to be measured. |
| y(0), x(0) | An optional value y0 may be stated forcing the regression line to pass through the y-axis at a given point. By stating both y0 and x0 it is possible to force the regression line to pass through a single fixed coordinate.  Unless both y0 and x0 are stated, the function requires at least two valid data-pairs to calculate. If y0 and x0 are stated, a single data pair will do. |

Limitations:

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

## Learn more

- [*Examples of how to use linest functions*](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest-example.htm)
