---
title: "Date and time interpretation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/date-time-interpretation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Data types"]
---

# Date and time interpretation

Qlik Sense stores each date, time, and timestamp found in data as a date serial number. The date serial number is used for dates, times and timestamps and in arithmetic calculations based on date and time entities. Dates and times can thus be added and subtracted, intervals can be compared, and so on.

The date serial number is the (real valued) number of days passed since December 30, 1899, that is, the Qlik Sense format is identical to the 1900 date system used by Microsoft Excel and other programs, in the range between March 1, 1900 and February 28, 2100. For example, 33857 corresponds to September 10, 1992. Outside this range, Qlik Sense uses the same date system extended to the Gregorian calendar.

Information noteIf the field contains dates before January 1, 1980, the field will not contain the $date or $timestamp system tags. The field should still be recognized as a date field by Qlik Sense, but if you need the tags you can add them manually in the data load script with the Tag statement. See [*Tag*](ScriptRegularStatements/Tag.htm) for more information.

The serial number for times is a number between 0 and 1. The serial number 0.00000 corresponds to 00:00:00, whereas 0.99999 corresponds to 23:59:59. Mixed numbers indicate the date and time: the serial number 2.5 represents January 1, 1900 at 12:00 noon.

The data is, however, displayed according to the format of the string. By default, the settings made in the Control Panel are used. It is also possible to set the format of the data by using the number interpretation [variables](#glossary-0 "Glossary term") in the script or with the help of a formatting function. Lastly, it is also possible to reformat the data in the [properties](#glossary-1 "Glossary term") sheet of the [sheet](#glossary-2 "Glossary term") object.

To learn more about number interpretation variables, see [*Number interpretation variables*](NumberInterpretationVariables/number-interpretation-variables.htm).

To learn more about formatting functions, see [*Formatting functions*](FormattingFunctions/formatting-functions.htm).

Example 1:

- 1997-08-06 is stored as 35648
- 09:00 is stored as 0.375
- 1997-08-06 09:00 is stored as 35648.375

and the other way around:

- 35648  with number format 'D/M/YY' is shown as  6/8/97
- 0.375 with number format 'hh.mm' is shown as 09.00

Qlik Sense follows a set of rules to try to interpret dates, times, and other data types. The final result, however, will be affected by a number of factors as described here.

Example 2:

These examples assume the following default settings:

- Number decimal separator:
- Short date format: YY-MM-DD
- Time format: hh:mm

The following table shows the different representations when data is read into Qlik Sense without the special interpretation function in the script:

Table when data is read without the special interpretation function in the script

| Source data | Qlik Sense default interpretation | 'YYYY-MM-DD' date format | 'MM/DD/YYYY' date format | 'hh:mm' time format | '# ##0.00' number format |
| --- | --- | --- | --- | --- | --- |
| 0.375 | 0.375 | 1899-12-30 | 12/30/1899 | 09:00 | 0.38 |
| 33857 | 33857 | 1992-09-10 | 09/10/1992 | 00:00 | 33 857.00 |
| 97-08-06 | 97-08-06 | 1997-08-06 | 08/06/1997 | 00:00 | 35 648.00 |
| 970806 | 970806 | 4557-12-21 | 12/21/4557 | 00:00 | 970 806.00 |
| 8/6/97 | 8/6/97 | 8/6/97 | 8/6/97 | 8/6/97 | 8/6/97 |

The following table shows the different representations when data is read into Qlik Sense using the date#( A, 'M/D/YY') interpretation function in the script:

Table when using the date#( A, 'M/D/YY') interpretation function in the script

| Source data | Qlik Sense default interpretation | 'YYYY-MM-DD' date format | 'MM/DD/YYYY' date format | 'hh:mm' time format | '# ##0.00' number format |
| --- | --- | --- | --- | --- | --- |
| 0.375 | 0.375 | 0.375 | 0.375 | 0.375 | 0.375 |
| 33857 | 33857 | 33857 | 33857 | 33857 | 33857 |
| 97-08-06 | 97-08-06 | 97-08-06 | 97-08-06 | 97-08-06 | 97-08-06 |
| 970806 | 970806 | 970806 | 970806 | 970806 | 970806 |
| 8/6/97 | 8/6/97 | 1997-08-06 | 08/06/1997 | 00:00 | 35 648.00 |
