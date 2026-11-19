---
title: "year Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---
Expand/Collapse all

# year Script and chart function

This function returns an integer representing the year when the
expression is interpreted as a date
according to the standard number interpretation.

Syntax:

year(expression)

Return data type:  integer

The `year()` function is available as both a script and [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-0 "Glossary term") function. The function returns the year for a particular date. It is commonly used to create a year [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-1 "Glossary term") as a [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-2 "Glossary term") in a Master Calendar.

## When to use year

The `year()` function is useful when you would like to compare aggregations by year. For example, the function could be used if you would like to see the total sales of products by year.

These dimensions can be created either in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-3 "Glossary term") by using the function to create a field in a Master Calendar table. Alternatively, it could be used directly in a chart as a calculated dimension.

Function examples

| Example | Result |
| --- | --- |
| `year( '2012-10-12' )` | returns 2012 |
| `year( '35648' )` | returns 1997, because 35648 = 1997-08-06 |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – DateFormat dataset (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-4 "Glossary term") of dates, which is loaded into a table named `Master Calendar`.
- The default `DateFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-5 "Glossary term") (MM/DD/YYYY) is used.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-6 "Glossary term") which is used to create an additional field, `year`, using the `year()` function.

Load script

```
SET DateFormat='MM/DD/YYYY';

Master_Calendar:

    Load
        date,
        year(date) as year
        ;
Load
date
Inline 
[
date
12/28/2020
12/29/2020
12/30/2020
12/31/2020
01/01/2021
01/02/2021
01/03/2021
01/04/2021
01/05/2021
01/06/2021
01/07/2021
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `year`

Results table

| date | year |
| --- | --- |
| 12/28/2020 | 2020 |
| 12/29/2020 | 2020 |
| 12/30/2020 | 2020 |
| 12/31/2020 | 2020 |
| 01/01/2021 | 2021 |
| 01/02/2021 | 2021 |
| 01/03/2021 | 2021 |
| 01/04/2021 | 2021 |
| 01/05/2021 | 2021 |
| 01/06/2021 | 2021 |
| 01/07/2021 | 2021 |

## Example 2 – ANSI Dates

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates, which is loaded into a table named `Master Calendar`.
- The default `DateFormat` system variable (MM/DD/YYYY) is used. However, the dates included in the dataset are in ANSI standard date format.
- A preceding load, which is used to create an additional field, named `year`, using the `year()` function.

Load script

```
SET DateFormat='MM/DD/YYYY';

Master_Calendar:
    Load
        date,
        year(date) as year
        ;
Load
date
Inline 
[
date
2020-12-28
2020-12-29
2020-12-30
2020-12-31
2021-01-01
2021-01-02
2021-01-03
2021-01-04
2021-01-05
2021-01-06
2021-01-07
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `year`

Results table

| date | year |
| --- | --- |
| 2020-12-28 | 2020 |
| 2020-12-29 | 2020 |
| 2020-12-30 | 2020 |
| 2020-12-31 | 2020 |
| 2021-01-01 | 2021 |
| 2021-01-02 | 2021 |
| 2021-01-03 | 2021 |
| 2021-01-04 | 2021 |
| 2021-01-05 | 2021 |
| 2021-01-06 | 2021 |
| 2021-01-07 | 2021 |

## Example 3 – Unformatted dates

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates in numerical format, which is loaded into a table named `Master Calendar`.
- The default `DateFormat` system variable (MM/DD/YYYY) is used.
- A preceding load, which is used to create an additional field, `year`, using the `year()` function.

The original unformatted date is loaded, named `unformatted_date`, and to provide clarity, a further additional field, named `long_date`, is used to convert the numerical date into a formatted date field using the `date()` function.

Load script

```
SET DateFormat='MM/DD/YYYY';

Master_Calendar:
    Load
        unformatted_date,
        date(unformatted_date) as long_date,
        year(unformatted_date) as year
        ;
Load
unformatted_date
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
- `year`

Results table

| unformatted\_date | long\_date | year |
| --- | --- | --- |
| 44868 | 11/03/2022 | 2022 |
| 44898 | 12/03/2022 | 2022 |
| 44928 | 01/02/2023 | 2023 |
| 44958 | 02/01/2023 | 2023 |
| 44988 | 03/03/2023 | 2023 |
| 45008 | 03/23/2023 | 2023 |
| 45018 | 04/02/2023 | 2023 |
| 45038 | 04/22/2023 | 2023 |
| 45048 | 05/02/2023 | 2023 |
| 45068 | 05/22/2023 | 2023 |
| 45078 | 06/01/2023 | 2023 |

## Example 4 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-7 "Glossary term") and add the load script below to a new tab.

In this example, a dataset of orders placed is loaded into a table named Sales. The table contains three fields:

- `id`
- `sales_date`
- `amount`

Warranties on product sales last two years from the date of sale. The task is to create a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm#glossary-8 "Glossary term") in a chart to determine the year in which each warranty will expire.

Load script

```
Sales:
Load
id,
sales_date,
amount
Inline 
[
id,sales_date,amount
1,12/28/2020,231.24,
2,12/29/2020,567.28,
3,12/30/2020,364.28,
4,12/31/2020,575.76,
5,01/01/2021,638.68,
6,01/02/2021,785.38,
7,01/03/2021,967.46,
8,01/04/2021,287.67
9,01/05/2021,764.45,
10,01/06/2021,875.43,
11,01/07/2021,957.35
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `sales_date`.

Create the following measure:

`=year(sales_date+365*2)`

Results table

| sales\_date | =year(sales\_date+365\*2) |
| --- | --- |
| 12/28/2020 | 2022 |
| 12/29/2020 | 2022 |
| 12/30/2020 | 2022 |
| 12/31/2020 | 2022 |
| 01/01/2021 | 2023 |
| 01/02/2021 | 2023 |
| 01/03/2021 | 2023 |
| 01/04/2021 | 2023 |
| 01/05/2021 | 2023 |
| 01/06/2021 | 2023 |
| 01/07/2021 | 2023 |

The results of this measure can be seen in the table above. To add two years to a date, multiply 365 by 2 and add the result to the sales date. Therefore, sales that took place in 2020 have an expiry year of 2022.
