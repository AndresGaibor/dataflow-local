---
title: "Set modifiers with implicit set operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers-using-assignments-implicit-set-operators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis", "Set modifiers"]
---

# Set modifiers with implicit set operators

The standard way to write [selections](#glossary-0 "Glossary term") in a set modifier is to use an equals sign. For example:

Year = {">2015"}

The expression to the right of the equals sign in the set modifier is called an element set. It defines a set of distinct [field](#glossary-1 "Glossary term") values, in other words a selection.

This notation defines a new selection, disregarding the current selection in the field. So, if the set identifier contains a selection in this field, the old selection will be replaced by the one in the element set.

When you want to base your selection on the current selection in the field, you need to use a different expression

For example, if you want to respect the old selection, and add the requirement that the year is after 2015, you can write the following:

Year = Year \* {">2015"}

The asterisk is a set operator defining an intersection, so you will get the intersection between the current selection in Year, and the additional requirement that the year be after 2015. An alternative way to write this is the following:

Year \*= {">2015"}

That is, the assignment operator (\*=) implicitly defines an intersection.

Similarly, implicit unions, exclusions and symmetric differences can be defined using the following: +=, –=, /=

## Examples: Chart expressions for set modifiers with implicit set operators

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

Chart expressions with implicit set operators

Create a table in a Qlik Sense sheet with the following chart expressions.

Select Canada and Czech Republic from a list of countries.

Table - Chart expressions with implicit set operators

| Country | Sum(Amount) | Sum({<Country\*={Canada}>} Amount) | Sum({<Country-={Canada}>} Amount) | Sum({<Country+= {France}>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 24 | 14 | 10 | 28 |
| Canada | 14 | 14 | 0 | 14 |
| Czech Republic | 10 | 0 | 10 | 10 |
| France | 0 | 0 | 0 | 4 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount for the current selection. Note that only Canada and Czech Republic have non-zero values.
  - Sum({<Country\*={Canada}>}Amount)

    Sum Amount for the current selection, intersected with the requirement that the Country be Canada. If Canada is not part of the user selection, the set expression returns an empty set, and the column will have 0 on all rows.
  - Sum({<Country-={Canada}>}Amount)

    Sum Amount for the current selection, but first exclude Canada from the Country selection. If Canada is not part of the user selection, the set expression will not change any numbers.
  - Sum({<Country+={France}>}Amount)

    Sum Amount for the current selection, but first add France to the Country selection. If France is already part of the user selection, the set expression will not change any numbers.

Set modifiers with implicit set operators

![Set modifiers with implicit set operators.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_implicit_set_operators.png "Click to view full size")

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

| Examples | Results |
| --- | --- |
| sum( {$<Product += {OurProduct1, OurProduct2} >} Sales ) | Returns the sales for the current selection, but using an implicit union to add the products 'OurProduct1' and 'OurProduct2' to the list of selected products. |
| sum( {$<Year += {“20\*”,1997} – {2000} >} Sales ) | Returns the sales for the current selection but using an implicit union to add a number of years in the selection: 1997 and all that begin with “20” – however, not 2000.  Note that if 2000 is included in the current selection, it will still be included after the modification. Same as <Year=Year + ({“20\*”,1997}–{2000})>. |
| sum( {$<Product \*= {OurProduct1} >} Sales ) | Returns the sales for the current selection, but only for the intersection of currently selected products and the product OurProduct1. |
