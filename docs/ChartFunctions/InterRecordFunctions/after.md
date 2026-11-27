---
title: "After  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/after.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# After  - chart function

Expand/Collapse all

# After - chart function

After() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
column after the current column within a row segment in the pivot table.

Syntax:

after([TOTAL] expr
[, offset [, count
]])

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Information note
This function returns NULL in all [chart](#glossary-0 "Glossary term") types except pivot tables.

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| offset | Specifying an offset n, greater than 1 moves the evaluation of the expression n columns further to the right from the current column.  Specifying an offset of 0 will evaluate the expression on the current column.  Specifying a negative offset number makes the After function work like the Before function with the corresponding positive offset number. |
| count | By specifying a third parameter count greater than 1, the function will return a range of values, one for each of the table columns up to the value of count, counting to the right from the original cell. |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

On the last column of a row segment a NULL value will be returned, as
there is no column after this one.

If the pivot table has multiple horizontal dimensions, the current row
segment will include only columns with the same values as the current
column in all dimension rows except for the row showing the last horizontal
dimension of the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Example: Chart expressions

| Example | Result |
| --- | --- |
| After( Sum(Sales )) | Returns the sum of Sales from the next column immediately to the right relative to the current column. |
| After( Sum(Sales ), 2) | Returns the sum of Sales from the column that is two columns to the right of the current column. |
| After( Total Sum( Sales )) | Returns the total sum of Sales from the next column immediately to the right relative to the current column. |
| RangeAvg (After(Sum(x),1,3)) | Returns an average of the three results of the sum(x) function evaluated in the three columns immediately to the right of the current column. |

## Example - After fundamentals

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
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Year

Add this field as a column dimension:

- Quarter

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =After(Sum(Sales)), to show the sum of sales in the following quarter.

Results table

| Year | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | After(Sum(Sales)) | Sum(Sales) | After(Sum(Sales)) | Sum(Sales) | After(Sum(Sales)) | Sum(Sales) | After(Sum(Sales)) |
| 2023 | 5000 | 4000 | 4000 | 6000 | 6000 | 7000 | 7000 | - |

Looking at the results, you can see how the After function returns the value of the next column that is immediately to the right of the Sum(Sales) column for each Quarter. For example, in Q1 the Sum(Sales) value for that period is 5000. The output of the After function for Q1 is 4000 because this is the value of the column immediately to the right of the Sum(Sales) for Q1, namely the Sum(Sales) for Q2.

## Example - After scenario

Chart expression

Overview

A dataset contains several years of sales figures of units sold at an electronics company. The company wants to present the total sales for each year and compare the unit sales from year-to-year.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Year
  - Sales

Load script

```
Example:
Load * inline [
Year, Sales
2021, 1350
2022, 1840
2023, 2250
2024, 1750
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- Year

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =Sum(Sales) - After(Sum(Sales)), to calculate the difference in sales year-to-year.

Results table

| Year | 2021 | | 2022 | | 2023 | | 2024 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | Sum(Sales)-After(Sum(Sales)) | Sum(Sales) | Sum(Sales)-After(Sum(Sales)) | Sum(Sales) | Sum(Sales)-After(Sum(Sales)) | Sum(Sales) | Sum(Sales)-After(Sum(Sales)) |
| 2023 | 1350 | -490 | 1840 | -410 | 2250 | 500 | 1750 | - |

The results show the sum of sales for each year and the difference between sales figures from one year to the next. For example, in 2022, the Sum(Sales) was 1840. The output of the After function indicates that this value was 410 units less that the sum of sales for 2023.

## Example - After advanced scenario

Chart expression

Overview

A dataset contains several years of sales figures. The company wants to present the total sales for the current year and a rolling total of the next 3 years of sales.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - SalesYear
  - Sales

Load script

```
Example:
Load * inline [
SalesYear, Sales
2021, 1300
2022, 1800
2023, 2000
2024, 2150
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- SalesYear

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =RangeSum(After(Sum(Sales),1,3)), to calculate the sum of sales for the next 3 years.

Results table

| 2021 | | 2022 | | 2023 | | 2024 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | RangeSum(After(Sum(Sales),1,3)) | Sum(Sales) | RangeSum(After(Sum(Sales),1,3)) | Sum(Sales) | RangeSum(After(Sum(Sales),1,3)) | Sum(Sales) | RangeSum(After(Sum(Sales),1,3)) |
| 1300 | 5950 | 1800 | 4150 | 2000 | 2150 | 2150 | 0 |

The results demonstrate how to use the After function to return sum of sales values for the next three years. For example, in 2021, the annual Sum(Sales) is 1300 and the sum of sales for the next 3 years (2022, 2023, 2024) is 5950. A value of 0 is returned for 2024 because the data for future years is not available.
