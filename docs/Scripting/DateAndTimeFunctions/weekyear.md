---
title: "weekyear Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekyear.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# weekyear Script and chart function

Expand/Collapse all

# weekyear Script and chart function

This function returns the year to which the week number belongs according to the environment [variables](#glossary-0 "Glossary term"). The week number ranges between
1 and approximately 52.

Syntax:

weekyear(timestamp [, first\_week\_day [, broken\_weeks [, reference\_day]]])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The date or timestamp to evaluate. |
| first\_week\_day | Specifies the day on which the week starts. If omitted, the value of [variable](#glossary-1 "Glossary term") FirstWeekDay is used.  The possible values first\_week\_day are 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, and 6 for Sunday.  For more information about the system variable, see [*FirstWeekDay*](../NumberInterpretationVariables/FirstWeekDay.htm). |
| broken\_weeks | If you don't specify broken\_weeks, the value of variable BrokenWeeks will be used to define if weeks are broken or not.  For more information about the system variable, see [*BrokenWeeks*](../NumberInterpretationVariables/BrokenWeeks.htm) |
| reference\_day | If you don't specify reference\_day, the value of variable ReferenceDay will be used to define which day in January to set as reference day to define week 1. By default, Qlik Sense functions use 4 as the reference day. This means that week 1 must contain January 4, or put differently, that week 1 must always have at least 4 days in January.  For more information about the system variable, see [*ReferenceDay*](../NumberInterpretationVariables/ReferenceDay.htm) |

The weekyear() function determines which week of a year a date falls into. It then returns the year corresponding to that week number.

If BrokenWeeks is set to 0 (false), weekyear() will return the same as year().

Diagram of weekyear() function's range

![Diagram that shows the range of time that the weekyear() function evaluates. The weekyear() identifies the year that a week number took place in. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekyear-diagram1.png "Click to view full size")

However, if the BrokenWeeks system variable is set to use unbroken weeks, week 1 must only contain a certain number of days in January based on the value specified in the ReferenceDay system variable.

For example, if a ReferenceDay value of 4 is used, week 1 must include at least four days in January. It is possible for week 1 to include dates in December of the previous year or for the final week number of a year to include dates in January of the following year. In situations like this, the weekyear() function will return a different value to the year() function.

Diagram of weekyear() function's range when using unbroken weeks

![Diagram that shows how the weekyear() function works with unbroken weeks. If unbroken weeks are used, the weekyear() function will return a different value than the year() function. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekyear-diagram2.png "Click to view full size")

When to use weekyear

The weekyear() function is useful when you would like to compare aggregations by years. For example, if you would like to see the total sales of products by year. The weekyear() function is chosen over year() when the user would like to retain consistency with the BrokenWeeks system variable in the application.

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| weekyear('12/30/1996',0,0,4) | Returns 1997, because week 1 of 1997 starts on 12/30/1996 |
| weekyear('01/02/1997',0,0,4) | Returns 1997 |
| weekyear('12/28/1997',0,0,4) | Returns 1997 |
| weekyear('12/30/1997',0,0,4) | Returns 1998, because week 1 of 1998 starts on 12/29/1997 |
| weekyear('01/02/1999',0,0,4) | Returns 1998, because week 53 of 1998 ends on 01/03/1999 |

Related topics

| Topic | Interaction |
| --- | --- |
| [*week Script and chart function*](week.htm) | Returns an integer representing the week number according to ISO 8601 |
| [*year Script and chart function*](year.htm) | Returns an integer representing the year when the expression is interpreted as a date according to the standard number interpretation. |

## Example 1 - Broken weeks

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-3 "Glossary term") containing a set of transactions for the last week of 2020 and first week of 2021 which is loaded into a table called ‘Transactions’.
- The BrokenWeeks variable which is set to 1.
- A [preceding load](#glossary-4 "Glossary term") which contains the following:

  - The weekyear() function, set as the [field](#glossary-5 "Glossary term") ‘week\_year’ that returns the year in which the transactions took place.
  - The week() function, set as the field ‘week’ that shows the week number of each transaction date.

Load script

```
SET BrokenWeeks=1;

Transactions:
	Load
       *,
       week(date) as week,
       weekyear(date) as week_year
       ;
Load
*
Inline
[
id,date,amount
8176,12/28/2020,19.42
8177,12/29/2020,23.80
8178,12/30/2020,82.06
8179,12/31/2020,40.56
8180,01/01/2021,37.23
8181,01/02/2021,17.17
8182,01/03/2021,88.27
8183,01/04/2021,57.42
8184,01/05/2021,67.42
8185,01/06/2021,23.80
8186,01/07/2021,82.06
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week
- week\_year

Results table

| id | date | week | week\_year |
| --- | --- | --- | --- |
| 8176 | 12/28/2020 | 53 | 2020 |
| 8177 | 12/29/2020 | 53 | 2020 |
| 8178 | 12/30/2020 | 53 | 2020 |
| 8179 | 12/31/2020 | 53 | 2020 |
| 8180 | 01/01/2021 | 1 | 2021 |
| 8181 | 01/02/2021 | 1 | 2021 |
| 8182 | 01/03/2021 | 2 | 2021 |
| 8183 | 01/04/2021 | 2 | 2021 |
| 8184 | 01/05/2021 | 2 | 2021 |
| 8185 | 01/06/2021 | 2 | 2021 |
| 8186 | 01/07/2021 | 2 | 2021 |

The ‘week\_year’ field is created in the preceding load statement by using the weekyear() function and passing the date field as the function’s argument.

The BrokenWeeks system variable is set to 1 meaning that the application uses broken weeks. Week 1 begins on January 1.

Diagram of weekyear() function's range with the use of broken weeks

![Diagram that shows the weekyear() function identifies that transaction 8181 took place in week 1 and returns the year of that week, 2021. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekyear-examples1_and3-diagram.png "Click to view full size")

Transaction 8181 takes place on January 2, which is part of week 1. Therefore, it returns a value of 2021 for the ‘week\_year’ field.

## Example 2 - Unbroken weeks

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for the last week of 2020 and first week of 2021 which is loaded into a table called ‘Transactions’.
- The BrokenWeeks variable which is set to 0.
- A preceding load which contains the following:

  - The weekyear() function, set as the field ‘week\_year’ that returns the year in which the transactions took place.
  - The week() function, set as the field ‘week’ that shows the week number of each transaction date.

However, in this example, the company policy is to use unbroken weeks.

Load script

```
SET BrokenWeeks=0;

Transactions:
	Load
       *,
       week(date) as week,
       weekyear(date) as week_year
       ;
Load
*
Inline
[
id,date,amount
8176,12/28/2020,19.42
8177,12/29/2020,23.80
8178,12/30/2020,82.06
8179,12/31/2020,40.56
8180,01/01/2021,37.23
8181,01/02/2021,17.17
8182,01/03/2021,88.27
8183,01/04/2021,57.42
8184,01/05/2021,67.42
8185,01/06/2021,23.80
8186,01/07/2021,82.06
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- week
- week\_year

Results table

| id | date | week | week\_year |
| --- | --- | --- | --- |
| 8176 | 12/28/2020 | 53 | 2020 |
| 8177 | 12/29/2020 | 53 | 2020 |
| 8178 | 12/30/2020 | 53 | 2020 |
| 8179 | 12/31/2020 | 53 | 2020 |
| 8180 | 01/01/2021 | 53 | 2020 |
| 8181 | 01/02/2021 | 53 | 2020 |
| 8182 | 01/03/2021 | 1 | 2021 |
| 8183 | 01/04/2021 | 1 | 2021 |
| 8184 | 01/05/2021 | 1 | 2021 |
| 8185 | 01/06/2021 | 1 | 2021 |
| 8186 | 01/07/2021 | 1 | 2021 |

The BrokenWeeks system variable is set to 0 meaning that the application uses unbroken weeks. Therefore, week 1 is not required to begin on January 1.

Week 53 of 2020 continues until the end of January 2, 2021, with week 1 of 2020 beginning on Sunday, January 3, 2021.

Diagram of weekyear() function's range with the use of unbroken weeks

![Diagram that shows how the weekyear() function works with unbroken weeks and that week 53 has days in 2020 and 2021. Transaction 8181 takes place on January 2 but the weekyear() function identifies its year as 2020 because of the unbroken weeks. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekyear-example2-diagram.png "Click to view full size")

Transaction 8181 takes place on January 2, which is part of week 1. Therefore, it returns a value of 2021 for the ‘week\_year’ field.

## Example 3 - Chart object example

Load script and chart expression

Overview

The same dataset and scenario as the first example are used.

However, in this example the dataset is unchanged and loaded into the application. The calculation that returns the week number of the year when the transactions took place is created as a [measure](#glossary-6 "Glossary term") in a chart in the application.

Load script

```
SET BrokenWeeks=1;

Transactions:
Load
*
Inline
[
id,date,amount
8176,12/28/2020,19.42
8177,12/29/2020,23.80
8178,12/30/2020,82.06
8179,12/31/2020,40.56
8180,01/01/2021,37.23
8181,01/02/2021,17.17
8182,01/03/2021,88.27
8183,01/04/2021,57.42
8184,01/05/2021,67.42
8185,01/06/2021,23.80
8186,01/07/2021,82.06
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date

To calculate the week that a transaction takes place in, create the following measure:

- =week(date)

To calculate the year that a transaction takes place in based on the week number, create the following measure:

- =weekyear(date)

Results table

| id | date | week | week\_year |
| --- | --- | --- | --- |
| 8176 | 12/28/2020 | 53 | 2020 |
| 8177 | 12/29/2020 | 53 | 2020 |
| 8178 | 12/30/2020 | 53 | 2020 |
| 8179 | 12/31/2020 | 53 | 2020 |
| 8180 | 01/01/2021 | 1 | 2021 |
| 8181 | 01/02/2021 | 1 | 2021 |
| 8182 | 01/03/2021 | 2 | 2021 |
| 8183 | 01/04/2021 | 2 | 2021 |
| 8184 | 01/05/2021 | 2 | 2021 |
| 8185 | 01/06/2021 | 2 | 2021 |
| 8186 | 01/07/2021 | 2 | 2021 |

The ‘week\_year’ field is created in the preceding load statement by using the weekyear() function and passing the date field as the function’s argument.

The BrokenWeeks system variable is set to 1 meaning that the application uses broken weeks. week 1 begins on January 1.

Diagram of weekyear() function's range with the use of broken weeks

![Diagram that shows the weekyear() function identifies that transaction 8181 took place in week 1 and returns the year of that week, 2021. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-weekyear-examples1_and3-diagram.png "Click to view full size")

Transaction 8181 takes place on January 2, which is part of week 1. Therefore, it returns a value of 2021 for the ‘week\_year’ field.

## Example 4 - Scenario

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a set of transactions for the last week of 2020 and first week of 2021 which is loaded into a table called ‘Transactions’.
- The BrokenWeeks variable which is set to 0. This means the application will use unbroken weeks.
- The ReferenceDay variable which is set to 2. This means the year will begin on January 2 and will contain a minimum of two days in January.
- The FirstWeekDay variable which is set to 1. This means the first day of the week will be Tuesday.

The company policy is to use broken weeks. The end user would like a chart that presents the total sales by year. The application uses unbroken weeks with week 1 containing a minimum of two days in January.

Load script

```
SET BrokenWeeks=0;
SET ReferenceDay=2;
SET FirstWeekDay=1;

Transactions:
Load
*
Inline
[
id,date,amount
8176,12/28/2020,19.42
8177,12/29/2020,23.80
8178,12/30/2020,82.06
8179,12/31/2020,40.56
8180,01/01/2021,37.23
8181,01/02/2021,17.17
8182,01/03/2021,88.27
8183,01/04/2021,57.42
8184,01/05/2021,67.42
8185,01/06/2021,23.80
8186,01/07/2021,82.06
];
```

Results

Load the data and open a [sheet](#glossary-7 "Glossary term"). Create a new table.

To calculate the year that a transaction takes place in based on the week number, create the following measure:

- =weekyear(date)

To calculate total sales, create the following measure:

- sum(amount)

Set the measure’s Number Formatting to Money.

Results table

| weekyear(date) | =sum(amount) |
| --- | --- |
| 2020 | 19.42 |
| 2021 | 373.37 |
