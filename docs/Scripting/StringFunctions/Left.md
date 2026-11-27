---
title: "Left Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Left.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Left Script and chart function

Expand/Collapse all

# Left Script and chart function

Left() returns a string consisting of the first (leftmost) characters of the input string, where the number of characters is determined by the second argument.

Syntax:

Left(text, count)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| count | Defines the number of characters to included from the left-hand part of the string text. |

Example: Chart expression

| Example | Result |
| --- | --- |
| Left( 'abcdef', 3 ) | Returns abc |

## Example - Left fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - InputText
  - NoOfChars

Load script

```
Example:
Load * inline [
InputText, NoOfChars
'abcdef', 3
'2021-07-14', 4
'2021-07-14', 2
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputText
- NoOfChars

Create the following calculated dimension:

- =Left(InputText,NoOfChars)

Results table

| InputText | NoOfChars | Left(InputText,NoOfChars) |
| --- | --- | --- |
| abcdef | 3 | abc |
| 2021-07-14 | 2 | 20 |
| 2021-07-14 | 4 | 2021 |

The first row returns abc, as these are the first 3 characters from the left of the string InputText.

The second row returns 20, as these are the first 2 characters from the left of the string InputText.

The third row returns 2021, as these are the first 4 characters from the left of the string InputText.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load
*,
left(Text,NoOfChars) as Left;
Load * inline [
Text, NoOfChars
'abcdef', 3
'2021-07-14', 4
'2021-07-14', 2
];
```

Results table

| Text | NoOfChars | Left |
| --- | --- | --- |
| abcdef | 3 | abc |
| 2021-07-14 | 4 | 2021 |
| 2021-07-14 | 2 | 20 |

## Example - Left scenario

Chart expression

Overview

This example parses the order codes in a dataset, which contain a region code, year, and order number, to create a new field for data analysis.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - OrderID
  - CustomerName
  - SalesAmount

Load script

```
Example:
Load * inline [
OrderID, CustomerName, SalesAmount
US2024001, John Doe, 1500
EU2024002, Jane Smith, 2300
AS2024003, Mike Davis, 1800
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- OrderID
- CustomerName
- SalesAmount

Create the following calculated dimension:

- =Left(OrderID, 2) to calculate the region.

Results table

| OrderID | CustomerName | SalesAmount | Left(OrderID, 2) |
| --- | --- | --- | --- |
| AS2024003 | Mike Davis | 1800 | AS |
| EU2024002 | Jane Smith | 2300 | EU |
| US2024001 | John Doe | 1500 | US |

The output from the Left function parses the OrderID to extract the region, creating a new field to use for further data analysis.

## Example - Left advanced scenario

Chart expression

Overview

This example parses the product codes in a dataset, which contain a department category code and a unique identifier, to create a new field for data analysis.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called ProductCode.

Load script

```
Example:
Load * inline [
ProductCode
ELC12345
HOM67890
FAS09876
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- ProductCode

Create the following calculated dimension:

- =Pick(Match(left(ProductCode,3),'ELC','HOM','FAS'),'Electronics','Home Appliances','Fashion'), to calculate the department.

Results table

| ProductCode | Pick(Match(left(ProductCode,3),'ELC','HOM','FAS'),'Electronics','Home Appliances','Fashion') |
| --- | --- |
| ELC12345 | Electronics |
| FAS09876 | Fashion |
| HOM67890 | Home Appliances |

The output uses the Pick, Match, and Left functions to extract the department from the product code, creating a new field for data analysis.

See also [*Index Script and chart function*](Index.htm),
which allows more complex string analysis.
