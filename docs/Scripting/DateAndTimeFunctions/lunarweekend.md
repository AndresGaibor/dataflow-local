---
title: "lunarweekend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "sheet"]
---
Expand/Collapse all

# lunarweekend Script and chart function

This function returns a value corresponding to a timestamp of the last millisecond of the last day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

Syntax:

LunarweekEnd(date[, period\_no[, first\_week\_day]])

Return data type:  dual

Example diagram of `lunarweekend()` function

![ADD ALT TEXT HERE.....!!!!!!](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekend-general.png)

The `lunarweekend()` function determines which lunar week the `date` falls into. It then returns a timestamp, in date format, for the last millisecond of that week.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer or expression resolving to an integer, where the value 0 indicates the lunar week which contains date. Negative values in period\_no indicate preceding lunar weeks and positive values indicate succeeding lunar weeks. |
| first\_week\_day | An offset that may be greater than or less than zero. This changes the beginning of the year by the specified number of days and/or fractions of a day. |

## When to use lunarweekend

The `lunarweekend()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of the week that has not yet occurred. Unlike the `weekend()` function, the final lunar week of each calendar year will end on December 31.
For example, the `lunarweekend()` function can be used to calculate interest not yet incurred during the week.

Function examples

| Example | Result |
| --- | --- |
| `lunarweekend('01/12/2013')` | Returns 01/14/2013 23:59:59. |
| `lunarweekend('01/12/2013', -1)` | Returns 01/07/2013 23:59:59. |
| `lunarweekend('01/12/2013', 0, 1)` | Returns 01/15/2013 23:59:59. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-0 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-1 "Glossary term") provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `end_of_week`, that returns a timestamp for the end of the lunar week in which the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekend(date) as end_of_week,
        timestamp(lunarweekend(date)) as end_of_week_timestamp
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

- `date`
- `end_of_week`
- `end_of_week_timestamp`

Results table

| date | end\_of\_week | end\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/07/2022 | 1/7/2022 11:59:59 PM |
| 1/19/2022 | 01/21/2022 | 1/21/2022 11:59:59 PM |
| 2/5/2022 | 02/11/2022 | 2/11/2022 11:59:59 PM |
| 2/28/2022 | 03/04/2022 | 3/4/2022 11:59:59 PM |
| 3/16/2022 | 03/18/2022 | 3/18/2022 11:59:59 PM |
| 4/1/2022 | 04/01/2022 | 4/1/2022 11:59:59 PM |
| 5/7/2022 | 05/13/2022 | 5/13/2022 11:59:59 PM |
| 5/16/2022 | 05/20/2022 | 5/20/2022 11:59:59 PM |
| 6/15/2022 | 06/17/2022 | 6/17/2022 11:59:59 PM |
| 6/26/2022 | 07/01/2022 | 7/1/2022 11:59:59 PM |
| 7/9/2022 | 07/15/2022 | 7/15/2022 11:59:59 PM |
| 7/22/2022 | 07/22/2022 | 7/22/2022 11:59:59 PM |
| 7/23/2022 | 07/29/2022 | 7/29/2022 11:59:59 PM |
| 7/27/2022 | 07/29/2022 | 7/29/2022 11:59:59 PM |
| 8/2/2022 | 08/05/2022 | 8/5/2022 11:59:59 PM |
| 8/8/2022 | 08/12/2022 | 8/12/2022 11:59:59 PM |
| 8/19/2022 | 08/19/2022 | 8/19/2022 11:59:59 PM |
| 9/26/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 10/14/2022 | 10/14/2022 | 10/14/2022 11:59:59 PM |
| 10/29/2022 | 11/04/2022 | 11/4/2022 11:59:59 PM |

The `end_of_week` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-3 "Glossary term") statement by using the `lunarweekend()` function, and passing the `date` field as the function’s argument.

The `lunarweekend()` function identifies which lunar week the date value falls into, returning a timestamp for the last millisecond of that week.

Diagram of `lunarweekend()` function, example with no additional arguments

![Diagram showing how the lunarweekend function converts the input date for each transaction into a timestamp for the last millisecond of the lunar week in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekend-examples-no-add-arg.png)

Transaction 8189 took place on January 19. The `lunarweekend()` function identifies that the lunar week begins on January 15. Therefore, the `end_of_week` value for that transaction returns the last millisecond of the lunar week, which is January 21 at 11:59:59 PM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_lunar_week_end`, that returns the timestamp for the end of the lunar week before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekend(date,-1) as previous_lunar_week_end,
        timestamp(lunarweekend(date,-1)) as previous_lunar_week_end_timestamp
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

- `date`
- `previous_lunar_week_end`
- `previous_lunar_week_end_timestamp`

Results table

