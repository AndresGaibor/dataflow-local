---
title: "First  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/first.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# First  - chart function

Expand/Collapse all

# First - chart function

First() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
first column of the current row segment in the pivot table. This function
returns NULL in all chart types except pivot tables.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Syntax:

First([TOTAL] expr
[, offset [, count]])

Arguments

| Argument | Description |
| --- | --- |
| expression | The expression or field containing the data to be measured. |
| offset | Specifying an offset n, greater than 1 moves the evaluation of the expression n columns further to the right from the first column. Specifying an offset of 0 will evaluate the expression on the first column of the current row segment.  Specifying an offset of 0 will evaluate the expression on the current row.  Specifying a negative offset number makes the First function work like the Last function with the corresponding positive offset number. |
| count | By specifying a third parameter count greater than 1, the function will return a range of values, one for each of the table columns up to the value of count, counting to the right from the original cell. |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

If the pivot table has multiple horizontal dimensions, the current row
segment will include only columns with the same values as the current
column in all dimension rows except for the row showing the last horizontal
dimension of the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Example: Chart expressions

| Example | Result |
| --- | --- |
| First( Sum(Sales )) | Returns the sum of Sales from the first column of the current row segment. |
| First( Sum(Sales ), 2) | Returns the sum of Sales that is two columns to the right of the first column in the current row segment. |
| First( Total Sum( Sales )) | Returns the total sum of Sales from the first column of the current row segment. |
| RangeAvg (First(Sum(x),1,5)) | Returns an average of the results of the sum(x) function evaluated on the five leftmost columns of the current row segment. |

## Example - First fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Year
  - Quarter
  - Sales

Load script

