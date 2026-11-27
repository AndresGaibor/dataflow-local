---
title: "coalesce Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/coalesce.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---

# coalesce Script and chart function

Expand/Collapse all

# coalesce Script and chart function

The coalesce function returns the first of the parameters that has a valid non-NULL representation. Any number of parameters can be used.

Syntax:

coalesce(expr1[ , expr2
, expr3 , ...])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| expr1 | The first expression to check for a valid non-NULL representation. |
| expr2 | The second expression to check for a valid non-NULL representation. |
| expr3 | The third expression to check for a valid non-NULL representation. |

Examples: Chart expressions

| Example | Result |
| --- | --- |
| Coalesce(ProductDescription, ProductName, ProductCode, 'no description available') | This expression will select between three different product description fields when some fields do not have values for the product. Following the order listed in the function, the first field with a non-null value is returned. If none of the fields contain a value, the result will be no description available. |
| Coalesce(TextBetween(FileName, '"', '"'), FileName) | This expression will trim potential enclosing quotes from the field FileName. If the FileName given is quoted, these are removed, and the enclosed, unquoted FileName is returned. If the TextBetween function doesn't find the delimiters it returns null, which the Coalesce rejects, returning instead the raw FileName. |

## Example - Coalesce fundamentals

Chart expression

Overview

A data table is loaded that contains product and price data. You want to ensure that any null values are replaced with an alternative value.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ProductID
  - ProductName
  - Price
- A NullInterpret variable statement to ensure that any missing values are treated as NULL.

Load script

```
Set NullInterpret = '';
Example:
LOAD * INLINE [
ProductID, ProductName, Price
1, Laptop, 1000
2, , 800
3, Desktop, 1200
4, , 500
5, Tablet, 600
];
```

Results

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - ProductID
   - ProductName
2. Create the following calculated dimension:

   - =Coalesce(ProductName, 'Unknown Product')
3. Create the following measure:

   - =Sum(Price), to return a valid number representation.
4. Create a new table and add the following expression as a calculated dimension:

   - =Coalesce(ProductName, 'Unknown Product')
5. Create the following measure:

   - =Sum(Price), to return a valid number representation.

The results in the following tables show how the Coalesce function can replace the null values in the original dataset with the alternative value Unknown Product.

Results table 1

| ProductID | ProductName | Coalesce(ProductName, 'Unknown Product') | Sum(Price) |
| --- | --- | --- | --- |
| Totals |  |  | 4100 |  |
| 1 | Laptop | Laptop | 1000 |
| 2 | - | Unknown Product | 800 |
| 3 | Desktop | Desktop | 1200 |
| 4 | - | Unknown Product | 500 |
| 5 | Tablet | Tablet | 600 |

Results table 2

| Coalesce(ProductName, 'Unknown Product') | Sum(Price) |
| --- | --- |
| Totals | 5 |
| Desktop | 600 |
| Laptop | 1000 |
| Tablet | 600 |
| Unknown Product | 1300 |

## Example - Replace null values with a prioritized alternative value

Chart expression

Overview

This example uses the Coalesce function to replace missing location data with an alternative value according to the specified priority logic.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - LocationID
  - Country
  - State
  - City
- A NullInterpret variable statement to ensure that any missing values are treated as NULL.

Load script

```
Set NullInterpret = '';
Example:
LOAD * INLINE [
LocationID, Country, State, City
L001, USA, California, Los Angeles
L002, USA, ,
L003, Canada, Ontario,
L004, , New South Wales, Sydney
L005, UK, , London
L006, , , London
];
```

Results

1. Load the data and open a sheet. Create a new table and add these fields as dimensions:

   - LocationID
   - Country
   - State
   - City
2. Create the following calculated dimension:

   - =Coalesce(Country, State, City), to populate any null values with alternatives.

Results table

| LocationID | Country | State | City | Coalesce(Country, State, City) |
| --- | --- | --- | --- | --- |
| L001 | USA | California | Los Angeles | USA |
| L002 | USA | - | - | USA |
| L003 | Canada | Ontario | - | Canada |
| L004 | - | New South Wales | Sydney | New South Wales |
| L005 | UK | - | London | UK |
| L006 | - | - | London | London |

The results show that although there are missing values, you can use the Coalesce function to provide logic about how to populate these instances with an alternative value to complete the dataset. For example, L004 is missing a Country value. The Coalesce function returns New South Wales because State is the second field listed in the priority logic to use when the value for Country is missing.
