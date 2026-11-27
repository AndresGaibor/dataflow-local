---
title: "RangeStdev Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangestdev.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeStdev Script and chart function

RangeStdev() finds the standard deviation of a range of numbers.

Syntax:

RangeStdev(first\_expr[, Expression])

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

Function examples

| Examples | Results |
| --- | --- |
| RangeStdev (1,2,4) | Returns 1.5275252316519 |
| RangeStdev (null( )) | Returns NULL |
| RangeStdev (above(SalesValue),0,3)) | Returns a sliding standard of the range of three values returned from the above() function calculated on the current row and the two rows above the current row. |

Data used in example:

Sample data

| CustID | RangeStdev(SalesValue, 0,3)) |
| --- | --- |
| 1-20 | -,43.841, 34.192, 18.771, 20.953, 41.138, 47.655, 36.116, 32.716, 25.325,  38,000, 27.737, 35.553, 33.650, 42.532, 33.858, 32.146, 25.239, 35.595 |

SalesTable:

LOAD recno() as CustID, \* inline [

SalesValue

101

163

126

139

167

86

83

22

32

70

108

124

176

113

95

32

42

92

61

21

] ;

## Learn more

- [*Stdev - chart function*](../StatisticalAggregationFunctionsinCharts/stdev.htm)
