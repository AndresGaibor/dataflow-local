---
title: "monthsstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "dimensions"]
---
Expand/Collapse all

# monthsstart Script and chart function

This function returns a value corresponding to the timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for a previous or following time period.The default output format is the DateFormat set in the script.

Syntax:

MonthsStart(n\_months, date[, period\_no [, first\_month\_of\_year]])

Return data type:  dual

Diagram of `monthsstart()` function

![Example diagram showing how each of the elements of the function work together to return the timestamp result. The year is broken up into a number of segments and given a date input, the function returns a timestamp value.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsstart-general.png)

The `monthsstart()` function divides the year into segments based on the `n_months` argument provided. It then evaluates what segment each date provided falls into and returns the first millisecond of that segment, in date format. The function also provides the ability to return the start timestamp from preceding or following segments, as well as redefining which is the first month of the year.

The following segments of the year are available in the function as `n_month` arguments:

Possible `n_month` arguments

| Periods | Number of months |
| --- | --- |
| month | 1 |
| bi-month | 2 |
| quarter | 3 |
| four months | 4 |
| half-year | 6 |

Arguments

| Argument | Description |
| --- | --- |
| n\_months | The number of months that defines the period. An integer or expression that resolves to an integer that must be one of: 1 (equivalent to the inmonth() function), 2 (bi-month), 3 (equivalent to the inquarter()function), 4 (four-month period), or 6 (half year). |
| date | The date or timestamp to evaluate. |
| period\_no | The period can be offset by period\_no, an integer, or expression resolving to an integer, where the value 0 indicates the period that contains base\_date. Negative values in period\_no indicate preceding periods and positive values indicate succeeding periods. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use monthsstart

The `monthsstart()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of a period that has not yet occurred. This could be used, for example, to provide an input [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-0 "Glossary term") to let the user calculate the total interest that has been accumulated so far in the month, quarter, or half-year.

Function examples

| Example | Result |
| --- | --- |
| `monthsstart(4, '10/19/2013')` | Returns 09/01/2013. |
| `monthsstart(4, '10/19/2013, -1)` | Returns 05/01/2013. |
| `monthsstart(4, '10/19/2013', 0, 2 )` | Returns 10/01/2013, because the start of the year becomes month 2. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-2 "Glossary term") provided in the `DateFormat` system variable (MM/DD/YYYY) format.
- The creation of a field, `bi_monthly_start`, that groups transactions into bi-monthly segments and returns the starting timestamp of the segment for each transaction.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthsstart(2,date) as bi_monthly_start,
        timestamp(monthsstart(2,date)) as bi_monthly_start_timestamp
        ;
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
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
- `bi_monthly_start`
- `bi_monthly_start_timestamp`

Results table

| date | bi\_monthly\_start | bi\_monthly\_start\_timestamp |
| --- | --- | --- |
| 2/19/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 3/7/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 3/30/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/5/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/1/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/22/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/15/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/26/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/2/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/8/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/19/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 9/26/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/14/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/29/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |

The `bi_monthly_start` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-3 "Glossary term") statement by using the `monthsstart()` function. The first argument provided is 2, dividing the year into bi-monthly segments. The second argument identifies which field is being evaluated.

Diagram of `monthsstart()` function, example with no additional arguments

![Diagram showing the results of using the monthsstart function to determine the segment of the year in which a transaction took place. In this case, the year is broken up into segments and the input date is converted to a timestamp.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsstart-example-no-add-arg.png)

Transaction 8195 takes place on May 22. The `monthsstart()` function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. Therefore, the function returns the first millisecond of this segment, May 1, 2022 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `prev_bi_monthly_start`, that returns the first millisecond of the bi-monthly segment before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthsstart(2,date,-1) as prev_bi_monthly_start,
	    timestamp(monthsstart(2,date,-1)) as prev_bi_monthly_start_timestamp
	    ;
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
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
- `prev_bi_monthly_start`
- `prev_bi_monthly_start_timestamp`

Results table

| date | prev\_bi\_monthly\_start | prev\_bi\_monthly\_start\_timestamp |
| --- | --- | --- |
| 2/19/2022 | 11/01/2021 | 11/1/2021 12:00:00 AM |
| 3/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 3/30/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 4/5/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 4/16/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 5/1/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/7/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/22/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 6/15/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 6/26/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 7/9/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 7/22/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 7/23/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 7/27/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 8/2/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 8/8/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 8/19/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 9/26/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 10/14/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 10/29/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |

By using -1 as the `period_no` argument in the `monthsstart()` function, after initially dividing a year into bi-monthly segments, the function then returns the first millisecond of the previous bi-monthly segment to when a transaction takes place.

Diagram of `monthsstart()` function, period\_no example

![Diagram showing the results of using the monthsstart function to determine the segment of the year in which a transaction took place. In this case, the year is broken up into segments and the input date is converted to a timestamp.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsstart-example-period-no.png)

