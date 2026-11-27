---
title: "Sum - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/sum.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Sum - chart function

Expand/Collapse all

# Sum - chart function

Sum()
 calculates the total of the values given by the expression or field across the aggregated data.

Syntax:

Sum([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] expr])

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. Information noteAlthough the DISTINCT qualifier is supported, use it only with extreme caution because it may mislead the reader into thinking a total value is shown when some data has been omitted. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Sum(UnitSales) | Returns the total of the values in UnitSales. |
| Sum(UnitSales\*UnitPrice) | Returns the total of UnitPrice multiplied by UnitSales aggregated. |
| Sum(TOTAL UnitSales\*UnitPrice) | Returns the total sum for all rows in the table, as well as the total, because the TOTAL qualifier means the sum is calculated disregarding the chart dimensions. |
| Sum({1} TOTAL UnitSales\*UnitPrice) | The set analysis expression {1} defines the set of records to be evaluated as ALL, independent of any selection made. |

## Example - Sum fundamentals

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

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Customer
- Product

Create the following measures:

- =Sum(UnitSales), to calculate the sum of UnitSales.
- =Sum(UnitSales\*UnitPrice), to calculate the aggregated total of UnitSales multiplied by UnitPrice.
- =Sum(TOTAL UnitSales\*UnitPrice), to calculate the total for all rows in the table as well as the total, because the TOTAL qualifier means the sum is the same for all cells, disregarding the chart dimensions.
- =Sum({1} TOTAL UnitSales\*UnitPrice), to calculate the total, independent of the selection made, because the set analysis expression {1} defines the set of records to be evaluated as ALL, no matter what selection is made.

Results table

| Customer | Product | Sum(UnitSales) | Sum(UnitSales\*UnitPrice) | Sum(TOTAL UnitSales\*UnitPrice) | Sum({1} TOTAL UnitSales\*UnitPrice) |
| --- | --- | --- | --- | --- | --- |
| Totals | - | 38 | 505 | 505 | 505 |
| Astrida | AA | 14 | 214 | 505 | 505 |
| Astrida | BB | 9 | 81 | 505 | 505 |
| Betacab | BB | 5 | 50 | 505 | 505 |
| Betacab | CC | 2 | 40 | 505 | 505 |
| Betacab | DD | 0 | 0 | 505 | 505 |
| Canutility | AA | 8 | 120 | 505 | 505 |
| Canutility | CC | 0 | 0 | 505 | 505 |

In this example, observe the following:

- For the first measure, Sum(UnitSales, the Totals cell returns 38, which is the total of the values in UnitSales across all customers and products. The results for each customer and product combination are aggregated to return the total sum of UnitSales for each combination. For example, the sum of all UnitSales of product AA from customer Astrida is 14.
- For the second measure, Sum(UnitSales\*UnitPrice), the Totals cell returns 505. This is the aggregated total of UnitSales multiplied by UnitPrice for each customer and product combination.
- For the third measure, Sum(TOTAL UnitSales\*UnitPrice), the value returned in all rows including Totals is 505, because the TOTAL qualifier disregards the chart dimensions. However, if a selection is made on a dimension such as Customer, then the values will change. For example, if you select Betacab, the resulting table will have only three rows, one for each of the Betacab records, but the column will return the same total value for all rows (90).
- The fourth measure, Sum({1} TOTAL UnitSales\*UnitPrice), returns the value 505 independent of any selections because the set analysis expression {1} defines the set of records to be evaluated as ALL. If you select a customer, for example, Canutility, the value returned is still 505.

## Example - Sum scenario aggregating sales data

Chart expression

Overview

A dataset contains sales figures for stores by region. The company wants to aggregate the sales.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Month
  - SalesProduct
  - Region
  - Sales

Load script

```
Example:
Load * inline [
Month,SalesProduct, Region, Sales
2024-01-01, T-shirt, East, 100
2024-01-01, T-shirt, West, 120
2024-01-01, Jeans, East, 200
2024-01-01, Jeans, West, 180
2024-02-01, T-shirt, East, 150
2024-02-01, T-shirt, West, 130
2024-02-01, Jeans, East, 250
2024-02-01, Jeans, West, 220
];
```

Results

Load the data and open a sheet. Create a new pivot table and add these fields as row dimensions:

- Month
- Region

Add this field as a column dimension:

- SalesProduct

Create the following measure:

- =Sum(Sales), to calculate the total sales for each product.

To expand the pivot table to see all rows, in the properties panel, under Appearance, select Presentation. Under Rows, select Fully expanded.

Results table

| Month  Region | SalesProduct | |
| --- | --- | --- |
| Jeans | T-shirt |
| 2024-01-01 | 380 | 220 |
| East | 200 | 100 |
| West | 180 | 120 |
| 2024-02-01 | 470 | 280 |
| East | 250 | 150 |
| West | 220 | 130 |

The results show the sales for each SalesProduct by Month and Region, with an aggregated total for each Month.

## Learn more

- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
