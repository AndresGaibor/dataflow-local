---
title: "Using functions in charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/use-functions-in-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations"]
---

# Using functions in charts

A function is a type of procedure or routine that performs a specific task on data in applications. Qlik Sense contains several hundred ready-made functions that can be used in [charts](#glossary-0 "Glossary term") when creating [visualizations](#glossary-1 "Glossary term"). Functions can be, for example, mathematical, logical, can operate on financial or date and time information, can be used to manipulate strings, and other situations.

Functions can be grouped into the types:

- Aggregation functions, which use several records as input and produce a single value result.
- Scalar functions, which take a single input and produce a single output.
- Range functions, which produce a single value based on a range of input values.
- Range-producing functions, which are like range functions, but produce a range of values as output.

Many of the functions can be used in both chart expressions and scripts, but some are specific for chart expressions.

The following list shows some examples of functions:

- Max: an [aggregation](#glossary-2 "Glossary term") function that can be used in scripts and charts.

  For example: Max(Sales) calculates the highest value in the [field](#glossary-3 "Glossary term") Sales.
- IF: a conditional function that can be used in scripts and charts.

  For example:  IF(Amount>0, 'OK','Alarm') determines if the condition 'is the value of Amount greater than zero?' is met. If it is, OK is written, otherwise Alarm is written.
- Date#: an interpretation function that can be used in scripts and charts.

  For example:  Date#(A) takes the input value A and evaluates it as a date.

Information noteA few differences exist between script expressions and chart expressions in terms of syntax and available functions. The most important difference is the role of the aggregation functions and the use of field references. The basic rule is that any field name in a chart expression must be enclosed by exactly one aggregation function. An aggregation function can never have another expression containing an aggregation function as argument.

## Learn more

- [*Script and chart functions*](../Scripting/functions-in-scripts-chart-expressions.htm)
- [*Using expressions in visualizations*](use-expressions-in-visualizations.htm)
- [*Expression editor*](../Expressions/expression-editor.htm)
