---
title: "RangeMin Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangemin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeMin Script and chart function

RangeMin() returns the lowest numeric values found within the expression or field.

Syntax:

RangeMin(first\_expr[, Expression])

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
| RangeMin (1,2,4) | Returns 1 |
| RangeMin (1,'xyz') | Returns 1 |
| RangeMin (null( ), 'abc') | Returns NULL |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, RangeMin(Field1,Field2,Field3) as MyRangeMin INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeMin for each of the records in the table.

Resulting table

| RangeID | MyRangeMin |
| --- | --- |
| 1 | 5 |
| 2 | 2 |
| 3 | 2 |
| 4 | 9 |
| 5 | 5 |
| 6 | 2 |

Example with expression:

RangeMin
(Above(MyField,0,3)

Returns the minimum value in
the range of three values of MyField
calculated on the current row and two rows above the current row. By specifying the third argument as 3, the Above() function returns three values, where there are sufficient rows above, which are taken as input to the RangeMin() function.

Data used in examples:

Sample data

| MyField | RangeMin(Above(MyField,0,3)) |
| --- | --- |
| 10 | 10 |
| 2 | 2 |
| 8 | 2 |
| 18 | 2 |
| 5 | 5 |
| 9 | 5 |

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

- [*Min - chart function*](../BasicAggregationFunctions/min.htm)
