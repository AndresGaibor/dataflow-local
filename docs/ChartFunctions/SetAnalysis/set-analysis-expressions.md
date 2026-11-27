---
title: "Set analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-analysis-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions"]
---

# Set analysis

When you make a selection in an app, you define a subset of records in the data. Aggregation functions, such as Sum(), Max(), Min(), Avg(), and Count() are calculated based on this subset.

In other words, your selection defines the scope of the [aggregation](#glossary-1 "Glossary term"), it defines the set of records on which calculations are made.

Set analysis offers a way of defining a scope that is different from the set of records defined by the current selection. This new scope can also be regarded as an alternative selection.

This can be useful if you want to compare the current selection with a particular value, for example last year’s value or the global market share.

## Set expressions

Set expressions can be used inside and outside aggregation functions, and are enclosed in curly brackets.

Example: Inner set expression

```
Sum( {$<Year={2021}>} Sales )
```

Example: Outer set expression

```
{<Year={2021}>} Sum(Sales) / Count(distinct Customer)
```

For more information about inner and outer set expressions, see [*Inner and outer set expressions*](set-expressions-inner-and-outer.htm).

A set expression consists of a combination of the following elements:

- Identifiers. A set identifier represents a selection, defined elsewhere. It also represents a specific set of records in the data. It could be the current selection, a selection from a bookmark, or a selection from an alternate state. A simple set expression consists of a single identifier, such as the dollar sign, {$}, which means all records in the current selection.

  Examples: $, 1, BookMark1, State2

  See: [*Set identifiers*](set-identifiers.htm)
- Operators. A set operator can be used to create unions, differences or intersections between different set identifiers. This way, you can create a subset or a superset of the selections defined by the set identifiers.

  Examples: +, -, \*, /

  See: [*Set operators*](set-operators.htm)
- Modifiers. A set modifier can be added to the set identifier to change its selection. A modifier can also be used on its own and will then modify the default identifier. A modifier must be enclosed in angle brackets <…>.

  Examples: <Year={2020}>, <Supplier={ACME}>

  See: [*Set modifiers*](set-modifiers.htm)
- Empty set preserve flag. An advanced element that can be used in any outer set expression—except the last—in a chain of outer set expressions. This flag overrides implicit set clearing on any sets defined in these outer set expression, simplifying configuration of advanced expressions.

  Syntax: &

  See: [*Empty set preserve flag*](empty-set-preserve-flag.htm)

The elements are combined to form set expressions.

Elements in a set expression

![Elements in a set expression.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_callout.png "Click to view full size")

The set expression above, for example, is built from the aggregation Sum(Sales).

The first operand returns sales for the year 2021 for the current selection, which is indicated by the $ set identifier and the modifier containing the selection of year 2021. The second operand returns Sales for Sweden, and ignores the current selection, which is indicated by the 1 set identifier.

Finally, the expression returns a set consisting of the records that belongs to any of the two set operands, as indicated by the + set operator.

For a full syntax description, see [*Syntax for set expressions*](syntax-for-sets.htm).

## Examples

Examples that combine the set expression elements above are available in the following topics:

- [*Set modifiers with searches*](set-modifiers-advanced-searches.htm)
- [*Set modifiers with dollar-sign expansions*](set-modifiers-dollar-sign-expansions.htm)
- [*Set modifiers with set operators*](set-modifiers-set-operators.htm)
- [*Set modifiers with implicit set operators*](set-modifiers-using-assignments-implicit-set-operators.htm)
- [*Set modifiers using set functions*](set-modifiers-implicit-field-value-definitions.htm)

To try out some other expressions, see [*Tutorial - Creating a set expression*](set-analysis-tutorial.htm).

## Natural sets

Usually, a set expression represents both a set of records in the data model, and a selection that defines this subset of data. In this case, the set is called a natural set.

Set identifiers, with or without set modifiers, always represent natural sets.

However, a set expression using set operators also represents a subset of the records, but can generally still not be described using a selection of [field](#glossary-2 "Glossary term") values. Such an expression is a non-natural set.

For example, the set given by {1-$} cannot always be defined by a selection. It is therefore not a natural set. This can be shown by loading the following data, adding it to a table, and then making selections using filter panes.

```
Load * Inline
[Dim1, Dim2, Number
A, X, 1
A, Y, 1
B, X, 1
B, Y, 1];
```

By making selections for Dim1 and Dim2, you get the view shown in the following table.

Table with natural and non-natural sets

![Table with natural and non-natural sets.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_natural.png "Click to view full size")

The set expression in the first [measure](#glossary-3 "Glossary term") uses a natural set: it corresponds to the selection that is made {$}.

The second measure is different. It uses {1-$}. It is not possible to make a selection that corresponds to this set, so it is a non-natural set.

This distinction has a number of consequences:

- Set modifiers can only be applied to set identifiers. They cannot be applied to an arbitrary set expression. For example, it is not possible to use a set expression such as:

  ```
  { (BM01 * BM02) <Field={x,y}> }
  ```

  Here, the normal (round) brackets imply that the intersection between BM01 and BM02 should be evaluated before the set modifier is applied. The reason is that there is no element set that can be modified.
- You cannot use non-natural sets inside the P() and E() element functions. These functions return an element set, but it is not possible to deduce the element set from a non-natural set.
- A measure using a non-natural set cannot always be attributed to the right dimensional value if the data model has many tables. For example, in the following [chart](#glossary-4 "Glossary term"), some excluded sales numbers are attributed to the correct Country, whereas others have NULL as Country.

  Chart with non-natural set

  ![Table with non-natural set.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_non_natural.png "Click to view full size")

  Whether or not the assignment is made correctly depends on the data model. In this case, the number cannot be assigned if it pertains to a country that is excluded by the selection.

| Identifier | Description |
| --- | --- |
| 1 | Represents the full set of all the records in the application, irrespective of any selections made. |
| $ | Represents the records of the current selection. The set expression {$} is thus the equivalent to not stating a set expression. |
| $1 | Represents the previous selection. $2 represents the previous selection-but-one, and so on. |
| $\_1 | Represents the next (forward) selection. $\_2 represents the next selection-but-one, and so on. |
| BM01 | You can use any [bookmark](#glossary-5 "Glossary term") ID or bookmark name. |
| MyAltState | You can reference the selections made in an alternate state by its state name. |

| Example | Result |
| --- | --- |
| sum ({1} Sales) | Returns total sales for the app, disregarding selections but not the [dimension](#glossary-6 "Glossary term"). |
| sum ({$} Sales) | Returns the sales for the current selection, that is, the same as sum(Sales). |
| sum ({$1} Sales) | Returns the sales for the previous selection. |
| sum ({BM01} Sales) | Returns the sales for the bookmark named BM01. |

| Example | Result |
| --- | --- |
| sum({$<OrderDate = DeliveryDate>} Sales) | Returns the sales for the current selection where OrderDate = DeliveryDate. |
| sum({1<Region = {US}>} Sales) | Returns the sales for region US, disregarding the current selection. |
| sum({$<Region = >} Sales) | Returns the sales for the selection, but with the selection in Region removed. |
| sum({<Region = >} Sales) | Returns the same as the example above. When the set to modify is omitted, $ is assumed. |
| sum({$<Year={2000}, Region={“U\*”}>} Sales) | Returns the sales for the current selection, but with new selections both in Year and in Region. |

Related learning:

- [How do I configure set expressions using my current selection state?](/lnk/How_configure_set_expression_using_selection_state)
