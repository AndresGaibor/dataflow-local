---
title: "Avg - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/avg.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Avg - chart function

Avg() returns the aggregated average of the expression or field iterated over the chart dimensions.

Syntax:

Avg([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] expr)

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

| Customer | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Astrida | 46 | 60 | 70 | 13 | 78 | 20 | 45 | 65 | 78 | 12 | 78 | 22 |
| Betacab | 65 | 56 | 22 | 79 | 12 | 56 | 45 | 24 | 32 | 78 | 55 | 15 |
| Canutility | 77 | 68 | 34 | 91 | 24 | 68 | 57 | 36 | 44 | 90 | 67 | 27 |
| Divadip | 57 | 36 | 44 | 90 | 67 | 27 | 57 | 68 | 47 | 90 | 80 | 94 |

Function examples

| Example | Result |
| --- | --- |
| Avg(Sales) | For a table including the [dimension](#glossary-0 "Glossary term") `Customer` and the [measure](#glossary-1 "Glossary term") Avg([Sales]), if Totals are shown, the result is 2566. |
| Avg([TOTAL (Sales)) | 53.458333 for all values of Customer, because the TOTAL qualifier means that dimensions are disregarded. |
| Avg(DISTINCT (Sales)) | 51.862069 for the total, because using the Distinct qualifier means only unique values in Sales for each Customer are evaluated. |

Data used in examples:

```
Monthnames:
LOAD *, Dual(MonthText,MonthNumber) as Month INLINE [
MonthText, MonthNumber
Jan, 1
Feb, 2
Mar, 3
Apr, 4
May, 5
Jun, 6
Jul, 7
Aug, 8
Sep, 9
Oct, 10
Nov, 11
Dec, 12
];

Sales2013:
Crosstable (MonthText, Sales) LOAD * inline [
Customer|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec
Astrida|46|60|70|13|78|20|45|65|78|12|78|22
Betacab|65|56|22|79|12|56|45|24|32|78|55|15
Canutility|77|68|34|91|24|68|57|36|44|90|67|27
Divadip|57|36|44|90|67|27|57|68|47|90|80|94
] (delimiter is '|');
```

## Learn more

- [*Aggr - chart function*](../aggr.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
