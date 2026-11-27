---
title: "monthsend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# monthsend Script and chart function

Expand/Collapse all

# monthsend Script and chart function

This function returns a value corresponding to the timestamp of the last millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for the end of a previous or following time period. The default output format is the DateFormat set in the script.

Syntax:

MonthsEnd(n\_months, date[, period\_no [, first\_month\_of\_year]])

Return data type:  dual

Diagram of monthsend function.

![Diagram showing how monthsend function can be used to identify the latest timestamp of chosen period.  ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-MonthsEnd-diagram1.png "Click to view full size")

Arguments

| Argument | Description |
| --- | --- |
| n\_months | The number of months that defines the period. An integer or expression that resolves to an integer that must be one of: 1 (equivalent to the inmonth() function), 2 (bi-month), 3 (equivalent to the inquarter()function), 4 (four-month period), or 6 (half year). |
| date | The date or timestamp to evaluate. |
| period\_no | The period can be offset by period\_no, an integer, or expression resolving to an integer, where the value 0 indicates the period that contains base\_date. Negative values in period\_no indicate preceding periods and positive values indicate succeeding periods. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

The monthsend() function divides the year into segments based on the n\_months argument provided. It then evaluates what segment each date provided falls into and returns the last millisecond, in date format, of that segment. The function can return the end timestamp from preceding or following segments as well as redefine the first month of the year.

The following segments of the year are available in the function as n\_month arguments.

n\_month arguments

| Period | Number of months |
| --- | --- |
| month | 1 |
| bi-month | 2 |
| quarter | 3 |
| four months | 4 |
| half-year | 6 |

When to use monthsend

