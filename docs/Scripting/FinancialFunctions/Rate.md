---
title: "Rate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/Rate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Financial functions"]
---
# Rate Script and chart function

This function returns the interest rate per period on annuity. The result has a default
number format of Fix two decimals
and %.

Syntax:

Rate(nper, pmt ,
pv [ ,fv [ , type ] ])

Return data type:  numeric.

The rate is calculated by iteration and can have zero or more solutions. If the
successive results of rate do
not converge, a NULL value will be returned.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| nper | The total number of payment periods in an annuity. |
| pmt | The payment made each period. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20. |
| pv | The present value, or lump-sum amount, that a series of future payments is worth right now. If pv is omitted, it is assumed to be 0 (zero). |
| fv | The future value, or cash balance, you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0. |
| type | Should be 0 if payments are due at the end of the period and 1 if payments are due at the beginning of the period. If type is omitted, it is assumed to be 0. |

Examples and results:

Scripting example

| Example | Result |
| --- | --- |
| What is the interest rate of a five-year $10,000 annuity loan with monthly payments of $300?  `Rate(60,-300,10000)` | Returns 2.00% |
