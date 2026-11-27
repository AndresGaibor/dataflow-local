---
title: "Empty set preserve flag"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/empty-set-preserve-flag.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Empty set preserve flag

You can use the & symbol (the empty set preserve flag) at the beginning of some outer set expressions to override [implicit selection set clearing](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/empty-set-preserve-flag.htm#Implicit) during user analysis. The empty set preserve flag allows you to change how aggregations are calculated and represented when users make selections, without requiring you to rewrite long, advanced set expressions.

For example, in the following set expression, the empty set preserve flag is used:

```
{&<Country*={'Sweden', 'Denmark'}>} {<ProductCategory={'shirts'}>} Sum( Sales )
```

## Background

### Conditions for use

The empty set preserve flag can be used in set expressions that have either of the following components:

- At least one inner and one outer set expression
- Two or more outer set expressions

Use the empty set preserve flag when you want to avoid [*Implicit selection set clearing*](#Implicit).

### Implicit selection set clearing

Implicit selection set clearing is an internal behavior that can sometimes be undesirable for end user analysis when complex chains of set expressions are used. Implicit selection set clearing can occur for set expressions that are structured as per the [*Conditions for use*](#Requirements).

The undesirable behavior is as follows:

1. One or more outer set expressions in the chain—specifically, the first (or only) and any subsequent outer set expressions except the last —define data sets. For example: Country\*={'Sweden', 'Denmark'}>}
2. Something happens to produce an empty set for one or more of these outer set expression components. Most commonly, a conflicting selection is made in the app.
3. For the empty sets, the sets defined by these expressions are cleared as the expression is evaluated. This means that the data used in the aggregations is no longer reduced to the defined sets, but instead all data is used.

   On the other hand, the sets defined in any outer set expressions producing non-empty sets, as well as the last outer set expression in the chain, are respected during evaluation.

This behavior results in aggregation values that may be unexpected and can lead to inconsistent analysis. To bypass implicit selection set clearing, you can use the empty set preserve flag. See [*The solution: Using the empty set preserve flag*](#Solution).

### The solution: Using the empty set preserve flag

Use the & symbol (the empty set preserve flag) to override implicit selection set clearing. This flag ensures that sets defined in all outer set expressions, except the last, in a chain will not be cleared, and instead will be respected throughout the evaluation of the entire expression.

The empty set preserve flag provides:

- Flexibility and time-saving when you have advanced, long set expressions that you would like to keep intact, rather than rewriting.
- An ability to change aggregation logic to suit advanced use cases.

## Syntax

In an outer set expression, the empty set preserve flag is placed as a single & character at the beginning of the expression—that is, before the set modifiers, identifiers, and operators.

Examples:

Examples — empty set preserve flag

| Expression | Expression without empty set preserve flag |
| --- | --- |
| {&<Country\*={'Sweden', 'Denmark'}>} {<ProductCategory={'shirts'}>} Sum( Sales ) | {<Country={'Sweden'}>} {<ProductCategory={'shirts'}>} Sum (Sales) |
| {& <Year=, Product={XI345}>} {<Region={Europe}>} Sum (Sales) | {<Year=, Product={XI345}>} {<Region={Europe}>} Sum (Sales) |

## Details and examples

For more in-depth information, see [*Chains of multiple outer and inner set expressions*](set-expressions-inner-and-outer.htm#Chains).

## Learn more

- [*Set analysis*](set-analysis-expressions.htm)
- [*Inner and outer set expressions*](set-expressions-inner-and-outer.htm)
