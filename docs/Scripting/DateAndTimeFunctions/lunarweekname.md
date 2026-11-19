---
title: "lunarweekname Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "sheet"]
---
Expand/Collapse all

# lunarweekname Script and chart function

This function returns a display value showing the year and lunar week number corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

Syntax:

LunarWeekName(date [, period\_no[, first\_week\_day]])

Return data type:  dual

Example diagram of `lunarweekname()` function

![Example diagram showing how the lunarweekname function converts an input date into a value displaying a combination of year and lunar week number.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekname-general.png)

The `lunarweekname()` function determines which lunar week the date falls into, beginning a week count from January 1. It then returns a value comprised of `year/weekcount`.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer or expression resolving to an integer, where the value 0 indicates the lunar week which contains date. Negative values in period\_no indicate preceding lunar weeks and positive values indicate succeeding lunar weeks. |
| first\_week\_day | An offset that may be greater than or less than zero. This changes the beginning of the year by the specified number of days and/or fractions of a day. |

## When to use lunarweekname

The `lunarweekname()` function is useful when you would like to compare aggregations by lunar weeks. For example, the function could be used to determine the total sales of products by lunar week. Lunar weeks are useful when you would like to ensure that all values contained in the first week of the year contain only values from January 1 at the earliest.

These [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-0 "Glossary term") can be created in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-1 "Glossary term") by using the function to create a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-2 "Glossary term") in a Master Calendar table. The function can also be used directly in a [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-3 "Glossary term") as a calculated [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-4 "Glossary term").

Function examples

| Example | Result |
| --- | --- |
| `lunarweekname('01/12/2013')` | Returns 2006/02. |
| `lunarweekname('01/12/2013', -1)` | Returns 2006/01. |
| `lunarweekname('01/12/2013', 0, 1)` | Returns 2006/02. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – date with no additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-5 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-6 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `lunar_week_name`, that returns the year and week number for the lunar week in which the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekname(date) as lunar_week_name
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
- `lunar_week_name`

Results table

| date | lunar\_week\_name |
| --- | --- |
| 1/7/2022 | 2022/01 |
| 1/19/2022 | 2022/03 |
| 2/5/2022 | 2022/06 |
| 2/28/2022 | 2022/09 |
| 3/16/2022 | 2022/11 |
| 4/1/2022 | 2022/13 |
| 5/7/2022 | 2022/19 |
| 5/16/2022 | 2022/20 |
| 6/15/2022 | 2022/24 |
| 6/26/2022 | 2022/26 |
| 7/9/2022 | 2022/28 |
| 7/22/2022 | 2022/29 |
| 7/23/2022 | 2022/30 |
| 7/27/2022 | 2022/30 |
| 8/2/2022 | 2022/31 |
| 8/8/2022 | 2022/32 |
| 8/19/2022 | 2022/33 |
| 9/26/2022 | 2022/39 |
| 10/14/2022 | 2022/41 |
| 10/29/2022 | 2022/44 |

The `lunar_week_name` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-7 "Glossary term") statement by using the `lunarweekname()` function, and passing the `date` field as the function’s argument.

The `lunarweekname()` function identifies which lunar week the date value falls into, returning the year and week number of that date.

Diagram of `lunarweekname()` function, example with no additional arguments

![Diagram showing how the lunarweekname function converts an input date into a value displaying a combination of year and lunar week number. Here, date is passed into the function as its only parameter.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekname-examples-no-add-arg.png)

Transaction 8189 took place on January 19. The `lunarweekname()` function identifies that this date falls into the lunar week beginning on January 15; this is the third lunar week of the year. Therefore, the `lunar_week_name` value returned for that transaction is 2022/03.

