---
title: "Right Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Right.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Right Script and chart function

Right() returns a string consisting of the last (rightmost)
characters of the input string, where the number of characters is determined by the second argument.

Syntax:

Right(text, count)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| count | Defines the number of characters to be included from the rightmost part of the string text. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `Right( 'abcdef', 3 )` | Returns `def` |

## Example - Right fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `InputText`
  - `NoOfChars`

Load script

```
Example:
Load * inline [
InputText, NoOfChars
'abcdef', 3
'2021-07-14', 5
'2021-07-14', 2
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `InputText`
- `NoOfChars`

Create the following calculated dimension:

- `=Right(InputText,NoOfChars)`, to calculate the characters in `InputText` that need to be extracted from the right-most side.

Results table

| InputText | NoOfChars | Right(InputText,NoOfChars) |
| --- | --- | --- |
| 2021-07-14 | 5 | 07-14 |
| abcdef | 3 | def |
| 2021-07-14 | 2 | 14 |

The first row returns `07-14`, as these are the first 5 characters from the right of the string `InputText`.

The second row returns `def`, as these are the first 3 characters from the right of the string `InputText`.

The third row returns `14`, as these are the first 2 characters from the right of the string `InputText`.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load
*,
right(Text,NoOfChars) as Right;
Load * inline [
Text, NoOfChars
'abcdef', 3
'2021-07-14', 5
'2021-07-14', 2
];
```

Results table

| Text | NoOfChars | Right |
| --- | --- | --- |
| abcdef | 3 | def |
| 2021-07-14 | 5 | 7-14 |
| 2021-07-14 | 2 | 14 |

## Example - Right scenario

Chart expression

Overview

This example parses the order codes in a dataset, which contain a region code and order number, to create a new field for data analysis.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `OrderID`
  - `CustomerName`
  - `SalesAmount`

Load script

```
Example:
Load * inline [
OrderID, CustomerName, SalesAmount
US1000001, John Doe, 1500
EU3000002, Jane Smith, 2300
AS2000003, Mike Davis, 1800
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `OrderID`
- `CustomerName`
- `SalesAmount`

Create the following calculated dimension:

- `=Right(OrderID, 7)` to split out the order number.

Results table

| OrderID | CustomerName | SalesAmount | Right(OrderID, 7) |
| --- | --- | --- | --- |
| AS2000003 | Mike Davis | 1800 | 2000003 |
| EU3000002 | Jane Smith | 2300 | 3000002 |
| US1000001 | John Doe | 1500 | 1000001 |

Compare the output of the `Right` function with the input `OrderID`. The calculated dimension derives a numeric value that can now be used for tasks such as sorting the output in numerical order rather than alphabetical.
