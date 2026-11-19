---
title: "day Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# day Script and chart function

This function returns an integer
representing the day when the fraction of the expression
is interpreted as a date according to the standard number interpretation.

The function returns the day of the month for a particular date. It is commonly used to derive a day [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-0 "Glossary term") as part of a calendar [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-1 "Glossary term").

Syntax:

day(expression)

Return data type:  integer

Function examples

| Example | Result |
| --- | --- |
| `day( 1971-10-12 )` | returns 12 |
| `day( 35648 )` | returns 6, because 35648 = 1997-08-06 |

## Example 1 – DateFormat dataset (script)

Load script and results

Overview

Open the Data load editor and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-2 "Glossary term") below to a new tab.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-3 "Glossary term") of dates named `Master_Calendar`. The `DateFormat` system variable is set to DD/MM/YYYY.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-4 "Glossary term") that creates an additional field, named `day_of_month`, using the `day()` function.
- An additional field, named `long_date`, using the `date()` function to express the full month name.

Load script

```
SET DateFormat='DD/MM/YYYY';

Master_Calendar:
Load
        date,
        date(date,'dd-MMMM-YYYY') as long_date,
        day(date) as day_of_month
Inline 
[
date
03/11/2022
03/12/2022
03/13/2022
03/14/2022
03/15/2022
03/16/2022
03/17/2022
03/18/2022
03/19/2022
03/20/2022
03/21/2022						
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `long_date`
- `day_of_month`

Results table

| date | long\_date | day\_of\_month |
| --- | --- | --- |
| 03/11/2022 | 11-March- 2022 | 11 |
| 03/12/2022 | 12-March- 2022 | 12 |
| 03/13/2022 | 13-March- 2022 | 13 |
| 03/14/2022 | 14-March- 2022 | 14 |
| 03/15/2022 | 15-March- 2022 | 15 |
| 03/16/2022 | 16-March- 2022 | 16 |
| 03/17/2022 | 17-March- 2022 | 17 |
| 03/18/2022 | 18-March- 2022 | 18 |
| 03/19/2022 | 19-March- 2022 | 19 |
| 03/20/2022 | 20-March- 2022 | 20 |
| 03/21/2022 | 21-March- 2022 | 21 |

The day of the month is correctly evaluated by the `day()` function in the script.

## Example 2 – ANSI dates (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of dates named `Master_Calendar`. The DateFormat system variable DD/MM/YYYY is used. However, the dates that are included in the dataset are in ANSI standard date format.
- A preceding load that creates an additional field, named `day_of_month`, using the `date()` function.
- An additional field, named `long_date`, using the `date()` function to express the date with the full month name.

Load script

```
SET DateFormat='DD/MM/YYYY'; 
Master_Calendar: 
Load 
       date, 
       date(date,'dd-MMMM-YYYY') as long_date, 
       day(date) as day_of_month

Inline  
[ 
date 
2022-03-11
2022-03-12
2022-03-13
2022-03-14
2022-03-15
2022-03-16
2022-03-17
2022-03-18
2022-03-19
2022-03-20
2022-03-21
 ];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `long_date`
- `day_of_month`

Results table

| date | long\_date | day\_of\_month |
| --- | --- | --- |
| 03/11/2022 | 11-March- 2022 | 11 |
| 03/12/2022 | 12-March- 2022 | 12 |
| 03/13/2022 | 13-March- 2022 | 13 |
| 03/14/2022 | 14-March- 2022 | 14 |
| 03/15/2022 | 15-March- 2022 | 15 |
| 03/16/2022 | 16-March- 2022 | 16 |
| 03/17/2022 | 17-March- 2022 | 17 |
| 03/18/2022 | 18-March- 2022 | 18 |
| 03/19/2022 | 19-March- 2022 | 19 |
| 03/20/2022 | 20-March- 2022 | 20 |
| 03/21/2022 | 21-March- 2022 | 21 |

The day of the month is correctly evaluated by the `day()` function in the script.

## Example 3 – Unformatted dates (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of dates named `Master_Calendar`. The `DateFormat` system variable DD/MM/YYYY is used.
- A preceding load that creates an additional field, named `day_of_month`, using the `day()` function.
- The original unformatted date, named `unformatted_date`.
- An additional field, named `long_date`, using the `date()` is used to convert the numerical date into a formatted date field.

Load script

```
SET DateFormat='DD/MM/YYYY'; 

Master_Calendar: 
Load 
      unformatted_date, 
      date(unformatted_date,'dd-MMMM-YYYY') as long_date, 
      day(date) as day_of_month

Inline
[ 
unformatted_date 
44868 
44898 
44928 
44958 
44988 
45018 
45048 
45078 
45008 
45038 
45068 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `unformatted_date`
- `long_date`
- `day_of_month`

Results table

| unformatted\_date | long\_date | day\_of\_month |
| --- | --- | --- |
| 44868 | 03-November- 2022 | 3 |
| 44898 | 03-December- 2022 | 3 |
| 44928 | 02-January- 2023 | 2 |
| 44958 | 01-February- 2023 | 1 |
| 44988 | 03-March- 2023 | 3 |
| 45008 | 23-March- 2023 | 23 |
| 45018 | 02-April- 2023 | 2 |
| 45038 | 22-April- 2023 | 22 |
| 45048 | 02-May- 2023 | 2 |
| 45068 | 22-May- 2023 | 22 |
| 45078 | 01-June- 2023 | 1 |

The day of the month is correctly evaluated by the `day()` function in the script.

## Example 4 – Calculating expiry month (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of orders placed in March named `Orders`. The table contains three fields:

  - id
  - order\_date
  - amount

Load script

```
Orders: 
Load 
	 id, 
	 order_date, 
	 amount 
Inline  
[ 
id,order_date,amount 
1,03/01/2022,231.24 
2,03/02/2022,567.28 
3,03/03/2022,364.28 
4,03/04/2022,575.76 
5,03/05/2022,638.68 
6,03/06/2022,785.38 
7,03/07/2022,967.46 
8,03/08/2022,287.67 
9,03/09/2022,764.45 
10,03/10/2022,875.43 
11,03/11/2022,957.35 
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`order_date`.

To calculate the delivery date, create this [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm#glossary-5 "Glossary term") `=day(order_date+5)`.

Results table

| order\_date | =day(order\_date+5) |
| --- | --- |
| 03/11/2022 | 16 |
| 03/12/2022 | 17 |
| 03/13/2022 | 18 |
| 03/14/2022 | 19 |
| 03/15/2022 | 20 |
| 03/16/2022 | 21 |
| 03/17/2022 | 22 |
| 03/18/2022 | 23 |
| 03/19/2022 | 24 |
| 03/20/2022 | 25 |
| 03/21/2022 | 26 |

The `day()` function correctly determines that an order placed on the 11th of March would be delivered on the 16th based on a 5 day delivery period.

## Learn more

- [*Loading data from a previously loaded table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm)
