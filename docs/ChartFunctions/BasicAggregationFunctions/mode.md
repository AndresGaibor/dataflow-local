---
title: "Mode - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/mode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Mode - chart function

Expand/Collapse all

# Mode - chart function

Mode()
 finds the most commonly occurring value, the mode value, in the aggregated data. The Mode() function
can process text values as well as numeric values.

Syntax:

Mode({[SetExpression] [TOTAL [<fld {,fld}>]]} expr)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Mode(UnitSales) | Returns the most commonly occurring value in UnitSales. Returns NULL (-). No single value occurs more often than another. |
| Mode(Customer) | Returns the most commonly occurring value in Customer. Returns NULL (-). No single value occurs more often than another. |
| Mode(TOTAL UnitSales) | The TOTAL qualifier returns the most commonly occurring value in Unitsales disregarding the chart dimensions. |
| Mode({1} TOTAL UnitSales) | The set analysis expression {1} defines the set of records to be evaluated as ALL, independent of any selection made. For example, if a specific customer is selected, it will still return the most commonly occurring value of UnitSales across the full dataset. |

## Example - Mode fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - UnitSales
  - UnitPrice

Load script

```
Example:
LOAD * inline [
Customer|UnitSales|UnitPrice
Astrida|4|16
Astrida|10|15
Astrida|9|9
Astrida|10|10
Betacab|5|10
Betacab|4|20
Betacab||25
Canutility|8|15
Canutility|4|19
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Mode(UnitSales), to calculate the most commonly occurring UnitSales value.
- =Mode(Customer), to calculate the most commonly occurring Customer value.
- =Mode(TOTAL UnitSales), to calculate the most commonly occurring UnitSales value across the entire dataset disregarding the chart dimensions. If a selection is made then the value will adjust to reflect that selection.
- =Mode({1} TOTAL UnitSales), to calculate the most commonly occurring UnitSales value, ignoring selections. If a selection is made then the value stays constant.

Results table

| Customer | Mode(UnitSales) | Mode(Customer) | Mode(TOTAL UnitSales) | Mode({1} TOTAL UnitSales) |
| --- | --- | --- | --- | --- |
| Totals | 4 | Astrida | 4 | 4 |
| Astrida | 10 | Astrida | 4 | 4 |
| Betacab | - | Betacab | 4 | 4 |
| Canutility | - | Canutility | 4 | 4 |

In this example, observe the following :

- In the first measure (Mode(UnitSales)), the most commonly occurring value for the customer Astrida is 10. The Totals cell returns 4, which is the most commonly occurring value for UnitSales across the whole dataset. There are no instances of most commonly occurring values for Betacab and Canutility so the results return NULL for those customers.
- In the second measure (Mode(Customer)), the results return each customer name. However, the Totals cell returns Astrida because this is the most commonly occurring customer value across the whole dataset.
- The third measure (Mode(TOTAL UnitSales)) returns the value of 4. If no Customer is selected, then all cells in this column will display the value of 4. If you select a customer, such as Betacab, this column will return NULL as there is no commonly occurring value for Betacab.
- The fourth measure (Mode({1} TOTAL UnitSales)) returns 4 regardless of any selections in the Customer field because the set analysis expression {1} defines the set of records to be evaluated as ALL. For example, if you select Betacab this column will continue to return the value 4.

## Example - Mode scenario to determine anomalies in sales data

Chart expression

Overview

A dataset contains sales figures by month. The company wants to see the most commonly occurring value of sales for each product and across the entire dataset. It also wants to compare the sales by product to the entire dataset to identify any atypical anomalies in the data.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Date
  - Product
  - Category
  - Sales

Load script

```
Example:
Load * inline [
Date, Product, Category, Sales
2024-01-01, Apple, Fruit, 100
2024-01-15, Banana, Fruit, 80
2024-01-30, Carrot, Vegetable, 50
2024-02-05, Apple, Fruit, 100
2024-02-20, Banana, Fruit, 90
2024-02-28, Carrot, Vegetable, 60
2024-03-10, Apple, Fruit, 110
2024-03-22, Banana, Fruit, 80
2024-03-31, Carrot, Vegetable, 50
2024-04-10, Apple, Fruit, 125
2024-04-22, Banana, Fruit, 60
2024-04-31, Carrot, Vegetable, 80
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Category
- Product

Create the following measures:

- =Mode(Sales), to calculate the most commonly occurring value for each product.
- =Mode(TOTAL Sales), to calculate the most commonly-occurring value for the entire dataset.
- If(Mode(Sales) = Mode(TOTAL Sales), 'Typical', 'Atypical'), to calculate whether the most commonly-occurring value for each product is typical when compared to results across the entire dataset.

Results table

| Category | Product | Mode(Sales) | Mode(TOTAL Sales) | If(Mode(Sales) = Mode(TOTAL Sales), 'Typical', 'Atypical') |
| --- | --- | --- | --- | --- |
| Fruit | Apple | 100 | 80 | Atypical |
| Fruit | Banana | 80 | 80 | Typical |
| Vegetable | Carrot | 50 | 80 | Atypical |

The output of the Mode function returns the most commonly occurring value of sales by product, Mode(Sales), and across all products, Mode(TOTAL Sales). These two values are then compared to determine which sales results are typical or atypical.

## Learn more

- [*Avg - chart function*](../StatisticalAggregationFunctionsinCharts/avg.htm)
- [*Median - chart function*](../StatisticalAggregationFunctionsinCharts/median.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
