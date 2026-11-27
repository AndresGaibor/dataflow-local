---
title: "inquarter Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inquarter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inquarter Script and chart function

Expand/Collapse all

# inquarter Script and chart function

This function returns
True if timestamp lies inside the
quarter containing base\_date.

Syntax:

InQuarter
(timestamp, base\_date, period\_no[, first\_month\_of\_year])

Return data type:  Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Diagram of inquarter() function's range

![Diagram that shows the range of time that the inquarter() function evaluates. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquarter-diagram1.png "Click to view full size")

In other words, the inquarter() function divides the year into four equal quarters between January 1 and December 31. You can use the first\_month\_of\_year argument to change what month is considered the first in your application and the quarters will change based on that argument. The base\_date, the function identifies which quarter should be used as the comparator for the function. Finally, the function returns a Boolean result when comparing date values to that quarter segment.

When to use inquarter

The inquarter() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. This returns an [aggregation](#glossary-1 "Glossary term") or calculation that depends on whether a date occurred in the selected quarter.

For example, the inquarter() function can be used to identify all equipment manufactured in a quarter segment based on the dates when the equipment was manufactured.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the quarter. |
| period\_no | The quarter can be offset by period\_no. period\_no is an integer, where the value 0 indicates the quarter which contains base\_date. Negative values in period\_no indicate preceding quarters and positive values indicate succeeding quarters. |
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
| inquarter ('01/25/2013', '01/01/2013', 0) | Returns TRUE |
| inquarter ('01/25/2013', '04/01/2013', 0) | Returns FALSE |
| inquarter ('01/25/2013', '01/01/2013', -1) | Returns FALSE |
| inquarter ('12/25/2012', '01/01/2013', -1) | Returns TRUE |
| inquarter ('01/25/2013', '03/01/2013', 0, 3) | Returns FALSE |
| inquarter ('03/25/2013', '03/01/2013', 0, 3) | Returns TRUE |

## Example 1 - No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A [preceding load](#glossary-3 "Glossary term") which contains the inquarter() function that is set as the ‘in\_quarter’ [field](#glossary-4 "Glossary term") and determines which transactions took place in the same quarter as May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       inquarter (date,'05/15/2022', 0) as in_quarter
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
- in\_quarter

Results table

| date | in\_quarter |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
| 5/16/2022 | -1 |
| 6/15/2022 | -1 |
| 6/26/2022 | -1 |
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

The ‘in\_quarter’ field is created in the preceding load statement by using the inquarter() function. The first argument identifies which field is being evaluated. The second argument is a hard-coded date for May 15 that identifies which quarter to define as the comparator. A period\_no of 0 is the final argument and ensures the inquarter() function does not compare quarters preceding or following the segmented quarter.

Diagram of inquarter() function with May 15 as the base date

![Diagram that shows the range of time the inquarter() function evaluates with May 15 as the base date, and the year divided into quarter segments.  ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquarter-example1-diagram.png "Click to view full size")

Any transaction that occurs between April 1 and the end of June 30 returns a Boolean result of TRUE.

## Example 2 - period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A preceding load which contains the inquarter() function that is set as the ‘previous\_quarter’ field, and determines which transactions took place in the quarter preceding the quarter of May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       inquarter (date,'05/15/2022', -1) as previous_qtr
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
- previous\_qtr

Results table

| date | previous\_qtr |
| --- | --- |
| 1/7/2022 | -1 |
| 1/19/2022 | -1 |
| 2/5/2022 | -1 |
| 2/28/2022 | -1 |
| 3/16/2022 | -1 |
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

Using -1 as the period\_no argument in the inquarter() function shifts the boundaries of the comparator quarter back by a full quarter. May 15 falls into the second quarter of the year and therefore the segment initially equates to the quarter of April 1 to June 30. The period\_no offsets this segment by a negative three months and causes the date boundaries to become January 1 to March 30.

Diagram of inquarter() function with May 15 as the base date

![Diagram that shows the range of time the inquarter() function evaluates with May 15 as the base date, and period_no set -1, moving the date boundaries back by one quarter.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquarter-example2-diagram.png "Click to view full size")

Therefore, any transaction that occurs between January 1 and March 30 will return a Boolean result of TRUE.

## Example 3 - first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A preceding load which contains the inquarter() function that is set as the ‘in\_quarter’ field, and determines which transactions took place in the same quarter as May 15, 2022.

However, in this example, the organizational policy is for March to be the first month of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
       *,
       inquarter (date,'05/15/2022', 0, 3) as in_quarter
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
- previous\_qtr

Results table

| date | previous\_qtr |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | -1 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
| 5/16/2022 | -1 |
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

Using 3 as the first\_month\_of\_year argument in the inquarter() function sets March 1 as the start of the year and then divides the year into quarters. Therefore, the quarter segments are Mar-May, Jun-Aug, Sep-Nov, Dec-Feb. The base\_date of May 15 sets the Mar-May quarter as the comparator quarter for the function.

Diagram of inquarter() function with March set as the first month of the year

![Diagram that shows the range of time the inquarter() function evaluates with May 15 as the base date, March set as the first month of the year. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquarter-example3-diagram.png "Click to view full size")

Therefore, any transaction that occurs between March 1 and May 31 will return a Boolean result of TRUE.

## Example 4 - Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions in 2022 which is loaded into a table called ‘Transactions’.
- A preceding load which contains the inquarter() function that is set as the ‘in\_quarter’ field, and determines which transactions took place in the same quarter as May 15, 2022.

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

- date

Create the following [measure](#glossary-5 "Glossary term") to calculate whether transactions took place in the same quarter as May 15:

=inquarter(date,'05/15/2022', 0)

Results table

| date | in\_quarter |
| --- | --- |
| 1/7/2022 | 0 |
| 1/19/2022 | 0 |
| 2/5/2022 | 0 |
| 2/28/2022 | 0 |
| 3/16/2022 | 0 |
| 4/1/2022 | -1 |
| 5/7/2022 | -1 |
| 5/16/2022 | -1 |
| 6/15/2022 | -1 |
| 6/26/2022 | -1 |
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

The ‘in\_quarter’ measure is created in the chart by using the inquarter() function. The first argument identifies which field is being evaluated. The second argument is a hard-coded date for May 15 that identifies which quarter to define as the comparator. A period\_no of 0 is the final argument and ensures the inquarter() function does not compare quarters preceding or following the segmented quarter.

Diagram of inquarter() function with May 15 as the base date

![Diagram that shows the range of time the inquarter() function evaluates with May 15 as the base date, and the year divided into quarter segments.  ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inquarter-example1-diagram.png "Click to view full size")

Any transaction that occurs between April 1 and the end of June 30 returns a Boolean result of TRUE.

## Example 5 - Scenario

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called ‘Products’.
- The table contains the following fields:

  - product ID
  - product type
  - manufacture date
  - cost price

It has been identified that due to equipment error, products that were manufactured in the quarter of May 15, 2022 were defective. The end user would like a chart that displays, by quarter name, the status of which products manufactured were ‘defective’ or ‘faultless’ and the cost of the products manufactured in that quarter.

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

=quartername(manufacture\_date)

Create the following measures:

- =if(only(InQuarter(manufacture\_date,makedate(2022,05,15),0)),'Defective','Faultless'), to identify which of the products are defective and which are faultless using the inquarter() function.
- =sum(cost\_price), to show the sum of the cost of each product.

Do the following:

1. Set the measure’s Number Formatting to Money.
2. Under Appearance, turn off Totals.

Results table

| quartername(manufacture\_date) | =if(only(InQuarter(manufacture\_date,makedate(2022,05,15),0)),'Defective','Faultless') | Sum(cost\_price) |
| --- | --- | --- |
| Jan-Mar 2022 | Faultless | 253.89 |
| Apr-Jun 2022 | Defective | 351.48 |
| Jul-Sep 2022 | Faultless | 446.31 |
| Oct-Dec 2022 | Faultless | 163.91 |

The inquarter() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured in the quarter that contains May 15, the inquarter() function returns a Boolean value of TRUE and marks the products as ‘Defective’. For any product returning a value of FALSE, and therefore not manufactured in that quarter, it marks the products as ‘Faultless’.
