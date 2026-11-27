---
title: "Only - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/BasicAggregationFunctions/only.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Only - chart function

Expand/Collapse all

# Only - chart function

Only()
 returns a value if there is one and only one possible result from the aggregated data. For example, searching for the only product where the unit price =9 will return NULL if more than one product has a unit price of 9.

Syntax:

Only([{SetExpression}] [TOTAL [<fld {,fld}>]] expr)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Tip noteUse Only() when you want a NULL result if there are multiple possible values in the sample data.

Example: Chart expression

| Example | Result |
| --- | --- |
| Only(Category) | Displays the Category as long as it is unique within the context. |

## Example - Only fundamentals

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

Load the data and open a sheet. Create a new table with the following measures:

- =Only({<UnitPrice={9}>} Product), to calculate the only Product that has a UnitPrice of 9.
- =Only({<Product={DD}>} Customer), to calculate the only Customer selling a Product called DD.
- =Only({<UnitPrice={20}>} UnitSales) to calculate the number of UnitSales where UnitPrice is 20.
- =Only({<UnitPrice={15}>} UnitSales), to calculate the values of UnitSales where the UnitPrice = 15.

Results table

| Only({<UnitPrice={9}>} Product) | Only({<Product={DD}>} Customer) | Only({<UnitPrice={20}>} UnitSales) | Only({<UnitPrice={15}>} UnitSales) |
| --- | --- | --- | --- |
| BB | Betacab | 2 | - |

In this example, observe the following:

- The first column returns the value BB because this is the only Product that has a UnitPrice of 9.
- The second column returns Betacab because it is the only Customer selling a Product called DD.
- The third column returns 2 because this is the only value of UnitSales where UnitPrice = 20.
- The fourth column returns NULL because there is no single result where UnitPrice = 15. In this dataset, there are two values of UnitSales where the UnitPrice =15.

## Example - Only scenario

Chart expression

Overview

A dataset contains product sales by period. The company wants to determine whether a product is sold in a single store or multiple stores.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Date
  - RecordID
  - StoreProduct
  - Sales

Load script

```
Example:
Load * inline [
Date, RecordID, StoreProduct, Sales, Store
2024-01-01, 1, Apple, 100, A
2024-01-15, 2, Banana, 80, B
2024-01-30, 3, Carrot, 50, C
2024-02-05, 4, Apple, 120, A
2024-02-20, 5, Banana, 90, B
2024-02-28, 6, Carrot, 60, D
2024-03-10, 7, Apple, 110, A
2024-03-22, 8, Banana, 85, B
2024-03-31, 9, Carrot, 55, C
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- StoreProduct

Create the following measures:

- =Only(Store), to calculate the unique store where the product is sold.
- =If(IsNull(Only(Store)), 'Multiple Stores', 'Single Store'), to calculate if the product is sold in a single store or in multiple stores.
- =Sum(Sales), to calculate the total product sales.

Results table

| StoreProduct | Only(Store) | If(IsNull(Only(Store)), 'Multiple Stores', 'Single Store') | Sum(Sales) |
| --- | --- | --- | --- |
| Apple | A | Single Store | 330 |
| Banana | B | Single Store | 255 |
| Carrot | - | Multiple Stores | 165 |

The results indicate that Apples and Bananas are sold in only a single store while Carrots are sold in multiple stores.

## Example - Advanced scenario to create a single-month table of records

Chart expression

Overview

This example uses the Only function to show a line-by-line table of records for a single month. To achieve this, set analysis is used to scope the desired record set. Set analysis requires at least one measure, although since we do not actually need to aggregate the record set, we can effectively use the Only aggregation function to host the set analysis scope.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- A preceding load statement that derives the MonthYear field from the Date field by truncating the day of the month, using the MonthStart function, and returning a date representation of the 1st of each month. This result is supplied to the Date function to set the display format to MMM YY, for example, Jan 24.
- The following fields in the data table:

  - Date
  - RecordID
  - StoreProduct
  - Sales
  - Store

Load script

```
Example:
Load
*,
date(MonthStart (Date),'MMM YY') AS MonthYear
inline [
Date, RecordID, StoreProduct, Sales, Store
2024-01-01, 1, Apple, 100, A
2024-01-15, 2, Banana, 80, B
2024-01-30, 3, Carrot, 50, C
2024-02-05, 4, Apple, 120, A
2024-02-20, 5, Banana, 90, B
2024-02-28, 6, Carrot, 60, D
2024-03-10, 7, Apple, 110, A
2024-03-22, 8, Banana, 85, B
2024-03-31, 9, Carrot, 55, C
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- MonthYear
- RecordID
- Date
- StoreProduct
- Store

Create the following measures:

- =Only({$<MonthYear={'$(=MaxString(MonthYear))'}>} Sales), to evaluate the Sales value and return only those where MonthYear is the latest (most recent) MonthYear available, based on the current selections in the table. The dollar-sign ($) expansion performs an in-line calculation using the MaxString function, $(=MaxString(MonthYear)), which returns the text representation of the latest MonthYear value.

Information noteAttempting to filter MonthYear based on the numeric representation, for example using the Max function, Max(MonthYear), would not deliver any result. Set analysis applies filter selections based only on the text representation of any dual data type; a data type with a numeric and text representation such as a Date.

Results table

| MonthYear | RecordID | Date | StoreProduct | Only({$<MonthYear={‘$(=MaxString(MonthYear))’}>} Sales) |
| --- | --- | --- | --- | --- |
| Mar 24 | 7 | 2024-03-10 | Apple | 110 |
| Mar 24 | 8 | 2024-03-22 | Banana | 85 |
| Mar 24 | 9 | 2024-03-31 | Carrot | 55 |

The output of the Only function produces a table of records that defaults to presenting the sales value for the latest, or most recent, MonthYear that is available in the data. If you select an earlier month from the MonthYear column, such as Feb 24, the latest sales value for that month will appear.

## Learn more

- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
- [*Defining the aggregation scope*](../define-aggregation-scope.htm)
