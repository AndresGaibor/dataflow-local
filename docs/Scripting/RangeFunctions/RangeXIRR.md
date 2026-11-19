---
title: "RangeXIRR Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXIRR.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---
# RangeXIRR Script and chart function

RangeXIRR() returns the internal rate of return (yearly) for a
schedule of cash flows that is not necessarily periodic. To calculate
the internal rate of return for a series of periodic cash flows, use the
RangeIRR
function.

Qlik's XIRR functionality (XIRR() and RangeXIRR() functions) uses the following equation, solving for the `Rate` value, to determine the correct XIRR value:

`XNPV(Rate, pmt, date) = 0`

The equation is solved using a simplified version of the Newton method.

Syntax:

RangeXIRR(value,
date{, value, date})

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| value | A cash flow or a series of cash flows that correspond to a schedule of payments in dates. The series of values must contain at least one positive and one negative value. |
| date | A payment date or a schedule of payment dates that corresponds to the cash flow payments. |

When working with this function, the following limitations apply:

- Text values, NULL values and missing values are disregarded.
- All payments are discounted based on a 365-day year.
- This function requires at least one valid negative and at least one valid positive payment (with corresponding valid dates). If these payments are not provided, a NULL value is returned.

The following topics might help you work with this function:

- [*RangeXNPV Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXNPV.htm): Use this function calculate the net present value for a schedule
  of cash flows that is not necessarily periodic.
- [*XIRR Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XIRR.htm): The **XIRR()** function calculates the aggregated internal
  rate of return (yearly) for a schedule of cash flows (that is not necessarily periodic).

> **Note:** For information about recent updates to the underlying algorithm used by this function, see support article [XIRR function Fix and Update](https://community.qlik.com/t5/Member-Articles/XIRR-function-Fix-and-Update/ta-p/2049021).

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| `RangeXIRR(-2500,'2008-01-01',2750,'2008-09-01')` | Returns 0.1532 |

## Learn more

- [*RangeIRR Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeIRR.htm)
- [*RangeXNPV Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXNPV.htm)
- [*XIRR Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FinancialAggregationFunctions/XIRR.htm)
- [XIRR function Fix and Update](https://community.qlik.com/t5/Member-Articles/XIRR-function-Fix-and-Update/ta-p/2049021)
