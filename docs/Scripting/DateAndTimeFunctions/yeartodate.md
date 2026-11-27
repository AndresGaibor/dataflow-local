---
title: "yeartodate Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yeartodate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# yeartodate Script and chart function

Expand/Collapse all

# yeartodate Script and chart function

This function finds if the input timestamp falls within the year of the date the script was last loaded, and returns True if it does, False if it does not. The year of the date the script was last loaded is evaluated as per UTC time.

Syntax:

YearToDate(timestamp[ , yearoffset
[ , firstmonth [ , todaydate] ] ])

Return data type:  Boolean

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Example diagram of yeartodate() function

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between January 1 and April 26, 2022, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-overview.png "Click to view full size")

If none of the optional parameters
are used, the year to date means any date within one calendar year from
January 1 up to and including the date of the last script execution.

In other words, the yeartodate() function, when triggered with no additional parameters, is used to evaluate a timestamp and return a Boolean result based on whether the date occurred within the calendar year up to and including the date that the reload took place.

However, it is also possible to supersede the start date of the year using the firstmonth argument, as well as to make comparisons with preceding or following years using the yearoffset argument.

Finally, in instances of historical datasets, the yeartodate() function provides a parameter to set todaydate, which will instead compare the timestamp to the calendar year up to and including the date provided in the todaydate argument.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The timestamp to evaluate, for example '10/12/2012'. |
| yearoffset | By specifying a yearoffset, yeartodate returns True for the same period in another year. A negative yearoffset indicates a previous year, a positive offset a future year. The most recent year-to-date is achieved by specifying yearoffset = -1. If omitted, 0 is assumed. |
| firstmonth | By specifying a firstmonth between 1 and 12 (1 if omitted), the beginning of the year may be moved forward to the first day of any month. For example, if you want to work with a fiscal year beginning on May 1, specify firstmonth = 5. A value of 1 would indicate a fiscal year starting on January 1, and a value of 12 would indicate a fiscal year starting on December 1. |
| todaydate | By specifying a todaydate (timestamp of the last script execution if omitted) it is possible to move the day used as the upper boundary of the period. |

## When to use yeartodate

