---
title: "RangeSum Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangesum.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeSum Script and chart function

RangeSum() returns the sum of a range of values. All non-numeric
values are treated as 0.

Syntax:

RangeSum(first\_expr[, Expression])

Return data type:  numeric

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

 | Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

The RangeSum function treats all non-numeric
values as 0.

Examples and results:

Examples

| Examples | Results |
| --- | --- |
| RangeSum (1,2,4) | Returns 7 |
| RangeSum (5,'abc') | Returns 5 |
| RangeSum (null( )) | Returns 0 |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, Rangesum(Field1,Field2,Field3) as MyRangeSum INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeSum for each of the records in the table.

Resulting table

| RangeID | MyRangeSum |
| --- | --- |
| 1 | 21 |
| 2 | 12 |
| 3 | 18 |
| 4 | 38 |
| 5 | 19 |
| 6 | 15 |

Example with expression:

RangeSum (Above(MyField,0,3))

Returns the sum of the
three values of MyField): from
the current row and two rows above the current row. By specifying the third argument as 3, the Above() function returns three values, where there are sufficient rows above, which are taken as input to the RangeSum() function.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeSum(Above(MyField,0,3)) |
| --- | --- |
| 10 | 10 |
| 2 | 12 |
| 8 | 20 |
| 18 | 28 |
| 5 | 31 |
| 9 | 32 |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

10

2

8

18

5

9

] ;

## Learn more

- [*Sum - chart function*](../BasicAggregationFunctions/sum.htm)
- [*Above - chart function*](../InterRecordFunctions/above.htm)
