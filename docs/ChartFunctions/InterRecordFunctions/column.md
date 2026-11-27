---
title: "Column - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/column.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Column - chart function

Expand/Collapse all

# Column - chart function

Column() returns the value found in the column corresponding to ColumnNo in a straight table, disregarding dimensions. For example Column(2) returns the value of the second measure column.

Syntax:

Column(ColumnNo)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| ColumnNo | Column number of a column in the table containing a [measure](#glossary-0 "Glossary term"). Information noteThe Column() function disregards [dimension](#glossary-1 "Glossary term") columns. |

Limitations:

- Recursive calls will return NULL.
- If ColumnNo references a column for which there is no measure, a NULL value is returned.
- Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Example: Chart expressions

| Example | Result |
| --- | --- |
| Column(1)/Column(2) | Returns the value of the first measure divided by the value of second measure in the chart. |

## Example - Column fundamentals

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
- UnitSales
- UnitPrice

Create the following measures:

- =Sum(UnitPrice\*UnitSales), to find the annual sales.
- =Sum(TOTAL UnitPrice\*UnitSales), to find the total sales value.
- =100\*Column(1)/Column(2), to calculate the percentage (%) sales of the total sales.

Results table

| Customer | Product | UnitPrice | UnitSales | Sum(UnitPrice\*UnitSales) | Sum(TOTAL UnitPrice\*UnitSales) | 100\*Column(1)/Column(2) |
| --- | --- | --- | --- | --- | --- | --- |
| Totals |  |  |  | 505 | 505 | 100.00 |
| Astrida | AA | ​15 | 10 | 150 | 505 | 29.70 |
| Astrida | AA | ​16 | 4 | 64 | 505 | 12.67 |
| Astrida | BB | ​9 | 9 | 81 | 505 | 16.04 |
| Betacab | BB | ​10 | 5 | 50 | 505 | 9.90 |
| Betacab | CC | ​20 | 2 | 40 | 505 | 7.92 |
| Betacab | DD | ​25 |  | 0 | 505 | 0.00 |
| Canutility | AA | ​15 | 8 | 120 | 505 | 23.76 |
| Canutility | CC | ​19 |  | 0 | 505 | 0.00 |

The results show that you can analyze data by referring to a column position and reusing that logic in a measure expression. For example, the measure 100\*Column(1)/Column(2) takes the value from the first measure, Sum(UnitPrice\*UnitSales), divides it by the value from the second measure, Sum(TOTAL UnitPrice\*UnitSales), and then multiplies the result by 100.

## Example - Column scenario

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Month
  - Sales
  - Expenses
  - Profit

Load script

```
Example:
LOAD * INLINE [
Month, Sales, Expenses, Profit
Jan, 10000, 4000, 6000
Feb, 12000, 4500, 7500
Mar, 15000, 5000, 10000
Apr, 11000, 4200, 6800
May, 13000, 4800, 8200
Jun, 14000, 4700, 9300
Jul, 16000, 5100, 10900
Aug, 12500, 4300, 8200
Sep, 15500, 4900, 10600
Oct, 13500, 4600, 8900
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Product

Create the following measures:

- =Sum(Sales), to aggregate the sales.
- =Sum(Expenses) to aggregate the sales.
- =Column(1) - Column(2), to calculate the difference between the sales and the expense column.

Results table

| Month | Sum(Sales) | Sum(Expenses) | Column(1) - Column(2) |
| --- | --- | --- | --- |
| Totals | 132500 | 46100 | 86400 |
| Jan | 10000 | 4000 | 6000 |
| Feb | 12000 | 4500 | 7500 |
| Mar | 15000 | 5000 | 10000 |
| Apr | 11000 | 4200 | 6800 |
| May | 13000 | 4800 | 8200 |
| Jun | 14000 | 4700 | 9300 |
| Jul | 16000 | 5100 | 10900 |
| Aug | 12500 | 4300 | 8200 |
| Sep | 15500 | 4900 | 8200 |
| Oct | 13500 | 4600 | 8900 |

The table results show how to use the Column function to perform data analysis. The measure Column(1) - Column(2) returns the leftover sales amount after subtracting expenses (the second measure column).

## Example - Column scenario analyzing sales data

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ProductName
  - Q1\_Sales
  - Q2\_Sales
  - Q3\_Sales
  - Q4\_Sales

Load script

```
Example:
LOAD * INLINE [
ProductName, Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales
Product A, 1200, 1500, 1100, 1300
Product B, 1400, 1600, 1200, 1450
Product C, 1350, 1700, 1150, 1550
Product D, 1250, 1550, 1300, 1500
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- ProductName

Create the following measures:

- =Sum(Q1\_Sales), to aggregate the first quarter sales.
- =Sum(Q2\_Sales), to aggregate the second quarter sales.
- =Sum(Q3\_Sales), to aggregate the third quarter sales.
- =Sum(Q4\_Sales), to aggregate the fourth quarter sales.
- =Column(1) - Column(2), to calculate the ratio of Q1\_Sales to Q2\_Sales.
- =(Column(2) - Column(1)) / Column(1) to calculate the growth rates between two periods.

Results table

| ProductName | Sum(Q1\_Sales) | Sum(Q2\_Sales) | Sum(Q3\_Sales) | Sum(Q4\_Sales) | Column(1) - Column(2) | (Column(2) - Column(1)) / Column(1) |
| --- | --- | --- | --- | --- | --- | --- |
| Totals | 5200 | 6350 | 4750 | 5800 | ​0.81889763779528 | 0.22115384615385 |
| Product A | 1200 | 1500 | 1100 | 1300 | 0.8 | 0.25 |
| Product B | 1400 | 1600 | 1200 | 1450 | 0.875 | ​0.14285714285714 |
| Product C | 1350 | 1700 | 1150 | 1550 | 0.79411764705882 | 0.25925925925926 |
| Product D | 1250 | 1550 | 1300 | 1500 | ​0.80645161290323 | 0.24 |

The table results show that you can use the Column function to analyze data.
