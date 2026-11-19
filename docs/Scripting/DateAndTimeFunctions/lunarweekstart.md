---
title: "lunarweekstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "sheet"]
---
Expand/Collapse all

# lunarweekstart Script and chart function

This function returns a value corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

Syntax:

LunarweekStart(date[, period\_no[, first\_week\_day]])

Return data type:  dual

The `lunarweekstart()` function determines which lunar week the `date` falls into. It then returns a timestamp, in date format, for the first millisecond of that week.

Example diagram of `lunarweekstart()` function

![Example diagram showing how the lunarweekstart function converts an input date into a timestamp for the first millisecond of the lunar week in which the input date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekstart-general.png)

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer or expression resolving to an integer, where the value 0 indicates the lunar week which contains date. Negative values in period\_no indicate preceding lunar weeks and positive values indicate succeeding lunar weeks. |
| first\_week\_day | An offset that may be greater than or less than zero. This changes the beginning of the year by the specified number of days and/or fractions of a day. |

## When to use lunarweekstart

The `lunarweekstart()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of the week that has elapsed thus far. Unlike the `weekstart()` function, at the start of each new calendar year, week’s begin on January 1 and each subsequent week begins seven days later. The `lunarweekstart()` function is not affected by the `FirstWeekDay` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-0 "Glossary term").

For example, the `lunarweekstart()` can be used to calculate the interest that has been accumulated in a week to date.

Function examples

| Example | Result |
| --- | --- |
| `lunarweekstart('01/12/2013')` | Returns 01/08/2013. |
| `lunarweekstart('01/12/2013', -1)` | Returns 01/01/2013. |
| `lunarweekstart('01/12/2013', 0, 1 )` | Returns 01/09/2013, because setting first\_week\_day to 1 means the beginning of the year is changed to 01/02/2013. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.
- The creation of a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-2 "Glossary term") `start_of_week`, that returns a timestamp for the start of the lunar week in which the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekstart(date) as start_of_week,
        timestamp(lunarweekstart(date)) as start_of_week_timestamp
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
- `start_of_week`
- `start_of_week_timestamp`

Results table

| date | start\_of\_week | start\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/15/2022 | 1/15/2022 12:00:00 AM |
| 2/5/2022 | 02/05/2022 | 2/5/2022 12:00:00 AM |
| 2/28/2022 | 02/26/2022 | 2/26/2022 12:00:00 AM |
| 3/16/2022 | 03/12/2022 | 3/12/2022 12:00:00 AM |
| 4/1/2022 | 03/26/2022 | 3/26/2022 12:00:00 AM |
| 5/7/2022 | 05/07/2022 | 5/7/2022 12:00:00 AM |
| 5/16/2022 | 05/14/2022 | 5/14/2022 12:00:00 AM |
| 6/15/2022 | 06/11/2022 | 6/11/2022 12:00:00 AM |
| 6/26/2022 | 06/25/2022 | 6/25/2022 12:00:00 AM |
| 7/9/2022 | 07/09/2022 | 7/9/2022 12:00:00 AM |
| 7/22/2022 | 07/16/2022 | 7/16/2022 12:00:00 AM |
| 7/23/2022 | 07/23/2022 | 7/23/2022 12:00:00 AM |
| 7/27/2022 | 07/23/2022 | 7/23/2022 12:00:00 AM |
| 8/2/2022 | 07/30/2022 | 7/30/2022 12:00:00 AM |
| 8/8/2022 | 08/06/2022 | 8/6/2022 12:00:00 AM |
| 8/19/2022 | 08/13/2022 | 8/13/2022 12:00:00 AM |
| 9/26/2022 | 09/24/2022 | 9/24/2022 12:00:00 AM |
| 10/14/2022 | 10/08/2022 | 10/8/2022 12:00:00 AM |
| 10/29/2022 | 10/29/2022 | 10/29/2022 12:00:00 AM |

The `start_of_week` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-3 "Glossary term") statement by using the `lunarweekstart()` function and passing the `date` field as the function’s argument.

The `lunarweekstart()` function identifies the lunar week into which the date falls, returning a timestamp for the first millisecond of that week.

Diagram of `lunarweekstart()` function, example with no additional arguments

![Diagram showing how the lunarweekstart function converts the input date for each transaction into a timestamp for the first millisecond of the lunar week in which this date occurs. Here, the date field is passed into the function as its only argument.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekstart-examples-no-add-arg.png)

Transaction 8189 took place on January 19. The `lunarweekstart()` function identifies that the lunar week begins on January 15. Therefore, the `start_of_week` value for that transaction returns the first millisecond of that day, which is January 15 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_lunar_week_start`, that returns the timestamp for the start of the lunar week before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekstart(date,-1) as previous_lunar_week_start,
        timestamp(lunarweekstart(date,-1)) as previous_lunar_week_start_timestamp
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

