---
title: "RangeFractile Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangefractile.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeFractile Script and chart function

RangeFractile() returns the value that corresponds to the n-th fractile (quantile) of a range of numbers.

Information note
RangeFractile() uses linear interpolation between closest ranks when calculating the fractile.

Syntax:

RangeFractile(fractile, first\_expr[, Expression])

Return data type:  numeric

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

Arguments

| Argument | Description |
| --- | --- |
| fractile | A number between 0 and 1 corresponding to the fractile (quantile expressed as a fraction) to be calculated. |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Examples and results:

Function examples

| Examples | Results |
| --- | --- |
| RangeFractile (0.24,1,2,4,6) | Returns 1.72 |
| RangeFractile(0.5,1,2,3,4,6) | Returns 3 |
| RangeFractile (0.5,1,2,5,6) | Returns 3.5 |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

RangeTab:

LOAD recno() as RangeID, RangeFractile(0.5,Field1,Field2,Field3) as MyRangeFrac INLINE [

Field1, Field2, Field3

10,5,6

2,3,7

8,2,8

18,11,9

5,5,9

9,4,2

];

The resulting table shows the returned values of MyRangeFrac for each of the records in the table.

Resulting table

| RangeID | MyRangeFrac |
| --- | --- |
| 1 | 6 |
| 2 | 3 |
| 3 | 8 |
| 4 | 11 |
| 5 | 5 |
| 6 | 4 |

Example with expression:

RangeFractile
(0.5, Above(Sum(MyField),0,3))

In this example, the inter-record function  Above() contains the optional offset and count arguments. This produces a range of results that can be used as input to the any of the range functions. In this case, Above(Sum(MyField),0,3) returns the values of MyField for the current row and the two rows above. These values provide the input to the RangeFractile() function. So, for the bottom row in the table below, this is the equivalent of RangeFractile(0.5, 3,4,6), that is, calculating the 0.5 fractile for the series 3, 4, and 6. The first two rows in the table below, the number of values in the range is reduced accordingly, where there no rows above the current row. Similar results are produced for other inter-record functions.

Sample data

| MyField | RangeFractile(0.5, Above(Sum(MyField),0,3)) |
| --- | --- |
| 1 | 1 |
| 2 | 1.5 |
| 3 | 2 |
| 4 | 3 |
| 5 | 4 |
| 6 | 5 |

Data used in examples:

RangeTab:

LOAD \* INLINE [

MyField

1

2

3

4

5

6

] ;

## Learn more

- [*Above - chart function*](../InterRecordFunctions/above.htm)
- [*Fractile - chart function*](../StatisticalAggregationFunctionsinCharts/fractile.htm)
