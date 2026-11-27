---
title: "setdateyearmonth Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/setdateyearmonth.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# setdateyearmonth Script and chart function

This function takes as input a timestamp, a month and a year and updates the timestamp with the year and the month specified in input. .

Syntax:

SetDateYearMonth
(timestamp, year, month)

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| timestamp | A standard Qlik Sense timestamp (often just a date). |
| year | A four-digit year. |
| month | A one or two-digit month. |

Examples and results:

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Scripting examples

| Example | Result |
| --- | --- |
| setdateyearmonth ('29/10/2005', 2013, 3) | Returns '29/03/2013 |
| setdateyearmonth ('29/10/2005 04:26:14', 2013, 3) | Returns '29/03/2013 04:26:14'   To see the time part of the timestamp in a visualization, you must set the number formatting to Date and choose a value for Formatting that displays time values. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

SetYearMonth:

Load \*,

SetDateYearMonth(testdates, 2013,3) as NewYearMonth

Inline [

testdates

1/11/2012

10/12/2012

2/1/2013

19/5/2013

15/9/2013

11/12/2013

14/5/2014

13/6/2014

7/7/2014

4/8/2014

];

The resulting table contains the original dates and a column in which the year has be set to 2013.

Results table

| testdates | NewYearMonth |
| --- | --- |
| 1/11/2012 | 1/3/2013 |
| 10/12/2012 | 10/3/2013 |
| 2/1/2012 | 2/3/2013 |
| 19/5/2013 | 19/3/2013 |
| 15/9/2013 | 15/3/2013 |
| 11/12/2013 | 11/3/2013 |
| 14/5/2014 | 14/3/2013 |
| 13/6/2014 | 13/3/2013 |
| 7/7/2014 | 7/3/2013 |
| 4/8/2014 | 4/3/2013 |
