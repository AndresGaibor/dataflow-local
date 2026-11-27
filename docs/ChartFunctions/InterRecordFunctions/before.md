---
title: "Before  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/before.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Before  - chart function

Expand/Collapse all

# Before - chart function

Before() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
column before the current column within a row segment in the pivot table.

Syntax:

Before([TOTAL] expr
[, offset [, count]])

Information noteThis function returns NULL in all [chart](#glossary-0 "Glossary term") types except pivot tables.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| offset | Specifying an offset n, greater than 1 moves the evaluation of the expression n columns further to the left from the current column.  Specifying an offset of 0 will evaluate the expression on the current column.  Specifying a negative offset number makes the Before function work like the After function with the corresponding positive offset number. |
| count | By specifying a third parameter count greater than 1, the function will return a range of values, one for each of the table columns up to the value of count, counting to the left from the original cell. |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

On the first column of a row segment a NULL value will be returned,
as there is no column before this one.

If the pivot table has multiple horizontal dimensions, the current row
segment will include only columns with the same values as the current column in all dimension rows except for the row showing the last horizontal
dimension of the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Example: Chart expressions

| Example | Result |
| --- | --- |
| Before( Sum(Sales )) | Returns the sum of Sales from the previous column immediately to the left relative to the current column. |
| Before( Sum(Sales ), 2) | Returns the sum of Sales from the column that is two columns to the left of the current column. |
| Before( Total Sum( Sales )) | Returns the total sum of Sales from the previous column immediately to the left relative to the current column. |
| RangeAvg ( Before(Sum(x),1,3)) | Returns an average of the three results of the sum(x) function evaluated in the three columns immediately to the left of the current column. |

## Example - Before fundamentals

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
- =Before(Sum(Sales)), to show the sum of sales in the previous quarter.

Results table

| Year | Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | Before(Sum(Sales)) | Sum(Sales) | Before(Sum(Sales)) | Sum(Sales) | Before(Sum(Sales)) | Sum(Sales) | Before(Sum(Sales)) |
| 2023 | 5000 | - | 4000 | 5000 | 6000 | 4000 | 7000 | 6000 |

Looking at the results, you can see how the Before function returns the value of the previous column that is immediately to the left of the Sum(Sales) column for each Quarter. For example, in Q4 the Sum(Sales) value for that period is 7000.The output of the Before function for Q4 is 6000, which is the value of the column immediately to the left of the Sum(Sales) for Q4, namely the Sum(Sales) for Q3.

## Example - Using the Before function to calculate sales growth year-over-year

Chart expression

Overview

A dataset contains sales figures for several years. The company wants to present the total sales for each year and the growth in sales based on the value from the previous year.

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
2021, 1300
2022, 1800
2023, 2000
2024, 2100
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a column dimension:

- Year

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =(Sum(Sales) - Before(Sum(Sales))) / Before(Sum(Sales)), to calculate the annual sales growth. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| 2021 | | 2022 | | 2023 | | 2024 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | (Sum(Sales) - Before(Sum(Sales)))/Before(Sum(Sales)) | Sum(Sales) | (Sum(Sales) - Before(Sum(Sales)))/Before(Sum(Sales)) | Sum(Sales) | (Sum(Sales) - Before(Sum(Sales)))/Before(Sum(Sales)) | Sum(Sales) | (Sum(Sales) - Before(Sum(Sales)))/Before(Sum(Sales)) |
| 1300 | - | 1800 | 38.46% | 2000 | 11.11% | 2100 | 5.00% |

The output of the Before function returns the year-over-year growth based on the previous year's sales figures. For example, the sum of sales for 2022 was 38.46% higher than the Sum(Sales) for 2021.

Tip noteYou can also use the After function to perform the same sales growth calculation in this scenario. When you specify a negative offset number in the function parameters, it makes the After function work like the Before function with the corresponding positive offset number. For example, the following expression using the After function (with a negative offset value of -1) returns the same annual sales growth results as the Before function: 
=(Sum(Sales)-After(Sum(Sales),-1))/(After(Sum(Sales),-1)).
