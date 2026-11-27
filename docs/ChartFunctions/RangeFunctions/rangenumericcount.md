---
title: "RangeNumericCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangenumericcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeNumericCount Script and chart function

RangeNumericCount() finds the number of numeric values in an expression or field.

Syntax:

RangeNumericCount(first\_expr[, Expression])

Return data type:  integer

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

| Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeNumericCount (1,2,4) | Returns 3 |
| RangeNumericCount (5,'abc') | Returns 1 |
| RangeNumericCount (null( )) | Returns 0 |

Example with expression:

RangeNumericCount
(Above(MaxString(MyField),0,3))

Returns the number of numeric values in the
three results of the MaxString(MyField) function
evaluated
on the current row and two rows above the current row.

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeNumericCount(Above(MaxString(MyField),0,3)) |
| --- | --- |
| 10 | 1 |
| abc | 1 |
| 8 | 2 |
| def | 1 |
| xyz | 1 |
| 9 | 1 |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

10

'abc'

8

def

xyz

9

] ;

## Learn more

- [*NumericCount - chart function*](../CounterAggregationFunctions/numericcount.htm)
