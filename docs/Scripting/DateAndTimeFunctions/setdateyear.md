---
title: "setdateyear Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/setdateyear.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
# setdateyear Script and chart function

This function takes as input a timestamp and a year and updates the timestamp with the year specified in input.

Syntax:

setdateyear
(timestamp, year)

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| timestamp | A standard Qlik Sense timestamp (often just a date). |
| year | A four-digit year. |

Examples and results:

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Scripting examples

| Example | Result |
| --- | --- |
| `setdateyear ('29/10/2005', 2013)` | Returns '29/10/2013 |
| `setdateyear ('29/10/2005 04:26:14', 2013)` | Returns '29/10/2013 04:26:14'  To see the time part of the timestamp in a visualization, you must set the number formatting to Date and choose a value for Formatting that displays time values. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

SetYear:

Load \*,

SetDateYear(testdates, 2013) as NewYear

Inline [

testdates

1/11/2012

10/12/2012

1/5/2013

2/1/2013

19/5/2013

15/9/2013

11/12/2013

2/3/2014

14/5/2014

13/6/2014

7/7/2014

4/8/2014

];

The resulting table contains the original dates and a column in which the year has be set to 2013.

Results table

| testdates | NewYear |
| --- | --- |
| 1/11/2012 | 1/11/2013 |
| 10/12/2012 | 10/12/2013 |
| 2/1/2012 | 2/1/2013 |
| 1/5/2013 | 1/5/2013 |
| 19/5/2013 | 19/5/2013 |
| 15/9/2013 | 15/9/2013 |
| 11/12/2013 | 11/12/2013 |
| 2/3/2014 | 2/3/2013 |
| 14/5/2014 | 14/5/2013 |
| 13/6/2014 | 13/6/2013 |
| 7/7/2014 | 7/7/2013 |
| 4/8/2014 | 4/8/2013 |
