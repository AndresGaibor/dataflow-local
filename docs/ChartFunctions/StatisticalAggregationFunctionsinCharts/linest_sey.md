---
title: "LINEST_SEY - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_sey.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# LINEST\_SEY - chart function

LINEST\_SEY() returns the
aggregated standard error of the y estimate of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

Syntax:

LINEST\_SEY([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] y\_value, x\_value[, y0\_const[, x0\_const]])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| y\_value | The expression or field containing the range of y-values to be measured. |
| x\_value | The expression or field containing the range of x-values to be measured. |
| y0, x0 | An optional value y0 may be stated forcing the regression line to pass through the y-axis at a given point. By stating both y0 and x0 it is possible to force the regression line to pass through a single fixed coordinate. Information noteUnless both y0 and x0 are stated, the function requires at least two valid data-pairs to calculate. If y0 and x0 are stated, a single data pair will do. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

## Learn more

- [*Examples of how to use linest functions*](linest-example.htm)
- [*Avg - chart function*](avg.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
