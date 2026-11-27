---
title: "Set modifiers using set functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers-implicit-field-value-definitions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis", "Set modifiers"]
---

# Set modifiers using set functions

Sometimes you need to define a set of [field](#glossary-0 "Glossary term") values using a nested set definition. For example, you may want to select all customers that have bought a specific product, without selecting the product.

In such cases, use the element set functions P() and E(). These return the element sets of possible values and excluded values of a field, respectively. Inside the brackets, you can specify the field in question, and a set expression that defines the scope. For example:

P({1<Year = {2021}>} Customer)

This will return the set of customers that had transactions in 2021. You can then use this in a set modifier. For example:

Sum({<Customer = P({1<Year = {2021}>} Customer)>} Amount)

This set expression will select these customers, but it will not restrict the selection to 2021.

These functions cannot be used in other expressions.

Additionally, only natural sets can be used inside the element set functions. That is, a set of records that can be defined by a simple selection.

For example, the set given by {1-$} cannot always be defined through a selection, and is therefore not a natural set. Using these functions on non-natural sets will return unexpected results.

## Examples: Chart expressions for set modifiers using set functions

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

Table - Set modifiers using set functions

| Country | Sum(Amount) | Sum({<Country=P({<Year={2019}>}Country)>} Amount) | Sum({<Product=P({<Year={2019}>}Product)>} Amount) | Sum({<Country=E({<Product={Washer}>}Country)>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 10 | 17 | 13 |
| Canada | 14 | 0 | 6 | 0 |
| Czech Republic | 10 | 10 | 10 | 0 |
| France | 4 | 0 | 1 | 0 |
| Germany | 13 | 0 | 0 | 13 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<Country=P({<Year={2019}>} Country)>} Amount)

    Sum Amount for the countries that are associated with year 2019. It will however not limit the calculation to 2019.
  - Sum({<Product=P({<Year={2019}>} Product)>} Amount)

    Sum Amount for the products that are associated with year 2019. It will however not limit the calculation to 2019.
  - Sum({<Country=E({<Product={Washer}>} Country)>} Amount)

    Sum Amount for the countries that are not associated with the product Washer.

Set modifiers using set functions

![Set modifiers using set functions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_modifiers_set_functions.png "Click to view full size")

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

| Examples | Results |
| --- | --- |
| sum( {$<Customer = P({1<Product={'Shoe'}>} Customer)>} Sales ) | Returns the sales for current selection, but only those customers that ever have bought the product 'Shoe'. The element function P( ) here returns a list of possible customers; those that are implied by the selection 'Shoe' in the field Product. |
| sum( {$<Customer = P({1<Product={'Shoe'}>})>} Sales ) | Same as above. If the field in the element function is omitted, the function will return the possible values of the field specified in the outer assignment. |
| sum( {$<Customer = P({1<Product={'Shoe'}>} Supplier)>} Sales ) | Returns the sales for current selection, but only those customers that ever have supplied the product 'Shoe', that is, the customer is also a supplier. The element function P( ) here returns a list of possible suppliers; those that are implied by the selection 'Shoe' in the field Product. The list of suppliers is then used as a selection in the field Customer. |
| sum( {$<Customer = E({1<Product={'Shoe'}>})>} Sales ) | Returns the sales for current selection, but only those customers that never bought the product 'Shoe'. The element function E( ) here returns the list of excluded customers; those that are excluded by the selection 'Shoe' in the field Product. |
