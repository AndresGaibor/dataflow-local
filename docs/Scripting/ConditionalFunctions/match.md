---
title: "match Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/match.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---
Expand/Collapse all

# match Script and chart function

The match function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case sensitive.

Syntax:

match( str, expr1
[ , expr2,...exprN ])

Return data type: integer

> **Tip:** If you want to use case insensitive comparison, use the mixmatch function. If you want to use case insensitive comparison and wildcards, use the wildmatch function.

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
| `match( ColorCode,'Blue','Black' )` | This expression returns the index of the match to the `ColorCode` field. If the value of `ColorCode` is `Blue` then it returns `1`. If the value of `ColorCode` is `Black` then it returns `2`. If no match is found then `0` is returned. |
| `match( Region, 'North', 'East' )` | This expression returns the index of the match to the `Region` field. If the value of `Region` is `North` then it returns `1`. If the value of `Region` is `East` then it returns `2`. If no match is found then `0` is returned. |

Some of the examples in this topic use inline loads. For more information, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

## Example - Categorize products using match

Chart expression

Overview

A data set contains product data. You want to identify and categorize products that are consumable.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductID`
  - `ProductName`
  - `ProductCategory`

Load script

```
Example:
LOAD * INLINE [
ProductID, ProductName, ProductCategory
1, "Laptop", "Electronics"
2, "Banana", "Fruits"
3, "Shampoo", "Toiletries"
4, "TV", "Electronics"
5, "Apple", "Fruits"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ProductID`
- `ProductName`
- `ProductCategory`

Create the following measures:

- `=match(ProductCategory,'Toiletries', 'Fruits')`, to return the index where `ProductCategory` has the value `Toiletries` or `Fruits`.
- `=If(match(ProductCategory, 'Toiletries', 'Fruits'), 'Consumable', 'Other')`, to return the index where `ProductCategory` has the value `Toiletries` or `Fruits`. If either are found, then `Consumable` is returned. Otherwise, `Other` is returned.

Results table

| ProductID | ProductName | ProductCategory | match(ProductCategory,'Toiletries', 'Fruits') | If(match(ProductCategory, 'Toiletries', 'Fruits'), 'Consumable', 'Other') |
| --- | --- | --- | --- | --- |
| 1 | Laptop | Electronics | 0 | Other |
| 2 | Banana | Fruits | 2 | Consumable |
| 3 | Shampoo | Toiletries | 1 | Consumable |
| 4 | TV | Electronics | 0 | Other |
| 5 | Apple | Fruits | 2 | Consumable |

The `match` function returns the index of the search string in the first measure. In the second measure, this result is then used in an `If` function to categorize products as `Consumable` or `Other`.

## Example - Evaluate and classify client data using match

Chart expression

Overview

A data set contains client data. You want to identify and categorize the clients whose region and industry category meet your classification requirements.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ClientID`
  - `ClientName`
  - `Region`
  - `Industry`

Load script

```
Example:
LOAD * INLINE [
ClientID, ClientName, Region, Industry
1, "Acme Corp", "North", "Manufacturing"
2, "Beta Ltd", "East", "Technology"
3, "Gamma Inc", "West", "Retail"
4, "Delta LLC", "North", "Technology"
5, "Epsilon GmbH", "South", "Healthcare"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ClientID`
- `ClientName`
- `Region`
- `Industry`

Create the following measure:

`=IF(match(Region, 'North', 'East') AND match(Industry, 'Technology', 'Manufacturing'), 'Target Segment', 'Secondary Segment')`, to return the index of the search string. If found, then `Target Segment` is returned. If not found, then `Secondary Segment` is returned.

Results table

| ClientID | ClientName | Region | Industry | IF(match(Region, 'North', 'East') AND match(Industry, 'Technology', 'Manufacturing'), 'Target Segment', 'Secondary Segment') |
| --- | --- | --- | --- | --- |
| 1 | Acme Corp | North | Manufacturing | Target Segment |
| 2 | Beta Ltd | East | Technology | Target Segment |
| 3 | Gamma Inc | West | Retail | Secondary Segment |
| 4 | Delta LLC | North | Technology | Target Segment |
| 5 | Epsilon GmbH | South | Healthcare | Secondary Segment |

The `match` function searches for text and returns an index that can then be used to perform additional analysis and data classification. For example, `Acme Corp` is classified as a `Target Segment` because it meets the search requirements of the `match` function for both the `Region` and `Industry` fields.

## Example: Load script using match

Load script

Overview

You can use match to load a subset of data. For example, you can return a numeric value for an expression in the function. You can then limit the data that is loaded based on the numeric value. The Match function returns 0 if there is no match. All expressions that are not matched in this example will therefore return 0 and will be excluded from the data load by the `WHERE` statement.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into two data tables called:

  - `Transactions`: Includes transaction fields
  - `Transaction_Buckets`: Creates two new fields `Customer` and `Color Code Blue and Black`. The `where` statement loads the results from the `match` function.

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
Create new fields called Customer, and Color code Blue and Black
Load Transactions table.
Match returns 1 for 'Blue', 2 for 'Black'. 
Does not return a value for 'blue' because match is case sensitive.
Only values that returned numeric value greater than 0 
are loaded by WHERE statement into Transactions_Buckets table.
*/
 
Transaction_Buckets:
Load
 customer_id,
 customer_id as [Customer], 
 color_code as [Color Code Blue and Black]
Resident Transactions
Where match(color_code,'Blue','Black') > 0;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `[Color Code Blue and Black]`
- `Customer`

Results table showing the output from using the match function in the load script

| Color Code Blue and Black | Customer |
| --- | --- |
| Black | 203521 |
| Black | 3036491 |
| Blue | 2038593 |

## Example - Chart expression using match

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Cities`
  - `Count`

Load script

```
Example:
Load * inline [
Cities, Count
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

- `Cities`

Create the following measures:

- `=match( Cities,'Toronto','Boston','Beijing','Zurich')`, to return the index of the search string.
- `=match( Cities,'Toronto','Boston','Beijing','Stockholm','zurich')`, to return the index of the search string.
- `=Cities & ' - ' & match ( Cities, 'Toronto','Boston', 'Beijing','Stockholm','zurich')`, to return the `Cities` field and the index of the search string.

The first measure in the table below returns `0` for `Stockholm` because `Stockholm` is not included in the list of expressions in the `match` function. It also returns `0` for `Zurich` because the `match` comparison is case sensitive.

Results table

| Cities | match( Cities,'Toronto','Boston','Beijing','Zurich') | match( Cities,'Toronto','Boston','Beijing','Stockholm','zurich') | Cities & ' - ' & match ( Cities, 'Toronto','Boston', 'Beijing','Stockholm','zurich') |
| --- | --- | --- | --- |
| Beijing | 3 | 3 | Beijing - 3 |
| Boston | 2 | 2 | Boston - 2 |
| Stockholm | 0 | 4 | Stockholm - 4 |
| Toronto | 1 | 1 | Toronto - 1 |
| zurich | 0 | 5 | zurich - 5 |

## Example - Custom sort expression using match

Chart expression

Overview

You can use `match` to perform a custom sort for an expression. This example uses the same dataset as the previous example.

By default, columns sort numerically or alphabetically depending on the data.

Results table showing the default sort order

| Cities |
| --- |
| Beijing |
| Boston |
| Stockholm |
| Toronto |
| zurich |

To change the sort order, do the following:

1. Open the **Sorting** section for your chart in the **Properties** panel.
2. Turn off auto sorting for the column on which you want to do a custom sort.
3. Clear the **Sort numerically** and **Sort alphabetically** check boxes.
4. Select **Sort by expression**, and then enter an expression similar to the following:

   `=match( Cities, 'Toronto','Boston','Beijing','Stockholm','zurich')`

   The sort order on the Cities column changes.

Results table showing the sort order using the match function

| Cities |
| --- |
| Toronto |
| Boston |
| Beijing |
| Stockholm |
| zurich |

## Learn more

- [*mixmatch Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/mixmatch.htm)
- [*wildmatch Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/wildmatch.htm)
