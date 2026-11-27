---
title: "DayNames"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DayNames.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# DayNames

Expand/Collapse all

# DayNames

The format defined replaces the weekday names convention set by your regional settings.

Syntax:

DayNames

When modifying the [variable](#glossary-0 "Glossary term"), a semicolon ; is required to separate the individual values.

DayName Function examples

| Function example | Result definition |
| --- | --- |
| Set DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun'; | This use of the DayNames function defines day names in their abbreviated form. |
| Set DayNames='M;Tu;W;Th;F;Sa;Su'; | This use of the DayNames function defines day names by their first letters. |

The DayNames function is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*weekday Script and chart function*](../DateAndTimeFunctions/weekday.htm) | Script function to return DayNames as [field](#glossary-1 "Glossary term") values . |
| [*Date Script and chart function*](../FormattingFunctions/Date.htm) | Script function to return DayNames as field values. |
| [*LongDayNames*](LongDayNames.htm) | Long form values of DayNames. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - System variables default

Load script and results

Overview

In this example, the dates in the [dataset](#glossary-2 "Glossary term") are set in the MM/DD/YYYY format.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset with dates, which will be loaded into a table named, Transactions.
- A date field.
- The default DayNames definition.

Load script

```
SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';

Transactions:
LOAD
date,
WeekDay(date) as dayname,
id,
amount
INLINE
[
date,id,amount
01/01/2022,1,1000
02/01/2022,2,2123
03/01/2022,3,4124
04/01/2022,4,2431
];
```

Results

Load the data and open a [sheet](#glossary-3 "Glossary term"). Create a new table and add these fields as [dimensions](#glossary-4 "Glossary term"):

- date
- dayname

Create this measure:

sum(amount)

Results table

| date | dayname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Sat | 1000 |
| 02/01/2022 | Tue | 2123 |
| 03/01/2022 | Tue | 4124 |
| 04/01/2022 | Fri | 2431 |

In the [load script](#glossary-5 "Glossary term"), the WeekDay function is used with the date field as the provided argument. In the results table, the output of this WeekDay function displays the days of the week in the format of the DayNames definition.

## Example 2 - Change system variable

Load script and results

Overview

Open the [Data load editor](#glossary-6 "Glossary term") and add the load script below to a new tab.
The same dataset and scenario from the first example are used.

However, at the start of the script, the DayNames definition is modified to use the abbreviated days of the week in Afrikaans.

Load script

```
SET DayNames='Ma;Di;Wo;Do;Vr;Sa;So';

Transactions:
Load
date,
WeekDay(date) as dayname,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,1000
02/01/2022,2,2123
03/01/2022,3,4124
04/01/2022,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- dayname

Create this measure:

sum(amount)

Results table

| date | dayname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Sa | 1000 |
| 02/01/2022 | Di | 2123 |
| 03/01/2022 | Di | 4124 |
| 04/01/2022 | Vr | 2431 |

In the results table, the output of this WeekDay function displays the days of the week in the format of the DayNames definition.

It is important to remember that if the language for the DayNames is modified like it has been in this example, the LongDayNames would still contain the days of the week in English. This would need to be modified as well if both [variables](#glossary-7 "Glossary term") are used in the application.

## Example 3 – Date function

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset with dates, which will be loaded into a table named, Transactions.
- A date field.
- The default DayNames definition.

Load script

```
SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';

Transactions:
Load
date,
Date(date,'WWW') as dayname,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,1000
02/01/2022,2,2123
03/01/2022,3,4124
04/01/2022,4,2431
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- dayname

Create this measure:

sum(amount)

Results table

| date | dayname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Sat | 1000 |
| 02/01/2022 | Tue | 2123 |
| 03/01/2022 | Tue | 4124 |
| 04/01/2022 | Fri | 2431 |

The default DayNamesdefinition is used. In the load script, the Date function is used with the date field as the first argument. The second argument is WWW. This formatting converts the result into the values stored in the DayNames definition. This is displayed in the output of the results table.
