---
title: "SecondaryDimensionality - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/secondarydimensionality.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# SecondaryDimensionality - chart function

Expand/Collapse all

# SecondaryDimensionality - chart function

SecondaryDimensionality() returns the number of dimension
pivot table rows that have non-aggregation content, that is, do not contain
partial sums or collapsed aggregates. This function is the equivalent
of the dimensionality() function for horizontal pivot table dimensions.

Syntax:

SecondaryDimensionality( )

Return data type: integer

Limitations:

- Unless used in pivot tables, the SecondaryDimensionality function always returns 0.
- Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

## Example - SecondaryDimensionality fundamentals

Chart expression

Overview

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
2024-01-01, Banana, Fruit, 80
2024-02-01, Apple, Fruit, 120
2024-02-01, Banana, Fruit, 90
2024-03-01, Apple, Fruit, 110
2024-03-01, Banana, Fruit, 85
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Date

Add these fields as column dimensions:

- Category
- Product

Create the following measures:

- =Sum(Sales), to calculate the total sales.
- =SecondaryDimensionality(), to return the dimension number to demonstrate the use of this function.

Pivot table showing results for the dimension: Category

|  | (+) Fruit | |
| --- | --- | --- |
| Date | Sum(Sales) | SecondaryDimensionality() |
| 2024-01-01 | 180 | 1 |
| 2024-02-01 | 120 | 1 |
| 2024-03-01 | 110 | 1 |

The pivot table results show only the Category dimension displayed as a column. Therefore, the SecondaryDimensionality function returns a value of 1.

If you expand the Category dimension, Fruit, the table results will now include the Product dimension values, Apple and Banana.

Pivot table showing results for two dimensions: Category, Product

| Date | (-) Fruit | | | |
| --- | --- | --- | --- | --- |
| Apple | | Banana | |
| Sum(Sales) | SecondaryDimensionality() | Sum(Sales) | SecondaryDimensionality() |
| 2024-01-01 | 100 | 2 | 80 | 2 |
| 2024-02-01 | 120 | 2 | 90 | 2 |
| 2024-03-01 | 110 | 2 | 85 | 2 |

The SecondaryDimensionality function now returns a value of 2, as there are values showing for two dimensions in the pivot table: Category and Product.

## Example - Using SecondaryDimensionality to apply conditional formatting in a chart expression

Chart expression

Overview

This example uses the function in a chart expression in a pivot table to apply conditional cell formatting depending on which dimension level is displayed.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Year
  - Quarter
  - Product Category
  - Sales

Load script

```
Example:
Load * inline [
Year, Quarter, Product Category, Sales
2023, Q1, Electronics, 5000
2023, Q1, Furniture, 3000
2023, Q2, Electronics, 4000
2023, Q2, Furniture, 3500
2023, Q3, Electronics, 6000
2023, Q3, Furniture, 4500
2023, Q4, Electronics, 7000
2023, Q4, Furniture, 5000
];
```

Results

Load the data and open a sheet. Create a new pivot table and add this field as a row dimension:

- Product Category

Add these fields as column dimensions:

- Year
- Quarter

Create the following measure:

- =Sum(Sales), to calculate the total sales.

In the Properties panel of the Sum(Sales) measure, enter the following expression as the Background color expression:

```
IF(SecondaryDimensionality() = 1,
RGB(144, 238, 144),  // Green for Year-level
RGB(173, 216, 230),  // Blue for Quarter-level
)
```

The expression will apply a green background to the table cells when the SecondaryDimensionality function returns 1 and a blue background when the function returns any other result.

Pivot table showing results for one dimension: Year with green cell background

| Product Category | (+) 2023 |
| --- | --- |
| Electronics | 22000 |
| Furniture | 16000 |

The results show that when only the Year dimension is displayed, therefore the SecondaryDimensionality value is 1, the Sum(Sales) cells appear with a green background. When you expand the table to show the Sum(Sales) by Quarter, the background now appears blue because there are two dimensions showing, Year and Quarter, and the SecondaryDimensionality value is now 2.

Pivot table showing results for two dimensions: Year and Quarter with blue cell background

| Product Category | (-) 2023 | | | |
| --- | --- | --- | --- | --- |
| Q1 | Q2 | Q3 | Q4 |
| Electronics | 5000 | 4000 | 6000 | 7000 |
| Furniture | 3000 | 3500 | 4500 | 5000 |
