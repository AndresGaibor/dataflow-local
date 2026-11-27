---
title: "GMT Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/GMT.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# GMT Script and chart function

Expand/Collapse all

# GMT Script and chart function

This function returns the current Greenwich
Mean Time, as derived from the regional settings. The function returns values in the TimestampFormat system variable format.

Whenever the application is reloaded, any [load script](#glossary-1 "Glossary term") table, [variable](#glossary-2 "Glossary term") or [chart](#glossary-3 "Glossary term") object that uses the GMT function will be adjusted to the latest current Greenwich Mean Time as derived from the system clock.

Syntax:

GMT( )

Return data type:  dual

These examples use the timestamp format M/D/YYYY h:mm:ss[.fff] TT. The date format is specified in the SET TimestampFormat statement at the top of your data load script. Change the format in the examples to suit your requirements.

Function examples

| Example | Result |
| --- | --- |
| GMT() | 3/28/2022 2:47:36 PM |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - Variable (script)

Load script and results

Overview

Open the [Data load editor](#glossary-4 "Glossary term") and add the load script below to a new tab. This example will set the current Greenwich Mean Time as a variable in the load script using the GMT function.

Load script

```
LET vGMT = GMT();
```

Results

Load the data and create a [sheet](#glossary-5 "Glossary term"). Create a text box using the Text & image chart object.

Add this [measure](#glossary-6 "Glossary term") to the text box:

=vGMT

The text box should contain a line of text with a date and time, similar to the one shown below:

3/28/2022 2:47:36 PM

## Example 2 - November start of year (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-7 "Glossary term") containing overdue library books, which is loaded into a table named Overdue. The default DateFormat system variable MM/DD/YYYY is used.
- The creation of a new [field](#glossary-8 "Glossary term") called days\_overdue, which calculates how many day overdue each book is.

Load script

```
SET DateFormat='MM/DD/YYYY';

Overdue:
    Load
        *,
        Floor(GMT()-due_date) as days_overdue
        ;
Load
*
Inline
[
cust_id,book_id,due_date
1,4,01/01/2021,
2,24,01/10/2021,
6,173,01/31/2021,
31,281,02/01/2021,
86,265,02/10/2021,
52,465,06/30/2021,
26,537,07/26/2021,
92,275,10/31/2021,
27,455,11/01/2021,
27,46,12/31/2021
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- due\_date
- book\_id
- days\_overdue

Results table

| due\_date | book\_id | days\_overdue |
| --- | --- | --- |
| 01/01/2021 | 4 | 455 |
| 01/10/2021 | 24 | 446 |
| 01/31/2021 | 173 | 425 |
| 02/01/2021 | 281 | 424 |
| 02/10/2021 | 265 | 415 |
| 06/30/2021 | 465 | 275 |
| 07/26/2021 | 537 | 249 |
| 10/31/2021 | 275 | 152 |
| 11/01/2021 | 455 | 151 |
| 12/31/2021 | 46 | 91 |

The values in the days\_overdue field are calculated by finding the difference between the current Greenwich Mean Time, using the GMT() function, and the original due date. In order to calculate only the days, the results are rounded off to the nearest whole number using the Floor() function.

## Example 3 - chart object (chart)

Load script and chart expression

Overview

Open the Data load editor, and add the load script below to a new tab. The load script contains the same dataset as the previous example. The default DateFormat system variable MM/DD/YYYY is used.

However, in this example, the unchanged dataset is loaded into the application. The value of the number of days overdue is calculated via a measure in a chart object.

Load script

```
SET DateFormat='MM/DD/YYYY';

Overdue:
Load
*
Inline
[
cust_id,book_id,due_date
1,4,01/01/2021,
2,24,01/10/2021,
6,173,01/31/2021,
31,281,02/01/2021,
86,265,02/10/2021,
52,465,06/30/2021,
26,537,07/26/2021,
92,275,10/31/2021,
27,455,11/01/2021,
27,46,12/31/2021
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- due\_date
- book\_id

Create the following measure:

=Floor(GMT() – due\_date)

Results table

| due\_date | book\_id | =Floor(GMT()-due\_date) |
| --- | --- | --- |
| 01/01/2021 | 4 | 455 |
| 01/10/2021 | 24 | 446 |
| 01/31/2021 | 173 | 425 |
| 02/01/2021 | 281 | 424 |
| 02/10/2021 | 265 | 415 |
| 06/30/2021 | 465 | 275 |
| 07/26/2021 | 537 | 249 |
| 10/31/2021 | 275 | 152 |
| 11/01/2021 | 455 | 151 |
| 12/31/2021 | 46 | 91 |

The values in the days\_overdue field are calculated by finding the difference between the current Greenwich Mean Time, using the GMT() function, and the original due date. In order to calculate only the days, the results are rounded off to the nearest whole number using the Floor() function.
