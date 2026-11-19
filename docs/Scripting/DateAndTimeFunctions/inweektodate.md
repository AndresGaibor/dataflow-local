---
title: "inweektodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "sheet"]
---
Expand/Collapse all

# inweektodate Script and chart function

This function returns
True if timestamp lies inside the
part of week containing base\_date
up until and including the last millisecond of base\_date.

Syntax:

InWeekToDate
(timestamp, base\_date, period\_no [, first\_week\_day])

Return data type:  Boolean

> **Note:** In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Diagram of inweektodate function

![Example diagram of the range of date within which the inweektodate function will return a value of TRUE. In this case, it returns TRUE for certain days of the week, and FALSE for others.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inweektodate-general.png)

The `inweektodate()` function uses the `base_date` parameter to identify a maximum boundary date of a week segment, as well as its corresponding date for the start of the week, which is based on the `FirstWeekDay` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-0 "Glossary term") (or user-defined `first_week_day` parameter). Once this week segment has been defined, the function will then return Boolean results when comparing the prescribed date values to that segment.

## When to use inweektodate

The `inweektodate()` function returns a Boolean result. Typically, this type of function will be used as a condition in an `if` expression. This will return an [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-1 "Glossary term") or calculation dependent on whether a date evaluated occurred during the week in question up to and including a particular date.

For example, the `inweektodate()` function can be used to calculate all sales made during a specified week up to a particular date.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the week. |
| period\_no | The week can be offset by period\_no. period\_no is an integer, where the value 0 indicates the week which contains base\_date. Negative values in period\_no indicate preceding weeks and positive values indicate succeeding weeks. |
| first\_week\_day | By default, the first day of the week is Sunday (as determined by the FirstWeekDay system variable), starting at midnight between Saturday and Sunday. The first\_week\_day parameter supersedes the FirstWeekDay variable. To indicate the week starting on another day, specify a flag between 0 and 6.  For a week starting on Monday and ending on Sunday, use a flag of 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday. |

Function examples

| Example | Interaction |
| --- | --- |
| `inweektodate('01/12/2006', '01/12/2006', 0)` | Returns `TRUE`. |
| `inweektodate('01/12/2006', '01/11/2006', 0)` | Returns `FALSE`. |
| `inweektodate('01/12/2006', '01/18/2006', -1)` | Returns `FALSE`. Because `period_no` is specified as -1, the effective data that `timestamp` is measured against is 01/11/2006. |
| `inweektodate('01/11/2006', '01/12/2006', 0, 3 )` | Returns `FALSE`, since `first_week_day` is specified as `3` (Thursday), which makes 01/12/2006 the first day of the week following the week containing 01/12/2006. |

These topics may help you work with this function:

Related topics

| Topic | Default Flag / Value | Description |
| --- | --- | --- |
| [*FirstWeekDay*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/FirstWeekDay.htm) | 6 / Sunday | Defines the start day of each week. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-2 "Glossary term") containing a set of transactions for the month of January 2022, which is loaded into a table called `Transactions`.
- The data [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-3 "Glossary term") provided in the `TimestampFormat='M/D/YYYY h:mm:ss[.fff]'` format.
- The creation of a field, `in_week_to_date`, which determines which transactions took place in the week up until January 14, 2022.
- The creation of an additional field, named `weekday`, using the `weekday()` function. This new field is created to show which day of the week corresponds to each date.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff]';
SET FirstWeekDay=6;
Transactions:
    Load
        *,
        weekday(date) as week_day,
        inweektodate(date,'01/14/2022', 0) as in_week_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'2022-01-02 12:22:06',37.23
8189,'2022-01-05 01:02:30',17.17
8190,'2022-01-06 15:36:20',88.27
8191,'2022-01-08 10:58:35',57.42
8192,'2022-01-09 08:53:32',53.80
8193,'2022-01-10 21:13:01',82.06
8194,'2022-01-11 00:57:13',40.39
8195,'2022-01-12 09:26:02',87.21
8196,'2022-01-13 15:05:09',95.93
8197,'2022-01-14 18:44:57',45.89
8198,'2022-01-15 06:10:46',36.23
8199,'2022-01-16 06:39:27',25.66
8200,'2022-01-17 10:44:16',82.77
8201,'2022-01-18 18:48:17',69.98
8202,'2022-01-26 04:36:03',76.11
8203,'2022-01-27 08:07:49',25.12
8204,'2022-01-28 12:24:29',46.23
8205,'2022-01-30 11:56:56',84.21
8206,'2022-01-30 14:40:19',96.24
8207,'2022-01-31 05:28:21',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `week_day`
- `in_week_to_date`

