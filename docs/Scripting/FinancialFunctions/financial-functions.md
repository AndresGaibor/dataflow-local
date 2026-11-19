---
title: "Financial functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/financial-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Financial functions

Financial functions can be used in the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/financial-functions.htm#glossary-0 "Glossary term") and in chart expressions to calculate payments and interest rates.

For all the
arguments, cash that is paid out is represented by negative numbers. Cash
received is represented by positive numbers.

Listed here are the arguments that are used in the financial functions (excepting the ones beginning with range-).

> **Note:** 
> For all financial functions it is vital that you are consistent when specifying units for rate
> and nper. If monthly
> payments are made on a five-year loan at 6% annual interest, use 0.005 (6%/12)
> for rate and 60 (5\*12) for nper. If annual payments are made on
> the same loan, use 6% for rate
> and 5 for nper.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

FV

This function returns the future value of an investment based on periodic, constant
payments and a simple annual interest.

[**FV**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/FV.htm)(rate, nper, pmt
[ ,pv [ , type ] ])

nPer

This function returns the number of periods for an investment based on periodic, constant
payments and a constant interest rate.

[**nPer**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/nPer.htm)(rate, pmt,
pv [ ,fv [ , type ] ])

Pmt

This function returns the payment for a loan based on periodic, constant payments
and a constant interest rate. It cannot change over the life of the annuity. A payment is stated as a negative number, for example, -20.

[**Pmt**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/Pmt.htm)(rate, nper,
pv [ ,fv [ , type ] ] )

PV 

This function returns the present value of an investment.

[**PV**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/PV.htm)(rate, nper, pmt
[ ,fv [ , type ] ])

Rate

This function returns the interest rate per period on annuity. The result has a default
number format of Fix two decimals
and %.

[**Rate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialFunctions/Rate.htm)(nper, pmt ,
pv [ ,fv [ , type ] ])

## Learn more

- [*BlackAndSchole Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Black-and-Scholes.htm)
- [*Money Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Money.htm)
