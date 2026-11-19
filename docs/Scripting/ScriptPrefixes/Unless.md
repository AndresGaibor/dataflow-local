---
title: "Unless"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Unless.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
Expand/Collapse all

# Unless

The unless prefix and suffix
is used for creating a conditional clause which determines whether a statement
or exit clause should be evaluated or not. It may be seen as a compact
alternative to the full if..end if
statement.

Syntax:

(Unless condition
statement | exitstatement Unless condition )

The statement or the exitstatement will only be executed
if condition is evaluated to
False.

The unless prefix may be used
on statements which already have one or several other statements, including
additional when or unless
prefixes.

Arguments

| Argument | Description |
| --- | --- |
| condition | A logical expression evaluating to True or False. |
| statement | Any Qlik Sense script statement except control statements. |
| exitstatement | An exit for, exit do or exit sub clause or an exit script statement. |

## When to use Unless

The `Unless` statement returns a Boolean result. Typically, this type of function will be used as a condition when the user would like to conditionally load or exclude parts of the script.

The following lines show three examples of how the `Unless` function may be used:

exit script
unless A=1;

unless A=1
LOAD \* from myfile.csv;

unless A=1
when B=2 drop table Tab1;

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Unless prefix

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The creation of variable A, which is given a value of 1.
- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Unless.htm#glossary-0 "Glossary term") which is loaded into a table named Transactions, unless the variable A = 2.

Load script

```
LET A = 1;

UNLESS A = 2

Transactions:
LOAD 
* 
Inline [
id, date, amount
1, 08/30/2018, 23.56
2, 09/07/2018, 556.31
3, 09/16/2018, 5.75
4, 09/22/2018, 125.00
5, 09/22/2018, 484.21
6, 09/22/2018, 59.18
7, 09/23/2018, 177.42
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `id`
- `date`
- `amount`

Results table

| id | date | amount |
| --- | --- | --- |
| 1 | 08/30/2018 | 23.56 |
| 2 | 09/07/2018 | 556.31 |
| 3 | 09/16/2018 | 5.75 |
| 4 | 09/22/2018 | 125.00 |
| 5 | 09/22/2018 | 484.21 |
| 6 | 09/22/2018 | 59.18 |
| 7 | 09/23/2018 | 177.42 |

Because the variable A is assigned the value of 1 at the start of the script, the condition following the `Unless` prefix is evaluated, returning a result of `FALSE`. As a result, the script continues to run the `Load` statement. In the results table, all the records from the `Transactions` table can be seen.

If this variable value is set to equal to 2, no data will be loaded into the data model.

## Example 2 – Unless suffix

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Unless.htm#glossary-1 "Glossary term") and add the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Unless.htm#glossary-2 "Glossary term") below to a new tab.

The load script starts by loading an initial dataset into a table named `Transactions`. The script is then terminated unless there are less than 10 records in the `Transactions` table.

If this condition does not result in a termination of the script, a further set of transactions is concatenated into the `Transactions` table and this process is repeated.

Load script

```
Transactions:
LOAD 
* 
Inline [
id, date, amount
1, 08/30/2018, 23.56
2, 09/07/2018, 556.31
3, 09/16/2018, 5.75
4, 09/22/2018, 125.00
5, 09/22/2018, 484.21
6, 09/22/2018, 59.18
7, 09/23/2018, 177.42
];

exit script unless NoOfRows('Transactions') < 10 ;

Concatenate
LOAD
* 
Inline [
id, date, amount
8, 10/01/2018, 164.27
9, 10/03/2018, 384.00
10, 10/06/2018, 25.82
11, 10/09/2018, 312.00
12, 10/15/2018, 4.56
13, 10/16/2018, 90.24
14, 10/18/2018, 19.32
];

exit script unless NoOfRows('Transactions') < 10 ;

Concatenate
LOAD
* 
Inline [
id, date, amount
15, 10/01/2018, 164.27
16, 10/03/2018, 384.00
17, 10/06/2018, 25.82
18, 10/09/2018, 312.00
19, 10/15/2018, 4.56
20, 10/16/2018, 90.24
21, 10/18/2018, 19.32
];

exit script unless NoOfRows('Transactions') < 10 ;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `id`
- `date`
- `amount`

Results table

| id | date | amount |
| --- | --- | --- |
| 1 | 08/30/2018 | 23.56 |
| 2 | 09/07/2018 | 556.31 |
| 3 | 09/16/2018 | 5.75 |
| 4 | 09/22/2018 | 125.00 |
| 5 | 09/22/2018 | 484.21 |
| 6 | 09/22/2018 | 59.18 |
| 7 | 09/23/2018 | 177.42 |
| 8 | 10/01/2018 | 164.27 |
| 9 | 10/03/2018 | 384.00 |
| 10 | 10/06/2018 | 25.82 |
| 11 | 10/09/2018 | 312.00 |
| 12 | 10/15/2018 | 4.56 |
| 13 | 10/16/2018 | 90.24 |
| 14 | 10/18/2018 | 19.32 |

There are seven records in each of the three datasets of the load script.

The first dataset (with transaction `id` 1 through 7) is loaded into the application. The `Unless` condition evaluates whether there are less than 10 rows in the `Transactions` table. This evaluates to `TRUE`, and therefore the second dataset (with transaction `id` 8 through 14) is loaded into the application. The second `Unless` condition evaluates if there are less than 10 records in the `Transactions` table. This evaluates to `FALSE`, and so the script terminates.

## Example 3 – Multiple Unless prefixes

Load script and results

Overview

Open the Data load editor and add the load script below to a new tab.

In this example, a dataset containing one transaction is created as a table called `Transactions`.
A 'for' loop is then triggered, in which two nested unless statements evaluate:

1. Unless there are more than 100 records in the `Transactions` table
2. Unless the number of records in the `Transactions` table is a multiple of 6

If these conditions are `FALSE`, a further seven records are generated and concatenated onto the existing `Transactions` table. This process is repeated until one of the two transactions returns a value of `TRUE`.

Load script

```
Transactions:
Load
        0 as id
Autogenerate 1;

For i = 1 to 100
        unless NoOfRows('Transactions') > 100 unless mod(NoOfRows('Transactions'),6) = 0
                Concatenate
      Load
if(isnull(Peek(id)),1,peek(id)+1) as id
		Autogenerate 7;	
next i
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`id`.

Results table

| id |
| --- |
| 0 |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| +30 more rows |

The nested unless statements that occur in the 'for' loop evaluate the following:

1. Are there more than 100 rows in the `Transactions` table?
2. Is the total number of records in the `Transactions` table a multiple of 6?

Whenever both unless statements return a value of `FALSE`, a further seven records are generated and concatenated onto the existing `Transactions` table.

These statements return a value of `FALSE` five times, at which point there are a total of 36 rows of data in the `Transactions` table.

After this, the second `Unless` statement returns a value of `TRUE`, and therefore the load statement following this will no longer be executed.
