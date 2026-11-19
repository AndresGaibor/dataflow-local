---
title: "inmonth Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# inmonth Script and chart function

This function returns
True if timestamp lies inside the
month containing base\_date.

Syntax:

InMonth (timestamp, base\_date, period\_no)

Diagram of `indaytotime` function.

![Diagram showing the conditions of the inmonth function.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_Diagram_InMonth.png)

In other words, the `inmonth()` function determines if a set of dates fall into this month and returns a Boolean value based on a `base_date` that identifies the month.

When to use inmonth

The `inmonth()` function returns a Boolean result. Typically, this type of function will be used as a condition in an `if expression`. This returns an [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-0 "Glossary term") or calculation depending on whether a date occurred in the month, including the date in question.

For example, the `inmonth()` function can be used to identify all equipment manufactured in a specific month.

Return data type:  Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with `base_date`. |
| base\_date | Date that is used to evaluate the month. It is important to note that the `base_date` can be any day within a month. |
| period\_no | The month can be offset by `period_no`. `period_no` is an integer, where the value 0 indicates the month which contains `base_date`. Negative values in `period_no` indicate preceding months and positive values indicate succeeding months. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `inmonth ('25/01/2013', '01/01/2013', 0)` | Returns True |
| `inmonth('25/01/2013', '23/04/2013', 0)` | Returns False |
| `inmonth ('25/01/2013', '01/01/2013', -1)` | Returns False |
| `inmonth ('25/12/2012', '17/01/2013', -1)` | Returns True |

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-1 "Glossary term") containing a set of transactions for the first half of 2022.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-2 "Glossary term") with an additional [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-3 "Glossary term") ‘`in_month`’, that determines whether transactions took place in April.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Transactions: 
  Load 
    *, 
    inmonth(date,'04/01/2022', 0) as in_month 
    ; 
