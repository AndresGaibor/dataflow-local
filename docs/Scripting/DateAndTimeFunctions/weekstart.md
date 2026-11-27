---
title: "weekstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# weekstart Script and chart function

Expand/Collapse all

# weekstart Script and chart function

This function returns
a value corresponding to a timestamp of the first millisecond of the
first day of the calendar week containing date.
The default output format is the DateFormat set in the script.

Syntax:

WeekStart(timestamp [, period\_no [, first\_week\_day ]])

Return data type:  dual

The weekstart() function determines which week the date falls into. It then returns a timestamp, in date format, for the first millisecond of that week. The first day of the week is determined by the FirstWeekDay environment [variable](#glossary-0 "Glossary term"). However, this can be superseded by the first\_week\_day argument in the weekstart() function.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| period\_no | shift is an integer, where the value 0 indicates the week which contains date. Negative values in shift indicate preceding weeks and positive values indicate succeeding weeks. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of variable FirstWeekDay is used.  The possible values first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm). |

## When to use weekstart

The weekstart() function is commonly used as part of an expression when the user would like the calculation to use the fraction of the week that has elapsed thus far. For example, it could be used if a user would like to calculate the total wages earned by employees in the week so far.

The following examples assume:

SET FirstWeekDay=0;

Function examples

| Example | Result |
| --- | --- |
| weekstart('01/12/2013') | Returns 01/07/2013. |
| weekstart('01/12/2013', -1 ) | Returns 11/31/2012. |
| weekstart('01/12/2013', 0, 1) | Returns 01/08/2013. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Examples:

If you want ISO settings for weeks and week numbers, make sure to have the following in the script:

Set DateFormat ='YYYY-MM-DD';
Set FirstWeekDay =0; // Monday as first week day
Set BrokenWeeks =0; //(use unbroken weeks)
Set ReferenceDay =4; // Jan 4th is always in week 1

If you want US settings, make sure to have the following in the script:

Set DateFormat ='M/D/YYYY';
Set FirstWeekDay =6; // Sunday as first week day
Set BrokenWeeks =1; //(use broken weeks)
Set ReferenceDay =1; // Jan 1st is always in week 1

The examples above results in the following from the weekstart() function:

Example of Weekstart function

| Date | ISO week start | US week start |
| --- | --- | --- |
| Sat 2020 Dec 26 | 2020-12-21 | 12/20/2020 |
| Sun 2020 Dec 27 | 2020-12-21 | 12/27/2020 |
| Mon 2020 Dec 28 | 2020-12-28 | 12/27/2020 |
| Tue 2020 Dec 29 | 2020-12-28 | 12/27/2020 |
| Wed 2020 Dec 30 | 2020-12-28 | 12/27/2020 |
| Thu 2020 Dec 31 | 2020-12-28 | 12/27/2020 |
| Fri 2021 Jan 1 | 2020-12-28 | 12/27/2020 |
| Sat 2021 Jan 2 | 2020-12-28 | 12/27/2020 |
| Sun 2021 Jan 3 | 2020-12-28 | 1/3/2021 |
| Mon 2021 Jan 4 | 2021-01-04 | 1/3/2021 |
| Tue 2021 Jan 5 | 2021-01-04 | 1/3/2021 |

Information noteThe week starts are on Mondays in the ISO column, and on Sundays in the US column.

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called Transactions.
- The date [field](#glossary-2 "Glossary term") provided in the DateFormat system variable (MM/DD/YYYY) format.
- The creation of a field, start\_of\_week, that returns a timestamp for the start of the week when the transactions took place.

Load script

```
SET FirstWeekDay=6;

Transactions:
    Load
        *,
        weekstart(date) as start_of_week,
        timestamp(weekstart(date)) as start_of_week_timestamp
        ;
Load
*
Inline
[
id,date,amount
8188,1/7/2022,17.17
8189,1/19/2022,37.23
8190,2/28/2022,88.27
8191,2/5/2022,57.42
8192,3/16/2022,53.80
8193,4/1/2022,82.06
8194,5/7/2022,40.39
8195,5/16/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- start\_of\_week
- start\_of\_week\_timestamp

Results table

| date | start\_of\_week | start\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/02/2022 | 1/2/2022 12:00:00 AM |
| 1/19/2022 | 01/16/2022 | 1/16/2022 12:00:00 AM |
| 2/5/2022 | 01/30/2022 | 1/30/2022 12:00:00 AM |
| 2/28/2022 | 02/27/2022 | 2/27/2022 12:00:00 AM |
| 3/16/2022 | 03/13/2022 | 3/13/2022 12:00:00 AM |
| 4/1/2022 | 03/27/2022 | 3/27/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/16/2022 | 05/15/2022 | 5/15/2022 12:00:00 AM |
| 6/15/2022 | 06/12/2022 | 6/12/2022 12:00:00 AM |
| 6/26/2022 | 06/26/2022 | 6/26/2022 12:00:00 AM |
| 7/9/2022 | 07/03/2022 | 7/3/2022 12:00:00 AM |
| 7/22/2022 | 07/17/2022 | 7/17/2022 12:00:00 AM |
| 7/23/2022 | 07/17/2022 | 7/17/2022 12:00:00 AM |
| 7/27/2022 | 07/24/2022 | 7/24/2022 12:00:00 AM |
| 8/2/2022 | 07/31/2022 | 7/31/2022 12:00:00 AM |
| 8/8/2022 | 08/07/2022 | 8/7/2022 12:00:00 AM |
| 8/19/2022 | 08/14/2022 | 8/14/2022 12:00:00 AM |
| 9/26/2022 | 09/25/2022 | 9/25/2022 12:00:00 AM |
| 10/14/2022 | 10/09/2022 | 10/9/2022 12:00:00 AM |
| 10/29/2022 | 10/23/2022 | 10/23/2022 12:00:00 AM |

The start\_of\_week field is created in the [preceding load](#glossary-3 "Glossary term") statement by using the weekstart() function and passing the date field as the function’s argument.

The weekstart() function initially identifies which week the date value falls into, returning a timestamp for the first millisecond of that week.

Diagram of weekstart() function, example with no additional arguments

![Diagram showing how the weekstart function converts the transaction date into a timestamp for the first millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekstart-examples-no-add-arg.png "Click to view full size")

Transaction 8191 took place on February 5. The FirstWeekDay system variable sets the first day of the week to a Sunday. The weekstart() function identifies that the first Sunday before February 5 – and therefore the start of the week – was on January 30, Therefore, the start\_of\_week value for that transaction returns the first millisecond of that day, which is January 30 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, previous\_week\_start, that returns the timestamp for the start of the quarter before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        weekstart(date,-1) as previous_week_start,
        timestamp(weekstart(date,-1)) as previous_week_start_timestamp
        ;
Load
*
Inline
[
id,date,amount
8188,1/7/2022,17.17
8189,1/19/2022,37.23
8190,2/28/2022,88.27
8191,2/5/2022,57.42
8192,3/16/2022,53.80
8193,4/1/2022,82.06
8194,5/7/2022,40.39
8195,5/16/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- previous\_week\_start
- previous\_week\_start\_timestamp

Results table

| date | previous\_week\_start | previous\_week\_start\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 12/26/2021 | 12/26/2021 12:00:00 AM |
| 1/19/2022 | 01/09/2022 | 1/9/2022 12:00:00 AM |
| 2/5/2022 | 01/23/2022 | 1/23/2022 12:00:00 AM |
| 2/28/2022 | 02/20/2022 | 2/20/2022 12:00:00 AM |
| 3/16/2022 | 03/06/2022 | 3/6/2022 12:00:00 AM |
| 4/1/2022 | 03/20/2022 | 3/20/2022 12:00:00 AM |
| 5/7/2022 | 04/24/2022 | 4/24/2022 12:00:00 AM |
| 5/16/2022 | 05/08/2022 | 5/8/2022 12:00:00 AM |
| 6/15/2022 | 06/05/2022 | 6/5/2022 12:00:00 AM |
| 6/26/2022 | 06/19/2022 | 6/19/2022 12:00:00 AM |
| 7/9/2022 | 06/26/2022 | 6/26/2022 12:00:00 AM |
| 7/22/2022 | 07/10/2022 | 7/10/2022 12:00:00 AM |
| 7/23/2022 | 07/10/2022 | 7/10/2022 12:00:00 AM |
| 7/27/2022 | 07/17/2022 | 7/17/2022 12:00:00 AM |
| 8/2/2022 | 07/24/2022 | 7/24/2022 12:00:00 AM |
| 8/8/2022 | 07/31/2022 | 7/31/2022 12:00:00 AM |
| 8/19/2022 | 08/07/2022 | 8/7/2022 12:00:00 AM |
| 9/26/2022 | 09/18/2022 | 9/18/2022 12:00:00 AM |
| 10/14/2022 | 10/02/2022 | 10/2/2022 12:00:00 AM |
| 10/29/2022 | 10/16/2022 | 10/16/2022 12:00:00 AM |

In this instance, because a period\_no of -1 was used as the offset argument in the weekstart() function, the function first identifies the week that the transactions take place in. It then looks one week prior and identifies the first millisecond of that week.

Diagram of weekstart() function, period\_no example

![Diagram showing how the weekstart function converts the transaction date into a timestamp for the first millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekstart-examples-period-no.png "Click to view full size")

Transaction 8196 took place on June 15. The weekstart() function identifies that the week begins on June 12. Therefore, the previous week began on June 5 at 12:00:00 AM; this is the value that is returned for the previous\_week\_start field.

## Example 3 – first\_week\_day

Load script and results

Overview

Open the [Data load editor](#glossary-4 "Glossary term") and add the [load script](#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, we need to set Tuesday as the first day of the work week.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        weekstart(date,0,1) as start_of_week,
        timestamp(weekstart(date,0,1)) as start_of_week_timestamp
        ;
Load
*
Inline
[
id,date,amount
8188,1/7/2022,17.17
8189,1/19/2022,37.23
8190,2/28/2022,88.27
8191,2/5/2022,57.42
8192,3/16/2022,53.80
8193,4/1/2022,82.06
8194,5/7/2022,40.39
8195,5/16/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- start\_of\_week
- start\_of\_week\_timestamp

Results table

| date | start\_of\_week | start\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/04/2022 | 1/4/2022 12:00:00 AM |
| 1/19/2022 | 01/18/2022 | 1/18/2022 12:00:00 AM |
| 2/5/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 2/28/2022 | 02/22/2022 | 2/22/2022 12:00:00 AM |
| 3/16/2022 | 03/15/2022 | 3/15/2022 12:00:00 AM |
| 4/1/2022 | 03/29/2022 | 3/29/2022 12:00:00 AM |
| 5/7/2022 | 05/03/2022 | 5/3/2022 12:00:00 AM |
| 5/16/2022 | 05/10/2022 | 5/10/2022 12:00:00 AM |
| 6/15/2022 | 06/14/2022 | 6/14/2022 12:00:00 AM |
| 6/26/2022 | 06/21/2022 | 6/21/2022 12:00:00 AM |
| 7/9/2022 | 07/05/2022 | 7/5/2022 12:00:00 AM |
| 7/22/2022 | 07/19/2022 | 7/19/2022 12:00:00 AM |
| 7/23/2022 | 07/19/2022 | 7/19/2022 12:00:00 AM |
| 7/27/2022 | 07/26/2022 | 7/26/2022 12:00:00 AM |
| 8/2/2022 | 08/02/2022 | 8/2/2022 12:00:00 AM |
| 8/8/2022 | 08/02/2022 | 8/2/2022 12:00:00 AM |
| 8/19/2022 | 08/16/2022 | 8/16/2022 12:00:00 AM |
| 9/26/2022 | 09/20/2022 | 9/20/2022 12:00:00 AM |
| 10/14/2022 | 10/11/2022 | 10/11/2022 12:00:00 AM |
| 10/29/2022 | 10/25/2022 | 10/25/2022 12:00:00 AM |

In this instance, because the first\_week\_date argument of 1 is used in the weekstart() function, it sets the first day of the week to Tuesday.

Diagram of weekstart() function, first\_week\_day example

![Diagram showing how the weekstart function converts the transaction date into a timestamp for the first millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekstart-examples-first-week-day.png "Click to view full size")

Transaction 8191 took place on February 5. The weekstart() function identifies that the first Tuesday before the this date – and therefore the start of the week and value returned – was February 1 at 12:00:00 AM.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the start of the week when the transactions took place is created as a [measure](#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
Transactions:

Load
*
Inline
[
id,date,amount
8188,1/7/2022,17.17
8189,1/19/2022,37.23
8190,2/28/2022,88.27
8191,2/5/2022,57.42
8192,3/16/2022,53.80
8193,4/1/2022,82.06
8194,5/7/2022,40.39
8195,5/16/2022,87.21
8196,6/15/2022,95.93
8197,6/26/2022,45.89
8198,7/9/2022,36.23
8199,7/22/2022,25.66
8200,7/23/2022,82.77
8201,7/27/2022,69.98
8202,8/2/2022,76.11
8203,8/8/2022,25.12
8204,8/19/2022,46.23
8205,9/26/2022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

To calculate the start of the week in which a transaction takes place, add the following measures:

- =weekstart(date)
- =timestamp(weekstart(date))

Results table

| date | start\_of\_week | start\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/02/2022 | 1/2/2022 12:00:00 AM |
| 1/19/2022 | 01/16/2022 | 1/16/2022 12:00:00 AM |
| 2/5/2022 | 01/30/2022 | 1/30/2022 12:00:00 AM |
| 2/28/2022 | 02/27/2022 | 2/27/2022 12:00:00 AM |
| 3/16/2022 | 03/13/2022 | 3/13/2022 12:00:00 AM |
| 4/1/2022 | 03/27/2022 | 3/27/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/16/2022 | 05/15/2022 | 5/15/2022 12:00:00 AM |
| 6/15/2022 | 06/12/2022 | 6/12/2022 12:00:00 AM |
| 6/26/2022 | 06/26/2022 | 6/26/2022 12:00:00 AM |
| 7/9/2022 | 07/03/2022 | 7/3/2022 12:00:00 AM |
| 7/22/2022 | 07/17/2022 | 7/17/2022 12:00:00 AM |
| 7/23/2022 | 07/17/2022 | 7/17/2022 12:00:00 AM |
| 7/27/2022 | 07/24/2022 | 7/24/2022 12:00:00 AM |
| 8/2/2022 | 07/31/2022 | 7/31/2022 12:00:00 AM |
| 8/8/2022 | 08/07/2022 | 8/7/2022 12:00:00 AM |
| 8/19/2022 | 08/14/2022 | 8/14/2022 12:00:00 AM |
| 9/26/2022 | 09/25/2022 | 9/25/2022 12:00:00 AM |
| 10/14/2022 | 10/09/2022 | 10/9/2022 12:00:00 AM |
| 10/29/2022 | 10/23/2022 | 10/23/2022 12:00:00 AM |

The start\_of\_week measure is created in the chart object by using the weekstart() function and passing the date field as the function’s argument.

The weekstart() function initially identifies which week the date value falls into, returning a timestamp for the first millisecond of that week.

Diagram of weekstart() function, chart object example

![Diagram showing how the weekstart function converts the transaction date into a timestamp for the first millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekstart-examples-chart-object.png "Click to view full size")

Transaction 8191 took place on February 5. The FirstWeekDay system variable sets the first day of the week to a Sunday. The weekstart() function identifies that the first Sunday before February 5 – and therefore the start of the week – was January 30. Therefore, the start\_of\_week value for that transaction returns the first millisecond of that day, which is January 30 at 12:00:00 AM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Payroll.
- Data consisting of employee IDs, employee names, and the daily wage earned by each employee.

Employees begin work on Monday and work six days per week. The FirstWeekDay system variable must not be modified.

The end user would like a chart object that displays, by employee ID and employee name, the wages earned in the week to date.

Load script

```
Payroll:
Load
*
Inline
[
employee_id,employee_name,day_rate
182,Mark, $150
183,Deryck, $125
184,Dexter, $125
185,Sydney,$270
186,Agatha,$128
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - employee\_id
   - employee\_name
2. Next, create a measure to calculate the wages earned in the week to date:

   =if(today(1)-weekstart(today(1),0,0)<7,(today(1)-weekstart(today(1),0,0))\*day\_rate,day\_rate\*6)
3. Set the measure's Number formatting to Money.

Results table

| employee\_id | employee\_name | =if(today(1)-weekstart(today(1),0,0)<7,(today(1)-weekstart(today(1),0,0))\*day\_rate,day\_rate\*6) |
| --- | --- | --- |
| 182 | Mark | $600.00 |
| 183 | Deryck | $500.00 |
| 184 | Dexter | $500.00 |
| 185 | Sydney | $1080.00 |
| 186 | Agatha | $512.00 |

The weekstart() function, by using today’s date as its first argument and 0 as its third argument, sets Monday as the first day of the week and returns the start date of the current week. By subtracting that result from the current date, the expression then returns the number of days that have elapsed so far this week.

The condition then evaluates whether there have been more than six days this week. If so, the employee’s day\_rate is multiplied by 6 days. Otherwise, the day\_rate is multiplied by the number of days that have occurred so far this week.
