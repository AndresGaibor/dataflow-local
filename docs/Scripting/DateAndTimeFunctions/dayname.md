---
title: "dayname Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/dayname.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# dayname Script and chart function

This function returns
a value showing the date with an underlying numeric value corresponding
to a timestamp of the first millisecond of the day containing time.

Syntax:

DayName(time[, period\_no [, day\_start]])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| time | The timestamp to evaluate. |
| period\_no | period\_no is an integer, or expression that resolves to an integer, where the value 0 indicates the day that contains time. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | To specify that days do not starting at midnight, indicate an offset as a fraction of a day in day\_start. For example, 0.125 to denote 3:00 AM. |

Examples and results:

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Scripting examples

| Example | Result |
| --- | --- |
| dayname('25/01/2013 16:45:00') | Returns 25/01/2013. |
| dayname('25/01/2013 16:45:00', -1) | Returns 24/01/2013. |
| dayname('25/01/2013 16:45:00', 0, 0.5 ) | Returns 25/01/2013.  Displaying the full timestamp shows the underlying numeric value corresponds to '25/01/2013 12:00:00.000. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

In this example, the day name is created from the timestamp that marks the beginning of the day after each invoice date in the table.

TempTable:

LOAD RecNo() as InvID, \* Inline [

InvDate

28/03/2012

10/12/2012

5/2/2013

31/3/2013

19/5/2013

15/9/2013

11/12/2013

2/3/2014

14/5/2014

13/6/2014

7/7/2014

4/8/2014

];

InvoiceData:

LOAD \*,

DayName(InvDate, 1) AS DName

Resident TempTable;

Drop table TempTable;

The resulting table contains the original dates and a column with the return value of the dayname() function. You can display the full timestamp by specifying the formatting in the [properties](#glossary-0 "Glossary term")panel.

Results table

| InvDate | DName |
| --- | --- |
| 28/03/2012 | 29/03/2012 00:00:00 |
| 10/12/2012 | 11/12/2012 00:00:00 |
| 5/2/2013 | 07/02/2013 00:00:00 |
| 31/3/2013 | 01/04/2013 00:00:00 |
| 19/5/2013 | 20/05/2013 00:00:00 |
| 15/9/2013 | 16/09/2013 00:00:00 |
| 11/12/2013 | 12/12/2013 00:00:00 |
| 2/3/2014 | 03/03/2014 00:00:00 |
| 14/5/2014 | 15/05/2014 00:00:00 |
| 13/6/2014 | 14/06/2014 00:00:00 |
| 7/7/2014 | 08/07/2014 00:00:00 |
| 4/8/2014 | 05/08/2014 00:00:00 |
