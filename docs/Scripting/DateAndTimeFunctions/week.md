---
title: "week Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/week.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# week Script and chart function

Expand/Collapse all

# week Script and chart function

This function returns an integer representing the week number corresponding to the date entered.

Syntax:

week(timestamp [, first\_week\_day [, broken\_weeks [, reference\_day]]])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of [variable](#glossary-0 "Glossary term") FirstWeekDay is used.  The possible values first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm). |
| broken\_weeks | If you don't specify broken\_weeks, the value of variable BrokenWeeks will be used to define if weeks are broken or not.  For more information about the system variable, see [*BrokenWeeks*](../NumberInterpretationVariables/BrokenWeeks.htm) |
| reference\_day | If you don't specify reference\_day, the value of variable ReferenceDay will be used to define which day in January to set as reference day to define week 1. By default, Qlik Sense functions use 4 as the reference day. This means that week 1 must contain January 4, or put differently, that week 1 must always have at least 4 days in January.  For more information about the system variable, see [*ReferenceDay*](../NumberInterpretationVariables/ReferenceDay.htm) |

The week() function determines which week the date falls into and returns the week number.

 In Qlik Sense, the regional settings are fetched when the application is created, and the corresponding settings are stored in the script as environment [variables](#glossary-2 "Glossary term"). These are used to determine the week number.

This means that most European application developers gets the following environment variables, corresponding to the ISO 8601 definition:

Set FirstWeekDay =0; // Monday as first week day
Set BrokenWeeks =0; // Use unbroken weeks
Set ReferenceDay =4; // Jan 4th is always in week 1

A North American application developer often gets the following environment variables:

Set FirstWeekDay =6; // Sunday as first week day
Set BrokenWeeks =1; // Use broken weeks
Set ReferenceDay =1; // Jan 1st is always in week 1

The first day of the week is determined by the FirstWeekDay system variable. You can also change the first day of the week by using the first\_week\_day argument in the week() function.

If your application uses broken weeks, the week number count begins on January 1 and ends on the day prior to the FirstWeekDay system variable regardless of how many days have occurred.

If your application is using unbroken weeks, week 1 can begin in the previous year or in the first few days of January. This depends on how you use the FirstWeekDay and the ReferenceDay environment variables.

## When to use week

The week() function is useful when you would like to compare aggregations by weeks. For example, it could be used if you would like to see the total sales of products by week. The week() function is chosen over weekname() when the user would like the calculation to not necessarily use the application’s BrokenWeeks, FirstWeekDay, or ReferenceDay system variables.

For example, if you want to see the total sales of products by week.

If the application is using unbroken weeks, week 1 may contain dates from December of the previous year or exclude dates in January of the current year. If the application is using broken weeks, week 1 may contain less than seven days..

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

The examples below assume

Set DateFormat= 'MM/DD/YYYY';
Set FirstWeekDay=0;
Set BrokenWeeks=0;
Set ReferenceDay=4;

Function examples

| Example | Result |
| --- | --- |
| week('12/28/2021') | Returns 52. |
| week(44614) | Returns 8, since this is the serial number for 02/22/2022. |
| week('01/03/2021') | Returns 53. |
| week('01/03/2021',6) | Returns 1. |

## Example 1 – Default system variables

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-3 "Glossary term") containing a set of transactions for the last week of 2021 and the first two weeks of 2022, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system variable (MM/DD/YYYY) format.
- The creation of a field, week\_number, that returns the year and week number when the transactions took place.
- The creation of a field called week\_day, showing the weekday value of each transaction date.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=6;
SET BrokenWeeks=1;
SET ReferenceDay=0;

Transactions:
    Load
        *,
        WeekDay(date) as week_day,
        Week(date) as week_number
        ;
Load
*
Inline
[
id,date,amount
8183,12/27/2021,58.27
8184,12/28/2021,67.42
8185,12/29/2021,23.80
8186,12/30/2021,82.06
8187,12/31/2021,40.56
8188,01/01/2022,37.23
8189,01/02/2022,17.17
8190,01/03/2022,88.27
8191,01/04/2022,57.42
8192,01/05/2022,53.80
8193,01/06/2022,82.06
8194,01/07/2022,40.56
8195,01/08/2022,53.67
8196,01/09/2022,26.63
8197,01/10/2022,72.48
8198,01/11/2022,18.37
8199,01/12/2022,45.26
8200,01/13/2022,58.23
8201,01/14/2022,18.52
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week\_day
- week\_number

Results table

| id | date | week\_day | week\_number |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | Mon | 53 |
| 8184 | 12/28/2021 | Tue | 53 |
| 8185 | 12/29/2021 | Wed | 53 |
| 8186 | 12/30/2021 | Thu | 53 |
| 8187 | 12/31/2021 | Fri | 53 |
| 8188 | 01/01/2022 | Sat | 1 |
| 8189 | 01/02/2022 | Sun | 2 |
| 8190 | 01/03/2022 | Mon | 2 |
| 8191 | 01/04/2022 | Tue | 2 |
| 8192 | 01/05/2022 | Wed | 2 |
| 8193 | 01/06/2022 | Thu | 2 |
| 8194 | 01/07/2022 | Fri | 2 |
| 8195 | 01/08/2022 | Sat | 2 |
| 8196 | 01/09/2022 | Sun | 3 |
| 8197 | 01/10/2022 | Mon | 3 |
| 8198 | 01/11/2022 | Tue | 3 |
| 8199 | 01/12/2022 | Wed | 3 |
| 8200 | 01/13/2022 | Thu | 3 |
| 8201 | 01/14/2022 | Fri | 3 |

The week\_number field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the week() function and passing the date field as the function’s argument.

No other parameters are passed into the function, and therefore the following default variables that affect the week() function are in effect:

- BrokenWeeks: The week count begins on January 1
- FirstWeekDay: The first day of the week is Sunday

Diagram of week() function, using default system variables

![Diagram displaying how the week function breaks up the dates of year into corresponding week numbers. Here, default system variables lead week 1 to begin on January 1, with week 2 starting on January 2.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-def-sys-variables.png "Click to view full size")

Because the application is using the default BrokenWeeks system variable, week 1 begins on January 1, a Saturday.

Because of the default FirstWeekDay system variable, weeks begin on a Sunday. The first Sunday after January 1 occurs on January 2, which is when week 2 begins.

## Example 2 – first\_week\_day

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The creation of a field, week\_number, that returns the year and week number when the transactions took place.
- The creation of a field called week\_day, showing the weekday value of each transaction date.

In this example, we would like to set the start of the work week to Tuesday.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=6;
SET BrokenWeeks=1;
SET ReferenceDay=0;

Transactions:
    Load
        *,
        WeekDay(date) as week_day,
        Week(date,1) as week_number
        ;
Load
*
Inline
[
id,date,amount
8183,12/27/2022,58.27
8184,12/28/2022,67.42
8185,12/29/2022,23.80
8186,12/30/2022,82.06
8187,12/31/2021,40.56
8188,01/01/2022,37.23
8189,01/02/2022,17.17
8190,01/03/2022,88.27
8191,01/04/2022,57.42
8192,01/05/2022,53.80
8193,01/06/2022,82.06
8194,01/07/2022,40.56
8195,01/08/2022,53.67
8196,01/09/2022,26.63
8197,01/10/2022,72.48
8198,01/11/2022,18.37
8199,01/12/2022,45.26
8200,01/13/2022,58.23
8201,01/14/2022,18.52
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week\_day
- week\_number

Results table

| id | date | week\_day | week\_number |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | Mon | 52 |
| 8184 | 12/28/2021 | Tue | 53 |
| 8185 | 12/29/2021 | Wed | 53 |
| 8186 | 12/30/2021 | Thu | 53 |
| 8187 | 12/31/2021 | Fri | 53 |
| 8188 | 01/01/2022 | Sat | 1 |
| 8189 | 01/02/2022 | Sun | 1 |
| 8190 | 01/03/2022 | Mon | 1 |
| 8191 | 01/04/2022 | Tue | 2 |
| 8192 | 01/05/2022 | Wed | 2 |
| 8193 | 01/06/2022 | Thu | 2 |
| 8194 | 01/07/2022 | Fri | 2 |
| 8195 | 01/08/2022 | Sat | 2 |
| 8196 | 01/09/2022 | Sun | 2 |
| 8197 | 01/10/2022 | Mon | 2 |
| 8198 | 01/11/2022 | Tue | 3 |
| 8199 | 01/12/2022 | Wed | 3 |
| 8200 | 01/13/2022 | Thu | 3 |
| 8201 | 01/14/2022 | Fri | 3 |

The application is still using broken weeks. However, the first\_week\_day argument has been set to 1 in the week() function. This sets the first day of the week to a Tuesday.

Diagram of week() function, first\_week\_day example

![Diagram displaying how the week function breaks up the dates of year into corresponding week numbers. Here, with weeks beginning on Jaunary 2, week 1 of the year starts on January 1 and week 2 starts on January 4.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-first-week-day.png "Click to view full size")

The application is using the default BrokenWeeks system variable, so week 1 begins on January 1, a Saturday.

The first\_week\_day argument of the week() function sets the first week day to a Tuesday. Therefore, week 53 begins on December 28, 2021.

However, because the function is still using broken weeks, week 1 will only be two days long, due to the first Tuesday after January 1 occurring on January 3.

## Example 3 – unbroken\_weeks

Load script and results

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

In this example, we use unbroken weeks.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=6;
SET BrokenWeeks=1;
SET ReferenceDay=0;

Transactions:
    Load
        *,
        WeekDay(date) as week_day,
        Week(date,6,0) as week_number
        ;
Load
*
Inline
[
id,date,amount
8183,12/27/2022,58.27
8184,12/28/2022,67.42
8185,12/29/2022,23.80
8186,12/30/2022,82.06
8187,12/31/2021,40.56
8188,01/01/2022,37.23
8189,01/02/2022,17.17
8190,01/03/2022,88.27
8191,01/04/2022,57.42
8192,01/05/2022,53.80
8193,01/06/2022,82.06
8194,01/07/2022,40.56
8195,01/08/2022,53.67
8196,01/09/2022,26.63
8197,01/10/2022,72.48
8198,01/11/2022,18.37
8199,01/12/2022,45.26
8200,01/13/2022,58.23
8201,01/14/2022,18.52
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week\_day
- week\_number

Diagram of week() function, chart object example

![ADD ALT TEXT HERE.....!!!!!!](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-chart-object.png "Click to view full size")

Results table

| id | date | week\_day | week\_number |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | Mon | 52 |
| 8184 | 12/28/2021 | Tue | 52 |
| 8185 | 12/29/2021 | Wed | 52 |
| 8186 | 12/30/2021 | Thu | 52 |
| 8187 | 12/31/2021 | Fri | 52 |
| 8188 | 01/01/2022 | Sat | 52 |
| 8189 | 01/02/2022 | Sun | 1 |
| 8190 | 01/03/2022 | Mon | 1 |
| 8191 | 01/04/2022 | Tue | 1 |
| 8192 | 01/05/2022 | Wed | 1 |
| 8193 | 01/06/2022 | Thu | 1 |
| 8194 | 01/07/2022 | Fri | 1 |
| 8195 | 01/08/2022 | Sat | 1 |
| 8196 | 01/09/2022 | Sun | 2 |
| 8197 | 01/10/2022 | Mon | 2 |
| 8198 | 01/11/2022 | Tue | 2 |
| 8199 | 01/12/2022 | Wed | 2 |
| 8200 | 01/13/2022 | Thu | 2 |
| 8201 | 01/14/2022 | Fri | 2 |

The first\_week\_date parameter is set to 1, making Tuesday the first day of the week. The broken\_weeks parameter it set to 0, forcing the function to use unbroken weeks. Finally, the third parameter sets the reference\_day to 2.

The first\_week\_date parameter is set to 6, making Sunday the first day of the week. The broken\_weeks parameter is set to 0, forcing the function to use unbroken weeks.

Diagram of week() function, example using unbroken weeks

![Diagram displaying how the week function breaks up the dates of year into corresponding week numbers. Here, since we use unbroken weeks, week 1 of the year starts on January 2, a Sunday.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-unbroken-weeks.png "Click to view full size")

By using unbroken weeks, week 1 does not necessarily begin on January 1; instead, it is required to have a minimum of four days. Therefore, in the dataset, week 52 concludes on Saturday, January 1, 2022. Week 1 then begins on the FirstWeekDay system variable, which is Sunday, January 2. This week will conclude on the following Saturday, January 8.

## Example 4 – reference\_day

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the third example.
- The creation of a field, week\_number, that returns the year and week number when the transactions took place.
- The creation of a field called week\_day, showing the weekday value of each transaction date.

Additionally, the following conditions must be met:

- The work week begins on a Tuesday.
- The company uses unbroken weeks.
- The reference\_day value is 2. In other words, the minimum number of days in January in week 1 will be 2.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=6;
SET BrokenWeeks=1;
SET ReferenceDay=0;

Transactions:
    Load
        *,
        WeekDay(date) as week_day,
        Week(date,1,0,2) as week_number
        ;
Load
*
Inline
[
id,date,amount
8183,12/27/2022,58.27
8184,12/28/2022,67.42
8185,12/29/2022,23.80
8186,12/30/2022,82.06
8187,12/31/2021,40.56
8188,01/01/2022,37.23
8189,01/02/2022,17.17
8190,01/03/2022,88.27
8191,01/04/2022,57.42
8192,01/05/2022,53.80
8193,01/06/2022,82.06
8194,01/07/2022,40.56
8195,01/08/2022,53.67
8196,01/09/2022,26.63
8197,01/10/2022,72.48
8198,01/11/2022,18.37
8199,01/12/2022,45.26
8200,01/13/2022,58.23
8201,01/14/2022,18.52
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week\_day
- week\_number

Results table

| id | date | week\_day | week\_number |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | Mon | 52 |
| 8184 | 12/28/2021 | Tue | 1 |
| 8185 | 12/29/2021 | Wed | 1 |
| 8186 | 12/30/2021 | Thu | 1 |
| 8187 | 12/31/2021 | Fri | 1 |
| 8188 | 01/01/2022 | Sat | 1 |
| 8189 | 01/02/2022 | Sun | 1 |
| 8190 | 01/03/2022 | Mon | 1 |
| 8191 | 01/04/2022 | Tue | 2 |
| 8192 | 01/05/2022 | Wed | 2 |
| 8193 | 01/06/2022 | Thu | 2 |
| 8194 | 01/07/2022 | Fri | 2 |
| 8195 | 01/08/2022 | Sat | 2 |
| 8196 | 01/09/2022 | Sun | 2 |
| 8197 | 01/10/2022 | Mon | 2 |
| 8198 | 01/11/2022 | Tue | 3 |
| 8199 | 01/12/2022 | Wed | 3 |
| 8200 | 01/13/2022 | Thu | 3 |
| 8201 | 01/14/2022 | Fri | 3 |

The first\_week\_date parameter is set to 1, making Tuesday the first day of the week. The broken\_weeks parameter it set to 0, forcing the function to use unbroken weeks. Finally, the third parameter sets the reference\_day parameter to 2.

Diagram of week() function, reference\_day example

![Diagram displaying how the week function breaks up the dates of year into corresponding week numbers. Here, week 1 begins on December 28, 2021, and concludes on Monday, January 3, 2022.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-reference-day.png "Click to view full size")

With the function using unbroken weeks and a reference\_day value of 2 used as a parameter, week 1 only needs to include two days in January. Due to the first weekday being Tuesday, week 1 begins on December 28, 2021, and concludes on Monday, January 3, 2022.

## Example 5 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns the week number is created as a [measure](#glossary-6 "Glossary term") in a chart object.

Load script

```
Transactions:
Load
*
Inline
[
id,date,amount
8183,12/27/2022,58.27
8184,12/28/2022,67.42
8185,12/29/2022,23.80
8186,12/30/2022,82.06
8187,12/31/2021,40.56
8188,01/01/2022,37.23
8189,01/02/2022,17.17
8190,01/03/2022,88.27
8191,01/04/2022,57.42
8192,01/05/2022,53.80
8193,01/06/2022,82.06
8194,01/07/2022,40.56
8195,01/08/2022,53.67
8196,01/09/2022,26.63
8197,01/10/2022,72.48
8198,01/11/2022,18.37
8199,01/12/2022,45.26
8200,01/13/2022,58.23
8201,01/14/2022,18.52
];
```

Results

Do the following:

1. Load the data and open a [sheet](#glossary-7 "Glossary term"). Create a new table.
2. Add the following fields as dimensions:

   - id
   - date
3. Next, create the following measure:

   =week (date)
4. Create a measure, week\_day, to show the weekday value of each transaction date:

   =weekday(date)

Results table

| id | date | =week(date) | =weekday(date) |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | 53 | Mon |
| 8184 | 12/28/2021 | 53 | Tue |
| 8185 | 12/29/2021 | 53 | Wed |
| 8186 | 12/30/2021 | 53 | Thu |
| 8187 | 12/31/2021 | 53 | Fri |
| 8188 | 01/01/2022 | 1 | Sat |
| 8189 | 01/02/2022 | 2 | Sun |
| 8190 | 01/03/2022 | 2 | Mon |
| 8191 | 01/04/2022 | 2 | Tue |
| 8192 | 01/05/2022 | 2 | Wed |
| 8193 | 01/06/2022 | 2 | Thu |
| 8194 | 01/07/2022 | 2 | Fri |
| 8195 | 01/08/2022 | 2 | Sat |
| 8196 | 01/09/2022 | 3 | Sun |
| 8197 | 01/10/2022 | 3 | Mon |
| 8198 | 01/11/2022 | 3 | Tue |
| 8199 | 01/12/2022 | 3 | Wed |
| 8200 | 01/13/2022 | 3 | Thu |
| 8201 | 01/14/2022 | 3 | Fri |

The week\_number field is created in the preceding load statement by using the week() function and passing the date field as the function’s argument.

No other parameters are passed into the function, and therefore the following default variables that affect the week() function are in effect:

- BrokenWeeks: The week count begins on January 1
- FirstWeekDay: The first day of the week is Sunday

Diagram of week() function, chart object example

![Diagram displaying how the week function breaks up the dates of year into corresponding week numbers. Here, week 1 begins on January 1, with week 2 starting on January 2.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-week-examples-def-sys-variables.png "Click to view full size")

Because the application is using the default BrokenWeeks system variable, week 1 begins on January 1, a Saturday.

Because of the default FirstWeekDay system variable, weeks begin on a Sunday. The first Sunday after January 1 occurs on January 2, which is when week 2 begins.

## Example 6 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for the last week of 2019 and first two weeks of 2020, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system variable (MM/DD/YYYY) format.

The application primarily uses broken weeks across its dashboard. However, the end user would like a chart object that presents the total sales by week using unbroken weeks. The reference day should be January 2, with weeks beginning on a Tuesday. This could be achieved even when this dimension is not available in the data model, using the week() function as a calculated dimension in the chart.

Load script

```
SET BrokenWeeks=1;
SET ReferenceDay=0;
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8183,12/27/2019,58.27
8184,12/28/2019,67.42
8185,12/29/2019,23.80
8186,12/30/2019,82.06
8187,12/31/2019,40.56
8188,01/01/2020,37.23
8189,01/02/2020,17.17
8190,01/03/2020,88.27
8191,01/04/2020,57.42
8192,01/05/2020,53.80
8193,01/06/2020,82.06
8194,01/07/2020,40.56
8195,01/08/2020,53.67
8196,01/09/2020,26.63
8197,01/10/2020,72.48
8198,01/11/2020,18.37
8199,01/12/2020,45.26
8200,01/13/2020,58.23
8201,01/14/2020,18.52
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table.
2. Create the following calculated dimension:

   =week(date)
3. Next, create the following [aggregation](#glossary-8 "Glossary term") measure:

   =sum(amount)
4. Set the measure's Number formatting to Money.
5. Select the Sorting menu, and for the calculated dimension, remove custom sorting.
6. De-select the Sort numerically and Sort alphabetically options.

Results table

| week(date) | sum(amount) |
| --- | --- |
| 52 | $125.69 |
| 53 | $146.42 |
| 1 | $200.09 |
| 2 | $347.57 |
| 3 | $122.01 |