Results table

| date | week\_day | in\_week\_to\_date |
| --- | --- | --- |
| 2022-01-02 12:22:06 | Sun | 0 |
| 2022-01-05 01:02:30 | Wed | 0 |
| 2022-01-06 15:36:20 | Thu | 0 |
| 2022-01-08 10:58:35 | Sat | 0 |
| 2022-01-09 08:53:32 | Sun | -1 |
| 2022-01-10 21:13:01 | Mon | -1 |
| 2022-01-11 00:57:13 | Tue | -1 |
| 2022-01-12 09:26:02 | Wed | -1 |
| 2022-01-13 15:05:09 | Thu | -1 |
| 2022-01-14 18:44:57 | Fri | -1 |
| 2022-01-15 06:10:46 | Sat | 0 |
| 2022-01-16 06:39:27 | Sun | 0 |
| 2022-01-17 10:44:16 | Mon | 0 |
| 2022-01-18 18:48:17 | Tue | 0 |
| 2022-01-26 04:36:03 | Wed | 0 |
| 2022-01-27 08:07:49 | Thu | 0 |
| 2022-01-28 12:24:29 | Fri | 0 |
| 2022-01-30 11:56:56 | Sun | 0 |
| 2022-01-30 14:40:19 | Sun | 0 |
| 2022-01-31 05:28:21 | Mon | 0 |

The `in_week_to_date` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-4 "Glossary term") statement by using the `inweektodate()` function. The first argument provided identifies which field is being evaluated. The second argument is a hard-coded date for January 14, which is the `base_date` that identifies which week to segment and defines the end boundary of that segment. A `period_no` of 0 is the final argument, meaning that the function is not comparing weeks preceding or following the segmented week.

The `FirstWeekDay` system variable determines that weeks begin on a Sunday and end on a Saturday. Therefore, January would be broken into weeks according to the diagram below, with the dates between January 9 and 14 providing the valid period for the `inweekdodate()` calculation:

Calendar diagram showing transaction dates which would return a Boolean result of TRUE

![Diagram showing the range of dates for which the inweektodate function will return a value of TRUE. In this example, the dates returning a TRUE value are January 9 to 14, inclusive.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inweektodate-no-add-arg-calendar.png)

Any transaction that occurs in between January 9 and 14 returns a Boolean result of `TRUE`. Transactions before and after the dates return a Boolean result of `FALSE`.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `prev_week_to_date`, that determines which transactions took place a full week before the week segment ending on January 14, 2022.
- The creation of an additional field, named `weekday`, using the `weekday()` function. This is to show which day of the week corresponds to each date.

Load script

