---
title: "ColumnNo  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/columnno.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# ColumnNo  - chart function

Expand/Collapse all

# ColumnNo - chart function

ColumnNo() returns the number of the current column within the current row segment
in a pivot table. The first column is number 1.

Syntax:

ColumnNo([total])

Arguments

| Argument | Description |
| --- | --- |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

If the pivot table has multiple horizontal [dimensions](#glossary-0 "Glossary term"), the current row
segment will include only columns with the same values as the current column in all dimension rows except for the row showing the last horizontal
dimension of the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Example: Chart expression

| Example | Result |
| --- | --- |
| IF( ColumnNo()=1, 0, Sum(Sales) / Before(Sum(Sales))) | Where the ColumnNo is equal to 1, the chart will return zero. Otherwise, it will return the result of Sum(Sales) / Before(Sum(Sales). In this example, the chart will return values from column 2 onwards, while column 1 will return zero. |

## Example - ColumnNo fundamentals

Chart expression

Overview

A dataset contains quarterly sales data. This example multiplies the sales value for each period by the column number of the period.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Period
  - Sales

Load script

```
Example:
Load * inline [
Period, Sales
Q1, 1000
Q2, 2000
Q3, 3000
Q4, 4000
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- Period

Create the following measure:

- =Sum(Sales) \* ColumnNo(), to calculate the sum of the sales values multiplied by the column number, which is the quarter in this example.

Results table

| Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- |
| 1000 | 4000 | 9000 | 16000 |

The sum of sales value for each quarter is multiplied by the output of the ColumnNo function. For example, the value of sales in Q4 is 4000, and the output of the ColumnNo function returns 4 because Q4 is the fourth column. Therefore, the measure expression multiplies 4000 by 4 and returns 16000.

## Example - ColumnNo scenario

Chart expression

Overview

A dataset contains quarterly sales figures. A company wants to increase the sales data for Q1 and Q3 (the odd-numbered columns) by 5% and increase the sales for the remaining columns (Q2 and Q4) by 10%.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Period
  - Sales

Load script

```
Example:
Load * inline [
Period, Sales
Q1, 1000
Q2, 2000
Q3, 3000
Q4, 4000
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- Period

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =If(Odd(ColumnNo()), Amount \* 1.05, Amount \* 1.10), to increase the sales amounts for the odd-numbered columns by 5% and the remaining columns by 10%.

Results table

| Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | If(Odd(ColumnNo()), Amount \* 1.05, Amount \* 1.10) | Sum(Sales) | If(Odd(ColumnNo()), Amount \* 1.05, Amount \* 1.10) | Sum(Sales) | If(Odd(ColumnNo()), Amount \* 1.05, Amount \* 1.10) | Sum(Sales) | If(Odd(ColumnNo()), Amount \* 1.05, Amount \* 1.10) |
| 1000 | 1050 | 2000 | 2200 | 3000 | 3150 | 4000 | 4400 |

The results show that the sales values for the odd-numbered columns, 1 and 3 (Q1 and Q3), have increased by 5%, while the remaining even-numbered columns, 2 and 4 (Q2 and Q4), have increased by 10%.

## Example - ColumnNo advanced scenario

Chart expression

Overview

This example uses the same dataset as the previous scenario to present the cumulative total for the values in each period.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Period
  - Sales

Load script

```
Example:
Load * inline [
Period, Sales
Q1, 1000
Q2, 2000
Q3, 3000
Q4, 4000
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- Period

Create the following measure:

- =RangeSum(Before(Sum(Sales), 0, ColumnNo())), to calculate the cumulative total.

Results table

| Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- |
| 1000 | 3000 | 6000 | 10000 |

This example shows how to use the ColumnNo function to generate a running total. The following explanation provides more details about the measure expression: RangeSum(Before(Sum(Sales), 0, ColumnNo())).

Sum(Sales): calculates the sum of sales for the current cell in the pivot table.

Before(Sum(Sales), 0, ColumnNo()): The Before function retrieves values from the preceding columns in the pivot table.

- The Sum(Sales) argument ensures that the function retrieves the summed Sales for the preceding cells.
- The offset value of 0 specifies the offset for the column (remaining in the current row segment of the current column).
- ColumnNo() determines how many columns to go back when retrieving the data. It dynamically represents the position of the current column (for example, for column 3, ColumnNo() equals 3, so the function looks back across three columns).

RangeSum(): The RangeSum function calculates the sum of the range of values provided. It handles null values by treating them as zero. In this expression, RangeSum effectively generates a cumulative total by summing all the preceding Sales values retrieved by the Before() function, as well as the sales of the current cell.
