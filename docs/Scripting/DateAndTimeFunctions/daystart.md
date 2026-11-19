---
title: "daystart Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "measure"]
---
Expand/Collapse all

# daystart Script and chart function

This function returns
a value corresponding to a timestamp with the first millisecond of the
day contained in the time argument. The
default output format will be the TimestampFormat
set in the script.

Syntax:

DayStart(time[, [period\_no[, day\_start]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| time | The timestamp to evaluate. |
| period\_no | period\_no is an integer, or expression that resolves to an integer, where the value 0 indicates the day that contains time. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | To specify that days do not starting at midnight, indicate an offset as a fraction of a day in day\_start. For example, 0.125 to denote 3:00 AM. In other words, to create the offset, divide the start time by 24 hours. For example, for a day to begin at 7:00 AM, use the fraction 7/24. |

## When to use daystart

The `daystart()` function is commonly used as part of an expression when the user would like the calculation to use the fraction of the day that has elapsed thus far. For example, it could be used to calculate the total wages earned by employees in the day so far.

These examples use the timestamp format `'M/D/YYYY h:mm:ss[.fff] TT'`. The timestamp format is specified in the `SET TimeStamp` statement at the top of your data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-0 "Glossary term"). Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| `daystart('01/25/2013 4:45:00 PM')` | Returns 1/25/2013 12:00:00 AM. |
| `daystart('1/25/2013 4:45:00 PM', -1)` | Returns 1/24/2013 12:00:00 AM. |
| `daystart('1/25/2013 16:45:00',0,0.5 )` | Returns 1/25/2013 12:00:00 PM. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 - Simple example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A simple [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-1 "Glossary term") containing a list of dates, which is loaded into a table named `Calendar`.
- The default `TimeStampFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-2 "Glossary term") `(M/D/YYYY h:mm:ss[.fff] TT`) is used.
- A [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-3 "Glossary term") which creates an additional [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-4 "Glossary term") named `SOD_timestamp`, using the `daystart()` function.

Aside from the date, no additional parameters are provided to the function.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Calendar:
    Load
        date,
        daystart(date) as SOD_timestamp
        ;
Load
date
Inline 
[
date
03/11/2022 1:47:15 AM
03/12/2022 4:34:58 AM
03/13/2022 5:15:55 AM
03/14/2022 9:25:14 AM
03/15/2022 10:06:54 AM
03/16/2022 10:44:42 AM
03/17/2022 11:33:30 AM
03/18/2022 12:58:14 PM
03/19/2022 4:23:12 PM
03/20/2022 6:42:15 PM
03/21/2022 7:41:16 PM
];
					
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `date`
- `SOD_timestamp`

Results table

| date | SOD\_timestamp |
| --- | --- |
| 03/11/2022 1:47:15 AM | 3/11/2022 12:00:00 AM |
| 03/12/2022 4:34:58 AM | 3/12/2022 12:00:00 AM |
| 03/13/2022 5:15:55 AM | 3/13/2022 12:00:00 AM |
| 03/14/2022 9:25:14 AM | 3/14/2022 12:00:00 AM |
| 03/15/2022 10:06:54 AM | 3/15/2022 12:00:00 AM |
| 03/16/2022 10:44:42 AM | 3/16/2022 12:00:00 AM |
| 03/17/2022 11:33:30 AM | 3/17/2022 12:00:00 AM |
| 03/18/2022 12:58:14 PM | 3/18/2022 12:00:00 AM |
| 03/19/2022 4:23:12 PM | 3/19/2022 12:00:00 AM |
| 03/20/2022 6:42:15 PM | 3/20/2022 12:00:00 AM |
| 03/21/2022 7:41:16 PM | 3/21/2022 12:00:00 AM |

As can be seen in the table above, the end of day timestamp is generated for each date in our dataset. The timestamp is in the format of the system variable `TimestampFormat M/D/YYYY h:mm:ss[.fff] TT`.

## Example 2 - period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing parking fines, which is loaded into a table named `Fines`. The dataset includes the following fields:

  - `id`
  - `due_date`
  - `number_plate`
  - `amount`
- A preceding load using the `daystart()` function and supplying all three parameters: `time`, `period_no`, and `day_start`. This preceding load creates the following two new date fields:

  - An `early_repayment_period` date field, beginning seven days before the payment is due.
  - A `late_penalty_period` date field, beginning 14 days after the payment is due.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Fines:
    Load
        *,
        daystart(due_date,-7) as early_repayment_period,
        daystart(due_date,14) as late_penalty_period
        ;
Load
*
Inline
[
id, due_date, number_plate,amount
1,02/11/2022, 573RJG,50.00
2,03/25/2022, SC41854,50.00
3,04/14/2022, 8EHZ378,50.00
4,06/28/2022, 8HSS198,50.00
5,08/15/2022, 1221665,50.00
6,11/16/2022, EAK473,50.00
7,01/17/2023, KD6822,50.00
8,03/22/2023, 1GGLB,50.00
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `due_date`
- `early_repayment_period`
- `late_penalty_period`

Results table

| due\_date | early\_repayment\_period | late\_penalty\_period |
| --- | --- | --- |
| 02/11/2022 9:25:14 AM | 2/4/2022 12:00:00 AM | 2/25/2022 12:00:00 AM |
| 03/25/2022 10:06:54 AM | 3/18/2022 12:00:00 AM | 4/8/2022 12:00:00 AM |
| 04/14/2022 10:44:42 AM | 4/7/2022 12:00:00 AM | 4/28/2022 12:00:00 AM |
| 06/28/2022 11:33:30 AM | 6/21/2022 12:00:00 AM | 7/12/2022 12:00:00 AM |
| 08/15/2022 12:58:14 PM | 8/8/2022 12:00:00 AM | 8/29/2022 12:00:00 AM |
| 11/16/2022 4:23:12 PM | 11/9/2022 12:00:00 AM | 11/30/2022 12:00:00 AM |
| 01/17/2023 6:42:15 PM | 1/10/2023 12:00:00 AM | 1/31/2023 12:00:00 AM |
| 03/22/2023 7:41:16 PM | 3/15/2023 12:00:00 AM | 4/5/2023 12:00:00 AM |

The values of the new fields are in the `TimestampFormat M/DD/YYYY tt`. Because the function `daystart()` was used, the timestamp values are all the first millisecond of the day.

The early repayment period values are seven days before the due date, as a result of the second argument being passed in the `daystart()` function being negative.

The late repayment period values are 14 days after the due date, as a result of the second argument being passed in the `daystart()` function being positive.

## Example 3 - day\_start

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the previous example.
- The same preceding load as the previous example.

In this example, we set the working day to begin and end at 7:00 AM each day.

Load script

```
SET DateFormat='MM/DD/YYYY';

Fines:
    Load
        *,
        daystart(due_date,-7,7/24) as early_repayment_period,	 
        daystart(due_date,14, 7/24) as late_penalty_period
        ;
Load
*
Inline
[
id, due_date, number_plate,amount
1,02/11/2022, 573RJG,50.00
2,03/25/2022, SC41854,50.00
3,04/14/2022, 8EHZ378,50.00
4,06/28/2022, 8HSS198,50.00
5,08/15/2022, 1221665,50.00
6,11/16/2022, EAK473,50.00
7,01/17/2023, KD6822,50.00
8,03/22/2023, 1GGLB,50.00
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `due_date`
- `early_repayment_period`
- `late_penalty_period`

Results table

| due\_date | early\_repayment\_period | late\_penalty\_period |
| --- | --- | --- |
| 02/11/2022 | 2/3/2022 7:00:00 AM | 2/24/2022 7:00:00 AM |
| 03/25/2022 | 3/17/2022 7:00:00 AM | 4/7/2022 7:00:00 AM |
| 04/14/2022 | 4/6/2022 7:00:00 AM | 4/27/2022 7:00:00 AM |
| 06/28/2022 | 6/20/2022 7:00:00 AM | 7/11/2022 7:00:00 AM |
| 08/15/2022 | 8/7/2022 7:00:00 AM | 8/28/2022 7:00:00 AM |
| 11/16/2022 | 11/8/2022 7:00:00 AM | 11/29/2022 7:00:00 AM |
| 01/17/2023 | 1/9/2023 7:00:00 AM | 1/30/2023 7:00:00 AM |
| 03/22/2023 | 3/14/2023 7:00:00 AM | 4/4/2023 7:00:00 AM |

The dates now have a timestamp of 7:00 AM because the value of the `day_start` argument which was passed into the `daystart()` function was 7/24. This sets the beginning of the day to 7:00 AM.

Because the `due_date` field does not have a timestamp, it is treated as 12:00 AM, which is thus still part of the previous day, since the days start and end at 7:00 AM. Therefore, the early repayment period for a fine due on February 11 begins on February 3 at 7:00 AM.

## Example 4 - Chart object example

Load script and chart expression

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-5 "Glossary term") and add the load script below to a new tab.

This example uses the same dataset and scenario as the previous example.

However, only the original `Fines` table is loaded into the application, with the two additional due dates values being calculated in a chart object.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Fines:
    Load
*
Inline 
[
id, due_date, numer_plate,amount
1,02/11/2022 9:25:14 AM, 573RJG,50.00
2,03/25/2022 10:06:54 AM, SC41854,50.00
3,04/14/2022 10:44:42 AM, 8EHZ378,50.00
4,06/28/2022 11:33:30 AM, 8HSS198,50.00
5,08/15/2022 12:58:14 PM, 1221665,50.00
6,11/16/2022 4:23:12 PM, EAK473,50.00
7,01/17/2023 6:42:15 PM, KD6822,50.00
8,03/22/2023 7:41:16 PM, 1GGLB,50.00
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add this field as a dimension: `due_date`.
2. To create the `early_repayment_period` field, create the following [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm#glossary-6 "Glossary term").

   `=daystart(due_date,-7,7/24)`
3. To create the `late_penalty_period` field, create the following measure:

   =daystart(due\_date,14,7/24)

Results table

| due\_date | =daystart(due\_date,-7,7/24) | =daystart(due\_date,14,7/24) |
| --- | --- | --- |
| 02/11/2022 9:25:14 AM | 2/4/2022 7:00:00 AM | 2/25/2022 7:00:00 AM |
| 03/25/2022 10:06:54 AM | 3/18/2022 7:00:00 AM | 4/8/2022 7:00:00 AM |
| 04/14/2022 10:44:42 AM | 4/7/2022 7:00:00 AM | 4/28/2022 7:00:00 AM |
| 06/28/2022 11:33:30 AM | 6/21/2022 7:00:00 AM | 7/12/2022 7:00:00 AM |
| 08/15/2022 12:58:14 PM | 8/8/2022 7:00:00 AM | 8/29/2022 7:00:00 AM |
| 11/16/2022 4:23:12 PM | 11/9/2022 7:00:00 AM | 11/30/2022 7:00:00 AM |
| 01/17/2023 6:42:15 PM | 1/10/2023 7:00:00 AM | 1/31/2023 7:00:00 AM |
| 03/22/2023 7:41:16 PM | 3/15/2023 7:00:00 AM | 4/5/2023 7:00:00 AM |

The values of the new fields are in the `TimestampFormat M/D/YYYY h:mm:ss[.fff] TT`. Because the `daystart()` function was used, the timestamp values correspond to the first millisecond of the day.

The early repayment period values are seven days before the due date, since the second argument passed in the `daystart()` function was negative.

The late repayment period values are 14 days after the due date, since the second argument passed in the `daystart()` function was positive.

The dates have a timestamp of 7:00 AM because the value of the third argument passed into the `daystart()` function, `day_start`, was 7/24.