## Example 2 – date with period\_no argument

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_lunar_week_name`, that returns the year and week number for the lunar week prior to when the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekname(date,-1) as previous_lunar_week_name
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
- `previous_lunar_week_name`

Results table

| date | previous\_lunar\_week\_name |
| --- | --- |
| 1/7/2022 | 2021/52 |
| 1/19/2022 | 2022/02 |
| 2/5/2022 | 2022/05 |
| 2/28/2022 | 2022/08 |
| 3/16/2022 | 2022/10 |
| 4/1/2022 | 2022/12 |
| 5/7/2022 | 2022/18 |
| 5/16/2022 | 2022/19 |
| 6/15/2022 | 2022/23 |
| 6/26/2022 | 2022/25 |
| 7/9/2022 | 2022/27 |
| 7/22/2022 | 2022/28 |
| 7/23/2022 | 2022/29 |
| 7/27/2022 | 2022/29 |
| 8/2/2022 | 2022/30 |
| 8/8/2022 | 2022/31 |
| 8/19/2022 | 2022/32 |
| 9/26/2022 | 2022/38 |
| 10/14/2022 | 2022/40 |
| 10/29/2022 | 2022/43 |

In this instance, because a `period_no` of -1 was used as the offset argument in the `lunarweekname()` function, the function first identifies the lunar week in which the transactions took place. It then returns the year and the number of one week prior.

Diagram of `lunarweekname()` function, period\_no example

![Diagram showing how the lunarweekname function converts the input date for a transaction into a combined value displaying the year and week number for the lunar week in which the transaction happened. Here, a period_no of -1 is passed as an additional parameter into the function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekname-examples-period-no.png)

Transaction 8189 took place on January 19. The `lunarweekname()` function identifies that this transaction took place in the third lunar week of the year, so it then returns the year and value for one week prior, 2022/02, for the `previous_lunar_week_name` field.

## Example 3 – date with first\_week\_day argument

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-8 "Glossary term") and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example. In this example, we set lunar weeks to begin on January 5.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        lunarweekname(date,0,4) as lunar_week_name
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
- `lunar_week_name`

Results table

| date | lunar\_week\_name |
| --- | --- |
| 1/7/2022 | 2022/01 |
| 1/19/2022 | 2022/03 |
| 2/5/2022 | 2022/05 |
| 2/28/2022 | 2022/08 |
| 3/16/2022 | 2022/11 |
| 4/1/2022 | 2022/13 |
| 5/7/2022 | 2022/18 |
| 5/16/2022 | 2022/19 |
| 6/15/2022 | 2022/24 |
| 6/26/2022 | 2022/25 |
| 7/9/2022 | 2022/27 |
| 7/22/2022 | 2022/29 |
| 7/23/2022 | 2022/29 |
| 7/27/2022 | 2022/30 |
| 8/2/2022 | 2022/30 |
| 8/8/2022 | 2022/31 |
| 8/19/2022 | 2022/33 |
| 9/26/2022 | 2022/38 |
| 10/14/2022 | 2022/41 |
| 10/29/2022 | 2022/43 |

Diagram of `lunarweekname()` function, first\_week\_day example

![Diagram showing how the lunarweekname function converts the input date for each transaction into a combined value displaying the year and lunar week number. Here, the first_week_day argument is defined as 4, which shifts the start of lunar weeks by 4 days.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekname-examples-first-week-day.png)

In this instance, because the `first_week_date` argument of 4 is used in the `lunarweekname()` function, it offsets the start of lunar weeks from January 1 to January 5.

Transaction 8188 took place on January 7. Due to lunar weeks beginning on January 5, the `lunarweekname()` function identifies that the lunar week containing January 7 is the first lunar week of the year. Therefore, the returned `lunar_week_name` value for that transaction is 2022/01.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns the lunar week number and year in which the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-9 "Glossary term") in a chart object of the application.

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

To calculate the start date of the lunar week in which a transaction takes place, create the following measure:

`=lunarweekname(date)`

Results table

| date | =lunarweekname(date) |
| --- | --- |
| 1/7/2022 | 2022/01 |
| 1/19/2022 | 2022/03 |
| 2/5/2022 | 2022/06 |
| 2/28/2022 | 2022/09 |
| 3/16/2022 | 2022/11 |
| 4/1/2022 | 2022/13 |
| 5/7/2022 | 2022/19 |
| 5/16/2022 | 2022/20 |
| 6/15/2022 | 2022/24 |
| 6/26/2022 | 2022/26 |
| 7/9/2022 | 2022/28 |
| 7/22/2022 | 2022/29 |
| 7/23/2022 | 2022/30 |
| 7/27/2022 | 2022/30 |
| 8/2/2022 | 2022/31 |
| 8/8/2022 | 2022/32 |
| 8/19/2022 | 2022/33 |
| 9/26/2022 | 2022/39 |
| 10/14/2022 | 2022/41 |
| 10/29/2022 | 2022/44 |

The `lunar_week_name` measure is created in the chart object by using the `lunarweekname()` function and passing the `date` field as the function’s argument.

The `lunarweekname()` function identifies which lunar week the date value falls into, returning the year and week number of that date.

Diagram of `lunarweekname()` function, chart object example

![Diagram showing how the lunarweekname function converts an input date into a value displaying a combination of year and lunar week number. Here, a chart object is used to perform the calculation.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-lunarweekname-examples-chart-object.png)

Transaction 8189 took place on January 19. The `lunarweekname()` function identifies that this date falls into the lunar week beginning on January 15; this is the third lunar week of the year. Therefore, the `lunar_week_name` value for that transaction is 2022/03.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.

The end user would like a chart object that presents the total sales by week for the current year. Week 1, with a length of seven days, should begin on January 1. This could be achieved even when this dimension is not available in the data model by using the `lunarweekname()` function as a calculated dimension in the chart.

Load script

```
SET DateFormat='MM/DD/YYYY';

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

Do the following:

1. Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-10 "Glossary term"). Create a new table.
2. Create a calculated dimension using the following expression:

   `=lunarweekname(date)`
3. Calculate total sales using the following [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm#glossary-11 "Glossary term") measure:

   `=sum(amount)`
4. Set the measure's **Number formatting** to **Money**.

Results table

| =lunarweekname(date) | =sum(amount) |
| --- | --- |
| 2022/01 | $17.17 |
| 2022/03 | $37.23 |
| 2022/06 | $57.42 |
| 2022/09 | $88.27 |
| 2022/11 | $53.80 |
| 2022/13 | $82.06 |
| 2022/19 | $40.39 |
| 2022/20 | $87.21 |
| 2022/24 | $95.93 |
| 2022/26 | $45.89 |
| 2022/28 | $36.23 |
| 2022/29 | $25.66 |
| 2022/30 | $152.75 |
| 2022/31 | $76.11 |
| 2022/32 | $25.12 |
| 2022/33 | $46.23 |
| 2022/39 | $84.21 |
| 2022/41 | $96.24 |
| 2022/44 | $67.67 |
