---
title: "RangeSkew Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangeskew.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeSkew Script and chart function

RangeSkew() returns the value corresponding to the skewness of a range of numbers.

Syntax:

RangeSkew(first\_expr[, Expression])

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
| rangeskew (1,2,4) | Returns 0.93521952958283 |
| rangeskew (above(SalesValue,0,3)) | Returns a sliding skewness of the range of three values returned from the above() function calculated on the current row and the two rows above the current row. |

Data used in example:

Sample data

| CustID | RangeSkew(Above(SalesValue,0,3)) |
| --- | --- |
| 1-20 | -, -, 0.5676, 0.8455, 1.0127, -0.8741, 1.7243, -1.7186, 1.5518, 1.4332, 0,  1.1066, 1.3458, 1.5636, 1.5439, 0.6952, -0.3766 |

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

- [*Skew - chart function*](../StatisticalAggregationFunctionsinCharts/skew.htm)