```
SET FirstWeekDay=6;
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff]';
Transactions:
    Load
        *,
        weekday(date) as week_day,
        inweektodate(date,'01/14/2022', -1) as prev_week_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'2022-01-02 12:22:06',37.23
8189,'2022-01-05 01:02:30',17.17
8190,'2022-01-06 15:36:20',88.27
8191,'2022-01-08 10:58:35',57.42
8192,'2022-01-09 08:53:32',53.80
8193,'2022-01-10 21:13:01',82.06
8194,'2022-01-11 00:57:13',40.39
8195,'2022-01-12 09:26:02',87.21
8196,'2022-01-13 15:05:09',95.93
8197,'2022-01-14 18:44:57',45.89
8198,'2022-01-15 06:10:46',36.23
8199,'2022-01-16 06:39:27',25.66
8200,'2022-01-17 10:44:16',82.77
8201,'2022-01-18 18:48:17',69.98
8202,'2022-01-26 04:36:03',76.11
8203,'2022-01-27 08:07:49',25.12
8204,'2022-01-28 12:24:29',46.23
8205,'2022-01-30 11:56:56',84.21
8206,'2022-01-30 14:40:19',96.24
8207,'2022-01-31 05:28:21',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `week_day`
- `prev_week_to_date`

Results table

| date | week\_day | prev\_week\_to\_date |
| --- | --- | --- |
| 2022-01-02 12:22:06 | Sun | -1 |
| 2022-01-05 01:02:30 | Wed | -1 |
| 2022-01-06 15:36:20 | Thu | -1 |
| 2022-01-08 10:58:35 | Sat | 0 |
| 2022-01-09 08:53:32 | Sun | 0 |
| 2022-01-10 21:13:01 | Mon | 0 |
| 2022-01-11 00:57:13 | Tue | 0 |
| 2022-01-12 09:26:02 | Wed | 0 |
| 2022-01-13 15:05:09 | Thu | 0 |
| 2022-01-14 18:44:57 | Fri | 0 |
| 2022-01-15 06:10:46 | Sat | 0 |
| 2022-01-16 06:39:27 | Sun | 0 |
| 2022-01-17 10:44:16 | Mon | 0 |
| 2022-01-18 18:48:17 | Tue | 0 |
| 2022-01-26 04:36:03 | Wed | 0 |
| 2022-01-27 08:07:49 | Thu | 0 |
| 2022-01-28 12:24:29 | Fri | 0 |
| 2022-01-30 11:56:56 | Sun | 0 |
| 2022-01-30 14:40:19 | Sun | 0 |
| 2022-01-31 05:28:21 | Mon | 0 |

A `period_no` value of -1 indicates that the `inweektodate ()` function compares the input quarter segment to the preceding week. The week segment initially equates to between January 9 and January 14. The `period_no` then offsets both the start and end boundary of this segment to one week earlier, causing the date boundaries to become January 2 to January 7.

Calendar diagram showing transaction dates which would return a Boolean result of TRUE

![Diagram showing the range of dates for which the inweektodate function will return a value of TRUE. In this example, the dates returning a TRUE value are January 2 to 7.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inweektodate-period-no-calendar.png)

Therefore, any transaction that occurs between January 2 and 8 (not including January 8 itself) will return a Boolean result of `TRUE`.

## Example 3 – first\_week\_day

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `in_week_to_date`, that determines which transactions took place in the week up until January 14, 2022.
- The creation of an additional field, named `weekday`, using the `weekday()` function. This is to show which day of the week corresponds to each date.

In this example, we consider Monday as the first day of the week.

Load script

```
SET FirstWeekDay=6;
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff]';

Transactions:
    Load
        *,
        weekday(date) as week_day,
        inweektodate(date,'01/14/2022', 0, 0) as in_week_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'2022-01-02 12:22:06',37.23
8189,'2022-01-05 01:02:30',17.17
8190,'2022-01-06 15:36:20',88.27
8191,'2022-01-08 10:58:35',57.42
8192,'2022-01-09 08:53:32',53.80
8193,'2022-01-10 21:13:01',82.06
8194,'2022-01-11 00:57:13',40.39
8195,'2022-01-12 09:26:02',87.21
8196,'2022-01-13 15:05:09',95.93
8197,'2022-01-14 18:44:57',45.89
8198,'2022-01-15 06:10:46',36.23
8199,'2022-01-16 06:39:27',25.66
8200,'2022-01-17 10:44:16',82.77
8201,'2022-01-18 18:48:17',69.98
8202,'2022-01-26 04:36:03',76.11
8203,'2022-01-27 08:07:49',25.12
8204,'2022-01-28 12:24:29',46.23
8205,'2022-01-30 11:56:56',84.21
8206,'2022-01-30 14:40:19',96.24
8207,'2022-01-31 05:28:21',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `week_day`
- `in_week_to_date`

Results table