The monthsend() function is used as part of an expression when the user would like the calculation to use the fraction of the month that has elapsed so far. The user has the opportunity, using a [variable](#glossary-0 "Glossary term") to select the period of their choosing. For example, the monthsend() can provide an input variable to let the user calculate the total interest not yet incurred during the month, quarter, or half-year.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| monthsend(4, '07/19/2013') | Returns 08/31/2013. |
| monthsend(4, '10/19/2013', -1) | Returns 08/31/2013. |
| monthsend(4, '10/19/2013', 0, 2) | Returns 01/31/2014.  Because the start of the year becomes month 2. |

## Example 1 - Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for 2022 is loaded into a table called ‘Transactions’.
- A date [field](#glossary-2 "Glossary term") provided in the DateFormat system variable (MM/DD/YYYY) format.
- A [preceding load](#glossary-3 "Glossary term") statement containing:

  - The monthsend function which is set as the field, ‘bi\_monthly\_end’. This groups transactions into bi-monthly segments.
  - The timestamp function which returns the starting timestamp of the segment for each transaction.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							monthsend(2,date) as bi_monthly_end,
							timestamp(monthsend(2,date)) as bi_monthly_end_timestamp
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

- id
- date
- bi\_monthly\_end
- bi\_monthly\_end\_timestamp

Results table

| id | date | bi\_monthly\_end | bi\_monthly\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8195 | 5/22/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |

The ‘bi\_monthly\_end’ field is created in the preceding load statement by using the monthsend() function. The first argument provided is 2, dividing the year into bi-monthly segments. The second argument identifies which field is being evaluated.

Diagram of monthsend function with bi-monthly segments.

![Diagram showing how the monthsend function identifies the selected bi-monthly segment. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-MonthsEnd-example1-diagram.png "Click to view full size")

Transaction 8195 takes place on May 22. The monthsend() function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. As a result, the function returns the last millisecond of this segment, 06/30/2022 11:59:59 PM.

## Example 2 - period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

In this example, the task is to create a field, ‘prev\_bi\_monthly\_end’, that returns the first millisecond of the bi-monthly segment before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							monthsend(2,date,-1) as prev_bi_monthly_end,
							timestamp(monthsend(2,date,-1)) as prev_bi_monthly_end_timestamp
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

- id
- date
- prev\_bi\_monthly\_end
- prev\_bi\_monthly\_end\_timestamp

Results table

| id | date | prev\_bi\_monthly\_end | prev\_bi\_monthly\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8189 | 1/19/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8190 | 2/5/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8191 | 2/28/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8192 | 3/16/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8195 | 5/22/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |

By using -1 as the period\_no argument in the monthsend() function, after initially dividing a year into bi-monthly segments, the function returns the last millisecond of the previous bi-monthly segment to when a transaction takes place.

Diagram of monthsend function that returns the previous bi-monthly segment.

![Diagram of monthsend function with a negative one period_no which returns the previous bi-monthly segment. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-MonthsEnd-example2-diagram.png "Click to view full size")

Transaction 8195 occurs in the segment between May and June. As a result, the previous bi-monthly segment was between March 1 and April 30 and so the function returns the last millisecond of this segment, 04/30/2022 11:59:59 PM.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

The same dataset and scenario as the first example are used.

In this example, the organizational policy is for April to be the first month of the financial year.

Create a field, ‘bi\_monthly\_end’, that groups transactions into bi-monthly segments and returns the last millisecond timestamp of the segment for each transaction.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							monthsend(2,date,0,4) as bi_monthly_end,
							timestamp(monthsend(2,date,0,4)) as bi_monthly_end_timestamp
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

- id
- date
- bi\_monthly\_end
- bi\_monthly\_end\_timestamp

Results table

| id | date | bi\_monthly\_end | bi\_monthly\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 01/31/2022 | 1/31/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 01/31/2022 | 1/31/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8195 | 5/22/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 07/31/2022 | 7/31/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 11/30/2022 | 11/30/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 11/30/2022 | 11/30/2022 11:59:59 PM |

By using 4 as the first\_month\_of\_year argument in the monthsend() function, the function begins the year on April 1. It then divides the year into bi-monthly segments: Apr-May, Jun-Jul, Aug-Sep, Oct-Nov, Dec-Jan, Feb-Mar.

Diagram of monthsend function with the first month of the year set as April

![Diagram of monthsend function with bi-monthly segments and April set as the first month of the year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-MonthsEnd-example3-diagram.png "Click to view full size")

Transaction 8195 took place on May 22 and falls into the segment between April 1 and May 31. As a result, the function returns the last millisecond of this segment, 05/31/2022 11:59:59 PM.

## Example 4 - Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used. However in this example, the dataset is unchanged, and loaded into the application.

In this example, the task is to create a calculation that groups transactions into bi-monthly segments and returns the last millisecond timestamp of the segment for each transaction as a [measure](#glossary-5 "Glossary term") in a chart object of an application.

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

Load the data and open a sheet. Create a new table and add this field as a dimension:

date

To fetch the last millisecond timestamp of the bi-monthly segment when the transaction took place, create the following measures:

- =monthsEnd(2,date)
- =timestamp(monthsend(2,date))

Results table

| id | date | =monthsend(2,date) | =timestamp(monthsend(2,date)) |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 04/30/2022 | 4/30/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8195 | 5/22/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 10/31/2022 | 10/31/2022 11:59:59 PM |

The ‘bi\_monthly\_end’ field is created as a measure in the chart object by using the monthsend() function. The first argument provided is 2, which divides the year into bi-monthly segments. The second argument identifies which field is being evaluated.

Diagram of monthsend function with bi-monthly segments.

![Diagram showing how the monthsend function identifies the selected bi-monthly segment using a chart object. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-MonthsEnd-example4-diagram.png "Click to view full size")

Transaction 8195 takes place on May 22. The monthsend() function initially divides the year into bi-monthly segments. Transaction 8195 falls into the segment between May 1 and June 30. As a result, the function returns the first millisecond of this segment, 06/30/2022 11:59:59 PM.

## Example 5 – Scenario

Load script and results

Overview

Open the data load editor and add the [load script](#glossary-6 "Glossary term") below to a new tab.

In this example, a dataset is loaded into a table called ‘Employee\_Expenses’. The table contains the following fields:

- Employee IDs
- Employee names
- The average daily expense claims of each employee.

The end user would like a chart that displays, by employee id and employee name, the estimated expense claim for the remainder of a period of their own choosing. The financial year begins in January.

Load script

```
SET vPeriod = 1;

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

Load the data and open a new [sheet](#glossary-7 "Glossary term").

At the start of the load script, a variable, vPeriod, is created that is tied to the variable input control.

Do the following:

1. In the assets panel, click Charts.
2. Under Dashboard objects, drag a Variable input onto the sheet.
3. Enter a title for the chart object.
4. Under Variable, select vPeriod as the name and set the object to show as a Drop down.
5. Under Values, click Dynamic values. Enter the following:

   ```
   ='1~month|2~bi-month|3~quarter|4~tertial|6~half-year'.
   ```

Create a new table and these fields as [dimensions](#glossary-8 "Glossary term"):

- employee\_id
- employee\_name

To calculate the accumulated interest, create this measure:

```
=floor(monthsend($(vPeriod),today(1))-today(1))*avg_daily_claim
```

Information noteThis measure is dynamic and will produce different table results depending on the date when you load the data.

Set the measure’s Number formatting to Money.

Results table

| employee\_id | employee\_name | =floor(monthsend($(vPeriod),today(1))-today(1))\*avg\_daily\_claim |
| --- | --- | --- |
| 182 | Mark | $1410.00 |
| 183 | Deryck | $1175.00 |
| 184 | Dexter | $1175.00 |
| 185 | Sydney | $2538.00 |
| 186 | Agatha | $1692.00 |

The monthsend() function uses the user input as its first argument and today’s date as its second argument. This returns the end date for the user selected period of time. Then, the expression returns the number of days that remain the selected period of time by subtracting today’s date from this end date.

This value is then multiplied by the average daily expense claim by each employee to calculate the estimated value of claims each employee is expected to make in the remaining days of this period.
