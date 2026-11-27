---
title: "Median - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/median.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Median - chart function

Median() returns the median value of the range of values aggregated in the expression iterated over the chart dimensions.

Syntax:

Median([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] expr)

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

## Example: Chart expression using Median

Example - chart expression

### Load script

Load the following data as an inline load in the data load editor to create the chart expression example below.

```
Load RecNo() as RowNo, Letter, Number Inline
[Letter, Number
A,1
A,3
A,4
A,9
B,2
B,8
B,9];
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

### Create a visualization

Create a table [visualization](#glossary-0 "Glossary term") in a Qlik Sense [sheet](#glossary-1 "Glossary term") with Letter as a [dimension](#glossary-2 "Glossary term").

### Chart expression

Add the following expression to the table, as a [measure](#glossary-3 "Glossary term"):

Median(Number)

### Result

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Median.png)

### Explanation

The median is considered the "middle" number when the numbers have been sorted in order from smallest to greatest. If the data set has an even number of values, the function returns the average of the two middle values.
In this example, the median is calculated for each set of values of A and B, which is 3.5 and 8, respectively.

The median for Totals is calculated from all values, which equals 4.

## Learn more

- [*Avg - chart function*](avg.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
