---
title: "yearend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# yearend Script and chart function

Expand/Collapse all

# yearend Script and chart function

This function returns
a value corresponding to a timestamp of the last millisecond of the
last day of the year containing date.
The default output format will be the DateFormat set in the script.

Syntax:

YearEnd( date[, period\_no[, first\_month\_of\_year
= 1]])

In other words, the yearend() function determines which year the date falls into. It then returns a timestamp, in date format, for the last millisecond of that year. The first month of the year is, by default, January. However, you can change which month is set as first by using the first\_month\_of\_year argument in the yearend() function.

Information note The yearend() function does not consider the FirstMonthOfYear system [variable](#glossary-0 "Glossary term"). The year begins on January 1 unless the first\_month\_of\_year argument is used to change it.

Diagram of yearend() function.

![Diagram that shows how the yearend() function identifies a date and the end of the year in which it takes place. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearend-diagram.png "Click to view full size")

When to use yearend

The yearend() function is used as part of an expression when you want the calculation to use the fraction of the year that has not yet occurred. For example, if you want to calculate the total interest not yet incurred during the year.

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the year which contains date. Negative values in period\_no indicate preceding years and positive values indicate succeeding years. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

You can use the following values to set the first month of year in the first\_month\_of\_year argument:

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
| yearend('10/19/2001') | Returns 12/31/2001 23:59:59. |
| yearend('10/19/2001', -1) | Returns 12/31/2000 23:59:59. |
| yearend('10/19/2001', 0, 4) | Returns 03/31/2002 23:59:59. |

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions between 2020 and 2022 is loaded into a table called ‘Transactions’.
- The date [field](#glossary-2 "Glossary term") has been provided in the DateFormat system variable (MM/DD/YYYY) format.
- A [preceding load](#glossary-3 "Glossary term") statement which contains the following:

  - yearend() function which is set as the year\_end field.
  - Timestamp() function which is set as the year\_end\_timestamp field.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       yearend(date) as year_end,
       timestamp(yearend(date)) as year_end_timestamp
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
- year\_end
- year\_end\_timestamp

Results table

| id | date | year\_end | year\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8189 | 02/26/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8190 | 03/27/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8191 | 04/16/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8192 | 05/21/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8193 | 08/14/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8194 | 10/07/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8195 | 12/05/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8196 | 01/22/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8197 | 02/03/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8198 | 03/17/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8199 | 04/23/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8200 | 05/04/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8201 | 06/30/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8202 | 07/26/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8203 | 12/27/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8204 | 06/06/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8205 | 07/18/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8206 | 11/14/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8207 | 12/12/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |

The ‘year\_end’ field is created in the preceding load statement by using the yearend() function and passing the date field as the function’s argument.

The yearend() function initially identifies which year the date value falls into and returns a timestamp for the last millisecond of that year.

Diagram of yearend() function with transaction 8199 selected.

![Diagram that shows that transaction 8199 took place on April 23, 2021 and that the yearend() function then returns the last millisecond of that year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearend-example1-diagram.png "Click to view full size")

Transaction 8199 took place on April 23, 2021. The yearend() function returns the last millisecond of that year, which is December 31 at 11:59:59 PM.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the task is to create a field, ‘previous\_year\_end’ , that returns the end date timestamp of the year prior to the year in which a transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       yearend(date,-1) as previous_year_end,
       timestamp(yearend(date,-1)) as previous_year_end_timestamp
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
- previous\_year\_end
- previous\_ year\_end\_timestamp

Results table

| id | date | previous\_year\_end | previous\_year\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8189 | 02/26/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8190 | 03/27/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8191 | 04/16/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8192 | 05/21/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8193 | 08/14/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8194 | 10/07/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8195 | 12/05/2020 | 12/31/2019 | 12/31/2019 11:59:59 PM |
| 8196 | 01/22/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8197 | 02/03/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8198 | 03/17/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8199 | 04/23/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8200 | 05/04/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8201 | 06/30/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8202 | 07/26/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8203 | 12/27/2021 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8204 | 06/06/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8205 | 07/18/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8206 | 11/14/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8207 | 12/12/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |

Because a period\_no of -1 was used as the offset argument in the yearend() function, the function first identifies the year that the transactions take place in. It then looks one year prior and identifies the last millisecond of that year.

Diagram of yearend() function with a period\_no of -1.

![Diagram that shows how a period_no of negative one makes the yearend() function identify the last millisecond of the previous year. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearend-example2-diagram.png "Click to view full size")

Transaction 8199 takes place on April 23, 2021. The yearend() function returns the last millisecond of the prior year, December 31, 2020 at 11:59:59 PM, for the ‘previous\_year\_end’ field.

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
       yearend(date,0,4) as year_end,
       timestamp(yearend(date,0,4)) as year_end_timestamp
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
- year\_end
- year\_end\_timestamp

Results table

| id | date | year\_end | year\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 03/31/2020 | 3/31/2020 11:59:59 PM |
| 8189 | 02/26/2020 | 03/31/2020 | 3/31/2020 11:59:59 PM |
| 8190 | 03/27/2020 | 03/31/2020 | 3/31/2020 11:59:59 PM |
| 8191 | 04/16/2020 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8192 | 05/21/2020 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8193 | 08/14/2020 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8194 | 10/07/2020 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8195 | 12/05/2020 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8196 | 01/22/2021 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8197 | 02/03/2021 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8198 | 03/17/2021 | 03/31/2021 | 3/31/2021 11:59:59 PM |
| 8199 | 04/23/2021 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8200 | 05/04/2021 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8201 | 06/30/2021 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8202 | 07/26/2021 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8203 | 12/27/2021 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8204 | 06/06/2022 | 03/31/2023 | 3/31/2023 11:59:59 PM |
| 8205 | 07/18/2022 | 03/31/2023 | 3/31/2023 11:59:59 PM |
| 8206 | 11/14/2022 | 03/31/2023 | 3/31/2023 11:59:59 PM |
| 8207 | 12/12/2022 | 03/31/2023 | 3/31/2023 11:59:59 PM |

Because the first\_month\_of\_year argument of 4 is used in the yearend() function, it sets the first day of the year to April 1, and the last day of the year to March 31.

Diagram of yearend() function with April as the first month of the year.

![Diagram that shows how the yearend() function works when the first_month_of_year is set to four. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearend-example3-diagram.png "Click to view full size")

Transaction 8199 takes place on April 23, 2021. Because the yearend() function sets the start of the year to April 1, it returns March 31, 2022 as the ‘year\_end’ value for the transaction.

## Example 4 – Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that returns the end date timestamp of the year in which a transaction took place is created as a [measure](#glossary-4 "Glossary term") in a chart object of the application.

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

- =yearend(date)
- =timestamp(yearend(date))

Results table

| id | date | =yearend(date) | =timestamp(yearend(date)) |
| --- | --- | --- | --- |
| 8188 | 01/13/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8189 | 02/26/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8190 | 03/27/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8191 | 04/16/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8192 | 05/21/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8193 | 08/14/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8194 | 10/07/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8195 | 12/05/2020 | 12/31/2020 | 12/31/2020 11:59:59 PM |
| 8196 | 01/22/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8197 | 02/03/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8198 | 03/17/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8199 | 04/23/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8200 | 05/04/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8201 | 06/30/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8202 | 07/26/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8203 | 12/27/2021 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8204 | 06/06/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8205 | 07/18/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8206 | 11/14/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8207 | 12/12/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |

The ‘end\_of\_year’ measure is created in the chart object by using the yearend() function and passing the date field as the function’s argument.

The yearend() function initially identifies which year the date value falls into returning a timestamp for the last millisecond of that year.

Diagram of yearend() function that shows Transaction 8199 took place in April.

![Diagram that shows the range of time which the yearend() function identifies and returns a timestamp for. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearend-example4-diagram.png "Click to view full size")

Transaction 8199 takes place on April 23, 2021. The yearend() function returns the last millisecond of that year, which is December 31 at 11:59:59 PM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset is loaded into a table called ‘Employee\_Expenses’. The table contains the following fields:

  - employee IDs
  - employee name
  - average daily expense claims of each employee

The end user would like a chart object that displays, by employee id and employee name, the estimated expense claims still to be incurred for the remainder of the year. The financial year begins in January.

Load script

```
Employee_Expenses:
Load
*
Inline
[
employee_id,employee_name,avg_daily_claim
182,Mark, $15
183,Deryck, $12.5
184,Dexter, $12.5
185,Sydney,$27
186,Agatha,$18
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- employee\_id
- employee\_name

To calculate the projected expense claims, create the following measure:

=(yearend(today(1))-today(1))\*avg\_daily\_claim

Set the measure’s Number Formatting to Money.

Results table

| employee\_id | employee\_name | =(yearend(today(1))-today(1))\*avg\_daily\_claim |
| --- | --- | --- |
| 182 | Mark | $3240.00 |
| 183 | Deryck | $2700.00 |
| 184 | Dexter | $2700.00 |
| 185 | Sydney | $5832.00 |
| 186 | Agatha | $3888.00 |

By using today’s date as its only argument, the yearend() function returns the end date of the current year. Then, by subtracting today’s date from the year end date, the expression returns the number of days remaining in this year.

This value is then multiplied by the average daily expense claim by each employee to calculate the estimated value of claims each employee is expected to make in the remaining year.
