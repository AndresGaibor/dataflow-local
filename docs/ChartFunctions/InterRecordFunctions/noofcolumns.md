---
title: "NoOfColumns  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/noofcolumns.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# NoOfColumns  - chart function

Expand/Collapse all

# NoOfColumns - chart function

NoOfColumns() returns the number of columns in the current row segment in a pivot
table.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Syntax:

NoOfColumns([total])

Arguments

| Argument | Description |
| --- | --- |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

In a pivot table with multiple horizontal dimensions, the current row
segment includes only columns with the same values as the current
column across all dimension rows—except for the row showing the last dimension
in the inter-field sort order. The inter-field sort order for horizontal dimensions in pivot tables
is defined simply by the order of the dimensions from top to bottom.

Example: Chart expression

| Example | Result |
| --- | --- |
| IF(ColumnNo() > NoOfColumns() - 2, Sum(Sales), Null()) | Where the ColumnNo is greater than the NoOfColumns minus 2, the chart will return the value Sum(Sales). Otherwise, if ColumnNo is less than that it will return NULL. In this example, from the third column onwards, it will return values while columns 1 and 2 will not return any value. |

## Example - NoOfColumns fundamentals

Chart expression

Overview

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
- =NoOfColumns(), to calculate the number of columns.

Results table

| Q1 | | Q2 | | Q3 | | Q4 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sum(Sales) | NoOfColumns() | Sum(Sales) | NoOfColumns() | Sum(Sales) | NoOfColumns() | Sum(Sales) | NoOfColumns() |
| 1000 | 4 | 2000 | 4 | 3000 | 4 | 4000 | 4 |

The results show the sum of sales for periods Q1 to Q4. The NoOfColumns function returns a value of 4 because there are 4 columns showing for the current row segment.

## Example - NoOfColumns scenario

Chart expression

Overview

A dataset contains quarterly sales figures. You want to show sales values for only the last two quarters (Q3 and Q4) in the pivot table.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Quarter
  - Sales

Load script

```
Example:
Load * inline [
Product, Quarter, Sales
Apple, Q1, 100
Apple, Q2, 120
Apple, Q3, 140
Apple, Q4, 160
Banana, Q1, 150
Banana, Q2, 180
Banana, Q3, 200
Banana, Q4, 220
Cherry, Q1, 80
Cherry, Q2, 90
Cherry, Q3, 110
Cherry, Q4, 150
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Product

Add this field as a column dimension:

- Quarter

Create the following measure:

- =IF(ColumnNo() > NoOfColumns() - 2, Sum(Sales), Null()), to display the values for only the last two columns in the pivot table (Q3 and Q4).

Results table

| Product | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- |
| Apple | - | - | 140 | 160 |
| Banana | - | - | 200 | 220 |
| Cherry | - | - | 110 | 150 |

The results show sales values for only columns 3 and 4, the last two quarters of the year.
