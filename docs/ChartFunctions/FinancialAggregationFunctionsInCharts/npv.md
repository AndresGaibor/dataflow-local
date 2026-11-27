---
title: "NPV - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FinancialAggregationFunctionsInCharts/npv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---

# NPV - chart function

NPV() returns the aggregated net present value of an investment based on a discount\_rate per period and a series of future
payments (negative values) and incomes (positive values,) represented by the numbers in value, iterated over the chart dimensions. The payments and incomes are assumed to occur at the end of each period.

Syntax:

NPV([TOTAL [<fld {,fld}>]] discount\_rate, value)

Return data type:  numeric By default, the result will be formatted as currency.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | discount\_rate is the percentage rate of discount applied. |
| value | The expression or field containing the data to be measured. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm)  The TOTAL qualifier may be followed by a list of one or more field names within angle brackets. These field names should be a subset of the chart dimension variables. In this case, the calculation is made disregarding all chart dimension variables except those listed, that is, one value is returned for each combination of field values in the listed dimension fields. Also, fields that are not currently a dimension in a chart may be included in the list. This may be useful in the case of group dimensions, where the dimension fields are not fixed. Listing all of the variables in the group causes the function to work when the drill-down level changes. |

Limitations:

discount\_rate and value must not
contain [aggregation](#glossary-0 "Glossary term") functions, unless these inner aggregations contain
the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values are disregarded.

Examples and results:

Examples and results

| Example | Result |
| --- | --- |
| NPV(Discount, Payments) | -$540.12 |

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

- [*XNPV - chart function*](xnpv.htm)
- [*Aggr - chart function*](../aggr.htm)
