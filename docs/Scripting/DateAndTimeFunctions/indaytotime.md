---
title: "indaytotime Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/indaytotime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# indaytotime Script and chart function

Expand/Collapse all

# indaytotime Script and chart function

This function returns
True if timestamp lies inside
the part of day containing base\_timestamp
up until and including the exact millisecond of base\_timestamp.

Syntax:

InDayToTime (timestamp, base\_timestamp, period\_no[, day\_start])

The indaytotime() function returns a Boolean result depending on when a timestamp value occurs during the segment of the day. The start boundary of this segment is the start of the day, which is set as midnight by default; the start of the day can be modified by the day\_start argument of the indaytotime() function. The end boundary of the day segment is determined by a base\_timestamp argument of the function.

Diagram of indaytotime function.

![Diagram showing the relations between the variables of the indaytotime function. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-indaytotime-diagram-overview.png "Click to view full size")

When to use indaytotime

The indaytotime() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. The indaytotime() function returns an [aggregation](#glossary-0 "Glossary term") or calculation depending on if a timestamp occurred in the segment of the day up to and including the time of the base timestamp.

For example, the indaytotime() function can be used to show the sum of ticket sales for shows that have taken place so far today.

Return data type: Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date and time that you want to compare with base\_timestamp. |
| base\_timestamp | Date and time that is used to evaluate the timestamp. |
| period\_no | The day can be offset by period\_no. period\_no is an integer, where the value 0 indicates the day which contains base\_timestamp. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | (optional) If you want to work with days not starting midnight, indicate an offset as a fraction of a day in day\_start. For example, use 0.125 to denote 3 AM. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| indaytotime ('01/12/2006 12:23:00 PM', '01/12/2006 11:59:00 PM', 0) | Returns True |
| indaytotime ('01/12/2006 12:23:00 PM', '01/12/2006 12:00:00 AM', 0) | Returns False |
| indaytotime '01/11/2006 12:23:00 PM', '01/12/2006 11:59:00 PM', -1) | Returns True |

## Example 1 – no additional arguments

Load script and results

Overview

