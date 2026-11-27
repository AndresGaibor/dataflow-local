---
title: "RangeAvg Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangeavg.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeAvg Script and chart function

RangeAvg() returns the average of a range. Input to the function can be either a range of values or an expression.

Syntax:

RangeAvg(first\_expr[, Expression])

Return data type:  numeric

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

| Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

If no numeric
value is found, NULL is returned.

Examples and results:

Scripting examples

| Examples | Results |
| --- | --- |
| RangeAvg (1,2,4) | Returns 2.33333333 |
| RangeAvg (1,'xyz') | Returns 1 |
| RangeAvg (null( ), 'abc') | Returns NULL |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, RangeAvg(Field1,Field2,Field3) as MyRangeAvg INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeAvg for each of the records in the table.

Resulting table

| RangeID | MyRangeAvg |
| --- | --- |
| 1 | 7 |
| 2 | 4 |
| 3 | 6 |
| 4 | 12.666 |
| 5 | 6.333 |
| 6 | 5 |

Example with expression:

RangeAvg (Above(MyField),0,3))

Returns a sliding average of the result of
the range of three values of MyField
calculated on the current row and two rows above the current row. By specifying the third argument as 3, the Above() function returns three values, where there are sufficient rows above, which are taken as input to the RangeAvg() function.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeAvg (Above(MyField,0,3)) | Comments |
| --- | --- | --- |
| 10 | 10 | Because this is the top row, the range consists of one value only. |
| 2 | 6 | There is only one row above this row, so the range is: 10,2. |
| 8 | 6.6666666667 | The equivalent to RangeAvg(10,2,8) |
| 18 | 9.333333333 | - |
| 5 | 10. 333333333 | - |
| 9 | 10.6666666667 | - |

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

- [*Avg - chart function*](../StatisticalAggregationFunctionsinCharts/avg.htm)
- [*Count - chart function*](../CounterAggregationFunctions/count.htm)