The yeartodate() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. This would return an [aggregation](#glossary-0 "Glossary term") or calculation dependent on whether the evaluated date occurred in the year up to and including the last reload date of the application.

For example, the YearToDate() function can be used to identify all equipment manufactured so far in the current year.

The following examples assume last reload time = 11/18/2011.

Function examples

| Example | Result |
| --- | --- |
| yeartodate( '11/18/2010') | returns False |
| yeartodate( '02/01/2011') | returns True |
| yeartodate( '11/18/2011') | returns True |
| yeartodate( '11/19/2011') | returns False |
| yeartodate( '11/19/2011', 0, 1, '12/31/2011') | returns True |
| yeartodate( '11/18/2010', -1) | returns True |
| yeartodate( '11/18/2011', -1) | returns False |
| yeartodate( '04/30/2011', 0, 5) | returns False |
| yeartodate( '05/01/2011', 0, 5) | returns True |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – Basic example

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a set of transactions between 2020 and 2022, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system variable (MM/DD/YYYY) format.
- The creation of a [field](#glossary-2 "Glossary term") year\_to\_date, that determines which transactions took place in the calendar year up to the date of the last reload.

At the time of writing, the date is April 26, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        yeartodate(date) as year_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- year\_to\_date

Results table

| date | year\_to\_date |
| --- | --- |
| 01/10/2020 | 0 |
| 02/28/2020 | 0 |
| 04/09/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 12/27/2021 | 0 |
| 02/02/2022 | -1 |
| 02/26/2022 | -1 |
| 03/07/2022 | -1 |
| 03/11/2022 | -1 |

Diagram of yeartodate() function, basic example

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between January 1 and April 26, 2022, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-examples-basic.png "Click to view full size")

The year\_to\_date field is created in the [preceding load](#glossary-3 "Glossary term") statement by using the yeartodate() function and passing the date field as the function’s argument.

Because no further parameters are passed into the function, the yeartodate() function initially identifies the reload date and therefore the boundaries for the current calendar year (starting January 1) that will return a Boolean result of TRUE.

Therefore, any transaction that occurs between January 1 and April 26, the reload date, will return a Boolean result of TRUE. Any transaction that occurs before the start of 2022 will return a Boolean result of FALSE.

## Example 2 – yearoffset

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, two\_years\_prior, that determines which transactions took place a full two years before the calendar year to date.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        yeartodate(date,-2) as two_years_prior
        ;
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- two\_years\_prior

Results table

| date | two\_years\_prior |
| --- | --- |
| 01/10/2020 | -1 |
| 02/28/2020 | -1 |
| 04/09/2020 | -1 |
| 04/16/2020 | -1 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 12/27/2021 | 0 |
| 02/02/2022 | 0 |
| 02/26/2022 | 0 |
| 03/07/2022 | 0 |
| 03/11/2022 | 0 |

By using -2 as the yearoffset argument in the yeartodate() function, the function shifts the boundaries of the comparator calendar year segment by a full two years. Initially, the year segment equates to between January 1 and April 26, 2022. The yearoffset argument then offsets this segment to two years prior. The date boundaries will then fall between the January 1 and April 26, 2020.

Diagram of yeartodate() function, yearoffset example

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between January 1 and April 26, 2020, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-examples-yearoffset.png "Click to view full size")

Therefore, any transaction that occurs between January 1 and April 26, 2020 will return a Boolean result of TRUE. Any transactions that appear before or after this segment will return FALSE.

## Example 3 – firstmonth

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, year\_to\_date, that determines which transactions took place in the calendar year up to the date of the last reload.

In this example, we set the start of the fiscal year to July 1.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        yeartodate(date,0,7) as year_to_date
        ;
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- year\_to\_date

Results table

| date | year\_to\_date |
| --- | --- |
| 01/10/2020 | 0 |
| 02/28/2020 | 0 |
| 04/09/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | -1 |
| 12/27/2021 | -1 |
| 02/02/2022 | -1 |
| 02/26/2022 | -1 |
| 03/07/2022 | -1 |
| 03/11/2022 | -1 |

In this instance, because the firstmonth argument of 7 is used in the yeartodate() function, it sets the first day of the year to July 1, and the last day of the year to June 30.

Diagram of yeartodate() function, firstmonth example

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between July 1, 2021 and April 26, 2022, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-examples-firstmonth.png "Click to view full size")

Therefore, any transaction that occurs between July 1, 2021 and April 26, 2022, the reload date, will return a Boolean result of TRUE. Any transaction that occurs before July 1, 2021 will return a Boolean result of FALSE.

## Example 4 – todaydate

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset and scenario as the first example.
- The creation of a field, year\_to\_date, that determines which transactions took place in the calendar year up to the date of the last reload.

However, in this example, we need to identify all transactions that took place in the calendar year up to and including March 1, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
    Load
        *,
        yeartodate(date, 0, 1, '03/01/2022') as year_to_date
;
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- year\_to\_date

Results table

| date | year\_to\_date |
| --- | --- |
| 01/10/2020 | 0 |
| 02/28/2020 | 0 |
| 04/09/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 12/27/2021 | 0 |
| 02/02/2022 | -1 |
| 02/26/2022 | -1 |
| 03/07/2022 | 0 |
| 03/11/2022 | 0 |

In this instance, because the todaydate argument of 03/01/2022 is used in the yeartodate() function, it sets the end boundary of the comparator calendar year segment to March 1, 2022. It is critical to provide the firstmonth parameter (between 1 and 12); otherwise the function will return null results.

Diagram of yeartodate() function, example using todaydate argument

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between January 1 and March 1, 2022, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-examples-todaydate.png "Click to view full size")

Therefore, any transaction that occurs between January 1, 2022 and March 1, 2022, the todaydate parameter, will return a Boolean result of TRUE. Any transaction that occurs before January 1, 2022 or after March 1, 2022 will return a Boolean result of FALSE.

