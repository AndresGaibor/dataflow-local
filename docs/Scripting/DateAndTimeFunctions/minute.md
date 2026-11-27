---
title: "minute Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/minute.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# minute Script and chart function

Expand/Collapse all

# minute Script and chart function

This function returns an integer representing the minute when the fraction
of the expression is interpreted as a time
according to the standard number interpretation.

Syntax:

minute(expression)

Return data type:  integer

## When to use minute

The minute() function is useful when you would like to compare aggregations by minute. For example, you could use the function if you would like to see activity count distribution by minute.

These [dimensions](#glossary-0 "Glossary term") can be created either in the [load script](#glossary-1 "Glossary term") by using the function to create a [field](#glossary-2 "Glossary term") in a Master Calendar table. Alternatively, they can be used directly in a [chart](#glossary-3 "Glossary term") as a calculated dimension.

Function examples

| Example | Result |
| --- | --- |
| minute ( '09:14:36' ) | Returns 14. |
| minute ( '0.5555' ) | Returns 19 ( Because 0.5555 = 13:19:55 ). |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – Variable (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-4 "Glossary term") containing transactions by timestamp, which is loaded into a table called Transactions.
- The default TimeStamp system [variable](#glossary-5 "Glossary term") (M/D/YYYY h:mm:ss[.fff] TT) is used.
- The creation of a field, minute, to calculate when transactions took place.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        minute(timestamp) as minute
        ;
Load
*
Inline
[
id,timestamp,amount
9497,'2022-01-05 19:04:57',47.25,
9498,'2022-01-03 14:21:53',51.75,
9499,'2022-01-03 05:40:49',73.53,
9500,'2022-01-04 18:49:38',15.35,
9501,'2022-01-01 22:10:22',31.43,
9502,'2022-01-05 19:34:46',13.24,
9503,'2022-01-04 22:58:34',74.34,
9504,'2022-01-06 11:29:38',50.00,
9505,'2022-01-02 08:35:54',36.34,
9506,'2022-01-06 08:49:09',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- timestamp
- minute

Results table

| timestamp | minute |
| --- | --- |
| 2022-01-01 22:10:22 | 10 |
| 2022-01-02 08:35:54 | 35 |
| 2022-01-03 05:40:49 | 40 |
| 2022-01-03 14:21:53 | 21 |
| 2022-01-04 18:49:38 | 49 |
| 2022-01-04 22:58:34 | 58 |
| 2022-01-05 19:04:57 | 4 |
| 2022-01-05 19:34:46 | 34 |
| 2022-01-06 08:49:09 | 49 |
| 2022-01-06 11:29:38 | 29 |

The values in the minute field are created by using the minute() function and passing the timestamp as the expression in the [preceding load](#glossary-6 "Glossary term") statement.

## Example 2 – Chart object (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The default TimeStamp system variable (M/D/YYYY h:mm:ss[.fff] TT) is used.

However, in this example, the unchanged dataset is loaded into the application. The minute values are calculated via a [measure](#glossary-7 "Glossary term") in a chart object.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
Load
*
Inline
[
id,timestamp,amount
9497,'2022-01-05 19:04:57',47.25,
9498,'2022-01-03 14:21:53',51.75,
9499,'2022-01-03 05:40:49',73.53,
9500,'2022-01-04 18:49:38',15.35,
9501,'2022-01-01 22:10:22',31.43,
9502,'2022-01-05 19:34:46',13.24,
9503,'2022-01-04 22:58:34',74.34,
9504,'2022-01-06 11:29:38',50.00,
9505,'2022-01-02 08:35:54',36.34,
9506,'2022-01-06 08:49:09',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: timestamp.

Create the following measure:

=minute(timestamp)

Results table

| timestamp | minute |
| --- | --- |
| 2022-01-01 22:10:22 | 10 |
| 2022-01-02 08:35:54 | 35 |
| 2022-01-03 05:40:49 | 40 |
| 2022-01-03 14:21:53 | 21 |
| 2022-01-04 18:49:38 | 49 |
| 2022-01-04 22:58:34 | 58 |
| 2022-01-05 19:04:57 | 4 |
| 2022-01-05 19:34:46 | 34 |
| 2022-01-06 08:49:09 | 49 |
| 2022-01-06 11:29:38 | 29 |

The values for minute are created by using the minute() function and passing the timestamp as the expression in a measure for the chart object.

## Example 3 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of timestamps, which is generated to represent entries at a ticket barrier.
- Information with each timestamp and its corresponding id, which is loaded into a table called Ticket\_Barrier\_Tracker.
- The default TimeStamp system variable (M/D/YYYY h:mm:ss[.fff] TT) is used.

The user would like a chart object that shows, by minute, the count of barrier entries.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

tmpTimeStampCreator:
	load
		*
    where year(date)=2022;
load
	date(recno()+makedate(2021,12,31)) as date
AutoGenerate 1;

join load
	maketime(floor(rand()*24),floor(rand()*59),floor(rand()*59)) as time
autogenerate 10000;

Ticket_Barrier_Tracker:
load
	recno() as id,
	timestamp(date + time) as timestamp
resident tmpTimeStampCreator;

drop table tmpTimeStampCreator;
```

Results

Do the following:

1. Load the data and open a [sheet](#glossary-8 "Glossary term"). Create a new table.
2. Create a calculated dimension using the following expression:

   =minute(timestamp)
3. Add the following [aggregation](#glossary-9 "Glossary term") measure to calculate total count of entries:

   =count(id)
4. Set the measure's Number formatting to Money.

Results table

| minute(timestamp) | =count(id) |
| --- | --- |
| 0 | 174 |
| 1 | 171 |
| 2 | 175 |
| 3 | 165 |
| 4 | 188 |
| 5 | 176 |
| 6 | 158 |
| 7 | 187 |
| 8 | 178 |
| 9 | 178 |
| 10 | 197 |
| 11 | 161 |
| 12 | 166 |
| 13 | 184 |
| 14 | 159 |
| 15 | 161 |
| 16 | 152 |
| 17 | 160 |
| 18 | 176 |
| 19 | 164 |
| 20 | 170 |
| 21 | 170 |
| 22 | 142 |
| 23 | 145 |
| 24 | 155 |
| + 35 more rows |  |