Open the Data load editor and add the [load script](#glossary-1 "Glossary term") below to a new tab.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") containing a set of transactions for the period between January 4 and 5 is loaded into a table called 'Transactions'.
- A date [field](#glossary-3 "Glossary term") which is provided in the TimeStamp system variable (M/D/YYYY h:mm:ss[.fff] TT) format.
- A [preceding load](#glossary-4 "Glossary term") which contains the indaytotime() function which is set as the 'in\_day\_to\_time', field that determines whether each of the transactions take place before 9:00 AM.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        indaytotime(date,'01/05/2022 9:00:00 AM',0) as in_day_to_time
        ;
Load
*
Inline
[
id,date,amount
8188,'01/04/2022 3:41:54 AM',25.66
8189,'01/04/2022 4:19:43 AM',87.21
8190,'01/04/2022 4:53:47 AM',53.80
8191,'01/04/2022 8:38:53 AM',69.98
8192,'01/04/2022 10:37:52 AM',57.42
8193,'01/04/2022 1:54:10 PM',45.89
8194,'01/04/2022 5:53:23 PM',82.77
8195,'01/04/2022 8:13:26 PM',36.23
8196,'01/04/2022 10:00:49 PM',76.11
8197,'01/05/2022 7:45:37 AM',82.06
8198,'01/05/2022 8:44:36 AM',17.17
8199,'01/05/2022 11:26:08 AM',40.39
8200,'01/05/2022 6:43:08 PM',37.23
8201,'01/05/2022 10:54:10 PM',88.27
8202,'01/05/2022 11:09:09 PM',95.93
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day\_to\_time

Results table

| date | in\_day\_to\_time |
| --- | --- |
| 01/04/2022 3:41:54 AM | 0 |
| 01/04/2022 4:19:43 AM | 0 |
| 01/04/2022 04:53:47 AM | 0 |
| 01/04/2022 8:38:53 AM | 0 |
| 01/04/2022 10:37:52 AM | 0 |
| 01/04/2022 1:54:10 PM | 0 |
| 01/04/2022 5:53:23 PM | 0 |
| 01/04/2022 8:13:26 PM | 0 |
| 01/04/2022 10:00:49 PM | 0 |
| 01/05/2022 7:45:37 AM | -1 |
| 01/05/2022 8:44:36 AM | -1 |
| 01/05/2022 11:26:08 AM | 0 |
| 01/05/2022 6:43:08 PM | 0 |
| 01/05/2022 10:54:10 PM | 0 |
| 01/05/2022 11:09:09 PM | 0 |

Example 1 diagram of indaytotime function with 9:00 AM limit..

![Diagram showing indaytotime() function with a 9:00 limit. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-indaytotime-example1-diagram.png "Click to view full size")

The in\_day\_to\_time field is created in the preceding load statement by using the indaytotime() function and passing the date field, a hard-coded timestamp for 9:00 AM January 5 and an offset of 0 as the function’s arguments. Any transactions that occur between midnight and 9:00 AM on January 5 return TRUE.

## Example 2 – period\_no

Load script and results

Overview

The load script uses the same dataset and scenario that were used in the first example.

However, in this example, you will calculate whether the transaction date occurred one day before 9:00 AM on January 5.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        indaytotime(date,'01/05/2022 9:00:00 AM', -1) as in_day_to_time
        ;
Load
*
Inline
[
id,date,amount
8188,'01/04/2022 3:41:54 AM',25.66
8189,'01/04/2022 4:19:43 AM',87.21
8190,'01/04/2022 4:53:47 AM',53.80
8191,'01/04/2022 8:38:53 AM',69.98
8192,'01/04/2022 10:37:52 AM',57.42
8193,'01/04/2022 1:54:10 PM',45.89
8194,'01/04/2022 5:53:23 PM',82.77
8195,'01/04/2022 8:13:26 PM',36.23
8196,'01/04/2022 10:00:49 PM',76.11
8197,'01/05/2022 7:45:37 AM',82.06
8198,'01/05/2022 8:44:36 AM',17.17
8199,'01/05/2022 11:26:08 AM',40.39
8200,'01/05/2022 6:43:08 PM',37.23
8201,'01/05/2022 10:54:10 PM',88.27
8202,'01/05/2022 11:09:09 PM',95.93
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day\_to\_time

Results table

| date | in\_day\_to\_time |
| --- | --- |
| 01/04/2022 3:41:54 AM | -1 |
| 01/04/2022 4:19:43 AM | -1 |
| 01/04/2022 04:53:47 AM | -1 |
| 01/04/2022 8:38:53 AM | -1 |
| 01/04/2022 10:37:52 AM | 0 |
| 01/04/2022 1:54:10 PM | 0 |
| 01/04/2022 5:53:23 PM | 0 |
| 01/04/2022 8:13:26 PM | 0 |
| 01/04/2022 10:00:49 PM | 0 |
| 01/05/2022 7:45:37 AM | 0 |
| 01/05/2022 8:44:36 AM | 0 |
| 01/05/2022 11:26:08 AM | 0 |
| 01/05/2022 6:43:08 PM | 0 |
| 01/05/2022 10:54:10 PM | 0 |
| 01/05/2022 11:09:09 PM | 0 |

Example 2 diagram of indaytotime function with transactions from January 4.

![Diagram showing the indaytotime () function that uses a period_no of -1 to return transactions from January 4. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-indaytotime-example2-diagram.png "Click to view full size")

In this example, because an offset of -1 was used as the offset argument in the indaytotime() function, the function determines whether each transaction date took place before 9:00 AM on January 4. This can be verified in the output table where a transaction returns a Boolean result of TRUE.

## Example 3 – day\_start

Load script and results

Overview

The same dataset and scenario as the first example are used.

However, in this example, the company policy is that the workday begins and ends at 8AM.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        indaytotime(date,'01/05/2022 9:00:00 AM', 0,8/24) as in_day_to_time
        ;
Load
*
Inline
[
id,date,amount
8188,'01/04/2022 3:41:54 AM',25.66
8189,'01/04/2022 4:19:43 AM',87.21
8190,'01/04/2022 4:53:47 AM',53.80
8191,'01/04/2022 8:38:53 AM',69.98
8192,'01/04/2022 10:37:52 AM',57.42
8193,'01/04/2022 1:54:10 PM',45.89
8194,'01/04/2022 5:53:23 PM',82.77
8195,'01/04/2022 8:13:26 PM',36.23
8196,'01/04/2022 10:00:49 PM',76.11
8197,'01/05/2022 7:45:37 AM',82.06
8198,'01/05/2022 8:44:36 AM',17.17
8199,'01/05/2022 11:26:08 AM',40.39
8200,'01/05/2022 6:43:08 PM',37.23
8201,'01/05/2022 10:54:10 PM',88.27
8202,'01/05/2022 11:09:09 PM',95.93
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day\_to\_time

Results table

| date | in\_day\_to\_time |
| --- | --- |
| 01/04/2022 3:41:54 AM | 0 |
| 01/04/2022 4:19:43 AM | 0 |
| 01/04/2022 04:53:47 AM | 0 |
| 01/04/2022 8:38:53 AM | 0 |
| 01/04/2022 10:37:52 AM | 0 |
| 01/04/2022 1:54:10 PM | 0 |
| 01/04/2022 5:53:23 PM | 0 |
| 01/04/2022 8:13:26 PM | 0 |
| 01/04/2022 10:00:49 PM | 0 |
| 01/05/2022 7:45:37 AM | 0 |
| 01/05/2022 8:44:36 AM | -1 |
| 01/05/2022 11:26:08 AM | 0 |
| 01/05/2022 6:43:08 PM | 0 |
| 01/05/2022 10:54:10 PM | 0 |
| 01/05/2022 11:09:09 PM | 0 |

Example 3 diagram of indaytotime function with transactions from 8:00 AM to 9:00 AM.,

![Diagram showing the indaytotime() function that shows transactions from 8:00am to 9:00am.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-indaytotime-example3-diagram.png "Click to view full size")

Because the start\_day argument of 8/24, which equates to 8:00 AM, is used in the indaytotime() function, each day begins and ends at 8:00 AM. Therefore, the indaytotime() function will return a Boolean result of TRUE for any transaction that took place between 8:00 AM and 9:00 AM on January 5.

## Example 4 – Chart object

expression

Overview

The same dataset and scenario as the first example are used.

However, in this example, the dataset is unchanged and loaded into the application. You will calculate to determine if a transaction takes place on January 5 before 9:00 AM by creating a [measure](#glossary-6 "Glossary term") in a chart object.

Load script

```
Transactions:
Load
*
Inline
[
id,date,amount
8188,'01/04/2022 3:41:54 AM',25.66
8189,'01/04/2022 4:19:43 AM',87.21
8190,'01/04/2022 4:53:47 AM',53.80
8191,'01/04/2022 8:38:53 AM',69.98
8192,'01/04/2022 10:37:52 AM',57.42
8193,'01/04/2022 1:54:10 PM',45.89
8194,'01/04/2022 5:53:23 PM',82.77
8195,'01/04/2022 8:13:26 PM',36.23
8196,'01/04/2022 10:00:49 PM',76.11
8197,'01/05/2022 7:45:37 AM',82.06
8198,'01/05/2022 8:44:36 AM',17.17
8199,'01/05/2022 11:26:08 AM',40.39
8200,'01/05/2022 6:43:08 PM',37.23
8201,'01/05/2022 10:54:10 PM',88.27
8202,'01/05/2022 11:09:09 PM',95.93
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

date.

To determine if a transaction takes place on January 5 before 9:00 AM, create the following measure:

=indaytotime(date,'01/05/2022 9:00:00 AM',0)

Results table

| date | =indaytotime(date,'01/05/2022 9:00:00 AM',0) |
| --- | --- |
| 01/04/2022 3:41:54 AM | 0 |
| 01/04/2022 4:19:43 AM | 0 |
| 01/04/2022 04:53:47 AM | 0 |
| 01/04/2022 8:38:53 AM | 0 |
| 01/04/2022 10:37:52 AM | 0 |
| 01/04/2022 1:54:10 PM | 0 |
| 01/04/2022 5:53:23 PM | 0 |
| 01/04/2022 8:13:26 PM | 0 |
| 01/04/2022 10:00:49 PM | 0 |
| 01/05/2022 7:45:37 AM | -1 |
| 01/05/2022 8:44:36 AM | -1 |
| 01/05/2022 11:26:08 AM | 0 |
| 01/05/2022 6:43:08 PM | 0 |
| 01/05/2022 10:54:10 PM | 0 |
| 01/05/2022 11:09:09 PM | 0 |

The in\_day\_to\_time measure is created in the chart object by using the indaytotime() function and passing the date field, a hard-coded timestamp for 9:00 AM on January 5 and an offset of 0 as the function’s arguments. Any transactions that occur between midnight and 9:00 AM on January 5 return TRUE. This is validated in the results table.

## Example 5 – Scenario

Load script and results

Overview

In this example, a dataset containing ticket sales for a local cinema is loaded into a table called Ticket\_Sales. Today is May 3, 2022 and it is 11:00 AM.

The user would like a KPI chart object to show the revenue earned from all shows that have taken place so far today.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Ticket_Sales:
Load
*
Inline
[
sale ID, show time, ticket price
1,05/01/2022 09:30:00 AM,10.50
2,05/03/2022 05:30:00 PM,21.00
3,05/03/2022 09:30:00 AM,10.50
4,05/03/2022 09:30:00 AM,31.50
5,05/03/2022 09:30:00 AM,10.50
6,05/03/2022 12:00:00 PM,42.00
7,05/03/2022 12:00:00 PM,10.50
8,05/03/2022 05:30:00 PM,42.00
9,05/03/2022 08:00:00 PM,31.50
10,05/04/2022 10:30:00 AM,31.50
11,05/04/2022 12:00:00 PM,10.50
12,05/04/2022 05:30:00 PM,10.50
13,05/05/2022 05:30:00 PM,21.00
14,05/06/2022 12:00:00 PM,21.00
15,05/07/2022 09:30:00 AM,42.00
16,05/07/2022 10:30:00 AM,42.00
17,05/07/2022 10:30:00 AM,10.50
18,05/07/2022 05:30:00 PM,10.50
19,05/08/2022 05:30:00 PM,21.00
20,05/11/2022 09:30:00 AM,10.50
];
```

Results

Do the following:

1. Create a KPI object.
2. Create a measure that will show the sum of all ticket sales for shows that have taken place today so far using the indaytotime() function:

=sum(if(indaytotime([show time],'05/03/2022 11:00:00 AM',0),[ticket price],0))

1. Create a label for the KPI object, ‘Current Revenue’.
2. Set the measure’s Number Formatting to Money.

The sum total of ticket sales up to 11:00 AM on May 3, 2022 is $52.50.

The indaytotime () function returns a Boolean value when comparing the show times of each of the ticket sales to the current time ('05/03/2022 11:00:00 AM’). For any show on May 3 before 11:00 AM, the indaytotime () function returns a Boolean value of TRUE and its ticket price will be included in the sum total.
