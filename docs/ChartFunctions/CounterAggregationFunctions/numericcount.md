---
title: "NumericCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/CounterAggregationFunctions/numericcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# NumericCount - chart function

Expand/Collapse all

# NumericCount - chart function

NumericCount()
 aggregates the number of numeric values in each chart dimension.

Syntax:

NumericCount({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| NumericCount(OrderNumber) | Returns the number of rows in the OrderNumber field that have numeric values. Information note"0" counts as a value and not an empty cell. However, if a measure aggregates to 0 for a dimension, that dimension will not be included in charts. Empty cells are evaluated as non-numeric values and are not counted by NumericCount. |
| NumericCount(Product) | Returns the number of product names that are numeric values. Typically you might use this to check that no text fields have been given numeric content. |
| NumericCount (DISTINCT OrderNumber)/Count(DISTINCT OrderNumber) | Counts the number of distinct numeric order numbers and divides it by the number of order numbers, numeric and non-numeric. This will be 1 if all field values are numeric. |

## Example - NumericCount fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - Product
  - OrderNumber

Load script

```
Example:
LOAD * inline [
Customer|Product|OrderNumber
Astrida|AA|1
Astrida|AA|7
Astrida|BB|4
Betacab|CC|6
Betacab|AA|5
Betacab|BB|
Canutility|AA|
Canutility|CC|
Divadip|CC|2
Divadip|DD|3
](delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- OrderNumber

Create the following measures:

- =NumericCount(OrderNumber), to calculate the number of orders containing numeric values.
- =NumericCount(Product), to return the number of product names which are wholly numeric values.
- =NumericCount(DISTINCT OrderNumber)/Count(DISTINCT OrderNumber), to calculate the total number of order numbers with distinct numeric values and divide this amount by the total number of order numbers with distinct numeric and non-numeric values. This will be 1 if all field values are numeric.

Results table

| OrderNumber | NumericCount(OrderNumber) | NumericCount(Product) | NumericCount (DISTINCT OrderNumber)/Count(DISTINCT OrderNumber) |
| --- | --- | --- | --- |
| Totals | 7 | 0 | 0.875 |
| 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 |
| 4 | 1 | 0 | 1 |
| 5 | 1 | 0 | 1 |
| 6 | 1 | 0 | 1 |
| 7 | 1 | 0 | 1 |
|  | 0 | 0 | 0 |

The output of the first measure returns 7 because three of the ten records in OrderNumber are empty and the remaining are numeric.

The second measure returns 0 because there are no numeric values; all product names are text. Typically you might use this type of measure to verify that no text fields have numeric content.

The third measure counts the number of distinct numeric order numbers and divides it by the number of order numbers both numeric and non-numeric. This will be 1 if all field values are numeric. Typically you might use this to check that all field values are numeric. In this example, there are 7 distinct numeric values for OrderNumber of 8 distinct numeric and non-numeric values, so the expression returns 0.875.

## Example - NumericCount scenario

Chart expression

Overview

A dataset contains monthly sales data across several stores. The store manager wants to find out which stores and products have sales values which are not numeric. This indicates which sales records have invalid values, for example, the record was empty or contains non-numeric data.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Store
  - StoreProduct
  - Sales

Load script

```
Example:
LOAD * inline [
Store, StoreProduct, Sales
A, Widget A, 1200
B, Widget A, No data
C, Widget A, 1300
A, Widget B, 800
B, Widget B,
C, Widget B, "Error"
A, Widget C, 500
B, Widget C, 600
C, Widget C, 700
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Store

Add this field as a column dimension:

- StoreProduct

Create the following measure:

- =NumericCount(Sales), to calculate the store sales that have numeric data.

Results table

| Store | StoreProduct | | |
| --- | --- | --- | --- |
| Widget A | Widget B | Widget C |
| A | 1 | 1 | 1 |
| B | 0 | 0 | 1 |
| C | 1 | 0 | 1 |

The results show that there are 3 records where the numeric count is 0. Those are the sales records which need to be investigated as they contain non-numeric values.
