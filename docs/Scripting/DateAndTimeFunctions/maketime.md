---
title: "maketime Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/maketime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# maketime Script and chart function

Expand/Collapse all

# maketime Script and chart function

This function returns a time calculated from the hour hh, the minute mm, and the second ss.

Syntax:

MakeTime(hh [ , mm [ , ss ] ])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| hh | The hour as an integer. |
| mm | The minute as an integer.  If no minute is stated, 00 is assumed. |
| ss | The second as an integer.  If no second is stated, 00 is assumed. |

## When to use maketime

The maketime() function would commonly be used in the script for data generation to generate a time [field](#glossary-0 "Glossary term"). Sometimes, when the time field is derived from input text, this function could be used to construct the time using its components.

These examples use the time format h:mm:ss. The time format is specified in the SET TimeFormatstatement at the top of your data [load script](#glossary-1 "Glossary term") Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| maketime(22) | Returns 22:00:00. |
| maketime(22, 17) | Returns 22:17:00. |
| maketime(22,17,52 ) | Returns 22:17:52. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – maketime()

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") containing a set of transactions , which is loaded into a table called Transactions.
- Transaction times provided across three fields: hours, minutes, and seconds.
- The creation of a field, transaction\_time, that returns the time in the format of the TimeFormat system [variable](#glossary-3 "Glossary term").

Load script

```
SET TimeFormat='h:mm:ss TT';

Transactions:
    Load
        *,
        maketime(transaction_hour, transaction_minute, transaction_second) as transaction_time
        ;
Load * Inline [
transaction_id, transaction_hour, transaction_minute, transaction_second, transaction_amount, transaction_quantity, customer_id
3750, 18, 43, 30, 12423.56, 23, 2038593
3751, 6, 32, 07, 5356.31, 6, 203521
3752, 12, 09, 16, 15.75, 1, 5646471
3753, 21, 43, 41, 7, 3036491
3754, 17, 55, 22, 21484.21, 1356, 049681
3756, 2, 52, 22, -59.18, 2, 2038593
3757, 9, 25, 23, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_hour
- transaction\_minute
- transaction\_second
- transaction\_time

Results table

| transaction\_hour | transaction\_minute | transaction\_second | transaction\_time |
| --- | --- | --- | --- |
| 2 | 52 | 22 | 2:52:22 AM |
| 6 | 32 | 07 | 6:32:07 AM |
| 9 | 25 | 23 | 9:25:23 AM |
| 12 | 09 | 16 | 12:09:16 PM |
| 17 | 55 | 22 | 5:55:22 PM |
| 18 | 43 | 30 | 6:43:30 PM |
| 21 | 43 | 41 | 9:43:41 PM |

The transaction\_time field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the maketime() function, and passing the hour, minute, and second fields as function arguments.

The function then combines and converts these values into a time field, returning the results in the time format of the TimeFormat system variable.

## Example 2 – time() function

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, transaction\_time, which will allow us to show the results in 24-hour time format without modifying the TimeFormat system variable.

Load script

```
SET TimeFormat='h:mm:ss TT';

Transactions:
    Load
        *,
        time(maketime(transaction_hour, transaction_minute, transaction_second),'h:mm:ss') as transaction_time
        ;
Load * Inline [
transaction_id, transaction_hour, transaction_minute, transaction_second, transaction_amount, transaction_quantity, customer_id
3750, 18, 43, 30, 12423.56, 23, 2038593
3751, 6, 32, 07, 5356.31, 6, 203521
3752, 12, 09, 16, 15.75, 1, 5646471
3753, 21, 43, 41, 7, 3036491
3754, 17, 55, 22, 21484.21, 1356, 049681
3756, 2, 52, 22, -59.18, 2, 2038593
3757, 9, 25, 23, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_hour
- transaction\_minute
- transaction\_second
- transaction\_time

Results table

| transaction\_hour | transaction\_minute | transaction\_second | transaction\_time |
| --- | --- | --- | --- |
| 2 | 52 | 22 | 2:52:22 |
| 6 | 32 | 07 | 6:32:07 |
| 9 | 25 | 23 | 9:25:23 |
| 12 | 09 | 16 | 12:09:16 |
| 17 | 55 | 22 | 17:55:22 |
| 18 | 43 | 30 | 18:43:30 |
| 21 | 43 | 41 | 21:43:41 |

In this instance, the maketime() function is nested inside the time() function. The second argument of the time() function sets the format of the maketime() function results as the required h:mm:ss.

## Example 3 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions , which is loaded into a table called Transactions.
- Transaction times provided across two fields: hours and minutes.
- The creation of a field, transaction\_time, that returns the time in the format of the TimeFormat system variable.

Create a chart object [measure](#glossary-5 "Glossary term") transaction\_time, that returns a time in the format h:mm:ss TT.

Load script

```
SET TimeFormat='h:mm:ss TT';

Transactions:
Load * Inline [
transaction_id, transaction_hour, transaction_minute, transaction_amount, transaction_quantity, customer_id
3750, 18, 43, 12423.56, 23, 2038593
3751, 6, 32, 5356.31, 6, 203521
3752, 12, 09, 15.75, 1, 5646471
3753, 21, 43, 7, 3036491
3754, 17, 55, 21484.21, 1356, 049681
3756, 2, 52, -59.18, 2, 2038593
3757, 9, 25, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_hour
- transaction\_minute

To calculate the transaction\_time, create this measure:

=maketime(transaction\_hour,transaction\_minute)

Results table

| transaction\_hour | transaction\_minute | =maketime(transaction\_hour, transaction\_minute) |
| --- | --- | --- |
| 2 | 52 | 2:52:00 AM |
| 6 | 32 | 6:32:00 AM |
| 9 | 25 | 9:25:00 AM |
| 12 | 09 | 12:09:00 PM |
| 17 | 55 | 5:55:00 PM |
| 18 | 43 | 6:43:00 PM |
| 21 | 43 | 9:43:00 PM |

The transaction\_time measure is created in the chart object by using the maketime() function, and passing the hour and minute fields as function arguments.

The function then combines these values, and seconds are assumed to be 00. These values are then converted into a time field, returning the results in the format of the TimeFormat system variable.

## Example 4 – Scenario

Load script and chart expression

Overview

Create a calendar dataset for the month of January 2022, broken out into eight-hour increments.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

tmpCalendar:
	load
		*
    where year(date)=2022;
load
	date(recno()+makedate(2021,12,31)) as date
AutoGenerate 31;

Left join(tmpCalendar)
load
	maketime((recno()-1)*8,00,00) as time
autogenerate 3;

Calendar:
load
	timestamp(date + time) as timestamp
resident tmpCalendar;

drop table tmpCalendar;
```

Results

Results table

| timestamp |
| --- |
| 1/1/2022 12:00:00 AM |
| 1/1/2022 8:00:00 AM |
| 1/1/2022 4:00:00 PM |
| 1/2/2022 12:00:00 AM |
| 1/2/2022 8:00:00 AM |
| 1/2/2022 4:00:00 PM |
| 1/3/2022 12:00:00 AM |
| 1/3/2022 8:00:00 AM |
| 1/3/2022 4:00:00 PM |
| 1/4/2022 12:00:00 AM |
| 1/4/2022 8:00:00 AM |
| 1/4/2022 4:00:00 PM |
| 1/5/2022 12:00:00 AM |
| 1/5/2022 8:00:00 AM |
| 1/5/2022 4:00:00 PM |
| 1/6/2022 12:00:00 AM |
| 1/6/2022 8:00:00 AM |
| 1/6/2022 4:00:00 PM |
| 1/7/2022 12:00:00 AM |
| 1/7/2022 8:00:00 AM |
| 1/7/2022 4:00:00 PM |
| 1/8/2022 12:00:00 AM |
| 1/8/2022 8:00:00 AM |
| 1/8/2022 4:00:00 PM |
| 1/9/2022 12:00:00 AM |
| + 68 more rows |

The initial autogenerate function creates a calendar containing all the dates in January in a table called tmpCalendar.

A second table, containing three records, is created. For each record, recno() – 1 is taken (values 0, 1, 2) and the result is multiplied by 8. As a result, this generates the values 0, 8 16. These values are used as the hour parameter in a maketime() function, with minute and second values of 0. As a result, the table contains three time fields: 12:00:00 AM, 8:00:00 AM, and 4:00:00 PM.

This table is joined to the tmpCalendar table. Because there are no matching fields between the two tables for the join, the time rows are added to each date row. As a result, each date row is now repeated three times with each time value.

Finally, the Calendar table is created from a [resident load](#glossary-6 "Glossary term") of the tmpCalendar table. The date and time fields are concatenated and wrapped in the timestamp() function to create the timestamp field.

The tmpCalendar table is then dropped.
