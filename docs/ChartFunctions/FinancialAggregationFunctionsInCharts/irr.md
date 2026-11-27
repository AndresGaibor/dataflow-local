---
title: "IRR - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FinancialAggregationFunctionsInCharts/irr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---

# IRR - chart function

IRR() returns the aggregated internal
rate of return for a series of cash flows represented by the numbers in the expression given by value iterated over the chart dimensions.

These cash flows do not have to be even, as they would be for an annuity. However, the cash flows
must occur at regular intervals, such as monthly or annually. The internal rate of return is the interest rate received for an investment consisting of payments (negative values) and income (positive values) that occur at regular periods. The function needs at least one positive and one negative
value to calculate.

This function uses a simplified version of the Newton method for calculating the internal rate of return (IRR).

Syntax:

IRR([TOTAL [<fld {,fld}>]] value)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The expression or field containing the data to be measured. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values are disregarded.

Examples and results:

Examples and results

| Example | Result |
| --- | --- |
| IRR(Payments) | 0.1634  The payments are assumed to be periodic in nature, for example monthly.  Information noteThe Date [field](#glossary-0 "Glossary term") is used in the XIRR example where payments can be non-periodical as long as you provide the dates on which payments were made. |

Data used in examples:

Cashflow:

LOAD 2013 as Year, \* inline [

Date|Discount|Payments

2013-01-01|0.1|-10000

2013-03-01|0.1|3000

2013-10-30|0.1|4200

2014-02-01|0.2|6800

] (delimiter is '|');

## Learn more

- [*XIRR - chart function*](xirr.htm)
- [*Aggr - chart function*](../aggr.htm)
