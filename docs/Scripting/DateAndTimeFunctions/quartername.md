---
title: "quartername Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "sheet"]
---
Expand/Collapse all

# quartername Script and chart function

This function returns
a display value showing the months of the quarter (formatted according
to the MonthNames script variable) and year with an underlying numeric
value corresponding to a timestamp of the first millisecond of the first
day of the quarter.

Syntax:

QuarterName(date[, period\_no[, first\_month\_of\_year]])

Return data type:  dual

Diagram of `quartername()` function

![Example diagram showing how the quartername function converts an input date into a range of months contained in the quarter in which date occurs.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quartername-general.png)

The `quartername()` function determines which quarter the date falls into. It then returns a value showing the start-end months of this quarter as well as the year. The underlying numeric value of this result is the first millisecond of the quarter.

Arguments

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the quarter which contains date. Negative values in period\_no indicate preceding quarters and positive values indicate succeeding quarters. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use quartername

The `quartername()` function is useful when you would like to compare aggregations by quarter. For example, if you would like to see the total sales of products by quarter.

This function could be used in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-0 "Glossary term") to create a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-1 "Glossary term") in a Master Calendar table. Alternatively, it could be used directly in a [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-2 "Glossary term") as a calculated [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-3 "Glossary term").

These examples use the date format MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement at the top of your data load script. Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| `quartername('10/29/2013')` | Returns Oct-Dec 2013. |
| `quartername('10/29/2013', -1)` | Returns Jul-Sep 2013. |
| `quartername('10/29/2013', 0, 3)` | Returns Sep-Nov 2013. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – date with no additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-4 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-5 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, `transaction_quarter`, which returns the quarter in which the transactions took place.

Add your other text here, as needed, with lists etc.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';

Transactions:
    Load
        *,
        quartername(date) as transaction_quarter
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
- `transaction_quarter`

Results table

| date | transaction\_quarter |
| --- | --- |
| 1/7/2022 | Jan-Mar 2022 |
| 1/19/2022 | Jan-Mar 2022 |
| 2/5/2022 | Jan-Mar 2022 |
| 2/28/2022 | Jan-Mar 2022 |
| 3/16/2022 | Jan-Mar 2022 |
| 4/1/2022 | Apr-Jun 2022 |
| 5/7/2022 | Apr-Jun 2022 |
| 5/16/2022 | Apr-Jun 2022 |
| 6/15/2022 | Apr-Jun 2022 |
| 6/26/2022 | Apr-Jun 2022 |
| 7/9/2022 | Jul-Sep 2022 |
| 7/22/2022 | Jul-Sep 2022 |
| 7/23/2022 | Jul-Sep 2022 |
| 7/27/2022 | Jul-Sep 2022 |
| 8/2/2022 | Jul-Sep 2022 |
| 8/8/2022 | Jul-Sep 2022 |
| 8/19/2022 | Jul-Sep 2022 |
| 9/26/2022 | Jul-Sep 2022 |
| 10/14/2022 | Oct-Dec 2022 |
| 10/29/2022 | Oct-Dec 2022 |

The `transaction_quarter` field is created in the [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-6 "Glossary term") statement by using the `quartername()` function and passing the date field as the function’s argument.

The `quartername()` function initially identifies the quarter into which the date value falls. It then returns a value showing the start-end months of this quarter, as well as the year.

Diagram of `quartername()` function, example with no additional arguments

![Diagram showing how the quartername function determines the range of months of the quarter in which a transaction takes place.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quartername-examples-no-add-arg.png)

Transaction 8203 took place on August 8, 2022. The `quartername()` function identifies that the transaction took place in the third quarter, and therefore returns Jul-Sep 2022. The months are displayed in the same format as the `MonthNames` system variable.

## Example 2 – date with period\_no argument

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, `previous_quarter`, that that returns the previous quarter to when the transactions took place.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';

Transactions:
    Load
        *,
        quartername(date,-1) as previous_quarter
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
- `previous_quarter`

Results table

| date | previous\_quarter |
| --- | --- |
| 1/7/2022 | Oct-Dec 2021 |
| 1/19/2022 | Oct-Dec 2021 |
| 2/5/2022 | Oct-Dec 2021 |
| 2/28/2022 | Oct-Dec 2021 |
| 3/16/2022 | Oct-Dec 2021 |
| 4/1/2022 | Jan-Mar 2022 |
| 5/7/2022 | Jan-Mar 2022 |
| 5/16/2022 | Jan-Mar 2022 |
| 6/15/2022 | Jan-Mar 2022 |
| 6/26/2022 | Jan-Mar 2022 |
| 7/9/2022 | Apr-Jun 2022 |
| 7/22/2022 | Apr-Jun 2022 |
| 7/23/2022 | Apr-Jun 2022 |
| 7/27/2022 | Apr-Jun 2022 |
| 8/2/2022 | Apr-Jun 2022 |
| 8/8/2022 | Apr-Jun 2022 |
| 8/19/2022 | Apr-Jun 2022 |
| 9/26/2022 | Apr-Jun 2022 |
| 10/14/2022 | Jul-Sep 2022 |
| 10/29/2022 | Jul-Sep 2022 |

In this instance, because a `period_no` of -1 was used as the offset argument in the `quartername()` function, the function first identifies that the transactions took place in the third quarter. It then shifts one quarter prior and returns a value showing the start-end months of this quarter, as well as the year.

Diagram of `quartername()` function, period\_no example

![Diagram showing how the quartername function determines the range of months of the quarter in which a transaction takes place.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quartername-examples-period-no.png)

Transaction 8203 took place on August 8. The `quartername()` function identifies that the quarter before the transaction took place was between April 1 and June 30. Therefore, it returns Apr-Jun 2022.

