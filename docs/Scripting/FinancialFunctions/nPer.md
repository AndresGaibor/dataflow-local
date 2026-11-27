---
title: "nPer Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/nPer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---

# nPer Script and chart function

This function returns the number of periods for an investment based on periodic, constant
payments and a constant interest rate.

Syntax:

nPer(rate, pmt,
pv [ ,fv [ , type ] ])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| rate | The interest rate per period. |
| nper | The total number of payment periods in an annuity. |
| pmt | The payment made each period. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20. |
| pv | The present value, or lump-sum amount, that a series of future payments is worth right now. If pv is omitted, it is assumed to be 0 (zero). |
| fv | The future value, or cash balance, you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0. |
| type | Should be 0 if payments are due at the end of the period and 1 if payments are due at the beginning of the period. If type is omitted, it is assumed to be 0. |

Examples and results:

Scripting example

| Example | Result |
| --- | --- |
| You want to sell a household appliance by monthly installments of $20. The interest rate is 6% per annum. The bill comes at the end of every month. How many periods are required if the value of the money received after the last bill has been paid should equal $800?  nPer(0.005,-20,0,800) | Returns 36.56 |
