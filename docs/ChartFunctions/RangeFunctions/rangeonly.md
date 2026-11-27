---
title: "RangeOnly Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/rangeonly.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeOnly Script and chart function

RangeOnly() is a dual function that returns a value if the expression evaluates to one unique value. If this is not the case then NULL is returned.

Syntax:

RangeOnly(first\_expr[, Expression])

Return data type:  dual

Arguments:

The arguments of this function may contain inter-record functions which in themselves return a list of values.

| Argument | Description |
| --- | --- |
| first\_expr | The expression or field containing the data to be measured. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Examples and results:

| Examples | Results |
| --- | --- |
| RangeOnly (1,2,4) | Returns NULL |
| RangeOnly (5,'abc') | Returns NULL |
| RangeOnly (null( ), 'abc') | Returns 'abc' |
| RangeOnly(10,10,10) | Returns 10 |

## Learn more

- [*Only - chart function*](../BasicAggregationFunctions/only.htm)
