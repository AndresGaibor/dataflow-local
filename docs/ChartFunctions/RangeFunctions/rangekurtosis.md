---
title: "RangeKurtosis Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangekurtosis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeKurtosis Script and chart function

RangeKurtosis() returns the value that corresponds to the kurtosis of a range of numbers.

Syntax:

RangeKurtosis(first\_expr[, Expression])

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
| RangeKurtosis (1,2,4,7) | Returns -0.28571428571429 |

## Learn more

- [*Kurtosis - chart function*](../StatisticalAggregationFunctionsinCharts/kurtosis.htm)
