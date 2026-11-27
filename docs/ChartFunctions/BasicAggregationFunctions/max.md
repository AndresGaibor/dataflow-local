---
title: "Max - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/max.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Max - chart function

Expand/Collapse all

# Max - chart function

Max() finds the highest value of the aggregated data. By specifying a rank n, the nth highest value can be found.

Tip noteYou might also want to look at FirstSortedValue and RangeMax, which have similar functionality to the Max function.

Syntax:

Max([{SetExpression}] [TOTAL [<fld {,fld}>]] expr [,rank])

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| rank | The default value of rank is 1, which corresponds to the highest value. By specifying rank as 2, the second highest value is returned. If rank is 3, the third highest value is returned, and so on. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Max(UnitSales) | Returns the highest value in the UnitSales field. |
| Max(UnitSales\*UnitPrice) The value of an order is calculated by multiplying the number of units sold in (UnitSales) by the unit price. | Returns the highest value of the result of calculating all possible values of (UnitSales) \* (UnitPrice). |
| Max(UnitSales, 2) | Returns the value for the second highest value. |
| Max(TOTAL UnitSales) | The TOTAL qualifier means the highest possible value is found, disregarding the chart dimensions. For a chart with Customer as dimension, the TOTAL qualifier will ensure the maximum value across the full dataset is returned, instead of the maximum UnitSales for each customer. |
| Max({1} TOTAL UnitSales) | The set analysis expression {1} defines the set of records to be evaluated as ALL, independent of any selection made. For example, if a specific customer is selected, it will still return the maximum UnitSales across the full dataset. |

## Example - Max fundamentals

Chart expression

Overview

A dataset contains product sales figures by month. We want to identify the maximum sales value for each product and the month when this occurred.

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

- =Max(UnitSales), to calculate the maximum UnitSales value.
- =Max(UnitSales\*UnitPrice), to calculate the maximum value after multiplying UnitSales by UnitPrice on a row-by-row basis.
- =Max(UnitSales, 2), to calculate the second highest value.
- =Max(TOTAL UnitSales), to calculate the highest total regardless of the chart dimension.
- =Max({1} TOTAL UnitSales), to calculate the highest total ignoring all selections.

Results table

| Customer | Max(UnitSales) | Max(UnitSales\*UnitPrice) | Max(UnitSales, 2) | Max(TOTAL UnitSales) | Max({1} TOTAL UnitSales) |
| --- | --- | --- | --- | --- | --- |
| Totals | 10 | 150 | 9 | 10 | 10 |
| Astrida | 10 | 150 | 9 | 10 | 10 |
| Betacab | 5 | 50 | 2 | 10 | 10 |
| Canutility | 8 | 120 | - | 10 | 10 |

In this example, observe the following:

- In the first measure (Max(UnitSales)), the highest value for UnitSales for the customer Astrida is 10. The Totals cell in this column returns 10 because this value is also the highest UnitSales value in the entire dataset.
- In the second measure (Max(UnitSales\*UnitPrice)), 150 is returned for Astrida.This is the highest value for that customer when multiplying UnitSales by UnitPrice. The Totals cell for this column also returns 150, as this is also the highest calculated value in the entire dataset.
- In the third measure (Max(UnitSales, 2)), the second highest UnitSales value for the customer Astrida is 9. This value is also the second highest value of all three customers, therefore the Totals row also returns 9.
- The fourth measure (Max(TOTAL UnitSales)) returns the value 10. This is the highest value found independent of the customer dimension, therefore, all rows return the same value. However, if you select the customer Betacab, the table will return only values for that customer, in this case 5 because this is the highest UnitSales across all products for Betacab.
- The fifth measure (Max({1} TOTAL UnitSales)) returns the value 10 regardless of which Customer is selected because set modified {1} is used. For example, if you select Betacab this column will continue to return the value 10.

## Example - Max scenario calculating highest sales by month

Chart expression

Overview

A dataset contains product sales figures by month. An sales manager wants to identify the maximum sales value for each product and the month when this occurred.

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

Create the following measures:

- =If(Sales = Max(TOTAL <Product> Sales), Sales), to calculate the maximum sales for each product. In the property panel of the measure, select Add-ons > Data Handling. Clear the Include zero values checkbox to remove any null values.

Results table

| Product | Month | If(Sales = Max(TOTAL <Product> Sales), Sales) |
| --- | --- | --- |
| A | 2024-02-01 | 700 |
| B | 2024-02-01 | 800 |
| C | 2024-03-01 | 710 |

The results of the measure return the maximum sales value for each product and the month in which this value was reached. For example, Product B had the highest sales (800) in 2024-02-01.

## Learn more

- [*FirstSortedValue - chart function*](firstsortedvalue.htm)
- [*RangeMax Script and chart function*](../RangeFunctions/rangemax.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
