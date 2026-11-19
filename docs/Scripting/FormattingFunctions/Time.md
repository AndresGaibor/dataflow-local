---
title: "Time Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Time.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---
Expand/Collapse all

# Time Script and chart function

Time() formats an expression as a time value, in the time format set
in the system variables in the data load script, or in the operating system, unless a format string is supplied.

Syntax:

Time(number[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| number | The number to be formatted. |
| format | String describing how the resulting time string is to be formatted. If omitted, the time format and decimal separator set in the operating system is used.  The `Time` function supports many format options for different time structures, for example:  `hh:mm:ss`—Formats a time value in a standard time format and display hours, minutes, and seconds with leading zeros.  ​`hh:mm TT`—​Uses a 12-hour format with AM/PM suffix.  ​`hh:mm`—Shows only hours and minutes, omitting seconds.  ​`hh.mm.ss`—​Time format with different separators, such as a period (`.`) instead of a colon.  ​`hh TT`—​Includes only hour and AM/PM.  ​`hh "Hrs" mm "Mins"`—​Displays the time with custom text, such as Hrs.​  [*Descriptions for number and time formats*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/conventions-number-time-formats.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Time( 0.375 )` | Returns `09:00:00` when the `TimeFormat` setting is `'hh:mm:ss'`. |
| `Time( 35648.375 )` | Returns `09:00:00` when the `Timeformat` supplied is `'hh:mm:ss'`. |
| `Time( 0.99999, 'hh-mm' )` | Returns `23-59` by ignoring the `TimeFormat` setting since the format is supplied in the measure. |

## Example - Time fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following field in a data table:

  - `TimeValue`
- The `TimeFormat` variable, which uses the `hh:mm:ss` format.

Load script

```
SET TimeFormat='hh:mm:ss';
Example:
Load * inline [
TimeValue
0.375
35648.375
0.99999
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `TimeValue`

Create the following measures:

- `=Time(TimeValue )`, to view the value as a time that is formatted using the system setting.
- `=Time(TimeValue, 'hh-mm' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm:ss' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm TT' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh.mm.ss' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh TT' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh "Hrs" mm "Mins"' )`, to view the value as a time in the format supplied in the function.

Results table

| TimeValue | Time(TimeValue) | Time(TimeValue, 'hh-mm') | Time(TimeValue, 'hh:mm:ss') | Time(TimeValue, 'hh:mm TT') | Time(TimeValue, 'hh:mm') | Time(TimeValue, 'hh.mm.ss') | Time(TimeValue, 'hh TT') | Time(TimeValue, 'hh "Hrs" mm "Mins"') |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.375 | 09:00:00 | 09-00 | 09:00:00 | 09:00 AM | 09:00 | 09.00.00 | 09 AM | 09 Hrs 00 Mins |
| 0.99999 | 23:59:59 | 23-59 | 23:59:59 | 11:59 PM | 23:59 | 23.59.59 | 11 PM | 23 Hrs 59 Mins |
| 35648.375 | 09:00:00 | 09-00 | 09:00:00 | 09:00 AM | 09:00 | 09.00.00 | 09 AM | 09 Hrs 00 Mins |

The results show how the `Time` function can display values based on the format supplied in the function expression.

## Example - Time fundamentals using a different TimeFormat setting

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following field in a data table:

  - `TimeValue`
- The `TimeFormat` variable, which uses the `hh.mm.ss` format.

Load script

```
SET TimeFormat='hh.mm.ss';
Example:
Load * inline [
TimeValue
0.375
35648.375
0.99999
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `TimeValue`

Create the following measures:

- `=Time(TimeValue )`, to view the value as a time that is formatted using the system setting.
- `=Time(TimeValue, 'hh-mm' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm:ss' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm TT' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh:mm' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh.mm.ss' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh TT' )`, to view the value as a time in the format supplied in the function.
- `=Time(TimeValue, 'hh "Hrs" mm "Mins"' )`, to view the value as a time in the format supplied in the function.

Results table

| TimeValue | Time(TimeValue) | Time(TimeValue, 'hh-mm') | Time(TimeValue, 'hh:mm:ss') | Time(TimeValue, 'hh:mm TT') | Time(TimeValue, 'hh:mm') | Time(TimeValue, 'hh.mm.ss') | Time(TimeValue, 'hh TT') | Time(TimeValue, 'hh "Hrs" mm "Mins"') |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.375 | 09.00.00 | 09-00 | 09:00:00 | 09:00 AM | 09:00 | 09.00.00 | 09 AM | 09 Hrs 00 Mins |
| 0.99999 | 23.59.59 | 23-59 | 23:59:59 | 11:59 PM | 23:59 | 23.59.59 | 11 PM | 23 Hrs 59 Mins |
| 35648.375 | 09.00.00 | 09-00 | 09:00:00 | 09:00 AM | 09:00 | 09.00.00 | 09 AM | 09 Hrs 00 Mins |

The results show how the `Time` function can display values based on the format supplied in the function expression.
