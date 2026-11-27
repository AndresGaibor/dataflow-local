---
title: "inday Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inday.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# inday Script and chart function

Expand/Collapse all

# inday Script and chart function

This function returns
True if timestamp lies inside
the day containing base\_timestamp.

Syntax:

InDay (timestamp, base\_timestamp, period\_no[, day\_start])

Diagram of inday function

![Diagram that shows how the inday function is used to identify a segment of time and return boolean results based on that segment. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-inday-diagram.png "Click to view full size")

The inday() function uses the base\_timestamp argument to identify which day the timestamp falls into. The start time of the day is, by default, midnight; but you can change the start time of the day by using the day\_start argument of the inday() function. Once this day is defined, the function will return Boolean results when comparing the prescribed timestamp values to that day.

When to use inday

The inday() function returns a Boolean result. Typically, this type of function will be used as a condition in an if expression. This returns an [aggregation](#glossary-0 "Glossary term") or calculation dependent on whether a date evaluated occurred in the day of the timestamp in question.

For example, the inday() function can be used to identify all equipment manufactured in a given day.

Return data type:  Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date and time that you want to compare with base\_timestamp. |
| base\_timestamp | Date and time that is used to evaluate the timestamp. |
| period\_no | The day can be offset by period\_no. period\_no is an integer, where the value 0 indicates the day which contains base\_timestamp. Negative values in period\_no indicate preceding days and positive values indicate succeeding days. |
| day\_start | If you want to work with days not starting midnight, indicate an offset as a fraction of a day in day\_start, For example, 0.125 to denote 3 AM. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| inday ('01/12/2006 12:23:00 PM', '01/12/2006 12:00:00 AM', 0) | Returns True |
| inday ('01/12/2006 12:23:00 PM', '01/13/2006 12:00:00 AM', 0) | Returns False |
| inday ('01/12/2006 12:23:00 PM', '01/12/2006 12:00:00 AM', -1) | Returns False |
| inday ('01/11/2006 12:23:00 PM', '01/12/2006 12:00:00 AM', -1) | Returns True |
| inday ('01/12/2006 12:23:00 PM', '01/12/2006 12:00:00 AM', 0, 0.5) | Returns False |
| inday ('01/12/2006 11:23:00 AM', '01/12/2006 12:00:00 AM', 0, 0.5) | Returns True |

## Example 1 – Load statement (script)

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-1 "Glossary term") containing transactions by timestamp which is loaded into a table called Transactions.
- A date [field](#glossary-2 "Glossary term") which is provided in the TimeStamp system [variable](#glossary-3 "Glossary term") (M/D/YYYY h:mm:ss[.fff] TT) format.
- A [preceding load](#glossary-4 "Glossary term") which contains the inday() function which is set as the in\_day field.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        inday(date,'01/05/2022 12:00:00 AM', 0) as in_day
        ;
Load
*
Inline
[
id,date,amount
9497,'01/01/2022 7:34:46 PM',13.24
9498,'01/01/2022 10:10:22 PM',31.43
9499,'01/02/2022 8:35:54 AM',36.34
9500,'01/03/2022 2:21:53 PM',51.75
9501,'01/04/2022 6:49:38 PM',15.35
9502,'01/04/2022 10:58:34 PM',74.34
9503,'01/05/2022 5:40:49 AM',73.53
9504,'01/05/2022 11:29:38 AM',50.00
9505,'01/05/2022 7:04:57 PM',47.25
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day

Results table

| date | in\_day |
| --- | --- |
| 01/01/2022 7:34:46 PM | 0 |
| 01/01/2022 10:10:22 PM | 0 |
| 01/02/2022 8:35:54 AM | 0 |
| 01/03/2022 2:21:53 PM | 0 |
| 01/04/2022 6:49:38 PM | 0 |
| 01/04/2022 10:58:34 PM | 0 |
| 01/05/2022 5:40:49 AM | -1 |
| 01/05/2022 11:29:38 AM | -1 |
| 01/05/2022 7:04:57 PM | -1 |
| 01/06/2022 8:49:09 AM | 0 |

The in\_day field is created in the preceding load statement by using the inday() function and passing the date field, a hard-coded timestamp for January 5 and a period\_no of 0 as the function’s arguments.

## Example 2 – period\_no

Load script and results

Overview

The [load script](#glossary-5 "Glossary term") uses the same dataset and scenario that were used in the first example.

However, in this example, the task is to calculate whether the transaction date occurred two days before January 5.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        inday(date,'01/05/2022 12:00:00 AM', -2) as in_day
        ;
Load
*
Inline
[
id,date,amount
9497,'01/01/2022 7:34:46 PM',13.24
9498,'01/01/2022 10:10:22 PM',31.43
9499,'01/02/2022 8:35:54 AM',36.34
9500,'01/03/2022 2:21:53 PM',51.75
9501,'01/04/2022 6:49:38 PM',15.35
9502,'01/04/2022 10:58:34 PM',74.34
9503,'01/05/2022 5:40:49 AM',73.53
9504,'01/05/2022 11:29:38 AM',50.00
9505,'01/05/2022 7:04:57 PM',47.25
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day

Results table

| date | in\_day |
| --- | --- |
| 01/01/2022 7:34:46 PM | 0 |
| 01/01/2022 10:10:22 PM | 0 |
| 01/02/2022 8:35:54 AM | 0 |
| 01/03/2022 2:21:53 PM | -1 |
| 01/04/2022 6:49:38 PM | 0 |
| 01/04/2022 10:58:34 PM | 0 |
| 01/05/2022 5:40:49 AM | 0 |
| 01/05/2022 11:29:38 AM | 0 |
| 01/05/2022 7:04:57 PM | 0 |
| 01/06/2022 8:49:09 AM | 0 |

In this instance, because a period\_no of -2 is used as the offset argument in the inday() function, the function determines whether each transaction date took place on January 3. This can be verified in the output table where one transaction returns a Boolean result of TRUE.

## Example 3 – day\_start

Load script and results

Overview

The load script uses the same dataset and scenario that were used in the previous examples.

However, in this example, the company policy is that the workday begins and ends at 7 AM.

Load script

```
SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';

Transactions:
    Load
        *,
        inday(date,'01/05/2022 12:00:00 AM', 0, 7/24) as in_day
        ;
Load
*
Inline
[
id,date,amount
9497,'01/01/2022 7:34:46 PM',13.24
9498,'01/01/2022 10:10:22 PM',31.43
9499,'01/02/2022 8:35:54 AM',36.34
9500,'01/03/2022 2:21:53 PM',51.75
9501,'01/04/2022 6:49:38 PM',15.35
9502,'01/04/2022 10:58:34 PM',74.34
9503,'01/05/2022 5:40:49 AM',73.53
9504,'01/05/2022 11:29:38 AM',50.00
9505,'01/05/2022 7:04:57 PM',47.25
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- in\_day

Results table

| date | in\_day |
| --- | --- |
| 01/01/2022 7:34:46 PM | 0 |
| 01/01/2022 10:10:22 PM | 0 |
| 01/02/2022 8:35:54 AM | 0 |
| 01/03/2022 2:21:53 PM | 0 |
| 01/04/2022 6:49:38 PM | -1 |
| 01/04/2022 10:58:34 PM | -1 |
| 01/05/2022 5:40:49 AM | -1 |
| 01/05/2022 11:29:38 AM | 0 |
| 01/05/2022 7:04:57 PM | 0 |
| 01/06/2022 8:49:09 AM | 0 |

Because the start\_day argument of 7/24, which is 7 AM, is used in the inday() function, the function determines whether each transaction date took place on January 4 from 7 AM and January 5 before 7 AM.

This can be verified in the output table where transactions that take place after 7 AM on January 4 return a Boolean result of TRUE whilst transactions that take place after 7 AM on January 5 return a Boolean result of FALSE.

## Example 4 – Chart object

Load script and chart expression

Overview

The load script uses the same dataset and scenario that were used in the previous examples.

However, in this example, the dataset is unchanged and loaded into the application. You will calculate to determine if a transaction takes place on January 5 by creating a [measure](#glossary-6 "Glossary term") in a chart object.

Load script

```
Transactions:
Load
*
Inline
[
id,date,amount
9497,'01/01/2022 7:34:46 PM',13.24
9498,'01/01/2022 10:10:22 PM',31.43
9499,'01/02/2022 8:35:54 AM',36.34
9500,'01/03/2022 2:21:53 PM',51.75
9501,'01/04/2022 6:49:38 PM',15.35
9502,'01/04/2022 10:58:34 PM',74.34
9503,'01/05/2022 5:40:49 AM',73.53
9504,'01/05/2022 11:29:38 AM',50.00
9505,'01/05/2022 7:04:57 PM',47.25
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- date

To calculate whether a transaction takes place on January 5, create the following measure:

=inday(date,'01/05/2022 12:00:00 AM',0)

Results table

| date | inday(date,'01/05/2022 12:00:00 AM',0) |
| --- | --- |
| 01/01/2022 7:34:46 PM | 0 |
| 01/01/2022 10:10:22 PM | 0 |
| 01/02/2022 8:35:54 AM | 0 |
| 01/03/2022 2:21:53 PM | 0 |
| 01/04/2022 6:49:38 PM | 0 |
| 01/04/2022 10:58:34 PM | 0 |
| 01/05/2022 5:40:49 AM | -1 |
| 01/05/2022 11:29:38 AM | -1 |
| 01/05/2022 7:04:57 PM | -1 |
| 01/06/2022 8:49:09 AM | 0 |

## Example 5 – Scenario

Load script and results

Overview

In this example, it has been identified that due to equipment error, products that were manufactured on January 5 were defective. The end user would like a chart object that displays, by date, the status of which products that were manufactured were ‘defective’ or ‘faultless’ and the cost of the products manufactured on January 5.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table called ‘Products’.
- The table contains the following fields:

  - product ID
  - manufacture time
  - cost price

Load script

```
Products:
Load
*
Inline
[
product_id,manufacture_date,cost_price
9497,'01/01/2022 7:34:46 PM',13.24
9498,'01/01/2022 10:10:22 PM',31.43
9499,'01/02/2022 8:35:54 AM',36.34
9500,'01/03/2022 2:21:53 PM',51.75
9501,'01/04/2022 6:49:38 PM',15.35
9502,'01/04/2022 10:58:34 PM',74.34
9503,'01/05/2022 5:40:49 AM',73.53
9504,'01/05/2022 11:29:38 AM',50.00
9505,'01/05/2022 7:04:57 PM',47.25
9506,'01/06/2022 8:49:09 AM',74.23
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

=dayname(manufacture\_date)

Create the following measures:

- =if(only(InDay(manufacture\_date,makedate(2022,01,05),0)),'Defective','Faultless')
- =sum(cost\_price)

Set the measure’s Number Formatting to Money.

Under Appearance, turn off Totals.

Results table

| dayname(manufacture\_date) | =if(only(InDay(manufacture\_date,makedate(2022,01,05),0)),'Defective','Faultless') | =sum(cost\_price) |
| --- | --- | --- |
| 01/01/2022 | Faultless | 44.67 |
| 01/02/2022 | Faultless | 36.34 |
| 01/03/2022 | Faultless | 51.75 |
| 01/04/2022 | Faultless | 89.69 |
| 01/05/2022 | Defective | 170.78 |
| 01/06/2022 | Faultless | 74.23 |

The inday() function returns a Boolean value when evaluating the manufacturing dates of each of the products. For any product manufactured on January 5, the inday() function returns a Boolean value of TRUE and marks the products as ‘Defective’. For any product returning a value of FALSE, and therefore not manufactured on that day, it marks the products as ‘Faultless’.
