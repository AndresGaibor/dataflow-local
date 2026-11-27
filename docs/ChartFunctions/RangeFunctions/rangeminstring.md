---
title: "RangeMinString Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangeminstring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMinString Script and chart function

RangeMinString() returns the first value in the text sort order that it finds in the expression or field.

Syntax:

RangeMinString(first\_expr[, Expression])

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
| RangeMinString (1,2,4) | Returns 1 |
| RangeMinString ('xyz','abc') | Returns 'abc' |
| RangeMinString (5,'abc') | Returns 5 |
| RangeMinString (null( )) | Returns NULL |

Example with expression:

RangeMinString
(Above(MinString(MyField),0,3))

Returns the first (in text sort order) of the
three results of the MinString(MyField) function
evaluated
on the current row and two rows above the current row.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeMinString(Above(MinString(MyField),0,3)) |
| --- | --- |
| 10 | 10 |
| abc | 10 |
| 8 | 8 |
| def | 8 |
| xyz | 8 |
| 9 | 9 |

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

- [*MinString - chart function*](../StringAggregationFunctions/minstring.htm)
