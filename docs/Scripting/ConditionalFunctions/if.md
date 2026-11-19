---
title: "if Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---
Expand/Collapse all

# if Script and chart function

The if function returns a value depending on whether the condition provided with the function evaluates as True or False.

[Video: https://share.vidyard.com/watch/qnkaRddq32LnAGUTTDGdLA]

Syntax:

if(condition , then [, else])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| condition | Expression that is interpreted logically. |
| then | Expression that can be of any type. If the condition is True, then the if function returns the value of the then expression. |
| else | Expression that can be of any type. If the condition is False, then the if function returns the value of the else expression. This parameter is optional. If the condition is False, NULL is returned if you have not specified else. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `if( Amount>= 0, 'OK', 'Alarm' )` | This expression tests if the amount is a positive number (0 or larger) and returns `OK` if it is. If the amount is less than 0, `Alarm` is returned. |

Some of the examples in this topic use inline loads. For more information, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

## Example - Load script using if

Load script

Overview

If can be used in a [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm#glossary-0 "Glossary term") with other methods and objects, including [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm#glossary-1 "Glossary term"). This example uses the `threshold` variable and includes a new [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm#glossary-2 "Glossary term") in the data model that is based on the threshold.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into two data tables called:

  - `Transactions`: Includes transaction fields
  - `Transaction_Buckets`: Includes a `transaction_id` field and creates a new field, `[Compared to Threshold]`, using the `if` function to compare the `transaction_amount` field to the `threshold` variable setting.
- A `threshold` variable statement set to `100`.

Load script

```
Transactions:
Load * Inline [
transaction_id, transaction_date, transaction_amount, transaction_quantity, customer_id, size, color_code
3750, 20180830, 23.56, 2, 2038593, L, Red
3751, 20180907, 556.31, 6, 203521, m, orange
3752, 20180916, 5.75, 1, 5646471, S, blue
3753, 20180922, 125.00, 7, 3036491, l, Black
3754, 20180922, 484.21, 13, 049681, xs, Red
3756, 20180922, 59.18, 2, 2038593, M, Blue
3757, 20180923, 177.42, 21, 203521, XL, Black
];
 
set threshold = 100;
					
/* Create new table called Transaction_Buckets 
Compare transaction_amount field from Transaction table to threshold of 100.
Output results into a new field called Compared to Threshold
 */

Transaction_Buckets:
Load
   transaction_id,
   If(transaction_amount > $(threshold),'Greater than $(threshold)','Less than $(threshold)') as [Compared to Threshold]
Resident Transactions;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `transaction_id`
- `[Compared to Threshold]`

Results table showing the output from using the if function in the load script.

| transaction\_id | Compared to Threshold |
| --- | --- |
| 3750 | Less than 100 |
| 3751 | Greater than 100 |
| 3752 | Less than 100 |
| 3753 | Greater than 100 |
| 3754 | Greater than 100 |
| 3756 | Less than 100 |
| 3757 | Greater than 100 |

## Example - Evaluate product data using if

Chart expression

Overview

A data set contains product data. You want to identify and categorize products according to whether they are consumable or not.

Load script

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductID`
  - `ProductName`
  - `ProductCategory`

```
Example:
LOAD * INLINE [
ProductID, ProductName, ProductCategory
1, "Laptop", "Electronics"
2, "Banana", "Fruits"
3, "Shampoo", "Toiletries"
4, "TV", "Electronics"
5, "Apple", "Fruits"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ProductID`
- `ProductName`
- `ProductCategory`

Create the following measure:

- `=If(ProductCategory = 'Toiletries' or ProductCategory = 'Fruits', 'Consumable', 'Other')`, to return the values required.

Results table

| ProductID | ProductName | ProductCategory | If(ProductCategory = 'Toiletries' or ProductCategory = 'Fruits', 'Consumable', 'Other') |
| --- | --- | --- | --- |
| 1 | Laptop | Electronics | Other |
| 2 | Banana | Fruits | Consumable |
| 3 | Shampoo | Toiletries | Consumable |
| 4 | TV | Electronics | Other |
| 5 | Apple | Fruits | Consumable |

You can see from the results that the `if` function evaluates the expression and returns the values required. For example, products in the category `Fruits` or `Toiletries` are classified as `Consumable`.

## Example - Evaluate and classify client data using if

Chart expression

Overview

A data set contains client data. You want to identify and categorize the clients whose region and industry category meet your classification requirements.

Load script

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ClientID`
  - `ClientName`
  - `Region`
  - `Industry`

```
Example:
LOAD * INLINE [
ClientID, ClientName, Region, Industry
1, "Acme Corp", "North", "Manufacturing"
2, "Beta Ltd", "East", "Technology"
3, "Gamma Inc", "West", "Retail"
4, "Delta LLC", "North", "Technology"
5, "Epsilon GmbH", "South", "Healthcare"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ClientID`
- `ClientName`
- `Region`
- `Industry`

Create the following measure:

- `=If((Region = 'North' or Region = 'East') AND (Industry= 'Technology' or Industry = 'Manufacturing'), 'Target Segment', 'Secondary Segment')`, to return the value required.

Results table

| ClientID | ClientName | Region | Industry | If((Region = 'North' or Region = 'East') AND (Industry= 'Technology' or Industry = 'Manufacturing'), 'Target Segment', 'Secondary Segment') |
| --- | --- | --- | --- | --- |
| 1 | Acme Corp | North | Manufacturing | Target Segment |
| 2 | Beta Ltd | East | Technology | Target Segment |
| 3 | Gamma Inc | West | Retail | Secondary Segment |
| 4 | Delta LLC | North | Technology | Target Segment |
| 5 | Epsilon GmbH | Sound | Healthcare | Secondary Segment |

You can see from the results that the `if` function evaluates the expression and returns the values required. For example, `Acme Corp` is classified as a `Target Segment` because it meets the requirements to be part of the `North` or `East` region and the `Manufacturing` or `Technology` industry.

## Example - Evaluate incident data using if

Chart expression

Overview

Use the `if` function to categorize a dataset of incident reports.

Load script

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Date`
  - `Location`
  - `Incidents`

```
Example:
LOAD * inline [
Date, Location, Incidents
1/3/2016, Beijing, 0
1/3/2016, Boston, 12
1/3/2016, Stockholm, 3
1/3/2016, Toronto, 0
1/4/2016, Beijing, 0
1/4/2016, Boston, 8];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Date
- Location
- Incidents

Create the following calculated dimensions:

- `=if(Incidents>=10, 'Critical', 'Ok' )`
- `=if(Incidents>=10, 'Critical', If( Incidents>=1 and
  Incidents<10, 'Warning', 'Ok'))`

Results table

| Date | Location | Incidents | if(Incidents>=10, 'Critical', 'Ok' ) | if(Incidents>=10, 'Critical', If( Incidents>=1 and Incidents<10, 'Warning', 'Ok')) |
| --- | --- | --- | --- | --- |
| 1/3/2016 | Beijing | 0 | Ok | Ok |
| 1/3/2016 | Boston | 12 | Critical | Critical |
| 1/3/2016 | Stockholm | 3 | Ok | Warning |
| 1/3/2016 | Toronto | 0 | Ok | Ok |
| 1/4/2016 | Beijing | 0 | Ok | Ok |
| 1/4/2016 | Boston | 8 | Ok | Warning |

## Example - Categorize dates using if

Chart expression

Overview

Use the `if` function to categorize dates.

Load script

Open the Data load editor and add the load script below to a new section.

```
SET FirstWeekDay=0;
Load 
Date(MakeDate(2022)+RecNo()-1) as Date
Autogenerate 14;
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `Date`

Create the following calculated dimensions:

- `WeekDay(Date)`
- `=If(WeekDay(Date)>=5,'WeekEnd','Normal Day')`

Results table

| Date | WeekDay(Date) | If(WeekDay(Date)>=5,'WeekEnd','Normal Day') |
| --- | --- | --- |
| 1/1/2022 | Sat | WeekEnd |
| 1/2/2022 | Sun | WeekEnd |
| 1/3/2022 | Mon | Normal Day |
| 1/4/2022 | Tue | Normal Day |
| 1/5/2022 | Wed | Normal Day |
| 1/6/2022 | Thu | Normal Day |
| 1/7/2022 | Fri | Normal Day |
| 1/8/2022 | Sat | WeekEnd |
| 1/9/2022 | Sun | WeekEnd |
| 1/10/2022 | Mon | Normal Day |
| 1/11/2022 | Tue | Normal Day |
| 1/12/2022 | Wed | Normal Day |
| 1/13/2022 | Thu | Normal Day |
| 1/14/2022 | Fri | Normal Day |