| date | previous\_lunar\_week\_end | previous\_lunar\_week\_end\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 1/19/2022 | 01/14/2022 | 1/14/2022 11:59:59 PM |
| 2/5/2022 | 02/04/2022 | 2/4/2022 11:59:59 PM |
| 2/28/2022 | 02/25/2022 | 2/25/2022 11:59:59 PM |
| 3/16/2022 | 03/11/2022 | 3/18/2022 11:59:59 PM |
| 4/1/2022 | 03/25/2022 | 3/25/2022 11:59:59 PM |
| 5/7/2022 | 05/06/2022 | 5/6/2022 11:59:59 PM |
| 5/16/2022 | 05/13/2022 | 5/13/2022 11:59:59 PM |
| 6/15/2022 | 06/10/2022 | 6/10/2022 11:59:59 PM |
| 6/26/2022 | 06/24/2022 | 6/24/2022 11:59:59 PM |
| 7/9/2022 | 07/08/2022 | 7/8/2022 11:59:59 PM |
| 7/22/2022 | 07/15/2022 | 7/15/2022 11:59:59 PM |
| 7/23/2022 | 07/22/2022 | 7/22/2022 11:59:59 PM |
| 7/27/2022 | 07/22/2022 | 7/22/2022 11:59:59 PM |
| 8/2/2022 | 07/29/2022 | 7/29/2022 11:59:59 PM |
| 8/8/2022 | 08/05/2022 | 8/5/2022 11:59:59 PM |
| 8/19/2022 | 08/12/2022 | 8/12/2022 11:59:59 PM |
| 9/26/2022 | 09/23/2022 | 9/23/2022 11:59:59 PM |
| 10/14/2022 | 10/07/2022 | 10/7/2022 11:59:59 PM |
| 10/29/2022 | 10/28/2022 | 10/28/2022 11:59:59 PM |

In this instance, because a `period_no` of -1 was used as the offset argument in the `lunarweekend()` function, the function first identifies the lunar week in which the transactions took place. It then shifts one week prior and identifies the final millisecond of that lunar week.

Diagram of `lunarweekend()` function, period\_no example

![Diagram showing how the lunarweekend function converts the input date for each transaction into a timestamp for the last millisecond of the lunar week in which this date occurs. Here, a period_no of -1 is passed as an argument in the function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekend-examples-period-no.png)

Transaction 8189 took place on January 19. The `lunarweekend()` function identifies that the lunar week begins on January 15. Therefore, the previous lunar week began on the January 8 and ended on January 14 at 11:59:59 PM; this is the value that is returned for the `previous_lunar_week_end` field.

## Example 3 – first\_week\_day

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. In this example, we set lunar weeks to begin on January 5.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekend(date,0,4) as end_of_week,
timestamp(lunarweekend(date,0,4)) as end_of_week_timestamp
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

- `date`
- `end_of_week`
- `end_of_week_timestamp`

Results table

| date | end\_of\_week | end\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/11/2022 | 1/11/2022 11:59:59 PM |
| 1/19/2022 | 01/25/2022 | 1/25/2022 11:59:59 PM |
| 2/5/2022 | 02/08/2022 | 2/8/2022 11:59:59 PM |
| 2/28/2022 | 03/01/2022 | 3/1/2022 11:59:59 PM |
| 3/16/2022 | 03/22/2022 | 3/22/2022 11:59:59 PM |
| 4/1/2022 | 04/05/2022 | 4/5/2022 11:59:59 PM |
| 5/7/2022 | 05/10/2022 | 5/10/2022 11:59:59 PM |
| 5/16/2022 | 05/17/2022 | 5/17/2022 11:59:59 PM |
| 6/15/2022 | 06/21/2022 | 6/21/2022 11:59:59 PM |
| 6/26/2022 | 06/28/2022 | 6/28/2022 11:59:59 PM |
| 7/9/2022 | 07/12/2022 | 7/12/2022 11:59:59 PM |
| 7/22/2022 | 07/26/2022 | 7/26/2022 11:59:59 PM |
| 7/23/2022 | 07/26/2022 | 7/26/2022 11:59:59 PM |
| 7/27/2022 | 08/02/2022 | 8/2/2022 11:59:59 PM |
| 8/2/2022 | 08/02/2022 | 8/2/2022 11:59:59 PM |
| 8/8/2022 | 08/09/2022 | 8/9/2022 11:59:59 PM |
| 8/19/2022 | 08/23/2022 | 8/23/2022 11:59:59 PM |
| 9/26/2022 | 09/27/2022 | 9/27/2022 11:59:59 PM |
| 10/14/2022 | 10/18/2022 | 10/18/2022 11:59:59 PM |
| 10/29/2022 | 11/01/2022 | 11/1/2022 11:59:59 PM |

In this instance, because the `first_week_date` argument of 4 is used in the `lunarweekend()` function, it offsets the start of the year from January 1 to January 5.

