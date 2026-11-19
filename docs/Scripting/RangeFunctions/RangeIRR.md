---
title: "RangeIRR Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/RangeFunctions/RangeIRR.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Range functions"]
---
# RangeIRR Script and chart function

RangeIRR() returns the internal rate of return for a
series of cash flows represented by the input values.

The internal rate of return is the interest rate received for an investment consisting of payments (negative values) and income (positive values)
that occur at regular periods.

This function uses a simplified version of the Newton method for calculating the internal rate of return (IRR).

Syntax:

RangeIRR(value[, value][, Expression])

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| value | A single value or a range of values as returned by an inter record function with a third optional parameter. The function needs at least one positive and one negative value to be calculated. |
| Expression | Optional expressions or fields containing the range of data to be measured. |

Limitations:

Text values, NULL values and missing values are disregarded.

Example table

| Examples | Results |
| --- | --- |
| `RangeIRR(-70000,12000,15000,18000,21000,26000)` | Returns 0.0866 |
| Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.  RangeTab3:  LOAD \*,  recno() as RangeID,  RangeIRR(Field1,Field2,Field3) as RangeIRR;  LOAD \* INLINE [  Field1|Field2|Field3  -10000|5000|6000  -2000|NULL|7000  -8000|'abc'|8000  -1800|11000|9000  -5000|5000|9000  -9000|4000|2000  `] (delimiter is '|');` | |  | | --- | | The resulting table shows the returned values of RangeIRR for each of the records in the table. | | |  |  | | --- | --- | | RangeID | RangeIRR | | 1 | 0.0639 | | 2 | 0.8708 | | 3 | - | | 4 | 5.8419 | | 5 | 0.9318 | | 6 | -0.2566 | | |

## Learn more

- [*Inter-record functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/inter-record-functions-charts.htm)
