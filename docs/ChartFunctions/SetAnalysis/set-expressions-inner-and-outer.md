---
title: "Inner and outer set expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-expressions-inner-and-outer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Inner and outer set expressions

Set expressions can be used inside and outside aggregation functions, and are enclosed in curly brackets.

When you use a set expression inside an aggregation function, it can look like this:

Example: Inner set expression

```
Sum( {$<Year={2021}>} Sales )
```

Use a set expression outside the aggregation function if you have expressions with multiple aggregations and want to avoid writing the same set expression in every aggregation function.

If you use an outer set expression, it must be placed at the beginning of the scope.

Example: Outer set expression

```
{<Year={2021}>} Sum(Sales) / Count(distinct Customer)
```

If you use a set expression outside the aggregation function, you can also apply it on existing master measures.

Example: Outer set expression applied to master measure

```
{<Year={2021}>} [Master Measure]
```

A set expression used outside aggregation functions affects the entire expression, unless it is enclosed in brackets then the brackets define the scope. In the lexical scoping example below, the set expression is only applied to the aggregation inside the brackets.

Example: Lexical scoping

```
( {<Year={2021}>} Sum(Amount) / Count(distinct Customer) ) – Avg(CustomerSales)
```

## Rules

#### Lexical scope

The set expression affects the entire expression, unless it is enclosed in brackets. If so, the brackets define the lexical scope.

#### Position

The set expression must be placed in the beginning of the lexical scope.

#### Context

The context is the selection that is relevant for the expression. Traditionally, the context has always been the default state of current selection. But if an object is set to an alternate state, the context is the alternate state of the current selection.

You can also define a context in the form of an outer set expression.

#### Inheritance

Inner set expressions have precedence over outer set expressions. If the inner set expression contains a set identifier, it overrides the context defined in the outer set expression. Otherwise, the inner and outer set expressions are both evaluated.

Example 1: Inner set expression with set identifier

{<Year={2023}>} Sum(Sales) / Count({1} distinct OrderNumber)

In the above expression, the inner set expression Count({1} distinct OrderNumber) consists of the set identifier {1}. When this inner set expression is evaluated, the scope defined in the outer set expression {<Year={2023}>} is not applied.

Example 2: Inner set expressions without set identifiers

{<Year={2023}>} Sum ({<Status={'Confirmed'}>} Sales\_Stream1) + Sum ({<UpdatedStatus={'Confirmed'}>} Sales\_Stream2)

In the above expression, the inner set expressions Sum ({<Status={'Confirmed'}>} Sales\_Stream1) and Sum ({<UpdatedStatus={'Confirmed'}>} Sales\_Stream2) do not contain set identifiers. Therefore, the outer set expression {<Year={2023}>} and both inner set expressions are all applied when evaluating the result.

#### Element set assignment

The element set assignment determines how the two selections are merged. If a normal equals sign is used, the selection in the inner set expression has precedence. Otherwise, the implicit set operator will be used.

- {<Field={value}>} - this inner selection replaces any outer selection in “Field”.
- {<Field+={value}>} - this inner selection is merged with the outer selection in “Field”, using the union operator.
- {<Field\*={value}>} - this inner selection is merged with the outer selection in “Field”, using the intersection operator.

#### Inheritance in multiple steps

The inheritance can occur in multiple steps. Examples:

- Current Selection → Sum(Amount)

  The aggregation function will use the context, which here is the current selection.
- Current Selection → {<Set1>} Sum(Amount)

  Set1 will inherit from current selection, and the result will be the context for the aggregation function.
- Current Selection → {<Set1>} ({<Set2>} Sum(Amount))

  Set2 will inherit from Set1, which in turn inherits from current selection, and the result will be the context for the aggregation function.

#### Inheritance for chains of inner and outer set expressions

