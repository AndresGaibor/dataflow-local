---
title: "FirstSortedValue - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/firstsortedvalue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# FirstSortedValue - chart function

Expand/Collapse all

# FirstSortedValue - chart function

FirstSortedValue() returns the value from the expression specified in value that corresponds to the result of sorting the sort\_weight argument, for example, the name of the product with the lowest unit price. The nth value in the sort order, can be specified in rank. If more than one resulting value shares the same sort\_weight for the specified rank, the function returns NULL.

Syntax:

FirstSortedValue([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] value, sort\_weight [,rank])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| value | Output field. The function finds the value of the expression value that corresponds to the result of sorting sort\_weight. |
| sort\_weight | Input field. The expression containing the data to be sorted. The first (lowest) value of sort\_weight is found, from which the corresponding value of the value expression is determined. If you place a minus sign in front of sort\_weight, the function returns the last (highest) sorted value instead. |
| rank | By stating a rank "n" larger than 1, you get the nth sorted value. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| FirstSortedValue (Product, UnitPrice) | Returns the Product with the lowest UnitPrice. |
| FirstSortedValue (Product, UnitPrice, 2) | Returns the Product with the second-lowest UnitPrice. |
| FirstSortedValue (Customer, -UnitPrice, 2) | Returns the Customer with the Product that has second-highest UnitPrice. |
| FirstSortedValue (Customer, -UnitPrice\*UnitSales, 2) | Returns the Customer with the second-highest sales order value, UnitPrice multiplied by UnitSales. |

## Example - FirstSortedValue fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - Product
  - UnitSales
  - UnitPrice

Load script

```
Example:
LOAD * inline [
Customer|Product|UnitSales|UnitPrice
Astrida|AA|4|16
Astrida|AA|10|15
Astrida|BB|9|9
Betacab|BB|5|10
Betacab|CC|2|20
Betacab|DD||25
Canutility|AA|8|15
Canutility|CC||19
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add these fields as measures:

- =FirstSortedValue (Product, UnitPrice), to calculate the product with the lowest unit price.
- =FirstSortedValue (Product, UnitPrice, 2), to calculate the product with the second-lowest unit price.
- =FirstSortedValue (Customer, -UnitPrice, 2) to calculate the customer with the product that has the second-highest unit price.
- =FirstSortedValue (Customer, UnitPrice, 3) to calculate the customer with the product that has the third-highest unit price.
- =FirstSortedValue (Customer, -UnitPrice\*UnitSales, 2) to calculate the customer with the second-highest sales order value, UnitPrice multiplied by UnitSales.

Results table

| FirstSortedValue (Product, UnitPrice) | FirstSortedValue (Product, UnitPrice, 2) | FirstSortedValue (Customer, -UnitPrice, 2) | FirstSortedValue (Customer, UnitPrice, 3) | FirstSortedValue (Customer, -UnitPrice\*UnitSales, 2) |
| --- | --- | --- | --- | --- |
| BB | BB | Betacab | - | Canutility |

The first column returns the value BB as this is the product which has the lowest UnitPrice (9)

The second column returns the value BB as this is the product with the second lowest UnitPrice (10).

The third column returns the value Betacab, which is the Customer with the Product that has the second-highest UnitPrice (20).

The fourth column returns NULL, because there are two values of Customer (Astrida and Canutility) with the same rank (third-lowest) UnitPrice (15).

The fifth column returns Canutility, which is the Customer with the second-highest sales order value, UnitPrice multiplied by UnitSales (120).

## Example - FirstSortedValue scenario

Chart expression

Overview

A dataset contains sales figures for the first three months of the year. The regional manager wants to identify the best and worst selling products to plan for future inventory.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Date
  - SalesProduct
  - Category
  - Sales

Load script

```
Example:
Load * inline [
Date,SalesProduct, Category, Sales
2024-01-01, Apple, Fruit, 100
2024-01-15, Banana, Fruit, 80
2024-01-30, Carrot, Vegetable, 50
2024-02-05, Apple, Fruit, 120
2024-02-20, Banana, Fruit, 90
2024-02-28, Carrot, Vegetable, 60
2024-03-10, Apple, Fruit, 110
2024-03-22, Banana, Fruit, 85
2024-03-31, Carrot, Vegetable, 55
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Category

Create the following measures:

- =FirstSortedValue(SalesProduct, -Sales), to calculate the top selling product in each category.
- =FirstSortedValue(TOTAL SalesProduct, -Sales), to calculate the top selling product overall.
- =FirstSortedValue(TOTAL SalesProduct, Sales) to calculate the lowest selling product overall.

Results table

| Category | FirstSortedValue(SalesProduct, -Sales) | FirstSortedValue(TOTAL SalesProduct, -Sales) | FirstSortedValue(TOTAL SalesProduct, Sales) |
| --- | --- | --- | --- |
| Fruit | Apple | Apple | Carrot |
| Vegetable | Carrot | Apple | Carrot |

The results indicate that Apple and Carrot are the best selling products in their respective categories, Fruit and Vegetable. However, across all categories, Apple was the best selling product and Carrot was the worst-selling product.

## Learn more

- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
