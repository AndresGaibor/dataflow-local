---
title: "Set operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-operators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Set operators

Set operators are used to include, exclude, or intersect data sets. All operators use sets as operands and return a set as result.

You can use set operators in two different situations:

- To perform a set operation on set identifiers, representing sets of records in data.
- To perform a set operation on the element sets, on the [field](#glossary-0 "Glossary term") values, or inside a set modifier.

The following table shows the operators that can be used in set expressions.

Operators

| Operator | Description |
| --- | --- |
| + | Union. This binary operation returns a set consisting of the records or elements that belong to any of the two set operands. |
| - | Exclusion. This binary operation returns a set consisting of the records or elements that belong to the first but not the other of the two set operands. Also, when used as a unary operator, it returns the complement set. |
| \* | Intersection. This binary operation returns a set consisting of the records or elements that belong to both set operands. |
| / | Symmetric difference (XOR). This binary operation returns a set consisting of the records or elements that belong to either, but not both set operands. |

The following table shows examples with operators.

Examples with operators

| Example | Result |
| --- | --- |
| Sum ({1-$} Sales) | Returns sales for everything excluded by current selection. |
| Sum ({$\*BM01} Sales) | Returns sales for the intersection between the selection and [bookmark](#glossary-1 "Glossary term") #160;BM01. |
| Sum ({-($+BM01)} Sales) | Returns sales excluded by the selection and bookmark BM01. |
| Sum ({$<Year={2009}>+1<Country={'Sweden'}>} Sales) | Returns sales for the year 2009 associated with the current [selections](#glossary-2 "Glossary term") and add the full set of data associated with the country Sweden across all years. |
| Sum ({$<Country={"S\*"}+{"\*land"}>} Sales) | Returns the sales for countries that begin with S or end with land. |

See also:

- [*Set analysis*](set-analysis-expressions.htm)
- [*Set identifiers*](set-identifiers.htm)
- [*Set modifiers*](set-modifiers.htm)
