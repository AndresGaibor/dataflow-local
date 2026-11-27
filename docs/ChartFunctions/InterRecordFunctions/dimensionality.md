---
title: "Dimensionality - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/dimensionality.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Dimensionality - chart function

Expand/Collapse all

# Dimensionality - chart function

Dimensionality() returns the number of dimensions for the current row. In the case of pivot tables, the function returns the total number of dimension columns that have non-aggregation content, that is, do not contain partial
sums or collapsed aggregates.

Syntax:

Dimensionality ( )

Return data type:  integer

Limitations:

This function is only available in [charts](#glossary-0 "Glossary term"). For all chart types, except pivot table, it will return the number
of [dimensions](#glossary-1 "Glossary term") in all rows except the total, which will be 0.

Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

## Example: Chart expression using Dimensionality

Chart expression

Overview

Use the Dimensionality function in a pivot table as a chart expression where you want to apply different cell formatting depending on the number of dimensions in a row that has non-aggregated data. This example applies a background color to table cells that match a given condition.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Country
  - Product
  - Sales
  - Budget

Load script

```
Example:
Load * inline [
Country, Product, Sales, Budget
Sweden, AA, 100000, 50000
Germany, AA, 125000, 175000
Canada, AA, 105000, 98000
Norway, AA, 74850, 68500
Ireland, AA, 49000, 48000
Sweden, BB, 98000, 99000
Germany, BB, 115000, 175000
Norway,BB,71850,68500
Ireland,BB,31000,48000
] (delimiter is ',');
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

Results

Load the data and open a sheet. Create a new pivot table and add these fields as row dimensions:

- Country
- Product

Create the following measures:

- =Sum(Sales), to calculate the sum of the Sales values.
- =Sum(Budget), to calculate the sum of the Budget values.
- =Dimensionality(), to return the number of dimensions for the current row.

In the Properties panel of the Sum(Sales) measure, enter the following expression as the Background color expression:

```
=If(Dimensionality()=1 and Sum(Sales)<Sum(Budget),RGB(255,156,156),
  If(Dimensionality()=2 and Sum(Sales)<Sum(Budget),RGB(178,29,29)
  )
 )
```

The output of the background color expression applies a light red or dark red cell background to the table cells when the applicable conditions are met.

Pivot table showing results for the row dimensions: Country, Product

| Country |  | | |
| --- | --- | --- | --- |
| Product |
|  | Sum(Sales) | Sum(Budget) | Dimensionality() |
| (+) Canada | 105000 | 98000 | 1 |
| (-) Germany | 240000 | 350000 | 1 |
| AA | 125000 | 175000 | 2 |
| BB | 115000 | 175000 | 2 |
| (+) Ireland | 80000 | 96000 | 1 |
| (+) Norway | 146700 | 137000 | 1 |
| (+) Sweden | 198000 | 149000 | 1 |

When the first row dimension (Country) is displayed, the Dimensionality function returns 1. When you expand a row dimension, such as Germany, to display the second row dimension (Product), the function returns 2.

The background color expressions for the measure Sum(Sales) perform calculations based on dimensionality and sales to highlight different results. When the dimensionality is 1, any Country with Sum(Sales) less than Sum(Budget) appears light red, in this example, Germany and Ireland. When the dimensionality is 2, any Product with Sum(Sales) less than Sum(Budget) appears dark red, in this example, AA and BB for Germany.

## Example - Dimensionality scenario

Chart expression

Overview

This example uses the Dimensionality function to apply details to a report and highlight table cells for some dimensions.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Region
  - SalesProduct
  - Year
  - SalesValue
  - Quantity
  - Product

Load script

```
Example:
LOAD * INLINE [
Region, SalesProduct, Year, SalesValue, Quantity, Profit
North, Laptop, 2023, 20000, 15, 4000
North, Mobile, 2023, 15000, 25, 3000
North, Laptop, 2022, 18000, 20, 3500
North, Mobile, 2022, 14000, 22, 2800
South, Laptop, 2023, 22000, 18, 4500
South, Mobile, 2023, 16000, 27, 3200
South, Laptop, 2022, 19000, 19, 3800
South, Mobile, 2022, 15000, 23, 3100
East, Laptop, 2023, 21000, 16, 4200
East, Mobile, 2023, 15500, 24, 3100
East, Laptop, 2022, 18500, 18, 3900
East, Mobile, 2022, 14500, 21, 2950
West, Laptop, 2023, 23000, 17, 4700
West, Mobile, 2023, 16500, 26, 3300
West, Laptop, 2022, 19500, 20, 4000
West, Mobile, 2022, 15500, 24, 3100
North, Tablet, 2023, 12000, 10, 2500
South, Tablet, 2023, 13000, 12, 2700
East, Tablet, 2023, 12500, 11, 2600
West, Tablet, 2023, 13500, 13, 2800
];
```

Results

Load the data and open a sheet. Create a new pivot table and add these fields as row dimensions:

- Year
- SalesProduct
- Region

Create the following measures:

- =If(Dimensionality()=1, 'Total', 'Detail'), to indicate whether it is a Total or Detail row.
- =If(Dimensionality()=3, 'Region-Level', If(Dimensionality()=2, 'Product-Level', 'Summary-Level')), to indicate the dimension level that is being displayed.
- =Sum(SalesValue), to calculate the sum of sales.

In the Properties panel of the Sum(SalesValue) measure, enter the following expression as the Background color expression:

```
=If(Dimensionality()=1, LightGray())
```

The output of the background color expression applies a light gray cell background to the table cells when the dimensionality is 1.

Pivot table showing results for the row dimensions: Country, Product

| Year |  | | |
| --- | --- | --- | --- |
| SalesProduct |
| Region |  |  |  |
|  | If(Dimensionality()=1, 'Total', 'Detail') | If(Dimensionality()=3, 'Region-Level', If(Dimensionality()=2, 'Product-Level', 'Summary-Level')) | Sum(SalesValue) |
| (+) 2022 | Total | Summary-Level | 134000 |
| (-) 2023 | Total | Summary-Level | 200000 |
| (-)Laptop | Detail | Product-Level | 86000 |
| East | Detail | Region-Level | 21000 |
| North | Detail | Region-Level | 20000 |
| South | Detail | Region-Level | 22000 |
| West | Detail | Region-Level | 23000 |
| (-) Mobile | Detail | Product-Level | 63000 |
| (-) Tablet | Detail | Product-Level | 51000 |

You can see how the Dimensionality function can be used to enhance the detail of the report and highlight all top-level row dimensions.
