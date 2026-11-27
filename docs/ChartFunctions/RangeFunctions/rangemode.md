---
title: "RangeMode Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangemode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMode Script and chart function

RangeMode() finds the most commonly occurring value (mode value) in the expression or field.

Syntax:

RangeMode(first\_expr {, Expression})

Return data type:  numeric

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

 | Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

If more than one value shares the highest
frequency, NULL is returned.

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeMode (1,2,9,2,4) | Returns 2 |
| RangeMode ('a',4,'a',4) | Returns NULL |
| RangeMode (null( )) | Returns NULL |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, RangeMode(Field1,Field2,Field3) as MyRangeMode INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeMode for each of the records in the table.

Results table

| RangeID | MyRangMode |
| --- | --- |
| 1 | - |
| 2 | - |
| 3 | 8 |
| 4 | - |
| 5 | 5 |
| 6 | - |

Example with expression:

RangeMode (Above(MyField,0,3))

Returns the most commonly occurring value in the
three results of MyField
evaluated
on the current row and two rows above the current row. By specifying the third argument as 3, the Above() function returns three values, where there are sufficient rows above, which are taken as input to the RangeMode() function.

Data used in example:

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

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeMode(Above(MyField,0,3)) |
| --- | --- |
| 10 | Returns 10 because there are no rows above so the single value is the most commonly occurring. |
| 2 | - |
| 8 | - |
| 18 | - |
| 5 | - |
| 9 | - |

## Learn more

- [*Mode - chart function*](../BasicAggregationFunctions/mode.htm)
