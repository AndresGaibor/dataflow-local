---
title: "XNPV - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FinancialAggregationFunctionsInCharts/xnpv.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Financial aggregation functions"]
---

# XNPV - chart function

XNPV() returns the aggregated net present
value for a schedule of cash flows (not necessarily periodic) represented
by paired numbers in the expressions given by pmt
and date, iterated over
the chart dimensions. All payments are discounted based on a 365-day year.

Syntax:

XNPV([TOTAL [<fld{,fld}>]] discount\_rate, pmt, date)

Return data type:  numeric

Information noteBy default, the result will be formatted as currency.

The formula to calculate XNPV is shown below:

XNPV aggregation formula

![Image of formula for XNPV script function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-xnpv-formula.png "Click to view full size")

where:

- Pi = Net cash inflow-outflows during a single period i
- d1= the first payment date
- di = the ith payment date
- rate = discount rate

Net present value, or NPV, is used to calculate the current total value of a future stream of cash flows given a discount rate. To calculate XNPV, we need to estimate future cash flows with corresponding dates. After this, for each payment, we apply the compounded discount rate based on the date of the payment.

Performing the XNPV aggregation over a series of payments is similar to performing a Sum aggregation over those payments. The difference is that each amount is modified (or “discounted”) according to the chosen discount rate (similar to interest rate) and how far into the future the payment is. Performing XNPV with the discount\_rate parameter set to zero will make XNPV equivalent to a Sum operation (the payments will not be modified before being summed). In general, the closer the discount\_rate is set to zero, the more similar the XNPV result will be to that of a Sum aggregation.

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | discount\_rate is the yearly rate that the payments should be discounted by.  A value of 0.1 would indicate a 10% discount rate. |
| pmt | Payments. The expression or field containing the cash flows corresponding to the payment schedule given in date. Positive values are assumed to be inflows, and negative values are assumed to be outflows. Information noteXNPV() does not discount the initial cash flow since it will always happen on the start date. Subsequent payments are discounted based on a 365-day year. This is different from NPV(), where also the first payment is discounted. |
| date | The expression or field containing the schedule of dates corresponding to the cash flow payments given in pmt. The first value is used as the start date for calculating the time offsets for future cash flows. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

When working with this function, the following limitations apply:

- discount\_rate,
  pmt and date
  must not contain [aggregation](#glossary-0 "Glossary term") functions, unless these inner aggregations
  contain the TOTAL or ALL qualifiers. For
  more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.
- Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

## When to use XNPV

- XNPV() is used in financial modeling for calculating the net present value (NPV) of an investment opportunity.
- Due to its higher precision, XNPV is preferred over NPV, for all types of financial models.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing cashflow transactions.
- Information stored in a table called Cashflow.

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
```

Results

Do the following:

Load the data and open a [sheet](#glossary-2 "Glossary term"). Create a new table and add the following calculation as a [measure](#glossary-3 "Glossary term"):

=XNPV(0.09, Payments, Date)

Results table

| =XNPV(0.09, Payments, Date) |
| --- |
| $3062.49 |

## Learn more

- [*NPV - chart function*](npv.htm)
- [*Aggr - chart function*](../aggr.htm)
