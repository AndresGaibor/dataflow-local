---
title: "monthstart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# monthstart Script and chart function

This function returns
a value corresponding to a timestamp of the first millisecond of the
first day of the month containing date. The default output format will be the DateFormat set in the script.

Syntax:

MonthStart(date[, period\_no])

Return data type:  dual

Diagram of `monthstart()` function

![Example diagram of how the elements of the function work together to return the result. The monthstart takes an input date and converts it to a timestamp of the first millisecond of the month in which the date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthstart-general.png)

The `monthstart()` function determines which month the date falls into. It then returns a timestamp, in date format, for the first millisecond of that month.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, which, if 0 or omitted, indicates the month that contains date. Negative values in period\_no indicate preceding months and positive values indicate succeeding months. |

## When to use monthstart

The `monthstart()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of the month that has elapsed thus far. For example, it can be used to calculate the interest that has been accumulated in a month up to a certain date.

Function examples

| Example | Result |
| --- | --- |
| `monthstart('10/19/2001')` | Returns 10/01/2001. |
| `monthstart('10/19/2001', -1)` | Returns 09/01/2001. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-0 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-1 "Glossary term") provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-2 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `start_of_month`, which returns a timestamp for the start of the month when the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthstart(date) as start_of_month,
        timestamp(monthstart(date)) as start_of_month_timestamp
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
- `start_of_month`
- `start_of_month_timestamp`

Results table

| date | start\_of\_month | start\_of\_month\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/5/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 2/28/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 3/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 4/1/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/16/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/15/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 6/26/2022 | 07/01/2022 | 6/1/2022 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/2/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/8/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/19/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 9/26/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |

The `start_of_month` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-3 "Glossary term") statement by using the `monthstart()` function and passing the date field as the function’s argument.

The `monthstart()` function identifies which month the date value falls into, returning a timestamp for the first millisecond of that month.

Diagram of `monthstart()` function, example with no additional arguments

![Diagram showing the results of using the monthstart function to determine the month in which a transaction took place. In this case, it determines that transaction number 8192, which took place on March 16, will return 12:00:00 AM on March 1, 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthstart-example-no-add-arg.png)

Transaction 8192 took place on March 16. The `monthstart()` function returns the first millisecond of that month, which is March 1 at 12:00:00 AM.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_month_start`, which returns the timestamp for the start of the month before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        monthstart(date,-1) as previous_month_start,
        timestamp(monthstart(date,-1)) as previous_month_start_timestamp
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
- `previous_month_start`
- `previous_month_start_timestamp`

Results table

| date | previous\_month\_start | previous\_month\_start\_timestamp |
| --- | --- | --- |
| 1/7/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 1/19/2022 | 12/01/2021 | 12/1/2021 12:00:00 AM |
| 2/5/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 2/28/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 3/16/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 4/1/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 5/7/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 5/16/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 6/15/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 6/26/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 7/9/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/22/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/23/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 7/27/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 8/2/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/8/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 8/19/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 9/26/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 10/14/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 10/29/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |

In this instance, because a `period_no` of -1 was used as the offset argument in the `monthstart()` function, the function first identifies the month that the transactions take place in. It then shifts one month prior and identifies the first millisecond of that month.

Diagram of `monthstart()` function, period\_no example

![Diagram showing the results of using the monthstart function to determine the month in which a transaction took place. In this case demonstrating period_no, it determines that transaction number 8192, which took place on March 16, will return 12:00:00 AM on February 1, 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthstart-example-period-no.png)

Transaction 8192 took place on March 16. The `monthstart()` function identifies that the month before the transaction took place in was February. It then returns the first millisecond of that month, February 1 at 12:00:00 AM.

## Example 3 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-4 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the start of the month when the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';
 
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

To calculate the start date of the month that a transaction takes place in, create the following measures:

- `=monthstart(date)`
- `=timestamp(monthstart(date))`

Results table

| date | =monthstart(date) | =timestamp(monthstart(date)) |
| --- | --- | --- |
| 10/14/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 10/29/2022 | 10/01/2022 | 10/1/2022 12:00:00 AM |
| 9/26/2022 | 09/01/2022 | 9/1/2022 12:00:00 AM |
| 8/2/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/8/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 8/19/2022 | 08/01/2022 | 8/1/2022 12:00:00 AM |
| 7/9/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/22/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/23/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 7/27/2022 | 07/01/2022 | 7/1/2022 12:00:00 AM |
| 6/15/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 6/26/2022 | 06/01/2022 | 6/1/2022 12:00:00 AM |
| 5/7/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 5/16/2022 | 05/01/2022 | 5/1/2022 12:00:00 AM |
| 4/1/2022 | 04/01/2022 | 4/1/2022 12:00:00 AM |
| 3/16/2022 | 03/01/2022 | 3/1/2022 12:00:00 AM |
| 2/5/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 2/28/2022 | 02/01/2022 | 2/1/2022 12:00:00 AM |
| 1/7/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |
| 1/19/2022 | 01/01/2022 | 1/1/2022 12:00:00 AM |

The `start_of_month` measure is created in the chart object by using the `monthstart()` function and passing the date field as the function’s argument.

The `monthstart()` function identifies which month the date value falls into returning a timestamp for the first millisecond of that month.

Diagram of `monthstart()` function, chart object example

![Diagram showing the results of using the monthstart function to determine the month in which a transaction took place. This example uses a chart object to do this. In this case, it determines that transaction number 8192, which took place on March 16, will return 12:00:00 AM on March 1, 2022.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-monthstart-example-chart-object.png)

Transaction 8192 took place on March 16. The `monthstart()` function identifies that the transaction took place in March and returns the first millisecond of that month, which is March 1 at 12:00:00 AM.

## Example 4 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of loan balances, which is loaded into a table called `Loans`.
- Data consisting of loan IDs, the balance at the start of the month, and the simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan ID, the current interest that has been accrued on each loan in the month to date.

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

Do the following:

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - `loan_id`
   - `start_balance`
2. Next, create a measure to calculate the accumulated interest:

   `=start_balance*(rate*(today(1)-monthstart(today(1)))/365)`
3. Set the measure's **Number formatting** to **Money**.

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)-monthstart(today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $16.44 |
| 8189 | $15000.00 | $58.56 |
| 8190 | $17500.00 | $28.77 |
| 8191 | $21000.00 | $48.90 |
| 8192 | $90000.00 | $517.81 |

The `monthstart()` function, using today’s date as its only argument, returns the start date of the current month. By subtracting that result from the current date, the expression returns the number of days that have elapsed so far this month.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate incurred for this period. The result is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this month.
