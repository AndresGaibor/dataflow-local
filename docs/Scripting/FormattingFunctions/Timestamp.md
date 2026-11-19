---
title: "Timestamp Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Timestamp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---
Expand/Collapse all

# Timestamp Script and chart function

TimeStamp() formats
an expression as a date and
time value, in the timestamp format set in the system variables in the data load script, or in the operating
system, unless a format string is supplied.

Syntax:

Timestamp(number[,
format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| number | The number to be formatted. |
| format | String describing how the resulting timestamp string is to be formatted. If omitted, the short date format, time format, and decimal separator set in the operating system is used.  The `Timestamp` function supports many format options for different time structures, for example:  `DD/MM/YYYY`: Focuses on just the date (for example: `15/11/2024`).  ​`YYYY-MM-DD hh:mm:ss`: ​Displays the full timestamp (for example: `2024-11-15 13:30:45`).  `​MMM DD, YYYY`: ​Displays a short version of the month and the full year (for example: `Nov 15, 2024`).  ​`hh:mm:ss TT`: ​Shows only the time in 12-hour format (for example: `01:30:45 PM`)  `​HH:mm:ss`: ​Displays time in 24-hour format (for example: `13:30:45`)  `​wwww, MMM DD YYYY`: ​Shows full day of the week and date (for example: `Friday, Nov 15 2024`)  `​YYYY-MM-DD hh:mm:ss.fff`: ​Includes milliseconds (for example: `2024-11-15 13:30:45.123`​).  [*Descriptions for number and time formats*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/conventions-number-time-formats.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Timestamp( 35648 )` | Returns `97-08-06 00:00:00` when the `TimestampFormat` is `YY-MM-DD hh:mm:ss`. |
| `Timestamp(35648,'YYYY-MM-DD hh.mm')` | Returns `1997-08-06 00.00` when the format supplied is `YYYY-MM-DD hh.mm`. |
| `Timestamp( 35648,'M/D/YYYY h:mm:ss[.fff] TT')` | Returns `8/6/1997 12:00:00 AM` when the format supplied is `M/D/YYYY h:mm:ss[.fff] TT`. |
| `Timestamp( 35648,'www, DD MMM YYYY hh:mm TT')` | Returns `Wed, 06 Aug 1997 12:00 AM` when the format supplied is `www, DD MMM YYYY hh:mm TT`. |

## Example - Timestamp fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following field in a data table:

  - `TimeStampValue`
- The `TimestampFormat` variable, which uses the `YY-MM-DD hh:mm:ss` format.

Load script

```
SET TimestampFormat='YY-MM-DD hh:mm:ss';
Example:
Load * inline [
TimeStampValue
35648.375
35648
36648.875
36648.8756789
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `TimeStampValue`

Create the following measures:

- `=Timestamp(TimeStampValue)` to view the value as a timestamp format using the system setting.
- `=Timestamp(TimeStampValue,'YYYY-MM-DD hh.mm')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'M/D/YYYY h:mm:ss[.fff] TT')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'YYYY-MM-DD hh:mm:ss.fff')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'www, DD MMM YYYY hh:mm TT')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'wwww, MMM DD YYYY')` to view the value as a timestamp format using the format supplied in the function.

Results table

| TimeStampValue | Timestamp(TimeStampValue) | Timestamp(TimeStampValue,'YYYY-MM-DD hh.mm' | Timestamp(TimeStampValue,'M/D/YYYY h:mm:ss[.fff] TT') | Timestamp(TimeStampValue,'YYYY-MM-DD hh:mm:ss.fff') | Timestamp(TimeStampValue,'www, DD MMM YYYY hh:mm TT') | Timestamp(TimeStampValue,'wwww, MMM DD YYYY') |
| --- | --- | --- | --- | --- | --- | --- |
| 35648 | 97-08-06 00:00:00 | 1997-08-06 00.00 | 8/6/1997 12:00:00 AM | 1997-08-06 00:00:00.000 | Wed, 06 Aug 1997 12:00 AM | Wednesday, Aug 06 1997 |
| 35648.375 | 97-08-06 09:00:00 | 1997-08-06 09.00 | 8/6/1997 9:00:00 AM | 1997-08-06 09:00:00.000 | Wed, 06 Aug 1997 09:00 AM | Wednesday, Aug 06 1997 |
| 36648.875 | 00-05-02 21:00:00 | 2000-05-02 21.00 | 5/2/2000 9:00:00 PM | 2000-05-02 21:00:00.000 | Tue, 02 May 2000 09:00 PM | Tuesday, May 02 2000 |
| 36648.8756789 | 00-05-02 21:00:58 | 2000-05-02 21.00 | 5/2/2000 9:00:58 PM | 2000-05-02 21:00:58.657 | Tue, 02 May 2000 09:00 PM | Tuesday, May 02 2000 |

The results show how the `TimestampFormat` function can display values using different format parameters.

## Example - Timestamp fundamentals using a different TimestampFormat setting

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following field in a data table:

  - `TimeStampValue`
- The `TimestampFormat` variable, which uses the `YY-MM-DD hh:mm:ss` format.

Load script

```
SET TimestampFormat='M/D/YY hh:mm:ss';
Example:
Load * inline [
TimeStampValue
35648.375
35648
36648.875
36648.8756789
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `TimeStampValue`

Create the following measures:

- `=Timestamp(TimeStampValue)` to view the value as a timestamp format using the system setting.
- `=Timestamp(TimeStampValue,'YYYY-MM-DD hh.mm')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'M/D/YYYY h:mm:ss[.fff] TT')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'YYYY-MM-DD hh:mm:ss.fff')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'www, DD MMM YYYY hh:mm TT')` to view the value as a timestamp format using the format supplied in the function.
- `=Timestamp(TimeStampValue,'wwww, MMM DD YYYY')` to view the value as a timestamp format using the format supplied in the function.

Results table

| TimeStampValue | Timestamp(TimeStampValue) | Timestamp(TimeStampValue,'YYYY-MM-DD hh.mm' | Timestamp(TimeStampValue,'M/D/YYYY h:mm:ss[.fff] TT') | Timestamp(TimeStampValue,'YYYY-MM-DD hh:mm:ss.fff') | Timestamp(TimeStampValue,'www, DD MMM YYYY hh:mm TT') | Timestamp(TimeStampValue,'wwww, MMM DD YYYY') |
| --- | --- | --- | --- | --- | --- | --- |
| 35648 | 8/6/97 00:00:00 | 1997-08-06 00.00 | 8/6/1997 12:00:00 AM | 1997-08-06 00:00:00.000 | Wed, 06 Aug 1997 12:00 AM | Wednesday, Aug 06 1997 |
| 35648.375 | 8/6/97 09:00:00 | 1997-08-06 09.00 | 8/6/1997 9:00:00 AM | 1997-08-06 09:00:00.000 | Wed, 06 Aug 1997 09:00 AM | Wednesday, Aug 06 1997 |
| 36648.875 | 5/2/00 21:00:00 | 2000-05-02 21.00 | 5/2/2000 9:00:00 PM | 2000-05-02 21:00:00.000 | Tue, 02 May 2000 09:00 PM | Tuesday, May 02 2000 |
| 36648.8756789 | 5/2/00 21:00:58 | 2000-05-02 21.00 | 5/2/2000 9:00:58 PM | 2000-05-02 21:00:58.657 | Tue, 02 May 2000 09:00 PM | Tuesday, May 02 2000 |

The results show how the `TimestampFormat` function can display values using different format parameters.

## Example - Changing the timestamp format of customer orders

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Customer`
  - `CustomerName`
  - `OrderTimestamp`

Load script

```
Example:
Load * inline [
OrderID, CustomerName, OrderTimestamp
1, Alice, 2024-02-20 11:00:00
2, Bob, 2024-03-01 15:30:00
3, Charlie, 2024-04-12 09:45:00
4, David, 2024-05-21 21:10:00
5, Eve, 2024-06-30 14:25:00
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `OrderID`
- `CustomerName`

Create the following measure:

- `=Timestamp(OrderTimestamp, 'WWWW, DD MMM YYYY hh:mm TT')`, to display the order timestamp in a format that shows the day of the week, the date, and the time.

Results table

| OrderID | CustomerName | Timestamp(OrderTimestamp, 'WWWW, DD MMM YYYY hh:mm TT') |
| --- | --- | --- |
| 1 | Alice | Tuesday, 20 Feb 2024 11:00 AM |
| 2 | Bob | Friday, 01 Mar 2024 03:30 PM |
| 3 | Charlie | Friday, 12 Apr 2024 09:45 AM |
| 4 | David | Tuesday, 21 May 2024 09:10 PM |
| 5 | Eve | Sunday, 30 Jun 2024 02:25 PM |

Using the `Timestamp` function, the timestamp data is now formatted to include the day of the week and the new format for the date and time.
