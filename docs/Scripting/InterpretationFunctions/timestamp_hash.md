---
title: "Timestamp# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/timestamp_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Timestamp# Script and chart function

Expand/Collapse all

# Timestamp# Script and chart function

Timestamp#() evaluates
an expression as a date and
time value, in the timestamp format set in the data load script or the operating system, unless a format string is supplied.

Syntax:

timestamp#(text[,
format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String describing the format that should be used to interpret the text string. If omitted, the short date format, time format, and decimal separator set in the operating system is used. ISO 8601 is supported for timestamps.  The Timestamp# function supports many format options for different time structures, for example:  DD/MM/YYYY: Focuses on just the date (for example: 15/11/2024).  ​YYYY-MM-DD hh:mm:ss: ​Displays the full timestamp (for example: 2024-11-15 13:30:45).  ​MMM DD, YYYY: ​Displays a short version of the month and the full year (for example: Nov 15, 2024).  ​hh:mm:ss TT: ​Shows only the time in 12-hour format (for example: 01:30:45 PM)  ​HH:mm:ss: ​Displays time in 24-hour format (for example: 13:30:45)  ​wwww, MMM DD YYYY: ​Shows full day of the week and date (for example: Friday, Nov 15 2024)  ​YYYY-MM-DD hh:mm:ss.fff: ​Includes milliseconds (for example: 2024-11-15 13:30:45.123​).  [*Descriptions for number and time formats*](../../Introduction/conventions-number-time-formats.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Timestamp#('12-03-2023 10:25:30', 'DD-MM-YYYY hh:mm:ss') | Returns 12-03-2023 10:25:30 |
| Timestamp#('2023/03/15 13:45', 'YYYY/MM/DD hh:mm') | Returns 2023/03/15 13:45 |

## Example - Timestamp# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - InputString
- A preceding load that uses the Timestamp# function to treat the expression as a date and time value. When executed, it creates an additional field called TimeStamp\_InputString.

Load script

```
SET DateFormat='M/D/YYYY'
Example:
Load *,
Timestamp(Timestamp#(InputString)) as TimeStamp_InputString;
LOAD * INLINE [
InputString
2015-09-15T12:13:14
1952-10-16T13:14:00+0200
1109-03-01T14:15
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputString
- TimeStamp\_InputString

Results table

| InputString | TimeStamp\_InputString |
| --- | --- |
| 1109-03-01T14:15 | 3/1/1109 2:15:00 PM |
| 1952-10-16T13:14:00+0200 | 10/16/1952 11:14:00 AM |
| 2015-09-15T12:13:14 | 9/15/2015 12:13:14 PM |

In this example, you can see how string values can be evaluated as a timestamp using the Timestamp# function.

## Example - Timestamp# scenario

Load script

Overview

Data from an event log contains a timestamp format that you want to use.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Event
  - EventDateTime
- A preceding load that uses the Timestamp# function to convert the values in the EventDateTime field into a date and time format that the system can understand. When executed, it creates an additional field called EventTimestamp.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';
Example:
LOAD
Event,
EventDateTime,
Timestamp#(EventDateTime, 'DD-MM-YYYY hh:mm:ss') AS EventTimestamp
INLINE [
Event, EventDateTime
"Login", "12-03-2023 10:25:30"
"Logout", "12-03-2023 12:45:10"
"Login", "13-03-2023 09:10:15"
"Logout", "13-03-2023 17:30:20"
"Login", "14-03-2023 08:00:00"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Event
- EventDateTime
- EventTimestamp

Create the following measure:

- =Timestamp(EventTimestamp), to view the timestamp formatted using the format supplied in the load script as a default setting.

Results table

| Event | EventDateTime | EventTimestamp | Timestamp(EventTimestamp) |
| --- | --- | --- | --- |
| Login | 12-03-2023 10:25:30 | 12-03-2023 10:25:30 | 3/12/2023 10:25:30 AM |
| Login | 13-03-2023 09:10:15 | 13-03-2023 09:10:15 | 3/13/2023 9:10:15 AM |
| Login | 14-03-2023 08:00:00 | 14-03-2023 08:00:00 | 3/14/2023 8:00:00 AM |
| Logout | 12-03-2023 12:45:10 | 12-03-2023 12:45:10 | 3/12/2023 12:45:10 PM |
| Logout | 13-03-2023 17:30:20 | 13-03-2023 17:30:20 | 3/13/2023 5:30:20 PM |

In this example, you can see how values can be converted using the Timestamp# function.
