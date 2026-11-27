---
title: "daynumberofyear Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofyear.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# daynumberofyear Script and chart function

Expand/Collapse all

# daynumberofyear Script and chart function

This function calculates
the day number of the year in which a timestamp falls. The calculation is made from the first millisecond
of the first day of the year, but the first month can be offset.

Syntax:

DayNumberOfYear(timestamp[,start\_month])

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
| DayNumberOfYear( '12/09/2014' ) | Returns 256, the day number counted from the first of the year. |
| DayNumberOfYear( '12/09/2014',3 ) | Returns 196, the number of the day, as counted from 1 March. |

## Example 1 – January start of year (script)

Load script and results

Overview

Open the Data load editor and add the [load script](#glossary-0 "Glossary term") below to a new tab.

The load script contains:

- A simple [dataset](#glossary-1 "Glossary term") containing a list of dates, which is loaded into a table named Calendar. The default DateFormat system variable MM/DD/YYYY is used.
- A [preceding load](#glossary-2 "Glossary term") that creates an additional [field](#glossary-3 "Glossary term") named daynryear, using the DayNumberOfYear() function.

Aside from the date, no additional parameters are provided to the function.

Load script

```
SET DateFormat='MM/DD/YYYY';

Calendar:
Load
	date,
	DayNumberOfYear(date) as daynryear
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
06/30/2022
07/26/2022
10/31/2022
11/01/2022
12/31/2022
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- daynryear

Results table

| date | daynryear |
| --- | --- |
| 01/01/2022 | 1 |
| 01/10/2022 | 10 |
| 01/31/2022 | 31 |
| 02/01/2022 | 32 |
| 02/10/2022 | 41 |
| 06/30/2022 | 182 |
| 07/26/2022 | 208 |
| 10/31/2022 | 305 |
| 11/01/2022 | 306 |
| 12/31/2022 | 366 |

The first day of the year is the 1st of January because no second argument was passed into the DayNumberOfYear() function.

January 1st is the 1st day of the quarter whilst February 1st is the 32nd day of the year. The 30th of June is the 182nd whilst the 31st of December is the 366th and final day of the year.

## Example 2 – November start of year (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default DateFormat system variable MM/DD/YYYY is used
- A start\_month argument beginning on November 1. This sets the financial year to November 1.

Load script

```
SET DateFormat='MM/DD/YYYY';

Calendar:
Load
	date,
	DayNumberOfYear(date,11) as daynryear
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
06/30/2022
07/26/2022
10/31/2022
11/01/2022
12/31/2022
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- daynryear

Results table

| date | daynryear |
| --- | --- |
| 01/01/2022 | 62 |
| 01/10/2022 | 71 |
| 01/31/2022 | 92 |
| 02/01/2022 | 93 |
| 02/10/2022 | 102 |
| 06/30/2022 | 243 |
| 07/26/2022 | 269 |
| 10/31/2022 | 366 |
| 11/01/2022 | 1 |
| 12/31/2022 | 61 |

The first day of the year is the 1st of November because the second argument passed into the DayNumberOfYear() function was 11.

January 1st is the 1st day of the quarter whilst February 1st is the 32nd day of the year. The 30th of June is the 182nd whilst the 31st of December is the 366th and final day of the year.

## Example 3 – January start of year (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default DateFormat system variable MM/DD/YYYY is used.

However, in this example, the unchanged dataset is loaded into the application. The value of the day of the quarter is calculated via a [measure](#glossary-4 "Glossary term") in a chart object.

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
06/30/2022
07/26/2022
10/31/2022
11/01/2022
12/31/2022
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

Create the following measure:

=daynumberofyear(date)

Results table

| date | =daynumberofyear(date) |
| --- | --- |
| 01/01/2022 | 1 |
| 01/10/2022 | 10 |
| 01/31/2022 | 31 |
| 02/01/2022 | 32 |
| 02/10/2022 | 41 |
| 06/30/2022 | 182 |
| 07/26/2022 | 208 |
| 10/31/2022 | 305 |
| 11/01/2022 | 306 |
| 12/31/2022 | 366 |

The first day of the year is the 1st of January because no second argument was passed into the DayNumberOfYear() function.

January 1st is the 1st day of the year whilst February 1st is the 32nd day of the year. The 30th of June is the 182nd whilst the 31st of December is the 366th and final day of the year.

## Example 4 – November start of year (chart)

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The load script contains:

- The same dataset from the first example.
- The default DateFormat system variable MM/DD/YYYY is used.
- The financial year runs from the 1st of November to the 31st of October.

However, in this example, the unchanged dataset is loaded into the application. The value of the day of the year is calculated via a measure in a chart object.

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
06/30/2022
07/26/2022
10/31/2022
11/01/2022
12/31/2022
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

Create the following measure:

=daynumberofyear(date)

Results table

| date | =daynumberofyear(date,11) |
| --- | --- |
| 01/01/2022 | 62 |
| 01/10/2022 | 71 |
| 01/31/2022 | 92 |
| 02/01/2022 | 93 |
| 02/10/2022 | 102 |
| 06/30/2022 | 243 |
| 07/26/2022 | 269 |
| 10/31/2022 | 366 |
| 11/01/2022 | 1 |
| 12/31/2022 | 61 |

The first day of the year is the 1st of November because the second argument passed into the DayNumberOfYear() function was 11.

The financial year operates between November and October. This is shown in the results table where November 1st is the 1st day of the year whilst October 31st is the 366th and last day of the year.
