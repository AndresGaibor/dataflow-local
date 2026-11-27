---
title: "Sterr - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/sterr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Sterr - chart function

Sterr() finds the value of the standard error of the mean, (stdev/sqrt(n)), for the series of values aggregated in the expression iterated over the chart dimensions.

Syntax:

Sterr([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] expr)

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values are disregarded.

Examples and results:

Add the example script to your app and run it. Then build a straight table with Type as [dimension](#glossary-1 "Glossary term") and Sterr(Value) as [measure](#glossary-2 "Glossary term").

Totals should be enabled in the [properties](#glossary-3 "Glossary term") of the table.

| Example | Result |
| --- | --- |
| ``` Table1: Crosstable (Type, Value) Load recno() as ID, * inline [ Observation|Comparison 35|2 40|27 12|38 15|31 21|1 14|19 46|1 10|34 28|3 48|1 16|2 30|3 32|2 48|1 31|2 22|1 12|3 39|29 19|37 25|2 ] (delimiter is '|'); ``` | The results of the Sterr(Value) calculation are:   - Total is 2.4468583 - Comparison  is 3.2674431 - Observation is 2.7968733 |

## Learn more

- [*Avg - chart function*](avg.htm)
- [*STEYX - chart function*](steyx.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
