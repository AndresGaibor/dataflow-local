---
title: "LongMonthNames"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
Expand/Collapse all

# LongMonthNames

The format defined replaces the long month names convention in the regional settings.

Syntax:

LongMonthNames

When modifying the [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-0 "Glossary term"), the `;` needs to be used to separate the individual values.

The following example of the LongMonthNames function defines month names in full:

Set LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December';

The `LongMonthNames` function is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*Date Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Date.htm) | Script function to return `DayNames`as [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-1 "Glossary term") values. |
| [*LongDayNames*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongDayNames.htm) | Long form values of `DayNames`. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 - System variables default

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-2 "Glossary term")of dates that is loaded into a table named `Transactions`.
- A `date` field.
- The default `LongMonthNames` definition.

Load script

```
SET LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December'; 
						
Transactions: 
Load 
date, 
Date(date,’MMMM’) as monthname, 
id, 
amount 
Inline  
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

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-3 "Glossary term"). Create a new table and add these fields as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-4 "Glossary term").

- date
- monthname

Create this [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-5 "Glossary term")

`=sum(amount)`

Results table

| date | monthname | sum(amount) |
| --- | --- | --- |
| 01/01/2022 | January | 1000.45 |
| 01/02/2022 | January | 2123.34 |
| 01/03/2022 | January | 4124.35 |
| 01/04/2022 | January | 2431.36 |
| 01/05/2022 | January | 4787.78 |
| 01/06/2022 | January | 2431.84 |
| 01/07/2022 | January | 2854.83 |
| 01/08/2022 | January | 3554.28 |
| 01/09/2022 | January | 3756.17 |
| 01/10/2022 | January | 3454.35 |

The default `LongMonthNames` definition is used. In the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm#glossary-6 "Glossary term"), to create a field called, `month`, the `Date` function is used with the `date` field as the first argument. The second argument in the function is the formatting `MMMM`.

Using this formatting Qlik Sense converts the values from the first argument into the corresponding full month name set in the variable `LongMonthNames`. In the results table, the field values of our created field `month` display this.

## Example 2 - Change system variable

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates that is loaded into a table named `Transactions`.
- A `date` field.
- The `LongMonthNames` variable that is modified to use the abbreviated days of the week in Spanish.

Load script

```
SET LongMonthNames='Enero;Febrero;Marzo;Abril;Mayo;Junio;Julio;Agosto;Septiembre;OctubreNoviembre;Diciembre'; 

Transactions: 
LOAD 
date, 
Date(date,'MMMM') as monthname, 
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

Load the data and open a sheet. Create a new table and add `sum(amount)` as a measure and these fields as dimensions:

- date
- monthname

Create this measure:

`=sum(amount)`

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

In the load script, the `LongMonthNames` variable is modified to list the months of the year in Spanish. Then, to create a field called, `monthname`, the`Date` function is used with the `date` field as the first argument. The second argument in the function is the formatting `MMMM`.

Using this formatting Qlik Sense converts the values from the first argument into the corresponding full month name set in the variable `LongMonthNames`. In the results table, the field values of our created field `monthname` display the month name written in Spanish.
