---
title: "EmptyIsNull Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/EmptyIsNull.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "NULL functions"]
---
Expand/Collapse all

# EmptyIsNull Script and chart function

The EmptyIsNull function converts empty strings to NULL. Hence, it returns NULL if the parameter is an empty string, otherwise it returns the parameter.

Syntax:

EmptyIsNull(exp
)

Return data type:  NULL if the parameter is an empty string, otherwise it returns the parameter

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| EmptyIsNull(AdditionalComments) | This expression will return NULL for any empty string values of the `AdditionalComments` [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/EmptyIsNull.htm#glossary-0 "Glossary term") instead of empty strings. Non-empty strings and numbers are returned. |
| EmptyIsNull(PurgeChar(PhoneNumber, ' -()')) | This expression will strip any dashes, spaces, and parentheses from the `PhoneNumber` field. If there are no characters left, the `EmptyIsNull` function returns the empty string as NULL; an empty phone number is the same as no phone number. |

## Example - EmptyIsNull fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `CustomerID`
  - `OrderID`
  - `Product`
  - `Status`
  - `PhoneNumber`

Load script

```
Example:
LOAD * inline [
CustomerID, OrderID, Product, Status, PhoneNumber
1, 1001, Widget,, (0123) 456 789
2, 1002, Gizmo, Open,-
3, 1003, Gadget, Closed,()
4, 1004, Widget,,678-9888
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `CustomerID`
- `OrderID`
- `Product`
- `Status`

Create the following calculated dimensions:

- `=EmptyIsNull(Status)`, to return as NULL any empty string values in the `Status` field.
- `=EmptyIsNull(PurgeChar(PhoneNumber, ' -()'))`, to remove any dashes, spaces, and parentheses from the `PhoneNumber` field. If there are no characters left, the `EmptyIsNull` function returns the empty string as NULL; an empty phone number is the same as no phone number.

> **Note:** The following table contains empty cells to demonstrate the use of the `EmptyIsNull` function.

Results table

| CustomerID | OrderID | Product | Status | EmptyIsNull(Status) | EmptyIsNull(PurgeChar(PhoneNumber, ' -()')) |
| --- | --- | --- | --- | --- | --- |
| 1 | 1001 | Widget |  | - | 0123456789 |
| 2 | 1002 | Gizmo | Open | Open | - |
| 3 | 1003 | Gadget | Closed | Closed | - |
| 4 | 1004 | Widget |  | - | 6789888 |

In the `Status` column, notice that the records with empty values appear as empty cells with a default transparent background color. The output of the `EmptyIsNull(Status)` measure returns NULL for these empty values, as indicated by the dash (-) character with gray cell background.

The second measure uses the `EmptyIsNull` function with the [*PurgeChar Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/PurgeChar.htm) to remove any dashes (-), spaces, and parentheses () from the `PhoneNumber` field, and then return any remaining empty strings as NULL. The cells with null values now appear with a dash (-) and gray background formatting.

## Example - Replacing null values with text and adding conditional formatting

Chart expression

Overview

A sales manager wants to analyze sales data and easily identify the records that contain missing values.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ID`
  - `Name`
  - `Age`
  - `Email`
  - `Sales`
  - `Region`
  - `OrderStatus`

Load script

```
Example:
LOAD * inline [
ID,Name, Age, Email, Sales, Region, OrderStatus
1, John Smith, 30, john@email.com, 1000, North, Active
2, Jane Doe, '', jane@email.com, 1500, South, Active
3, Bob Johnson, 45, '', 800, East, Inactive
4, Alice Brown, 28, alice@email.com, '', West, Active
5, Charlie Lee, '', charlie@email.com, 1200, '', Active
6, Eva Green, 35, eva@email.com, 950, North, ''
7, David White, 50, '', '', South, Inactive
8, Fiona Black, 42, fiona@email.com, 1100, East, Active
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `ID`

Create the following calculated dimensions:

- `=If(IsNull(EmptyIsNull(Age)), 'NULL', EmptyIsNull(Age))`, to return as NULL any empty string values in the `Age` field, and then identify and populate all null values with the value `NULL` instead of a dash (`-`) character.
- `=If(IsNull(EmptyIsNull(Email)), 'NULL', EmptyIsNull(Email))`, to return as NULL any empty string values in the `Email` field, and then identify and populate all null values with the value `NULL` instead of a dash (`-`) character.
- `=If(IsNull(EmptyIsNull(Sales)), 'NULL', EmptyIsNull(Sales))`, to return as NULL any empty string values in the `Sales` field, and then identify and populate all null values with the value `NULL` instead of a dash (`-`) character.
- `=If(IsNull(EmptyIsNull(Region)), 'NULL', EmptyIsNull(Region))`, to return as NULL any empty string values in the `Region` field, and then identify and populate all null values with the value `NULL` instead of a dash (`-`) character.
- `=If(IsNull(EmptyIsNull(OrderStatus)), 'NULL', EmptyIsNull(OrderStatus))`, to return as NULL any empty string values in the `OrderStatus` field, and then identify and populate all null values with the value `NULL` instead of a dash (`-`) character.

Set conditional cell formatting to change the background color to red for `NULL` values and green for all other values. In the **Properties** panel for each dimension and measure, enter the following expressions as the **Background color expression**:

- `ID` (dimension): `=RGB(200,255,200)`
- `Age` (measure): `=If(IsNull(EmptyIsNull(Age)), RGB(255,200,200), RGB(200,255,200))`
- `Email` (measure): `=If(IsNull(EmptyIsNull(Email)), RGB(255,200,200), RGB(200,255,200))`
- `Sales` (measure): `=If(IsNull(EmptyIsNull(Sales)), RGB(255,200,200), RGB(200,255,200))`
- `Region` (measure): `=If(IsNull(EmptyIsNull(Region)), RGB(255,200,200), RGB(200,255,200))`
- `OrderStatus` (measure): `=If(IsNull(EmptyIsNull(OrderStatus)), RGB(255,200,200), RGB(200,255,200))`

Results table

| ID | If(IsNull(EmptyIsNull(Age)), 'NULL', EmptyIsNull(Age)) | If(IsNull(EmptyIsNull(Email)), 'NULL', EmptyIsNull(Email)) | If(IsNull(EmptyIsNull(Sales)), 'NULL', EmptyIsNull(Sales)) | If(IsNull(EmptyIsNull(Region)), 'NULL', EmptyIsNull(Region)) | If(IsNull(EmptyIsNull(OrderStatus)), 'NULL', EmptyIsNull(OrderStatus)) |
| --- | --- | --- | --- | --- | --- |
| 1 | 30 | john@email.com | 1000 | North | Active |
| 2 | NULL | jane@email.com | 1500 | South | Active |
| 3 | 45 | NULL | 800 | East | Inactive |
| 4 | 28 | alice@email.com | NULL | West | Active |
| 5 | NULL | charlie@email.com | 1200 | NULL | Active |
| 6 | 35 | eva@email.com | 950 | North | NULL |
| 7 | 50 | NULL | NULL | South | Inactive |
| 8 | 42 | fiona@email.com | 1100 | East | Active |

The results show that by using the `EmptyIsNull` function and adding conditional formatting, you can easily identify records with missing values.
