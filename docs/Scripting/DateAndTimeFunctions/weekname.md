---
title: "weekname Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekname.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# weekname Script and chart function

Expand/Collapse all

# weekname Script and chart function

This function returns
a value showing the year and week number with an underlying numeric
value corresponding to a timestamp of the first millisecond of the first
day of the week containing date.

Syntax:

WeekName(date[, period\_no [, first\_week\_day [, broken\_weeks [, reference\_day]]]])

The weekname() function determines which week the date falls into and returns the week number and year of that week. The first day of the week is determined by the FirstWeekDay system [variable](#glossary-0 "Glossary term"). However, you can also change the first day of the week by using the first\_week\_day argument in the weekname() function.

 In Qlik Sense, the regional settings are fetched when the application is created, and the corresponding settings are stored in the script as environment [variables](#glossary-2 "Glossary term").

A North American application developer often gets Set BrokenWeeks=1; in the script, corresponding to broken weeks. A European application developer often gets Set BrokenWeeks=0; in the script, corresponding to unbroken weeks.

If your application uses broken weeks, the week number count begins on the January 1 and ends on the day prior to the FirstWeekDay system variable regardless of how many days have occurred.

However, if your application is using unbroken weeks, week 1 can begin in the previous year or in the first few days in January. This depends on how you use the ReferenceDay and FirstWeekDay system variables.

Example of Weekname function

| Date | ISO week name | US week name |
| --- | --- | --- |
| Sat 2020 Dec 26 | 2020/52 | 2020/52 |
| Sun 2020 Dec 27 | 2020/52 | 2020/53 |
| Mon 2020 Dec 28 | 2020/53 | 2020/53 |
| Tue 2020 Dec 29 | 2020/53 | 2020/53 |
| Wed 2020 Dec 30 | 2020/53 | 2020/53 |
| Thu 2020 Dec 31 | 2020/53 | 2020/53 |
| Fri 2021 Jan 1 | 2020/53 | 2021/01 |
| Sat 2021 Jan 2 | 2020/53 | 2021/01 |
| Sun 2021 Jan 3 | 2020/53 | 2021/02 |
| Mon 2021 Jan 4 | 2021/01 | 2021/02 |
| Tue 2021 Jan 5 | 2021/01 | 2021/02 |

When to use weekname

The weekname() function is useful for when you would like to compare aggregations by weeks.

For example, if you want to see the total sales of products by week. To maintain consistency with the BrokenWeeks environment variable in the application, use weekname() instead of lunarweekname(). If the application is using unbroken weeks, week 1 may contain dates from December of the previous year or exclude dates in January of the current year. If the application is using broken weeks, week 1 may contain less than seven days.

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| period\_no | shift is an integer, where the value 0 indicates the week which contains date. Negative values in shift indicate preceding weeks and positive values indicate succeeding weeks. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of variable FirstWeekDay is used.  The possible values first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm). |
| broken\_weeks | If you don't specify broken\_weeks, the value of variable BrokenWeeks will be used to define if weeks are broken or not.  For more information about the system variable, see [*BrokenWeeks*](../NumberInterpretationVariables/BrokenWeeks.htm) |
| reference\_day | If you don't specify reference\_day, the value of variable ReferenceDay will be used to define which day in January to set as reference day to define week 1. By default, Qlik Sense functions use 4 as the reference day. This means that week 1 must contain January 4, or put differently, that week 1 must always have at least 4 days in January.  For more information about the system variable, see [*ReferenceDay*](../NumberInterpretationVariables/ReferenceDay.htm) |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

The examples below assume:

Set FirstWeekDay=0;
Set BrokenWeeks=0;
Set ReferenceDay=4;

Function examples

| Example | Result |
| --- | --- |
| weekname('01/12/2013') | Returns 2013/02. |
| weekname('01/12/2013', -1) | Returns 2013/01. |
| weekname('01/12/2013', 0, 1) | Returns 2013/02. |

## Example 1 – Date with no additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-3 "Glossary term") containing a set of transactions for the last week of 2021 and first two weeks of 2022 is loaded into a table called ‘Transactions’.
- The DateFormat system variable which is set to the MM/DD/YYYY format.
- The BrokenWeeks system variable which is set to 1.
- The FirstWeekDay system variable which is set to 6.
- A [preceding load](#glossary-4 "Glossary term") which contains the following:

  - The weekday() function which is set as the [field](#glossary-5 "Glossary term") ‘week\_number’, that returns the year and week number when the transactions took place.
  - The weekname() function which is set as the field called ‘week\_day’, to show the weekday value of each transaction date.

Load script

```
SET BrokenWeeks=1;
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=6;

Transactions:
   Load
     *,
     WeekDay(date) as week_day,
     Weekname(date) as week_number
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
| 8183 | 12/27/2021 | Mon | 2021/53 |
| 8184 | 12/28/2021 | Tue | 2021/53 |
| 8185 | 12/29/2021 | Wed | 2021/53 |
| 8186 | 12/30/2021 | Thu | 2021/53 |
| 8187 | 12/31/2021 | Fri | 2021/53 |
| 8188 | 01/01/2022 | Sat | 2022/01 |
| 8189 | 01/02/2022 | Sun | 2022/02 |
| 8190 | 01/03/2022 | Mon | 2022/02 |
| 8191 | 01/04/2022 | Tue | 2022/02 |
| 8192 | 01/05/2022 | Wed | 2022/02 |
| 8193 | 01/06/2022 | Thu | 2022/02 |
| 8194 | 01/07/2022 | Fri | 2022/02 |
| 8195 | 01/08/2022 | Sat | 2022/02 |
| 8196 | 01/09/2022 | Sun | 2022/03 |
| 8197 | 01/10/2022 | Mon | 2022/03 |
| 8198 | 01/11/2022 | Tue | 2022/03 |
| 8199 | 01/12/2022 | Wed | 2022/03 |
| 8200 | 01/13/2022 | Thu | 2022/03 |
| 8201 | 01/14/2022 | Fri | 2022/03 |

The ‘week\_number’ field is created in the preceding load statement by using the weekname() function and passing the date field as the function’s argument.

The weekname() function initially identifies which week the date value falls into and returns the week number count and the year the transaction takes place.

The FirstWeekDay system variable sets Sunday as the first day of the week. The BrokenWeeks system variable sets the application to use broken weeks, meaning that week 1 will begin on January 1.

Diagram of weekname() function with the default variables.

![Diagram that shows how the weekname() function identifies the week number and year in which a transaction takes place. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example1-diagram1.png "Click to view full size")

Week 1 begins on January 1, which is a Saturday, and therefore transactions occurring on this date return the value 2022/01 (the year and week number).

Diagram of weekname() function identifying the week number of transaction 8192.

![Diagram that shows how the weekname() function identifies the week number in which a transaction 8192 took place. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example1-diagram2.png "Click to view full size")

Because the application is using broken weeks and the first weekday is Sunday, transactions occurring from January 2 to January 8 return the value 2022/02 (week number 2 in 2022.) An example of this would be transaction 8192 which took place on January 5 and returns the value 2022/02 for the ‘week\_number’ field.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the task is to create a field, ‘previous\_week\_number’, that returns the year, and week number, prior to when the transactions took place.

Open the Data load editor and add the following load script to a new section.

Load script

```
SET BrokenWeeks=1;
SET FirstWeekDay=6;

Transactions:
   Load
     *,
     weekname(date,-1) as previous_week_number
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
| 8183 | 12/27/2021 | Mon | 2021/52 |
| 8184 | 12/28/2021 | Tue | 2021/52 |
| 8185 | 12/29/2021 | Wed | 2021/52 |
| 8186 | 12/30/2021 | Thu | 2021/52 |
| 8187 | 12/31/2021 | Fri | 2021/52 |
| 8188 | 01/01/2022 | Sat | 2021/52 |
| 8189 | 01/02/2022 | Sun | 2021/53 |
| 8190 | 01/03/2022 | Mon | 2021/53 |
| 8191 | 01/04/2022 | Tue | 2021/53 |
| 8192 | 01/05/2022 | Wed | 2021/53 |
| 8193 | 01/06/2022 | Thu | 2021/53 |
| 8194 | 01/07/2022 | Fri | 2021/53 |
| 8195 | 01/08/2022 | Sat | 2022/01 |
| 8196 | 01/09/2022 | Sun | 2022/02 |
| 8197 | 01/10/2022 | Mon | 2022/02 |
| 8198 | 01/11/2022 | Tue | 2022/02 |
| 8199 | 01/12/2022 | Wed | 2022/02 |
| 8200 | 01/13/2022 | Thu | 2022/02 |
| 8201 | 01/14/2022 | Fri | 2022/02 |

Because a period\_no of -1 is used as the offset argument in the weekname() function, the function first identifies the week that the transactions take place in. It then looks one week prior and identifies the first millisecond of that week.

Diagram of weekname() function with a period\_no offset of -1.

![Diagram that shows how the period_no offset of negative one makes the weekname() function retreive the week number of the previous week. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example2-diagram.png "Click to view full size")

Transaction 8192 took place on January 5, 2022. The weekname() function looks one week prior, December 30, 2021, and returns the week number and year for that date – 2021/53.

## Example 3 – first\_week\_day

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the company policy is for the work week to begin on Tuesday.

Open the Data load editor and add the following load script to a new section.

Load script

```
SET BrokenWeeks=1;
SET DateFormat='MM/DD/YYYY';

Transactions:
   Load
     *,
     weekday(date) as week_day,
     weekname(date,0,1) as week_number
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
| 8183 | 12/27/2021 | Mon | 2021/52 |
| 8184 | 12/28/2021 | Tue | 2021/53 |
| 8185 | 12/29/2021 | Wed | 2021/53 |
| 8186 | 12/30/2021 | Thu | 2021/53 |
| 8187 | 12/31/2021 | Fri | 2021/53 |
| 8188 | 01/01/2022 | Sat | 2022/01 |
| 8189 | 01/02/2022 | Sun | 2022/01 |
| 8190 | 01/03/2022 | Mon | 2022/01 |
| 8191 | 01/04/2022 | Tue | 2022/02 |
| 8192 | 01/05/2022 | Wed | 2022/02 |
| 8193 | 01/06/2022 | Thu | 2022/02 |
| 8194 | 01/07/2022 | Fri | 2022/02 |
| 8195 | 01/08/2022 | Sat | 2022/02 |
| 8196 | 01/09/2022 | Sun | 2022/02 |
| 8197 | 01/10/2022 | Mon | 2022/02 |
| 8198 | 01/11/2022 | Tue | 2022/03 |
| 8199 | 01/12/2022 | Wed | 2022/03 |
| 8200 | 01/13/2022 | Thu | 2022/03 |
| 8201 | 01/14/2022 | Fri | 2022/03 |

Diagram of weekname() function with Tuesday as the first day of the week.

![Diagram that shows how the weekname() function works when Tuesday is set as the first day of week. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example3-diagram1.png "Click to view full size")

Because the first\_week\_date argument of 1 is used in the weekname() function, it uses Tuesday as the first day of the week. The function therefore determines that week 53 of 2021 begins on Tuesday December 28; and, due to the application using broken weeks, week 1 begins on January 1, 2022, and ends on the last millisecond of Monday January 3, 2022.

Diagram showing week number of transaction 8192 with Tuesday as the first day of week.

![Diagram that shows how setting Tuesday as the first day of the week makes the weekname() function return a different week number for transaction 8192.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example3-diagram2.png "Click to view full size")

Transaction 8192 took place on January 5, 2022. Therefore, using a first\_week\_day parameter of Tuesday, the weekname() function returns the value 2022/02 for the ‘week\_number’ field.

## Example 4 – Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that returns the year number of the week for when the transactions took place is created as a [measure](#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
SET BrokenWeeks=1;
Transactions:
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
- =week\_day (date)

To calculate the start of the week that a transaction takes place in, create the following measure:

=weekname(date)

Results table

| id | date | =weekday(date) | =weekname(date) |
| --- | --- | --- | --- |
| 8183 | 12/27/2021 | Mon | 2021/53 |
| 8184 | 12/28/2021 | Tue | 2021/53 |
| 8185 | 12/29/2021 | Wed | 2021/53 |
| 8186 | 12/30/2021 | Thu | 2021/53 |
| 8187 | 12/31/2021 | Fri | 2021/53 |
| 8188 | 01/01/2022 | Sat | 2022/01 |
| 8189 | 01/02/2022 | Sun | 2022/02 |
| 8190 | 01/03/2022 | Mon | 2022/02 |
| 8191 | 01/04/2022 | Tue | 2022/02 |
| 8192 | 01/05/2022 | Wed | 2022/02 |
| 8193 | 01/06/2022 | Thu | 2022/02 |
| 8194 | 01/07/2022 | Fri | 2022/02 |
| 8195 | 01/08/2022 | Sat | 2022/02 |
| 8196 | 01/09/2022 | Sun | 2022/03 |
| 8197 | 01/10/2022 | Mon | 2022/03 |
| 8198 | 01/11/2022 | Tue | 2022/03 |
| 8199 | 01/12/2022 | Wed | 2022/03 |
| 8200 | 01/13/2022 | Thu | 2022/03 |
| 8201 | 01/14/2022 | Fri | 2022/03 |

The ‘week\_number’ field is created as a measure in the chart object by using the weekname() function and passing the date field as the function’s argument.

The weekname() function initially identifies which week the date value falls into and returns the week number count and the year that the transaction takes place.

The FirstWeekDay system variable sets Sunday as the first day of the week. The BrokenWeeks system variable sets the application to use broken weeks, meaning that week 1 begins on January 1.

Diagram showing week number with Sunday as the first day of the week.

![Diagram that shows the week 1 begins on January 1 and Sunday as the first day of the week. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example4-diagram1.png "Click to view full size")

Diagram showing that transaction 8192 took place in week number two.

![Diagram that shows transaction 8192 takes place in week 2. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekname-example4-diagram1.png "Click to view full size")

Because the application is using broken weeks and the first weekday is Sunday, transactions occurring from January 2 to January 8 return the value 2022/02, week number 2 in 2022. Note that transaction 8192 took place on January 5 and returns the value 2022/02 for the ‘week\_number’ field.

## Example 5 – Scenario

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for the last week of 2019 and first two weeks of 2020 is loaded into a table called ‘Transactions’.
- The BrokenWeeks system variable which is set to 0.
- The ReferenceDay system variable which is set to 2.
- The DateFormat system variable which is set to the MM/DD/YYYY format.

Load script

```
SET BrokenWeeks=0;
SET ReferenceDay=2;
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

Load the data and open a [sheet](#glossary-7 "Glossary term"). Create a new table.

Create a calculated [dimension](#glossary-8 "Glossary term") using the following expression:

=weekname(date)

To calculate total sales create the following [aggregation](#glossary-9 "Glossary term") measure:

=sum(amount)

Set the measure’s Number Formatting to Money.

Results table

| weekname(date) | =sum(amount) |
| --- | --- |
| 2019/52 | $125.69 |
| 2020/01 | $346.51 |
| 2020/02 | $347.57 |
| 2020/03 | $122.01 |

To demonstrate the results of using the weekname() function in this scenario, add the following field as a dimension:

date

Results table with date field

| weekname(date) | date | =sum(amount) |
| --- | --- | --- |
| 2019/52 | 12/27/2019 | $58.27 |
| 2019/52 | 12/28/2019 | $67.42 |
| 2020/01 | 12/29/2019 | $23.80 |
| 2020/01 | 12/30/2019 | $82.06 |
| 2020/01 | 12/31/2019 | $40.56 |
| 2020/01 | 01/01/2020 | $37.23 |
| 2020/01 | 01/02/2020 | $17.17 |
| 2020/01 | 01/03/2020 | $88.27 |
| 2020/01 | 01/04/2020 | $57.42 |
| 2020/02 | 01/05/2020 | $53.80 |
| 2020/02 | 01/06/2020 | $82.06 |
| 2020/02 | 01/07/2020 | $40.56 |
| 2020/02 | 01/08/2020 | $53.67 |
| 2020/02 | 01/09/2020 | $26.63 |
| 2020/02 | 01/10/2020 | $72.48 |
| 2020/02 | 01/11/2020 | $18.37 |
| 2020/03 | 01/12/2020 | $45.26 |
| 2020/03 | 01/13/2020 | $58.23 |
| 2020/03 | 01/14/2020 | $18.52 |

Because the application uses unbroken weeks, and week 1 requires a minimum of two days in January because of the ReferenceDay system variable, week 1 of 2020 includes transactions from December 29, 2019.