Results table

| date | previous\_lunar\_week\_start | previous\_lunar\_week\_start\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 12/24/2021 | 12/24/2021 12:00:00 AM |
| 1/19/2022 | 01/08/2022 | 1/8/2022 12:00:00 AM |
| 2/5/2022 | 01/29/2022 | 1/29/2022 12:00:00 AM |
| 2/28/2022 | 02/19/2022 | 2/19/2022 12:00:00 AM |
| 3/16/2022 | 03/05/2022 | 3/5/2022 12:00:00 AM |
| 4/1/2022 | 03/19/2022 | 3/19/2022 12:00:00 AM |
| 5/7/2022 | 04/30/2022 | 4/30/2022 12:00:00 AM |
| 5/16/2022 | 05/07/2022 | 5/7/2022 12:00:00 AM |
| 6/15/2022 | 06/04/2022 | 6/4/2022 12:00:00 AM |
| 6/26/2022 | 06/18/2022 | 6/18/2022 12:00:00 AM |
| 7/9/2022 | 07/02/2022 | 7/2/2022 12:00:00 AM |
| 7/22/2022 | 07/09/2022 | 7/9/2022 12:00:00 AM |
| 7/23/2022 | 07/16/2022 | 7/16/2022 12:00:00 AM |
| 7/27/2022 | 07/16/2022 | 7/16/2022 12:00:00 AM |
| 8/2/2022 | 07/23/2022 | 7/23/2022 12:00:00 AM |
| 8/8/2022 | 07/30/2022 | 7/30/2022 12:00:00 AM |
| 8/19/2022 | 08/06/2022 | 8/6/2022 12:00:00 AM |
| 9/26/2022 | 09/17/2022 | 9/17/2022 12:00:00 AM |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/22/2022 | 10/22/2022 12:00:00 AM |

In this instance, because a `period_no` of -1 was used as the offset argument in the `lunarweekstart()` function, the function first identifies the lunar week that the transactions take place in. It then shifts one week prior and identifies the first millisecond of that lunar week.

Diagram of `lunarweekstart()` function, period\_no example

![Diagram showing how the lunarweekstart function converts the input date for each transaction into a timestamp for the first millisecond of the lunar week in which this date occurs. Here, a period_no of -1 is passed as an argument in the function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekstart-examples-period-no.png)

Transaction 8189 took place on January 19. The `lunarweekstart()` function identifies that the lunar week begins on January 15. Therefore, the previous lunar week began on January 8 at 12:00:00 AM; this is the value returned for the `previous_lunar_week_start` field.

## Example 3 – first\_week\_day

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. In this example, we set lunar weeks to begin on January 5.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekstart(date,0,4) as start_of_week,
        timestamp(lunarweekstart(date,0,4)) as start_of_week_timestamp
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
- `start_of_week`
- `start_of_week_timestamp`

Results table

| date | start\_of\_week | start\_of\_week\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/05/2022 | 1/5/2022 12:00:00 AM |
| 1/19/2022 | 01/19/2022 | 1/19/2022 12:00:00 AM |
| 2/5/2022 | 02/02/2022 | 2/2/2022 12:00:00 AM |
| 2/28/2022 | 02/23/2022 | 2/23/2022 12:00:00 AM |
| 3/16/2022 | 03/16/2022 | 3/16/2022 12:00:00 AM |
| 4/1/2022 | 03/30/2022 | 3/30/2022 12:00:00 AM |
| 5/7/2022 | 05/04/2022 | 5/4/2022 12:00:00 AM |
| 5/16/2022 | 05/11/2022 | 5/11/2022 12:00:00 AM |
| 6/15/2022 | 06/15/2022 | 6/15/2022 12:00:00 AM |
| 6/26/2022 | 06/22/2022 | 6/22/2022 12:00:00 AM |
| 7/9/2022 | 07/06/2022 | 7/6/2022 12:00:00 AM |
| 7/22/2022 | 07/20/2022 | 7/20/2022 12:00:00 AM |
| 7/23/2022 | 07/20/2022 | 7/20/2022 12:00:00 AM |
| 7/27/2022 | 07/27/2022 | 7/27/2022 12:00:00 AM |
| 8/2/2022 | 07/27/2022 | 7/27/2022 12:00:00 AM |
| 8/8/2022 | 08/03/2022 | 8/3/2022 12:00:00 AM |
| 8/19/2022 | 08/17/2022 | 8/17/2022 12:00:00 AM |
| 9/26/2022 | 09/21/2022 | 9/21/2022 12:00:00 AM |
| 10/14/2022 | 10/12/2022 | 10/12/2022 12:00:00 AM |
| 10/29/2022 | 10/26/2022 | 10/26/2022 12:00:00 AM |