Load 
* 
Inline  
[ 
id,date,amount 
8188,'1/10/2022',37.23 
8189,'1/14/2022',17.17 
8190,'1/20/2022',88.27 
8191,'1/22/2022',57.42 
8192,'2/1/2022',53.80 
8193,'2/2/2022',82.06 
8194,'2/20/2022',40.39 
8195,'4/11/2022',87.21 
8196,'4/13/2022',95.93 
8197,'4/15/2022',45.89 
8198,'4/25/2022',36.23 
8199,'5/20/2022',25.66 
8200,'5/22/2022',82.77 
8201,'6/19/2022',69.98 
8202,'6/22/2022',76.11 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_month

Function examples

| date | in\_month |
| --- | --- |
| 1/10/2022 | 0 |
| 1/14/2022 | 0 |
| 1/20/2022 | 0 |
| 1/22/2022 | 0 |
| 2/1/2022 | 0 |
| 2/2/2022 | 0 |
| 2/20/2022 | 0 |
| 4/11/2022 | -1 |
| 4/13/2022 | -1 |
| 4/15/2022 | -1 |
| 4/25/2022 | -1 |
| 5/20/2022 | 0 |
| 5/22/2022 | 0 |
| 6/19/2022 | 0 |
| 6/22/2022 | 0 |

The ‘`in_month`’ [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-4 "Glossary term")is created in the preceding load statement by using the `inmonth()` function and passing the date field, a hard-coded date of April 1, as our `base_date` and a `period_no` of `0` as the function’s arguments.

The `base_date` identifies the month that will return a Boolean result of TRUE. Therefore, all transactions that occurred in April return TRUE which is validated in the results table.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario from the first example are used.

However, in this example, you will create a field, ‘`2_months_prior`’, that determines whether the transactions took place two months before April.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
 
Transactions: 
Load 
   *, 
   inmonth(date,'04/01/2022', -2) as [2_months_prior] 
Inline  
[ 
id,date,amount 
8188,'1/10/2022',37.23 
8189,'1/14/2022',17.17 
8190,'1/20/2022',88.27 
8191,'1/22/2022',57.42 
8192,'2/1/2022',53.80 
8193,'2/2/2022',82.06 
8194,'2/20/2022',40.39 
8195,'4/11/2022',87.21 
8196,'4/13/2022',95.93 
8197,'4/15/2022',45.89 
8198,'4/25/2022',36.23 
8199,'5/20/2022',25.66 
8200,'5/22/2022',82.77
8201,'6/19/2022',69.98 
8202,'6/22/2022',76.11 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- 2\_months\_prior

Function examples

| date | 2\_months\_prior |
| --- | --- |
| 1/10/2022 | 0 |
| 1/14/2022 | 0 |
| 1/20/2022 | 0 |
| 1/22/2022 | 0 |
| 2/1/2022 | -1 |
| 2/2/2022 | -1 |
| 2/20/2022 | -1 |
| 4/11/2022 | 0 |
| 4/13/2022 | 0 |
| 4/15/2022 | 0 |
| 4/25/2022 | 0 |
| 5/20/2022 | 0 |
| 5/22/2022 | 0 |
| 6/19/2022 | 0 |
| 6/22/2022 | 0 |

Using -2 as the `period_no` argument in the `inmonth()` function shifts the month defined by the `base_date` argument two months prior. In this example it changes the defined month from April to February.

Therefore, any transaction that takes place in February will return a Boolean result of TRUE.

## Example 3 – Chart object

expression

Overview

The same dataset and scenario from the previous examples are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that determines whether transactions took place in April is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-6 "Glossary term")in a chart object of the application.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Transactions: 
Load 
* 
Inline  
[ 
id,date,amount 
8188,'1/10/2022',37.23 
8189,'1/14/2022',17.17 
8190,'1/20/2022',88.27 
8191,'1/22/2022',57.42 
8192,'2/1/2022',53.80 
8193,'2/2/2022',82.06 
8194,'2/20/2022',40.39 
8195,'4/11/2022',87.21 
8196,'4/13/2022',95.93 
8197,'4/15/2022',45.89 
8198,'4/25/2022',36.23 
8199,'5/20/2022',25.66 
8200,'5/22/2022',82.77 
8201,'6/19/2022',69.98 
8202,'6/22/2022',76.11 
];
```

Chart object

Load the data and open a sheet. Create a new table and add this field as a dimension:

date

To calculate whether a transaction takes place in April, create the following measure:

=inmonth(date,'04/01/2022', 0)

Results

Function examples

| date | =inmonth(date,'04/01/2022', 0) |
| --- | --- |
| 1/10/2022 | 0 |
| 1/14/2022 | 0 |
| 1/20/2022 | 0 |
| 1/22/2022 | 0 |
| 2/1/2022 | 0 |
| 2/2/2022 | 0 |
| 2/20/2022 | 0 |
| 4/11/2022 | -1 |
| 4/13/2022 | -1 |
| 4/15/2022 | -1 |
| 4/25/2022 | -1 |
| 5/20/2022 | 0 |
| 5/22/2022 | 0 |
| 6/19/2022 | 0 |
| 6/22/2022 | 0 |

## Example 4 – Scenario

Load script and results

Overview

In this example, a dataset is loaded into a table called ‘`Products`’. The table contains the following fields:

- Product ID
- Manufacture date
- Cost price

Due to equipment error, products that were manufactured in the month of July 2022 were defective. The issue was resolved on July 27, 2022.

The end user would like a chart that displays, by month, the status of products that were manufactured as ‘defective’ (Boolean TRUE) or ‘faultless’ (Boolean FALSE) and the cost of the products manufactured in that month.

Load script

```
Products: 
Load 
* 
Inline  
[ 
product_id,manufacture_date,cost_price 
8188,'1/19/2022',37.23 
8189,'1/7/2022',17.17 
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

Load the data and open a sheet. Create a new table and add this field as a dimension:

=monthname(manufacture\_date)

Create the following [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm#glossary-7 "Glossary term")

- `=sum(cost_price)`
- `=if(only(inmonth(manufacture_date,makedate(2022,07,01),0)),'Defective','Faultless')`

1. Set the measure’s **Number Formatting** to **Money**.
2. Under **Appearance**, turn off **Totals**.

Results table

| monthname(manufacture\_date) | =if(only(inmonth(manufacture\_date,makedate(2022,07,01),0)),'Defective','Faultless') | sum(cost\_price) |
| --- | --- | --- |
| Jan 2022 | Faultless | $54.40 |
| Feb 2022 | Faultless | $145.69 |
| Mar 2022 | Faultless | $53.80 |
| Apr 2022 | Faultless | $82.06 |
| May 2022 | Faultless | $127.60 |
| Jun 2022 | Faultless | $141.82 |
| Jul 2022 | Defective | $214.64 |
| Aug 2022 | Faultless | $147.46 |
| Sep 2022 | Faultless | $84.21 |
| Oct 2022 | Faultless | $163.91 |

The `inmonth()` function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured in July 2022, the `inmonth()` function returns a Boolean value of True and marks the products as ‘Defective’. For any product returning a value of False, and therefore not manufactured in July, it marks the products as ‘Faultless’.
