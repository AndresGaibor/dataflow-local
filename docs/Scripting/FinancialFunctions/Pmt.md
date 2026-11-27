---
title: "Pmt Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/Pmt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---

# Pmt Script and chart function

This function returns the payment for a loan based on periodic, constant payments
and a constant interest rate. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20.

Pmt(rate, nper,
pv [ ,fv [ , type ] ] )

Return data type:  numeric. By default, the result will be formatted as currency..

To find the total amount paid over the duration of the loan, multiply
the returned pmt value by nper.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| rate | The interest rate per period. |
| nper | The total number of payment periods in an annuity. |
| pv | The present value, or lump-sum amount, that a series of future payments is worth right now. If pv is omitted, it is assumed to be 0 (zero). |
| fv | The future value, or cash balance, you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0. |
| type | Should be 0 if payments are due at the end of the period and 1 if payments are due at the beginning of the period. If type is omitted, it is assumed to be 0. |

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| The following formula returns the monthly payment on a $20,000 loan at an annual rate of 10 percent, that must be paid off in 8 months:  Pmt(0.1/12,8,20000) | Returns -$2,594.66 |
| For the same loan, if payment is due at the beginning of the period, the payment is:  Pmt(0.1/12,8,20000,0,1) | Returns -$2,573.21 |
