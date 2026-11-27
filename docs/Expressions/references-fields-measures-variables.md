---
title: "References to fields, measures, and variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/references-fields-measures-variables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations"]
---

# References to fields, measures, and variables

An expression can contain references to fields, [variables](#glossary-0 "Glossary term"), and [measures](#glossary-1 "Glossary term").

In most cases, expressions are aggregations, that is calculations that potentially can span multiple records. This means that all [field](#glossary-2 "Glossary term") references in an expression must be wrapped in an [aggregation](#glossary-3 "Glossary term") function. If no aggregation function is used, the Only() function is used.

When the name of a measure is used inside an expression, it is interpreted as an alias for the measure. This allows you to re-use an already defined entity. You can use the labels of master measures and [chart](#glossary-4 "Glossary term") measures in this way. However, the chart measure must be in the same chart. You cannot use labels of measures in other charts.

You can define a measure recursively. In other words, the measure can contain a reference to itself. However, you should only do this in charts with few rows. Performance degrades if the chart has many rows. If there are hundreds of rows, the recursive definition will stop working altogether.

A variable can be used in two different ways: in a direct reference or in a dollar-sign expansion. If you use a direct reference, the variable value will be used in the calculation. If you use a dollar-sign expansion, the entire dollar-sign expansion will be replaced by the variable value before the expression is parsed. Therefore, the two different methods may return different results.

## How names are interpreted

A name inside an expression can be a reference to a field, a variable, a function, or a measure. Depending on situation, the name is interpreted differently.

Example:

The string XXX represents a field, a variable, a function, or a measure. XXX will be interpreted as one of these depending on how you create the expression.

Examples of how names are interpreted

| Expression | XXX interpreted as |
| --- | --- |
| XXX | measure, variable, or field |
| $(XXX) | variable |
| Count(XXX) | field or variable |
| XXX() | function |

You should not use the same name for a field and a variable (or a measure). But if you do and there is ambiguity, the following order of precedence is used:

- If the name is found inside an aggregation function, a field has precedence over a variable.
- If the name is found outside an aggregation function, a measure label has precedence over a variable name, which in turn has precedence over a field name.

## Rules for expressions

The following rules apply for chart expressions:

- If a field reference isn’t wrapped in an aggregation function, the Only() function is used by the engine.
- All expressions return a number and/or a string, whichever is appropriate.
- Logical functions and operators return 0 for False,
  -1 for True. Number-to-string conversions and string-to-number conversions are implicit.
- Logical operators and functions interpret 0 as False
  and all else as True.
- Expressions that cannot be correctly evaluated, for example as a result of incorrect parameters or functions, return NULL.

## Learn more

- [*Script expressions*](../Scripting/script-expressions.htm)
- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
