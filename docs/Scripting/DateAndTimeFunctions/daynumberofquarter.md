---
title: "daynumberofquarter Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# daynumberofquarter Script and chart function

This function calculates
the day number of the quarter in which a timestamp falls. This function is used when creating a Master Calendar.

Syntax:

DayNumberOfQuarter(timestamp[,start\_month])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| start\_month | By specifying a start\_month between 2 and 12 (1, if omitted), the beginning of the year may be moved forward to the first day of any month. For example, if you want to work with a fiscal year starting March 1, specify start\_month = 3. |

These examples use the date format DD/MM/YYYY. The date format is specified in the SET DateFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| `DayNumberOfQuarter('12/09/2014')` | Returns 74, the day number of the current quarter. |
| `DayNumberOfQuarter('12/09/2014',3)` | Returns 12, the day number of the current quarter.  In this case, the first quarter starts with March (because start\_month is specified as 3). This means that the current quarter is the third quarter, which started on September 1. |

## Example 1 – January start of year (script)

Load script and results

Overview

Open the Data load editor and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm#glossary-0 "Glossary term") below to a new tab.

The load script contains:

- A simple [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm#glossary-1 "Glossary term") containing a list of dates, which is loaded into a table named `Calendar`. The default `DateFormat` system variable MM/DD/YYYY is used.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm#glossary-2 "Glossary term") that creates an additional [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm#glossary-3 "Glossary term") named `DayNrQtr`, using the `DayNumberOfQuarter()` function.

Aside from the date, no additional parameters are provided to the function.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
 
Calendar: 
Load 
        date, 
        DayNumberOfQuarter(date) as DayNrQtr 
        ; 
Load 
date 
Inline  
[	 
date 
01/01/2022 
01/10/2022 
01/31/2022 
02/01/2022 
02/10/2022 
02/28/2022 
03/01/2022 
03/31/2022 
04/01/2022 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `daynrqtr`

Results table

| date | daynrqtr |
| --- | --- |
| 01/01/2022 | 1 |
| 01/10/2022 | 10 |
| 01/31/2022 | 31 |
| 02/01/2022 | 32 |
| 02/10/2022 | 41 |
| 02/28/2022 | 59 |
| 03/01/2022 | 61 |
| 03/31/2022 | 91 |
| 04/01/2022 | 1 |

The first day of the year is January 1 because no second argument was passed into the `DayNumberOfQuarter()` function.

January 1st is the 1st day of the quarter whilst February 1st is the 32nd day of the quarter. The 31st of March is the 91st and final day of the quarter, whilst the 1st of April is the 1st day of the 2nd Quarter.

## Example 2 – February start of year (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default `DateFormat` system variable MM/DD/YYYY is used.
- A `start_month` argument beginning on February 1. This sets the financial year to February 1.

Load script

```
SET DateFormat='MM/DD/YYYY'; 
					
Calendar:
Load
	date,
	DayNumberOfQuarter(date,2) as DayNrQtr
	;
Load
date
Inline
[
date
01/01/2022
01/10/2022
01/31/2022
02/01/2022
02/10/2022
02/28/2022
03/01/2022
03/31/2022
04/01/2022
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `daynrqtr`

Results table

| date | daynrqtr |
| --- | --- |
| 01/01/2022 | 62 |
| 01/10/2022 | 71 |
| 01/31/2022 | 92 |
| 02/01/2022 | 1 |
| 02/10/2022 | 10 |
| 02/28/2022 | 28 |
| 03/01/2022 | 30 |
| 03/31/2022 | 60 |
| 04/01/2022 | 61 |

The first day of the year is the 1st of February because the second argument passed into the `DayNumberOfQuarter()` function was 2.

The first quarter of the year operates between February and April whilst the fourth quarter operates between November and January. This is shown in the results table where February 1st is the 1st day of the quarter whilst January 31st is the 92nd and last day of the quarter.

## Example 3 – January start of year (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default `DateFormat` system variable MM/DD/YYYY is used.

However, in this example, the unchanged dataset is loaded into the application. The value of the day of the quarter is calculated via a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm#glossary-4 "Glossary term") in a chart object.

Load script

```
SET DateFormat='MM/DD/YYYY';
						
Calendar:
Load
date
Inline
[
date
01/01/2022
01/10/2022
01/31/2022
02/01/2022
02/10/2022
02/28/2022
03/01/2022
03/31/2022
04/01/2022
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Create the following measure:

=daynumberofquarter(date)

Results table

| date | =daynumberofquarter(date) |
| --- | --- |
| 01/01/2022 | 1 |
| 01/10/2022 | 10 |
| 01/31/2022 | 31 |
| 02/01/2022 | 32 |
| 02/10/2022 | 41 |
| 02/28/2022 | 59 |
| 03/01/2022 | 61 |
| 03/31/2022 | 91 |
| 04/01/2022 | 1 |

The first day of the year is the 1st of January because no second argument passed into the `DayNumberOfQuarter()` function.

January 1st is the 1st day of the quarter whilst February 1st is the 32nd day of the quarter. The 31st of March is the 91st and final day of the quarter, whilst the 1st of April is the 1st day of the 2nd Quarter.

## Example 4 – February start of year (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default `DateFormat` system variable MM/DD/YYYY is used.
- The financial year runs from the 1st of February to the 31st of January.

However, in this example, the unchanged dataset is loaded into the application. The value of the day of the quarter is calculated via a measure in a chart object.

Load script

```
SET DateFormat='MM/DD/YYYY';
						
Calendar:
Load
date
Inline
[
date
01/01/2022
01/10/2022
01/31/2022
02/01/2022
02/10/2022
02/28/2022
03/01/2022
03/31/2022
04/01/2022
];
```

Chart object

Load the data and open a sheet. Create a new table and add this field as a dimension: `date`.

Create the following measure:

=daynumberofquarter(date,2)

Results

Results table

| date | =daynumberofquarter(date,2) |
| --- | --- |
| 01/01/2022 | 62 |
| 01/10/2022 | 71 |
| 01/31/2022 | 92 |
| 02/01/2022 | 1 |
| 02/10/2022 | 10 |
| 02/28/2022 | 28 |
| 03/01/2022 | 30 |
| 03/31/2022 | 60 |
| 04/01/2022 | 61 |

The first day of the year is the 1st of January because the second argument passed into the `DayNumberOfQuarter()` function was 2.

The first quarter of the year operates between February and April whilst the fourth quarter operates between November and January. This is evidenced in the results table where February 1st is the 1st day of the quarter whilst January 31st is the 92nd and last day of the quarter.
