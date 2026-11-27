---
title: "mixmatch Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/mixmatch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---

# mixmatch Script and chart function

Expand/Collapse all

# mixmatch Script and chart function

The mixmatch function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case insensitive and insensitive to the Japanese Hiragana and Katakana character systems.

Syntax:

mixmatch( str, expr1
[ , expr2,...exprN ])

Return data type: integer

If you want to use case sensitive comparison, use the match function. If you want to use case insensitive comparison and wildcards, use the wildmatch function.

Arguments

| Argument | Description |
| --- | --- |
| str | The string to be evaluated. |
| expr1 | The first expression to check for a valid number representation. |
| expr2 | The second expression to check for a valid number representation. |
| expr3 | The third expression to check for a valid number representation. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| mixmatch( ColorCode,'black','Blue' ) | This expression returns 1 if the value of ColorCode is Black or 2 if the value of ColorCode is Blue. |
| mixmatch( Cities,'toronto','Boston','Beijing','Zurich' ) | This expression returns the index of the item that matches the value in the Cities field. |

Some of the examples in this topic use inline loads. For more information, see [*Using inline loads to load data*](../inline-loads-qs.htm).

## Example - Categorize products using mixmatch

Chart expression

Overview

A data set contains product data. You want to identify and categorize products that are consumable.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ProductID
  - ProductName
  - ProductCategory

Load script

