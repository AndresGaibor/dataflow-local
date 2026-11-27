---
title: "LongDayNames"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongDayNames.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# LongDayNames

Expand/Collapse all

# LongDayNames

The format defined replaces the long weekday names convention in the regional settings.

Syntax:

LongDayNames

The following example of the LongDayNames function defines day names in full:

Set
LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';

When modifying the [variable](#glossary-0 "Glossary term"), a semicolon ; is required to separate the individual values.

The LongDayNames function can be used in combination with the [*Date Script and chart function*](../FormattingFunctions/Date.htm) function which returns DayNames as field values.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - System variable default

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") with dates, which will be loaded into a table named, Transactions.
- A date [field](#glossary-2 "Glossary term").
- The default LongDayNames definition.

Load script

```
SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';

Transactions:
LOAD
date,
Date(date,'WWWW') as dayname,
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
- dayname

Create this [measure](#glossary-3 "Glossary term"):

=sum(amount)

Results table

| date | dayname | =sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Saturday | 1000 |
| 02/01/2022 | Tuesday | 2123 |
| 03/01/2022 | Tuesday | 4124 |
| 04/01/2022 | Friday | 2431 |

In the [load script](#glossary-4 "Glossary term"), to create a field called, dayname, the Date function is used with the date field as the first argument. The second argument in the function is the formatting WWWW.

Using this formatting converts the values from the first argument into the corresponding full day name that is set in the variable LongDayNames. In the results table, the field values of our created field dayname display this.

## Example 2 – Change system variable

Load script and results

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the load script below to a new tab.

The same dataset and scenario from the first example are used. However, at the start of the script, the LongDayNames definition is modified to use the days of the week in Spanish.

Load Script

```
SET LongDayNames='Lunes;Martes;Miércoles;Jueves;Viernes;Sábado;Domingo';

Transactions:
LOAD
date,
Date(date,'WWWW') as dayname,
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
- dayname

Create this measure:

=sum(amount)

Results table

| date | dayname | =sum(amount) |
| --- | --- | --- |
| 01/01/2022 | Sábado | 1000 |
| 02/01/2022 | Martes | 2123 |
| 03/01/2022 | Martes | 4124 |
| 04/01/2022 | Viernes | 2431 |

In the load script, the LongDayNames variable is modified to list the days of the week in Spanish.

Then, you create a field called, dayname, which is the Date function used with the date field as the first argument.

The second argument in the function is the formatting WWWW. By using this formatting Qlik Sense converts the values from the first argument into the corresponding full day name set in the variable LongDayNames.

In the results table, the field values of our created field dayname displays the days of the week written in Spanish and in full.