Diagram of `lunarweekend()` function, first\_week\_day example

![Diagram showing how the lunarweekend function converts the input date for each transaction into a timestamp for the last millisecond of the lunar week in which this date occurs. Here, the first_week_day argument is defined as 4, which shifts the start of lunar weeks by 4 days.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekend-examples-first-week-day.png)

Transaction 8189 took place on January 19. Due to lunar weeks beginning on January 5, the `lunarweekend()` function identifies that the lunar week containing January 19 also begins on January 19. Therefore, the end of that lunar week occurs on January 25 at 11:59:59 PM; this is the value returned for the `end_of_week` field.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the end of the lunar week in which the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-6 "Glossary term") in a chart object of the application.

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

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Add the following measures:

`=lunarweekend(date)`

`=timestamp(lunarweekend(date))`

Results table

| date | =lunarweekend(date) | =timestamp(lunarweekend(date)) |
| --- | --- | --- |
| 1/7/2022 | 01/07/2022 | 1/7/2022 11:59:59 PM |
| 1/19/2022 | 01/21/2022 | 1/21/2022 11:59:59 PM |
| 2/5/2022 | 02/11/2022 | 2/11/2022 11:59:59 PM |
| 2/28/2022 | 03/04/2022 | 3/4/2022 11:59:59 PM |
| 3/16/2022 | 03/18/2022 | 3/18/2022 11:59:59 PM |
| 4/1/2022 | 04/01/2022 | 4/1/2022 11:59:59 PM |
| 5/7/2022 | 05/13/2022 | 5/13/2022 11:59:59 PM |
| 5/16/2022 | 05/20/2022 | 5/20/2022 11:59:59 PM |
| 6/15/2022 | 06/17/2022 | 6/17/2022 11:59:59 PM |
| 6/26/2022 | 07/01/2022 | 7/1/2022 11:59:59 PM |
| 7/9/2022 | 07/15/2022 | 7/15/2022 11:59:59 PM |
| 7/22/2022 | 07/22/2022 | 7/22/2022 11:59:59 PM |
| 7/23/2022 | 07/29/2022 | 7/29/2022 11:59:59 PM |
| 7/27/2022 | 07/29/2022 | 7/29/2022 11:59:59 PM |
| 8/2/2022 | 08/05/2022 | 8/5/2022 11:59:59 PM |
| 8/8/2022 | 08/12/2022 | 8/12/2022 11:59:59 PM |
| 8/19/2022 | 08/19/2022 | 8/19/2022 11:59:59 PM |
| 9/26/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 10/14/2022 | 10/14/2022 | 10/14/2022 11:59:59 PM |
| 10/29/2022 | 11/04/2022 | 11/4/2022 11:59:59 PM |

The `end_of_week` measure is created in the chart object by using the `lunarweekend()` function, and passing the `date` field as the function’s argument.

The `lunarweekend()` function identifies which lunar week the date value falls into, returning a timestamp for the last millisecond of that week.

Diagram of `lunarweekend()` function, chart object example

![Diagram showing how the lunarweekend function converts the input date for each transaction into a timestamp for the last millisecond of the lunar week in which this date occurs. In this case, the calculation shown is completed using a measure in a chart object.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekend-examples-chart-object.png)

Transaction 8189 took place on January 19. The `lunarweekend()` function identifies that the lunar week begins on January 15. Therefore, the `end_of_week` value for that transaction returns the last millisecond of the lunar week, which is January 21 at 11:59:59 PM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called `Employee_Expenses`.
- The employee IDs, employee name and the average daily expense claims of each employee.

The end user would like a chart object that displays, by employee ID and employee name, the estimated expense claims still to be incurred for the remainder of the lunar week.

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

1. Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-7 "Glossary term"). Create a new table.
2. Add the following fields as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm#glossary-8 "Glossary term").

   - `employee_id`
   - `employee_name`
3. Next, create the following measure to calculate the accumulated interest:

   `=(lunarweekend(today(1))-today(1))*avg_daily_claim`
4. Set the measure's **Number formatting** to **Money**.

Results table

| employee\_id | employee\_name | =(lunarweekend(today(1))-today(1))\*avg\_daily\_claim |
| --- | --- | --- |
| 182 | Mark | $75.00 |
| 183 | Deryck | $62.50 |
| 184 | Dexter | $62.50 |
| 185 | Sydney | $135.00 |
| 186 | Agatha | $90.00 |

The `lunarkweekend()` function, by using today’s date as its only argument, returns the end date of the current lunar week. Then, by subtracting today’s date from the lunar week end date, the expression returns the number of days that remain this week.

This value is then multiplied by the average daily expense claim by each employee to calculate the estimated value of claims each employee is expected to make in the remaining lunar week.
