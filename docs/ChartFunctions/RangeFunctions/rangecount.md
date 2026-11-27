---
title: "RangeCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangecount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeCount Script and chart function

RangeCount() returns the number of values, both text and numeric, in the expression or field.

Syntax:

RangeCount(first\_expr[, Expression])

Return data type:  integer

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

| Argument | Description |
| --- | --- |
| first\_expr | The expression or [field](#glossary-0 "Glossary term") containing the data to be counted. |
| Expression | Optional expressions or fields containing the range of data to be counted. |

Limitations:

NULL values are not counted.

Examples and results:

Function examples

 | Examples | Results |
| --- | --- |
| RangeCount (1,2,4) | Returns 3 |
| RangeCount (2,'xyz') | Returns 2 |
| RangeCount (null( )) | Returns 0 |
| RangeCount (2,'xyz', null()) | Returns 2 |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab3:

LOAD recno() as RangeID, RangeCount(Field1,Field2,Field3) as MyRangeCount INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeCount for each of the records in the table.

Results table

| RangeID | MyRangeCount |
| --- | --- |
| 1 | 3 |
| 2 | 3 |
| 3 | 3 |
| 4 | 3 |
| 5 | 3 |
| 6 | 3 |

Example with expression:

RangeCount
(Above(MyField,1,3))

Returns the number of values contained in the three
results of MyField. By specifying the first argument of the Above() function as 1 and second argument as 3, it returns the values from the first three fields above the current row, where there are sufficient rows, which are taken as input to the RangeCount() function.

Data used in examples:

Sample data

| MyField | RangeCount(Above(MyField,1,3)) |
| --- | --- |
| 10 | 0 |
| 2 | 1 |
| 8 | 2 |
| 18 | 3 |
| 5 | 3 |
| 9 | 3 |

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

- [*Count - chart function*](../CounterAggregationFunctions/count.htm)
