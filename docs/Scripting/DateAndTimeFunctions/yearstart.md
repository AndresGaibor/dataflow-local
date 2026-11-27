---
title: "yearstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# yearstart Script and chart function

Expand/Collapse all

# yearstart Script and chart function

This function returns
a timestamp corresponding to the start of the first day of the year containing date.
The default output format will be the DateFormat set in the script.

Syntax:

YearStart(date[, period\_no[, first\_month\_of\_year]])

In other words, the yearstart() function determines which year the date falls into. It then returns a timestamp, in date format, for the first millisecond of that year. The first month of the year is, by default, January; however, you can change which month is set as first by using the first\_month\_of\_year argument in the yearstart() function.

Diagram of yearstart() function that shows the range of time that the function can cover.

![Diagram that shows the yearstart() function identifies dates within a given year period and returns the timestamp of the start of the year for dates that fall into that given year. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearstart-diagram.png "Click to view full size")

When to use yearstart

The yearstart() function is used as part of an expression when you want the calculation to use the fraction of the year that has elapsed thus far. For example, if you want to calculate the interest that has accumulated in a year to date.

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the year which contains date. Negative values in period\_no indicate preceding years and positive values indicate succeeding years. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

The following months can be used in the first\_month\_of\_year argument:

first\_month\_of\_year values

| Month | Value |
| --- | --- |
| February | 2 |
| March | 3 |
| April | 4 |
| May | 5 |
| June | 6 |
| July | 7 |
| August | 8 |
| September | 9 |
| October | 10 |
| November | 11 |
| December | 12 |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| yearstart('10/19/2001') | Returns 01/01/2001 00:00:00. |
| yearstart('10/19/2001',-1) | Returns 01/01/2000 00:00:00. |
| yearstart('10/19/2001',0,4) | Returns 04/01/2001 00:00:00. |

