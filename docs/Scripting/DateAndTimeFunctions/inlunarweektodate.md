---
title: "inlunarweektodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inlunarweektodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inlunarweektodate Script and chart function

Expand/Collapse all

# inlunarweektodate Script and chart function

This function finds if timestamp lies inside the
part of the lunar week up to and including the last millisecond of base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

Syntax:

InLunarWeekToDate
(timestamp, base\_date, period\_no [, first\_week\_day])

Return data type:  Boolean

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Example diagram of inlunarweektodate() function

![Example diagram of inlunarweektodate function, showing the dates for which the function will return a TRUE value, given the input information.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweektodate-overview.png "Click to view full size")

The inlunarweektodate() function acts as the end point of the lunar week. In contrast, the inlunarweek() function, determines which lunar week the base\_date falls into. For example, if the base\_date were January 5, any timestamp between January 1 and January 5 would return a Boolean result of TRUE, while dates on January 6 and 7, and later, would return a Boolean result of FALSE.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the lunar week. |
| period\_no | The lunar week can be offset by period\_no. period\_no is an integer, where the value 0 indicates the lunar week which contains base\_date. Negative values in period\_no indicate preceding lunar weeks and positive values indicate succeeding lunar weeks. |
| first\_week\_day | An offset that may be greater than or less than zero. This changes the beginning of the year by the specified number of days and/or fractions of a day. |

## When to use inlunarweektodate

