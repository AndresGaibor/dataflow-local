---
title: "Kurtosis - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/kurtosis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Kurtosis - chart function

Kurtosis() finds the kurtosis of the range of data aggregated in the expression or field iterated over the chart dimensions.

Syntax:

Kurtosis([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] expr)

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

Examples and results:

Example table

| Type | Value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Comparison | 2 | 27 | 38 | 31 | 1 | 19 | 1 | 34 | 3 | 1 | 2 | 3 | 2 | 1 | 2 | 1 | 3 | 29 | 37 | 2 |
| Observation | 35 | 40 | 12 | 15 | 21 | 14 | 46 | 10 | 28 | 48 | 16 | 30 | 32 | 48 | 31 | 22 | 12 | 39 | 19 | 25 |

Function examples

| Example | Result |
| --- | --- |
| Kurtosis(Value) | For a table including the [dimension](#glossary-0 "Glossary term") `Type` and the [measure](#glossary-1 "Glossary term") Kurtosis(Value), if Totals are shown for the table, and number formatting is set to 3 significant figures, the result is 1.252. For Comparison it is 1.161 and for Observation it is 1.115. |
| Kurtosis(TOTAL Value)) | 1.252 for all values of Type, because the TOTAL qualifier means that dimensions are disregarded. |

Data used in examples:

```
Table1:
Crosstable (Type, Value)
Load recno() as ID, * inline [
Observation|Comparison
35|2
40|27
12|38
15|31
21|1
14|19
46|1
10|34
28|3
48|1
16|2
30|3
32|2
48|1
31|2
22|1
12|3
39|29
19|37
25|2 ] (delimiter is '|');
```

## Learn more

- [*Avg - chart function*](avg.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
