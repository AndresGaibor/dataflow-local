---
title: "MissingCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/CounterAggregationFunctions/missingcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# MissingCount - chart function

Expand/Collapse all

# MissingCount - chart function

MissingCount()
 is used to aggregate the number of missing values in each chart dimension. Missing values are all non-numeric values.

Syntax:

MissingCount({[SetExpression] [DISTINCT]
[TOTAL [<fld {,fld}>]]} expr)

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
| MissingCount(OrderNumber) | Returns the number of missing values where OrderNumber fields are empty. Information note"0" counts as a value and not an empty cell. However, if a measure aggregates to 0 for a dimension, that dimension will not be included in charts. |
| MissingCount(OrderNumber)/MissingCount({1} TOTAL OrderNumber) | The expression returns the number of incomplete orders from the selected customer as a fraction of incomplete orders from all customers. |

## Example - MissingCount fundamentals

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
Customer, Product, OrderNumber, UnitSales, UnitPrice
Astrida,AA, 1,4,16
Astrida, AA,7,10,15
Astrida, BB,4,9,9
Betacab, BB,6,5,10
Betacab, CC,5,2,20
Betacab ,DD,,,25
Canutility, AA,,,15
Canutility, CC,,,19
Divadip, AA,2,4,16
Divadip, BB,,4,16
Divadip, DD,3,,25
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =MissingCount(OrderNumber), to calculate the number of orders missing an OrderNumber.
- =MissingCount(OrderNumber)/MissingCount ({1} Total [OrderNumber]), to return the number of incomplete orders from the selected customer as a fraction of incomplete orders from all customers. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| Customer | MissingCount(OrderNumber) | MissingCount(OrderNumber)/MissingCount ({1} Total [OrderNumber]) |
| --- | --- | --- |
| Totals | 4 | 100.00% |
| Astrida | 0 | 0.00% |
| Betacab | 1 | 25.00% |
| Canutility | 2 | 50.00% |
| Divadip | 1 | 25.00% |

In the first measure, the MissingCount function returns 4 because 4 of the 11 records in the OrderNumber field are empty.

Information note"0" counts as a value and not an empty cell. However, if a measure aggregates to 0 for a dimension, that dimension will not be included in charts.

In the second measure, the output of the MissingCount function returns the number of incomplete orders from the selected customer as a percentage of incomplete orders from all customers. For example, if you select Canutility from the Customer dimension, the measure returns 50% because half of all incomplete orders (2 of 4) are with this customer.

## Example - Using MissingCount to identify missing product data

Chart expression

Overview

A dataset contains monthly key product indicater (KPI) data. A product manager wants to find out which KPIs have missing data.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Month
  - KPI
  - Value

Load script

```
Example:
Load * inline [
Month, KPI, Value
2024-01-01, Revenue, 5000
2024-02-01, Revenue,
2024-03-01, Revenue, 5500
2024-04-01, Revenue,
2024-01-01, Expenses, 3000
2024-02-01, Expenses, 3100
2024-03-01, Expenses,
2024-04-01, Expenses, 3200
2024-01-01,Customer Count, 200
2024-02-01,Customer Count, 210
2024-03-01,Customer Count,
2024-04-01,Customer Count,
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- KPI

Create the following measure:

- =MissingCount(Value), to calculate the number of missing values.

Results table

| KPI | MissingCount(Value) |
| --- | --- |
| Totals | 5 |
| Customer Count | 2 |
| Expenses | 1 |
| Revenue | 2 |

The results show that 5 records in the dataset have missing data as well as the KPI categories to which these records relate.
