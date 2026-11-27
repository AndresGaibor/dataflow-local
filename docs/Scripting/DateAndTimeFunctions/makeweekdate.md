---
title: "makeweekdate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/makeweekdate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# makeweekdate Script and chart function

Expand/Collapse all

# makeweekdate Script and chart function

This function returns a date calculated from the year, the week number, and the day of week.

Syntax:

MakeWeekDate(weekyear [, week [, weekday [, first\_week\_day [, broken\_weeks [, reference\_day]]]]])

Return data type:  dual

The makeweekdate() function is available both as script and chart function.
The function will calculate the date based on the parameters passed into the function.

Arguments

| Argument | Description |
| --- | --- |
| weekyear | The year as defined by the WeekYear() function for the specific date, that is the year to which the week number belongs.  Information noteThe week year can in some cases be different from the calendar year, for example if week 1 starts already in December of the previous year. |
| week | The week number as defined by the Week() function for the specific date.  If no week number is stated, 1 is assumed. |
| weekday | The day-of-week as defined by the WeekDay() function for the date in question. 0 is the first day of the week, and 6 is the last day of the week.  If no day-of-week is stated, 0 is assumed.  Information noteEven though 0 always means first day of the week and 6 is always the last, which weekdays that corresponds to is determined by the first\_week\_day parameter. If omitted, the value of [variable](#glossary-0 "Glossary term") FirstWeekDay is used.  If broken weeks are used, together with an impossible combination of parameters, this may lead to a result that does not belong to the chosen year.  Example:  MakeWeekDate(2021,1,0,6,1)  Returns ‘Dec 27 2020’ since this day is the first day (the Sunday) of the specified week. Jan 1 2021 was a Friday. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of variable FirstWeekDay is used.  The possible values first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm). |
| broken\_weeks | If you don't specify broken\_weeks, the value of variable BrokenWeeks is used to define whether weeks are broken or not.  For more information about the system variable, see [*BrokenWeeks*](../NumberInterpretationVariables/BrokenWeeks.htm) |
| reference\_day | If you don't specify reference\_day, the value of variable ReferenceDay is used to define which day in January to set as reference day to define week 1.  For more information about the system variable, see [*ReferenceDay*](../NumberInterpretationVariables/ReferenceDay.htm) |

## When to use makeweekdate

The makeweekdate() function would commonly be used in the script for data generation to generate a list of dates, or to construct dates when the year, week and day-of-week are provided in the input data.

The following examples assume:

SET FirstWeekDay=0;
SET BrokenWeeks=0;
SET ReferenceDay=4;

Function examples

| Example | Result |
| --- | --- |
| makeweekdate(2014,6,6) | returns 02/09/2014 |
| makeweekdate(2014,6,1) | returns 02/04/2014 |
| makeweekdate(2014,6) | returns 02/03/2014 (weekday 0 is assumed) |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – day included

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing weekly sales total for 2022 in a table called Sales.
- Transaction dates provided across three fields: year, week, and sales.
- A [preceding load](#glossary-2 "Glossary term") which is used to create a [measure](#glossary-3 "Glossary term") end\_of\_week, using the makeweekdate() function to return the date for the Friday of that week in the format MM/DD/YYYY.

To prove that the date returned is a Friday, the end\_of\_week expression is also wrapped in the weekday() function to show the day of the week.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=0;
SET BrokenWeeks=0;
SET ReferenceDay=4;

Transactions:
    Load
        *,
        makeweekdate(transaction_year, transaction_week,4) as end_of_week,
        weekday(makeweekdate(transaction_year, transaction_week,4)) as week_day
        ;
Load * Inline [
transaction_year, transaction_week, sales
2022, 01, 10000
2022, 02, 11250
2022, 03, 9830
2022, 04, 14010
2022, 05, 28402
2022, 06, 9992
2022, 07, 7292
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_year
- transaction\_week
- end\_of\_week
- week\_day

Results table

| transaction\_year | transaction\_week | end\_of\_week | week\_day |
| --- | --- | --- | --- |
| 2022 | 01 | 01/07/2022 | Fri |
| 2022 | 02 | 01/14/2022 | Fri |
| 2022 | 03 | 01/21/2022 | Fri |
| 2022 | 04 | 01/28/2022 | Fri |
| 2022 | 05 | 02/04/2022 | Fri |
| 2022 | 06 | 02/11/2022 | Fri |
| 2022 | 07 | 02/18/2022 | Fri |

The end\_of\_week [field](#glossary-4 "Glossary term") is created in the preceding load statement by using the makeweekdate() function. The transaction\_year, transaction\_week fields are passed through the function as the year and week arguments. A value of 4 is used for the day argument.

The function then combines and converts these values into a date field, returning the results in the format of the DateFormat system variable.

The makeweekdate() function, and its arguments are also wrapped in a weekday() function to return the week\_day field; and as can be seen in the table above, the week\_day field shows that these dates do occur on a Friday.

## Example 2 – day excluded

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing weekly sales totals for 2022 in a table called Sales.
- Transaction dates provided across three fields: year, week, and sales.
- A preceding load, which is used to create a measure, first\_day\_of\_week, using the makeweekdate() function. This will return the date for the Monday of that week in the format MM/DD/YYYY.

To prove that the date returned is a Monday, the first\_day\_of\_week expression is also wrapped in the weekday() function to show the day of the week.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=0;
SET BrokenWeeks=0;
SET ReferenceDay=4;

Transactions:
    Load
        *,
        makeweekdate(transaction_year, transaction_week) as first_day_of_week,
        weekday(makeweekdate(transaction_year, transaction_week)) as week_day
        ;
Load * Inline [
transaction_year, transaction_week, sales
2022, 01, 10000
2022, 02, 11250
2022, 03, 9830
2022, 04, 14010
2022, 05, 28402
2022, 06, 9992
2022, 07, 7292
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- transaction\_year
- transaction\_week
- first\_day\_of\_week
- week\_day

Results table

| transaction\_year | transaction\_week | first\_day\_of\_week | week\_day |
| --- | --- | --- | --- |
| 2022 | 01 | 01/03/2022 | Mon |
| 2022 | 02 | 01/10/2022 | Mon |
| 2022 | 03 | 01/17/2022 | Mon |
| 2022 | 04 | 01/24/2022 | Mon |
| 2022 | 05 | 01/31/2022 | Mon |
| 2022 | 06 | 02/07/2022 | Mon |
| 2022 | 07 | 02/14/2022 | Mon |

The first\_day\_of\_week field is created in the preceding load statement by using the makeweekdate() function. The transaction\_year and transaction\_week parameters are passed as function arguments, and the day parameter is left blank.

The function then combines and converts these values into a date field, returning the results in the format of the DateFormat system variable.

The makeweekdate() function and its arguments are also wrapped in a weekday() function to return the week\_day field. As can be seen in the table above, the week\_day field returns Monday in all cases since that parameter was left blank in the makeweekdate() function, which defaults to 0 (first day of the week), and first day of the week is set to Monday by the FirstWeekDay system variable.

## Example 3 – Chart object example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing weekly sales totals for 2022 in a table called Sales.
- Transaction dates provided across three fields: year, week, and sales.

In this example, a chart object will be used to create a measure equivalent to the end\_of\_week calculation from the first example. This measure will use the makeweekdate() function to return the date for the Friday of that week in the format MM/DD/YYYY.

To prove that the date returned is a Friday, a second measure is created to return the day of the week.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=0;
SET BrokenWeeks=0;
SET ReferenceDay=4;

Master_Calendar:
Load * Inline [
transaction_year, transaction_week, sales
2022, 01, 10000
2022, 02, 11250
2022, 03, 9830
2022, 04, 14010
2022, 05, 28402
2022, 06, 9992
2022, 07, 7292
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - transaction\_year
   - transaction\_week
2. To perform the calculation equivalent to that of the end\_of\_weekfield from the first example, create the following measure:

   =makeweekdate(transaction\_year,transaction\_week,4)
3. To calculate the day of the week for each transaction, create the following measure:

   =weekday(makeweekdate(transaction\_year,transaction\_week,4))

Results table

| transaction\_year | transaction\_week | =makeweekdate(transaction\_year,transaction\_week,4) | =weekday(makeweekdate(transaction\_year,transaction\_week,4)) |
| --- | --- | --- | --- |
| 2022 | 01 | 01/07/2022 | Fri |
| 2022 | 02 | 01/14/2022 | Fri |
| 2022 | 03 | 01/21/2022 | Fri |
| 2022 | 04 | 01/28/2022 | Fri |
| 2022 | 05 | 02/04/2022 | Fri |
| 2022 | 06 | 02/11/2022 | Fri |
| 2022 | 07 | 02/18/2022 | Fri |

An equivalent field to end\_of\_week is created in the chart object as a measure by using the makeweekdate() function. The transaction\_year and transaction\_week fields are passed as year and week arguments. A value of 4 is used for the day argument.

The function then combines and converts these values into a date field, returning the results in the format of the DateFormat system variable.

The makeweekdate() function and its arguments are also wrapped in a weekday() function to return a calculation equivalent to that of the week\_day field from the first example. As can be seen in the table above, the last column on the right shows that these dates do occur on a Friday.

## Example 4 – Scenario

Load script and chart expression

Overview

In this example, create a list of dates containing all the Fridays for the year 2022.

Open the [Data load editor](#glossary-5 "Glossary term") and add the [load script](#glossary-6 "Glossary term") below to a new tab.

Load script

```
SET DateFormat='MM/DD/YYYY';
SET FirstWeekDay=0;
SET BrokenWeeks=0;
SET ReferenceDay=4;

Calendar:
    load
	    *,
        weekday(date) as weekday
    where year(date)=2022;
load
    makeweekdate(2022,recno()-2,4) as date
AutoGenerate 60;
```

Results

Results table

| date | weekday |
| --- | --- |
| 01/07/2022 | Fri |
| 01/14/2022 | Fri |
| 01/21/2022 | Fri |
| 01/28/2022 | Fri |
| 02/04/2022 | Fri |
| 02/11/2022 | Fri |
| 02/18/2022 | Fri |
| 02/25/2022 | Fri |
| 03/04/2022 | Fri |
| 03/11/2022 | Fri |
| 03/18/2022 | Fri |
| 03/25/2022 | Fri |
| 04/01/2022 | Fri |
| 04/08/2022 | Fri |
| 04/15/2022 | Fri |
| 04/22/2022 | Fri |
| 04/29/2022 | Fri |
| 05/06/2022 | Fri |
| 05/13/2022 | Fri |
| 05/20/2022 | Fri |
| 05/27/2022 | Fri |
| 06/03/2022 | Fri |
| 06/10/2022 | Fri |
| 06/17/2022 | Fri |
| + 27 more rows |  |

The makeweekdate() function finds each Friday in 2022. Using a week parameter of -2 ensures that no dates are missed. Finally, a preceding load creates an additional weekday field for clarity, to show that each date value is a Friday.
