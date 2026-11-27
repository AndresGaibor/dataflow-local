---
title: "class Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/class.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---

# class Script and chart function

Expand/Collapse all

# class Script and chart function

The class function assigns the first parameter to a class interval.
The result is a dual value with a<=x<b as the textual value, where a and b are the upper and lower
limits of the bin, and the lower bound as numeric value.

Syntax:

class(expression, interval [ , label [ , offset ]])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| interval | A number that specifies the bin width. |
| label | An arbitrary string that can replace the 'x' in the result text. |
| offset | A number that can be used as offset from the default starting point of the classification. The default starting point is normally 0. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| class( var,10 ) with var = 23 | Returns 20<=x<30 |
| class( var,5,'value' ) with var = 23 | Returns 20<= value <25 |
| class( var,10,'x',5 ) with var = 23 | Returns 15<=x<25 |

Some of the examples in this topic use inline loads. For more information, see [*Using inline loads to load data*](../inline-loads-qs.htm).

## Example - class fundamentals

Chart expression

Overview

A data table is loaded that contains names and ages. You want to classify the people by age groups (with a ten year interval) and provide a count of the number of people in each group.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Age
  - Name

Load script

```
Example:
LOAD * INLINE [
Age, Name
25, John
42, Karen
53, Yoshi
43, Bob
27, Charles
];
```

Results

1. Load the data and open a sheet. Create two new tables.
2. In the first table, do the following:

   1. Add these dimensions:

      - Age
      - Name
   2. Create the following measure:

      - =class(Age, 10, 'age'), to classify the data into age categories.
3. In the second table, do the following:
   1. Add this expression as a dimension

      - =class(Age, 10, 'age')
   2. Create the following measure:

      - =Count(Age), to count the number of people age classification.

The first table shows the raw data for Name and Age, and which age category they are classified in.

Results table 1

| Name | Age | class(Age, 10, 'age') |
| --- | --- | --- |
| Bob | 43 | 40 <= age < 50 |
| Charles | 27 | 20 <= age < 30 |
| John | 25 | 20 <= age < 30 |
| Karen | 42 | 40 <= age < 50 |
| Yoshi | 53 | 50 <= age < 60 |

In the second table, you can see how the data is now classified and summarized. The results of the class function created 3 age categories in the first measure. The second measure counts the number of people in each age category.

Results table 2

| class(Age, 10, 'age') | Count(Age) |
| --- | --- |
| Totals | 5 |
| 20 <= age < 30 | 2 |
| 40 <= age < 50 | 2 |
| 50 <= age < 60 | 1 |

Load script

Overview

A data table is loaded that contains names and ages. You want to add a [field](#glossary-0 "Glossary term") that classifies each person according to an age group with a ten year interval. The original source table looks like the following.

Original source table

| Name | Age |
| --- | --- |
| John | 25 |
| Karen | 42 |
| Yoshi | 53 |

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [preceding load](#glossary-1 "Glossary term") statement that uses the class function to create a new field called Agegroup.

Load script

```
LOAD *,
class(Age, 10, 'age') As Agegroup;

LOAD * INLINE
[ Age, Name
25, John
42, Karen
53, Yoshi];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Name
- Age
- Agegroup

Results table

| Name | Age | Agegroup |
| --- | --- | --- |
| John | 25 | 20 <= age < 30 |
| Karen | 42 | 40 <= age < 50 |
| Yoshi | 53 | 50 <= age < 60 |

The new field Agegroup classifies each person by age category.

## Example - class scenario

Chart expression

Overview

A data table is loaded that contains customer data. You want to classify customers by the number of lifetime value points earned and provide a count of the number of customers in each category.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - CustomerID
  - CustomerName
  - LifetimeValue

Load script

```
Example:
Load * Inline [
CustomerID, CustomerName, LifetimeValue
1, John Doe, 12500
2, Jane Smith, 36000
3, Sam Brown, 15000
4, Lisa White, 50000
5, Tom Harris, 22000
];
```

Results

1. Load the data and open a sheet. Create two new tables.
2. In the first table, do the following:

   1. Add these dimensions:

      - CustomerID
      - CustomerName
      - LifetimeValue
   2. Create the following calculated dimension:
      - =Class(LifetimeValue, 10000, 'Lifetime Value Group'), to classify the data based on the LifetimeValue field.
3. In the second table, do the following:
   1. Add this expression as a dimension

      - =Class(LifetimeValue, 10000, 'Lifetime Value Group')
   2. Create the following measure:

      - =Count(CustomerID), to count the number of people age classification.

The first table shows the raw data that has been entered and the results of using the class function.

Results table 1

| CustomerID | CustomerName | LifetimeValue | Class(LifetimeValue, 10000, 'Lifetime Value Group') |
| --- | --- | --- | --- |
| 1 | John Doe | 12500 | 10000 <= Lifetime Value Group < 20000 |
| 2 | Jane Smith | 36000 | 30000 <= Lifetime Value Group < 40000 |
| 3 | Sam Brown | 15000 | 10000 <= Lifetime Value Group < 20000 |
| 4 | Lisa White | 50000 | 50000 <= Lifetime Value Group < 60000 |
| 5 | Tom Harris | 22000 | 20000 <= Lifetime Value Group < 30000 |

The second table shows how the data can be classified and summarized. The data is categorized into four groups using the class function, and then counted to show the number of customers in each group.

Results table 2

| Class(LifetimeValue, 10000, 'Lifetime Value Group') | Count(CustomerID) |
| --- | --- |
| Totals | 5 |
| 10000 <= Lifetime Value Group < 20000 | 2 |
| 20000 <= Lifetime Value Group < 30000 | 1 |
| 30000 <= Lifetime Value Group < 40000 | 1 |
| 50000 <= Lifetime Value Group < 60000 | 1 |
