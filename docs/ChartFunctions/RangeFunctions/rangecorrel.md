---
title: "RangeCorrel Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangecorrel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeCorrel Script and chart function

RangeCorrel() returns the correlation coefficient for two sets of data. The correlation coefficient is a measure of the relationship between the data sets.

Syntax:

RangeCorrel(x\_value
, y\_value[, Expression])

Return data type:  numeric

Data series should be entered as (x,y) pairs. For example, to evaluate two series of data, array 1 and array 2, where the array 1 = 2,6,9 and array 2 = 3,8,4 you would write RangeCorrel
(2,3,6,8,9,4) which returns 0.269.

Arguments:

Arguments

 | Argument | Description |
| --- | --- |
| x-value, y-value | Each value represents a single value or a range of values as returned by an inter-record functions with a third optional parameter. Each value or range of values must correspond to an x-value or a range of y-values. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

The function needs at least
two pairs of coordinates to be calculated.

Text values, NULL values and missing values return NULL.

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeCorrel (2,3,6,8,9,4,8,5) | Returns 0.2492. This function can be loaded in the script or added into a [visualization](#glossary-0 "Glossary term") in the expression editor. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeList:

Load \* Inline [

ID1|x1|y1|x2|y2|x3|y3|x4|y4|x5|y5|x6|y6

01|46|60|70|13|78|20|45|65|78|12|78|22

02|65|56|22|79|12|56|45|24|32|78|55|15

03|77|68|34|91|24|68|57|36|44|90|67|27

04|57|36|44|90|67|27|57|68|47|90|80|94

] (delimiter is '|');

XY:

LOAD recno() as RangeID, \* Inline [

X|Y

2|3

6|8

9|4

8|5

](delimiter is '|');

In a table with ID1 as a [dimension](#glossary-1 "Glossary term") and the [measure](#glossary-2 "Glossary term")  RangeCorrel(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)), the RangeCorrel() function finds the value of Correl over the range of six x,y pairs, for each of the ID1 values.

Resulting table

| ID1 | MyRangeCorrel |
| --- | --- |
| 01 | -0.9517 |
| 02 | -0.5209 |
| 03 | -0.5209 |
| 04 | -0.1599 |

Example:

XY:

LOAD recno() as RangeID, \* Inline [

X|Y

2|3

6|8

9|4

8|5

](delimiter is '|');

In a table with RangeID as a dimension and the measure: RangeCorrel(Below(X,0,4,BelowY,0,4)), the RangeCorrel() function uses the results of the Below() functions, which because of the third argument (count) set to 4, produce a range of four x-y values from the loaded table XY.

Resulting table

| RangeID | MyRangeCorrel2 |
| --- | --- |
| 01 | 0.2492 |
| 02 | -0.9959 |
| 03 | -1.0000 |
| 04 | - |

The value for RangeID 01 is the same as manually entering RangeCorrel(2,3,6,8,9,4,8,5). For the other values of RangeID, the series produced by the Below() function are: (6,8,9,4,8,5), (9,4,8,5), and (8,5), the last of which produces a null result.

## Learn more

- [*Correl - chart function*](../StatisticalAggregationFunctionsinCharts/correl.htm)