There are additional considerations for inheritance when using multiple set expressions in complex chains, particularly when an outer set expression is followed by other out set expressions and/or an inner set expression. For details, see [*Chains of multiple outer and inner set expressions*](#Chains).

#### The Aggr() function

The Aggr() function creates a nested aggregation that has two independent aggregations. In the example below, a Count() is calculated for each value of Dim, and the resulting array is aggregated using the Sum() function.

Example:

```
Sum(Aggr(Count(X),Dim))
```

Count() is the inner aggregation and Sum() is the outer aggregation.

- The inner aggregation does not inherit any context from the outer aggregation.
- The inner aggregation inherits the context from the Aggr() function, which may contain a set expression.
- Both the Aggr() function and the outer aggregation function inherit the context from an outer set expression.

## Chains of multiple outer and inner set expressions

Note that it is possible to have more than one outer set expression. In this example we have two outer set expressions and one inner:

{<Year={2021}>} {<Region={"Europe"}>} Sum( {$<Product={"XI345"}>} Sales )

The set expressions will be applied from left to right. This means that if two set expressions are using conflicting sets, the rightmost expression will have precedence.

Although there is no limit to the number of outer set expressions chained together in this manner, the number of inner set expressions is limited to one. Having more than one inner set expression next to each other will not produce any error, but only the rightmost of them will be used when evaluated.

### Set expression inheritance

When an aggregation expression contains more than one set expression as part of a chain, the set expressions will be evaluated one by one from left to right. The result of each set expression is a group of sets, potentially one for each dimension. The sets are passed to the next set expression, which can make further changes before being passed on to the next one.

As long as each set expression is operating on different dimensions, there will be no conflicts between them, and all sets will be preserved to the end of the chain (and applied during aggregation). There is one exception to this rule, which sometimes applies when a dimension in a set expression has produced an empty set. See the following for more information:

- [*Empty selection sets*](#Empty)
- [*Implicit selection set clearing*](#Implicit)

### Empty selection sets

When a dimension in a set expression is evaluated, it is possible for the set to contain no data. This is called an empty set. Empty sets can occur in many scenarios such as:

- Incorrect expression definition. For example, when trying to look for a value 2025 with a set expression {<OrderYear={‘2025’}>}, the expression is written as {<OrderYear={‘0025’}>}.
- During analysis, a selection is made in a different dimension than the one referenced in the expression and this selection results in no available data for the set expression dimension. For example, a user makes a selection for Region='Europe' and a set expression filters for {<ProductCategory={‘Shirts’}>} Sum (Sales). If no shirts are sold in Europe, the set expression contains an empty set.
- The empty set is defined explicitly in the expression. This is not common or useful, but is technically possible. For example: {<Year={}>}

### Implicit selection set clearing

If the result after applying a set expression is an empty set for any of the dimensions (see [*Empty selection sets*](#Empty)), and there is one more set expression being applied after this, then the selection set for that dimension will be cleared (restored back to the full set) just before that next set expression is applied. A cleared selection set means that all values are included. Note, however, that this clearing only happens if there are one or more additional outer set expressions being applied after the set expression where the empty set is being produced.

Here is an example of when a cleared selection set will happen:

```
{<Year={}>} {<Region={"Europe"}>} Sum( Sales )
```

Year={} will create the empty set for dimension Year. This means that the selection set for Year is cleared when the set is passed over to the next set expression, which contains Region={Europe}. Note that the selection clearing only happens for a single dimension. Sets in other dimensions—including sets within the same set expression— will still be passed on without modification.

Here is another example of a cleared selection set:

```
{<Year={}, Product={"XI345"}>} {<Region={"Europe"}>} Sum(Sales)
```

In the above example, the following happens:

- The selection sets Product={"XI345"} and Region={"Europe"} are applied.
- Year={} is not applied. This is because that set is cleared as the last set expression—{<Region={"Europe"}>}—is applied.

Moving a set expression component to the last outer set expression will prevent implicit clearing from happening. Take this example:

```
{<Product={"XI345"}>} {<Year={}, Region={"Europe"}>} Sum(Sales)
```

Here, we have moved the Year expression into the last set expression in the chain. This will prevent the implicit clearing from happening, and the empty set for Year dimension will actually be used for the Sum aggregation.

In any case, undesirable behavior can happen as selection sets are cleared. To improve the analysis experience and make it easier to write chains of set expressions, use the empty set preserve flag. For more information, see [*Empty set preserve flag (outer set expressions)*](#Flag).

## Empty set preserve flag (outer set expressions)

Use the & symbol (the empty set preserve flag) to simplify the evaluation model for outer set expressions. For example:

```
{& <Year={}, Product={XI345}>} {<Region={Europe}>} Sum( Sales )
```

In this example, Year={} defines an empty selection set for Year. Without the & symbol, the {<Region={Europe}>} expression would cause the Year empty selection set to be cleared, resulting in all data being used in the aggregation calculation. The & symbol forces the aggregation to respect the Year empty selection set, resulting in a more understandable output.

For full details about the empty set preserve flag, see [*Empty set preserve flag*](empty-set-preserve-flag.htm).

## Learn more

- [*Dollar-sign expansions*](../../Scripting/dollar-sign-expansions.htm)
- [*Creating a variable*](../../Variables/create-variable-using-dialog.htm)
- [*Variables dialog*](../../Sheets/variables-dialog.htm)
- [*Outer set expressions and dollar-sign expansions*](outer-set-expression-dollar-sign-expansion.htm)