```
Example:
Load * inline [
Year, Quarter, Sales
2023, Q1, 5000
2023, Q2, 4000
2023, Q3, 6000
2023, Q4, 7000
2024, Q1, 4500
2024, Q2, 3250
2024, Q3, 6500
2024, Q4, 7250
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Year

Add this field as a column dimension:

- Quarter

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =First(Sum(Sales)), to calculate the sum of sales of the first column for the current row segment.

Results table

| Year | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | First(Sum(Sales)) | Sum(Sales) | First(Sum(Sales)) | Sum(Sales) | First(Sum(Sales)) | Sum(Sales) | First(Sum(Sales)) |
| 2023 | 5000 | 5000 | 4000 | 5000 | 6000 | 5000 | 7000 | 5000 |
| 2024 | 4500 | 4500 | 3250 | 4500 | 6500 | 4500 | 7250 | 4500 |

Looking at the results, you can see how the First function returns the sum of sales value for the first column of each row segment for each quarter. For example, in Q4 the Sum(Sales) value for that period is 7000. The First(Sum(Sales) value for Q4 is 5000, which is the value for the Sum(Sales) in Q1, the first column value of the current row, 2023.

## Example - First scenario

Chart expression

Overview

A dataset contains sales figures by year for various products over a three year period. The company wants to present the total sales for the current year and the sales growth since the first year in the period.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Date
  - Product
  - Sales

Load script

```
Example:
Load * inline [
Date, Product, Sales
2021, Apple, 100
2021, Banana, 150
2021, Carrot, 120
2022, Carrot, 80
2022, Banana, 200
2022, Apple, 110
2023, Carrot, 160
2023, Banana, 300
2023, Apple, 150
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Product

Add this field as a column dimension:

- Date

Create the following measures:

- =Sum(Sales), to calculate the annual sales.
- =(Sum(Sales) - First(Sales)) / First(Sales), to calculate the growth in sales since the first year in the dataset. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| Product | 2021 | | 2022 | | 2023 | |
| --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | (Sum(Sales) - First(Sales)) / First(Sales) | Sum(Sales) | (Sum(Sales) - First(Sales)) / First(Sales) | Sum(Sales) | (Sum(Sales) - First(Sales)) / First(Sales) |
| Apple | 100 | 0.00% | 110 | 10.00% | 150 | 50.00% |
| Banana | 150 | 0.00% | 200 | 33.33% | 300 | 100.00% |
| Carrot | 120 | 0.00% | 80 | -33.33% | 160 | 33.33% |

The results show the annual sales figures for each year and the growth rate per year as a percentage compared to the sales values from the first year. For example, Apple sales increased from an initial value of 100 in 2021 to a value of 150 in 2023, which is an increase of 50%. The sale of Carrot decreased from 120 in 2021 to 80 in 2022, a reduction of 33.33%.

## Example - First scenario using a range sum to present budget figures

Chart expression

Overview

A dataset contains budget figures by quarter for a two-year period by product category. The company wants to present the budget for the current quarter and the running total of the budget for each year.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - BudgetYear
  - BudgetQuarter
  - QuarterNo
  - BudgetAmount
  - Category

Load script

```
Example:
Load * inline [
BudgetYear, BudgetQuarter, QuarterNo, BudgetAmount, Category
2023, Q1, 1, 2100, Online
2023, Q2, 2, 2500, Online
2023, Q3, 3, 3100, Online
2023, Q4, 4, 4100, Online
2023, Q1, 1, 5100, Store
2023, Q2, 2, 5500, Store
2023, Q3, 3, 6100, Store
2023, Q4, 4, 7100, Store
2024, Q1, 1, 2300, Online
2024, Q2, 2, 2800, Online
2024, Q3, 3, 3300, Online
2024, Q4, 4, 4400, Online
2024, Q1, 1, 5300, Store
2024, Q2, 2, 5800, Store
2024, Q3, 3, 6300, Store
2024, Q4, 4, 7400, Store
];
```

Results

Load the data and open a sheet. Create a new pivot table and add these fields as row dimensions:

- BudgetYear
- Category

Add this field as a column dimension:

- BudgetQuarter

Create the following measures:

- =Sum(BudgetAmount), to calculate the budget sales figure.
- =RangeSum(First(Sum(BudgetAmount), 1, QuarterNo)), to calculate the running total of the budget sales for every quarter by summing the range from the first quarter to QuarterNo as evaluated for each quarter.

Results table

| BudgetYear  Category | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(BudgetAmount) | RangeSum(First(Sum(BudgetAmount), 1, QuarterNo)) | Sum(BudgetAmount) | RangeSum(First(Sum(BudgetAmount), 1, QuarterNo)) | Sum(BudgetAmount) | RangeSum(First(Sum(BudgetAmount), 1, QuarterNo)) | Sum(BudgetAmount) | RangeSum(First(Sum(BudgetAmount), 1, QuarterNo)) |
| (-) 2023 | 7200 | 7200 | 8000 | 15200 | 9200 | 24400 | 11200 | 35600 |
| Online | 2100 | 2100 | 2500 | 4600 | 3100 | 7700 | 4100 | 11800 |
| Store | 5100 | 5100 | 5500 | 10600 | 6100 | 16700 | 7100 | 23800 |
| (-) 2024 | 7600 | 7600 | 8600 | 16200 | 9600 | 25800 | 11800 | 37600 |
| Online | 2300 | 2300 | 2800 | 5100 | 3300 | 8400 | 4400 | 12800 |
| Store | 5300 | 5300 | 5800 | 11100 | 6300 | 17400 | 7400 | 24800 |

The results show the budget figures for each Year and Category, and the running total by Quarter. For example, in Q2 of 2023, QuarterNo is 2. Therefore, the function expression is evaluated as RangeSum(First(Sum(BudgetAmount), 1, 2)), which sums the BudgetAmount columns for Q1 (7200) and Q2 (8000) and returns the value 15200. The result returns the total of the Sum(BudgetAmount) columns for Q1 and Q2. In 2024, for the Category Online, the Sum(BudgetAmount) for Q1 is 2300 and for Q2, is 2800. Therefore, the RangeSum expression returns 5100.
