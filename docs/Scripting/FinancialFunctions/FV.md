---
title: "FV Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/FV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---
# FV Script and chart function

This function returns the future value of an investment based on periodic, constant
payments and a simple annual interest.

Syntax:

FV(rate, nper, pmt
[ ,pv [ , type ] ])

Return data type:  numeric. By default, the result will be formatted as currency..

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| rate | The interest rate per period. |
| nper | The total number of payment periods in an annuity. |
| pmt | The payment made each period. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20. |
| pv | The present value, or lump-sum amount, that a series of future payments is worth right now. If pv is omitted, it is assumed to be 0 (zero). |
| type | Should be 0 if payments are due at the end of the period and 1 if payments are due at the beginning of the period. If type is omitted, it is assumed to be 0. |

Examples and results:

Scripting example

| Example | Result |
| --- | --- |
| You are paying a new household appliance by 36 monthly installments of $20. The interest rate is 6% per annum. The bill comes at the end of every month. What is the total invested, when the last bill has been paid?  `FV(0.005,36,-20)` | Returns $786.72 |
