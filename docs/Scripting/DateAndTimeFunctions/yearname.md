---
title: "yearname Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# yearname Script and chart function

This function returns
a four-digit year as display value with an underlying numeric value corresponding
to a timestamp of the first millisecond of the first day of the year
containing
date.

Diagram of range of time of the `yearname()` function.

![Diagram that shows the range of time in which the yearname function will return a result.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-diagram1.png)

The `yearname()` function is different to the `year()` function as it lets you offset the date you want evaluated and lets you set the first month of the year.

If the first month of the year is not January, the function will return the two four-digit years across the twelve month period that contain the date. For example, if the start of the year is April and the date being evaluated is 06/30/2020, the result returned would be `2020-2021`.

Diagram of `yearname()` function with April set as the first month of the year.

![Diagram that shows that the yearname function can identify dates within a twelve month period and that its return can depend on which month is set as the first month of the year.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-diagram2.png)

Syntax:

YearName(date[, period\_no[, first\_month\_of\_year]] )

Return data type:  dual

| Argument | Description |
| --- | --- |
| date | The date or timestamp to evaluate. |
| period\_no | period\_no is an integer, where the value 0 indicates the year which contains date. Negative values in period\_no indicate preceding years and positive values indicate succeeding years. |
| first\_month\_of\_year | If you want to work with (fiscal) years not starting in January, indicate a value between 2 and 12 in first\_month\_of\_year. The display value will then be a string showing two years. |

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

When to use yearname

The `yearname()` function is useful for comparing aggregations by year. For example, if you want to see the total sales of products by year.

These [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-0 "Glossary term") can be created in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-1 "Glossary term") by using the function to create a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-2 "Glossary term") in a Master Calendar table. They can also be created in a [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-3 "Glossary term") as calculated dimensions

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `yearname('10/19/2001')` | Returns '2001.' |
| `yearname('10/19/2001',-1)` | Returns '2000.' |
| `yearname('10/19/2001',0,4)` | Returns '2001-2002.' |

Related topics

| Topic | Description |
| --- | --- |
| [*year Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm) | This function returns an integer representing the year when the expression is interpreted as a date according to the standard number interpretation. |

## Example 1 – No additional arguments

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-4 "Glossary term") containing a set of transactions between 2020 and 2022 is loaded into a table called ‘`Transactions`’.
- The `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-5 "Glossary term") which is set to ‘`MM/DD/YYYY`’.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-6 "Glossary term") that uses the `yearname()` and which is set as the `year_name` field.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
						
Transactions: 
    Load 
      *, 
      yearname(date) as year_name 
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
- year\_name

Results table

| date | year\_name |
| --- | --- |
| 01/13/2020 | 2020 |
| 02/26/2020 | 2020 |
| 03/27/2020 | 2020 |
| 04/16/2020 | 2020 |
| 05/21/2020 | 2020 |
| 08/14/2020 | 2020 |
| 10/07/2020 | 2020 |
| 12/05/2020 | 2020 |
| 01/22/2021 | 2021 |
| 02/03/2021 | 2021 |
| 03/17/2021 | 2021 |
| 04/23/2021 | 2021 |
| 05/04/2021 | 2021 |
| 06/30/2021 | 2021 |
| 07/26/2021 | 2021 |
| 12/27/2021 | 2021 |
| 06/06/2022 | 2022 |
| 07/18/2022 | 2022 |
| 11/14/2022 | 2022 |
| 12/12/2022 | 2022 |

The ‘`year_name`’ field is created in the preceding load statement by using the `yearname()` function and passing the date field as the function’s argument.

The `yearname()` function identifies which year the date value falls into and returns this as a four-digit year value.

Diagram of `yearname()` function that shows 2021 as the year value.

![Diagram that shows the yearname() function returns 2021 for the date of March 17, 2021.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-example1-diagram.png)

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions between 2020 and 2022 is loaded into a table called ‘Transactions’.
- The DateFormat system variable which is set to ‘`MM/DD/YYYY`’.
- A preceding load that uses the `yearname()` and which is set as the `year_name` field.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Transactions: 
    Load 
      *, 
      yearname(date,-1) as prior_year_name 
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
- prior\_year\_name

Results table

| date | prior\_year\_name |
| --- | --- |
| 01/13/2020 | 2019 |
| 02/26/2020 | 2019 |
| 03/27/2020 | 2019 |
| 04/16/2020 | 2019 |
| 05/21/2020 | 2019 |
| 08/14/2020 | 2019 |
| 10/07/2020 | 2019 |
| 12/05/2020 | 2019 |
| 01/22/2021 | 2020 |
| 02/03/2021 | 2020 |
| 03/17/2021 | 2020 |
| 04/23/2021 | 2020 |
| 05/04/2021 | 2020 |
| 06/30/2021 | 2020 |
| 07/26/2021 | 2020 |
| 12/27/2021 | 2020 |
| 06/06/2022 | 2021 |
| 07/18/2022 | 2021 |
| 11/14/2022 | 2021 |
| 12/12/2022 | 2021 |

Because a `period_no` of `-1` is used as the offset argument in the `yearname()` function, the function first identifies the year that the transactions take place in. The function then shifts one year prior and returns the resulting year.

Diagram of `yearname()` function with the `period_no` set `-1`.

![Diagram that shows how a period_no of negative one changes the ranges of time that the yearname() function identifies.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-example2-diagram.png)

## Example 3 – first\_month\_of\_year

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset from the first example.
- The `DateFormat` system variable which is set to ‘`MM/DD/YYYY`’.
- A preceding load that uses the `yearname()` and which is set as the `year_name` field.

Load script

```
SET DateFormat='MM/DD/YYYY'; 

