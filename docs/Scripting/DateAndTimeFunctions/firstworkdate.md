---
title: "firstworkdate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/firstworkdate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# firstworkdate Script and chart function

The firstworkdate function returns
the latest starting date to achieve no\_of\_workdays
(Monday-Friday) ending no later than end\_date taking into account any
optionally listed holidays. end\_date
and holiday should
be valid dates or timestamps.

Syntax:

firstworkdate(end\_date, no\_of\_workdays {, holiday} )

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| end\_date | The timestamp of end date to evaluate. |
| no\_of\_workdays | The number of working days to achieve. |
| holiday | Holiday periods to exclude from working days. A holiday is stated as a string constant date. You can specify multiple holiday dates, separated by commas.  Example:  '12/25/2013', '12/26/2013', '12/31/2013', '01/01/2014' |

Examples and results:

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Scripting examples

| Example | Result |
| --- | --- |
| firstworkdate ('29/12/2014', 9) | Returns '17/12/2014. |
| firstworkdate ('29/12/2014', 9, '25/12/2014', '26/12/2014') | Returns 15/12/2014 because a holiday period of two days is taken into account. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

ProjectTable:

LOAD \*, recno() as InvID, INLINE [

EndDate

28/03/2015

10/12/2015

5/2/2016

31/3/2016

19/5/2016

15/9/2016

] ;

NrDays:

Load \*,

FirstWorkDate(EndDate,120) As StartDate

Resident ProjectTable;

Drop table ProjectTable;

The resulting table shows the returned values of FirstWorkDate for each of the records in the table.

Results table

| InvID | EndDate | StartDate |
| --- | --- | --- |
| 1 | 28/03/2015 | 13/10/2014 |
| 2 | 10/12/2015 | 26/06/2015 |
| 3 | 5/2/2016 | 24/08/2015 |
| 4 | 31/3/2016 | 16/10/2015 |
| 5 | 19/5/2016 | 04/12/2015 |
| 6 | 15/9/2016 | 01/04/2016 |
