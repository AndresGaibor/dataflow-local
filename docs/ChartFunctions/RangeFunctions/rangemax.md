---
title: "RangeMax Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangemax.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMax Script and chart function

RangeMax() returns the highest numeric values found within the expression or field.

Syntax:

RangeMax(first\_expr[, Expression])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

If no numeric
value is found, NULL is returned.

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeMax (1,2,4) | Returns 4 |
| RangeMax (1,'xyz') | Returns 1 |
| RangeMax (null( ), 'abc') | Returns NULL |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, RangeMax(Field1,Field2,Field3) as MyRangeMax INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeMax for each of the records in the table.

Resulting table

| RangeID | MyRangeMax |
| --- | --- |
| 1 | 10 |
| 2 | 7 |
| 3 | 8 |
| 4 | 18 |
| 5 | 9 |
| 6 | 9 |

Example with expression:

RangeMax
(Above(MyField,0,3))

Returns the maximum value in
the range of three values of MyField
calculated on the current row and two rows above the current row. By specifying the third argument as 3, the Above() function returns three values, where there are sufficient rows above, which are taken as input to the RangeMax() function.

Data used in examples:

Tip noteDisable sorting of MyField to ensure that the example works as expected.

Sample data

| MyField | RangeMax (Above(Sum(MyField),1,3)) |
| --- | --- |
| 10 | 10 |
| 2 | 10 |
| 8 | 10 |
| 18 | 18 |
| 5 | 18 |
| 9 | 18 |

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