## Example 1 – Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-0 "Glossary term") containing a set of transactions between 2020 and 2022 is loaded into a table called ‘Transactions’.
- The date [field](#glossary-1 "Glossary term") has been provided in the DateFormat system [variable](#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- A [preceding load](#glossary-3 "Glossary term") statement which contains the following:

  - yearstart() function which is set as the year\_start field.
  - Timestamp() function which is set as the year\_start\_timestamp field

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       yearstart(date) as year_start,
       timestamp(yearstart(date)) as year_start_timestamp
       ;
Load
*
Inline
[
id,date,amount
8188,01/13/2020,37.23
8189,02/26/2020,17.17
8190,03/27/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,06/06/2022,46.23
8205,07/18/2022,84.21
8206,11/14/2022,96.24
8207,12/12/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- year\_start
- year\_start\_timestamp

Results table

| id | date | year\_start | year\_start\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8189 | 02/26/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8190 | 03/27/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8191 | 04/16/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8192 | 05/21/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8193 | 08/14/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8194 | 10/07/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8195 | 12/05/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8196 | 01/22/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8197 | 02/03/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8198 | 03/17/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8199 | 04/23/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8200 | 05/04/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8201 | 06/30/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8202 | 07/26/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8203 | 12/27/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8204 | 06/06/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8205 | 07/18/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8206 | 11/14/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8207 | 12/12/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |

The ‘year\_start’ field is created in the preceding load statement by using the yearstart() function and passing the date field as the function’s argument.

The yearstart() function initially identifies which year the date value falls into and returns a timestamp for the first millisecond of that year.

Diagram of the yearstart() function and transaction 8199.

![Diagram that shows that transaction 8199 took place on April 23, and that the yearstart() function identifies the start of that year. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearstart-example1-diagram.png "Click to view full size")

Transaction 8199 took place on April 23, 2021. The yearstart() function returns the first millisecond of that year, which is January 1 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the task is to create a field, ‘previous\_year\_start’, that returns the start date timestamp of the year prior to the year in which a transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       yearstart(date,-1) as previous_year_start,
       timestamp(yearstart(date,-1)) as previous_year_start_timestamp
       ;
Load
*
Inline
[
id,date,amount
8188,01/13/2020,37.23
8189,02/26/2020,17.17
8190,03/27/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,06/06/2022,46.23
8205,07/18/2022,84.21
8206,11/14/2022,96.24
8207,12/12/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- previous\_year\_start
- previous\_ year\_start\_timestamp

Results table

| id | date | previous\_year\_start | previous\_year\_start\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8189 | 02/26/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8190 | 03/27/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8191 | 04/16/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8192 | 05/21/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8193 | 08/14/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8194 | 10/07/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8195 | 12/05/2020 | 01/01/2019 | 1/1/2019 12:00:00 AM |
| 8196 | 01/22/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8197 | 02/03/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8198 | 03/17/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8199 | 04/23/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8200 | 05/04/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8201 | 06/30/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8202 | 07/26/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8203 | 12/27/2021 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8204 | 06/06/2022 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8205 | 07/18/2022 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8206 | 11/14/2022 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8207 | 12/12/2022 | 01/01/2021 | 1/1/2021 12:00:00 AM |

In this instance, because a period\_no of -1 is used as the offset argument in the yearstart() function, the function first identifies the year that the transactions take place in. It then looks one year prior and identifies the first millisecond of that year.

Diagram of the yearstart() function with a period\_no of -1.

![Diagram that shows the yearstart() function with a period_no of negative one which places the year range of the function back one year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearstart-example2-diagram.png "Click to view full size")

Transaction 8199 took place on April 23, 2021. The yearstart() function returns the first millisecond of the prior year, January 1, 2020 at 12:00:00 AM, for the ‘previous\_year\_start’ field.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the company policy is for the year to begin from April 1.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       yearstart(date,0,4) as year_start,
       timestamp(yearstart(date,0,4)) as year_start_timestamp
       ;
Load
*
Inline
[
id,date,amount
8188,01/13/2020,37.23
8189,02/26/2020,17.17
8190,03/27/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,06/06/2022,46.23
8205,07/18/2022,84.21
8206,11/14/2022,96.24
8207,12/12/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- year\_start
- year\_start\_timestamp

Results table

| id | date | year\_start | year\_start\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 04/01/2019 | 4/1/2019 12:00:00 AM |
| 8189 | 02/26/2020 | 04/01/2019 | 4/1/2019 12:00:00 AM |
| 8190 | 03/27/2020 | 04/01/2019 | 4/1/2019 12:00:00 AM |
| 8191 | 04/16/2020 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8192 | 05/21/2020 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8193 | 08/14/2020 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8194 | 10/07/2020 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8195 | 12/05/2020 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8196 | 01/22/2021 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8197 | 02/03/2021 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8198 | 03/17/2021 | 04/01/2020 | 4/1/2020 12:00:00 AM |
| 8199 | 04/23/2021 | 04/01/2021 | 4/1/2021 12:00:00 AM |
| 8200 | 05/04/2021 | 04/01/2021 | 4/1/2021 12:00:00 AM |
| 8201 | 06/30/2021 | 04/01/2021 | 4/1/2021 12:00:00 AM |
| 8202 | 07/26/2021 | 04/01/2021 | 4/1/2021 12:00:00 AM |
| 8203 | 12/27/2021 | 04/01/2021 | 4/1/2021 12:00:00 AM |
| 8204 | 06/06/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 8205 | 07/18/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 8206 | 11/14/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 8207 | 12/12/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |

In this instance, because the first\_month\_of\_year argument of 4 is used in the yearstart() function, it sets the first day of the year to April 1, and the last day of the year to March 31.

Diagram of the yearstart() function with the first month set as April.

![Diagram that shows yearstart() function with the first month of the year set as April. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearstart-example3-diagram.png "Click to view full size")

Transaction 8199 took place on April 23, 2021. Because the yearstart() function sets the start of the year to April 1 and returns it as the ‘year\_start’ value for the transaction.

## Example 4 – Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that returns the start date timestamp of the year in which a transaction took place is created as a [measure](#glossary-4 "Glossary term") in a chart object of the application.

Load script

```
Transactions:
Load
*
Inline
[
id,date,amount
8188,01/13/2020,37.23
8189,02/26/2020,17.17
8190,03/27/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,06/06/2022,46.23
8205,07/18/2022,84.21
8206,11/14/2022,96.24
8207,12/12/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date

To calculate in which year a transaction took place, create the following measures:

- =yearstart(date)
- =timestamp(yearstart(date))

Results table

| id | date | =yearstart(date) | =timestamp(yearstart(date)) |
| --- | --- | --- | --- |
| 8188 | 06/06/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8189 | 07/18/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8190 | 11/14/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8191 | 12/12/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 8192 | 01/22/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8193 | 02/03/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8194 | 03/17/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8195 | 04/23/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8196 | 05/04/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8197 | 06/30/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8198 | 07/26/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8199 | 12/27/2021 | 01/01/2021 | 1/1/2021 12:00:00 AM |
| 8200 | 01/13/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8201 | 02/26/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8202 | 03/27/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8203 | 04/16/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8204 | 05/21/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8205 | 08/14/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8206 | 10/07/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |
| 8207 | 12/05/2020 | 01/01/2020 | 1/1/2020 12:00:00 AM |

The ‘start\_of\_year’ measure is created in the chart object by using the yearstart() function and passing the date field as the function’s argument.

The yearstart() function initially identifies which year the date value falls into and returns a timestamp for the first millisecond of that year.

Diagram of theyearstart() function and transaction 8199.

![Diagram that shows the yearstart() function identify the year that transaction 8199 takes place in and the timestamp of the start of that year. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearstart-example4-diagram.png "Click to view full size")

Transaction 8199 took place on April 23, 2021. The yearstart() function returns the first millisecond of that year, which is January 1 at 12:00:00 AM.

## Example 5 – Scenario

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset is loaded into a table called ‘Loans’. The table contains the following fields:

  - Loan IDs.
  - The balance at the beginning of the year.
  - The simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan id, the current interest that has been accrued on each loan in the year to date.

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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- loan\_id
- start\_balance

To calculate the accumulated interest, create the following measure:

=start\_balance\*(rate\*(today(1)-yearstart(today(1)))/365)

Set the measure’s Number Formatting to Money.

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)-yearstart(today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $39.73 |
| 8189 | $15000.00 | $339.66 |
| 8190 | $17500.00 | $166.85 |
| 8191 | $21000.00 | $283.64 |
| 8192 | $90000.00 | $3003.29 |

The yearstart() function, using today’s date as its only argument, returns the start date of the current year. By subtracting that result from the current date, the expression returns the number of days that have elapsed so far this year.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate for the period. The effective interest rate for the period is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this year.
