---
title: "weekend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# weekend Script and chart function

Expand/Collapse all

# weekend Script and chart function

This function returns
a value corresponding to a timestamp of the last millisecond of the
last day of the calendar week containing date.
The default output format will be the DateFormat set in the script.

Syntax:

WeekEnd(timestamp [, period\_no [, first\_week\_day ]])

Return data type:  dual

The weekend() function determines which week the date falls into. It then returns a timestamp, in date format, for the last millisecond of that week. The first day of the week is determined by the FirstWeekDay environment [variable](#glossary-0 "Glossary term"). However, this can be superseded by the first\_week\_day argument in the weekend() function.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| period\_no | shift is an integer, where the value 0 indicates the week which contains date. Negative values in shift indicate preceding weeks and positive values indicate succeeding weeks. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of variable FirstWeekDay is used.  The possible values for first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm) |

## When to use weekend

The weekend() function is commonly used as part of an expression when the user would like the calculation to use remaining days of the week for the specified date. For example, it could be used if a user would like to calculate the total interest not yet incurred during the week.

The following examples assume:

SET FirstWeekDay=0;

| Example | Result |
| --- | --- |
| weekend('01/10/2013') | Returns 01/12/2013 23:59:59. |
| weekend('01/10/2013', -1) | Returns 01/05/2013 23:59:59.. |
| weekend('01/10/2013', 0, 1) | Returns 01/14/2013 23:59:59. |

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

The examples above results in the following from the weekend() function:

Example of Weekend function

| Date | ISO week end | US week end |
| --- | --- | --- |
| Sat 2020 Dec 26 | 2020-12-27 | 12/26/2020 |
| Sun 2020 Dec 27 | 2020-12-27 | 1/2/2021 |
| Mon 2020 Dec 28 | 2021-01-03 | 1/2/2021 |
| Tue 2020 Dec 29 | 2021-01-03 | 1/2/2021 |
| Wed 2020 Dec 30 | 2021-01-03 | 1/2/2021 |
| Thu 2020 Dec 31 | 2021-01-03 | 1/2/2021 |
| Fri 2021 Jan 1 | 2021-01-03 | 1/2/2021 |
| Sat 2021 Jan 2 | 2021-01-03 | 1/2/2021 |
| Sun 2021 Jan 3 | 2021-01-03 | 1/9/2021 |
| Mon 2021 Jan 4 | 2021-01-10 | 1/9/2021 |
| Tue 2021 Jan 5 | 2021-01-10 | 1/9/2021 |

Information noteThe week ends are on Sundays in the ISO column, and on Saturdays in the US column.

## Example 1 – Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called Transactions.
- The date [field](#glossary-2 "Glossary term") provided in the DateFormat system variable (MM/DD/YYYY) format.
- The creation of a field, end\_of\_week, that returns a timestamp for the end of the week when the transactions took place.

Load script

```
SET FirstWeekDay=6;

Transactions:
    Load
        *,
        weekend(date) as end_of_week,
        timestamp(weekend(date)) as end_of_week_timestamp
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
- end\_of\_week
- end\_of\_week\_timestamp

Results table

| date | end\_of\_week | end\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/08/2022 | 1/8/2022 11:59:59 PM |
| 1/19/2022 | 01/22/2022 | 1/22/2022 11:59:59 PM |
| 2/5/2022 | 02/05/2022 | 2/5/2022 11:59:59 PM |
| 2/28/2022 | 03/05/2022 | 3/5/2022 11:59:59 PM |
| 3/16/2022 | 03/19/2022 | 3/19/2022 11:59:59 PM |
| 4/1/2022 | 04/02/2022 | 4/2/2022 11:59:59 PM |
| 5/7/2022 | 05/07/2022 | 5/7/2022 11:59:59 PM |
| 5/16/2022 | 05/21/2022 | 5/21/2022 11:59:59 PM |
| 6/15/2022 | 06/18/2022 | 6/18/2022 11:59:59 PM |
| 6/26/2022 | 07/02/2022 | 7/2/2022 11:59:59 PM |
| 7/9/2022 | 07/09/2022 | 7/9/2022 11:59:59 PM |
| 7/22/2022 | 07/23/2022 | 7/23/2022 11:59:59 PM |
| 7/23/2022 | 07/23/2022 | 7/23/2022 11:59:59 PM |
| 7/27/2022 | 07/30/2022 | 7/30/2022 11:59:59 PM |
| 8/2/2022 | 08/06/2022 | 8/6/2022 11:59:59 PM |
| 8/8/2022 | 08/13/2022 | 8/13/2022 11:59:59 PM |
| 8/19/2022 | 08/20/2022 | 8/20/2022 11:59:59 PM |
| 9/26/2022 | 10/01/2022 | 10/1/2022 11:59:59 PM |
| 10/14/2022 | 10/15/2022 | 10/15/2022 11:59:59 PM |
| 10/29/2022 | 10/29/2022 | 10/29/2022 11:59:59 PM |

The end\_of\_week field is created in the [preceding load](#glossary-3 "Glossary term") statement by using the weekend() function and passing the date field as the function’s argument.

The weekend() function identifies which week the date value falls into and returns a timestamp for the last millisecond of that week.

Diagram of weekend() function, basic example

![Diagram showing how the weekend function converts a transaction date into a timestamp for the last millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekend-examples-basic.png "Click to view full size")

Transaction 8191 took place on February 5. The FirstWeekDay system variable sets the first day of the week to a Sunday. The weekend() function identifies that the first Saturday after February 5– and therefore the end of the week – was on February 5. Therefore, the end\_of\_week value for that transaction returns the last millisecond of that day, which is February 5 at 11:59:59 PM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, previous\_week\_end,that returns the timestamp for the start of the week before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        weekend(date,-1) as previous_week_end,
        timestamp(weekend(date,-1)) as previous_week_end_timestamp
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
- previous\_week\_end
- previous\_week\_end\_timestamp

Results table

| date | end\_of\_week | end\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/01/2022 | 1/1/2022 11:59:59 PM |
| 1/19/2022 | 01/15/2022 | 1/15/2022 11:59:59 PM |
| 2/5/2022 | 01/29/2022 | 1/29/2022 11:59:59 PM |
| 2/28/2022 | 02/26/2022 | 2/26/2022 11:59:59 PM |
| 3/16/2022 | 03/12/2022 | 3/12/2022 11:59:59 PM |
| 4/1/2022 | 03/26/2022 | 3/26/2022 11:59:59 PM |
| 5/7/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 5/16/2022 | 05/14/2022 | 5/14/2022 11:59:59 PM |
| 6/15/2022 | 06/11/2022 | 6/11/2022 11:59:59 PM |
| 6/26/2022 | 06/25/2022 | 6/25/2022 11:59:59 PM |
| 7/9/2022 | 07/02/2022 | 7/2/2022 11:59:59 PM |
| 7/22/2022 | 07/16/2022 | 7/16/2022 11:59:59 PM |
| 7/23/2022 | 07/16/2022 | 7/16/2022 11:59:59 PM |
| 7/27/2022 | 07/23/2022 | 7/23/2022 11:59:59 PM |
| 8/2/2022 | 07/30/2022 | 7/30/2022 11:59:59 PM |
| 8/8/2022 | 08/06/2022 | 8/6/2022 11:59:59 PM |
| 8/19/2022 | 08/13/2022 | 8/13/2022 11:59:59 PM |
| 9/26/2022 | 09/24/2022 | 9/24/2022 11:59:59 PM |
| 10/14/2022 | 10/08/2022 | 10/8/2022 11:59:59 PM |
| 10/29/2022 | 10/22/2022 | 10/22/2022 11:59:59 PM |

In this instance, because a period\_no of -1 was used as the offset argument in the weekend() function, the function first identifies the week in which the transactions take place. It then looks one week prior and identifies the last millisecond of that week.

Diagram of weekend() function, period\_no example

![Diagram showing how the weekend function converts a transaction date into a timestamp for the last millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekend-examples-period-no.png "Click to view full size")

Transaction 8196 took place on June 15. The weekend() function identifies that the week begins on June 12. Therefore, the previous week ends on June 11 at 11:59:59 PM; this is the value returned for the previous\_week\_end field.

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
        weekend(date,0,1) as end_of_week,
        timestamp(weekend(date,0,1)) as end_of_week_timestamp,
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
- end\_of\_week
- end\_of\_week\_timestamp

Results table

| date | end\_of\_week | end\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/10/2022 | 1/10/2022 11:59:59 PM |
| 1/19/2022 | 01/24/2022 | 1/24/2022 11:59:59 PM |
| 2/5/2022 | 02/07/2022 | 2/7/2022 11:59:59 PM |
| 2/28/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 3/16/2022 | 03/21/2022 | 3/21/2022 11:59:59 PM |
| 4/1/2022 | 04/04/2022 | 4/4/2022 11:59:59 PM |
| 5/7/2022 | 05/09/2022 | 5/9/2022 11:59:59 PM |
| 5/16/2022 | 05/16/2022 | 5/16/2022 11:59:59 PM |
| 6/15/2022 | 06/20/2022 | 6/20/2022 11:59:59 PM |
| 6/26/2022 | 06/27/2022 | 6/27/2022 11:59:59 PM |
| 7/9/2022 | 07/11/2022 | 7/11/2022 11:59:59 PM |
| 7/22/2022 | 07/25/2022 | 7/25/2022 11:59:59 PM |
| 7/23/2022 | 07/25/2022 | 7/25/2022 11:59:59 PM |
| 7/27/2022 | 08/01/2022 | 8/1/2022 11:59:59 PM |
| 8/2/2022 | 08/08/2022 | 8/8/2022 11:59:59 PM |
| 8/8/2022 | 08/08/2022 | 8/8/2022 11:59:59 PM |
| 8/19/2022 | 08/22/2022 | 8/22/2022 11:59:59 PM |
| 9/26/2022 | 09/26/2022 | 9/26/2022 11:59:59 PM |
| 10/14/2022 | 10/17/2022 | 10/17/2022 11:59:59 PM |
| 10/29/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |

In this instance, because the first\_week\_date argument of 1 is used in the weekend() function, it sets the first day of the week to Tuesday.

Diagram of weekend() function, first\_week\_day example

![Diagram showing how the weekend function converts a transaction date into a timestamp for the last millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekend-examples-first-week-day.png "Click to view full size")

Transaction 8191 took place on February 5. The weekend() function identifies that the first Monday after the this date – and therefore the end of the week and value returned – was on February 6 at 11:59:59 PM.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the end of the week when the transactions took place is created as a [measure](#glossary-6 "Glossary term") in a chart object of the application.

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

To calculate the start of the week that a transaction takes place in, add the following measures:

- =weekend(date)
- =timestamp(weekend(date))

Results table

| date | =weekend(date) | =timestamp(weekend(date)) |
| --- | --- | --- |
| 1/7/2022 | 01/08/2022 | 1/8/2022 11:59:59 PM |
| 1/19/2022 | 01/22/2022 | 1/22/2022 11:59:59 PM |
| 2/5/2022 | 02/05/2022 | 2/5/2022 11:59:59 PM |
| 2/28/2022 | 03/05/2022 | 3/5/2022 11:59:59 PM |
| 3/16/2022 | 03/19/2022 | 3/19/2022 11:59:59 PM |
| 4/1/2022 | 04/02/2022 | 4/2/2022 11:59:59 PM |
| 5/7/2022 | 05/07/2022 | 5/7/2022 11:59:59 PM |
| 5/16/2022 | 05/21/2022 | 5/21/2022 11:59:59 PM |
| 6/15/2022 | 06/18/2022 | 6/18/2022 11:59:59 PM |
| 6/26/2022 | 07/02/2022 | 7/2/2022 11:59:59 PM |
| 7/9/2022 | 07/09/2022 | 7/9/2022 11:59:59 PM |
| 7/22/2022 | 07/23/2022 | 7/23/2022 11:59:59 PM |
| 7/23/2022 | 07/23/2022 | 7/23/2022 11:59:59 PM |
| 7/27/2022 | 07/30/2022 | 7/30/2022 11:59:59 PM |
| 8/2/2022 | 08/06/2022 | 8/6/2022 11:59:59 PM |
| 8/8/2022 | 08/13/2022 | 8/13/2022 11:59:59 PM |
| 8/19/2022 | 08/20/2022 | 8/20/2022 11:59:59 PM |
| 9/26/2022 | 10/01/2022 | 10/1/2022 11:59:59 PM |
| 10/14/2022 | 10/15/2022 | 10/15/2022 11:59:59 PM |
| 10/29/2022 | 10/29/2022 | 10/29/2022 11:59:59 PM |

The end\_of\_week measure is created in the chart object by using the weekend() function and passing the date field as the function’s argument.
The weekend() function identifies which week the date value falls into, returning a timestamp for the last millisecond of that week.

Diagram of weekend() function, chart object example

![Diagram showing how the weekend function converts a transaction date into a timestamp for the last millisecond of the week in which the transaction took place.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekend-examples-chart-object.png "Click to view full size")

Transaction 8191 took place on February 5. The FirstWeekDay system variable sets the first day of the week to a Sunday. The weekend() function identifies that the first Saturday after February 5 – and therefore the end of the week – was on February 5. Therefore, the end\_of\_week value for that transaction returns the last millisecond of that day, which is February 5 at 11:59:59 PM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Employee\_Expenses.
- Data consisting of employee IDs, employee names, and the average daily expense claims of each employee.

The end user would like a chart object that displays, by employee ID and employee name, the estimated expense claims still to be incurred for the remainder of the week.

Load script

```
Employee_Expenses:
Load
*
Inline
[
employee_id,employee_name,avg_daily_claim
182,Mark, $15
183,Deryck, $12.5
184,Dexter, $12.5
185,Sydney,$27
186,Agatha,$18
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - employee\_id
   - employee\_name
2. Next, create a measure to calculate the accumulated interest:

   =(weekend(today(1))-today(1))\*avg\_daily\_claim
3. Set the measure's Number formatting to Money.

Results table

| employee\_id | employee\_name | =(weekend(today(1))-today(1))\*avg\_daily\_claim |
| --- | --- | --- |
| 182 | Mark | $90.00 |
| 183 | Deryck | $75.00 |
| 184 | Dexter | $75.00 |
| 185 | Sydney | $162.00 |
| 186 | Agatha | $108.00 |

The weekend() function, by using today’s date as its only argument, returns the end date of the current week. Then, by subtracting today’s date from the week end date, the expression returns the number of days that remain this week.

This value is then multiplied by the average daily expense claim by each employee to calculate the estimated value of claims that each employee is expected to make in the remaining week.
