---
title: "inyeartodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyeartodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inyeartodate Script and chart function

Expand/Collapse all

# inyeartodate Script and chart function

This function returns
True if timestamp lies inside the
part of year containing base\_date
up until and including the last millisecond of base\_date.

Syntax:

InYearToDate
(timestamp, base\_date, period\_no[, first\_month\_of\_year])

Return data type:  Boolean

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Diagram of inyeartodate function

![Example diagram of the range of dates within which the inyeartodate function will return a value of TRUE.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyeartodate-general.png "Click to view full size")

The inyeartodate() function will segment a particular portion of the year with the base\_date, identifying the maximum allowed date for that year segment. The function then evaluates whether a date [field](#glossary-0 "Glossary term") or value falls into this segment and returns a Boolean result.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the year. |
| period\_no | The year can be offset by period\_no. period\_no is an integer, where the value 0 indicates the year that contains base\_date. Negative values in period\_no indicate preceding years, and positive values indicate succeeding years. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

## When to use inyeartodate

The inyeartodate() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. This would return an [aggregation](#glossary-1 "Glossary term") or calculation dependent on whether a date evaluated occurred in the year up to and including the date in question.

For example, the inyeartodate() function can be used to identify all equipment manufactured in a year up to a specific date.

These examples use the date format MM/DD/YYYY. The date format is specified in the SET DateFormat statement at the top of your data [load script](#glossary-2 "Glossary term"). Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| inyeartodate ('01/25/2013', '02/01/2013', 0) | Returns TRUE. |
| inyeartodate ('01/25/2012', '01/01/2013', 0) | Returns FALSE. |
| inyeartodate ('01/25/2012', '02/01/2013', -1) | Returns TRUE. |
| inyeartodate ('11/25/2012', '01/31/2013', 0, 4) | Returns TRUE. The value of timestamp falls inside the fiscal year beginning in the fourth month and before the value of base\_date. |
| inyeartodate ('3/31/2013', '01/31/2013', 0, 4 ) | Returns FALSE. Compared with the previous example, the value of timestamp is still inside the fiscal year, but it is after the value of base\_date, so it falls outside the part of the year. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-3 "Glossary term") containing a set of transactions between 2020 and 2022, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system [variable](#glossary-4 "Glossary term") (MM/DD/YYYY) format.
- The creation of a field, in\_year\_to\_date, that determines which transactions took place in the year up until July 26, 2021.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inyeartodate(date,'07/26/2021', 0) as in_year_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'01/13/2020',37.23
8189,'02/26/2020',17.17
8190,'03/27/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'06/14/2020',82.06
8194,'08/07/2020',40.39
8195,'09/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'07/27/2021',25.12
8204,'06/06/2022',46.23
8205,'07/18/2022',84.21
8206,'11/14/2022',96.24
8207,'12/12/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_year\_to\_date

Results table

| date | in\_year\_to\_date |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 06/14/2020 | 0 |
| 08/07/2020 | 0 |
| 09/05/2020 | 0 |
| 01/22/2021 | -1 |
| 02/03/2021 | -1 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 07/27/2021 | 0 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

The in\_year\_to\_date field is created in the [preceding load](#glossary-5 "Glossary term") statement by using the inyeartodate() function. The first argument provided identifies which field is being evaluated.

The second argument is a hard-coded date for the for the July 26, 2021, which is the base\_date that identifies the end boundary of the year segment. A period\_no of 0 is the final argument, meaning that the function is not comparing years preceding or following the segmented year.

Diagram of inyeartodate function, no additional arguments

![Diagram showing the range of dates for which the inyeartodate function will return a value of TRUE. This example contains no additional arguments.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyeartodate-examples-no-additional-arguments.png "Click to view full size")

Any transaction that occurs in between January 1 and July 26 returns a Boolean result of TRUE. Transactions dates before 2021 and beyond July 26, 2021 return FALSE.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, previous\_year\_to\_date, that determines which transactions took place a full year before the year segment ending on July 26, 2021.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inyeartodate(date,'07/26/2021', -1) as previous_year_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'01/13/2020',37.23
8189,'02/26/2020',17.17
8190,'03/27/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'06/14/2020',82.06
8194,'08/07/2020',40.39
8195,'09/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'07/27/2021',25.12
8204,'06/06/2022',46.23
8205,'07/18/2022',84.21
8206,'11/14/2022',96.24
8207,'12/12/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- previous\_year\_to\_date

Results table

| date | previous\_year\_to\_date |
| --- | --- |
| 01/13/2020 | -1 |
| 02/26/2020 | -1 |
| 03/27/2020 | -1 |
| 04/16/2020 | -1 |
| 05/21/2020 | -1 |
| 06/14/2020 | -1 |
| 08/07/2020 | 0 |
| 09/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 07/27/2021 | 0 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

A period\_no value of -1 indicates that the inyeartodate () function compares the input quarter segment to the preceding year. With an input date of July 26, 2021, the segment from January 1, 2021 to July 26, 2021 was initially identified as the year-to-date. The period\_no then offsets this segment by a full year earlier, causing the date boundaries to become January 1 to July 26, 2020.

Diagram of inyeartodate function, period\_no example

![Diagram showing the range of dates for which the inyeartodate function will return a value of TRUE. In this example, the period_no argument is set to -1.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyeartodate-examples-period-no.png "Click to view full size")

Therefore, any transaction that occurs between January 1 and July 26, 2020 will return a Boolean result of TRUE.

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, in\_year\_to\_date, that determines which transactions took place in the same year up to July 26, 2021.

In this example, we set March as the first month of the fiscal year.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        inyeartodate(date,'07/26/2021', 0,3) as in_year_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,'01/13/2020',37.23
8189,'02/26/2020',17.17
8190,'03/27/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'06/14/2020',82.06
8194,'08/07/2020',40.39
8195,'09/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'07/27/2021',25.12
8204,'06/06/2022',46.23
8205,'07/18/2022',84.21
8206,'11/14/2022',96.24
8207,'12/12/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_year\_to\_date

Results table

| date | in\_year\_to\_date |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 06/14/2020 | 0 |
| 08/07/2020 | 0 |
| 09/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 07/27/2021 | 0 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

By using 3 as the first\_month\_of\_year argument in the inyeartodate() function, the function begins the year on March 1. The base\_date of July 26, 2021 then sets the end date for that year segment.

Diagram of inyeartodate function, first\_month\_of\_year example

![Diagram showing the range of dates for which the inyeartodate function will return a value of TRUE. In this example, the first_month_of_year is defined as 3, setting March to the first month of the year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyeartodate-examples-first-mth-yr.png "Click to view full size")

Therefore, any transaction that occurs between March 1 and July 26, 2021 will return a Boolean result of TRUE, while transactions with dates outside these boundaries will return a value of FALSE.

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](#glossary-6 "Glossary term") and add the load script below to a new tab.

The load script contains the same dataset and scenario as the first example. However, in this example, the unchanged dataset is loaded into the application. The calculation that determines which transactions took place in the same year up to July 26, 2021 is created as a [measure](#glossary-7 "Glossary term") in a chart object in the application.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,'01/13/2020',37.23
8189,'02/26/2020',17.17
8190,'03/27/2020',88.27
8191,'04/16/2020',57.42
8192,'05/21/2020',53.80
8193,'06/14/2020',82.06
8194,'08/07/2020',40.39
8195,'09/05/2020',87.21
8196,'01/22/2021',95.93
8197,'02/03/2021',45.89
8198,'03/17/2021',36.23
8199,'04/23/2021',25.66
8200,'05/04/2021',82.77
8201,'06/30/2021',69.98
8202,'07/26/2021',76.11
8203,'07/27/2021',25.12
8204,'06/06/2022',46.23
8205,'07/18/2022',84.21
8206,'11/14/2022',96.24
8207,'12/12/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:date.

Create the following measure:

=inyeartodate(date,'07/26/2021', 0)

Results table

| date | =inyeartodate(date,'07/26/2021', 0) |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 06/14/2020 | 0 |
| 08/07/2020 | 0 |
| 09/05/2020 | 0 |
| 01/22/2021 | -1 |
| 02/03/2021 | -1 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 07/27/2021 | 0 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

The in\_year\_to\_date measure is created in the chart object by using the inyeartodate() function. The first argument provided identifies which field is being evaluated. The second argument is a hard-coded date for July 26, 2021, which is the base\_date that identifies the end boundary of the comparator year segment. A period\_no of 0 is the final argument, meaning that the function is not comparing years preceding or following the segmented year.

Diagram of inyeartodate function, chart object example

![Diagram showing the range of dates for which the inyeartodate function will return a value of TRUE. The function determines whether transactions took place in the same year as July 26.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyeartodate-examples-chart-object.png "Click to view full size")

Any transaction that occurs between January 1 and July 26, 2021 returns a Boolean result of TRUE. Transaction dates before 2021 and after July 26, 2021 return FALSE.

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called Products.
- Information concerning product ID, product type, manufacture date, and cost price.

The end user would like a chart object that displays, by product type, the cost of the products manufactured in 2021 up to July 26.

Load script

```
Products:
Load
*
Inline
[
product_id,product_type,manufacture_date,cost_price
8188,product A,'01/13/2020',37.23
8189,product B,'02/26/2020',17.17
8190,product B,'03/27/2020',88.27
8191,product C,'04/16/2020',57.42
8192,product D,'05/21/2020',53.80
8193,product D,'08/14/2020',82.06
8194,product C,'10/07/2020',40.39
8195,product B,'12/05/2020',87.21
8196,product A,'01/22/2021',95.93
8197,product B,'02/03/2021',45.89
8198,product C,'03/17/2021',36.23
8199,product C,'04/23/2021',25.66
8200,product B,'05/04/2021',82.77
8201,product D,'06/30/2021',69.98
8202,product D,'07/26/2021',76.11
8203,product D,'12/27/2021',25.12
8204,product C,'06/06/2022',46.23
8205,product C,'07/18/2022',84.21
8206,product A,'11/14/2022',96.24
8207,product B,'12/12/2022',67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:product\_type.

Create a measure that calculates the sum of each product that was manufactured in 2021 before July 27:

=sum(if(inyeartodate(manufacture\_date,makedate(2021,07,26),0),cost\_price,0))

Set the measure's Number formatting to Money.

Results table

| product\_type | =sum(if(inyeartodate(manufacture\_date,makedate(2021,07,26),0),cost\_price,0)) |
| --- | --- |
| product A | $95.93 |
| product B | $128.66 |
| product C | $61.89 |
| product D | $146.09 |

The inyeartodate() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured in 2021 before July 27, the inyeartodate() function returns a Boolean value of TRUE and sums the cost\_price.

Product D is the only product that was also manufactured after July 26th in 2021. The entry with product\_ID 8203 was manufactured on December 27 and cost $25.12. Therefore, this cost was not included in the total for Product D in the chart object.
