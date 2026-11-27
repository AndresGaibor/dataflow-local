---
title: "quarterend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# quarterend Script and chart function

Expand/Collapse all

# quarterend Script and chart function

This function returns
a value corresponding to a timestamp of the last millisecond of the
quarter containing date. The
default output format will be the DateFormat set in the script.

Syntax:

QuarterEnd(date[, period\_no[, first\_month\_of\_year]])

Return data type:  dual

Diagram of the quarterend() function

![Diagram that shows how the quarterend() function identifies the quarter that a date falls into and that it returns the last day of that quarter.  ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterend-diagram1.png "Click to view full size")

The quarterend() function determines which quarter the date falls into. It then returns a timestamp, in date format, for the last millisecond of the last month of that quarter. The first month of the year is, by default, January. However, you can change which month is set as first by using the first\_month\_of\_year argument in the quarterend() function.

Information noteThe quarterend() function does not consider the FirstMonthOfYear system [variable](#glossary-0 "Glossary term"). The year begins on January 1 unless the first\_month\_of\_year argument is used to change it.

When to use quarterend

The quarterend() function is commonly used as part of an expression when you would like the calculation to use the fraction of the quarter that has not yet occurred. For example, if you want to calculate the total interest not yet incurred during the quarter.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the quarter which contains date. Negative values in period\_no indicate preceding quarters and positive values indicate succeeding quarters. |
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
| quarterend('10/29/2005') | Returns 12/31/2005 23:59:59. |
| quarterend('10/29/2005', -1) | Returns 09/30/2005 23:59:59. |
| quarterend('10/29/2005', 0, 3) | Returns 11/30/2005 23:59:59. |

## Example 1 - Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A [preceding load](#glossary-2 "Glossary term") which contains the following:

  - The quarterend() function that is set as the ‘end\_of\_quarter’ [field](#glossary-3 "Glossary term") and returns a timestamp for the end of the quarter when the transactions took place.
  - The timestamp() function that is set as the ‘end\_of\_quarter\_timestamp’ field and returns the exact timestamp of the end of the selected quarter.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       quarterend(date) as end_of_quarter,
       timestamp(quarterend(date)) as end_of_quarter_timestamp
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

- id
- date
- end\_of\_quarter
- end\_of\_quarter\_timestamp

Results table

| id | date | end\_of\_quarter | end\_of\_quarter\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8195 | 5/16/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |

The ‘end\_of\_quarter’ field is created in the preceding load statement by using the quarterend() function and passing the date field as the function’s argument.

The quarterend() function initially identifies which quarter the date value falls into and then returns a timestamp for the last millisecond of that quarter.

Diagram of the quarterend() function with the quarter end of transaction 8203 identified

![Diagram that shows the end of the quarter that the quarterend() function identifies by the transaction date of transaction 8203. The end of the quarter is returned as September 30. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterend-examples1_and3-diagram.png "Click to view full size")

Transaction 8203 took place on August 8. The quarterend() function identifies that the transaction took place in the third quarter, and returns the last millisecond of that quarter, which is September 30 at 11:59:59 PM.

## Example 2 - period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A preceding load which contains the following:

  - The quarterend() function that is set as the ‘previous\_quarter\_end’ field and returns a timestamp for the end of the quarter before the transaction took place.
  - The timestamp() function that is set as the ‘previous\_end\_of\_quarter\_timestamp’ field and returns the exact timestamp of the end of the quarter before the transaction took place.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       quarterend(date, -1) as previous_quarter_end,
       timestamp(quarterend(date, -1)) as previous_quarter_end_timestamp
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

- id
- date
- previous\_quarter\_end
- previous\_quarter\_end\_timestamp

Results table

| id | date | previous\_quarter\_end | previous\_quarter\_end\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8189 | 1/19/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8190 | 2/5/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8191 | 2/28/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8192 | 3/16/2022 | 12/31/2021 | 12/31/2021 11:59:59 PM |
| 8193 | 4/1/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8195 | 5/16/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |

Because a period\_no of -1 is used as the offset argument in the quarterend() function, the function first identifies the quarter that the transactions take place in. It then shifts one quarter prior and identifies the final millisecond of that quarter.

Diagram of the quarterend() function with a period\_no of -1

![Diagram that shows the end of the quarter that the quarterend() function identifies by the transaction date of transaction 8203. The end of the quarter is returned as June 30 because a period_no of -1 is used. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterend-example2-diagram.png "Click to view full size")

Transaction 8203 took place on August 8. The quarterend() function identifies that the quarter before the transaction took place was between April 1 and June 30. The function then returns the final millisecond of that quarter, June 30 at 11:59:59 PM.

## Example 3 - first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A preceding load which contains the following:

  - The quarterend() function that is set as the ‘end\_of\_quarter’ field and returns a timestamp for the end of the quarter when the transactions took place.
  - The timestamp() function that is set as the ‘end\_of\_quarter\_timestamp’ field and returns the exact timestamp of the end of the selected quarter.

However, in this example, the company policy is that the financial year begins on March 1.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       quarterend(date, 0, 3) as end_of_quarter,
       timestamp(quarterend(date, 0, 3)) as end_of_quarter_timestamp
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

Results table

| id | date | end\_of\_quarter | end\_of\_quarter\_timestamp |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 02/28/2022 | 2/28/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8195 | 5/16/2022 | 05/31/2022 | 5/31/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 08/31/2022 | 8/31/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 11/30/2022 | 11/30/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 11/30/2022 | 11/30/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 11/30/2022 | 11/30/2022 11:59:59 PM |

Because the first\_month\_of\_year argument of 3 is used in the quarterend() function, the start of the year moves from January 1 to March 1.

Diagram of the quarterend() function with March as the first month of the year

![Diagram that shows the end of the quarter that the quarterend() function identifies by the transaction date of transaction 8203. The end of the quarter is returned as September 30 because of the first month of the year is set to March.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterend-example3-diagram.png "Click to view full size")

Transaction 8203 took place on August 8. Because the beginning of the year is March 1, the quarters in the year occur between Mar-May, Jun-Aug, Sep-Nov, and Dec-Feb.

The quarterend() function identifies that the transaction took place in the quarter between the start of June and of August and returns the last millisecond of that quarter, which is August 31 at 11:59:59 PM.

## Example 4 - Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that returns a timestamp for the end of the quarter when the transactions took place is created as a [measure](#glossary-4 "Glossary term") in a chart in the application.

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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date

To calculate the end date of the quarter that a transaction takes place in, create the following measures:

- =quarterend(date)
- =timestamp(quarterend(date))

Results table

| id | date | =quarterend(date) | =timestamp(quarterend(date)) |
| --- | --- | --- | --- |
| 8188 | 1/7/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8189 | 1/19/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8190 | 2/5/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8191 | 2/28/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8192 | 3/16/2022 | 03/31/2022 | 3/31/2022 11:59:59 PM |
| 8193 | 4/1/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8194 | 5/7/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8195 | 5/16/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8196 | 6/15/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8197 | 6/26/2022 | 06/30/2022 | 6/30/2022 11:59:59 PM |
| 8198 | 7/9/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8199 | 7/22/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8200 | 7/23/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8201 | 7/27/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8202 | 8/2/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8203 | 8/8/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8204 | 8/19/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8205 | 9/26/2022 | 09/30/2022 | 9/30/2022 11:59:59 PM |
| 8206 | 10/14/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |
| 8207 | 10/29/2022 | 12/31/2022 | 12/31/2022 11:59:59 PM |

The ‘end\_of\_quarter’ field is created in the preceding load statement by using the quarterend() function and passing the date field as the function’s argument.

The quarterend() function initially identifies which quarter the date value falls into and then returns a timestamp for the last millisecond of that quarter.

Diagram of the quarterend() function with the quarter end of transaction 8203 identified

![Diagram that shows the end of the quarter that the quarterend() function identifies by the transaction date of transaction 8203. The end of the quarter is returned as September 30. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quarterend-examples1_and3-diagram.png "Click to view full size")

Transaction 8203 took place on August 8. The quarterend() function identifies that the transaction took place in the third quarter, and returns the last millisecond of that quarter, which is September 30 at 11:59:59 PM.

## Example 5 - Scenario

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset is loaded into a table called ‘Employee\_Expenses’. The table contains the following fields:

  - Employee IDs
  - Employee names
  - The average daily expense claims of each employee.

The end user would like a chart object that displays, by employee id and employee name, the estimated expense claims still to be incurred for the remainder of the quarter. The financial year begins in January.

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

To calculate the accumulated interest, create the following measure:

- =(quarterend(today(1))-today(1))\*avg\_daily\_claim

Set the measure’s Number Formatting to Money.

Results table

| employee\_id | employee\_name | =(quarterend(today(1))-today(1))\*avg\_daily\_claim |
| --- | --- | --- |
| 182 | Mark | $480.00 |
| 183 | Deryck | $400.00 |
| 184 | Dexter | $400.00 |
| 185 | Sydney | $864.00 |
| 186 | Agatha | $576.00 |

The quarterend() function uses today’s date as its only argument and returns the end date of the current month. Then, it subtracts today’s date from the year end date, and the expression returns the number of days that remain this month.

This value is then multiplied by the average daily expense claim of each employee to calculate the estimated value of claims each employee is expected to make in the remaining quarter.
