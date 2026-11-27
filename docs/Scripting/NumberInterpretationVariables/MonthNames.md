---
title: "MonthNames"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MonthNames.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# MonthNames

Expand/Collapse all

# MonthNames

The format defined replaces the month names convention of the regional settings.

Syntax:

MonthNames

When modifying the [variable](#glossary-0 "Glossary term"), the ; needs to be used to separate the individual values.

Function examples

| Example | Results |
| --- | --- |
|
|  |
| Set MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec'; | This use of the MonthNames function defines month names in English and their abbreviated form. |
| Set MonthNames='Enero;Feb;Marzo;Abr;Mayo;Jun;Jul;Agosto;Set;Oct;Nov;Dic'; | This use of the MonthNames function defines month names in Spanish and their abbreviated form. |

The MonthNames function can be used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*month Script and chart function*](../DateAndTimeFunctions/month.htm) | Script function to return values defined in MonthNames as [field](#glossary-1 "Glossary term") values |
| [*Date Script and chart function*](../FormattingFunctions/Date.htm) | Script function to return values defined in MonthNames as field values based on a formatting argument provided |
| [*LongMonthNames*](LongMonthNames.htm) | Long form values of MonthNames |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – System variables default

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") of dates that is loaded into a table named Transactions.
- A date field.
- The default MonthNames definition.

Load script

```
SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';

Transactions:
LOAD
date,
Month(date) as monthname,
id,
amount
INLINE
[
date,id,amount
01/01/2022,1,1000.45
01/02/2022,2,2123.34
01/03/2022,3,4124.35
01/04/2022,4,2431.36
01/05/2022,5,4787.78
01/06/2022,6,2431.84
01/07/2022,7,2854.83
01/08/2022,8,3554.28
01/09/2022,9,3756.17
01/10/2022,10,3454.35
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- monthname

Create this [measure](#glossary-3 "Glossary term"):

=sum(amount)

Results table

| date | monthname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Jan | 1000.45 |
| 01/02/2022 | Jan | 2123.34 |
| 01/03/2022 | Jan | 4124.35 |
| 01/04/2022 | Jan | 2431.36 |
| 01/05/2022 | Jan | 4787.78 |
| 01/06/2022 | Jan | 2431.84 |
| 01/07/2022 | Jan | 2854.83 |
| 01/08/2022 | Jan | 3554.28 |
| 01/09/2022 | Jan | 3756.17 |
| 01/10/2022 | Jan | 3454.35 |

The default MonthNames definition is used. In the [load script](#glossary-4 "Glossary term"), the Month function is used with the date field as the provided argument.

In the results table, the output of this Month function displays the months of the year in the format of the MonthNames definition.

## Example 2 - Change system variable

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates that is loaded into a table named Transactions.
- A date field.
- The MonthNames variable that is modified to use the abbreviated months in Spanish.

Load script

```
Set MonthNames='Enero;Feb;Marzo;Abr;Mayo;Jun;Jul;Agosto;Set;Oct;Nov;Dic';

Transactions:
LOAD
date,
month(date) as month,
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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- monthname

Create this measure:

=sum(amount)

Results table

| date | monthname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Enero | 1000.45 |
| 01/02/2022 | Enero | 2123.34 |
| 01/03/2022 | Enero | 4124.35 |
| 01/04/2022 | Enero | 2431.36 |
| 01/05/2022 | Enero | 4787.78 |
| 01/06/2022 | Enero | 2431.84 |
| 01/07/2022 | Enero | 2854.83 |
| 01/08/2022 | Enero | 3554.28 |
| 01/09/2022 | Enero | 3756.17 |
| 01/10/2022 | Enero | 3454.35 |

In the load script, first the MonthNames variable is modified to list the months of the year abbreviated in Spanish. The Month function is used with the date field as the provided argument.

In the results table, the output of this Month function displays the months of the year in the format of the MonthNames definition.

It is important to remember that if the language for the MonthNames variable is modified like it has been in this example, the LongMonthNames variable would still contain the months of the year in English. The LongMonthNames variable would have to be modified if both [variables](#glossary-5 "Glossary term") are used in the application.

## Example 3 – Date function

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates that is loaded into a table named Transactions.
- A date field.
- The default MonthNames definition.

Load script

```
SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';

Transactions:
LOAD
date,
Month(date, ’MMM’) as monthname,
id,
amount
INLINE
[
date,id,amount
01/01/2022,1,1000.45
01/02/2022,2,2123.34
01/03/2022,3,4124.35
01/04/2022,4,2431.36
01/05/2022,5,4787.78
01/06/2022,6,2431.84
01/07/2022,7,2854.83
01/08/2022,8,3554.28
01/09/2022,9,3756.17
01/10/2022,10,3454.35
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- monthname

Create this measure:

=sum(amount)

Results table

| date | monthname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Jan | 1000.45 |
| 01/02/2022 | Jan | 2123.34 |
| 01/03/2022 | Jan | 4124.35 |
| 01/04/2022 | Jan | 2431.36 |
| 01/05/2022 | Jan | 4787.78 |
| 01/06/2022 | Jan | 2431.84 |
| 01/07/2022 | Jan | 2854.83 |
| 01/08/2022 | Jan | 3554.28 |
| 01/09/2022 | Jan | 3756.17 |
| 01/10/2022 | Jan | 3454.35 |

The default MonthNames definition is used. In the load script, the Date function is used with the date field as the first argument. The second argument is MMM.

Using this formatting Qlik Sense converts the values from the first argument into the corresponding month name set in the variable MonthNames. In the results table, the field values of our created field month display this.
