---
title: "FirstWeekDay"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/FirstWeekDay.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
Expand/Collapse all

# FirstWeekDay

Integer that defines which day to use as the first day of the week.

Syntax:

FirstWeekDay

Monday is the first day of the week according to ISO 8601, the international standard for the representation of dates and times. Monday is also used as the first day of the week in a number of countries, for example on the UK, France, Germany and Sweden.

But in other countries, like in the United States and Canada, Sunday is considered to be the start of the week.

In Qlik Sense, the regional settings are fetched when the application is created, and the corresponding settings are stored in the script as environment [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/FirstWeekDay.htm#glossary-1 "Glossary term").

A North American application developer often gets `Set FirstWeekDay=6;` in the script, corresponding to Sunday. A European application developer often gets `Set FirstWeekDay=0;` in the script, corresponding to Monday.

Values that can be set for FirstWeekDay

| Value | Day |
| --- | --- |
| 0 | Monday |
| 1 | Tuesday |
| 2 | Wednesday |
| 3 | Thursday |
| 4 | Friday |
| 5 | Saturday |
| 6 | Sunday |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Examples:

If you want ISO settings for weeks and week numbers, make sure to have the following in the script:

Set FirstWeekDay=0; // Monday as first week day
Set BrokenWeeks=0;
Set ReferenceDay=4;

If you want US settings, make sure to have the following in the script:

Set FirstWeekDay=6; // Sunday as first week day
Set BrokenWeeks=1;
Set ReferenceDay=1;

## Example 1 – Using default value (script)

Load script and results

Overview

Open the Data load editor and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/FirstWeekDay.htm#glossary-2 "Glossary term") below to a new tab.

In this example, the load script uses the default Qlik Sense system variable value, `FirstWeekDay=6`. This data contains data for the first 14 days in 2020.

Load script

```
// Example 1: Load Script using the default value of FirstWeekDay=6, i.e. Sunday

SET FirstWeekDay = 6;

Sales:
LOAD
	 date,
	 sales,
	 week(date) as week,
	 weekday(date) as weekday 
Inline [
date,sales
01/01/2021,6000
01/02/2021,3000
01/03/2021,6000
01/04/2021,8000
01/05/2021,5000
01/06/2020,7000
01/07/2020,3000
01/08/2020,5000
01/09/2020,9000
01/10/2020,5000
01/11/2020,7000
01/12/2020,7000
01/13/2020,7000
01/14/2020,7000
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `week`
- `weekday`

Results table

| Date | week | weekday |
| --- | --- | --- |
| 01/01/2021 | 1 | Wed |
| 01/02/2021 | 1 | Thu |
| 01/03/2021 | 1 | Fri |
| 01/04/2021 | 1 | Sat |
| 01/05/2021 | 2 | Sun |
| 01/06/2020 | 2 | Mon |
| 01/07/2020 | 2 | Tue |
| 01/08/2020 | 2 | Wed |
| 01/09/2020 | 2 | Thu |
| 01/10/2020 | 2 | Fri |
| 01/11/2020 | 2 | Sat |
| 01/12/2020 | 3 | Sun |
| 01/13/2020 | 3 | Mon |
| 01/14/2020 | 3 | Tue |

Because the default settings are being used, the `FirstWeekDay` system variable is set to 6. In the results table, each new week can be seen beginning on Sunday (the 5th and 12th of January).

## Example 2 – Changing the FirstWeekDay variable (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

In this example, the data contains the first 14 days in 2020. At the start of the script, we set the `FirstWeekDay` variable to 3.

Load script

```
// Example 2: Load Script setting the value of FirstWeekDay=3, i.e. Thursday

SET FirstWeekDay = 3;

Sales:
LOAD
	date,
	sales,
	week(date) as week,
	weekday(date) as weekday 
Inline [
date,sales
01/01/2021,6000
01/02/2021,3000
01/03/2021,6000
01/04/2021,8000
01/05/2021,5000
01/06/2020,7000
01/07/2020,3000
01/08/2020,5000
01/09/2020,9000
01/10/2020,5000
01/11/2020,7000
01/12/2020,7000
01/13/2020,7000
01/14/2020,7000
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `week`
- `weekday`

Results table

| Date | week | weekday |
| --- | --- | --- |
| 01/01/2021 | 52 | Wed |
| 01/02/2021 | 1 | Thu |
| 01/03/2021 | 1 | Fri |
| 01/04/2021 | 1 | Sat |
| 01/05/2021 | 1 | Sun |
| 01/06/2020 | 1 | Mon |
| 01/07/2020 | 1 | Tue |
| 01/08/2020 | 1 | Wed |
| 01/09/2020 | 2 | Thu |
| 01/10/2020 | 2 | Fri |
| 01/11/2020 | 2 | Sat |
| 01/12/2020 | 2 | Sun |
| 01/13/2020 | 2 | Mon |
| 01/14/2020 | 2 | Tue |

Because the `FirstWeekDay` system variable is set to 3, the first day of each week will be a Thursday. In the results table, each new week can be seen beginning on Thursday (the 2nd and 9th of January).
