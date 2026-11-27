---
title: "Round Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/round.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Round Script and chart function

Round() returns the result of rounding a number up or down to the nearest multiple of step shifted by the offset number.

If the number to round is exactly
in the middle of an interval, it is rounded upwards.

Syntax:

Round(x[, step[, offset]])

Return data type:  numeric

Information noteIf you are rounding a floating point number you may observe erroneous results. These rounding errors occur because floating point numbers are represented by a finite number of binary digits. Therefore, results are calculated using a number that is already rounded. If these rounding errors will affect your work, multiply the numbers to convert them to integers before rounding.

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
| Round(3.8 ) | Returns 4  In this example, the size of the step is 1 and the base of the step interval is 0.  The intervals are  ...0 <= x <1, 1 <= x < 2, 2<= x <3, 3<= x <4... |
| Round(3.8,4 ) | Returns 4 |
| Round(2.5 ) | Returns 3.  In this example, the size of the step is 1 and the base of the step interval is 0.  The intervals are ...0 <= x <1, 1 <= x <2, 2<= x <3... |
| Round(2,4 ) | Returns 4. Rounded up because 2 is exactly half of the step interval of 4.  In this example, the size of the step is 4 and the base of the step interval is 0.  The intervals are ...0 <= x <4, 4 <= x <8, 8<= x <12... |
| Round(2,6 ) | Returns 0. Rounded down because 2 is less than half of the step interval of 6.  In this example, the size of the step is 6 and the base of the step interval is 0.  The intervals are ...0 <= x <6, 6 <= x <12, 12<= x <18... |
| Round(3.88 ,0.1) | Returns 3.9  In this example, the size of the step is 0.1 and the base of the step interval is 0.  The intervals are ... 3.7 <= x <3.8, 3.8 <= x <3.9, 3.9 <= x < 4.0... |
| Round(3.88875,1/1000) | Returns 3.889  In this example, the size of the step is 0.001, which rounds the number up and limits it to three decimal places. |
| Round(3.88 ,5) | Returns 5 |
| Round(1.1 ,1,0.5) | Returns 1.5  In this example, the size of the step is 1 and the base of the step interval is 0.5.  The intervals are ...0.5 <= x <1.5, 1.5 <= x <2.5, 2.5<= x <3.5... |
