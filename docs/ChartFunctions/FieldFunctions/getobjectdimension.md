---
title: "GetObjectDimension  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getobjectdimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetObjectDimension  - chart function

Expand/Collapse all

# GetObjectDimension - chart function

GetObjectDimension() returns the name of the dimension. Index is an optional integer denoting the dimension that should be returned.

Information note

You cannot use this function in a chart in the following locations: title, subtitle, footer, reference line expression and min/max expression.

Information note

You cannot reference the name of a dimension or measure in another object using the Object ID.

Syntax:

GetObjectDimension ([index])

Return data type: String

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetObjectDimension () GetObjectDimension (0) | Returns the name of the first dimension in the chart. |
| GetObjectDimension (1) | Returns the name of the second dimension in the chart. |

## Example - GetObjectDimension fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - TransactionDate
  - CustomerID
  - TransactionQuantity

Load script

```
Example:
LOAD * INLINE [
TransactionDate, CustomerID, TransactionQuantity
2018/08/30, 049681, 13
2018/08/30, 203521, 6
2018/08/30, 203521, 21
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- TransactionDate
- CustomerID
- TransactionQuantity

Create the following measures:

- =GetObjectDimension (), to find the first dimension in the table.
- =GetObjectDimension (0), to find the first dimension in the table.
- =GetObjectDimension (1), to find the second dimension in the table.

Results table

| TransactionDate | CustomerID | TransactionQuantity | GetObjectDimension () | GetObjectDimension (0) | GetObjectDimension (1) |
| --- | --- | --- | --- | --- | --- |
| 2018/08/30 | 049681 | 13 | TransactionDate | TransactionDate | CustomerID |
| 2018/08/30 | 203521 | 6 | TransactionDate | TransactionDate | CustomerID |
| 2018/08/30 | 203521 | 21 | TransactionDate | TransactionDate | CustomerID |

Looking at the results, you can see how the GetObjectDimension function returns the name of the dimension indicated in the function parameters.

## Example - GetObjectDimension advanced scenario

Chart expression

Overview

This example uses the GetObjectDimension function in combination with filter selections. The dimension and measure calculation that appears in the chart object changes based on the filter that you select.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into two inline data tables: Sales and Filter. The first table, Sales, includes sales data. The second table, Filter, contains a list of field names that will be used as a dimension toggle. The toggle allows you to switch between dimensions in a chart and customize the measure calculation that appears depending on the dimension selected.
- The following fields in the Sales table:

  - Country
  - Salesperson
  - SalesValue
- The following field in the Filter table: FilterField.

Load script

```
Sales:
LOAD * INLINE [
Country, SalesPerson, SalesValue
USA, John, 500
USA, Alice, 700
Canada, Bob, 300
Canada, Carol, 400
Mexico, Dave, 200
];

Filter:
LOAD * INLINE [
FilterField
Country
SalesPerson
];
```

Results

1. Load the data and open a sheet. Create a new filter pane and add this field as a dimension:

   - FilterField
2. In the assets panel, under Fields, right-click FilterField and select Field settings. Select the Always one value selected check box, and then click Save.
3. Create a table, and then add a dimension by entering the following expression:

   - =$(= FilterField)
   - Under Label, enter the following expression to define the column name for the dimension: ='$(= FilterField)'
4. Create the following measure:

   - =If(GetObjectDimension() = 'Country', Sum(SalesValue), Avg(SalesValue)), to sum the sales values if the dimension selected is Country, otherwise to return the average of the sales value when the dimension selected is SalesPerson.
   - Under Label, enter the following expression to define the column name for the measure according to the filter selection: =If(GetObjectDimension() = 'Country', 'Sum(SalesValue)', 'Avg(SalesValue)')

In analysis mode, when you switch between SalesPerson and Country in the FieldFilter filter, the table changes to include the selected dimension and the corresponding measure calculation for that dimension. For example, if you select Country in the filter, the table shows Country as the dimension in the first column. The measure then uses the GetObjectDimension function, equates this to Country, and returns the Sum(SalesValue).

Filter pane and table results for Country

![A sheet with a filter pane to switch between country and salesperson and view the results for each dimension in a corresponding table. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-GetObjDim-example.png "Click to view full size")

The following table shows the results when you select Country in the FilterField filter.

Results table for Country

| Country | Sum(SalesValue) |
| --- | --- |
| Totals | 2100 |
| Canada | 700 |
| Mexico | 200 |
| USA | 1200 |

The following table shows the results when you select SalesPerson in the FilterField filter.

Results table for SalesPerson

| SalesPerson | Avg(SalesValue) |
| --- | --- |
| Totals | 420 |
| Alice | 700 |
| Bob | 300 |
| Carol | 400 |
| Dave | 200 |
| John | 500 |