| date | week\_day | in\_week\_to\_date |
| --- | --- | --- |
| 2022-01-02 12:22:06 | Sun | 0 |
| 2022-01-05 01:02:30 | Wed | 0 |
| 2022-01-06 15:36:20 | Thu | 0 |
| 2022-01-08 10:58:35 | Sat | 0 |
| 2022-01-09 08:53:32 | Sun | 0 |
| 2022-01-10 21:13:01 | Mon | -1 |
| 2022-01-11 00:57:13 | Tue | -1 |
| 2022-01-12 09:26:02 | Wed | -1 |
| 2022-01-13 15:05:09 | Thu | -1 |
| 2022-01-14 18:44:57 | Fri | -1 |
| 2022-01-15 06:10:46 | Sat | 0 |
| 2022-01-16 06:39:27 | Sun | 0 |
| 2022-01-17 10:44:16 | Mon | 0 |
| 2022-01-18 18:48:17 | Tue | 0 |
| 2022-01-26 04:36:03 | Wed | 0 |
| 2022-01-27 08:07:49 | Thu | 0 |
| 2022-01-28 12:24:29 | Fri | 0 |
| 2022-01-30 11:56:56 | Sun | 0 |
| 2022-01-30 14:40:19 | Sun | 0 |
| 2022-01-31 05:28:21 | Mon | 0 |

By using 0 as the `first_week_day` argument in the `inweektodate()` function, the function argument supersedes the `FirstWeekDay` system variable and sets Monday as the first day of the week.

Calendar diagram showing transaction dates which would return a Boolean result of TRUE

![Diagram showing the range of transaction dates for which the inweektodate function will return a value of TRUE. In this example, the dates returning a TRUE value are January 10 to 14, inclusive.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inweektodate-first-week-day-calendar.png)

Therefore, any transaction that occurs in between January 10 and 14 will return a Boolean result of `TRUE`, while transactions with dates outside these boundaries will return a value of `FALSE`.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-5 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-6 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The calculation that determines which transactions took place in the week up until January 14, 2022 is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-7 "Glossary term") in the chart object.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,'2022-01-02 12:22:06',37.23
8189,'2022-01-05 01:02:30',17.17
8190,'2022-01-06 15:36:20',88.27
8191,'2022-01-08 10:58:35',57.42
8192,'2022-01-09 08:53:32',53.80
8193,'2022-01-10 21:13:01',82.06
8194,'2022-01-11 00:57:13',40.39
8195,'2022-01-12 09:26:02',87.21
8196,'2022-01-13 15:05:09',95.93
8197,'2022-01-14 18:44:57',45.89
8198,'2022-01-15 06:10:46',36.23
8199,'2022-01-16 06:39:27',25.66
8200,'2022-01-17 10:44:16',82.77
8201,'2022-01-18 18:48:17',69.98
8202,'2022-01-26 04:36:03',76.11
8203,'2022-01-27 08:07:49',25.12
8204,'2022-01-28 12:24:29',46.23
8205,'2022-01-30 11:56:56',84.21
8206,'2022-01-30 14:40:19',96.24
8207,'2022-01-31 05:28:21',67.67
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.
2. To calculate whether transactions took place in the same week up until the 14th of January, create the following measure:

   `=inweektodate(date,'01/14/2022',0)`
3. To show which day of the week corresponds to each date, create an additional measure:

   `=weekday(date)`

Results table

| date | week\_day | in\_week\_to\_date |
| --- | --- | --- |
| 2022-01-02 12:22:06 | Sun | 0 |
| 2022-01-05 01:02:30 | Wed | 0 |
| 2022-01-06 15:36:20 | Thu | 0 |
| 2022-01-08 10:58:35 | Sat | 0 |
| 2022-01-09 08:53:32 | Sun | -1 |
| 2022-01-10 21:13:01 | Mon | -1 |
| 2022-01-11 00:57:13 | Tue | -1 |
| 2022-01-12 09:26:02 | Wed | -1 |
| 2022-01-13 15:05:09 | Thu | -1 |
| 2022-01-14 18:44:57 | Fri | -1 |
| 2022-01-15 06:10:46 | Sat | 0 |
| 2022-01-16 06:39:27 | Sun | 0 |
| 2022-01-17 10:44:16 | Mon | 0 |
| 2022-01-18 18:48:17 | Tue | 0 |
| 2022-01-26 04:36:03 | Wed | 0 |
| 2022-01-27 08:07:49 | Thu | 0 |
| 2022-01-28 12:24:29 | Fri | 0 |
| 2022-01-30 11:56:56 | Sun | 0 |
| 2022-01-30 14:40:19 | Sun | 0 |
| 2022-01-31 05:28:21 | Mon | 0 |