Transaction 8195 occurs in the segment between May and June. Therefore, the previous bi-monthly segment was between March 1 and April 30, so the function returns the first millisecond of this segment, March 1, 2022 at 12:00:00 AM.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `bi_monthly_start`, that groups transactions into bi-monthly segments and returns the starting timestamp of the set for each transaction.

However, in this example, we also need to set April as the first month of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthsstart(2,date,0,4) as bi_monthly_start,
        timestamp(monthsstart(2,date,0,4)) as bi_monthly_start_timestamp
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
- `bi_monthly_start`
- `bi_monthly_start_timestamp`

Results table

| date | bi\_monthly\_start | bi\_monthly\_start\_timestamp |
| --- | --- | --- |
| 2/19/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 3/7/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 3/30/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 4/5/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 4/16/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/1/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/7/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/22/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 6/15/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 6/26/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/9/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/22/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/23/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/27/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 8/2/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/8/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/19/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 9/26/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |

By using 4 as the `first_month_of_year` argument in the `monthsstart()` function, the function begins the year on April 1. It then divides the year into bi-monthly segments: Apr-May,Jun-Jul,Aug-Sep,Oct-Nov,Dec-Jan,Feb-Mar.

Diagram of `monthsstart()` function, first\_month\_of\_year example

![Diagram showing the results of using the monthsstart function to determine the segment of the year in which a transaction took place. In this case, the year is broken up into segments and the input date is converted to a timestamp.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsstart-example-first-mth-yr.png)

Transaction 8195 took place on May 22 and falls into the segment between April 1 and May 31. Therefore, the function returns the first millisecond of this segment, April 1, 2022 at 12:00:00 AM.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation which groups transactions into bi-monthly segments and returns the starting timestamp of the set for each transaction is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,2/19/2022,37.23
8189,3/7/2022,17.17
8190,3/30/2022,88.27
8191,4/5/2022,57.42
8192,4/16/2022,53.80
8193,5/1/2022,82.06
8194,5/7/2022,40.39
8195,5/22/2022,87.21
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

Create the following measures:

`=monthsstart(2,date)`

`=timestamp(monthsstart(2,date))`

These calculations will retrieve the starting timestamp of the bi-monthly segment in which each transaction took place.

Results table

| date | =monthsstart(2,date) | =timestamp(monthsstart(2,date)) |
| --- | --- | --- |
| 9/26/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/14/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/29/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/2/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/8/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/19/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 5/1/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/22/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/15/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/26/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 3/7/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 3/30/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/5/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 2/19/2022 | 01/01/2022 | 1/1/2021 12:00:00 AM |

Diagram of `monthsstart()` function, chart object example

![Diagram showing the results of using the monthsstart function to determine the segment of the year in which a transaction took place. In this case, the year is broken up into segments and the input date is converted to a timestamp.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthsstart-example-chart-object.png)

Transaction 8195 took place on May 22. The `monthsstart()` function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. Therefore, the function returns the first millisecond of this segment, 05/01/2022 12:00:00 AM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of loan balances, which is loaded into a table called `Loans`.
- Data consisting of loan IDs, the balance at the start of the month, and the simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan ID, the current interest that has been accrued on each loan for the period of their choosing. The financial year begins in January.

Load script

```
SET DateFormat='MM/DD/YYYY';

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

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-7 "Glossary term").

At the start of the load script, a variable (`vPeriod`) has been created that will be tied to the variable input control. Next, configure the variable as a [custom object](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-8 "Glossary term") in the sheet.

Do the following:

1. In the assets panel, click **Charts**.
2. Under **Dashboard objects**, drag a **Variable input** onto the sheet.
3. Enter a title for the chart object.
4. Under **Variable**, select **vPeriod** as the Name and set the object to show as a **Drop down**.
5. Under **Values**, configure the object to use dynamic values. Enter the following:  
   `='1~month|2~bi-month|3~quarter|4~tertial|6~half-year'`

Next, create the results table.

Do the following:

1. Create a new table. Add the following fields as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm#glossary-9 "Glossary term").

   - `employee_id`
   - `employee_name`
2. Create a measure to calculate the accumulated interest:

   `=start_balance*(rate*(today(1)-monthsstart($(vPeriod),today(1)))/365)`
3. Set the measure's **Number formatting** to **Money**.Click Edit sheet to finish editing. You can now modify the data shown in the table by adjusting the time segment in the variable object.

This is what the results table will look like when the `month` period option is selected:

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)-monthsstart($(vPeriod),today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $7.95 |
| 8189 | $15000.00 | $67.93 |
| 8190 | $17500.00 | $33.37 |
| 8191 | $21000.00 | $56.73 |
| 8192 | $90000.00 | $600.66 |

The `monthsstart()` function, using the user’s input as its first argument and today’s date as its second argument, returns the start date of the period of the user’s choosing. By subtracting that result from the current date, the expression returns the number of days that have elapsed so far in this period.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate incurred for this period. The result is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this period.
