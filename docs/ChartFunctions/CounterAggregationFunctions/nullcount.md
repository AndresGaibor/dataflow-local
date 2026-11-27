---
title: "NullCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/CounterAggregationFunctions/nullcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# NullCount - chart function

Expand/Collapse all

# NullCount - chart function

NullCount()
 is used to aggregate the number of null values in each chart dimension.

Syntax:

NullCount({[SetExpression][DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

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
| NullCount(OrderNumber) | Returns the count of the null values in the OrderNumber field. |
| NullCount (OrderNumber)/NullCount ({1} Total OrderNumber) | The expression returns the number of orders with NULL as the OrderNumber from the selected customer as a fraction of all orders from customers with NULL as the OrderNumber. |

## Example - NullCount fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The NullInterpret value handling variable which is set to NULL. The variable will interpret all records with the text NULL as null values.
- The following fields in the data table:

  - Customer
  - Product
  - OrderNumber

Load script

```
Set NULLINTERPRET = NULL;
Example:
LOAD * inline [
Customer|Product|OrderNumber
Astrida|AA|1
Astrida|AA|7
Astrida|BB|4
Astrida|CC|6
Betacab|AA|5
Betacab|BB|2
Betacab|DD|NULL
Canutility|AA|3
Canutility|AA|NULL
Canutility|CC|NULL
] (delimiter is '|');
```

Tip noteTo set the NullInterpret variable back to default include the following variable statement at the end of the load script: Set NULLINTERPRET =;

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =NullCount(OrderNumber), to calculate the number of orders that have NULL as an OrderNumber.
- =NullCount (OrderNumber)/NullCount ({1} Total OrderNumber), to return the number of orders (from the selected customer) with NULL as an OrderNumber as a fraction of all orders from customers with NULL as the OrderNumber. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| Customer | NullCount(OrderNumber) | NullCount (OrderNumber)/NullCount ({1} Total OrderNumber) |
| --- | --- | --- |
| Totals | 3 | 100.00% |
| Astrida | 0 | 0.00% |
| Betacab | 1 | 33.33% |
| Canutility | 2 | 66.67% |

The first measure returns 3 because there are 3 total OrderNumber records with a NULL value (1 record with the customer Betacab and 2 records with Canutility).

The second measure returns the number of NULL orders as a fraction of NULL orders from all customers. For example, 66.67% of all order numbers with a NULL value are attributed to the customer Canutility.

## Example - Using NullCount to identify null values in KPI data

Chart expression

Overview

A dataset contains monthly key product indicater (KPI) data. A product manager wants to find out which KPIs have null values in the data.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The NullInterpret value handling variable which is set to NULL. The variable will interpret all records with the text NULL as null values.
- The following fields in the data table:

  - Month
  - KPI
  - Value

Load script

```
Set NULLINTERPRET = NULL;
Example:
LOAD * inline [
Month, KPI, Value
2024-01-01, Revenue, 5000
2024-02-01, Revenue, NULL
2024-03-01, Revenue, 5500
2024-04-01, Revenue, NULL
2024-01-01, Expenses, 3000
2024-02-01, Expenses, 3100
2024-03-01, Expenses, NULL
2024-04-01, Expenses, 3200
2024-01-01,Customer Count, 200
2024-02-01,Customer Count, 210
2024-03-01,Customer Count, NULL
2024-04-01,Customer Count, NULL
];
```

Tip noteTo set the NullInterpret variable back to default include the following variable statement at the end of the load script: Set NULLINTERPRET =;

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- KPI

Create the following measure:

- =NullCount(Value), to calculate the number of missing values.

Results table

| KPI | NullCount(Value) |
| --- | --- |
| Customer Count | 2 |
| Expenses | 1 |
| Revenue | 2 |

The results show that 5 records in the dataset have NULL values and the KPI categories to which these records relate.
