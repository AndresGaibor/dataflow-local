---
title: "Set modifiers with dollar-sign expansions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-modifiers-dollar-sign-expansions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis", "Set modifiers"]
---

# Set modifiers with dollar-sign expansions

Dollar-sign expansions are constructs that are calculated before the expression is parsed and evaluated. The result is then injected into the expression instead of the $(…). The calculation of the expression is then made using the result of the dollar expansion.

The expression editor shows a dollar expansion preview so that you can verify what your dollar-sign expansion evaluates to.

Dollar-sign expansion preview in expression editor

![Dollar-sign expansion preview in expression editor.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_dollar_expansion_preview.png "Click to view full size")

Use dollar-sign expansions when you want to use a calculation inside your element set.

For example, if you want to look at the last possible year only, you can use the following construction:

<Year = {$(=Max(Year))}>

Max(Year) is calculated first, and the result would be injected in the expression instead of the $(…).

The result after the dollar expansion will be an expression such as the following:

<Year = {2021}>

The expression inside the dollar expansion is calculated based on the current selection. This means that if you have a selection in another [field](#glossary-0 "Glossary term"), the result of the expression will be affected.

If you want the calculation to be independent of the selection, use [set analysis](#glossary-1 "Glossary term") inside the dollar expansion. For example:

<Year = {$(=Max({1} Year))}>

## Strings

When you want the dollar expansion to result in a string, normal quoting rules apply. For example:

<Country = {'$(=FirstSortedValue(Country,Date)'}>

The result after the dollar expansion will be an expression such as the following:

<Country = {'New Zealand'}>

You will get a syntax error if you do not use the quotation marks.

## Numbers

When you want the dollar expansion to result in a number, ensure that the expansion gets the same formatting as the field. This means that you sometimes need to wrap the expression in a formatting function.

For example:

<Amount = {$(=Num(Max(Amount), '###0.00'))}>

The result after the dollar expansion will be an expression such as the following:

<Amount = {12362.00}>

Use a hash to force the expansion to always use decimal point and no thousand separator . For example:

<Amount = {$(#=Max(Amount))}>

## Dates

When you want the dollar expansion to result in a date, ensure that the expansion has the correct formatting. This means that you sometimes need to wrap the expression in a formatting function.

For example:

<Date = {'$(=Date(Max(Date)))'}>

The result after the dollar expansion will be an expression such as the following:

<Date = {'12/31/2015'}>

Just as with strings, you need to use the correct quotes.

A common use case is that you want your calculation to be limited to the last month (or year). Then you can use a numeric search in combination with the AddMonths() function.

For example:

<Date = {">=$(=AddMonths(Today(),-1))"}>

The result after the dollar expansion will be an expression such as the following:

<Date = {">=9/31/2021"}>

This will pick out all events that have occurred the last month.

## Example: Chart expressions for set modifiers with dollar-sign expansions

Example - chart expressions

Load script

Load the following data as an inline load in the data load editor to create the chart expression examples below.

```
Let vToday = Today();
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
2021-10-15, France, Washer, 1];
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

Chart expressions with dollar-sign expansions

Create a table in a Qlik Sense sheet with the following chart expressions.

Table - Set modifiers with dollar-sign expansions

| Country | Sum (Amount) | Sum({<US\_Date={'$(vToday)'}>} Amount) | Sum({<ISO\_Date={"$(=Date(Min(ISO\_Date),'YYYY-MM-DD'))"}>} Amount) | Sum({<US\_Date={">=$(=AddYears(Max(US\_Date),-1))"}>} Amount) |
| --- | --- | --- | --- | --- |
| Totals | 41 | 1 | 6 | 1 |
| Canada | 14 | 0 | 6 | 0 |
| Czech Republic | 10 | 0 | 0 | 0 |
| France | 4 | 1 | 0 | 1 |
| Germany | 13 | 0 | 0 | 0 |

Explanation

- Dimensions:

  - Country
- Measures:

  - Sum(Amount)

    Sum Amount with no set expression.
  - Sum({<US\_Date={'$(vToday)'}>}Amount)

    Sum Amount for all records where the US\_Date is the same as in the [variable](#glossary-2 "Glossary term")vToday.
  - Sum({<ISO\_Date={"$(=Date(Min(ISO\_Date),'YYYY-MM-DD'))"}>}Amount)

    Sum Amount for all records where the ISO\_Date is the same as the first (smallest) possible ISO\_Date. The Date() function is needed to ensure that the format of the date matches that of the field.
  - Sum({<US\_Date={">=$(=AddYears(Max(US\_Date),-1))"}>}Amount)

    Sum Amount for all records that have a US\_Date after or on the date a year before the latest (largest) possible US\_Date. The AddYears() function will return a date in the format specified by the variable DateFormat, and this needs to match the format of the field US\_Date.

Set modifiers with dollar-sign expansions

![Set modifiers with dollar-sign expansions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_dollar_expansion.png "Click to view full size")

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

| Examples | Results |
| --- | --- |
| sum( {$<Year = {$(#vLastYear)}>} Sales ) | Returns the sales for the previous year in relation to current selection. Here, a variable vLastYear containing the relevant year is used in a dollar-sign expansion. |
| sum( {$<Year = {$(#=Only(Year)-1)}>} Sales ) | Returns the sales for the previous year in relation to current selection. Here, a dollar-sign expansion is used to calculate previous year. |
