---
title: "Date# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/date_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Date# Script and chart function

Expand/Collapse all

# Date# Script and chart function

Date# evaluates
an expression as a date in the format specified in the second argument, if supplied.

Syntax:

Date#(text[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String describing the format that should be used to interpret the text string. If omitted, the date format set in the system [variables](#glossary-0 "Glossary term") in the [data load script](#glossary-1 "Glossary term") or the operating system is used.  The Date# function supports many format options for different date structures, for example:  ​DD/MM/YYYY: ​Day/Month/Year (for example, 15/02/2022)  ​MM-DD-YYYY: ​Month-Day-Year with hyphens (for example, 02-15-2022)  ​YYYY-MM-DD: ​Year-Month-Day, ISO format (for example, 2022-02-15)  ​D-MMM-YYYY: ​Day, short Month name, Year, with hyphens (for example, 15-Feb-2022)  ​MMMM YYYY: ​Long Month name and Year (for example, February 2022)  ​MM/YYYY: ​Month and Year (for example, 02/2022)  ​DD MMMM YYYY: ​Day, long Month name, and Year (for example, 15 February 2022)  [*Descriptions for number and time formats*](../../Introduction/conventions-number-time-formats.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Date#('8/7/97') | Returns a valid date of 8/7/97 when the DateFormat setting is M/D/YY. |
| Date#('21.10.2023', 'DD.MM.YYYY' ) | Returns a valid date of 21.10.2023 when the date setting is DD.MM.YYYY. |
| Date#('21.10.2023') | Returns NULL when the DateFormat setting is M/D/YY. |

## Example - Date# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - StringDate
- The DateFormat variable, which uses the M/D/YY format.
- A preceding load that creates a new field called Date. The Date# and Num functions are used to convert the string to a date, and then return the value as a number.

Load script

```
SET DateFormat='M/D/YY';
Example:
Load *,
Num(Date#(StringDate, 'D/M/YYYY')) as Date
;
LOAD * INLINE [
StringDate
13/12/2024
31/1/23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- StringDate
- Date

Create the following measures:

- =Date(Date), to view the value as a date that is formatted using the date format variable in the load script.
- =IsNum(StringDate), to verify that the value is a string and not evaluated as a date because the date format of the field values do not match the system setting.

Results table

| StringDate | Date | Date(Date) | IsNum(StringDate) |
| --- | --- | --- | --- |
| 13/12/2024 | 45639 | 12/13/24 | 0 |
| 31/1/23 | 44957 | 1/31/23 | 0 |

The results show that the Date field in column 2, created by the preceding load, has converted the StringDate values to a date that is expressed as a number. The Date format function in column 3 recognizes the Date values as dates and formats them according to the DateFormat variable in the load script.

## Example - Date# scenario

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - BirthDate
- A preceding load that creates a new field called ParsedBirthDate.

Load script

```
Example:
Load *,
Date#(BirthDate, 'MM.DD.YYYY') as ParsedBirthDate;
Load * inline [
Customer, BirthDate
Customer A, 08.25.2022
Customer B, 08.25.2022
Customer C, 08.25.2022
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Customer
- BirthDate
- ParsedBirthDate

Create the following measure:

- =Date(ParsedBirthDate,'DD/MM/YYYY'), to view the value as a formatted date.

Results table

| Customer | BirthDate | ParsedBirthDate | Date(ParsedBirthDate, 'DD/MM/YYYY') |
| --- | --- | --- | --- |
| Customer A | 08.25.2022 | 08.25.2022 | 25/08/2022 |
| Customer B | 06.29.2022 | 06.29.2022 | 29/06/2022 |
| Customer C | 05.31.2022 | 05.31.2022 | 31/05/2022 |

In this example we can see that in column 2, the BirthDate field is treated as text by the system. The Date# function used in the preceding load converts BirthDate to a recognizable date in column 3, ParsedBirthDate. The Date format function in column 4 can then display the ParsedBirthDate values in the format DD/MM/YYYY.
