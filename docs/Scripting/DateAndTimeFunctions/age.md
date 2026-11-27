---
title: "age Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/age.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# age Script and chart function

The age function returns
the age at the time of timestamp
(in completed years) of somebody born on date\_of\_birth.

Syntax:

age(timestamp,
date\_of\_birth)

Can be an expression.

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The timestamp,or expression resolving to a timestamp, up to which to calculate the completed number of years. |
| date\_of\_birth | Date of birth of the person whose age is being calculated. Can be an expression. |

Examples and results:

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Scripting examples

| Example | Result |
| --- | --- |
| age('25/01/2014', '29/10/2012') | Returns 1. |
| age('29/10/2014', '29/10/2012') | Returns 2. |

Example:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Employees:

LOAD \* INLINE [

Member|DateOfBirth

John|28/03/1989

Linda|10/12/1990

Steve|5/2/1992

Birg|31/3/1993

Raj|19/5/1994

Prita|15/9/1994

Su|11/12/1994

Goran|2/3/1995

Sunny|14/5/1996

Ajoa|13/6/1996

Daphne|7/7/1998

Biffy|4/8/2000

] (delimiter is |);

AgeTable:

Load \*,

age('20/08/2015', DateOfBirth) As Age

Resident Employees;

Drop table Employees;

The resulting table shows the returned values of age for each of the records in the table.

Results table

| Member | DateOfBirth | Age |
| --- | --- | --- |
| John | 28/03/1989 | 26 |
| Linda | 10/12/1990 | 24 |
| Steve | 5/2/1992 | 23 |
| Birg | 31/3/1993 | 22 |
| Raj | 19/5/1994 | 21 |
| Prita | 15/9/1994 | 20 |
| Su | 11/12/1994 | 20 |
| Goran | 2/3/1995 | 20 |
| Sunny | 14/5/1996 | 19 |
| Ajoa | 13/6/1996 | 19 |
| Daphne | 7/7/1998 | 17 |
| Biffy | 4/8/2000 | 15 |