Transactions: 
    Load 
      *, 
      yearname(date,0,4) as year_name 
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

- id
- date
- year\_name

Results table

| date | year\_name |
| --- | --- |
| 01/13/2020 | 2019-2020 |
| 02/26/2020 | 2019-2020 |
| 03/27/2020 | 2019-2020 |
| 04/16/2020 | 2020-2021 |
| 05/21/2020 | 2020-2021 |
| 08/14/2020 | 2020-2021 |
| 10/07/2020 | 2020-2021 |
| 12/05/2020 | 2020-2021 |
| 01/22/2021 | 2020-2021 |
| 02/03/2021 | 2020-2021 |
| 03/17/2021 | 2020-2021 |
| 04/23/2021 | 2021-2022 |
| 05/04/2021 | 2021-2022 |
| 06/30/2021 | 2021-2022 |
| 07/26/2021 | 2021-2022 |
| 12/27/2021 | 2021-2022 |
| 06/06/2022 | 2022-2023 |
| 07/18/2022 | 2022-2023 |
| 11/14/2022 | 2022-2023 |
| 12/12/2022 | 2022-2023 |

Because the `first_month_of_year` argument of `4` is used in the `yearname()` function, the start of the year moves from January 1 to April 1. Therefore, each twelve month period crosses two calendar years and the `yearname()` function returns the two four-digit years for dates evaluated.

Transaction 8198 takes place on March 17, 2021. The `yearname()` function sets the beginning of the year on April 1 and the ending on March 30. Therefore, transaction 8198 occurred in the year period from April 1, 2020 and March 30, 2021. As a result, the `yearname()` function returns the value 2020-2021.

Diagram of `yearname()` function with March set as the first month of the year.

![Diagram showing the range of time the yearname() function identifies when the first month of the year is set as March/](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-example3-diagram.png)

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset from the first example.
- The `DateFormat` system variable which is set to ‘`MM/DD/YYYY`’.

However, the field that returns the year that the transaction took place in is created as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-7 "Glossary term") in a chart object.

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

date

To calculate the ‘`year_name`’ field, create this measure:

=yearname(date)

Results table

| date | =yearname(date) |
| --- | --- |
| 01/13/2020 | 2020 |
| 02/26/2020 | 2020 |
| 03/27/2020 | 2020 |
| 04/16/2020 | 2020 |
| 05/21/2020 | 2020 |
| 08/14/2020 | 2020 |
| 10/07/2020 | 2020 |
| 12/05/2020 | 2020 |
| 01/22/2021 | 2021 |
| 02/03/2021 | 2021 |
| 03/17/2021 | 2021 |
| 04/23/2021 | 2021 |
| 05/04/2021 | 2021 |
| 06/30/2021 | 2021 |
| 07/26/2021 | 2021 |
| 12/27/2021 | 2021 |
| 06/06/2022 | 2022 |
| 07/18/2022 | 2022 |
| 11/14/2022 | 2022 |
| 12/12/2022 | 2022 |

The ‘`year_name`’ measure is created in the chart object using the `yearname()` function and passing the date field as the function’s argument.

The `yearname()` function identifies which year the date value falls into and returns this as a four-digit year value.

Diagram of `yearname()` function with 2021 as the year value.

![Diagram that shows the yearname() function return 2021 as the year value.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-yearname-example4-diagram.png)

## Example 5 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset from the first example.
- The `DateFormat` system variable which is set to ‘`MM/DD/YYYY`’.

The end user would like a chart that presents the total sales by quarter for the transactions. Use the `yearname()` function as a calculated [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-8 "Glossary term") to create this chart when the `yearname()` dimension is not available in the data model.

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

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm#glossary-9 "Glossary term"). Create a new table.

To compare aggregations by year, create this calculated dimension:

`=yearname(date)`

Create this measure:

`=sum(amount)`

Set the measure’s **Number Formatting** to **Money**.

Results table

| yearname(date) | =sum(amount) |
| --- | --- |
| 2020 | $463.55 |
| 2021 | $457.69 |
| 2022 | $294.35 |
