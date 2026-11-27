---
title: "dayend Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/dayend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# dayend Script and chart function

Expand/Collapse all

# dayend Script and chart function

This function returns
a value corresponding to a timestamp of the final millisecond of the
day contained in time. The
default output format will be the TimestampFormat set in the script.

Syntax:

DayEnd(time[, [period\_no[, day\_start]])

When to use dayend

The dayend() function is commonly used as part of an expression when the user would like the calculation to use the fraction of the day that has not yet occurred. For example, to calculate the total expenses still to be incurred during the day.

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| time | The timestamp to evaluate. |
| period\_no | period\_no is an integer, or expression that resolves to an integer, where the value 0 indicates the day that contains time. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | To specify that days do not starting at midnight, indicate an offset as a fraction of a day in day\_start. For example, 0.125 to denote 3:00 AM. In other words, to create the offset, divide the start time by 24 hours. For example, for a day to begin at 7:00 AM, use the fraction 7/24. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| dayend('01/25/2013 16:45:00') | Returns 01/25/2013 23:59:59. PM |
| dayend('01/25/2013 16:45:00', -1) | Returns 01/24/2013 23:59:59. PM |
| dayend('01/25/2013 16:45:00', 0, 0.5) | Returns 01/26/2013 11:59:59. PM |

## Example 1 - Basic script

Load script and results

Overview

Open the Data load editor and add the [load script](#glossary-0 "Glossary term") below to a new tab.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing a list of dates is loaded into a table named "Calendar".
- The default DateFormat system variable (MM/DD/YYYY).
- A [preceding load](#glossary-2 "Glossary term") to create an additional [field](#glossary-3 "Glossary term") 'EOD\_timestamp', using the dayend() function.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Calendar:
    Load
      date,
      dayend(date) as EOD_timestamp
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

- date
- EOD\_timestamp

Results table

| date | EOD\_timestamp |
| --- | --- |
| 03/11/2022 1:47:15 AM | 3/11/2022 11:59:59 PM |
| 03/12/2022 4:34:58 AM | 3/12/2022 11:59:59 PM |
| 03/13/2022 5:15:55 AM | 3/13/2022 11:59:59 PM |
| 03/14/2022 9:25:14 AM | 3/14/2022 11:59:59 PM |
| 03/15/2022 10:06:54 AM | 3/15/2022 11:59:59 PM |
| 03/16/2022 10:44:42 AM | 3/16/2022 11:59:59 PM |
| 03/17/2022 11:33:30 AM | 3/17/2022 11:59:59 PM |
| 03/18/2022 12:58:14 PM | 3/18/2022 11:59:59 PM |
| 03/19/2022 4:23:12 PM | 3/19/2022 11:59:59 PM |
| 03/20/2022 6:42:15 PM | 3/20/2022 11:59:59 PM |
| 03/21/2022 7:41:16 PM | 3/21/2022 11:59:59 PM |

As you can see in the table above, the end of day timestamp is generated for each date in our dataset. The timestamp is in the format of the system variable TimestampFormat M/D/YYYY h:mm:ss[.fff] TT.

## Example 2 – period\_no

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

You will load a dataset containing service bookings into a table named 'Services'.

The dataset includes the following fields:

- service\_id
- service\_date
- amount

You will create two new fields in the table:

- deposit\_due\_date: The date when the deposit should be received. This is the end of the day three days before the service\_date.
- final\_payment\_due\_date: The date when the final payment should be received. This is the end of the day seven days after the service\_date.

The two fields above are created in a preceding load using the dayend() function and they supply the first two parameters, time and period\_no.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Services:
   Load
     *,
     dayend(service_date,-3) as deposit_due_date,
     dayend(service_date,7) as final_payment_due_date
     ;
Load
service_id,
service_date,
amount
Inline
[
service_id, service_date,amount
1,03/11/2022 9:25:14 AM,231.24
2,03/12/2022 10:06:54 AM,567.28
3,03/13/2022 10:44:42 AM,364.28
4,03/14/2022 11:33:30 AM,575.76
5,03/15/2022 12:58:14 PM,638.68
6,03/16/2022 4:23:12 PM,785.38
7,03/17/2022 6:42:15 PM,967.46
8,03/18/2022 7:41:16 PM,287.67
9,03/19/2022 8:14:15 PM,764.45
10,03/20/2022 9:23:51 PM,875.43
11,03/21/2022 10:04:41 PM,957.35
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- service\_date
- deposit\_due\_date
- final\_payment\_due\_date

Results table

| service\_date | deposit\_due\_date | final\_payment\_due\_date |
| --- | --- | --- |
| 03/11/2022 9:25:14 AM | 3/8/2022 11:59:59 PM | 3/18/2022 11:59:59 PM |
| 03/12/2022 10:06:54 AM | 3/9/2022 11:59:59 PM | 3/19/2022 11:59:59 PM |
| 03/13/2022 10:44:42 AM | 3/10/2022 11:59:59 PM | 3/20/2022 11:59:59 PM |
| 03/14/2022 11:33:30 AM | 3/11/2022 11:59:59 PM | 3/21/2022 11:59:59 PM |
| 03/15/2022 12:58:14 PM | 3/12/2022 11:59:59 PM | 3/22/2022 11:59:59 PM |
| 03/16/2022 4:23:12 PM | 3/13/2022 11:59:59 PM | 3/23/2022 11:59:59 PM |
| 03/17/2022 6:42:15 PM | 3/14/2022 11:59:59 PM | 3/24/2022 11:59:59 PM |
| 03/18/2022 7:41:16 PM | 3/15/2022 11:59:59 PM | 3/25/2022 11:59:59 PM |
| 03/19/2022 8:14:15 PM | 3/16/2022 11:59:59 PM | 3/26/2022 11:59:59 PM |
| 03/20/2022 9:23:51 PM | 3/17/2022 11:59:59 PM | 3/27/2022 11:59:59 PM |
| 03/21/2022 10:04:41 PM | 3/18/2022 11:59:59 PM | 3/28/2022 11:59:59 PM |

The values of the new fields are in the TimestampFormat M/D/YYYY h:mm:ss[.fff] TT. Because the function dayend() was used, the timestamp values are all the last millisecond of the day.

The deposit due date values are three days before the service date because the second argument passed in the dayend() function is negative.

The final payment due date values are seven days after the service date because the second argument passed in the dayend() function is positive.

## Example 3 – day\_start script

Load script and results

Overview

Open the Data load editor and add the load script below in a new tab.

The dataset and scenario used in this example is the same as in the previous example.

As in the previous example, you will create two new fields:

- deposit\_due\_date: The date when the deposit should be received. This is the end of the day three days before the service\_date.
- final\_payment\_due\_date: The date when the final payment should be received. This is the end of the day seven days after the service\_date.

However, your company would like to operate under a policy where the working day begins at 5 PM and ends at 5 PM the following day. Your company can then monitor transactions that occur in those working hours.

To achieve these requirements, the two fields above are created in a preceding load using the dayend() function and use all three arguments, time, period\_no, and day\_start.

Load Script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Services:
   Load
     *,
     dayend(service_date,-3,17/24) as deposit_due_date,
     dayend(service_date,7,17/24) as final_payment_due_date
     ;
Load
service_id,
service_date,
amount
Inline
[
service_id, service_date,amount
1,03/11/2022 9:25:14 AM,231.24
2,03/12/2022 10:06:54 AM,567.28
3,03/13/2022 10:44:42 AM,364.28
4,03/14/2022 11:33:30 AM,575.76
5,03/15/2022 12:58:14 PM,638.68
6,03/16/2022 4:23:12 PM,785.38
7,03/17/2022 6:42:15 PM,967.46
8,03/18/2022 7:41:16 PM,287.67
9,03/19/2022 8:14:15 PM,764.45
10,03/20/2022 9:23:51 PM,875.43
11,03/21/2022 10:04:41 PM,957.35
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- service\_date
- deposit\_due\_date
- final\_payment\_due\_date

Results table

| service\_date | deposit\_due\_date | final\_payment\_due\_date |
| --- | --- | --- |
| 03/11/2022 9:25:14 AM | 3/8/2022 4:59:59 PM | 3/18/2022 4:59:59 PM |
| 03/12/2022 10:06:54 AM | 3/9/2022 4:59:59 PM | 3/19/2022 4:59:59 PM |
| 03/13/2022 10:44:42 AM | 3/10/2022 4:59:59 PM | 3/20/2022 4:59:59 PM |
| 03/14/2022 11:33:30 AM | 3/11/2022 4:59:59 PM | 3/21/2022 4:59:59 PM |
| 03/15/2022 12:58:14 PM | 3/12/2022 4:59:59 PM | 3/22/2022 4:59:59 PM |
| 03/16/2022 4:23:12 PM | 3/13/2022 4:59:59 PM | 3/23/2022 4:59:59 PM |
| 03/17/2022 6:42:15 PM | 3/14/2022 4:59:59 PM | 3/24/2022 4:59:59 PM |
| 03/18/2022 7:41:16 PM | 3/15/2022 4:59:59 PM | 3/25/2022 4:59:59 PM |
| 03/19/2022 8:14:15 PM | 3/16/2022 4:59:59 PM | 3/26/2022 4:59:59 PM |
| 03/20/2022 9:23:51 PM | 3/17/2022 4:59:59 PM | 3/27/2022 4:59:59 PM |
| 03/21/2022 10:04:41 PM | 3/18/2022 4:59:59 PM | 3/28/2022 4:59:59 PM |

While the dates remain the same as in Example 2, the dates now have a timestamp of the last millisecond before 5:00 PM because the value of the third argument, day\_start, passed into the dayend() function is 17/24.

## Example 4 – Chart example

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new tab.

The dataset and scenario used in this example is the same as in the previous two examples. The company would like to operate under a policy where the working day begins at 5:00 PM and ends at 5:00 PM the following day.

As in the previous example, you will create two new fields:

- deposit\_due\_date: The date when the deposit should be received. This is the end of the day three days before the service\_date.
- final\_payment\_due\_date: The date when the final payment should be received. This is the end of the day seven days after the service\_date.

Load Script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Services:
Load
service_id,
service_date,
amount
Inline
[
service_id, service_date,amount
1,03/11/2022 9:25:14 AM,231.24
2,03/12/2022 10:06:54 AM,567.28
3,03/13/2022 10:44:42 AM,364.28
4,03/14/2022 11:33:30 AM,575.76
5,03/15/2022 12:58:14 PM,638.68
6,03/16/2022 4:23:12 PM,785.38
7,03/17/2022 6:42:15 PM,967.46
8,03/18/2022 7:41:16 PM,287.67
9,03/19/2022 8:14:15 PM,764.45
10,03/20/2022 9:23:51 PM,875.43
11,03/21/2022 10:04:41 PM,957.35
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

service\_date.

To create the deposit\_due\_date field, create this [measure](#glossary-4 "Glossary term").

=dayend(service\_date,-3,17/24).

Then, to create the final\_payment\_due\_date field, create this measure:

=dayend(service\_date,7,17/24).

Results table

| service\_date | =dayend(service\_date,-3,17/24) | =dayend(service\_date,7,17/24 |
| --- | --- | --- |
| 03/11/2022 | 3/8/2022 16:59:59 PM | 3/18/2022 16:59:59 PM |
| 03/12/2022 | 3/9/2022 16:59:59 PM | 3/19/2022 16:59:59 PM |
| 03/13/2022 | 3/10/2022 16:59:59 PM | 3/20/2022 16:59:59 PM |
| 03/14/2022 | 3/11/2022 16:59:59 PM | 3/21/2022 16:59:59 PM |
| 03/15/2022 | 3/12/2022 16:59:59 PM | 3/22/2022 16:59:59 PM |
| 03/16/2022 | 3/13/2022 16:59:59 PM | 3/23/2022 16:59:59 PM |
| 03/17/2022 | 3/14/2022 16:59:59 PM | 3/24/2022 16:59:59 PM |
| 03/18/2022 | 3/15/2022 16:59:59 PM | 3/25/2022 16:59:59 PM |
| 03/19/2022 | 3/16/2022 16:59:59 PM | 3/26/2022 16:59:59 PM |
| 03/20/2022 | 3/17/2022 16:59:59 PM | 3/27/2022 16:59:59 PM |
| 03/21/2022 | 3/18/2022 16:59:59 PM | 3/28/2022 16:59:59 PM |

The values of the new fields are in the TimestampFormat M/D/YYYY h:mm:ss[.fff] TT. Because the function dayend() was used, the timestamp values are all the last millisecond of the day.

The payment due date values are three days before the service date because the second argument passed in the dayend() function is negative.

The final payment due date values are seven days after the service date because the second argument passed in the dayend() function is positive.

The dates have a timestamp of the last millisecond before 5:00 PM because the value of the third argument, day\_start,that passed into the dayend() function is 17/24.

## Learn more

- [*Loading data from a previously loaded table*](../load-data-from-previously-loaded-table.htm)

Arguments

| Argument | Description |
| --- | --- |
| time | The timestamp to evaluate. |
| period\_no | period\_no is an integer, or expression that resolves to an integer, where the value 0 indicates the day that contains time. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | To specify that days do not starting at midnight, indicate an offset as a fraction of a day in day\_start. For example, 0.125 to denote 3:00 AM. |