The inlunarweektodate() function returns a Boolean result. Typically, this type of function will be used as a condition in an IF expression. The inlunarweektodate() function would be used when the user would like the calculation to return an [aggregation](#glossary-0 "Glossary term") or calculation, dependent on whether the evaluated date occurred during a particular segment of the week in question.

For example, the inlunarweektodate() function can be used to identify all equipment manufactured in a particular week up to and including a particular date.

Function examples

| Example | Result |
| --- | --- |
| inlunarweektodate('01/12/2013', '01/13/2013', 0) | Returns TRUE, since the value of the timestamp, 01/12/2013, falls in the part of the week 01/08/2013 to 01/13/2013. |
| inlunarweektodate('01/12/2013', '01/11/2013', 0) | Returns FALSE, since the value of the timestamp is later than the value of base\_date, even though the two dates are in the same lunar week before 01/12/2012. |
| inlunarweektodate('01/12/2006', '01/05/2006', 1) | Returns TRUE. Specifying a value of 1 for period\_no shifts the base\_date forward one week, so the value of timestamp falls in the part of the lunar week. |

The inlunarweektodate() function is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*lunarweekname Script and chart function*](lunarweekname.htm) | This function is used to determine the lunar week number of the year in which an input date occurs. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for the month of January, which is loaded into a table called Transactions. The default DateFormat system [variable](#glossary-2 "Glossary term") MM/DD/YYYY is used.
- Create a [field](#glossary-3 "Glossary term") in\_lunar\_week\_to\_date, that determines which transactions took place in lunar week to date of January 10.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inlunarweektodate(date,'01/10/2022', 0) as in_lunar_week_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'1/10/2022',37.23
8189,'1/17/2022',17.17
8190,'1/26/2022',88.27
8191,'1/12/2022',57.42
8192,'1/19/2022',53.80
8193,'1/21/2022',82.06
8194,'1/1/2022',40.39
8195,'1/27/2022',87.21
8196,'1/11/2022',95.93
8197,'1/29/2022',45.89
8198,'1/31/2022',36.23
8199,'1/18/2022',25.66
8200,'1/23/2022',82.77
8201,'1/15/2022',69.98
8202,'1/4/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_lunar\_week\_to\_date

Results table

| date | in\_lunar\_week\_to\_date |
| --- | --- |
| 1/1/2022 | 0 |
| 1/4/2022 | 0 |
| 1/10/2022 | -1 |
| 1/11/2022 | 0 |
| 1/12/2022 | 0 |
| 1/15/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/21/2022 | 0 |
| 1/23/2022 | 0 |
| 1/26/2022 | 0 |
| 1/27/2022 | 0 |
| 1/29/2022 | 0 |
| 1/31/2022 | 0 |

inlunarweektodate() function, no additional arguments

![Example of the use of the inlunarweektodate function showing the range of dates for which the function will return a value of TRUE, given the input information. This example contains  no additional arguments.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweektodate-example-no-additional-arguments.png "Click to view full size")

The in\_lunar\_week\_to\_date field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the inlunarweektodate() function and passing the date field, a hard-coded date for January 10 as our base\_date, and an offset of 0 as the function’s arguments.

Because lunar weeks begin on January 1, January 10 would fall in the lunar week that begins on January 8; and because we are using the inlunarweektodate() function, that lunar week would then end on the 10th. Therefore, any transactions that occur between those two dates in January would return a Boolean value of TRUE. This is validated in the results table.

## Example 2 - period\_no

Load script and results

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the [load script](#glossary-6 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the task is to create a field, 2\_lunar\_weeks\_later, that determines whether or not the transactions took place two weeks after the lunar week to date of January 1.

Load script

```
SET DateFormat='MM/DD/YYYY';
Transactions:
    Load
        *,
        inlunarweektodate(date,'01/10/2022', 2) as [2_lunar_weeks_later]
        ;
Load
*
Inline
[
id,date,amount
8188,'1/10/2022',37.23
8189,'1/17/2022',17.17
8190,'1/26/2022',88.27
8191,'1/12/2022',57.42
8192,'1/19/2022',53.80
8193,'1/21/2022',82.06
8194,'1/1/2022',40.39
8195,'1/27/2022',87.21
8196,'1/11/2022',95.93
8197,'1/29/2022',45.89
8198,'1/31/2022',36.23
8199,'1/18/2022',25.66
8200,'1/23/2022',82.77
8201,'1/15/2022',69.98
8202,'1/4/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- 2\_lunar\_weeks\_later

Results table

| date | 2\_lunar\_weeks\_later |
| --- | --- |
| 1/1/2022 | 0 |
| 1/4/2022 | 0 |
| 1/10/2022 | 0 |
| 1/11/2022 | 0 |
| 1/12/2022 | 0 |
| 1/15/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/21/2022 | 0 |
| 1/23/2022 | -1 |
| 1/26/2022 | 0 |
| 1/27/2022 | 0 |
| 1/29/2022 | 0 |
| 1/31/2022 | 0 |

inlunarweektodate() function, period\_no example

![Example of the use of the inlunarweektodate function showing the range of dates for which the function will return a value of TRUE, given the input information. This example contains a period_no value of 2.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweektodate-example-period-no.png "Click to view full size")

In this instance, the inlunarweektodate() function determines that the lunar week up to January 10 equates to three days (January 8, 9, 10). Since a period\_no of 2 was used as the offset argument, this lunar week is shifted by 14 days. Therefore, this defines that three-day lunar week to include January 22, 23, and 24. Any transaction that takes place between January 22 and January 24 will return a Boolean result of TRUE.

## Example 3 - first\_week\_day

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The default DateFormat system variable MM/DD/YYYY is used.
- A first\_week\_date argument of 3. This sets lunar weeks to begin on January 3.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inlunarweek(date,'01/10/2022', 0,3) as in_lunar_week_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'1/10/2022',37.23
8189,'1/17/2022',17.17
8190,'1/26/2022',88.27
8191,'1/12/2022',57.42
8192,'1/19/2022',53.80
8193,'1/21/2022',82.06
8194,'1/1/2022',40.39
8195,'1/27/2022',87.21
8196,'1/11/2022',95.93
8197,'1/29/2022',45.89
8198,'1/31/2022',36.23
8199,'1/18/2022',25.66
8200,'1/23/2022',82.77
8201,'1/15/2022',69.98
8202,'1/4/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_lunar\_week\_to\_date

Results table

| date | in\_lunar\_week\_to\_date |
| --- | --- |
| 1/1/2022 | 0 |
| 1/4/2022 | -1 |
| 1/10/2022 | -1 |
| 1/11/2022 | 0 |
| 1/12/2022 | 0 |
| 1/15/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/21/2022 | 0 |
| 1/23/2022 | 0 |
| 1/26/2022 | 0 |
| 1/27/2022 | 0 |
| 1/29/2022 | 0 |
| 1/31/2022 | 0 |

inlunarweektodate() function, first\_week\_day example

![Example of the use of the inlunarweektodate function showing the range of dates for which the function will return a value of TRUE, given the input information. In this example, we set the first lunar week day as January 4.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweektodate-example-first-week-date.png "Click to view full size")

In this instance, because the first\_week\_date argument of 3 is used in the inlunarweek() function, the first lunar week will be from January 3 to January 10. Because January 10 is also the base\_date, any transaction that falls between these two dates will return a Boolean value of TRUE.

## Example 4 - Chart object example

Load script and chart expression

Overview

Open the Data load editor, and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that determines whether the transactions took place in the lunar week up to January 10 is created as a [measure](#glossary-7 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,'1/10/2022',37.23
8189,'1/17/2022',17.17
8190,'1/26/2022',88.27
8191,'1/12/2022',57.42
8192,'1/19/2022',53.80
8193,'1/21/2022',82.06
8194,'1/1/2022',40.39
8195,'1/27/2022',87.21
8196,'1/11/2022',95.93
8197,'1/29/2022',45.89
8198,'1/31/2022',36.23
8199,'1/18/2022',25.66
8200,'1/23/2022',82.77
8201,'1/15/2022',69.98
8202,'1/4/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

Create the following measure:

=inlunarweektodate(date,'01/10/2022', 0)

Results table

| date | =inlunarweektodate(date,'01/10/2022', 0) |
| --- | --- |
| 1/1/2022 | 0 |
| 1/4/2022 | 0 |
| 1/10/2022 | -1 |
| 1/11/2022 | 0 |
| 1/12/2022 | 0 |
| 1/15/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/21/2022 | 0 |
| 1/23/2022 | 0 |
| 1/26/2022 | 0 |
| 1/27/2022 | 0 |
| 1/29/2022 | 0 |
| 1/31/2022 | 0 |

inlunarweektodate() function, chart object example

![Example diagram of the use of the inlunarweektodate function, using a chart expression determining whether a transaction takes place in the lunar week that contains the 10th of January.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweektodate-example-chart-object.png "Click to view full size")

The in\_lunar\_week\_to\_date measure is created in the chart object by using the inlunarweektodate() function and passing the date field, a hard-coded date for January 10 as our base\_date, and an offset of 0 as the function’s arguments.

Because lunar weeks begin on January 1, January 10 would fall in the lunar week that begins on January 8. Additionally, since we are using the inlunarweektodate() function, that lunar week would then terminate on the 10th. Therefore, any transactions that occur between those two dates in January would return a Boolean value of TRUE. This is validated in the results table.

## Example 5 - Scenario

Load script and chart expressions

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Products.
- Information consisting of product ID, manufacture date, and cost price.

It has been identified that due to equipment error, products that were manufactured in the lunar week of January 12 were defective. The issue was resolved on January 13. The end user would like a chart object that displays, by week, the status of whether the products manufactured ‘defective’ or ‘faultless’ and the cost of the products manufactured in that week.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff]';

Products:
Load
*
Inline
[
product_id,manufacture_date,cost_price
8188,'01/02/2022 12:22:06',37.23
8189,'01/05/2022 01:02:30',17.17
8190,'01/06/2022 15:36:20',88.27
8191,'01/08/2022 10:58:35',57.42
8192,'01/09/2022 08:53:32',53.80
8193,'01/10/2022 21:13:01',82.06
8194,'01/11/2022 00:57:13',40.39
8195,'01/12/2022 09:26:02',87.21
8196,'01/13/2022 15:05:09',95.93
8197,'01/14/2022 18:44:57',45.89
8198,'01/15/2022 06:10:46',36.23
8199,'01/16/2022 06:39:27',25.66
8200,'01/17/2022 10:44:16',82.77
8201,'01/18/2022 18:48:17',69.98
8202,'01/26/2022 04:36:03',76.11
8203,'01/27/2022 08:07:49',25.12
8204,'01/28/2022 12:24:29',46.23
8205,'01/30/2022 11:56:56',84.21
8206,'01/30/2022 14:40:19',96.24
8207,'01/31/2022 05:28:21',67.67
];
```

Results

Do the following:

1. Load the data and open a [sheet](#glossary-8 "Glossary term"). Create a new table.
2. Create a [dimension](#glossary-9 "Glossary term") to show the week names:

   =weekname(manufacture\_date)
3. Next, create a dimension which uses the inlunarweektodate() function to identify which of the products are defective and which are faultless:

   =if(inlunarweektodate(manufacture\_date,makedate(2022,01,12),0),'Defective','Faultless')
4. Create a measure to sum the cost\_price of the products:

   =sum(cost\_price)
5. Set the measure's Number formatting to Money.

Results table

| =lunarweekname(manufacture\_date) | =if(InLunarWeekToDate(manufacture\_date,makedate(2022,01,12),0),'Defective','Faultless') | =Sum(cost\_price) |
| --- | --- | --- |
| 2022/01 | Faultless | $142.67 |
| 2022/02 | Defective | $320.88 |
| 2022/02 | Faultless | $141.82 |
| 2022/03 | Faultless | $214.64 |
| 2022/04 | Faultless | $147.46 |
| 2022/05 | Faultless | $248.12 |

The inlunarweektodate() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For those that return a Boolean value of TRUE, it marks the products as ‘Defective’. For any product returning a value of FALSE, and therefore not made in the lunar week up to January 12, it marks the products as ‘Faultless’.
