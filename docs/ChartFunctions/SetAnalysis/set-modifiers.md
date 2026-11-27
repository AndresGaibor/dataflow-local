---
title: "Set modifiers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Set modifiers

Set expressions are used to define the scope of a calculation. The central part of the set expression is the set modifier that specifies a selection. This is used to modify the user selection, or the selection in the set identifier, and the result defines a new scope for the calculation.

The set modifier consists of one or more [field](#glossary-0 "Glossary term") names, each followed by a selection that should be made on the field. The modifier is enclosed by angled brackets: < >

For example:

- Sum ( {$<Year = {2015}>} Sales )
- Count ( {1<Country = {Germany}>} distinct OrderID )
- Sum ( {$<Year = {2015}, Country = {Germany}>} Sales )

## Element sets

An element set can be defined using the following:

- A list of values
- A search
- A reference to another field
- A set function

If the element set definition is omitted, the set modifier will clear any selection in this field. For example:

Sum( {$<Year = >} Sales )

## Examples: Chart expressions for set modifiers based on element sets

Examples - chart expressions

Load script

Load the following data as an inline load in the data load editor to create the chart expression examples below.

```
MyTable:
Load * Inline [
Country, Year, Sales
Argentina, 2014, 66295.03
Argentina, 2015, 140037.89
Austria, 2014, 54166.09
Austria, 2015, 182739.87
Belgium, 2014, 182766.87
Belgium, 2015, 178042.33
Brazil, 2014, 174492.67
Brazil, 2015, 2104.22
Canada, 2014, 101801.33
Canada, 2015, 40288.25
Denmark, 2014, 45273.25
Denmark, 2015, 106938.41
Finland, 2014, 107565.55
Finland, 2015, 30583.44
France, 2014, 115644.26
France, 2015, 30696.98
Germany, 2014, 8775.18
Germany, 2015, 77185.68
];
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

Chart expressions

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers based on element sets

| Country | Sum(Sales) | Sum({1<Country={Belgium}>} Sales) | Sum({1<Country={"\*A\*"}>} Sales) | Sum({1<Country={"A\*"}>} Sales) | Sum({1<Year={$(=Max(Year))}>} Sales) |
| --- | --- | --- | --- | --- | --- |
| Totals | 1645397.3 | 360809.2 | 1284588.1 | 443238.88 | 788617.07 |
| Argentina | 206332.92 | 0 | 206332.92 | 206332.92 | 140037.89 |
| Austria | 236905.96 | 0 | 236905.96 | 236905.96 | 182739.87 |
| Belgium | 360809.2 | 360809.2 | 0 | 0 | 178042.33 |
| Brazil | 176596.89 | 0 | 176596.89 | 0 | 2104.22 |
| Canada | 142089.58 | 0 | 142089.58 | 0 | 40288.25 |
| Denmark | 152211.66 | 0 | 152211.66 | 0 | 106938.41 |
| Finland | 138148.99 | 0 | 138148.99 | 0 | 30583.44 |
| France | 146341.24 | 0 | 146341.24 | 0 | 30696.98 |
| Germany | 85960.86 | 0 | 85960.86 | 0 | 77185.68 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Sales)

    Sum Sales with no set expression.
  - Sum({1<Country={Belgium}>}Sales)

    Select Belgium, and then sum corresponding Sales.
  - Sum({1<Country={"\*A\*"}>}Sales)

    Select all countries that have an A, and then sum corresponding Sales.
  - Sum({1<Country={"A\*"}>}Sales)

    Select all countries that begin with an A, and then sum corresponding Sales.
  - Sum({1<Year={$(=Max(Year))}>}Sales)

    Calculate the Max(Year), which is 2015, and then sum corresponding Sales.

Set modifiers based on element sets

![Set modifiers based on element sets.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_set_modifiers_element_sets.png "Click to view full size")

## Listed values

The most common example of an element set is one that is based on a list of field values enclosed in curly brackets. For example:

- {$<Country = {Canada, Germany, Singapore}>}
- {$<Year = {2015, 2016}>}

The inner curly brackets define the element set. The individual values are separated by commas.

## Quotes and case sensitivity

If the values contain blanks or special characters, the values need to be quoted. Single quotes will be a literal, case-sensitive match with a single field value. Double quotes imply a case-insensitive match with one or several field values. For example:

- <Country = {'New Zealand'}>

  Matches New Zealand only.
- <Country = {"New Zealand"}>

  Matches New Zealand, NEW ZEALAND, and new zealand.

Dates must be enclosed in quotes and use the date format of the field in question. For example:

- <ISO\_Date = {'2021-12-31'}>
- <US\_Date = {'12/31/2021'}>
- <UK\_Date = {'31/12/2021'}>

Double quotes can be substituted by square brackets or by grave accents.

## Searches

Element sets can also be created through searches. For example:

- <Country = {"C\*"}>
- <Ingredient = {"\*garlic\*"}>
- <Year = {">2015"}>
- <Date = {">12/31/2015"}>

Wildcards can be used in text searches: An asterisk (\*) represents any number of characters, and a question mark (?) represents a single character. Relational operators can be used to define numeric searches.

You should always use double quotes for searches. Searches are case-insensitive.

For more information, see [*Set modifiers with searches*](set-modifiers-advanced-searches.htm).

## Dollar expansions

Dollar expansions are needed if you want to use a calculation inside your element set. For example, if you want to look at the last possible year only, you can use:

<Year = {$(=Max(Year))}>

For more information, see [*Set modifiers with dollar-sign expansions*](set-modifiers-dollar-sign-expansions.htm).

## Selected values in other fields

Modifiers can be based on the selected values of another field. For example:

<OrderDate = DeliveryDate>

This modifier will take the selected values from DeliveryDate and apply those as a selection on OrderDate. If there are many distinct values – more than a couple of hundred – then this operation is CPU intensive and should be avoided.

## Element set functions

The element set can also be based on the set functions P() (possible values) and E() (excluded values).

For example, if you want to select countries where the product Cap has been sold, you can use:

<Country = P({1<Product={Cap}>} Country)>

Similarly, if you want to pick out the countries where the product Cap has not been sold, you can use:

<Country = E({1<Product={Cap}>} Country)>

For more information, see [*Set modifiers using set functions*](set-modifiers-implicit-field-value-definitions.htm) .

## Learn more

- [*Set analysis*](set-analysis-expressions.htm)
- [*Set identifiers*](set-identifiers.htm)
- [*Set operators*](set-operators.htm)
