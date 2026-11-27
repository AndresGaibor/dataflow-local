---
title: "Last  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/last.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Last  - chart function

Expand/Collapse all

# Last - chart function

Last() returns the value of
an expression evaluated with a pivot table's dimension values as they appear in the
last column of the current row segment in the pivot table. This function
returns NULL in all chart types except pivot tables.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Syntax:

Last([TOTAL] expr
[, offset [, count]])

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| offset | Specifying an offset n, greater than 1 moves the evaluation of the expression n columns to the left from the last column. Specifying an offset of 0 will evaluate the expression on the last column of the current row segment.  Specifying a negative offset number makes the Last function work like the First function with the corresponding positive offset number. |
| count | By specifying a third parameter count greater than 1, the function will return a range of values, one for each of the table columns up to the value of count, counting to the left from the original cell. |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

If the pivot table has multiple horizontal dimensions, the current row segment will include only columns with the same values as the current
column in all dimension rows except for the row showing the last horizontal
dimension of the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Example: Chart expressions

| Example | Result |
| --- | --- |
| Last( Sum(Sales )) | Returns the sum of Sales from the last column of the current row segment. |
| Last( Sum(Sales ), 2) | Returns the sum of Sales from the column that is two columns to the left of the last column in the current row segment. |
| Last( Total Sum( Sales )) | Returns the total sum of Sales from the last column of the current row segment. |
| RangeAvg (Last(Sum(x),1,5)) | Returns an average of the results of the sum(x) function evaluated on the five rightmost columns of the current row segment. |

## Example - Last fundamentals

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
- =Last(Sum(Sales)), to calculate the sum of sales of the last column for the current row segment.

Results table

| Year | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | Last(Sum(Sales)) | Sum(Sales) | Last(Sum(Sales)) | Sum(Sales) | Last(Sum(Sales)) | Sum(Sales) | Last(Sum(Sales)) |
| 2023 | 5000 | 7000 | 4000 | 7000 | 6000 | 7000 | 7000 | 7000 |
| 2024 | 4500 | 7250 | 3250 | 7250 | 6500 | 7250 | 7250 | 7250 |

Looking at the results, you can see that the Last function returns the sum of sales value for the last column of each row segment for each quarter. For example, in Q1 the Sum(Sales) value for that period is 5000. The Last(Sum(Sales) value for Q1 is 7000, which is the value for the Sum(Sales) in Q4, the last column value of the current row, 2023.

## Example - Last scenario

Chart expression

Overview

A dataset contains sales figures for various products over a three-month period. The company wants to present the total sales for the current period and the sales growth compared to the last (or most recent) sales figures in the period.

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
2024-01-01, Apple, 100
2024-01-01, Banana, 150
2024-01-01, Carrot, 120
2024-02-01, Carrot, 80
2024-02-01, Banana, 200
2024-02-01, Apple, 110
2024-03-01, Carrot, 160
2024-03-01, Banana, 300
2024-03-01, Apple, 150
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Product

Add this field as a column dimension:

- Date

Create the following measures:

- =Sum(Sales), to calculate the annual sales.
- =(Last(Sum(Sales)) - Sum(Sales)) / Sum(Sales), to calculate the growth in sales from the current period to the latest period. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| Product | 2024-01-01 | | 2024-02-01 | | 2024-03-01 | |
| --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | (Last(Sum(Sales)) - Sum(Sales)) / Sum(Sales) | Sum(Sales) | (Last(Sum(Sales)) - Sum(Sales)) / Sum(Sales) | Sum(Sales) | (Last(Sum(Sales)) - Sum(Sales)) / Sum(Sales) |
| Apple | 100 | 50.00% | 110 | 36.36% | 150 | 0.00% |
| Banana | 150 | 100.00% | 200 | 50.00% | 300 | 0.00% |
| Carrot | 120 | 33.33% | 80 | 100.00% | 160 | 0.00% |

In this example, you can see how sales have progressed from the start of the sales period to the latest period. For example, in the first period 2024-01-01, Apple sales were 100 compared to the latest sales figures of 150 for the period 2024-03-01. This indicates an increase of 50%.

## Example - Using Last to calculate budget variance

Chart expression

Overview

A dataset contains budget figures by quarter over a two-year period. The company wants to present the total budget amount for each quarter and the variance between the budget amount for the current period compared to the average quarterly budget for the year.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Year
  - Quarter
  - Budget

Load script

```
Example:
Load * inline [
Year, Quarter, Budget
2023, Q1, 1200
2023, Q2, 1100
2023, Q3, 1300
2023, Q4, 1400
2024, Q1, 1550
2024, Q2, 1230
2024, Q3, 1400
2024, Q4, 1600
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Year

Add this field as a column dimension:

- Quarter

Create the following measures:

- =Sum(Budget), to calculate the budget for the quarter.
- =Sum(Budget) - RangeAvg(Last(Budget, 1, 4))to calculate the variance between the Budget amount for the current period compared to the average quarterly budget for the year.

Results table

| Year | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Budget) | Sum(Budget) - RangeAvg(Last(Budget, 1, 4)) | Sum(Budget) | Sum(Budget) - RangeAvg(Last(Budget, 1, 4)) | Sum(Budget) | Sum(Budget) - RangeAvg(Last(Budget, 1, 4)) | Sum(Budget) | Sum(Budget) - RangeAvg(Last(Budget, 1, 4)) |
| 2023 | 1200 | -50 | 1100 | -150 | 1300 | 50 | 1400 | 150 |
| 2024 | 1550 | 105 | 1230 | -215 | 1400 | -45 | 1600 | 155 |

Using the Last function, you can see how the budget amount per quarter varies compared to the average quarterly budget. For example, in 2023, the total budget for the year is 5000 (1200 + 1100 + 1300 + 1400), therefore, the average quarterly budget is 1250. Since the budget amount for Q1 is 1200, it is 50 less compared to the average quarterly budget of 1250, whereas the budget variance for Q4 is 150 over the average quarterly budget.