In this instance, because the `first_week_date` argument of 4 is used in the `lunarweekstart()` function, it offsets the start of the year from January 1 to January 5.

Diagram of `lunarweekstart()` function, first\_week\_day example

![ADD ALT TEXT HERE.....!!!!!!](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekstart-examples-first-week-day.png)

Transaction 8189 took place on January 19. Due to lunar weeks beginning on January 5, the `lunarweekstart()` function identifies that the lunar week containing January 19 begins on January 19 at 12:00:00 AM as well. Therefore, that is the value returned for the `start_of_week` field.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the start of the lunar week in which the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-6 "Glossary term") in a chart object of the application.

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

`=lunarweekstart(date)`

`=timestamp(lunarweekstart(date))`

Results table

| date | =lunarweekstart(date) | =timestamp(lunarweekstart(date)) |
| --- | --- | --- |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/15/2022 | 1/15/2022 12:00:00 AM |
| 2/5/2022 | 02/05/2022 | 2/5/2022 12:00:00 AM |
| 2/28/2022 | 02/26/2022 | 2/26/2022 12:00:00 AM |
| 3/16/2022 | 03/12/2022 | 3/12/2022 12:00:00 AM |
| 4/1/2022 | 03/26/2022 | 3/26/2022 12:00:00 AM |
| 5/7/2022 | 05/07/2022 | 5/7/2022 12:00:00 AM |
| 5/16/2022 | 05/14/2022 | 5/14/2022 12:00:00 AM |
| 6/15/2022 | 06/11/2022 | 6/11/2022 12:00:00 AM |
| 6/26/2022 | 06/25/2022 | 6/25/2022 12:00:00 AM |
| 7/9/2022 | 07/09/2022 | 7/9/2022 12:00:00 AM |
| 7/22/2022 | 07/16/2022 | 7/16/2022 12:00:00 AM |
| 7/23/2022 | 07/23/2022 | 7/23/2022 12:00:00 AM |
| 7/27/2022 | 07/23/2022 | 7/23/2022 12:00:00 AM |
| 8/2/2022 | 07/30/2022 | 7/30/2022 12:00:00 AM |
| 8/8/2022 | 08/06/2022 | 8/6/2022 12:00:00 AM |
| 8/19/2022 | 08/13/2022 | 8/13/2022 12:00:00 AM |
| 9/26/2022 | 09/24/2022 | 9/24/2022 12:00:00 AM |
| 10/14/2022 | 10/08/2022 | 10/8/2022 12:00:00 AM |
| 10/29/2022 | 10/29/2022 | 10/29/2022 12:00:00 AM |

The `start_of_week` measure is created in the chart object by using the `lunarweekstart()` function, and passing the date field as the function’s argument.

The `lunarweekstart()` function identifies which lunar week the date value falls into, returning a timestamp for the last millisecond of that week.

Diagram of `lunarweekstart()` function, chart object example

![Diagram showing how the lunarweekstart function converts the input date for each transaction into a timestamp for the first millisecond of the lunar week in which this date occurs. In this case, the calculation shown is completed using a measure in a chart object.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekstart-examples-chart-object.png)

Transaction 8189 took place on January 19. The `lunarweekstart()` function identifies that the lunar week begins on January 15. Therefore, the `start_of_week` value for that transaction is first millisecond of that day, which is the January 15 at 12:00:00 AM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of loan balances, which is loaded into a table called `Loans`.
- Data consisting of loan IDs, the balance at the beginning of the week, and the simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan ID, the current interest that has been accrued on each loan in the week to date.

Load script

```
Loans:
Load
*
Inline 
[
loan_id,start_balance,rate
8188,$10000.00,0.024
8189,$15000.00,0.057
8190,$17500.00,0.024
8191,$21000.00,0.034
8192,$90000.00,0.084
];
```

Results

Do the following:

1. Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-7 "Glossary term"). Create a new table.
2. Add the following fields as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm#glossary-8 "Glossary term").

   - `loan_id`
   - `start_balance`
3. Next, create the following measure to calculate the accumulated interest:

   `=start_balance*(rate*(today(1)-lunarweekstart(today(1)))/365)`
4. Set the measure's **Number formatting** to **Money**.

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)- lunarweekstart (today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $15.07 |
| 8189 | $15000.00 | $128.84 |
| 8190 | $17500.00 | $63.29 |
| 8191 | $21000.00 | $107.59 |
| 8192 | $90000.00 | $1139.18 |

The `lunarweekstart()` function, using today’s date as its only argument, returns the start date of the current year. By subtracting that result from the current date, the expression returns the number of days that have elapsed so far this week.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate incurred for this period. The result is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this week.