The `in_week_to_date` field is created as a measure in the chart object using the `inweektodate()` function. The first argument provided identifies which field is being evaluated. The second argument is a hard-coded date for January 14, which is the `base_date` that identifies which week to segment and defines the end boundary of that segment. A `period_no` of 0 is the final argument, meaning that the function is not comparing weeks preceding or following the segmented week.

The `FirstWeekDay` system variable determines that weeks begin on a Sunday and end on a Saturday. Therefore, January would be broken into weeks according to the diagram below, with the dates between January 9 and 14 providing the valid period for the `inweekdodate()` calculation:

Calendar diagram showing transaction dates which would return a Boolean result of TRUE

![Diagram showing the range of dates for which the inweektodate function will return a value of TRUE. In this example, the dates returning a TRUE value are January 9 to 14, inclusive.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inweektodate-chart-object-calendar.png)

Any transaction that occurs in between January 9 and 14 returns a Boolean result of `TRUE`. Transactions before and after the dates return a Boolean result of `FALSE`.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called `Products`.
- Information concerning product ID, manufacture date, and cost price.

It has been identified that due to equipment error, products that were manufactured in the week of January 12 were defective. The issue was resolved on January 13. The end user would like a chart object that displays, by week, the status of whether the products manufactured are ‘defective’ or ‘faultless’, and the cost of the products manufactured in that week.

Load script

```
Products:
Load
*
Inline
[
product_id,manufacture_date,cost_price
8188,'2022-01-02 12:22:06',37.23
8189,'2022-01-05 01:02:30',17.17
8190,'2022-01-06 15:36:20',88.27
8191,'2022-01-08 10:58:35',57.42
8192,'2022-01-09 08:53:32',53.80
8193,'2022-01-10 21:13:01',82.06
8194,'2022-01-11 00:57:13',40.39
8195,'2022-01-12 09:26:02',87.21
8196,'2022-01-13 15:05:09',95.93
8197,'2022-01-14 18:44:57',45.89
8198,'2022-01-15 06:10:46',36.23
8199,'2022-01-16 06:39:27',25.66
8200,'2022-01-17 10:44:16',82.77
8201,'2022-01-18 18:48:17',69.98
8202,'2022-01-26 04:36:03',76.11
8203,'2022-01-27 08:07:49',25.12
8204,'2022-01-28 12:24:29',46.23
8205,'2022-01-30 11:56:56',84.21
8206,'2022-01-30 14:40:19',96.24
8207,'2022-01-31 05:28:21',67.67
];
```

Results

Do the following:

1. Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-8 "Glossary term"). Create a new table. Create a [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm#glossary-9 "Glossary term") to show the week names:

   `=weekname(manufacture_date)`
2. Next, create a dimension to identify which of the products are defective and which are faultless:

   `=if(inWeektodate(manufacture_date,makedate(2022,01,12),0),'Defective','Faultless')`
3. Create a measure to sum the `cost_price` of the products:

   `=sum(cost_price)`
4. Set the measure's **Number formatting** to **Money**.

Results table

| weekname(manufacture\_date) | if(inweektodate(manufacture\_date,makedate(2022,01,12),0),'Defective','Faultless') | Sum(cost\_price) |
| --- | --- | --- |
| 2022/02 | Faultless | $200.09 |
| 2022/03 | Defective | $263.46 |
| 2022/03 | Faultless | $178.05 |
| 2022/04 | Faultless | $178.41 |
| 2022/05 | Faultless | $147.46 |
| 2022/06 | Faultless | $248.12 |

The `inweektodate()` function returns a Boolean value when evaluating the manufacturing dates of each of the products. For those that return a Boolean value of `TRUE`, it marks the products as `'Defective'`. For any product returning a value of `FALSE`, and therefore not made in the week up to January 12, it marks the products as `‘Faultless’`.
