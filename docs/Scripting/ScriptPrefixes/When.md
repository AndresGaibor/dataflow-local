---
title: "When"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/When.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
Expand/Collapse all

# When

The when prefix and suffix is
used for creating a conditional clause which determines whether a statement
or exit clause should be executed or not. It may be seen as a compact
alternative to the full if..end if
statement.

Syntax:

(when condition
statement | exitstatement when condition )

Return data type:  Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

The statement or the exitstatement will only be executed
if condition is evaluated to TRUE.

The `When` prefix may be used
on statements which already have one or several other statements, including
additional `When` or `Unless`
prefixes.

When to use the When prefix

The `When` statement returns a Boolean result. Typically, this type of function will be used as a condition when the user would like to load or exclude parts of a script.

Arguments

| Argument | Description |
| --- | --- |
| condition | A logical expression evaluating to TRUE or FALSE |
| statement | Any Qlik Sense script statement except control statements. |
| exitstatement | An exit for, exit do or exit sub clause or an exit script statement. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `exit script when A=1;` | When the statement `A=1` is evaluated to be TRUE, the script will stop. |
| `when A=1 LOAD * from myfile.csv;` | When the statement `A=1` is evaluated to be TRUE, the `myfile.csv` will be loaded. |
| `when A=1 unless B=2 drop table Tab1;` | When the statement `A=1` is evaluated to be TRUE, and if `B=2` is evaluated to be FALSE, than the `Tab1` table will be dropped. |

## Example 1 – When prefix

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/When.htm#glossary-0 "Glossary term") with dates and amounts that is sent to a table named ‘`Transactions`’.
- The `Let` statement which states that the variable `A` is created and has the value of `1`.
- The `When` condition which provides the condition that if `A` equals `1`, then the script will continue to load.

Load script

```
LET A = 1; 

WHEN A = 1 
 
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

- id
- date
- amount

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

Because the variable `A` is assigned the value of `1` at the start of the script, the condition following the `When` prefix is evaluated and returns a result of TRUE. Because it returns a TRUE result, the script continues to run the load statement. All the records from the results table can be seen.

If this variable value was set to any value not equal to `1`, no data would be loaded into the data model.

## Example 2 – When suffix

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Three datasets with dates and amounts that are sent to a table named ‘`Transactions`’.

  - The first dataset contains transactions 1-7.
  - The second dataset contains transactions 8-14.
  - The third dataset contains transactions 15-21.
- A `When` condition which determines whether the ‘`Transactions`’ table contains more than ten rows. If any of the `When` statements are evaluated to be TRUE, the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/When.htm#glossary-1 "Glossary term") will stop. This condition is placed at the end of each of the three datasets.

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
 
exit script when NoOfRows('Transactions') > 10 ; 

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

exit script when NoOfRows('Transactions') > 10 ; 
 
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
 
exit script when NoOfRows('Transactions') > 10 ;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- id
- date
- amount

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

There are seven transactions in each of the three datasets. The first dataset contains transaction 1-7 and is loaded into the application. The `When` condition following this load statement is evaluated as FALSE because there are less than ten rows in the ‘`Transactions`’ table. The load script continues to the next dataset.

The second dataset contains transaction 8-14 and is loaded into the application. The second `When` condition evaluates as TRUE because there are more than ten rows in the ‘`Transactions`’ table. Therefore, the script terminates.

## Example 3 – Multiple When prefixes

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset containing a single transaction is created as a table called '`Transactions`'.
- A `For` loop which is triggered contains two nested `When` conditions which evaluate whether:

  1. There are less than `100` records in the '`Transactions`' table.
  2. The number of records in the '`Transactions`' table is not a multiple of `6`.

Load script

```
RowsCheck = NoOfRows('Transactions') < 100 or mod(NoOfRows('Transactions'),6) <> 0;
Transactions: 
Load 
	0 as id 
Autogenerate 1; 
For i = 1 to 100 
	when(RowsCheck)
		Concatenate 
	Load 
		if(isnull(Peek(id)),1,peek(id)+1) as id 
	Autogenerate 7;     
next i
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `id`

The results table only shows the first five transaction IDs but the load script creates 36 rows and then terminates once the `When` condition is fulfilled.

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

The nested `When` conditions in the `For` loop evaluate the following questions:

- Are there less than 100 rows in the '`Transactions`' table?
- Is the total number of records in the '`Transactions`' table not a multiple of six?

Whenever both `When` conditions return a value of TRUE, a further seven records are generated and concatenated onto the existing ‘`Transactions`’ table.

The `When` conditions return a TRUE value five times. At that point there are a total of 36 rows of data in the ‘`Transactions`’ table.

When 36 rows of data are created in the '`Transactions`' table, the second `When` statement returns a value of FALSE and therefore the load statement following this will no longer be executed.
