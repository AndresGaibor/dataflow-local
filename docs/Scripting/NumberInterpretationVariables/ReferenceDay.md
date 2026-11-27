---
title: "ReferenceDay"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/ReferenceDay.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# ReferenceDay

Expand/Collapse all

# ReferenceDay

The setting defines which day in January to set as reference day to define week 1. In other words, this setting prescribes how many days in week 1 must be dates within January.

Syntax:

ReferenceDay

ReferenceDay sets how many days are included in the first week of the year. ReferenceDay can be set to any value between 1 and 7. Any value outside of the 1-7 range is interpreted as the midpoint of the week (4), which is equivalent to ReferenceDay being set to 4.

If you do not select a value for the ReferenceDay setting, then the default value will show ReferenceDay=0 which will be interpreted as the midpoint of the week (4), as seen in the ReferenceDay values table below.

The ReferenceDay function is often used in combination with the following functions:

Related functions

| Variable | Interaction |
| --- | --- |
| [*BrokenWeeks*](BrokenWeeks.htm) | If the Qlik Sense application is operating with unbroken weeks, the ReferenceDay [variable](#glossary-1 "Glossary term") setting will be enforced. However, if broken weeks are being used, week 1 will begin on January 1 and terminate in conjunction with the FirstWeekDay variable setting and ignore the ReferenceDay flag. |
| [*FirstWeekDay*](FirstWeekDay.htm) | Integer that defines which day to use as the first day of the week. |

Qlik Sense allows the following values to be set for ReferenceDay:

ReferenceDay values

| Value | Reference day |
| --- | --- |
| 0 (default) | January 4 |
| 1 | January 1 |
| 2 | January 2 |
| 3 | January 3 |
| 4 | January 4 |
| 5 | January 5 |
| 6 | January 6 |
| 7 | January 7 |

In the following example the ReferenceDay = 3 defines January 3 as the reference day:

SET ReferenceDay=3; //(set January 3 as the reference day)

For more information about using inline loads, see [*Using inline loads to load data*](../inline-loads-qs.htm).

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Examples:

If you want ISO settings for weeks and week numbers, make sure to have the following in the script:

Set FirstWeekDay=0;
Set BrokenWeeks=0;
Set ReferenceDay=4; // Jan 4th is always in week 1

If you want US settings, make sure to have the following in the script:

Set FirstWeekDay=6;
Set BrokenWeeks=1;
Set ReferenceDay=1; // Jan 1st is always in week 1

## Example 1 - Load script using the default value; ReferenceDay=0

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The ReferenceDay variable that is set to 0.
- The BrokenWeeks variable that is set to 0 which forces the application to use unbroken weeks.
- A [dataset](#glossary-2 "Glossary term") of dates from the end of 2019 to the start of 2020.

Load script

```
SET BrokenWeeks = 0;
SET ReferenceDay = 0;

Sales:
LOAD
date,
sales,
week(date) as week,
weekday(date) as weekday
Inline [
date,sales
12/27/2019,5000
12/28/2019,6000
12/29/2019,7000
12/30/2019,4000
12/31/2019,3000
01/01/2020,6000
01/02/2020,3000
01/03/2020,6000
01/04/2020,8000
01/05/2020,5000
01/06/2020,7000
01/07/2020,3000
01/08/2020,5000
01/09/2020,9000
01/10/2020,5000
01/11/2020,7000
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- week
- weekday

Results table

| date | week | weekday |
| --- | --- | --- |
| 12/27/2019 | 52 | Fri |
| 12/28/2019 | 52 | Sat |
| 12/29/2019 | 1 | Sun |
| 12/30/2019 | 1 | Mon |
| 12/31/2019 | 1 | Tue |
| 01/01/2020 | 1 | Wed |
| 01/02/2020 | 1 | Thu |
| 01/03/2020 | 1 | Fri |
| 01/04/2020 | 1 | Sat |
| 01/05/2020 | 2 | Sun |
| 01/06/2020 | 2 | Mon |
| 01/07/2020 | 2 | Tue |
| 01/08/2020 | 2 | Wed |
| 01/09/2020 | 2 | Thu |
| 01/10/2020 | 2 | Fri |
| 01/11/2020 | 2 | Sat |

Week 52 concludes on Saturday, December 28. Because ReferenceDay requires January 4 to be included in week 1, week 1 therefore begins on December 29 and concludes on Saturday, January 4.

## Example - ReferenceDay variable set to 5

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The ReferenceDay variable that is set to 5.
- The BrokenWeeks variable that is set to 0 which forces the application to use unbroken weeks.
- A dataset of dates from the end of 2019 to the start of 2020.

Load script

```
SET BrokenWeeks = 0;
SET ReferenceDay = 5;

Sales:
LOAD
date,
sales,
week(date) as week,
weekday(date) as weekday
Inline [
date,sales
12/27/2019,5000
12/28/2019,6000
12/29/2019,7000
12/30/2019,4000
12/31/2019,3000
01/01/2020,6000
01/02/2020,3000
01/03/2020,6000
01/04/2020,8000
01/05/2020,5000
01/06/2020,7000
01/07/2020,3000
01/08/2020,5000
01/09/2020,9000
01/10/2020,5000
01/11/2020,7000
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- week
- weekday

Results table

| date | week | weekday |
| --- | --- | --- |
| 12/27/2019 | 52 | Fri |
| 12/28/2019 | 52 | Sat |
| 12/29/2019 | 53 | Sun |
| 12/30/2019 | 53 | Mon |
| 12/31/2019 | 53 | Tue |
| 01/01/2020 | 53 | Wed |
| 01/02/2020 | 53 | Thu |
| 01/03/2020 | 53 | Fri |
| 01/04/2020 | 53 | Sat |
| 01/05/2020 | 1 | Sun |
| 01/06/2020 | 1 | Mon |
| 01/07/2020 | 1 | Tue |
| 01/08/2020 | 1 | Wed |
| 01/09/2020 | 1 | Thu |
| 01/10/2020 | 1 | Fri |
| 01/11/2020 | 1 | Sat |

Week 52 concludes on Saturday, December 28. The BrokenWeeks variable forces the application to use unbroken weeks. The reference day value of 5 requires January 5 to be included in week 1.

However, this is eight days after the conclusion of week 52 of the previous year. Therefore, week 53 begins on December 29 and concludes on January 4. Week 1 begins on Sunday, January 5.
