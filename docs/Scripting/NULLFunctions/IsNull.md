---
title: "IsNull Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/IsNull.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "NULL functions"]
---
Expand/Collapse all

# IsNull Script and chart function

The IsNull function tests if the value of an expression is NULL and if so, returns -1 (True), otherwise 0 (False).

Syntax:

IsNull(expr
)

> **Note:** A string with length zero is not considered as a NULL and will cause IsNull to return False.

Return data type:  Boolean

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |

Example: Chart expression

| Example | Result |
| --- | --- |
| IsNull(Productname) | Returns `-1` (True) if `ProductName` is a null value, otherwise `0` (False). |

## Example - IsNull fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ID`
  - `Value`

Load script

```
Example:
LOAD * Inline
[ID, Value
0,
1,NULL
2,-
3,378];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Value`

Create the following calculated dimensions:

- `=If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value )`, to return `NULL` if the `Value` field has no value, a dash (-) character, or the value `NULL`, otherwise return the value.
- `=If(IsNull(If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value )), 'T', 'F')`, to return the value `T` (True) or `F` (False) depending on whether the `Value` field contains a null value or not.

Results table

| ID | Value | If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value ) | If(IsNull(If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value )), 'T', 'F') |
| --- | --- | --- | --- |
| 0 |  | - | T |
| 1 | NULL | - | T |
| 2 | - | - | T |
| 3 | 378 | 378 | F |

The `Value` column shows the data as entered in the dataset. The first measure (column 3) returns `NULL` for the first 3 rows whose value met the conditions of the `IF` statement: `len(trim(Value))= 0 or Value='NULL' or Value='-'`. The last row returns the value as entered, `378`.

The second measure (column 4) takes the value of the expression in column 3 and returns `T` if `NULL` or `F` if not `NULL`. The results show that the first 3 rows are null values.

Load script

In this example, an inline table with four rows is loaded, where the first three lines contain either nothing, a dash - or the text NULL in the `Value` column. We convert these values to true NULL value representations with the middle preceding LOAD using the Null function.

The first preceding LOAD adds a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/IsNull.htm#glossary-0 "Glossary term") that checks if the value is NULL,using the IsNull function.

```
NullsDetectedAndConverted:
LOAD *,
If(IsNull(ValueNullConv), 'T', 'F') as IsItNull;

LOAD *,
If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value ) as ValueNullConv;

LOAD * Inline
[ID, Value
0,
1,NULL
2,-
3, 378];
```

Below is the resulting table. In the `ValueNullConv` column, the `NULL` values are represented by `-`.

Results table

| ID | Value | ValueNullConv | IsItNull |
| --- | --- | --- | --- |
| 0 |  | - | T |
| 1 | NULL | - | T |
| 2 | - | - | T |
| 3 | 378 | 378 | F |

## Example - IsNull scenario

Chart expression

Overview

A dataset of sales data is analyzed to see which fields have null values.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- A `NULLINTERPRET` variable set to `NULL`.
- The following fields in the data table:

  - `SalesID`
  - `Name`
  - `Age`
  - `Email`
  - `Region`
  - `Status`

Load script

```
Set NULLINTERPRET = NULL;
Example:
LOAD * Inline [
SalesID, Name, Age, Email, Region, Status
1, John Smith, 30, john@email.com, North, Active
2, Jane Doe, NULL, jane@email.com, South, Active
3, Bob Johnson, 45, NULL, East, Inactive
4, Alice Brown, 28, alice@email.com, West, Active
5, Charlie Lee, NULL, charlie@email.com, NULL, Active
6, Eva Green, 35, eva@email.com, North, NULL
7, David White, 50, NULL, South, Inactive
8, Fiona Black, 42, fiona@email.com, East, Active
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `SalesID`
- `Name`

Create the following calculated dimensions:

- `=If(IsNull(Age), 'Age unavailable', Age)`, to populate the `Age` field with the value `Age unavailable` if it is `NULL`.
- `=If(IsNull(Email), 'Email unavailable', Email)`, to populate the `Email` field with the value `Email unavailable` if it is `NULL`.
- `=If(IsNull(Region), 'Region unavailable', Region)`, to populate the `Region` field with the value `Region unavailable` if it is `NULL`.

Results table

| SalesID | Name | If(IsNull(Age), 'Age unavailable', Age | If(IsNull(Email), 'Email unavailable', Email) | If(IsNull(Region), 'Region unavailable', Region) |
| --- | --- | --- | --- | --- |
| 1 | John Smith | 30 | john@email.com | North |
| 2 | Jane Doe | Age unavailable | jane@email.com | South |
| 3 | Bob Johnson | 45 | Email unavailable | East |
| 4 | Alice Brown | 28 | alice@email.com | West |
| 5 | Charlie Lee | Age unavailable | charlie@email.com | Region unavailable |
| 6 | Eva Green | 35 | eva@email.com | North |
| 7 | David White | 50 | Email unavailable | South |
| 8 | Fiona Black | 42 | fiona@email.com | East |

The results of the `IsNull` function, which checks for and returns true if null values are found, indicate that several fields in the dataset contain null values. For example, a null value was identified in the `Age` column for `Charlie Lee`, and the output `Age unavailable` was returned.
