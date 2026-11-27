---
title: "Set modifiers with searches"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers-advanced-searches.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis", "Set modifiers"]
---

# Set modifiers with searches

You can create element sets through searches with set modifiers.

For example:

- <Country = {"C\*"}>
- <Year = {">2015"}>
- <Ingredient = {"\*garlic\*"}>

Searches should always be enclosed in double quotes, square brackets or grave accents. You can use a list with a mixture of literal strings (single quotes) and searches (double quotes). For example:

<Product = {'Nut', "\*Bolt", Washer}>

## Text searches

Wildcards and other symbols can be used in text searches:

- An asterisk (\*) will represent any number of characters.
- A question mark (?) will represent a single character.
- A circumflex accent (^) will mark the beginning of a word.

For example:

- <Country = {"C\*", "\*land"}>

  Match all countries beginning with a C or ending with land.
- <Country = {"\*^z\*"}>

  This will match all countries that have a word beginning with z, such as New Zealand.

## Numeric searches

You can make numeric searches using these relational operators: >, >=, <, <=

A numeric search always begins with one of these operators. For example:

- <Year = {">2015"}>

  Match 2016 and subsequent years.
- <Date = {">=1/1/2015<1/1/2016"}>

  Match all dates during 2015. Note the syntax for describing a time range between two dates. The date format needs to match the date format of the [field](#glossary-0 "Glossary term") in question.

## Expression searches

You can use expression searches to make more advanced searches. An [aggregation](#glossary-1 "Glossary term") is then evaluated for each field value in the search field. All values for which the search expression returns true are selected.

An expression search always begins with an equals sign: =

For example:

<Customer = {"=Sum(Sales)>1000"}>

This will return all customers with a sales value greater than 1000. Sum(Sales) is calculated on the current selection. This means that if you have a selection in another field, such as the Product field, you will get the customers that fulfilled the sales condition for the selected products only.

If you want the condition to be independent of the selection, you need to use [set analysis](#glossary-2 "Glossary term") inside the search string. For example:

<Customer = {"=Sum({1} Sales)>1000"}>

The expressions after the equals sign will be interpreted as a boolean value. This means that if it evaluates to something else, any non-zero number will be interpreted as true, while zero and strings are interpreted as false.

## Quotes

Use quotation marks when the search strings contain blanks or special characters. Single quotes imply a literal, case-sensitive match with a single field value. Double quotes imply a case insensitive search that potentially matches multiple field values.

For example:

- <Country = {'New Zealand'}>

  Match New Zealand only.
- <Country = {"New Zealand"}>

  Match New Zealand, NEW ZEALAND, and new zealand

Double quotes can be substituted by square brackets or by grave accents.

For more information, see [*Searching within selections or visualizations*](../../Selections/SelectionsToolbar/search-selections.htm).

Information noteIn previous versions of Qlik Sense, there was no distinction between single quotes and double quotes, and all quoted strings were treated as searches. To maintain backward compatibility, apps created with older versions of Qlik Sense will continue to work as they did in previous versions. Apps created with Qlik Sense November 2017 or later will respect the difference between the two types of quotes.

## Examples: Chart expressions for set modifiers with searches

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

Example 1: Chart expressions with text searches

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers with text searches

| Country | Sum (Amount) | Sum({<Country={"C\*"}>} Amount) | Sum({<Country={"\*^R\*"}>} Amount) | Sum({<Product={"\*bolt\*"}>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 24 | 10 | 26 |
| Canada | 14 | 14 | 0 | 8 |
| Czech Republic | 10 | 10 | 10 | 4 |
| France | 4 | 0 | 0 | 1 |
| Germany | 13 | 0 | 0 | 13 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<Country={"C\*"}>}Amount)

    Sum Amount for all countries that start with C, such as Canada and Czech Republic.
  - Sum({<Country={"\*^R\*"}>}Amount)

    Sum Amount for all countries that have a word that starts with R, such as Czech Republic.
  - Sum({<Product={"\*bolt\*"}>}Amount)

    Sum Amount for all products that contain the string bolt, such as Bolt and Anchor bolt.

Set modifiers with text searches

![Chart expressions with text searches.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_text_search.png "Click to view full size")

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

Example 2: Chart expressions with numeric searches

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers with numeric searches

| Country | Sum (Amount) | Sum({<Year={">2019"}>} Amount) | Sum({<ISO\_Date={">=2019-07-01"}>} Amount) | Sum({<US\_Date={">=4/1/2018<=12/31/2018"}>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 10 | 16 | 16 |
| Canada | 14 | 8 | 8 | 0 |
| Czech Republic | 10 | 0 | 6 | 1 |
| France | 4 | 2 | 2 | 2 |
| Germany | 13 | 0 | 0 | 13 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<Year={">2019"}>}Amount)

    Sum Amount for all years after 2019.
  - Sum({<ISO\_Date={">=2019-07-01"}>}Amount)

    Sum Amount for all dates on or after 2019-07-01. The format of the date in the search must match the format of the field.
  - Sum({<US\_Date={">=4/1/2018<=12/31/2018"}>}Amount)

    Sum Amount for all dates from 4/1/2018 to 12/31/2018, including the start and end dates. The format of the dates in the search must match the format of the field.

Set modifiers with numeric searches

![Chart expressions with numeric searches.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_numeric_search.png "Click to view full size")

Example 3: Chart expressions with expression searches

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers with expression searches

| Country | Sum (Amount) | Sum({<Country={"=Sum(Amount)>10"}>} Amount) | Sum({<Country={"=Count(distinct Product)=1"}>} Amount) | Sum({<Product={"=Count(Amount)>3"}>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 27 | 13 | 22 |
| Canada | 14 | 14 | 0 | 8 |
| Czech Republic | 10 | 0 | 0 | 0 |
| France | 4 | 0 | 0 | 1 |
| Germany | 13 | 13 | 13 | 13 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<Country={"=Sum(Amount)>10"}>}Amount)

    Sum Amount for all countries that have an aggregated sum of Amount greater than 10.
  - Sum({<Country={"=Count(distinct Product)=1"}>}Amount)

    Sum Amount for all countries that are associated with exactly one distinct product.
  - Sum({<Product={"=Count(Amount)>3"}>}Amount)

    Sum Amount for all countries that have more than three transactions in the data.

Set modifiers with expression searches

![Chart expressions with expression searches.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_expression_search.png "Click to view full size")

| Examples | Results |
| --- | --- |
| sum( {$–1<Product = {“\*Internal\*”, “\*Domestic\*”}>} Sales ) | Returns the sales for current selection, excluding transactions pertaining to products with the string 'Internal' or 'Domestic' in the product name. |
| sum( {$<Customer = {“=Sum({1<Year = {2007}>} Sales ) > 1000000”}>} Sales ) | Returns the sales for current selection, but with a new selection in the 'Customer' field: only customers who during 2007 had a total sales of more than 1000000. |
