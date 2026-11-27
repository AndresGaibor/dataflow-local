---
title: "RangeMaxString Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangemaxstring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMaxString Script and chart function

RangeMaxString() returns the last value in the text sort order that it finds in the expression or field.

Syntax:

RangeMaxString(first\_expr[, Expression])

Return data type:  string

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
| RangeMaxString (1,2,4) | Returns 4 |
| RangeMaxString ('xyz','abc') | Returns 'xyz' |
| RangeMaxString (5,'abc') | Returns 'abc' |
| RangeMaxString (null( )) | Returns NULL |

Example with expression:

RangeMaxString
(Above(MaxString(MyField),0,3))

Returns the last (in text sort order) of the
three results of the MaxString(MyField) function
evaluated
on the current row and two rows above the current row.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeMaxString(Above(MaxString(MyField),0,3)) |
| --- | --- |
| 10 | 10 |
| abc | abc |
| 8 | abc |
| def | def |
| xyz | xyz |
| 9 | xyz |

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

- [*MaxString - chart function*](../StringAggregationFunctions/maxstring.htm)
