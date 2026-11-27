---
title: "Time# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/time_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Time# Script and chart function

Expand/Collapse all

# Time# Script and chart function

Time#() evaluates
an expression as a time value, in the time format set in the data load script or the operating system, unless a format string is supplied.

Syntax:

time#(text[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String describing the format that should be used to interpret the text string. If omitted, the time format and decimal separator set in the operating system is used.  The Time# function supports many format options for different time structures, for example:  ​hh:mm:ss—Formats a time value in a standard time format and display hours, minutes, and seconds with leading zeros.  ​hh:mm TT—​Uses a 12-hour format with AM/PM suffix.  ​hh:mm—Shows only hours and minutes, omitting seconds.  ​hh.mm.ss—Time format with different separators, such as a period (.) instead of a colon.  ​hh TT—​Includes only hour and AM/PM.  ​hh "Hrs" mm "Mins"—Displays the time with custom text, such as Hrs.​  [*Descriptions for number and time formats*](../../Introduction/conventions-number-time-formats.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Time#('09:00:00') | Returns 09:00:00 when the TimeFormat setting is 'hh:mm:ss'. |
| Time#( '09:00:00','hh:mm:ss' ) | Returns 09:00:00 when the format supplied is 'hh:mm:ss'. |
| Time#('03:25 PM', 'hh:mm TT') | Returns 03:25 PM when the format supplied is 'hh:mm TT'. |

## Example - Time# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - InputTime
- The TimeFormat variable, which uses the h:mm:ss TT format.
- A preceding load that uses the Time# function to convert the text value of InputTime into a time/numeric field called ParsedTime which the system can use.

Load script

```
SET TimeFormat='h:mm:ss TT';
Example:
Load
InputTime,
Time#(InputTime, 'hh-mm-ss') as ParsedTime
Inline [
InputTime
12-30-45
05-15-00
22-10-55
08-20-35
19-45-15
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputTime
- ParsedTime

Create the following measure:

- =Time(ParsedTime), to view the time using the format supplied in the load script as a default setting.

Results table

| InputTime | ParsedTime | Time(ParsedTime) |
| --- | --- | --- |
| 05-15-00 | 05-15-00 | 5:15:00 AM |
| 08-20-35 | 08-20-35 | 8:20:35 AM |
| 12-30-45 | 12-30-45 | 12:30:45 PM |
| 19-45-15 | 19-45-15 | 7:45:15 PM |
| 22-10-55 | 22-10-55 | 10:10:55 PM |

The values in the InputTime field are displayed as text and are left aligned. Once the values in InputTime are parsed through the Time# function, the resulting ParsedTime field is created. The values in the new field are right-aligned as they are now treated as a valid time value. The third column uses the Time function to evaluate the ParsedTime values and format them according to the TimeFormat in the load script.

## Example - Time# scenario

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - NoDelimiterTime
- The TimeFormat variable, which uses the hh.mm.ss format.
- A preceding load that uses the Time# function to convert the text value of NoDelimiterTime into a time/numeric field called ParsedNoDelimiterTime.

Load script

```
SET TimeFormat='hh.mm.ss';
Example:
Load
NoDelimiterTime,
Time#(NoDelimiterTime, 'hhmmss') as ParsedNoDelimiterTime
Inline [
NoDelimiterTime
143015
091045
235959
060530
184010
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- NoDelimiterTime

Create the following measure:

- =Time(ParsedNoDelimiterTime,'hh:mm:ss'), to view the time using the format supplied in the load script as a default setting.

Results table

| NoDelimiterTime | Time(ParsedNoDelimiterTime,'hh:mm:ss') |
| --- | --- |
| 060530 | 06:05:30 |
| 091045 | 09:10:45 |
| 143015 | 14:30:15 |
| 184010 | 18:40:10 |
| 235959 | 23:59:59 |

The results show how you can use the Time# function to parse and convert values from text to a time/numeric value.
