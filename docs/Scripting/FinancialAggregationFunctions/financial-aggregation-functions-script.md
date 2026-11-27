---
title: "Financial aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/financial-aggregation-functions-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---

# Financial aggregation functions

Expand/Collapse all

# Financial aggregation functions

This section describes [aggregation](#glossary-0 "Glossary term") functions for financial operations regarding payments and cash flow.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Financial aggregation functions in the data load script

IRR

IRR() returns the aggregated internal
rate of return for a series of cash flows represented by the numbers in the
expression iterated over a number of records as defined by a group by
clause.

[**IRR**](IRR.htm)(expression)

XIRR

XIRR() returns the aggregated internal
rate of return (yearly) for a schedule of cash flows (that is not necessarily periodic)
represented by paired numbers in pmt and date iterated
over a number of records as defined by a group by clause. All payments are discounted based on a 365-day year.

[**XIRR**](XIRR.htm)(valueexpression,
dateexpression )

NPV

The NPV() script function takes a discount rate and multiple values ordered by period. Inflows (incomes) are positive, and outflows (future payments) are assumed to be negative values for these calculations. These occur at the end of each period.

[**NPV**](NPV.htm)(rate, expression)

XNPV

XNPV() returns the aggregated net present
value for a schedule of cashflows (not necessarily periodic) represented
by paired numbers in pmt and date. All payments are discounted based on a 365-day year.

[**XNPV**](XNPV.htm)(rate, valueexpression,
dateexpression)

## Financial aggregation functions in chart expressions

These financial aggregation functions can be used in [charts](#glossary-1 "Glossary term")

IRR

IRR() returns the aggregated internal
rate of return for a series of cash flows represented by the numbers in the expression given by value iterated over the chart dimensions.

[**irr**](../../ChartFunctions/FinancialAggregationFunctionsInCharts/irr.htm)[TOTAL [<fld {,fld}>]] value)

NPV

NPV() returns the aggregated net present value of an investment based on a discount\_rate per period and a series of future
payments (negative values) and incomes (positive values,) represented by the numbers in value, iterated over the chart dimensions. The payments and incomes are assumed to occur at the end of each period.

[**npv**](../../ChartFunctions/FinancialAggregationFunctionsInCharts/npv.htm)([TOTAL [<fld {,fld}>]] discount\_rate, value)

XIRR

XIRR() returns the aggregated internal
rate of return (yearly) for a schedule of cash flows (that is not necessarily periodic) represented by paired numbers in the expressions given by pmt and date iterated
over the chart dimensions. All payments are discounted based on a 365-day year.

[**xirr**](../../ChartFunctions/FinancialAggregationFunctionsInCharts/xirr.htm)([TOTAL [<fld {,fld}>]] pmt, date)

XNPV

XNPV() returns the aggregated net present
value for a schedule of cash flows (not necessarily periodic) represented
by paired numbers in the expressions given by pmt
and date, iterated over
the chart dimensions. All payments are discounted based on a 365-day year.

[**xnpv**](../../ChartFunctions/FinancialAggregationFunctionsInCharts/xnpv.htm)([TOTAL [<fld{,fld}>]] discount\_rate, pmt, date)