## Example 5 – Chart object example

Load script and chart expression

Overview

Open the [Data load editor](#glossary-4 "Glossary term") and add the [load script](#glossary-5 "Glossary term") below to a new tab.

The load script contains the same dataset and scenario as the first example.

However, in this example, the unchanged dataset is loaded into the application. The calculation that determines which transactions took place in the calendar year up to the date of the last reload is created as a [measure](#glossary-6 "Glossary term") in a chart object of the application.

Load script

```
Transactions:
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: date.

Add the following measure:

=yeartodate(date)

Results table

| date | =yeartodate(date) |
| --- | --- |
| 01/10/2020 | 0 |
| 02/28/2020 | 0 |
| 04/09/2020 | 0 |
| 04/16/2020 | 0 |
| 05/21/2020 | 0 |
| 08/14/2020 | 0 |
| 10/07/2020 | 0 |
| 12/05/2020 | 0 |
| 01/22/2021 | 0 |
| 02/03/2021 | 0 |
| 03/17/2021 | 0 |
| 04/23/2021 | 0 |
| 05/04/2021 | 0 |
| 06/30/2021 | 0 |
| 07/26/2021 | 0 |
| 12/27/2021 | 0 |
| 02/02/2022 | -1 |
| 02/26/2022 | -1 |
| 03/07/2022 | -1 |
| 03/11/2022 | -1 |

The year\_to\_date measure is created in the chart object by using the yeartodate() function and passing the date field as the function’s argument.

Because no further parameters are passed into the function, the yeartodate() function initially identifies the reload date, and therefore the boundaries for the current calendar year (starting January 1) that will return a Boolean result of TRUE.

Diagram of yeartodate() function, example using chart object

![Diagram displaying the date values for which the yeartodate function will return a value of True or False. In this case, it returns True for dates between January 1 and April 26, 2022, and False for all other dates.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-examples-chart-object.png "Click to view full size")

Any transaction that occurs between January 1 and April 26, the reload date, will return a Boolean result of TRUE. Any transaction that occurs before the start of 2022 will return a Boolean result of FALSE.

## Example 6 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions between 2020 and 2022, which is loaded into a table called Transactions.
- The date field provided in the DateFormat system variable (MM/DD/YYYY) format.

The end user would like a KPI object that presents the total sales for the equivalent period in 2021 as the current year to date as at the last reload time.

At the time of writing, the date is June 16, 2022.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:
Load
*
Inline
[
id,date,amount
8188,01/10/2020,37.23
8189,02/28/2020,17.17
8190,04/09/2020,88.27
8191,04/16/2020,57.42
8192,05/21/2020,53.80
8193,08/14/2020,82.06
8194,10/07/2020,40.39
8195,12/05/2020,87.21
8196,01/22/2021,95.93
8197,02/03/2021,45.89
8198,03/17/2021,36.23
8199,04/23/2021,25.66
8200,05/04/2021,82.77
8201,06/30/2021,69.98
8202,07/26/2021,76.11
8203,12/27/2021,25.12
8204,02/02/2022,46.23
8205,02/26/2022,84.21
8206,03/07/2022,96.24
8207,03/11/2022,67.67
];
```

Results

Do the following:

1. Create a KPI object.
2. Create the following aggregation measure to calculate total sales:

   =sum(if(yeartodate(date,-1),amount,0))
3. Set the measure’s Number formatting to Money.

KPI yeartodate() chart for 2021

![KPI visualization repesenting sales data for 2021, generated using the yeartodate function.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-function-yeartodate-scenario-kpi.png "Click to view full size")

The yeartodate() function returns a Boolean value when evaluating the dates of each transaction ID. Because the reload took place on June 16, 2022, the yeartodate function segments the year period to between 01/01/2022 and 06/16/2022. However, since a period\_no value of -1 was used in the function, these boundaries are then shifted to the previous year. Therefore, for any transaction that occurs between 01/01/2021 and 06/16/2021, the yeartodate() function returns a Boolean value of TRUE and sums the amount.
