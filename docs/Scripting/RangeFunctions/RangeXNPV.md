---
title: "RangeXNPV Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXNPV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---

# RangeXNPV Script and chart function

Expand/Collapse all

# RangeXNPV Script and chart function

RangeXNPV() returns the net present value for a schedule of cash flows (not necessarily periodic) represented by paired numbers in the expressions given by pmt and date. All payments are discounted based on a 365-day year.

Syntax:

RangeXNPV(discount\_rate,
value, date{, value, date})

Return data type: numeric

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | discount\_rate is the yearly rate that the payments should be discounted by. |
| value | A cash flow or a series of cash flows that corresponds to a schedule of payments in dates. Each value may be a single value or a range of values as returned by an inter-record function with a third optional parameter. The series of values must contain at least one positive and one negative value. |
| date | A payment date or a schedule of payment dates that corresponds to the cash flow payments. |

When working with this function, the following limitations apply:

- Text values, NULL values and missing values are disregarded.
- All payments are discounted based on a 365-day year.

## Example - script

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Financial data contained in a table called RangeTab3.
- The use of the RangeXNPV() function to compute net present value.

Load script

```
RangeTab3:
LOAD *,
recno() as RangeID,
RangeXNPV(DiscountRate,Value1,Date1,Value2,Date2) as RangeXNPV;
LOAD * INLINE [
DiscountRate|Value1|Date1|Value2|Date2
0.1|-100|2021-01-01|100|2022-01-01|
0.1|-100|2021-01-01|110|2022-01-01|
0.1|-100|2021-01-01|125|2022-01-01|
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- RangeID
- RangeXNPV

Results table

| RangeID | RangeXNPV |
| --- | --- |
| 1 | -$9.09 |
| 2 | -$0.00 |
| 3 | $13.64 |

## Example - chart expression

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Financial data contained in a table called RangeTab3.
- The use of the RangeXNPV() function to compute net present value.

Load script

```
RangeTab3:
LOAD *,
recno() as RangeID,
RangeXNPV(DiscountRate,Value1,Date1,Value2,Date2) as RangeXNPV;
LOAD * INLINE [
DiscountRate|Value1|Date1|Value2|Date2
0.1|-100|2021-01-01|100|2022-01-01|
0.1|-100|2021-01-01|110|2022-01-01|
0.1|-100|2021-01-01|125|2022-01-01|
] (delimiter is '|');
```

Results

Do the following:

Load the data and open a [sheet](#glossary-0 "Glossary term"). Create a new table and add the following calculation as a [measure](#glossary-1 "Glossary term").

=RangeXNPV(0.1, -2500,'2008-01-01',2750,'2008-09-01')

Results table

| =XIRR(Payments, Date) |
| --- |
| $80.25 |

## Learn more

- [*XNPV Script function*](../FinancialAggregationFunctions/XNPV.htm)
