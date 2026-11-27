---
title: "Floor Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/floor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Floor Script and chart function

Floor() rounds down a number to the nearest multiple of the step shifted by the offset number.

Compare with the ceil function, which rounds input numbers up.

Syntax:

Floor(x[, step[, offset]])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| x | Input number. |
| step | Interval increment. The default value is 1. |
| offset | Defines the base of the step interval. The default value is 0. |

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Floor(2.4) | Returns 2  In this example, the size of the step is 1 and the base of the step interval is 0.  The intervals are  ...0 <= x <1, 1 <= x < 2, 2<= x <3, 3<= x <4.... |
| Floor(4.2) | Returns 4 |
| Floor(3.88 ,0.1) | Returns 3.8  In this example, the size of the interval is 0.1 and the base of the interval is 0.  The intervals are ... 3.7 <= x < 3.8, 3.8 <= x < 3.9, 3.9 <= x < 4.0... |
| Floor(3.88 ,5) | Returns 0 |
| Floor(1.1 ,1) | Returns 1 |
| Floor(1.1 ,1,0.5) | Returns 0.5  In this example, the size of the step is 1 and the offset is 0.5. It means that the base of the step interval is 0.5 and not 0.  The intervals are ...0.5 <= x <1.5, 1.5 <= x < 2.5, 2.5<= x <3.5,... |

## Learn more

- [*Frac Script and chart function*](frac.htm)
- [*Ceil Script and chart function*](ceil.htm)
