---
title: "RangeMissingCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangemissingcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMissingCount Script and chart function

RangeMissingCount() returns the number of non-numeric values (including NULL) in the expression or field.

Syntax:

RangeMissingCount(first\_expr[, Expression])

Return data type:  integer

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

| Argument | Description |
| --- | --- |
| first\_expr | The expression or [field](#glossary-0 "Glossary term") containing the data to be counted. |
| Expression | Optional expressions or fields containing the range of data to be counted. |

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeMissingCount (1,2,4) | Returns 0 |
| RangeMissingCount (5,'abc') | Returns 1 |
| RangeMissingCount (null( )) | Returns 1 |

Example with expression:

RangeMissingCount
(Above(MinString(MyField),0,3))

Returns the number of non-numeric values in the
three results of the MinString(MyField) function
evaluated
on the current row and two rows above the current row.

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeMissingCount(Above(MinString(MyField),0,3)) | Explanation |
| --- | --- | --- |
| 10 | 2 | Returns 2 because there are no rows above this row so 2 of the 3 values are missing. |
| abc | 2 | Returns 2 because there is only 1 row above the current row and the current row is non-numeric ('abc'). |
| 8 | 1 | Returns 1 because 1 of the 3 rows includes a non-numeric ('abc'). |
| def | 2 | Returns 2 because 2 of the 3 rows include non-numeric values ('def' and 'abc'). |
| xyz | 2 | Returns 2 because 2 of the 3 rows include non-numeric values (' xyz' and 'def'). |
| 9 | 2 | Returns 2 because 2 of the 3 rows include non-numeric values (' xyz' and 'def'). |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

10

'abc'

8

'def'

'xyz'

9

] ;

## Learn more

- [*MissingCount - chart function*](../CounterAggregationFunctions/missingcount.htm)
