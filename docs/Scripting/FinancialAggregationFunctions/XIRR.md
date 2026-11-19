---
title: "XIRR Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XIRR.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---
# XIRR Script function

XIRR() returns the aggregated internal
rate of return (yearly) for a schedule of cash flows (that is not necessarily periodic)
represented by paired numbers in pmt and date iterated
over a number of records as defined by a group by clause. All payments are discounted based on a 365-day year.

Qlik's XIRR functionality (XIRR() and RangeXIRR() functions) uses the following equation, solving for the `Rate` value, to determine the correct XIRR value:

`XNPV(Rate, pmt, date) = 0`

The equation is solved using a simplified version of the Newton method.

Syntax:

XIRR(pmt,
date )

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| pmt | Payments. The expression or field containing the cash flows corresponding to the payment schedule given in date. |
| date | The expression or field containing the schedule of dates corresponding to the cash flow payments given in pmt. |

When working with this function, the following limitations apply:

- Text values, NULL values and missing
  values in any or both pieces of a data-pair will result in the entire
  data-pair to be disregarded.
- This function requires at least one valid negative and at least one valid positive payment (with corresponding valid dates). If these payments are not provided, a NULL value is returned.

These topics might help you work with this function:

- [*XNPV Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XNPV.htm): Use this function to calculate aggregated net present value for a schedule of cash flows.
- [*RangeXIRR Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXIRR.htm): **RangeXIRR()** is the equivalent range function for the **XIRR()** function.

> **Note:** For information about recent updates to the underlying algorithm used by this function, see support article [XIRR function Fix and Update](https://community.qlik.com/t5/Member-Articles/XIRR-function-Fix-and-Update/ta-p/2049021).

## Example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Transaction data for a series of cashflows.
- The use of the XIRR() function to compute internal yearly rate of return for these cashflows.

Load script

```
Cashflow:
LOAD 2013 as Year, * inline [
Date|Payments
2013-01-01|-10000
2013-03-01|3000
2013-10-30|4200
2014-02-01|6800
] (delimiter is '|');
 
Cashflow1:
LOAD Year,XIRR(Payments, Date) as XIRR2013  Resident Cashflow Group By Year;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Year`
- `XIRR2013`

Results table

| Year | XIRR2013 |
| --- | --- |
| 2013 | 0.5385 |

## Interpreting the XIRR return value

The XIRR functionality is usually used to analyze an investment, where there is an outgoing (negative) payment in the beginning, and then a series of smaller income (positive) payments later on. Here is a simplified example with only one negative and one positive payment:

Cashflow:

LOAD \* inline [

Date|Payments

2023-01-01|-100

2024-01-01|110

] (delimiter is '|');

We make an initial payment of 100 and get 110 back after exactly one year. This represents a rate of return of 10% per year. `XIRR(Payments, Date)` returns a value of 0.1.

The return value of the XIRR functionality can be positive or negative. In the case of an investment, a negative result indicates that the investment is a loss. The amount of gain or loss can be calculated simply by making a sum aggregation over the payments field.

In the example above, we are lending out our money for one year. The rate of return can be thought of as interest. It is also possible to use XIRR's functionality when you are on the other side of the transaction (for example, if you are the borrower instead of the lender).

Consider this example:

Cashflow:

LOAD \* inline [

Date|Payments

2023-01-01|100

2024-01-01|-110

] (delimiter is '|');

This is the same as the first example but inverted. Here, we are borrowing 100 for one year and we repay it with a 10% interest. In this example, the XIRR calculation returns 0.1 (10%), the same value as the first example.

Note that in the first example, we received a profit of 10, and in the second example, we experienced a loss of 10, but the return value of the XIRR functionality is positive for both these examples. This is because the XIRR functionality calculates the hidden interest in the transaction, regardless of which side you are on in the transaction.

## Limitations with multiple solutions

Qlik's XIRR functionality is defined by the following equation, in which the `Rate` value is solved:

`XNPV(Rate, pmt, date) = 0`

It is sometimes possible for this equation to have more than one solution. This is known as the “multiple-IRR problem”, and is caused by a non-normal cash flow stream (also called an unconventional cash flow). The following load script shows an example of this:

Cashflow:

LOAD \* inline [

Date|Payments

2021-01-01|-200

2022-01-01|500

2023-01-01|-250

] (delimiter is '|');

In this example, there is one negative solution and one positive solution (`Rate` = -0.3 and `Rate` = 0.8). **XIRR()** will return 0.8.

When Qlik's XIRR functionality searches for a solution, it starts at `Rate` = 0 and increases the rate in steps until it finds a solution. If there is more than one positive solution, it will return the first one that it encounters. If it cannot find a positive solution, it will reset the `Rate` back to zero and start searching for a solution in the negative direction.

Note that a “normal” cash flow stream is guaranteed to have only one solution. “Normal” cash flow stream means that all payments with the same sign (positive or negative) are in a continuous group.

## Learn more

- [*XNPV Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XNPV.htm)
- [*RangeXIRR Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXIRR.htm)
- [XIRR function Fix and Update](https://community.qlik.com/t5/Member-Articles/XIRR-function-Fix-and-Update/ta-p/2049021)
