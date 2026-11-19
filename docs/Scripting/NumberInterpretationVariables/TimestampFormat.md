---
title: "TimestampFormat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimestampFormat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
# TimestampFormat

The format defined replaces the date and time formats of the operating
system (regional
settings).

Syntax:

TimestampFormat

Example:

The following examples use 1983-12-14T13:15:30Z as timestamp data to show the results of different SET TimestampFormat statements. The date format used is YYYYMMDD and the time format is h:mm:ss TT. The date format is specified in the SET DateFormat statement and the time format is specified in the SET TimeFormat statement, at the top of the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimestampFormat.htm#glossary-0 "Glossary term").

Results

| Example | Result |
| --- | --- |
| SET TimestampFormat='YYYYMMDD'; | 19831214 |
| SET TimestampFormat='M/D/YY hh:mm:ss[.fff]'; | 12/14/83 13:15:30 |
| SET TimestampFormat='DD/MM/YYYY hh:mm:ss[.fff]'; | 14/12/1983 13:15:30 |
| SET TimestampFormat='DD/MM/YYYY hh:mm:ss[.fff] TT'; | 14/12/1983 1:15:30 PM |
| SET TimestampFormat='YYYY-MM-DD hh:mm:ss[.fff] TT'; | 1983-12-14 01:15:30 |

## Examples: Load script

Example: Load script

In the first load script SET TimestampFormat='DD/MM/YYYY h:mm:ss[.fff] TT' is used. In the second load script the timestamp format is changed to SET TimestampFormat='MM/DD/YYYY hh:mm:ss[.fff]'. The different results show how the SET TimeFormat statement works with different time data formats.

The table below shows the data set that is used in the load scripts that follow. The second column of the table shows the format of each timestamp in the data set. The first five timestamps follow ISO 8601 rules but the sixth does not.

Data set

Table showing the time data used and the format for each timestamp in the data set.

| transaction\_timestamp | time data format |
| --- | --- |
| 2018-08-30 | YYYY-MM-DD |
| 20180830T193614.857 | YYYYMMDDhhmmss.sss |
| 20180830T193614.857+0200 | YYYYMMDDhhmmss.sss±hhmm |
| 2018-09-16T12:30-02:00 | YYYY-MM-DDhh:mm±hh:mm |
| 2018-09-16T13:15:30Z | YYYY-MM-DDhh:mmZ |
| 9/30/18 19:36:14 | M/D/YY hh:mm:ss |

In the **[Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimestampFormat.htm#glossary-1 "Glossary term")**, create a new section, and then add the example script and run it. Then add, at least, the fields listed in the results column to a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimestampFormat.htm#glossary-2 "Glossary term") in your application to see the result.

Load script

```
SET FirstWeekDay=0;
SET BrokenWeeks=1;
SET ReferenceDay=0;
SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';
SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';
SET DateFormat='YYYYMMDD';
SET TimestampFormat='DD/MM/YYYY h:mm:ss[.fff] TT';
 
Transactions:
Load
*,
Timestamp(transaction_timestamp, 'YYYY-MM-DD hh:mm:ss[.fff]') as LogTimestamp
;
 
Load * Inline [
transaction_id, transaction_timestamp, transaction_amount, transaction_quantity, discount, customer_id, size, color_code
3750, 2018-08-30, 12423.56, 23, 0,2038593, L, Red
3751, 20180830T193614.857, 5356.31, 6, 0.1, 203521, m, orange
3752, 20180830T193614.857+0200, 15.75, 1, 0.22, 5646471, S, blue
3753, 2018-09-16T12:30-02:00, 1251, 7, 0, 3036491, l, Black
3754, 2018-09-16T13:15:30Z, 21484.21, 1356, 75, 049681, xs, Red
3755, 9/30/18 19:36:14, -59.18, 2, 0.333333333333333, 2038593, M, Blue
];
```

Results

Qlik Sense table showing results of the TimestampFormat interpretation variable being used in the load script. The last timestamp in the data set does not return a correct date.

| transaction\_id | transaction\_timestamp | LogTimeStamp |
| --- | --- | --- |
| 3750 | 2018-08-30 | 2018-08-30 00:00:00 |
| 3751 | 20180830T193614.857 | 2018-08-30 19:36:14 |
| 3752 | 20180830T193614.857+0200 | 2018-08-30 17:36:14 |
| 3753 | 2018-09-16T12:30-02:00 | 2018-09-16 14:30:00 |
| 3754 | 2018-09-16T13:15:30Z | 2018-09-16 13:15:30 |
| 3755 | 9/30/18 19:36:14 | - |

The next load script uses the same data set. However, it uses SET TimestampFormat='MM/DD/YYYY hh:mm:ss[.fff]' to match the non-ISO 8601 format of the sixth timestamp.

In the **Data load editor**, replace the previous example script with the one below and run it. Then add, at least, the fields listed in the results column to a sheet in your application to see the result.

Load script

```
SET FirstWeekDay=0;
SET BrokenWeeks=1;
SET ReferenceDay=0;
SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';
SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';
SET DateFormat='YYYYMMDD';
SET TimestampFormat='MM/DD/YYYY hh:mm:ss[.fff]';
 
Transactions:
Load
*,
Timestamp(transaction_timestamp, 'YYYY-MM-DD hh:mm:ss[.fff]') as LogTimestamp
;
 
Load * Inline [
transaction_id, transaction_timestamp, transaction_amount, transaction_quantity, discount, customer_id, size, color_code
3750, 2018-08-30, 12423.56, 23, 0,2038593, L, Red
3751, 20180830T193614.857, 5356.31, 6, 0.1, 203521, m, orange
3752, 20180830T193614.857+0200, 15.75, 1, 0.22, 5646471, S, blue
3753, 2018-09-16T12:30-02:00, 1251, 7, 0, 3036491, l, Black
3754, 2018-09-16T13:15:30Z, 21484.21, 1356, 75, 049681, xs, Red
3755, 9/30/18 19:36:14, -59.18, 2, 0.333333333333333, 2038593, M, Blue
];
```

Results

Qlik Sense table showing results of the TimestampFormat interpretation variable being used in the load script.

| transaction\_id | transaction\_timestamp | LogTimeStamp |
| --- | --- | --- |
| 3750 | 2018-08-30 | 2018-08-30 00:00:00 |
| 3751 | 20180830T193614.857 | 2018-08-30 19:36:14 |
| 3752 | 20180830T193614.857+0200 | 2018-08-30 17:36:14 |
| 3753 | 2018-09-16T12:30-02:00 | 2018-09-16 14:30:00 |
| 3754 | 2018-09-16T13:15:30Z | 2018-09-16 13:15:30 |
| 3755 | 9/30/18 19:36:14 | 2018-09-16 19:36:14 |
