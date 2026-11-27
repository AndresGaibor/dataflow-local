---
title: "inlunarweek Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inlunarweek.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inlunarweek Script and chart function

Expand/Collapse all

# inlunarweek Script and chart function

This function determines if timestamp lies inside the
lunar week
containing base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week., Apart from the final week of the year, each week will contain exactly seven days.

Syntax:

InLunarWeek
(timestamp, base\_date, period\_no[, first\_week\_day])

Return data type:  Boolean

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

The inlunarweek() function determines which lunar week the base\_date falls into. It then returns a Boolean result once it has determined whether each timestamp value occurs during the same lunar week as the base\_date.

Diagram of inlunarweek() function

![Example diagram of inlunarweek function, showing the dates for which the function will return a TRUE value, given the input information.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweek-overview.png "Click to view full size")

## When to use inlunarweek

The inlunarweek() function returns a Boolean result. Typically, this type of function will be used as a condition in an IF expression. This would return an [aggregation](#glossary-0 "Glossary term") or calculation dependent on whether the date evaluated occurred during the lunar week in question.

For example, the inlunarweek() function can be used to identify all equipment manufactured in a particular lunar week.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the lunar week. |
| period\_no | The lunar week can be offset by period\_no. period\_no is an integer, where the value 0 indicates the lunar week which contains base\_date. Negative values in period\_no indicate preceding lunar weeks and positive values indicate succeeding lunar weeks. |
| first\_week\_day | An offset that may be greater than or less than zero. This changes the beginning of the year by the specified number of days and/or fractions of a day. |

Function examples

| Example | Result |
| --- | --- |
| inlunarweek('01/12/2013', '01/14/2013', 0) | Returns TRUE, since the value of timestamp, 01/12/2013, falls in the week 01/08/2013 to 01/14/2013. |
| inlunarweek('01/12/2013', '01/07/2013', 0) | Returns FALSE, since the base\_date 01/07/2013 is in the lunar week defined as 01/01/2013 to 01/07/2013. |
| inlunarweek('01/12/2013', '01/14/2013', -1) | Returns FALSE. Specifying a value of period\_no as -1 shifts the week to the previous week, 01/01/2013 to 01/07/2013. |
| inlunarweek('01/07/2013', 01/14/2013', -1) | Returns TRUE. In comparison with the previous example, the timestamp is in the following week, after into account the shift backwards. |
| inlunarweek('01/11/2006', '01/08/2006', 0, 3) | Returns FALSE. Specifying a value of 3 for first\_week\_day means that the start of the year is calculated from 01/04/2013. Therefore, the value of base\_date falls in the first week, and the value of timestamp falls in the week 01/11/2013 to 01/17/2013. |

The inlunarweek() function is often used in combination with the following functions:

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

- A [dataset](#glossary-1 "Glossary term") of transactions for the month of January, which is loaded into a table called Transactions.
- The date [field](#glossary-2 "Glossary term") has been provided in the DateFormat system [variable](#glossary-3 "Glossary term") (MM/DD/YYYY) format.

Create a field, in\_lunar\_week, that determines whether the transactions took place in the same lunar week as January 10.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inlunarweek(date,'01/10/2022', 0) as in_lunar_week
        ;
Load
*
Inline
[
id,date,amount
8183,'1/5/2022',42.32
8184,'1/6/2022',68.22
8185,'1/7/2022',15.25
8186,'1/8/2022',25.26
8187,'1/9/2022',37.23
8188,'1/10/2022',37.23
8189,'1/11/2022',17.17
8190,'1/12/2022',88.27
8191,'1/13/2022',57.42
8192,'1/14/2022',53.80
8193,'1/15/2022',82.06
8194,'1/16/2022',87.21
8195,'1/17/2022',95.93
8196,'1/18/2022',45.89
8197,'1/19/2022',36.23
8198,'1/20/2022',25.66
8199,'1/21/2022',82.77
8200,'1/22/2022',69.98
8201,'1/23/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_lunar\_week

Results table

| date | in\_lunar\_week |
| --- | --- |
| 1/5/2022 | 0 |
| 1/6/2022 | 0 |
| 1/7/2022 | 0 |
| 1/8/2022 | -1 |
| 1/9/2022 | -1 |
| 1/10/2022 | -1 |
| 1/11/2022 | -1 |
| 1/12/2022 | -1 |
| 1/13/2022 | -1 |
| 1/14/2022 | -1 |
| 1/15/2022 | 0 |
| 1/16/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/20/2022 | 0 |
| 1/21/2022 | 0 |
| 1/22/2022 | 0 |
| 1/23/2022 | 0 |

inlunarweek() function, basic example

![Example of the use of the inlunarweek function showing the range of dates for which the function will return a value of TRUE, given the input information. This example contains  no additional arguments.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweek-basic-example.png "Click to view full size")

The in\_lunar\_week field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the inlunarweek() function, then passing the following as the function's arguments:

- The date field
- A hard-coded date for January 10 as the base\_date
- Aperiod\_no of 0

Because lunar weeks begin on January 1, January 10 would fall in the lunar week that begins on January 8 and ends on January 14. Therefore, any transactions that occur between those two dates in January would return a Boolean value of TRUE. This is validated in the results table.

## Example 2 - period\_no

Examples and results:

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The date field has been provided in the DateFormat system variable (MM/DD/YYYY) format.

However, in this example, the task is to create a field, 2\_lunar\_weeks\_later, that determines whether or not the transactions took place two lunar weeks after January 10.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inlunarweek(date,'01/10/2022', 2) as [2_lunar_weeks_later]
        ;
Load
*
Inline
[
id,date,amount
8183,'1/5/2022',42.32
8184,'1/6/2022',68.22
8185,'1/7/2022',15.25
8186,'1/8/2022',25.26
8187,'1/9/2022',37.23
8188,'1/10/2022',37.23
8189,'1/11/2022',17.17
8190,'1/12/2022',88.27
8191,'1/13/2022',57.42
8192,'1/14/2022',53.80
8193,'1/15/2022',82.06
8194,'1/16/2022',87.21
8195,'1/17/2022',95.93
8196,'1/18/2022',45.89
8197,'1/19/2022',36.23
8198,'1/20/2022',25.66
8199,'1/21/2022',82.77
8200,'1/22/2022',69.98
8201,'1/23/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- 2\_lunar\_weeks\_later

Results table

| date | 2\_lunar\_weeks\_later |
| --- | --- |
| 1/5/2022 | 0 |
| 1/6/2022 | 0 |
| 1/7/2022 | 0 |
| 1/8/2022 | 0 |
| 1/9/2022 | 0 |
| 1/10/2022 | 0 |
| 1/11/2022 | 0 |
| 1/12/2022 | 0 |
| 1/13/2022 | 0 |
| 1/14/2022 | 0 |
| 1/15/2022 | 0 |
| 1/16/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/20/2022 | 0 |
| 1/21/2022 | 0 |
| 1/22/2022 | -1 |
| 1/23/2022 | -1 |

inlunarweek() function, period\_no example

![inlunarweek function, period_no example](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweek-period-no.png "Click to view full size")

In this instance, because a period\_no of 2 was used as the offset argument in the inlunarweek() function, the function defines the week beginning on January 22 as the lunar week to validate transactions against. Therefore, any transaction that takes place between the January 22 and January 28 will return a Boolean result of TRUE.

## Example 3 - first\_week\_day

Load script and results

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the [load script](#glossary-6 "Glossary term") below to a new tab.

The load script uses the same dataset and scenario as the first example. However, in the example, we set lunar weeks to begin on January 6.

- The same dataset and scenario as the first example.
- The default DateFormat system variable MM/DD/YYYY is used.
- A first\_week\_day argument of 5. This sets lunar weeks to begin on January 5.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inlunarweek(date,'01/10/2022', 0,5) as in_lunar_week
        ;
Load
*
Inline
[
id,date,amount
8183,'1/5/2022',42.32
8184,'1/6/2022',68.22
8185,'1/7/2022',15.25
8186,'1/8/2022',25.26
8187,'1/9/2022',37.23
8188,'1/10/2022',37.23
8189,'1/11/2022',17.17
8190,'1/12/2022',88.27
8191,'1/13/2022',57.42
8192,'1/14/2022',53.80
8193,'1/15/2022',82.06
8194,'1/16/2022',87.21
8195,'1/17/2022',95.93
8196,'1/18/2022',45.89
8197,'1/19/2022',36.23
8198,'1/20/2022',25.66
8199,'1/21/2022',82.77
8200,'1/22/2022',69.98
8201,'1/23/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_lunar\_week

Results table

| date | in\_lunar\_week |
| --- | --- |
| 1/5/2022 | 0 |
| 1/6/2022 | -1 |
| 1/7/2022 | -1 |
| 1/8/2022 | -1 |
| 1/9/2022 | -1 |
| 1/10/2022 | -1 |
| 1/11/2022 | -1 |
| 1/12/2022 | -1 |
| 1/13/2022 | 0 |
| 1/14/2022 | 0 |
| 1/15/2022 | 0 |
| 1/16/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/20/2022 | 0 |
| 1/21/2022 | 0 |
| 1/22/2022 | 0 |
| 1/23/2022 | 0 |

inlunarweek() function, first\_week\_day example

![Example of the use of the inlunarweek function showing the range of dates for which the function will return a value of TRUE, given the input information. In this example, we set lunar weeks to begin on January 6 using the first_week_day argument.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inlunarweek-first-week-day.png "Click to view full size")

In this instance, because the first\_week\_date argument of 5 is used in the inlunarweek() function, it offsets the start of the lunar week calendar to January 6. Therefore, January 10 falls in the lunar week beginning on January 6 and ending on January 12. Any transaction that falls between these two dates will return a Boolean value of TRUE.

## Example 4 - Chart object

Load script and chart expression:

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The date field has been provided in the DateFormat system variable (MM/DD/YYYY) format.

However, in this example, the unchanged dataset is loaded into the application. The calculation that determines whether the transactions took place in the same lunar week as January 10 is created as a [measure](#glossary-7 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8183,'1/5/2022',42.32
8184,'1/6/2022',68.22
8185,'1/7/2022',15.25
8186,'1/8/2022',25.26
8187,'1/9/2022',37.23
8188,'1/10/2022',37.23
8189,'1/11/2022',17.17
8190,'1/12/2022',88.27
8191,'1/13/2022',57.42
8192,'1/14/2022',53.80
8193,'1/15/2022',82.06
8194,'1/16/2022',87.21
8195,'1/17/2022',95.93
8196,'1/18/2022',45.89
8197,'1/19/2022',36.23
8198,'1/20/2022',25.66
8199,'1/21/2022',82.77
8200,'1/22/2022',69.98
8201,'1/23/2022',76.11
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

To calculate whether a transaction takes place in the lunar week that contains January 10, create the following measure:

= inlunarweek(date,'01/10/2022', 0)

Results table

| date | =inlunarweek(date,'01/10/2022', 0) |
| --- | --- |
| 1/5/2022 | 0 |
| 1/6/2022 | 0 |
| 1/7/2022 | 0 |
| 1/8/2022 | -1 |
| 1/9/2022 | -1 |
| 1/10/2022 | -1 |
| 1/11/2022 | -1 |
| 1/12/2022 | -1 |
| 1/13/2022 | -1 |
| 1/14/2022 | -1 |
| 1/15/2022 | 0 |
| 1/16/2022 | 0 |
| 1/17/2022 | 0 |
| 1/18/2022 | 0 |
| 1/19/2022 | 0 |
| 1/20/2022 | 0 |
| 1/21/2022 | 0 |
| 1/22/2022 | 0 |
| 1/23/2022 | 0 |

## Example 5 - Scenario

Load script and chart expression:

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Products.
- Information consisting of product ID, manufacture date, and cost price.

It has been identified that due to equipment error, products that were manufactured in the lunar week that included January 12 were defective. The end user would like a chart object that displays, by lunar week name, the status of whether the products manufactured were ‘defective’ or ‘faultless’ and the cost of the products manufactured in that month.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
product_id,manufacture_date,cost_price
8183,'1/5/2022',42.32
8184,'1/6/2022',68.22
8185,'1/7/2022',15.25
8186,'1/8/2022',25.26
8187,'1/9/2022',37.23
8188,'1/10/2022',37.23
8189,'1/11/2022',17.17
8190,'1/12/2022',88.27
8191,'1/13/2022',57.42
8192,'1/14/2022',53.80
8193,'1/15/2022',82.06
8194,'1/16/2022',87.21
8195,'1/17/2022',95.93
8196,'1/18/2022',45.89
8197,'1/19/2022',36.23
8198,'1/20/2022',25.66
8199,'1/21/2022',82.77
8200,'1/22/2022',69.98
8201,'1/23/2022',76.11
];
```

Results

Do the following:

1. Load the data and open a [sheet](#glossary-8 "Glossary term"). Create a new table.
2. Create a [dimension](#glossary-9 "Glossary term") to show the month names:

   =lunarweekname(manufacture\_date)
3. Create a measure to identify which of the products are defective and which are faultless using the inlunarweek() function:

   =if(only(inlunarweek(manufacture\_date,makedate(2022,01,12),0)), 'Defective','Faultless')
4. Create a measure to sum the cost\_price of the products:

   =sum(cost\_price)
5. Set the measure's Number formatting to Money.
6. Under Appearance, turn off Totals.

Results table

| lunarweekname(manufacture\_date) | =if(only(inlunarweek(manufacture\_date,makedate(2022,01,12),0)), 'Defective','Faultless') | sum(cost\_price) |
| --- | --- | --- |
| 2022/01 | Faultless | $125.79 |
| 2022/02 | Defective | $316.38 |
| 2022/03 | Faultless | $455.75 |
| 2022/04 | Faultless | $146.09 |

The inlunarweek() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured in the lunar week that contains January 10, the inlunarweek() function returns a Boolean value of TRUE and marks the products as ‘Defective’. For any product returning a value of FALSE, and therefore not manufactured in that week, it marks the products as ‘Faultless’.
