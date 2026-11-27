---
title: "Interval Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Interval.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---

# Interval Script and chart function

Expand/Collapse all

# Interval Script and chart function

Interval() formats
a number as a time interval
using the format in the system variables in the data load script, or the operating system, or a format string, if supplied.

Intervals may be formatted as a time, as days or as a combination
of days, hours, minutes, seconds and fractions of seconds.

Syntax:

Interval(number[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| number | The number to be formatted. |
| format | String describing how the resulting interval string is to be formatted. If omitted, the time format and decimal separator, set in the operating system, are used. If omitted, the time format and decimal separator, set in the operating system, are used. The Interval function supports many format options for different time structures, for example:  ​hh:mm—Simple Hours and Minutes  ​hh:mm:ss—Hours, Minutes, and Seconds  ​d hh:mm—Days, Hours, and Minutes  [*Descriptions for number and time formats*](../../Introduction/conventions-number-time-formats.htm)​ |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Interval( 0.375 ) | Returns 9:00:00 when the TimeFormat is h:mm:ss. |
| Interval(.375​, 'hh:mm' ) | Returns 9:00 when the format supplied in the function is hh.mm. |
| Interval( 0.375​, 'd hh' ) | Returns 0 09 when the format supplied in the function is d hh. |

## Example - Interval fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - IntervalValue
- The TimeFormat variable, which uses the h:mm:ss format.

Load script

```
SET TimeFormat='h:mm:ss';
Example:
Load * inline [
IntervalValue
0.375
1.375
35.648
36.875
368.75
468.95
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- IntervalValue

Create the following measures:

- =Interval(IntervalValue), to view the value as an interval format using the system setting.
- =Interval(IntervalValue, 'd hh'), to view the value as an interval format using the format provided in the function.
- =Interval(IntervalValue, 'hh:mm'), to view the value as an interval format using the format supplied in the function.
- =Interval(IntervalValue, 'd hh:mm'), to view the value as an interval format using the format supplied in the function.

Results table

| IntervalValue | Interval(IntervalValue) | Interval(IntervalValue, 'd hh') | Interval(IntervalValue, 'hh:mm' | Interval(IntervalValue, 'd hh:mm') |
| --- | --- | --- | --- | --- |
| 0.375 | 9:00:00 | 0 09 | 09:00 | 0 09:00 |
| 1.375 | 33:00:00 | 1 09 | 33:00 | 1 09:00 |
| 35.648 | 855:33:07 | 35 15 | 855:33 | 35 15:33 |
| 36.875 | 885:00:00 | 36 21 | 885:00 | 36 21:00 |
| 368.75 | 8850:00:00 | 368 18 | 8850:00 | 368 18:00 |
| 468.95 | 11254:48:00 | 468 22 | 11254:48 | 468 22:48 |

The results show how the Interval function displays values according to the format parameter in the function. For example, in the last row, the value 468.95, when formatted using the Interval function and format parameter, d hh:mm, returns the value 468 days, 22 hours, and 48 minutes.

## Example - Interval scenario

Chart expression

Overview

Support ticket data calculates the resolution time per ticket in seconds. You want to convert this value to another format.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - TicketID
  - ResolutionTime

Load script

```
Example:
Load * inline [
TicketID, ResolutionTime
Ticket A, 4350
Ticket B, 560
Ticket C, 86400
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- TicketID

Create the following measure:

- =Interval(ResolutionTime / 86400, 'hh:mm:ss'), to convert the values to days, by dividing ResolutionTime by 86,400, and then formatting it using the format provided in the function.

Results table

| TicketID | Interval(ResolutionTime / 86400, 'hh:mm:ss') |
| --- | --- |
| Ticket A | 01:12:30 |
| Ticket B | 00:09:20 |
| Ticket C | 24:00:00 |

The resolution time values that were originally supplied in seconds are now converted to a fraction of a day, and then formatted in hours, minutes, and seconds. For example, the table shows that Ticket B took 9 hours and 20 minutes to resolve.
