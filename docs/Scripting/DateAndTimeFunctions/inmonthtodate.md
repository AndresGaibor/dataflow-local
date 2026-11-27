---
title: "inmonthtodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonthtodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inmonthtodate Script and chart function

Expand/Collapse all

# inmonthtodate Script and chart function

Returns
True if date lies inside the
part of month containing basedate
up until and including the last millisecond of basedate.

Syntax:

InMonthToDate
(timestamp, base\_date, period\_no)

Return data type:  Boolean

Diagram of inmonthtodate function.

![Diagram showing how inmonthtodate function can be used to identify if a timstamp falls within or outside of a set month.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthtodate-diagram1.png "Click to view full size")

The inmonthtodate() function identifies a selected month as a segment. The start boundary is the beginning of the month. The end boundary can be set as a later date in the month. It then determines whether a set of dates fall into this segment or not, returning a TRUE or FALSE Boolean value.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the month. |
| period\_no | The month can be offset by period\_no. period\_no is an integer, where the value 0 indicates the month which contains base\_date. Negative values in period\_no indicate preceding months and positive values indicate succeeding months. |

When to use inmonthtodate

The inmonthtodate() function returns a Boolean result. Typically, this type of function is used as a condition in an if expression. The inmonthtodate() function returns an [aggregation](#glossary-0 "Glossary term") or calculation that depends on whether a date occurred in the month up to and including the date in question.

For example, the inmonthtodate() function can be used to identify all equipment manufactured in a month up to a specific date.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| inmonthtodate ('01/25/2013', '25/01/2013', 0) | Returns True |
| inmonthtodate ('01/25/2013', '24/01/2013', 0) | Returns False |
| inmonthtodate ('01/25/2013', '28/02/2013', -1) | Returns True |

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for 2022 is loaded into a table called ‘Transactions’.
- A date [field](#glossary-2 "Glossary term") is provided in the DateFormat system [variable](#glossary-3 "Glossary term") (MM/DD/YYYY) format.
- A [preceding load](#glossary-4 "Glossary term") statement containing:

  - The inmonthtodate() function which is set as the field, ‘in\_month\_to\_date’. This determines which transactions took place between July 1 and July 26, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
    *,
    inmonthtodate(date,'07/26/2022', 0) as in_month_to_date
    ;
Load
*
Inline
[
id,date,amount
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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_month\_to\_date

Results table

| date | in\_month\_to\_date |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | 0 |
| 5/7/2022 | 0 |
| 5/16/2022 | 0 |
| 6/15/2022 | 0 |
| 6/26/2022 | 0 |
| 7/9/2022 | -1 |
| 7/22/2022 | -1 |
| 7/23/2022 | -1 |
| 7/27/2022 | 0 |
| 8/2/2022 | 0 |
| 8/8/2022 | 0 |
| 8/19/2022 | 0 |
| 9/26/2022 | 0 |
| 10/14/2022 | 0 |
| 10/29/2022 | 0 |

The ‘in\_month\_to\_date’ field is created in the preceding load statement by using the inmonthtodate() function.

The first argument identifies which field is being evaluated. The second argument is a hard-coded date, July 26, which is the base\_date. This base\_date argument identifies which month is segmented and the end boundary of that segment.

A period\_no of 0 is the final argument meaning that the function is not comparing months preceding or following the segmented month.

Diagram of inmonthtodate function with no additional arguments.

![Diagram showing the range of transactions that are identified as TRUE by the inmonthtodate function. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthtodate-example1-diagram.png "Click to view full size")

As a result, any transaction that occurs between July 1 and July 26 returns a Boolean result of TRUE. Any transaction that occurs in July after July 26 returns a Boolean result of FALSE as will any transaction in any other month of the year.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

In this example, the task is to create a field, ‘six\_months\_prior’, that determines which transactions took place a full six months before July 1 and July 26.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
    *,
    inmonthtodate(date,'07/26/2022', -6) as six_months_prior
    ;
Load
*
Inline
[
id,date,amount
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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- six\_months\_prior

Results table

| date | six\_months\_prior |
| --- | --- |
| 1/7/2022 | -1 |
| 1/19/2022 | -1 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | 0 |
| 5/7/2022 | 0 |
| 5/16/2022 | 0 |
| 6/15/2022 | 0 |
| 6/26/2022 | 0 |
| 7/9/2022 | 0 |
| 7/22/2022 | 0 |
| 7/23/2022 | 0 |
| 7/27/2022 | 0 |
| 8/2/2022 | 0 |
| 8/8/2022 | 0 |
| 8/19/2022 | 0 |
| 9/26/2022 | 0 |
| 10/14/2022 | 0 |
| 10/29/2022 | 0 |

By using -6 as the period\_no argument in the inmonthtodate() function, the boundaries of the comparator month segment shift by six months. Initially the month segment equates to between July 1 and July 26. The period\_no then offsets this segment by a negative six months and the date boundaries are shifted and fall between January 1 and January 26.

Diagram of inmonthtodate function with period\_no set to -6.

![Diagram showing the range of transactions with the period_no argument set to -6. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthtodate-example2-diagram.png "Click to view full size")

As a result, any transaction that occurs between January 1 and January 26 will return a Boolean result of TRUE.

## Example 3 – Chart example

expression

Overview

The same dataset and scenario as the first example are used.

In this example, the dataset is unchanged and loaded into the application. The task is to create a calculation that determines whether transactions took place between July 1 and July 26 as a [measure](#glossary-7 "Glossary term") in a chart of the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
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

date

To calculate whether transactions took place between July 1 and July 26, create the following measure:

=inmonthtodate(date,'07/26/2022', 0)

Results table

| date | =inmonthtodate(date,'07/26/2022', 0) |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | 0 |
| 5/7/2022 | 0 |
| 5/16/2022 | 0 |
| 6/15/2022 | 0 |
| 6/26/2022 | 0 |
| 7/9/2022 | -1 |
| 7/22/2022 | -1 |
| 7/23/2022 | -1 |
| 7/27/2022 | 0 |
| 8/2/2022 | 0 |
| 8/8/2022 | 0 |
| 8/19/2022 | 0 |
| 9/26/2022 | 0 |
| 10/14/2022 | 0 |
| 10/29/2022 | 0 |

The ‘in\_month\_to\_date’ field measure is created in the chart by using the inmonthtodate() function.

The first argument identifies which field is being evaluated. The second argument is a hard-coded date, July 26, which is the base\_date. This base\_date argument identifies which month is segmented and the end boundary of that segment. A period\_no of 0 is the final argument. This means that the function is not comparing months preceding or following the segmented month.

Diagram of inmonthtodate function with no additional arguments.

![Diagram showing the range of transactions with between July 1 and July 26. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthtodate-example3-diagram.png "Click to view full size")

As a result, any transaction that occurs between July 1 and July 26 returns a Boolean result of TRUE. Any transaction that occurs in July after July 26 returns a Boolean result of FALSE as will any transaction in any other month of the year.

## Example 4 – Scenario

Load script and results

Overview

In this example, a dataset is loaded into a table called ‘Products’. The table contains the following fields:

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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- =monthname(manufacture\_date)
- =if(Inmonthtodate(manufacture\_date,makedate(2022,07,26),0),'Defective','Faultless')

To calculate the sum cost of the products, create this measure:

=sum(cost\_price)

Set the measure’s Number Formatting to Money.

Results table

| monthname(manufacture\_date) | if(Inmonthtodate(manufacture\_date,makedate(2022,07,26),0),'Defective','Faultless') | Sum(cost\_price) |
| --- | --- | --- |
| Jan 2022 | Faultless | $54.40 |
| Feb 2022 | Faultless | $145.69 |
| Mar 2022 | Faultless | $53.80 |
| Apr 2022 | Faultless | $82.06 |
| May 2022 | Faultless | $127.60 |
| Jun 2022 | Faultless | $141.82 |
| Jul 2022 | Defective | $144.66 |
| Jul 2022 | Faultless | $69.98 |
| Aug 2022 | Faultless | $147.46 |
| Sep 2022 | Faultless | $84.21 |
| Oct 2022 | Faultless | $163.91 |

The inmonthtodate() function returns a Boolean value when evaluating the manufacturing dates of each of the products.

For the dates that return a Boolean value of TRUE, the product is marked as ‘Defective’. For any product returning a value of FALSE, and therefore not made in the month up to and including July 26, it marks the products as ‘Faultless’.
