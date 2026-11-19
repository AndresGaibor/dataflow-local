---
title: "IRR Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/IRR.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---
# IRR Script function

IRR() returns the aggregated internal
rate of return for a series of cash flows represented by the numbers in the
expression iterated over a number of records as defined by a group by
clause.

These cash flows do not have to be even, as they would be for
an annuity. However, the cash flows must occur at regular intervals, such
as monthly or annually. The internal rate of return is the interest rate
received for an investment consisting of payments (negative values) and
income (positive values) that occur at regular periods. The function needs
at least one positive and one negative value to calculate.

This function uses a simplified version of the Newton method for calculating the internal rate of return (IRR).

Syntax:

IRR(value)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value | The expression or field containing the data to be measured. |

Limitations:

Text values, NULL values and missing values are disregarded.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Examples and results:

Examples and results

| Example | Year | IRR2013 |
| --- | --- | --- |
| Cashflow:  LOAD 2013 as Year, \* inline [  Date|Discount|Payments  2013-01-01|0.1|-10000  2013-03-01|0.1|3000  2013-10-30|0.1|4200  2014-02-01|0.2|6800  ] (delimiter is '|');    Cashflow1:  LOAD Year,IRR(Payments) as IRR2013 Resident Cashflow Group By Year; | 2013 | 0.1634 |
