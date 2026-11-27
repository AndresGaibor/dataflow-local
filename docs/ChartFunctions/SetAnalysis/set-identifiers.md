---
title: "Set identifiers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-identifiers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Set identifiers

A set identifier represents a set of records in the data; either all the data or a subset of the data. It is the set of records defined by a selection. It could be the current selection, all data (no selection), a selection from a bookmark, or a selection from an alternate state.

In the example Sum( {$<Year = {2009}>} Sales ), the identifier is the dollar sign: $. This represents the current selection. It also represents all the possible records. This set can then altered by the modifier part of the set expression: the selection 2009 in Year is added.

The $ set identifier is the same as not stating a set identifier. For instance, with the example above, the expression Sum( {$<Year = {2009}>} Sales ) is equivalent to Sum( {<Year = {2009}>} Sales ).

In a more complex set expression, two identifiers can be used together with an operator to form a union, a difference, or an intersection of the two record sets.

The following table shows some common identifiers.

Examples with common identifiers

| Identifier | Description |
| --- | --- |
| 1 | Represents the full set of all the records in the application, irrespective of any [selections](#glossary-0 "Glossary term") made. |
| $ (or no set identifier) | Represents the records of the current selection in the default state. The set expression {$} is thus usually the equivalent to not stating a set expression. |
| $1 | Represents the previous selection in the default state. $2 represents the previous selection-but-one, and so on. |
| $\_1 | Represents the next (forward) selection. $\_2 represents the next selection-but-one, and so on. |
| BM01 | You can use any [bookmark](#glossary-1 "Glossary term") ID or bookmark name. |
| AltState | You can reference an alternate state by its state name. |
| AltState::BM01 | A bookmark contains the selections of all states, and you can reference a specific bookmark by qualifying the bookmark name. |

The following table shows examples with different identifiers.

Examples with different identifiers

| Example | Result |
| --- | --- |
| Sum ({1} Sales) | Returns total sales for the app disregarding selections but not the [dimension](#glossary-3 "Glossary term"). |
| Sum ({$} Sales) | Returns the sales for the current selection, that is, the same as Sum(Sales). |
| Sum ({$1} Sales) | Returns the sales for the previous selection. |
| Sum ({BM01} Sales) | Returns the sales for the bookmark named BM01. |

See also:

- [*Set analysis*](set-analysis-expressions.htm)
- [*Set operators*](set-operators.htm)
- [*Set modifiers*](set-modifiers.htm)
