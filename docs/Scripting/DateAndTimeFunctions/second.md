---
title: "second Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/second.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# second Script and chart function

Expand/Collapse all

# second Script and chart function

This function returns an integer representing the second when the fraction
of the expression is interpreted as a time
according to the standard number interpretation.

Syntax:

second (expression)

Return data type:  integer

## When to use second

The second() function is useful when you would like to compare aggregations by second. For example, the function can be used if you would like to see activity count distribution by second.

These [dimensions](#glossary-0 "Glossary term") can be created either in the [load script](#glossary-1 "Glossary term") by using the function to create a [field](#glossary-2 "Glossary term") in a Master Calendar table, or used directly in a [chart](#glossary-3 "Glossary term") as a calculated [dimension](#glossary-4 "Glossary term").

Function examples

| Example | Result |
| --- | --- |
| second( '09:14:36' ) | returns 36 |
| second( '0.5555' ) | returns 55 ( Because 0.5555 = 13:19:55 ) |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – Variable

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-5 "Glossary term") containing transactions by timestamp, which is loaded into a table called Transactions.
- The default TimeStamp system [variable](#glossary-6 "Glossary term") (M/D/YYYY h:mm:ss[.fff] TT) is used.
- The creation of a field, second, to calculate when purchases took place.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        second(date) as second
        ;
Load
*
Inline
[
id,date,amount
9497,'01/05/2022 7:04:57 PM',47.25
9498,'01/03/2022 2:21:53 PM',51.75
9499,'01/03/2022 5:40:49 AM',73.53
9500,'01/04/2022 6:49:38 PM',15.35
9501,'01/01/2022 10:10:22 PM',31.43
9502,'01/05/2022 7:34:46 PM',13.24
9503,'01/06/2022 10:58:34 PM',74.34
9504,'01/06/2022 11:29:38 AM',50.00
9505,'01/02/2022 8:35:54 AM',36.34
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- second

Results table

| date | second |
| --- | --- |
| 01/01/2022 10:10:22 PM | 22 |
| 01/02/2022 8:35:54 AM | 54 |
| 01/03/2022 5:40:49 AM | 49 |
| 01/03/2022 2:21:53 PM | 53 |
| 01/04/2022 6:49:38 PM | 38 |
| 01/05/2022 7:04:57 PM | 57 |
| 01/05/2022 7:34:46 PM | 46 |
| 01/06/2022 8:49:09 AM | 9 |
| 01/06/2022 11:29:38 AM | 38 |
| 01/06/2022 10:58:34 PM | 34 |

The values in the second field are created by using the second() function and passing the date as the expression in the [preceding load](#glossary-7 "Glossary term").statement.

## Example 2 – Chart object

Load script and chart expression

Overview

Open the [Data load editor](#glossary-8 "Glossary term") and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The second values are calculated via a [measure](#glossary-9 "Glossary term") in a chart object.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
Load
*
Inline
[
id,date,amount
9497,'01/05/2022 7:04:57 PM',47.25
9498,'01/03/2022 2:21:53 PM',51.75
9499,'01/03/2022 5:40:49 AM',73.53
9500,'01/04/2022 6:49:38 PM',15.35
9501,'01/01/2022 10:10:22 PM',31.43
9502,'01/05/2022 7:34:46 PM',13.24
9503,'01/06/2022 10:58:34 PM',74.34
9504,'01/06/2022 11:29:38 AM',50.00
9505,'01/02/2022 8:35:54 AM',36.34
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:date.

Create the following measure:

=second(date)

Results table

| date | =second(date) |
| --- | --- |
| 01/01/2022 10:10:22 PM | 22 |
| 01/02/2022 8:35:54 AM | 54 |
| 01/03/2022 5:40:49 AM | 49 |
| 01/03/2022 2:21:53 PM | 53 |
| 01/04/2022 6:49:38 PM | 38 |
| 01/05/2022 7:04:57 PM | 57 |
| 01/05/2022 7:34:46 PM | 46 |
| 01/06/2022 8:49:09 AM | 9 |
| 01/06/2022 11:29:38 AM | 38 |
| 01/06/2022 10:58:34 PM | 34 |

The values for second are created by using the second() function and passing the date as the expression in a measure for the chart object.

## Example 3 – Scenario

Load script and chart expressions

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of timestamps, which is generated to represent the traffic to a particular festival's ticket sales website. These timestamps and a corresponding id are loaded into a table called Web\_Traffic.
- The TimeStamp system variable M/D/YYYY h:mm:ss[.fff] TT is used.

In this scenario, there were 10000 tickets, which went on sale at 9:00 AM on May 20, 2021. One minute later, the tickets were sold out.

The user would like a chart object that shows, by second, the count of visits to the website.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

tmpTimeStampCreator:
load
    makedate(2022,05,20) as date
AutoGenerate 1;

join load
    maketime(9+floor(rand()*2),0,floor(rand()*59)) as time
autogenerate 10000;

Web_Traffic:
load
    recno() as id,
    timestamp(date + time) as timestamp
resident tmpTimeStampCreator;

drop table tmpTimeStampCreator;
```

Results

Do the following:

1. Load the data and open a [sheet](#glossary-10 "Glossary term"). Create a new table.
2. Next, create a calculated dimensions using the following expression:

   =second(timestamp)
3. Create an [aggregation](#glossary-11 "Glossary term") measure to calculate the total count of entries:

   =count(id)

The results table will look similar to the table below, but with different values for the aggregation measure:

Results table

| second(timestamp) | =count(id) |
| --- | --- |
| 0 | 150 |
| 1 | 184 |
| 2 | 163 |
| 3 | 178 |
| 4 | 179 |
| 5 | 158 |
| 6 | 177 |
| 7 | 169 |
| 8 | 149 |
| 9 | 186 |
| 10 | 169 |
| 11 | 179 |
| 12 | 186 |
| 13 | 182 |
| 14 | 180 |
| 15 | 153 |
| 16 | 191 |
| 17 | 203 |
| 18 | 158 |
| 19 | 159 |
| 20 | 163 |
| + 39 more rows |  |
