---
title: "RangeNullCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangenullcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeNullCount Script and chart function

RangeNullCount() finds the number of NULL values in the expression or field.

Syntax:

RangeNullCount(first\_expr [, Expression])

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
| RangeNullCount (1,2,4) | Returns 0 |
| RangeNullCount (5,'abc') | Returns 0 |
| RangeNullCount (null( ), null( )) | Returns 2 |

Example with expression:

RangeNullCount
(Above(Sum(MyField),0,3))

Returns the number of NULL values in the
three results of the Sum(MyField) function
evaluated
on the current row and two rows above the current row.

Information noteCopying MyField in example below will not result in NULL value.

Sample data

| MyField | RangeNullCount(Above(Sum(MyField),0,3)) |
| --- | --- |
| 10 | Returns 2 because there are no rows above this row so 2 of the 3 values are missing (=NULL). |
| 'abc' | Returns 1 because there is only one row above the current row, so one of the three values is missing (=NULL). |
| 8 | Returns 0 because none of the three rows is a NULL value. |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

10

'abc'

8

] ;

## Learn more

- [*NullCount - chart function*](../CounterAggregationFunctions/nullcount.htm)
