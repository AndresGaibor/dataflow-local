---
title: "quarterstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# quarterstart Script and chart function

This function returns
a value corresponding to a timestamp of the first millisecond of the
quarter containing date. The
default output format will be the DateFormat set in the script.

Syntax:

QuarterStart(date[, period\_no[, first\_month\_of\_year]])

Return data type:  dual

Diagram of `quarterstart()` function

![Example diagram showing how the quarterstart function converts an input date into a timestamp for the first millisecond of the first month of the quarter in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterstart-general.png)

The `quarterstart()` function determines which quarter the `date` falls into. It then returns a timestamp, in date format, for the first millisecond of the first month of that quarter.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the quarter which contains date. Negative values in period\_no indicate preceding quarters and positive values indicate succeeding quarters. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use quarterstart

The `quarterstart()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of the quarter that has elapsed thus far. For example, it could be used if a user would like to calculate the interest that has been accumulated in a quarter to date.

Function examples

| Example | Result |
| --- | --- |
| `quarterstart('10/29/2005')` | Returns 10/01/2005. |
| `quarterstart('10/29/2005', -1 )` | Returns 07/01/2005. |
| `quarterstart('10/29/2005', 0, 3)` | Returns 09/01/2005. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-0 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-1 "Glossary term") provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `start_of_quarter`, which returns a timestamp for the start of the quarter when the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        quarterstart(date) as start_of_quarter,
        timestamp(quarterstart(date)) as start_of_quarter_timestamp
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
- `start_of_quarter`
- `start_of_quarter_timestamp`

Results table

| date | start\_of\_quarter | start\_of\_quarter\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/5/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/28/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 3/16/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 4/1/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 5/7/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 5/16/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 6/15/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 6/26/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 8/2/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 8/8/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 8/19/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 9/26/2022 | 07/01/2022 | 7/1/2021 12:00:00 AM |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |

The `start_of_quarter` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-3 "Glossary term") statement by using the `quarterstart()` function and passing the date field as the function’s argument.
The q`uarterstart()` function initially identifies which quarter the date value falls into. It then returns a timestamp for the first millisecond of that quarter.

Diagram of `quarterstart()` function, example with no additional arguments

![Diagram showing how the quarterstart function converts the input date for each transaction into a timestamp for the first millisecond of the first month of the quarter in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterstart-examples-no-add-arg.png)

Transaction 8203 took place on August 8. The `quarterstart()` function identifies that the transaction took place in the third quarter, and returns the first millisecond of that quarter, which is July 1 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_quarter_start`, that returns the timestamp for the start of the quarter before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        quarterstart(date,-1) as previous_quarter_start,
        timestamp(quarterstart(date,-1)) as previous_quarter_start_timestamp
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
- `previous_quarter_start`
- `previous_quarter_start_timestamp`

Results table

| date | previous\_quarter\_start | previous\_quarter\_start\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 10/01/2021 | 10/1/2021 12:00:00 AM |
| 1/19/2022 | 10/01/2021 | 10/1/2021 12:00:00 AM |
| 2/5/2022 | 10/01/2021 | 10/1/2021 12:00:00 AM |
| 2/28/2022 | 10/01/2021 | 10/1/2021 12:00:00 AM |
| 3/16/2022 | 10/01/2021 | 10/1/2021 12:00:00 AM |
| 4/1/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 5/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 5/16/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 6/15/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 6/26/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 7/9/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 7/22/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 7/23/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 7/27/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 8/2/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 8/8/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 8/19/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 9/26/2022 | 04/01/2022 | 4/1/2021 12:00:00 AM |
| 10/14/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 10/29/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |

In this instance, because a `period_no` of -1 was used as the offset argument in the `quarterstart()` function, the function first identifies the quarter that the transactions take place in. It then shifts one quarter prior and identifies the first millisecond of that quarter.

Diagram of `quarterstart()` function, period\_no example

![Diagram showing how the quarterstart function converts the input date for each transaction into a timestamp for the first millisecond of the first month of the quarter in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterstart-examples-period-no.png)

Transaction 8203 took place on August 8. The `quarterstart()` function identifies that the quarter before the transaction took place was between April 1 and June 30. It then returns the first millisecond of that quarter, April 1 at 12:00:00 AM.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, we need to set March 1 as the beginning of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        quarterstart(date,0,3) as start_of_quarter,
        timestamp(quarterstart(date,0,3)) as start_of_quarter_timestamp
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
- `start_of_quarter`
- `start_of_quarter_timestamp`

Results table

| date | start\_of\_quarter | start\_of\_quarter\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 1/19/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 2/5/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 2/28/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 3/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/1/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/7/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 6/15/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 6/26/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/9/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/22/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/23/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/27/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 8/2/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 8/8/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 8/19/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 9/26/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/14/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/29/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |

In this instance, because the `first_month_of_year` argument of 3 is used in the `quarterstart()` function, the start of the year moves from January 1 to March 1.

Diagram of `quarterstart()` function, first\_month\_of\_year example

![Diagram showing how the quarterstart function converts the input date for each transaction into a timestamp for the first millisecond of the first month of the quarter in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterstart-examples-first-mth-yr.png)

Transaction 8203 took place on August 8. Because the beginning of the year is March 1, the quarters in the year occur between March-May, June-August, September-November and December-February. The `quarterstart()` function identifies that the transaction took place in the quarter between the start of June and of August and returns the first millisecond of that quarter, which is June 1 at 12:00:00 AM.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the end of the quarter when the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
Transactions:
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

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Add the following measures:

- `=quarterstart(date)`
- `=timestamp(quarterstart(date))`

Results table

| date | =quarterstart(date) | =timestamp(quarterstart(date)) |
| --- | --- | --- |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/2/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/8/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/19/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 9/26/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 4/1/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/7/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/16/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 6/15/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 6/26/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/5/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/28/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 3/16/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |

The `start_of_quarter` measure is created in the chart object by using the `quarterstart()` function and passing the `date` field as the function’s argument.

The `quarterstart()` function identifies the quarter into which the date value falls, returning a timestamp for the first millisecond of that quarter.

Diagram of `quarterstart()` function, chart object example

![Diagram showing how the quarterstart function converts the input date for each transaction into a timestamp for the first millisecond of the first month of the quarter in which this date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterstart-examples-chart-object.png)

Transaction 8203 took place on August 8. The `quarterstart()` function identifies that the transaction took place in the third quarter, and returns the first millisecond of that quarter. This returned value is July 1 at 12:00:00 AM.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of loan balances, which is loaded into a table called `Loans`.
- Data consisting of loan IDs, the balance at the beginning of the quarter, and the simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan ID, the current interest that has been accrued on each loan in the quarter to date.

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

Do the following:

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - `loan_id`
   - `start_balance`
2. Next, create this measure to calculate the accumulated interest:

   `=start_balance*(rate*(today(1)-quarterstart(today(1)))/365)`
3. Set the measure's **Number formatting** to **Money**.

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)-quarterstart(today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $15.07 |
| 8189 | $15000.00 | $128.84 |
| 8190 | $17500.00 | $63.29 |
| 8191 | $21000.00 | $107.59 |
| 8192 | $90000.00 | $1139.18 |

The `quarterstart()` function, using today’s date as its only argument, returns the start date of the current year. By subtracting that result from the current date, the expression returns the number of days that have elapsed so far this quarter.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate incurred for this period. The result is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this quarter.
