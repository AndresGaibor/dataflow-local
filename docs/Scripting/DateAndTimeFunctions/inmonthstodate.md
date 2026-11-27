---
title: "inmonthstodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonthstodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inmonthstodate Script and chart function

Expand/Collapse all

# inmonthstodate Script and chart function

This function finds if a timestamp falls within the part a period of the month, bi-month, quarter, four-month period, or half-year up to and including the last millisecond of base\_date. It is also possible to find if the timestamp falls within a previous or following time period.

Syntax:

InMonths (n\_months, timestamp, base\_date, period\_no[, first\_month\_of\_year ])

Return data type:  Boolean

Diagram of inmonthstodate function.

![Diagram showing how inmonthstodate function can be used to identify if a timstamp falls within or outside of a set segment of time.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-diagram1.png "Click to view full size")

Arguments

| Argument | Description |
| --- | --- |
| n\_months | The number of months that defines the period. An integer or expression that resolves to an integer that must be one of: 1 (equivalent to the inmonth() function), 2 (bi-month), 3 (equivalent to the inquarter()function), 4 (four-month period), or 6 (half year). |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the period. |
| period\_no | The period can be offset by period\_no, an integer, or expression resolving to an integer, where the value 0 indicates the period that contains base\_date. Negative values in period\_no indicate preceding periods and positive values indicate succeeding periods. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

In the inmonthstodate() function, the base\_date acts as the end point of the particular year segment that it is part of.

For example, if the year was broken into tertial segments, and the base\_date was May 15, any timestamp between the start of January and end of April would return a Boolean result of FALSE. Dates between May 1 and May 15 would return TRUE. The rest of the year would return FALSE.

Diagram of Boolean results range of inmonthstodate function.

![Diagram showing the range of Boolean results of the inmonthstodate function. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-diagram2.png "Click to view full size")

The following segments of the year are available in the function as n\_month arguments.

n\_month arguments

| Period | Number of months |
| --- | --- |
| month | 1 |
| bi-month | 2 |
| quarter | 3 |
| tertial | 4 |
| half-year | 6 |

When to use inmonthstodate

