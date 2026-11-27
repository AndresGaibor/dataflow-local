---
title: "Interval# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interval_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Interval# Script and chart function

Expand/Collapse all

# Interval# Script and chart function

Interval#() evaluates
a text expression as a time interval
in the format set in the operating system, by default, or in the format specified in the second argument, if supplied.

Syntax:

Interval#(text[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String describing the expected input format to use when converting the string to a numeric interval. If omitted, the time format and decimal separator set in the operating system are used.  The Interval# function supports many format options for different time structures, for example:  ​hh:mm—Simple Hours and Minutes  ​hh:mm:ss—Hours, Minutes, and Seconds  ​d hh:mm—Days, Hours, and Minutes  [*Descriptions for number and time formats*](../../Introduction/conventions-number-time-formats.htm)​ |

The Interval# function converts a text time interval to a numeric equivalent.

Example: Chart expressions

| Example | Result |
| --- | --- |
| Interval#( '12:30', 'hh:mm' ) | Returns the numeric value 0.5208, which is 12.5 hours when converted to a day fraction. |
| Interval#( '1 05', 'd hh' ) | Returns a numeric representation equivalent to 1.2083 days. |

## Example - Interval# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - IntervalValue
- A preceding load that uses the Interval# function to convert the text in the IntervalValue field to a number, which can be recognized as a time.

Load script

```
Example:
Load *, Interval#(IntervalValue, 'D hh') as FormattedIntervalValue;
Load * inline [
IntervalValue
1 05
2 15
1 09
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- IntervalValue

Create the following measures:

- =Num(FormattedIntervalValue), to view the value as a number after it has been processed in the load script using the Interval# function.
- =Interval(FormattedIntervalValue, 'dd:hh:mm'), to view the value as an interval format using the format provided in the function.

Results table

| IntervalValue | Num(FormattedIntervalValue) | Interval(FormattedIntervalValue, 'dd:hh:mm' |
| --- | --- | --- |
| 1 05 | 1.2083333333333 | 01:05:00 |
| 1 09 | 1.375 | 01:09:00 |
| 2 15 | 2.625 | 02:15:00 |

The results demonstrate how the Interval# function converts values to a number which can then be displayed using a specified format parameter. For example, in the IntervalValue column, the value 2 15 is converted to a number in the preceding load (FormattedIntervalValue field). The second column uses the Num function to show this converted value as a number, 2.625. The third column uses the Interval function to format this number in days, hours, and minutes, displaying it as 02:15:00, or 2 days 15 hours.

## Example - Interval# scenario

Load script

Overview

A dataset of support ticket data contains a field that mixes text and time data, for example 2 days 04 hours. We want to convert these values into normal time values.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - TicketID
  - ResolutionTime
- A preceding load that uses the Interval# function to convert the text in the ResolutionTime field into a number which can be recognized in days and hours.

Load script

```
Example:
Load *, Interval#(ResolutionTime, 'd "days" hh "hours"') as FormattedResolutionTime;
Load * inline [
TicketID, ResolutionTime
Ticket A, 2 days 04 hours
Ticket B, 2 days 06 hours
Ticket C, 3 days 10 hours
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- TicketID
- ResolutionTime

Create the following measures:

- =Interval(FormattedResolutionTime, 'dd:hh'), to convert the values into the desired format with a dual value.
- =Num(FormattedResolutionTime), to show the numeric values of the field.

Results table

| TicketID | ResolutionTime | Interval(FormattedResolutionTime, 'dd hh') | Num(FormattedResolutionTime) |
| --- | --- | --- | --- |
| Ticket A | 2 days 04 hours | 02 04 | 2.1666666666667 |
| Ticket B | 2 days 06 hours | 02 06 | 2.25 |
| Ticket C | 3 days 10 hours | 03 10 | 3.4166666666667 |

The results show how you can use the Interval# function to convert values to a number, and then display them in a more typical time format. For example, Ticket B has a resolution time of 2 days 06 hours. This value is converted to a number in the preceding load (FormattedResolutionTime field). The new value displays as 02 06 (2 days and 6 hours) when formatted using the Interval function in column 3. In column 4, the Num function displays its numeric value as 2.25.

## Learn more

- [*Time# Script and chart function*](time_hash.htm)
