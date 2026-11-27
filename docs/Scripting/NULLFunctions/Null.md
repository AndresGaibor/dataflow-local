---
title: "NULL Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/Null.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "NULL functions"]
---

# NULL Script and chart function

Expand/Collapse all

# NULL Script and chart function

The Null function returns a null value.

Syntax:

Null( )

Return data type: NULL

Example: Chart expressions

| Example | Result |
| --- | --- |
| If(Product = 'A', Null(),Sum(Sales)) | This expression returns NULL for Product A, otherwise it returns the sum of sales for the product. |

## Example - Null fundamentals

Chart expression

Overview

A simple dataset is used to demonstrate the different uses of the Null function.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ID
  - Value

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

- ID
- Value

Create the following calculated dimensions:

- =If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value ), to return NULL if the Value field has any of the following: no value, a dash (-) character, or the value NULL, otherwise it returns the value.
- =If(IsNull(If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value )), 'T', 'F'), to return the value T (true) or F (false) depending on whether the Value field contains a null value or not.

Results table

| ID | Value | If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value ) | If(IsNull(If(len(trim(Value))= 0 or Value='NULL' or Value='-', Null(), Value )), 'T', 'F') |
| --- | --- | --- | --- |
| 0 |  | - | T |
| 1 | NULL | - | T |
| 2 | - | - | T |
| 3 | 378 | 378 | F |

The Value column shows the data as entered in the dataset. The first measure (column 3) uses the Null function to return NULL for those values that met the conditions of the IF statement: len(trim(Value))= 0 or Value='NULL' or Value='-'. For example, the first 3 rows met the requirements and returned NULL. The last row returns the value as entered, 378.

The second measure (column 4) takes the value in column 3 and returns T if NULL or F if not NULL. The results show that the first 3 rows are null values.

Load script

In this example, an inline table with four rows is loaded, where the first three lines contain either nothing, a dash - or the text NULL in the Value column. We convert these values to true NULL value representations.

The middle preceding LOAD performs the conversion using the Null function.

The first preceding LOAD adds a [field](#glossary-0 "Glossary term") that checks if the value is NULL, just for illustration purposes in this example.

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
3, 386];
```

Below is the resulting table. In the ValueNullConv column, the NULL values are represented by -.

Results table

| ID | Value | ValueNullConv | IsItNull |
| --- | --- | --- | --- |
| 0 |  | - | T |
| 1 | NULL | - | T |
| 2 | - | - | T |
| 3 | 386 | 386 | F |

## Example - Excluding values using Null

Chart expression

Overview

Sales data is analyzed to determine total sales and those sales which are not related to Product A.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Sales

Load script

```
Example:
LOAD * Inline [
Product, Sales
A, 100
B, 150
C, 200
D, 250
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Product

Create the following measures:

- =Sum(Sales), to calculate the total sales.
- =If(Product = 'A', Null(),Sum(Sales)), to calculate the total sales where the Product is not A.

Results table

| Product | Sum(Sales) | If(Product = 'A', Null(),Sum(Sales)) |
| --- | --- | --- |
| A | 100 | - |
| B | 150 | 150 |
| C | 200 | 200 |
| D | 250 | 250 |

This example shows a simple way to calculate total sales and then exclude sales for a specific product using the Null function to set the value to NULL. For example, in the second measure, all values for Product A returned NULL and were excluded.
