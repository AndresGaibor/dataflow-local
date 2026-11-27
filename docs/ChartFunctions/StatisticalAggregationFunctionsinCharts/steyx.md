---
title: "STEYX - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/steyx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# STEYX - chart function

STEYX() returns the
aggregated standard error when predicting y-values for each x-value in a linear regression given by a series of coordinates represented by paired numbers in the expressions given by y\_value and x\_value.

Syntax:

STEYX([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] y\_value, x\_value)

Return data type:  numeric

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| y\_value | The expression or [field](#glossary-0 "Glossary term")containing the range of known y-values to be measured. |
| x\_value | The expression or field containing the range of known x-values to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

Examples and results:

Add the example script to your app and run it. Then build a straight table with KnownY and KnownX as [dimension](#glossary-2 "Glossary term") and Steyx(KnownY,KnownX) as [measure](#glossary-3 "Glossary term")

Totals should be enabled in the [properties](#glossary-4 "Glossary term") of the table.

| Example | Result |
| --- | --- |
| Trend:  LOAD \* inline [  Month|KnownY|KnownX  Jan|2|6  Feb|3|5  Mar|9|11  Apr|6|7  May|8|5  Jun|7|4  Jul|5|5  Aug|10|8  Sep|9|10  Oct|12|14  Nov|15|17  Dec|14|16  ] (delimiter is '|'); | The result of the STEYX(KnownY,KnownX) calculation is 2.071 (If number formatting is set to 3 decimal places.) |

## Learn more

- [*Avg - chart function*](avg.htm)
- [*Sterr - chart function*](sterr.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