```
Example:
LOAD * INLINE [
ProductID, ProductName, ProductCategory
1, "Laptop", "Electronics"
2, "Banana", "Fruits"
3, "Shampoo", "toiletries"
4, "TV", "Electronics"
5, "Apple", "fruits"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ProductID
- ProductName
- ProductCategory

Create the following measures:

- =mixmatch(ProductCategory,'Toiletries', 'Fruits'), to return the index where ProductCategory has the value Toiletries or Fruits.
- =If(mixmatch(ProductCategory, 'Toiletries', 'Fruits'), 'Consumable', 'Other'), to translate a ProductCategory match against either Toiletries or Fruits as Consumable. If no match is found, then Other is returned.

Information noteThe mixmatch function returns a non-zero positive value if a match is found, else zero if no match is found. The if statement in turn interprets non-zero results as true and zero results as false. By combining an if statement with mixmatch, wildmatch or match functions, it is possible to easily decode matches and mismatches.

Results table

| ProductID | ProductName | ProductCategory | mixmatch(ProductCategory,'Toiletries', 'Fruits') | If(mixmatch(ProductCategory, 'Toiletries', 'Fruits'), 'Consumable', 'Other') |
| --- | --- | --- | --- | --- |
| 1 | Laptop | Electronics | 0 | Other |
| 2 | Banana | Fruits | 2 | Consumable |
| 3 | Shampoo | toiletries | 1 | Consumable |
| 4 | TV | Electronics | 0 | Other |
| 5 | Apple | fruits | 2 | Consumable |

The mixmatch function returns the index of the search string in the first measure. In the second measure, this result is then used in an If function to provide custom results. Note that the mixmatch function is case insensitive.

## Example - Evaluate and classify client data using mixmatch

Chart expression

Overview

A data set contains client data. You want to identify and categorize the clients whose region and industry category meet your classification requirements.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ClientID
  - ClientName
  - Region
  - Industry

Load script

```
Example:
LOAD * INLINE [
ClientID, ClientName, Region, Industry
1, "Acme Corp", "north", "manufacturing"
2, "Beta Ltd", "East", "Technology"
3, "Gamma Inc", "west", "Retail"
4, "Delta LLC", "North", "Technology"
5, "Epsilon GmbH", "South", "healthcare"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ClientID
- ClientName
- Region
- Industry

Create the following measure:

=If(mixmatch(Region, 'North', 'East') AND mixmatch(Industry, 'Technology', 'Manufacturing'), 'Target Segment', 'Secondary Segment'), to return the index of the search string. If found, then Target Segment is returned. If not found, then Secondary Segment is returned.

Results table

| ClientID | ClientName | Region | Industry | If(mixmatch(Region, 'North', 'East') AND mixmatch(Industry, 'Technology', 'Manufacturing'), 'Target Segment', 'Secondary Segment') |
| --- | --- | --- | --- | --- |
| 1 | Acme Corp | north | manufacturing | Target Segment |
| 2 | Beta Ltd | East | Technology | Target Segment |
| 3 | Gamma Inc | west | Retail | Secondary Segment |
| 4 | Delta LLC | North | Technology | Target Segment |
| 5 | Epsilon GmbH | South | healthcare | Secondary Segment |

The mixmatch function searches for text and returns an index that can then be used to perform additional analysis and data classification. For example, Acme Corp is classified as a Target Segment because it meets the search requirements of the mixmatch function for both the Region and Industry fields. Note that the mixmatch function is case insensitive.

## Example - Load script using mixmatch

Load script

Overview

You can use mixmatch to load a subset of data. For example, you can return a numeric value for an expression in the function. You can then limit the data that is loaded based on the numeric value. Mixmatch returns 0 if there is no match. All expressions that are not matched in this example will therefore return 0 and will be excluded from the data load by the WHERE statement.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into two data tables called:

  - Transactions: Includes transaction fields
  - Transaction\_Buckets: Creates two new fields Customer and Color Code - Black, Blue, blue. The where statement loads the results from the mixmatch function.

Load script

```
Transactions:
Load * Inline [
transaction_id, transaction_date, transaction_amount, transaction_quantity, customer_id, size, color_code
3750, 20180830, 23.56, 2, 2038593, L, Red
3751, 20180907, 556.31, 6, 203521, m, orange
3752, 20180916, 5.75, 1, 5646471, S, blue
3753, 20180922, 125.00, 7, 3036491, l, Black
3754, 20180922, 484.21, 13, 049681, xs, Red
3756, 20180922, 59.18, 2, 2038593, M, Blue
3757, 20180923, 177.42, 21, 203521, XL, Black
];

/*
Create new table called Transaction_Buckets
Create new fields called Customer, and Color code - Black, Blue, blue
Load Transactions table.
Mixmatch returns 1 for 'Black', 2 for 'Blue'.
Also returns 3 for 'blue' because mixmatch is not case sensitive.
Only values that returned numeric value greater than 0
are loaded by WHERE statement into Transactions_Buckets table.
*/

Transaction_Buckets:
Load
   customer_id,
   customer_id as [Customer],
   color_code as [Color Code - Black, Blue, blue]
Resident Transactions
Where mixmatch(color_code,'Black','Blue') > 0;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- [Color Code - Black, Blue, blue]
- Customer

Results table showing the output from using the mixmatch function in the load script.

| Color Code - Black, Blue, blue | Customer |
| --- | --- |
| Black | 203521 |
| Black | 3036491 |
| Blue | 2038593 |
| blue | 5646471 |

## Example - Chart expression using mixmatch

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Cities
  - Count

Load script

```
Example:
Load * inline [Cities, Count
Toronto, 123
Toronto, 234
Toronto, 231
Boston, 32
Boston, 23
Boston, 1341
Beijing, 234
Beijing, 45
Beijing, 235
Stockholm, 938
Stockholm, 39
Stockholm, 189
zurich, 2342
zurich, 9033
zurich, 0039];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Cities

Create the following measures:

- =mixmatch( Cities,'Toronto','Boston','Beijing','Zurich'), to return the index of the search string.
- =mixmatch( Cities,'Toronto','Boston','Beijing','Stockholm','Zurich'), to return the index of the search string.
- =Cities & ' - ' & mixmatch ( Cities, 'Toronto','Boston', 'Beijing','Stockholm','Zurich'), to return the Cities field and the index of the search string.

The first measure in the table below returns 0 for Stockholm because Stockholm is not included in the list of expressions in the mixmatch function. It also returns 4 for Zurich because the mixmatch comparison is not case sensitive.

Results table

| Cities | mixmatch( Cities,'Toronto','Boston','Beijing','Zurich') | mixmatch( Cities,'Toronto','Boston','Beijing','Stockholm','Zurich') | Cities & ' - ' & mixmatch ( Cities, 'Toronto','Boston', 'Beijing','Stockholm','Zurich') |
| --- | --- | --- | --- |
| Beijing | 3 | 3 | Beijing - 3 |
| Boston | 2 | 2 | Boston - 2 |
| Stockholm | 0 | 4 | Stockholm - 4 |
| Toronto | 1 | 1 | Toronto - 1 |
| zurich | 4 | 5 | zurich - 5 |

## Example - Custom sort expression using mixmatch

Chart expression

Overview

You can use mixmatch to perform a custom sort for an expression. This example uses the same dataset as the previous example.

By default, columns sort numerically or alphabetically depending on the data.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Cities

Results table showing the default sort order

| Cities |
| --- |
| Beijing |
| Boston |
| Stockholm |
| Toronto |
| zurich |

To change the sort order, do the following:

1. Open the Sorting section for your chart in the Properties panel.
2. Turn off auto sorting for the column on which you want to do a custom sort.
3. Clear the Sort numerically and Sort alphabetically check boxes.
4. Select Sort by expression, and then enter an expression similar to the following:

   =mixmatch( Cities, 'Toronto','Boston','Beijing','Stockholm','Zurich')

   The sort order on the Cities column changes.

Results table showing the sort order using the mixmatch function

| Cities |
| --- |
| Toronto |
| Boston |
| Beijing |
| Stockholm |
| zurich |

## Learn more

- [*match Script and chart function*](match.htm)
- [*wildmatch Script and chart function*](wildmatch.htm)