## Example 3 – date with first\_week\_day argument

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-7 "Glossary term") and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, we need to set March 1 as the beginning of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';

Transactions:
    Load
        *,
        quartername(date,0,3) as transaction_quarter
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
- `transaction_quarter`

Results table

| date | transaction\_quarter |
| --- | --- |
| 1/7/2022 | Dec-Feb 2021 |
| 1/19/2022 | Dec-Feb 2021 |
| 2/5/2022 | Dec-Feb 2021 |
| 2/28/2022 | Dec-Feb 2021 |
| 3/16/2022 | Mar-May 2022 |
| 4/1/2022 | Mar-May 2022 |
| 5/7/2022 | Mar-May 2022 |
| 5/16/2022 | Mar-May 2022 |
| 6/15/2022 | Jun-Aug 2022 |
| 6/26/2022 | Jun-Aug 2022 |
| 7/9/2022 | Jun-Aug 2022 |
| 7/22/2022 | Jun-Aug 2022 |
| 7/23/2022 | Jun-Aug 2022 |
| 7/27/2022 | Jun-Aug 2022 |
| 8/2/2022 | Jun-Aug 2022 |
| 8/8/2022 | Jun-Aug 2022 |
| 8/19/2022 | Jun-Aug 2022 |
| 9/26/2022 | Sep-Nov 2022 |
| 10/14/2022 | Sep-Nov 2022 |
| 10/29/2022 | Sep-Nov 2022 |

In this instance, because the `first_month_of_year` argument of 3 is used in the `quartername()` function, the start of the year moves from January 1 to March 1. Therefore, the quarters in the year are separated into March-May, June-August, September-November and December-February.

Diagram of `quartername()` function, first\_week\_day example

![Diagram showing how the quartername function determines the range of months of the quarter in which a transaction takes place.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quartername-examples-first-week-day.png)

Transaction 8203 took place on August 8. The `quartername()` function identifies that the transaction took place in the second quarter, between the start of June and the end of August. Therefore, it returns Jun-Aug 2022.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that returns a timestamp for the end of the quarter when the transactions took place is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-8 "Glossary term") in a chart object of the application.

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
8205,9/26/022,84.21
8206,10/14/2022,96.24
8207,10/29/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Create the following measure:

`=quartername(date)`

Results table

| date | =quartername(date) |
| --- | --- |
| 1/7/2022 | Jan-Mar 2022 |
| 1/19/2022 | Jan-Mar 2022 |
| 2/5/2022 | Jan-Mar 2022 |
| 2/28/2022 | Jan-Mar 2022 |
| 3/16/2022 | Jan-Mar 2022 |
| 4/1/2022 | Apr-Jun 2022 |
| 5/7/2022 | Apr-Jun 2022 |
| 5/16/2022 | Apr-Jun 2022 |
| 6/15/2022 | Apr-Jun 2022 |
| 6/26/2022 | Apr-Jun 2022 |
| 7/9/2022 | Jul-Sep 2022 |
| 7/22/2022 | Jul-Sep 2022 |
| 7/23/2022 | Jul-Sep 2022 |
| 7/27/2022 | Jul-Sep 2022 |
| 8/2/2022 | Jul-Sep 2022 |
| 8/8/2022 | Jul-Sep 2022 |
| 8/19/2022 | Jul-Sep 2022 |
| 9/26/2022 | Jul-Sep 2022 |
| 10/14/2022 | Oct-Dec 2022 |
| 10/29/2022 | Oct-Dec 2022 |

The `transaction_quarter` measure is created in the chart object by using the `quartername()` function and passing the `date` field as the function’s argument.

The `quartername()` function initially identifies the quarter into which the date value falls. It then returns a value showing the start-end months of this quarter, as well as the year.

Diagram of `quartername()` function, chart object example

![Diagram showing how the quartername function determines the range of months of the quarter in which a transaction takes place.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-quartername-examples-chart-object.png)

Transaction 8203 took place on August 8, 2022. The `quartername()` function identifies that the transaction took place in the third quarter, and therefore returns Jul-Sep 2022. The months are displayed in the same format as the `MonthNames` system variable.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for 2022, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system variable (MM/DD/YYYY) format.

The end user would like a chart object that presents the total sales by quarter for the transactions. This could be achieved even when this dimension is not available in the data model, using the `quartername()` function as a calculated dimension in the chart.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,'1/7/2022',17.17
8189,'1/19/2022',37.23
8190,'2/28/2022',88.27
8191,'2/5/2022',57.42
8192,'3/16/2022',53.80
8193,'4/1/2022',82.06
8194,'5/7/2022',40.39
8195,'5/16/2022',87.21
8196,'6/15/2022',95.93
8197,'6/26/2022',45.89
8198,'7/9/2022',36.23
8199,'7/22/2022',25.66
8200,'7/23/2022',82.77
8201,'7/27/2022',69.98
8202,'8/2/2022',76.11
8203,'8/8/2022',25.12
8204,'8/19/2022',46.23
8205,'9/26/2022',84.21
8206,'10/14/2022',96.24
8207,'10/29/2022',67.67
];
```

Results

Do the following:

1. Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-9 "Glossary term"). Create a new table.
2. Create a calculated dimension using the following expression:

   `=quartername(date)`
3. Next, calculate total sales using the following [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm#glossary-10 "Glossary term") measure:

   `=sum(amount)`
4. Set the measure's **Number formatting** to **Money**.

Results table

| =quartername(date) | =sum(amount) |
| --- | --- |
| Jul-Sep 2022 | $446.31 |
| Apr-Jun 2022 | $351.48 |
| Jan-Mar 2022 | $253.89 |
| Oct-Dec 2022 | $163.91 |
