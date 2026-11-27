---
title: "makedate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/makedate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# makedate Script and chart function

Expand/Collapse all

# makedate Script and chart function

This function returns a date calculated from the year YYYY, the month MM and the day DD.

Syntax:

MakeDate(YYYY [ , MM [ , DD ] ])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| YYYY | The year as an integer. |
| MM | The month as an integer. If no month is stated, 1 (January) is assumed. |
| DD | The day as an integer. If no day is stated, 1 (the 1st) is assumed. |

## When to use makedate

The makedate() function would commonly be used in the script for data generation to generate a calendar. This could also be used when the date [field](#glossary-0 "Glossary term") is not directly available as date, but needs some transformations to extract year, month and day components.

These examples use the date format MM/DD/YYYY. The date format is specified in the SET DateFormat statement at the top of your data [load script](#glossary-1 "Glossary term") . Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| makedate(2012) | Returns 01/01/2012. |
| makedate(12) | Returns 01/01/2012. |
| makedate(2012,12) | Returns 12/01/2012. |
| makedate(2012,2,14) | Returns 02/14/2012. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") containing a set of transactions for 2018, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system [variable](#glossary-3 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, transaction\_date, that returns a date in the format MM/DD/YYYY.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        makedate(transaction_year, transaction_month, transaction_day) as transaction_date
        ;
Load * Inline [
transaction_id, transaction_year, transaction_month, transaction_day, transaction_amount, transaction_quantity, customer_id
3750, 2018, 08, 30, 12423.56, 23, 2038593
3751, 2018, 09, 07, 5356.31, 6, 203521
3752, 2018, 09, 16, 15.75, 1, 5646471
3753, 2018, 09, 22, 1251, 7, 3036491
3754, 2018, 09, 22, 21484.21, 1356, 049681
3756, 2018, 09, 22, -59.18, 2, 2038593
3757, 2018, 09, 23, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_year
- transaction\_month
- transaction\_day
- transaction\_date

Results table

| transaction\_year | transaction\_month | transaction\_day | transaction\_date |
| --- | --- | --- | --- |
| 2018 | 08 | 30 | 08/30/2018 |
| 2018 | 09 | 07 | 09/07/2018 |
| 2018 | 09 | 16 | 09/16/2018 |
| 2018 | 09 | 22 | 09/22/2018 |
| 2018 | 09 | 23 | 09/23/2018 |

The transaction\_date field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the makedate() function and passing the year, month, day fields as function arguments.

The function then combines and converts these values into a date field, returning the results in the format of the DateFormat system variable.

## Example 2 – Modified DateFormat

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, transaction\_date, in the format DD/MM/YYYY without modifying the DateFormat system variable.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        date(makedate(transaction_year, transaction_month, transaction_day), ‘DD/MM/YYYY’) as transaction_date
        ;
Load * Inline [
transaction_id, transaction_year, transaction_month, transaction_day, transaction_amount, transaction_quantity, customer_id
3750, 2018, 08, 30, 12423.56, 23, 2038593
3751, 2018, 09, 07, 5356.31, 6, 203521
3752, 2018, 09, 16, 15.75, 1, 5646471
3753, 2018, 09, 22, 1251, 7, 3036491
3754, 2018, 09, 22, 21484.21, 1356, 049681
3756, 2018, 09, 22, -59.18, 2, 2038593
3757, 2018, 09, 23, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_year
- transaction\_month
- transaction\_day
- transaction\_date

Results table

| transaction\_year | transaction\_month | transaction\_day | transaction\_date |
| --- | --- | --- | --- |
| 2018 | 08 | 30 | 30/08/2018 |
| 2018 | 09 | 07 | 07/09/2018 |
| 2018 | 09 | 16 | 16/09/2018 |
| 2018 | 09 | 22 | 22/09/2018 |
| 2018 | 09 | 23 | 23/09/2018 |

In this instance, the makedate() function is nested inside the date() function. The second argument of the date() function sets the format of the makedate() function results as the required DD/MM/YYYY.

## Example 3 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for 2018, which is loaded into a table called Transactions.
- The transaction dates provided across two fields: year and month.

Create a chart object [measure](#glossary-5 "Glossary term") transaction\_date, that returns a date in the format MM/DD/YYYY.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load * Inline [
transaction_id, transaction_year, transaction_month, transaction_amount, transaction_quantity, customer_id
3750, 2018, 08, 12423.56, 23, 2038593
3751, 2018, 09, 5356.31, 6, 203521
3752, 2018, 09, 15.75, 1, 5646471
3753, 2018, 09, 1251, 7, 3036491
3754, 2018, 09, 21484.21, 1356, 049681
3756, 2018, 09, -59.18, 2, 2038593
3757, 2018, 09, 3177.4, 21, 203521
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- year
- month

To determine the transaction\_date, create this measure:

=makedate(transaction\_year,transaction\_month)

Results table

| transaction\_year | transaction\_month | transaction\_date |
| --- | --- | --- |
| 2018 | 08 | 08/01/2018 |
| 2018 | 09 | 09/01/2018 |

The transaction\_date measure is created in the chart object by using the makedate() function, and passing the year and month fields as function arguments.

The function then combines these values, as well as the assumed day value of 01. These values are then converted into a date field, returning the results in the format of the DateFormat system variable.

## Example 4 – Scenario

Load script and chart expression

Overview

Create a calendar dataset for the calendar year of 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Calendar:
	load
		*
    where year(date)=2022;
load
	date(recno()+makedate(2021,12,31)) as date
AutoGenerate 400;
```

Results

Results table

| date |
| --- |
| 01/01/2022 |
| 01/02/2022 |
| 01/03/2022 |
| 01/04/2022 |
| 01/05/2022 |
| 01/06/2022 |
| 01/07/2022 |
| 01/08/2022 |
| 01/09/2022 |
| 01/10/2022 |
| 01/11/2022 |
| 01/12/2022 |
| 01/13/2022 |
| 01/14/2022 |
| 01/15/2022 |
| 01/16/2022 |
| 01/17/2022 |
| 01/18/2022 |
| 01/19/2022 |
| 01/20/2022 |
| 01/21/2022 |
| 01/22/2022 |
| 01/23/2022 |
| 01/24/2022 |
| 01/25/2022 |
| + 340 more rows |

The makedate() function creates a date value for December 31, 2021. The recno() function provides the record number of the current record being loaded into the table, starting from 1. Therefore, the first record has the date January 1, 2022. Each successive recno() will then increment this date by 1. This expression is wrapped in a date() function to convert the value into a date. This process is repeated 400 times by the autogenerate function. Finally, by using a preceding load, a where condition can be used to only load dates from year 2022. This script generates a calendar containing every date in 2022.
