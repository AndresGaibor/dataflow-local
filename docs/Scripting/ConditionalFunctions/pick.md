---
title: "pick Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/pick.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---
Expand/Collapse all

# pick Script and chart function

The pick function returns the n:th expression
in the list.

[Video: https://share.vidyard.com/watch/i2VAER2iYbPyuC46aLGxG3]

Syntax:

pick(n, expr1[ , expr2,...exprN])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| n | n is an integer between 1 and N. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `pick( N, 'A','B',4, 6 )` | returns `B` if `N` = `2` returns `4` if `N` = `3` |

## Example - Assign labels to products using pick

Chart expression

Overview

A data set contains product data. You want to assign category labels to products based on the category code.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductID`
  - `ProductName`
  - `CategoryCode`

Load script

```
Example:
LOAD * INLINE [
ProductID, ProductName, CategoryCode
1, "Laptop", 1
2, "Headphones", 2
3, "Printer", 3
4, "Smartphone", 1
5, "Tablet", 1
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ProductID`
- `ProductName`
- `CategoryCode`

Create the following measure:

- `=Pick(CategoryCode, 'Electronics', 'Accessories', 'Office Equipment')`, to return a valid expression from the list.

Results table

| ProductID | ProductName | CategoryCode | Pick(CategoryCode, 'Electronics', 'Accessories', 'Office Equipment') |
| --- | --- | --- | --- |
| 1 | Laptop | 1 | Electronics |
| 2 | Headphone | 2 | Accessories |
| 3 | Printer | 3 | Office Equipment |
| 4 | Smartphone | 1 | Electronics |
| 5 | Tablet | 1 | Electronics |

The `pick` function returns a list of values associated with the corresponding index from the `CategoryCode` numeric field. For example, the label `Electronics` is the first parameter in the function and is returned for all products with the `CategoryCode` of `1`.

## Example - Assign region labels using pick

Chart expression

Overview

A data set contains country and region codes. You want to assign region labels to countries based on the region code.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Country`
  - `RegionCode`

Load script

```
Example:
LOAD * INLINE [
Country, RegionCode
"USA", 1
"Canada", 1
"Germany", 2
"Japan", 3
"Australia", 4
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Country`
- `RegionCode`

Create the following measure:

- `=Pick(RegionCode, 'North America', 'Europe', 'Asia', 'Australia')`, to return a valid item from the list.

Results table

| Country | RegionCode | Pick(RegionCode, 'North America', 'Europe', 'Asia', 'Australia') |
| --- | --- | --- |
| Australia | 4 | Australia |
| Canada | 1 | North America |
| Germany | 2 | Europe |
| Japan | 3 | Asia |
| USA | 1 | North America |

The `pick` function returns a list of values associated with the corresponding index from the `RegionCode` numeric field. For example, the label `North America` is the first parameter in the function and is returned for all countries with the `RegionCode` of `1`.

## Example - Combining pick and match to translate lists of alternative text matches

Chart expression

Overview

This advanced scenario describes how to effectively use a combination of the `pick` and `match` functions to map text matches in-line. In programming terms, this serves a similar purpose to a `Case` statement. The scenario explores this functionality by mapping country names to region-equivalent names, while also providing a default `Region` value for any previously unmapped `Country` names.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Countries`.

  - The data table has one field called `Country`.

Load script

```
Countries:
LOAD * INLINE [
Country
"USA"
"Canada"
"Germany"
"Japan"
"Australia"
"South Africa"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Country`
- `RegionCode`

Create the following measure:

- `=Pick(1+match(Country,'USA','Canada','Germany','Japan','Australia'), 'Unmapped', 'North America', 'North America', 'Europe', 'Asia', 'Australia')`

The `match` function will return the index match of the comma-separated alternatives supplied, starting from `1 = ‘USA’`, `2 = ‘Canada’` and so on. If no match is found, zero is returned. This result is then incremented by `1` and fed into the `pick` function, such that `1 = default value` if no match is found, `2 = ‘USA’`, `3 = ‘Canada’` and so on.

This combination of `Match` and `Pick` function calls will then decode the matching `Country` names into an equivalent `Region` name. Any unmapped `Country` values will return the default `Region` value, `Unmapped`.

Results table

| Country | Pick(1+match(Country,'USA','Canada','Germany','Japan','Australia'), 'Unmapped', 'North America', 'North America', 'Europe', 'Asia', 'Australia') |
| --- | --- |
| Australia | Australia |
| Canada | North America |
| Germany | Europe |
| Japan | Asia |
| South Africa | Unmapped |
| USA | North America |
