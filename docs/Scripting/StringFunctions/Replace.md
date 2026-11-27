---
title: "Replace Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Replace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Replace Script and chart function

Expand/Collapse all

# Replace Script and chart function

Replace() returns a string after replacing all occurrences of a given substring
within the input string with another
substring. The function is non-recursive and works from left to right.

Syntax:

Replace(text, from\_str, to\_str)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| from\_str | A string that may occur one or more times within the input string text. |
| to\_str | The string that will replace all occurrences of from\_str within the string text. |

Example: Chart expression

| Example | Result |
| --- | --- |
| Replace( 'abccde','cc','xyz' ) | Returns abxyzde |

## Example - Replace fundamentals

Chart expression

Overview

A dataset of customer names contains some misspellings. This example uses the Replace function to process and replace any incorrect occurrence of 'Jhon' with 'John'.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - CustomerID
  - CustomerName

Load script

```
Example:
Load * inline [
CustomerID, CustomerName
1, Jhon Smith
2, Jhon Doe
3, John Williams
4, Jhonathan Harris
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- CustomerID
- CustomerName

Create the following calculated dimension:

- =Replace(CustomerName,'Jhon','John'), to replace all instances of Jhon with John.

Results table

| CustomerID | CustomerName | Replace(CustomerName,'Jhon','John') |
| --- | --- | --- |
| 1 | Jhon Smith | John Smith |
| 2 | Jhon Doe | John Doe |
| 3 | John Williams | John Williams |
| 4 | Jhonathan Harris | Johnathan Harris |

The output of the Repeat function finds and corrects all instances of Jhon with John.

## Example - Replace scenario

Chart expression

Overview

A dataset of products uses inconsistent labeling for the category codes. For example, electrical products have multiple code variations, such as ELEC, ELC, and elc. To standardize the codes, the Replace function is used to correct all inconsistent category codes for both electrical and furniture products.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ProductID
  - CategoryCode

Load script

```
Example:
Load * inline [
ProductID, CategoryCode
1, ELEC
2, ELC
3, FURN
4, FRN
5, ELEC
6, ELC
7, elc
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ProductID
- CategoryCode

Create the following calculated dimension:

- =Replace(Replace(Upper(CategoryCode), 'ELC', 'ELEC'),'FRN', 'FURN'), to replace any instances of ELC with ELEC and any instance of FRN with FURN.

Results table

| ProductID | CategoryCode | Replace(Replace(Upper(CategoryCode), 'ELC', 'ELEC'),'FRN', 'FURN') |
| --- | --- | --- |
| 1 | ELEC | ELEC |
| 2 | ELC | ELEC |
| 3 | FURN | FURN |
| 4 | FRN | FURN |
| 5 | ELEC | ELEC |
| 6 | ELC | ELEC |
| 7 | elc | ELEC |

The output of the Replace function has replaced any instances of ELC with ELEC, and FRN with FURN. Note that the code elc was also replaced. Although the Replace function is case-sensitive, the dimension formula uses the Upper function to conform the case of all CategoryCodes before replacing the string. This effectively renders the string replacement case-insensitive.

## Learn more

- [*Replace*](../Replace.htm)
