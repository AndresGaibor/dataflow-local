---
title: "inquartertodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inquartertodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inquartertodate Script and chart function

Expand/Collapse all

# inquartertodate Script and chart function

This function returns
True if timestamp lies inside the
part of the quarter containing base\_date
up until and including the last millisecond of base\_date.

Syntax:

InQuarterToDate
(timestamp, base\_date, period\_no [, first\_month\_of\_year])

Return data type:  Boolean

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Diagram of inquartertodate function

![Example diagram of the range of dates within which the inquartertodate function will return a value of TRUE. In this case, it returns TRUE for certain values in the first half of the second quarter of the year, and FALSE for all other values.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquartertodate-general.png "Click to view full size")

The inquartertodate() function divides the year into four equal quarters between January 1 and December 31 (or the user-defined start of year and its corresponding end date). Using the base\_date, the function will then segment a particular quarter, with the base\_date identifying both which quarter and the maximum allowed date for that quarter segment. Finally, the function returns a Boolean result when comparing the prescribed date values to that segment.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the quarter. |
| period\_no | The quarter can be offset by period\_no. period\_no is an integer, where the value 0 indicates the quarter which contains base\_date. Negative values in period\_no indicate preceding quarters and positive values indicate succeeding quarters. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use inquartertodate

The inquartertodate() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. The inquartertodate() function would be used to return an [aggregation](#glossary-0 "Glossary term") or calculation dependent on whether a date evaluated occurred in the quarter up to and including the date in question.

For example, the inquartertodate() function can be used to identify all equipment manufactured in a quarter up to a specific date.

Function examples

| Example | Result |
| --- | --- |
| inquartertodate('01/25/2013', '03/25/2013', 0) | Returns TRUE, since the value of timestamp, 01/25/2013, lies within the three-month period from 01/01/2013 to  03/25/2013, in which the value of base\_date, 03/25/2013, lies. |
| inquartertodate('04/26/2013', '03/25/2013', 0) | Returns FALSE, since 04/26/2013 is outside the same period as the previous example. |
| inquartertodate('02/25/2013', '06/09/2013', -1) | Returns TRUE, since the value of period\_no, -1, shifts the search period back one period of three months (one quarter of the year). This makes the search period 01/01/2013 to 03/09/2013. |
| inquartertodate('03/25/2006', '04/15/2006', 0, 2) | Returns TRUE, since the value of first\_month\_of\_year is set to 2, which makes the search period 02/01/2006 to 04/15/2006 instead of 04/01/2006 to 04/15/2006. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions for 2022, which is loaded into a table called Transactions.
- The date [field](#glossary-2 "Glossary term") provided in the DateFormat system [variable](#glossary-3 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, in\_quarter\_to\_date, that determines which transactions took place in the quarter up until May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inquartertodate(date,'05/15/2022', 0) as in_quarter_to_date
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
- in\_quarter\_to\_date

Results table

| date | in\_quarter\_to\_date |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
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

The in\_quarter\_to\_date field is created in the [preceding load](#glossary-4 "Glossary term") statement by using the inquartertodate() function. The first argument provided identifies which field is being evaluated. The second argument is a hard-coded date for the for May 15, which is the base\_date that identifies which quarter to segment and defines the end boundary of that segment. A period\_no of 0 is the final argument, meaning that the function is not comparing quarters preceding or following the segmented quarter.

Diagram of inquartertodate function, no additional arguments

![Diagram showing the range of dates for which the inquartertodate function will return a value of TRUE. This example contains no additional arguments.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquartertodate-example-no-additional-arguments.png "Click to view full size")

Any transaction that occurs in between April 1 and May 15 returns a Boolean result of TRUE. Transactions dates of May 16 and later will return FALSE, as do any transactions before April 1.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, previous\_qtr\_to\_date, that determines which transactions took place a full quarter before the quarter segment ending on May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inquartertodate(date,'05/15/2022', -1) as previous_qtr_to_date
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
- previous\_qtr\_to\_date

Results table

| date | previous\_qtr\_to\_date |
| --- | --- |
| 1/7/2022 | -1 |
| 1/19/2022 | -1 |
| 2/5/2022 | -1 |
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

A period\_no value of -1 indicates that the inquartertodate () function compares the input quarter segment to the preceding quarter. May 15 falls into the second quarter of the year, so the segment initially equates to between April 1 and May 15. The period\_no then offsets this segment by three months earlier, causing the date boundaries to become January 1 to February 15.

Diagram of inquartertodate function, period\_no example

![Diagram showing the range of dates for which the inquartertodate function will return a value of TRUE. In this example, the period_no argument is set to -1.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquartertodate-example-period-no.png "Click to view full size")

Therefore, any transaction that occurs between January 1 and February 15 will return a Boolean result ofTRUE.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, in\_quarter\_to\_date, that determines which transactions took place in the same quarter up to May 15, 2022.

In this example, we set March as the first month of the fiscal year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inquartertodate(date,'05/15/2022', 0,3) as in_quarter_to_date
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
- in\_quarter\_to\_date

Results table

| date | in\_quarter\_to\_date |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | -1 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
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

By using 3 as the first\_month\_of\_year argument in the inquartertodate() function, the function begins the year on March 1, and then divides the year into quarters. Therefore, the quarter segments are:

- March to May
- June to August
- September to November
- December to February

The base\_date of May 15 then segments the March to May quarter by setting its end boundary as May 15.

Diagram of inquartertodate function, first\_month\_of\_year example

![Diagram showing the range of dates for which the inquartertodate function will return a value of TRUE. In this example, the first_month_of_year is defined as 3, setting March to the first month of the year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquartertodate-example-first-mth-yr.png "Click to view full size")

Therefore, any transaction that occurs in between the March 1 and May 15 will return a Boolean result of TRUE, while transactions with dates outside these boundaries will return a value of FALSE.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the [load script](#glossary-6 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The calculation that determines which transactions took place in the same quarter as May 15 is created as a [measure](#glossary-7 "Glossary term") in the chart object.

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

Load the data and open a sheet. Create a new table and add this field as a dimension:date.

Create the following measure:

=inquartertodate(date,'05/15/2022', 0)

Results table

| date | =inquartertodate(date,'05/15/2022', 0) |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
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

The in\_quarter\_to\_date measure is created in a chart object by using the inquartertodate() function. The first argument is the date field being evaluated. The second argument is a hard-coded date for May 15, which is the base\_date that identifies which quarter to segment and defines the end boundary of that segment. A period\_no of 0 is the final argument, meaning that the function is not comparing quarters preceding or following the segmented quarter.

Diagram of inquartertodate function, chart object example

![Diagram showing the range of dates for which the inquartertodate function will return a value of TRUE. The function determines whether transactions took place in the same quarter as May 15.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquartertodate-example-chart-object.png "Click to view full size")

Any transaction that occurs between April 1 and May 15 returns a Boolean result of TRUE. Transactions on May 16 and later will return FALSE, as do any transactions before April 1.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Products.
- Information concerning product ID, manufacture date, and cost price.

On May 15, 2022, a piece of equipment error was identified in the manufacturing process and resolved. Products that were manufactured in that quarter up to this date will be defective. The end user would like a chart object that displays, by quarter name, the status of whether the product is ‘defective’ or ‘faultless’ and the cost of the products manufactured in that quarter to date.

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

Do the following:

1. Load the data and open a [sheet](#glossary-8 "Glossary term"). Create a new table. Create a [dimension](#glossary-9 "Glossary term") to show the quarter names:

   =quartername(manufacture\_date)
2. Next, create a dimension to identify which of the products are defective and which are faultless:

   =if(inquartertodate(manufacture\_date,makedate(2022,05,15),0),'Defective','Faultless')
3. Create a measure to sum the cost\_price of the products:

   =sum(cost\_price)
4. Set the measure's Number formatting to Money.

Results table

| quartername(manufacture\_date) | if(inquartertodate(manufacture\_date,makedate(2022,05,15),0),'Defective','Faultless') | Sum(cost\_price) |
| --- | --- | --- |
| Jan-Mar 2022 | Faultless | $253.89 |
| Apr-Jun 2022 | Faultless | $229.03 |
| Apr-Jun 2022 | Defective | $122.45 |
| Jul-Sep 2022 | Faultless | $446.31 |
| Oct-Dec 2022 | Faultless | $163.91 |

The inquartertodate() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For those that return a Boolean value of TRUE, it marks the products as ‘Defective’. For any product returning a value of FALSE, and therefore not made in the quarter up to and including May 15, it marks the products as ‘Faultless’.
