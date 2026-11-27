---
title: "Count - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/CounterAggregationFunctions/count.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# Count - chart function

Expand/Collapse all

# Count - chart function

Count()
 is used to aggregate the number of values, text and numeric, in each chart dimension.

Syntax:

Count({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Count(OrderNumber) | Returns the number of rows that could have a value for OrderNumber. All records, even empty ones, are counted. Information note"0" counts as a value and not an empty cell. However, if a measure aggregates to 0 for a dimension, that dimension will not be included in charts. |
| Count(Customer) | Evaluates the number of occurrences in all rows. |
| Count(DISTINCT [Customer]) | The DISTINCT qualifier restricts the Count to only evaluate unique occurrences. |
| Count(OrderNumber)/Count({1} TOTAL OrderNumber) | The expression returns the number of orders from the selected customer as a percentage of orders from all customers. |
| Count(TOTAL <Product> OrderNumber) | Returns the number of orders placed on products for the selected customers only. Empty cells are also counted. |

## Example - Count fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - Product
  - OrderNumber
  - UnitSales
  - UnitPrice

Load script

```
Example:
LOAD * inline [
Customer|Product|OrderNumber|UnitSales|UnitPrice
Astrida|AA|1|4|16
Astrida|AA|7|10|15
Astrida|BB|4|9|9
Betacab|CC|6|5|10
Betacab|AA|5|2|20
Betacab|BB|1|25| 25
Canutility|AA|3|8|15
Canutility|CC|||19
Divadip|CC|2|4|16
Divadip|DD|3|1|25
](delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Count(OrderNumber) , to count the number of orders.
- =Count(Customer), to calculate the number of customer records.
- =Count(DISTINCT Customer), to count the number of distinct customers.
- =Count(OrderNumber)/Count({1} TOTAL OrderNumber), to count the ratio of the selected customer orders as a ratio of the total customer orders.
- =Count(TOTAL <Product> OrderNumber), to count the number of orders placed for products for the selected customers only (empty cells are counted).

Results table

| Customer | Count(OrderNumber) | Count(Customer) | Count(DISTINCT Customer) | Count(OrderNumber)/Count({1} TOTAL OrderNumber) | Count(TOTAL <Product> OrderNumber) |
| --- | --- | --- | --- | --- | --- |
| Totals | 10 | 10 | 4 | 1 | 10 |
| Astrida | 3 | 3 | 1 | 0.3 | 10 |
| Betacab | 3 | 3 | 1 | 0.3 | 10 |
| Canutility | 2 | 2 | 1 | 0.2 | 10 |
| Divadip | 2 | 2 | 1 | 0.2 | 10 |

Looking at the results, we can observe the following:

- First measure: There are 10 order records in the dataset.
- Second measure: There are 10 customer records in the dataset.
- Third measure: There are 4 distinct (unique) customers in the dataset.
- Fourth measure: Returns 1 because no selection has been applied. If you select the customer Canutility, the value changes to 0.2 because there are 2 order records for this customer out of 10 total records in the dataset.
- Fifth measure: Returns 10 because no selection has been applied. If you select the customers Astrida and Canutility, the value changes to 5 because that is the number of orders placed on products for these customers (empty cells are also counted).

## Example - Using Count to find the number of sales per product

Chart expression

Overview

A dataset contains data for store sales. You want to find the number of sales per product.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Sales
  - Region
  - Status

Load script

```
Example:
Load * inline [
Product,Sales,Region,Status
Apple, 100, North, Completed
Banana, 80, South, Pending
Carrot, 50, East, Completed
Apple, 120, North, Completed
Banana, 90, South, Completed
Carrot, 60, West, Pending
Apple, 110, North, Completed
Banana, 85, South, Completed
Carrot, 55, East, Pending
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Product

Create the following measures:

- =Count(Sales), to calculate the number of sales per product.
- =Count({<Status={'Completed'}>} Sales), to calculate the number of sales with completed orders.
- =Count({<Status={'Pending'}>} Sales), to calculate the number of sales with orders still pending.
- =Count({<Region={'North'}>} Sales), to calculate the number of orders in the North region.

Results table

| Product | Count(Sales) | Count({<Status={'Completed'}>} Sales) | Count({<Status={'Pending'}>} Sales) | Count({<Region={'North'}>} Sales) |
| --- | --- | --- | --- | --- |
| Totals | 9 | 6 | 3 | 3 |
| Apple | 3 | 3 | 0 | 3 |
| Banana | 3 | 2 | 1 | 0 |
| Carrot | 3 | 1 | 2 | 0 |

The output of the Count function returns a breakdown of the total number of sales orders by product, as well as the number of orders that are completed and the number that are still pending. The last measure returns a count of sales records for the North region.
