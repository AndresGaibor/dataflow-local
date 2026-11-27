---
title: "Min - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/min.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Min - chart function

Expand/Collapse all

# Min - chart function

Min()
 finds the lowest value of the aggregated data. By specifying a rank n, the nth lowest value can be found.

Tip noteYou might also want to look at FirstSortedValue and RangeMin, which have similar functionality to the Min function.

Syntax:

Min({[SetExpression] [TOTAL [<fld {,fld}>]]} expr [,rank])

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| rank | The default value of rank is 1, which corresponds to the lowest value. By specifying rank as 2, the second lowest value is returned. If rank is 3, the third lowest value is returned, and so on. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Min(UnitSales) | Returns the lowest non-null value in the UnitSales field. |
| Min(UnitSales\*UnitPrice) The value of an order is calculated by multiplying the number of units sold ( in UnitSales) by the unit price. | Returns the lowest non-null value of the result of calculating all possible values of (UnitSales) \* (UnitPrice). |
| Min(UnitSales, 2) | Returns the value for the second lowest value in UnitSales (after the NULL values). |
| Min(TOTAL UnitSales) | The TOTAL qualifier means the lowest possible value is found, disregarding the chart dimensions. For a chart with Customer as dimension, the TOTAL qualifier will ensure the minimum value across the full dataset is returned, instead of the minimum UnitSales for each customer. |
| Min({1} TOTAL UnitSales) | The set analysis expression {1} defines the set of records to be evaluated as ALL, independent of any selection made. For example, if a specific customer is selected, it will still return the minimum UnitSales across the full dataset. |

## Example - Min fundamentals

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
Betacab|5|10
Betacab|2|20
Betacab||25
Canutility|8|15
Canutility||19
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Min(UnitSales), to calculate the minimum UnitSales value.
- =Min(UnitSales\*UnitPrice), to calculate the minimum value after multiplying UnitSales by UnitPrice on a row-by-row basis.
- =Min(UnitSales, 2), to calculate the second lowest value.
- =Min(TOTAL UnitSales), to calculate the lowest total regardless of the chart dimension.
- =Min({1} TOTAL UnitSales), to calculate the lowest total ignoring all selections.

Results table

| Customer | Min(UnitSales) | Min(UnitSales\*UnitPrice) | Min(UnitSales, 2) | Min(TOTAL UnitSales) | Min({1} TOTAL UnitSales) |
| --- | --- | --- | --- | --- | --- |
| Totals | 2 | 40 | 4 | 2 | 2 |
| Astrida | 4 | 64 | 9 | 2 | 2 |
| Betacab | 2 | 40 | 5 | 2 | 2 |
| Canutility | 8 | 120 | - | 2 | 2 |

In this example, observe the following:

- In the first measure Min(UnitSales), the lowest value for UnitSales for the customer Astrida is 4. The Totals cell in this column returns 2 because this value is the lowest UnitSales value in the entire dataset.
- In the second measure Min(UnitSales\*UnitPrice), 64 is returned for Astrida.This is the lowest value for that customer when multiplying UnitSales by UnitPrice. The Totals cell for this column returns 40, as this is also the lowest calculated value in the entire dataset.
- In the third measure Min(UnitSales, 2), the second lowest UnitSales value for customer Astrida is 9. The value 4 is returned in the Totals row, because this is the second lowest UnitSales value across all customers.
- The fourth measure Min(TOTAL UnitSales), returns the value 2. This is the lowest possible non-null value independent of the customer dimension, therefore, all rows return the same value. However, if you select the customer Betacab, the table will return only values for that customer, in this case 2 because this is the lowest UnitSales across all products for Betacab.
- The fifth measure Min({1} TOTAL UnitSales), returns 2 irrespective of the value selected in the Customer field as the measure calculates the lowest total. For example, if you select Betacab this column will continue to return the value 2.

## Example - Min scenario calculating lowest sales by month

Chart expression

Overview

A dataset contains product sales figures by month. An sales manager wants to identify the minimum sales value for each product and the month when this occurred.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Sales
  - Month

Load script

```
Example:
Load * inline [
Product,Sales,Month
A, 500, 2024-01-01
A, 700, 2024-02-01
A, 600, 2024-03-01
B, 300, 2024-01-01
B, 800, 2024-02-01
B, 450, 2024-03-01
C, 550, 2024-01-01
C, 620, 2024-02-01
C, 710, 2024-03-01
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Product
- Month

Create the following measure:

- =If(Sales = Min(TOTAL <Product> Sales), Sales), to calculate the minimum sales for each product. In the properties panel, select Add-ons > Data Handling. Clear the Include zero values checkbox.

Results table

| Product | Month | If(Sales = Min(TOTAL <Product> Sales), Sales) |
| --- | --- | --- |
| A | 2024-01-01 | 500 |
| B | 2024-01-01 | 300 |
| C | 2024-01-01 | 550 |

The results of the measure return the minimum sales value for each product and the month in which this value was reached. For example, Product B had the lowest sales (300) in 2024-01-01.

## Learn more

- [*FirstSortedValue - chart function*](firstsortedvalue.htm)
- [*RangeMin Script and chart function*](../RangeFunctions/rangemin.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
