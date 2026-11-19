---
title: "month Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# month Script and chart function

This function returns a dual value: a month name as defined in the environment variable MonthNames and an integer between 1-12. The month is calculated from the date interpretation of the expression, according to the standard number interpretation.

The function returns the name of the month in the format of the `MonthName` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-0 "Glossary term") for a particular date. It is commonly used to create a day [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-1 "Glossary term") as a [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-2 "Glossary term") in a Master Calendar.

Syntax:

month(expression)

Return data type:  integer

Function examples

| Example | Result |
| --- | --- |
| `month( 2012-10-12 )` | returns Oct |
| `month( 35648 )` | returns Aug, because 35648 = 1997-08-06 |

## Example 1 – DateFormat dataset (script)

Load script and results

Overview

Open the Data load editor and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-3 "Glossary term") below to a new tab.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-4 "Glossary term") of dates named `Master_Calendar`. The `DateFormat` system variable is set to DD/MM/YYYY.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-5 "Glossary term") that creates an additional field, named`month_name`, using the `month()` function.
- An additional field, named`long_date`, using the `date()` function to express the full date.

Load script

```
SET DateFormat='DD/MM/YYYY';

Master_Calendar:
Load
        date,
        date(date,'dd-MMMM-YYYY') as long_date,
        month(date) as month_name
Inline 
[
date
03/01/2022
03/02/2022
03/03/2022
03/04/2022
03/05/2022
03/06/2022
03/07/2022
03/08/2022
03/09/2022
03/10/2022
03/11/2022
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `long_date`
- `month_name`

Results table

| date | long\_date | month\_name |
| --- | --- | --- |
| 03/01/2022 | 03-January- 2022 | Jan |
| 03/02/2022 | 03-February- 2022 | Feb |
| 03/03/2022 | 03-March- 2022 | Mar |
| 03/04/2022 | 03-April- 2022 | Apr |
| 03/05/2022 | 03-May- 2022 | May |
| 03/06/2022 | 03-June- 2022 | Jun |
| 03/07/2022 | 03-July- 2022 | Jul |
| 03/08/2022 | 03-August- 2022 | Aug |
| 03/09/2022 | 03-September- 2022 | Sep |
| 03/10/2022 | 03-October- 2022 | Oct |
| 03/11/2022 | 03-November- 2022 | Nov |

The month name is correctly evaluated by the `month()` function in the script.

## Example 2 – ANSI dates (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of dates named `Master_Calendar`. The DateFormat system variable DD/MM/YYYY is used. However, the dates that are included in the dataset are in ANSI standard date format.
- A preceding load that creates an additional field, named`month_name`, using the month() function.
- An additional field, named`long_date`, using the date() function to express the full date.

Load script

```
SET DateFormat='DD/MM/YYYY'; 
Master_Calendar: 
Load 
       date, 
       date(date,'dd-MMMM-YYYY') as long_date, 
       month(date) as month_name 

Inline  
[ 
date 
2022-01-11 
2022-02-12 
2022-03-13 
2022-04-14 
2022-05-15 
2022-06-16 
2022-07-17 
2022-08-18 
2022-09-19
2022-10-20 
2022-11-21 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `long_date`
- `month_name`

Results table

| date | long\_date | month\_name |
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

The month name is correctly evaluated by the `month()` function in the script.

## Example 3 – Unformatted dates (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of dates named `Master_Calendar`. The `DateFormat` system variable DD/MM/YYYY is used.
- A preceding load that creates an additional field, named `month_name`, using the `month()` function.
- The original unformatted date, named `unformatted_date`.
- An additional field, named `long_date`, using the `date()` function to express the full date.

Load script

```
SET DateFormat='DD/MM/YYYY'; 

Master_Calendar: 
Load 
      unformatted_date, 
      date(unformatted_date,'dd-MMMM-YYYY') as long_date, 
      month(unformatted_date) as month_name 

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
- `month_name`

Results table

| unformatted\_date | long\_date | month\_name |
| --- | --- | --- |
| 44868 | 03-January- 2022 | Jan |
| 44898 | 03-February- 2022 | Feb |
| 44928 | 03-March- 2022 | Mar |
| 44958 | 03-April- 2022 | Apr |
| 44988 | 03-May- 2022 | May |
| 45018 | 03-June- 2022 | Jun |
| 45048 | 03-July- 2022 | Jul |
| 45078 | 03-August- 2022 | Aug |
| 45008 | 03-September- 2022 | Sep |
| 45038 | 03-October- 2022 | Oct |
| 45068 | 03-November- 2022 | Nov |

The month name is correctly evaluated by the `month()` function in the script.

## Example 4 – Calculating expiry month

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- A dataset of orders placed in March named `Subscriptions`. The table contains three fields:

  - id
  - order\_date
  - amount

Load script

```
Subscriptions: 
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

Load the data and open a sheet. Create a new table and add this field as a dimension: `order_date`.

To calculate the month an order will expire, create this [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm#glossary-6 "Glossary term") `=month(order_date+180)`.

Results table

| order\_date | =month(order\_date+180) |
| --- | --- |
| 03/01/2022 | Jul |
| 03/02/2022 | Aug |
| 03/03/2022 | Aug |
| 03/04/2022 | Sep |
| 03/05/2022 | Oct |
| 03/06/2022 | Nov |
| 03/07/2022 | Dec |
| 03/08/2022 | Jan |
| 03/09/2022 | Mar |
| 03/10/2022 | Apr |
| 03/11/2022 | May |

The `month()` function correctly determines that an order placed on the 11th of March would expire in July.

## Learn more

- [*Loading data from a previously loaded table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm)
