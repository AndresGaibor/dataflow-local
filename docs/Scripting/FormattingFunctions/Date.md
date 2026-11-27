---
title: "Date Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Date.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---

# Date Script and chart function

Expand/Collapse all

# Date Script and chart function

Date() formats an
expression as a date using the format set in the system variables in the data load script, or the operating system, or a format string, if supplied.

Syntax:

Date(number[, format])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| number | The number to be formatted. |
| format | String describing the format of the resulting string. If no format string is supplied, the date format set in the system [variables](#glossary-0 "Glossary term") in the [data load script](#glossary-1 "Glossary term") or the operating system is used. The Date function supports many format options for different date structures, for example:  ​DD/MM/YYYY: ​Day/Month/Year (for example, 15/02/2022)  ​MM-DD-YYYY: ​Month-Day-Year with hyphens (for example, 02-15-2022)  ​YYYY-MM-DD: ​Year-Month-Day, ISO format (for example, 2022-02-15)  ​D-MMM-YYYY: ​Day, short Month name, Year, with hyphens (for example, 15-Feb-2022)  ​MMMM YYYY: ​Long Month name and Year (for example, February 2022)  ​MM/YYYY: ​Month and Year (for example, 02/2022)  ​DD MMMM YYYY: ​Day, long Month name, and Year (for example, 15 February 2022) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Date( 35648 ) | Returns 97-08-06 when the DateFormat setting is YY-MM-DD. |
| Date( 35648, 'YY.MM.DD' ) | Returns 97.08.06 when the DateFormat setting is YY-MM-DD. |
| Date( '8/6/97', 'YY.MM.DD' ) | Returns NULL when the DateFormat setting is YY-MM-DD. |

## Example - Date fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - RowNo
  - InputDate
- The DateFormat variable, which uses the YY-MM-DD format.

Load script

```
SET DateFormat='YY-MM-DD';
Example:
Load * inline [
RowNo, InputDate
1, 35648
2, 35648.375
3, 8/6/97
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- RowNo
- InputDate

Create the following measures:

- =Date(InputDate), to view the value as a date that is formatted using the DateFormat variable settings.
- =Date(InputDate, 'DD.MM.YYYY'), to view the value as a date that is formatted using the format supplied in the function.
- =Date(InputDate, 'YY.MM.DD'), to view the value as a date that is formatted using the format supplied in the function.
- =Num(InputDate), to return the numeric value of the date.

Results table

| RowNo | InputDate | Date(InputDate) | Date(InputDate, 'DD.MM.YYYY') | Date(InputDate, 'YY.MM.DD') | Num(InputDate) |
| --- | --- | --- | --- | --- | --- |
| 1 | 35648 | 97-08-06 | 06.08.1997 | 97.08.06 | 35648 |
| 2 | 35648.375 | 97-08-06 | 06.08.1997 | 97.08.06 | 35648.375 |
| 3 | 8/6/97 | - | - | - | - |

The results show how the Date function can be used to display and format dates. In this example, the DateFormat is set as YY-MM-DD in the load script. The system is expecting the expression for the date to use this format. You can see that the value for InputDate in row 3 (8/6/97) does not follow this format, therefore the system does not recognize it as a date and returns NULL.

Change the DateFormat setting in the load script to SET DateFormat='M/D/YY'; and reload the data. The value in row 3 will now match the format that is expected. The system will recognize it as a valid date and format it accordingly. The following table shows the results with the new DateFormat setting.

Results table with variable statement Set DateFormat='M/D/YY'

| RowNo | InputDate | Date(InputDate) | Date(InputDate, 'DD.MM.YYYY') | Date(InputDate, 'YY.MM.DD') | Num(InputDate) |
| --- | --- | --- | --- | --- | --- |
| 1 | 35648 | 97-08-06 | 06.08.1997 | 97.08.06 | 35648 |
| 2 | 35648.375 | 97-08-06 | 06.08.1997 | 97.08.06 | 35648.375 |
| 3 | 35648 | 97-08-06 | 06.08.1997 | 97.08.06 | 35648.375 |

## Example - Date scenario

Chart expression

Overview

A dataset contains sales data that uses the date format MM-DD-YYYY. You want to use the date format DD/MM/YYYY.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - SalesDate
  - Amount
- The DateFormat variable, which uses the MM/DD/YYYY format.

Load script

```
SET DateFormat='MM/DD/YYYY';
Example:
Load * inline [
Customer, SalesDate, Amount
Customer A, 2/15/2024, 100008
Customer B, 9/30/2024, 12500
Customer C, 12/28/2024, 15000
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Date(SalesDate ,'DD/MM/YYYY') to view the value as a date that is formatted using the format supplied in the function.
- =Sum(Amount) to calculate the total value of the cost of sales.

Results table

| Customer | Date(SalesDate ,'DD/MM/YYYY') | Sum(Amount) |
| --- | --- | --- |
| Customer A | 15/02/2024 | 100008 |
| Customer B | 30/09/2024 | 12500 |
| Customer C | 28/12/2024 | 15000 |

Looking at the results, you can see that although the dates in the dataset used one format, the Date function allows you to present these dates in a different format.
