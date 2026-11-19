---
title: "quarter Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# quarter Script and chart function

The quarter function returns an integer representing the quarter of the provided date. The returned value is between 1 and 4. The function can be used in both load scripts and chart expressions.

Syntax:

quarter(date [, first\_month\_of\_year])

**Return data type:** integer

quarter function arguments

| Argument | Description |
| --- | --- |
| date | The date to evaluate. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year.  If not specified, the default value is 1. |

## When to use it

The quarter function is useful when you would like to compare aggregations by quarter. For example, the function could be used if you would like to see the total sales of products by quarter. It can be used to create new fields in the load script, as well as in calculated dimensions and set expressions.

Function examples

| Example | Result |
| --- | --- |
| `quarter('10/29/2026')` | Returns 4. |
| `quarter('10/29/2026', 3)` | Returns 3. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example – load script

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarter.htm#glossary-0 "Glossary term") containing a set of transactions for 2025, which is loaded into a table called `Transactions`.
- The date field provided in the `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarter.htm#glossary-1 "Glossary term") (M/D/YYYY) format.
- The creation of two fields:

  - `transaction_quarter` returns the quarter in which the transactions took place.
  - `transaction_quarter_march_yearstart` returns the quarter of the transactions, adjusted to set March 1 as the beginning of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*,
quarter(date) as transaction_quarter,
quarter(date,3) as transaction_quarter_march_yearstart
;
Load
*
Inline
[
id,date,amount
8188,1/7/2025,17.17
8189,1/19/2025,37.23
8190,2/28/2025,88.27
8191,2/5/2025,57.42
8192,3/16/2025,53.80
8193,4/1/2025,82.06
8194,5/7/2025,40.39
8195,5/16/2025,87.21
8196,6/15/2025,95.93
8197,6/26/2025,45.89
8198,7/9/2025,36.23
8199,7/22/2025,25.66
8200,7/23/2025,82.77
8201,7/27/2025,69.98
8202,8/2/2025,76.11
8203,8/8/2025,25.12
8204,8/19/2025,46.23
8205,9/26/2025,84.21
8206,10/14/2025,96.24
8207,10/29/2025,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `transaction_quarter`
- `transaction_quarter_march_yearstart`

Results table

| date | transaction\_quarter | transaction\_quarter\_march\_yearstart |
| --- | --- | --- |
| 1/7/2025 | 1 | 4 |
| 1/19/2025 | 1 | 4 |
| 2/28/2025 | 1 | 4 |
| 2/5/2025 | 1 | 4 |
| 3/16/2025 | 1 | 1 |
| 4/1/2025 | 2 | 1 |
| 5/7/2025 | 2 | 1 |
| 5/16/2025 | 2 | 1 |
| 6/15/2025 | 2 | 2 |
| 6/26/2025 | 2 | 2 |
| 7/9/2025 | 3 | 2 |
| 7/22/2025 | 3 | 2 |
| 7/23/2025 | 3 | 2 |
| 7/27/2025 | 3 | 2 |
| 8/2/2025 | 3 | 2 |
| 8/8/2025 | 3 | 2 |
| 8/19/2025 | 3 | 2 |
| 9/26/2025 | 3 | 3 |
| 10/14/2025 | 4 | 3 |
| 10/29/2025 | 4 | 3 |

## Example 2 – chart expressions

Chart expressions

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculations of the transaction quarters are created as [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarter.htm#glossary-2 "Glossary term") in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,1/7/2025,17.17
8189,1/19/2025,37.23
8190,2/28/2025,88.27
8191,2/5/2025,57.42
8192,3/16/2025,53.80
8193,4/1/2025,82.06
8194,5/7/2025,40.39
8195,5/16/2025,87.21
8196,6/15/2025,95.93
8197,6/26/2025,45.89
8198,7/9/2025,36.23
8199,7/22/2025,25.66
8200,7/23/2025,82.77
8201,7/27/2025,69.98
8202,8/2/2025,76.11
8203,8/8/2025,25.12
8204,8/19/2025,46.23
8205,9/26/2025,84.21
8206,10/14/2025,96.24
8207,10/29/2025,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- date

Create the following measures:

- ```
  =quarter(date)
  ```

  This measure returns the quarter in which the transactions took place.
- ```
  =quarter(date,3)
  ```

  This measure returns the quarter of the transactions, adjusted to set March 1 as the beginning of the financial year.

The measures are created in the chart object by using the `quarter()` function and passing the `date` field as arguments.

Results table

| date | =quarter(date) | =quarter(date,3) |
| --- | --- | --- |
| 1/7/2025 | 1 | 4 |
| 1/19/2025 | 1 | 4 |
| 2/28/2025 | 1 | 4 |
| 2/5/2025 | 1 | 4 |
| 3/16/2025 | 1 | 1 |
| 4/1/2025 | 2 | 1 |
| 5/7/2025 | 2 | 1 |
| 5/16/2025 | 2 | 1 |
| 6/15/2025 | 2 | 2 |
| 6/26/2025 | 2 | 2 |
| 7/9/2025 | 3 | 2 |
| 7/22/2025 | 3 | 2 |
| 7/23/2025 | 3 | 2 |
| 7/27/2025 | 3 | 2 |
| 8/2/2025 | 3 | 2 |
| 8/8/2025 | 3 | 2 |
| 8/19/2025 | 3 | 2 |
| 9/26/2025 | 3 | 3 |
| 10/14/2025 | 4 | 3 |
| 10/29/2025 | 4 | 3 |
