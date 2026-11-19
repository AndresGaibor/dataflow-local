---
title: "inyear Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# inyear Script and chart function

This function returns
True if timestamp lies inside the
year containing base\_date.

Syntax:

InYear (timestamp, base\_date, period\_no [, first\_month\_of\_year])

Return data type:  Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Diagram of `inyear()` function's range

![Diagram that shows the range of time that the inyear() function evaluates and will return a Boolean result depending on the placement of the base date.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyear-diagram1.png)

The `inyear()` function returns a Boolean result when comparing the selected date values to a year defined by the `base_date`.

When to use inyear

The `inyear()` function returns a Boolean result. Typically, this type of function will be used as a condition in an `if expression`. This returns an [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm#glossary-0 "Glossary term") or calculation dependent on whether a date evaluated occurred in the year in question. For example, the `inyear()` function can be used to identify all sales that occurred in a defined year.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date that you want to compare with base\_date. |
| base\_date | Date that is used to evaluate the year. |
| period\_no | The year can be offset by period\_no. period\_no is an integer, where the value 0 indicates the year that contains base\_date. Negative values in period\_no indicate preceding years, and positive values indicate succeeding years. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. |

You can use the following values to set the first month of year in the `first_month_of_year` argument:

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

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `inyear ('01/25/2013', '01/01/2013', 0 )` | Returns TRUE |
| `inyear ('01/25/2012', '01/01/2013', 0)` | Returns FALSE |
| `inyear ('01/25/2013', '01/01/2013', -1)` | Returns FALSE |
| `inyear ('01/25/2012', '01/01/2013', -1 )` | Returns TRUE |
| `inyear ('01/25/2013', '01/01/2013', 0, 3)` | Returns TRUE  The value of `base_date` and `first_month_of_year` specify that timestamp must fall within 01/03/2012 and 02/28/2013 |
| `inyear ('03/25/2013', '07/01/2013', 0, 3 )` | Returns TRUE |

## Example 1 - Basic example

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm#glossary-1 "Glossary term") containing a set of transactions between 2020 and 2022 which is loaded into a table called ‘`Transactions`’.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm#glossary-2 "Glossary term") which contains the `inyear()` function that is set as the ‘`in_year`’ [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm#glossary-3 "Glossary term") and determines which transactions took place in the same year as July 26, 2021.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
Transactions: 
    Load 
        *, 
        inyear(date,'07/26/2021', 0) as in_year 
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
8193,'08/14/2020',82.06 
8194,'10/07/2020',40.39 
8195,'12/05/2020',87.21 
8196,'01/22/2021',95.93 
8197,'02/03/2021',45.89 
8198,'03/17/2021',36.23 
8199,'04/23/2021',25.66 
8200,'05/04/2021',82.77 
8201,'06/30/2021',69.98 
8202,'07/26/2021',76.11 
8203,'12/27/2021',25.12 
8204,'06/06/2022',46.23 
8205,'07/18/2022',84.21 
8206,'11/14/2022',96.24 
8207,'12/12/2022',67.67 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_year

Results table

| date | in\_year |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | -1 |
| 02/03/2021 | -1 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 12/27/2021 | -1 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

The ‘`in_year`’ field is created in the preceding load statement by using the `inyear()` function. The first argument identifies which field is being evaluated. The second argument is a hard-coded date for July 26, 2021 which is the `base_date` that determines the comparator year. A `period_no` of `0` is the final argument meaning that the `inyear()` function does not compare years preceding or following the year.

Diagram of `inyear()` function's range with July 26 as the base date

![Diagram of the inyear() function with July 26 as the base date, and the range of time from January 1, 2021 to January 1, 2022 is highlighted.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyear-examples1_and4-diagram.png)

Any transaction that occurs in 2021 returns a Boolean result of TRUE.

## Example 2 - period\_no

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions between 2020 and 2022 which is loaded into a table called ‘`Transactions`’.
- A preceding load which contains the `inyear()` function that is set as the ‘`previous_year`’ field, and determines which transactions took place in the year before the year containing July 26, 2021.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
Transactions: 
    Load 
        *, 
        inyear(date,'07/26/2021', -1) as previous_year 
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
8193,'08/14/2020',82.06 
8194,'10/07/2020',40.39 
8195,'12/05/2020',87.21 
8196,'01/22/2021',95.93 
8197,'02/03/2021',45.89 
8198,'03/17/2021',36.23 
8199,'04/23/2021',25.66 
8200,'05/04/2021',82.77 
8201,'06/30/2021',69.98 
8202,'07/26/2021',76.11 
8203,'12/27/2021',25.12 
8204,'06/06/2022',46.23 
8205,'07/18/2022',84.21 
8206,'11/14/2022',96.24 
8207,'12/12/2022',67.67 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- previous\_year

Results table

| date | previous\_year |
| --- | --- |
| 01/13/2020 | -1 |
| 02/26/2020 | -1 |
| 03/27/2020 | -1 |
| 04/16/2020 | -1 |
| 05/21/2020 | -1 |
| 08/14/2020 | -1 |
| 10/07/2020 | -1 |
| 12/05/2020 | -1 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 12/27/2021 | 0 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

Using `-1` as the `period_no` argument in the `inyear()` function shifts the boundaries of the comparator year back by a full year. 2021 is initially identified as the comparator year. The `period_no` offsets the comparator year by one, making 2020 the comparator year.

Diagram of `inyear()` function's range with the period\_no argument set to `-1`

![Diagram of the inyear() function with July 26 as the base date, and the period_no argument set to negative one. The range of time from January 1, 2020 to January 1, 2021 is highlighted.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyear-example2-diagram.png)

Therefore, any transaction that occurs in 2020 returns a Boolean result of TRUE.

## Example 3 - first\_month\_of\_year

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions between 2020 and 2022 which is loaded into a table called ‘`Transactions`’.
- A preceding load which contains the `inyear()` function that is set as the ‘`in_year`’ field, and determines which transactions took place in the same year as July 26, 2021.

However, in this example, the organizational policy is for March to be the first month of the financial year.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
Transactions: 
    Load 
        *, 
        inyear(date,'07/26/2021', 0, 3) as in_year 
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
8193,'08/14/2020',82.06 
8194,'10/07/2020',40.39 
8195,'12/05/2020',87.21 
8196,'01/22/2021',95.93 
8197,'02/03/2021',45.89 
8198,'03/17/2021',36.23 
8199,'04/23/2021',25.66 
8200,'05/04/2021',82.77 
8201,'06/30/2021',69.98 
8202,'07/26/2021',76.11 
8203,'12/27/2021',25.12 
8204,'06/06/2022',46.23 
8205,'07/18/2022',84.21 
8206,'11/14/2022',96.24 
8207,'12/12/2022',67.67 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_year

Results table

| date | in\_year |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 12/27/2021 | -1 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

Using `3` as the `first_month_of_year` argument in the `inyear()` function begins the year on March 1 and ends the year at the end of February.

Diagram of `inyear()` function's range with March set as the first month of the year

![Diagram of the inyear() function with July 26 as the base date, and the first month of the year set as March. The range of time from March 1, 2021 to March 1, 2022 is highlighted.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyear-example3-diagram.png)

Therefore, any transaction that occurs between March 1, 2021 and March 1, 2022 will return a Boolean result of TRUE.

## Example 4 - Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. The calculation that determines whether transactions took place in the same year as July 26, 2021 is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm#glossary-4 "Glossary term") in a chart object of the application.

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
8193,'08/14/2020',82.06 
8194,'10/07/2020',40.39 
8195,'12/05/2020',87.21 
8196,'01/22/2021',95.93 
8197,'02/03/2021',45.89 
8198,'03/17/2021',36.23 
8199,'04/23/2021',25.66 
8200,'05/04/2021',82.77 
8201,'06/30/2021',69.98 
8202,'07/26/2021',76.11 
8203,'12/27/2021',25.12 
8204,'06/06/2022',46.23 
8205,'07/18/2022',84.21 
8206,'11/14/2022',96.24 
8207,'12/12/2022',67.67 
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `date`

To calculate whether transactions took place in the same year as July 26, 2021, create the following measure:

- `=inyear(date,'07/26/2021', 0)`

Results table

| date | =inyear(date,'07/26/2021',0) |
| --- | --- |
| 01/13/2020 | 0 |
| 02/26/2020 | 0 |
| 03/27/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | -1 |
| 02/03/2021 | -1 |
| 03/17/2021 | -1 |
| 04/23/2021 | -1 |
| 05/04/2021 | -1 |
| 06/30/2021 | -1 |
| 07/26/2021 | -1 |
| 12/27/2021 | -1 |
| 06/06/2022 | 0 |
| 07/18/2022 | 0 |
| 11/14/2022 | 0 |
| 12/12/2022 | 0 |

The ‘`in_year`’ field is created in the chart by using the `inyear()` function. The first argument identifies which field is being evaluated. The second argument is a hard-coded date for July 26, 2021 which is the `base_date` that determines the comparator year. A `period_no` of `0` is the final argument meaning that the `inyear()` function does not compare years preceding or following the year.

Diagram of `inyear()` function's range with July 27 as the base date

![Diagram of the inyear() function with July 27 as the base date, and the range of time from January 1, 2021 to January 1, 2022 highlighted.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inyear-examples1_and4-diagram.png)

Any transaction that occurs in 2021 returns a Boolean result of TRUE.

## Example 5 - Scenario

Load script and results 

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called ‘`Products`’.
- The table contains the following fields:

  - product ID
  - product type
  - manufacture date
  - cost price

The end user would like a chart object that displays, by product type, the cost of the products manufactured in 2021.

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

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `product_type`

To calculate the sum of each product that was manufactured in 2021, create the following measure:

- `=sum(if(InYear(manufacture_date,makedate(2021,01,01),0),cost_price,0))`

Do the following:

1. Set the measure’s **Number Formatting** to **Money**.
2. Under **Appearance**, turn off **Totals**.

Results table

| product\_type | =sum(if(InYear(manufacture\_date,makedate(2021,01,01),0),cost\_price,0)) |
| --- | --- |
| product A | $95.93 |
| product B | $128.66 |
| product C | $61.89 |
| product D | $171.21 |

The `inyear()` function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured in 2021, the `inyear()` function returns a Boolean value of TRUE and shows the sum of the `cost_price`.
