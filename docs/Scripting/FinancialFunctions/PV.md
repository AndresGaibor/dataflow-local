---
title: "PV Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/PV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---
# PV Script and chart function

This function returns the present value of an investment.

PV(rate, nper, pmt
[ ,fv [ , type ] ])

Return data type:  numeric. By default, the result will be formatted as currency..

The present value is the total amount that a series of future payments
is worth right now. For example, when borrowing money, the loan amount
is the present value to the lender.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| rate | The interest rate per period. |
| nper | The total number of payment periods in an annuity. |
| pmt | The payment made each period. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20. |
| fv | The future value, or cash balance, you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0. |
| type | Should be 0 if payments are due at the end of the period and 1 if payments are due at the beginning of the period. If type is omitted, it is assumed to be 0. |

Examples and results:

Scripting example

| Example | Result |
| --- | --- |
| What is the present value of a debt, when you have to pay $100 at the end of each month during a five-year period, given an interest rate of 7%?  `PV(0.07/12,12*5,-100,0,0)` | Returns $5,050.20 |