The inmonthstodate() function returns a Boolean result. Typically, this type of function is used as a condition in an if expression. By using the inmonthstodate() function, you can select the period you want to be evaluated. For example, providing an input variable that lets the user identify the products manufactured in the month, quarter, or half-year of a period, up to a certain date.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| inmonthstodate(4, '01/25/2013', '04/25/2013', 0) | Returns True, because the value of timestamp, 01/25/2013, lies within the four-month period 01/01/2013 up to the end of 04/25/2013, in which the value of base\_date, 04/25/2013 lies. |
| inmonthstodate(4, '04/26/2013', '04/25/2006', 0) | Returns False, because 04/26/2013 is outside the same period as the previous example. |
| inmonthstodate(4, '09/25/2005', '02/01/2006', -1) | Returns True, because the value of period\_no, -1, shifts the search period back one period of four months (the value of n-months), which makes the search period 01/09/2005 to 02/01/2006. |
| inmonthstodate(4, '04/25/2006', '06/01/2006', 0, 3) | Returns True, because the value of first\_month\_of\_year is set to 3, which makes the search period 03/01/2006 to 06/01/2006 instead of 05/01/2006 to 06/01/2006. |

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-0 "Glossary term") containing a set of transactions for 2022 that is loaded into a table called ‘Transactions’.
- A date [field](#glossary-1 "Glossary term") in the DateFormat system variable (MM/DD/YYYY) format.
- A [preceding load](#glossary-2 "Glossary term") statement containing:

  - The inmonthstodate() function that is set as the field, ‘in\_months\_to\_date’. This determines which transactions took place in the quarter up until May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							inmonthstodate(3,date,'05/15/2022', 0) as in_months_to_date
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
- in\_months\_to\_date

Results table

| date | in\_months\_to\_date |
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

The ‘in\_months\_to\_date’ field is created in the preceding load statement by using the inmonthstodate() function.

The first argument provided is 3, dividing the year into quarter segments. The second argument identifies which field is being evaluated. The third argument is a hard-coded date for May 15, which is the base\_date that defines the end boundary of the segment. A period\_no of 0 is the final argument.

Diagram of inmonthstodate function with no additional arguments.

![Diagram showing the range of transactions that are identified as TRUE by the inmonthstodate function. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-diagram2.png "Click to view full size")

Any transaction that occurs between April 1 and May 15 returns a Boolean result of TRUE. Transaction dates outside of that period return FALSE.

## Example 2 – period\_no

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the task is to create a field, ‘previous\_qtr\_to\_date’, that determines if the transactions took place a quarter before May 15.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							inmonthstodate(3,date,'05/15/2022', -1) as previous_qtr_to_date
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

By using -1 as the period\_no argument in the inmonthstodate() function, the function shifts the boundaries of the comparator year segment by a quarter.

May 15 falls into the second quarter of the year and therefore the segment initially equates to between April 1 and May 15. The period\_no argument offsets this segment by a negative three months. The date boundaries become January 1 to February 15.

Diagram of inmonthstodate function with period\_no set to -1.

![Diagram showing the range of transactions with the period_no argument set to -1. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-example2-diagram.png "Click to view full size")

Therefore, any transaction that occurs between January 1 and February 15 will return a Boolean result of TRUE.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

The same dataset and scenario as the first example are used.

In this example, the organizational policy is for March to be the first month of the financial year.

Create a field, ‘in\_months\_to\_date’, that determines which transactions took place in the same quarter up to May 15, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

							Transactions:
							Load
							*,
							inmonthstodate(3,date,'05/15/2022', 0,3) as in_months_to_date
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
- in\_months\_to\_date

Results table

| date | previous\_qtr\_to\_date |
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

By using 3 as the first\_month\_of\_year argument in the inmonthstodate() function, the function begins the year on March 1 and then divides the year into quarters based on the first argument provided. Therefore, the quarter segments are:

- Mar-May
- Jun-Aug
- Sep-Nov
- Dec-Feb

The base\_date of May 15 then segments the Mar-May quarter by setting its end boundary as May 15.

Diagram of inmonthstodate function with March set as first month of the year.

![Diagram showing the range of transactions with the first month of the year set as March.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-example3-diagram.png "Click to view full size")

Therefore, any transaction that occurs between March 1 and May 15 will return a Boolean result of TRUE, and transactions with dates outside these boundaries will return a value of FALSE.

## Example 4 – Chart example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

In this example, the dataset is unchanged and loaded into the application. The task is to create a calculation that determines whether transactions took place in the same quarter as May 15 as a [measure](#glossary-4 "Glossary term") in a chart of the application.

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

To calculate whether transactions took place in the same quarter as May 15, create the following measure:

=inmonthstodate(3,date,'05/15/2022', 0)

Results table

| date | =inmonthstodate(3,date,'05/15/2022', 0) |
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

The ‘in\_months\_to\_date’ measure is created in the chart by using the inmonthstodate() function.

The first argument provided is 3, dividing the year into quarter segments. The second argument identifies which field is being evaluated. The third argument is a hard-coded date May 15 which is the base\_date that defines the end boundary of the segment. A period\_no of 0 is the final argument.

Diagram of inmonthstodate function with quarter segments.

![Diagram showing the range of transactions that return a TRUE boolean value. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inmonthstodate-example4-diagram.png "Click to view full size")

Any transaction that occurs between April 1 and May 15 will return a Boolean result of TRUE. Transaction dates outside of that segment will return FALSE.

## Example 5 – Scenario

Load script and results

Overview

In this example, a dataset is loaded into a table called ‘Sales’. The table contains the following fields:

- Product ID
- Product type
- Sales date
- Sales price

The end user would like a chart that displays, by product type, the sales of products sold in the period leading up to December 24, 2022. The user would like to be able to define the length of this period.

Load script

```
SET vPeriod = 1;

							Products:
							Load
							*
							Inline
							[
							product_id,product_type,sales_date,sales_price
							8188,product A,'9/19/2022',37.23
							8189,product D,'10/27/2022',17.17
							8190,product C,'10/30/2022',88.27
							8191,product B,'10/31/2022',57.42
							8192,product D,'11/16/2022',53.80
							8193,product D,'11/28/2022',82.06
							8194,product A,'12/2/2022',40.39
							8195,product B,'12/5/2022',87.21
							8196,product C,'12/15/2022',95.93
							8197,product B,'12/16/2022',45.89
							8198,product C,'12/19/2022',36.23
							8199,product D,'12/22/2022',25.66
							8200,product D,'12/23/2022',82.77
							8201,product A,'12/24/2022',69.98
							8202,product A,'12/24/2022',76.11
							8203,product B,'12/26/2022',25.12
							8204,product B,'12/27/2022',46.23
							8205,product B,'12/27/2022',84.21
							8206,product C,'12/28/2022',96.24
							8207,product D,'12/29/2022',67.67
						];
```

Results

Load the data and open a [sheet](#glossary-5 "Glossary term").

At the start of the [load script](#glossary-6 "Glossary term") a variable, vPeriod, is created that is tied to the variable input control.

Do the following:

1. In the assets panel, click Charts.
2. Under Dashboard objects, drag a Variable input onto the sheet.
3. Enter a title for the chart.
4. Under Variable, select vPeriod as the name and set the object to show as a Drop down.
5. Under Values, click Dynamic values. Enter the following:

   ```
   ='1~month|2~bi-month|3~quarter|4~tertial|6~half-year'.
   ```
6. Add a new table to the sheet.
7. Under Data in the [properties](#glossary-7 "Glossary term") panel, add product\_type as a [dimension](#glossary-8 "Glossary term").
8. Add the following expression as a measure:

   =sum(if(inmonthstodate($(vPeriod),sales\_date,makedate(2022,12,24),0),sales\_price,0))
9. Set the measure’s Number formatting to Money.

Results table

| product\_type | =sum(if(inmonthstodate($(vPeriod),sales\_date,makedate(2022,12,24),0),sales\_price,0)) |
| --- | --- |
| product A | $186.48 |
| product B | $190.52 |
| product C | $220.43 |
| product D | $261.46 |

The inmonthstodate() function uses the user input as its argument to define the size of the starting segment of the year.

The function passes in the sales date of each of the products as the inmonthstodate() function’s second argument. By using December 24 as the third argument in the inmonthstodate() function, products with sales dates that occur in the defined period up to and including December 24 return a Boolean value of TRUE. The sum function adds the sales of these products.
