---
title: "RangeNPV Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeNPV.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---
# RangeNPV Script and chart function

RangeNPV() returns the net present value of an investment
based on a discount rate and
a series of future periodic payments (negative values) and incomes (positive values).
The result has a default number format of money.

For cash flows that are not necessarily periodic, see [*RangeXNPV Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeXNPV.htm).

Syntax:

RangeNPV(discount\_rate,
value[,value][, Expression])

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| discount\_rate | The interest rate per period. |
| value | A payment or income occurring at the end of each period. Each value may be a single value or a range of values as returned by an inter-record function with a third optional parameter. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

Text values, NULL values and missing values are disregarded.

| Examples | Results |
| --- | --- |
| `RangeNPV(0.1,-10000,3000,4200,6800)` | Returns 1188.44 |
| Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.  RangeTab3:  LOAD \*,  recno() as RangeID,  RangeNPV(Field1,Field2,Field3) as RangeNPV;  LOAD \* INLINE [  Field1|Field2|Field3  10|5|-6000  2|NULL|7000  8|'abc'|8000  18|11|9000  5|5|9000  9|4|2000  ] (delimiter is '|'); | |  | | --- | | The resulting table shows the returned values of RangeNPV for each of the records in the table. | | |  |  | | --- | --- | | RangeID | RangeNPV | | 1 | $-49.13 | | 2 | $777.78 | | 3 | $98.77 | | 4 | $25.51 | | 5 | $250.83 | | 6 | $20.40 | | |

## Learn more

- [*Inter-record functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/inter-record-functions-charts.htm)
