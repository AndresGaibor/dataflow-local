---
title: "RangeTextCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangetextcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeTextCount Script and chart function

RangeTextCount() returns the number of text values in an expression or field.

Syntax:

RangeTextCount(first\_expr[, Expression])

Return data type:  integer

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Argument

 | Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Examples and results:

Function examples

 | Examples | Results |
| --- | --- |
| RangeTextCount (1,2,4) | Returns 0 |
| RangeTextCount (5,'abc') | Returns 1 |
| RangeTextCount (null( )) | Returns 0 |

Example with expression:

RangeTextCount
(Above(MaxString(MyField),0,3))

Returns the number of text values within the
three results of the MaxString(MyField) function
evaluated over the current row and two rows above the current row.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Example data

| MyField | MaxString(MyField) | RangeTextCount(Above(Sum(MyField),0,3)) |
| --- | --- | --- |
| 10 | 10 | 0 |
| abc | abc | 1 |
| 8 | 8 | 1 |
| def | def | 2 |
| xyz | xyz | 2 |
| 9 | 9 | 2 |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

10

'abc'

8

null()

'xyz'

9

] ;

## Learn more

- [*TextCount - chart function*](../CounterAggregationFunctions/textcount.htm)
