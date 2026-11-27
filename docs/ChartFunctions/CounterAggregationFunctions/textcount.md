---
title: "TextCount - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/CounterAggregationFunctions/textcount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# TextCount - chart function

Expand/Collapse all

# TextCount - chart function

TextCount()
 is used to aggregate the number of field values that are non-numeric in each chart dimension.

Syntax:

TextCount({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Example: Chart expressions

| Example | Result |
| --- | --- |
| TextCount(Product) | Returns the number of product names that have text values. |
| TextCount(OrderNumber) | Returns the number of rows in the OrderNumber field that have text values. Information note"0" counts as a value and not an empty cell. However, if a measure aggregates to 0 for a dimension, that dimension will not be included in charts. Empty cells are evaluated as being non-text and are not counted by TextCount. |
| TextCount (DISTINCT Product)/Count(Product) | Counts all the number of distinct text values of Product and divides it by the total number of values in Product. |

## Example - TextCount fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - Product
  - OrderNumber

Load script

```
Set NULLINTERPRET = ' ';
Example:
LOAD * inline [
Customer|Product|OrderNumber
Astrida|AA|1
Astrida|AA|7
Astrida|BB|4
Betacab|CC|6
Betacab|AA|5
Betacab|BB|
Canutility|AA|
Canutility|CC|
Divadip|CC|2
Divadip|DD|3
](delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add the following measures:

- =TextCount(Product), to return the number of product names that are text values.
- =TextCount(OrderNumber), to calculate the number of order numbers that are text values.
- =TextCount(DISTINCT Product)/Count(Product), to count the total number of distinct text values of Product and divide it by the total number of values in Product.

Results table

| TextCount(Product) | TextCount(OrderNumber) | TextCount(DISTINCT Product)/Count(Product) |
| --- | --- | --- |
| 10 | 3 | 0.4 |

The first measure returns 10 because all ten records in Product are text.

The second measure returns 3 because empty cells are treated as text and counted. Typically, you might use this type of measure to check that no numeric fields have been given text values or are empty.

The third measure returns 0.4. This result is calculated by dividing the total number of distinct text values of Product (4) by the total number of values in Product (10).

## Example - TextCount scenario

Chart expression

Overview

A dataset contains survey response data with both complaints and general feedback by product. You want to review only those responses with text values.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - CustomerID
  - ProductPurchased
  - Complaint
  - Feedback

Load script

```
Set NullInterpret = '';
Example:
Load * Inline [
CustomerID, ProductPurchased, Complaint, Feedback
1, Laptop, Slow performance, "The laptop is slow, poor battery, slow graphics"
2, Mobile, Heating issue, "Mobile heats up, average camera"
3, Laptop, Battery problem, "Battery not working, slow to charge"
4, Tablet, Screen issue, "Screen is broken, unresponsive touch"
5, Mobile, No issues, "Excellent performance"
6, Mobile, 123, "123"
7, Laptop, ,
8, Tablet, Warranty expired,
9, Mobile, , "Contact customer service"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ProductPurchased

Create the following measures:

- =TextCount(ProductPurchased), to calculate the number of product names with non-numeric values.
- =TextCount(Complaint), to calculate the number of complaints with non-numeric values.
- =TextCount(Feedback), to calculate the number of feedback values with non-numeric values.

Results table

| ProductPurchased | TextCount(ProductPurchased) | TextCount(Complaint) | TextCount(Feedback) |
| --- | --- | --- | --- |
| Laptop | 3 | 2 | 2 |
| Mobile | 4 | 2 | 3 |
| Tablet | 2 | 2 | 1 |

The results show that for the product Laptop, there are 3 records of which 2 have complaints and 2 have feedback. Similarly, for the product Mobile, there are 4 records, including 2 complaints and 3 feedback responses. Numeric values or empty values are not counted because it is expected that the ProductPurchased, Complaint and Feedback fields are text values.
