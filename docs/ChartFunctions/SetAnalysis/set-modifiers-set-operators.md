---
title: "Set modifiers with set operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers-set-operators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis", "Set modifiers"]
---

# Set modifiers with set operators

Set operators are used to include, exclude, or intersect different element sets. They combine the different methods to define element sets.

The operators are the same as those used for set identifiers.

Operators

| Operator | Description |
| --- | --- |
| + | Union. This binary operation returns a set consisting of the records or elements that belong to any of the two set operands. |
| - | Exclusion. This binary operation returns a set consisting of the records or elements that belong to the first but not the other of the two set operands. Also, when used as a unary operator, it returns the complement set. |
| \* | Intersection. This binary operation returns a set consisting of the records or elements that belong to both set operands. |
| / | Symmetric difference (XOR). This binary operation returns a set consisting of the records or elements that belong to either, but not both set operands. |

For example, the following two modifiers define the same set of [field](#glossary-0 "Glossary term") values:

- <Year = {1997, "20\*"}>
- <Year = {1997} + {"20\*"}>

Both expressions select 1997 and the years that begin with 20. In other words, this is the union of the two conditions.

Set operators also allow for more complex definitions. For example:

<Year = {1997, "20\*"} - {2000}>

This expression will select the same years as those above, but in addition exclude year 2000.

For more information, see [*Set operators*](set-operators.htm).

## Examples: Chart expressions for set modifiers with set operators

Examples - chart expressions

Load script

Load the following data as an inline load in the data load editor to create the chart expression examples below.

```
MyTable:
Load
Year(Date) as Year,
Date#(Date,'YYYY-MM-DD') as ISO_Date,
Date(Date#(Date,'YYYY-MM-DD'),'M/D/YYYY') as US_Date,
Country, Product, Amount
Inline
[Date, Country, Product, Amount
2018-02-20, Canada, Washer, 6
2018-07-08, Germany, Anchor bolt, 10
2018-07-14, Germany, Anchor bolt, 3
2018-08-31, France, Nut, 2
2018-09-02, Czech Republic, Bolt, 1
2019-02-11, Czech Republic, Bolt, 3
2019-07-31, Czech Republic, Washer, 6
2020-03-13, France, Anchor bolt, 1
2020-07-12, Canada, Anchor bolt, 8
2020-09-16, France, Washer, 1];
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

Chart expressions

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers with set operators

| Country | Sum(Amount) | Sum({<Year={">2018"}-{2020}>} Amount) | Sum({<Country=-{Germany}>} Amount) | Sum({<Country={Germany}+P({<Product={Nut}>}Country)>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 9 | 28 | 17 |
| Canada | 14 | 0 | 14 | 0 |
| Czech Republic | 10 | 9 | 10 | 0 |
| France | 4 | 0 | 4 | 4 |
| Germany | 13 | 0 | 0 | 13 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<Year={">2018"}-{2020}>}Amount)

    Sum Amount for all years after 2018, except 2020.
  - Sum({<Country=-{Germany}>}Amount)

    Sum Amount for all countries except Germany. Note the unary exclusion operator.
  - Sum({<Country={Germany}+P({<Product={Nut}>}Country)>}Amount)

    Sum Amount for Germany and all countries associated with the product Nut.

Set modifiers with set operators

![Set modifiers with set operators.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_set_operators.png "Click to view full size")

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

| Examples | Results |
| --- | --- |
| sum( {$<Product = Product + {OurProduct1} – {OurProduct2} >} Sales ) | Returns the sales for the current selection, but with the product “OurProduct1” added to the list of selected products and “OurProduct2” removed from the list of selected products. |
| sum( {$<Year = Year + ({“20\*”,1997} – {2000}) >} Sales ) | Returns the sales for the current selection but with additional [selections](#glossary-1 "Glossary term") in the field “Year”: 1997 and all that begin with “20” – however, not 2000.  Note that if 2000 is included in the current selection, it will still be included after the modification. |
| sum( {$<Year = (Year + {“20\*”,1997}) – {2000} >} Sales ) | Returns almost the same as above, but here 2000 will be excluded, also if it initially is included in the current selection. The example shows the importance of sometimes using brackets to define an order of precedence. |
| sum( {$<Year = {“\*”} – {2000}, Product = {“\*bearing\*”} >} Sales ) | Returns the sales for the current selection but with a new selection in “Year”: all years except 2000; and only for products containing the string 'bearing'. |
