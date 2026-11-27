---
title: "Using expressions in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/tutorial-expressions-in-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Tutorial - Chart expressions"]
---

# Using expressions in visualizations

[Visualizations](#glossary-0 "Glossary term") in Qlik Sense are built from [charts](#glossary-1 "Glossary term"), which are built from [dimensions](#glossary-2 "Glossary term") and [measures](#glossary-3 "Glossary term"). You can make your visualizations more dynamic and complex with expressions.

Visualizations can have titles, subtitles, footnotes, and other elements to help convey information. The elements that make up a visualization can be simple. For example: a dimension consisting of a [field](#glossary-4 "Glossary term")representing data, and a title consisting of text.

Measures are calculations based on fields. For example: Sum(Cost) means that all the values of the field Cost are aggregated using the function Sum. In other words, Sum(Cost) is an expression.

## What is an expression?

An expression is a combination of functions, fields, and mathematical operators (+ \* / =). Expressions are used to process data in an application in order to produce a result that can be seen in a visualization. They can be simple, involving only basic calculations, or complex, involving functions fields and operators. Expressions are used both in scripts and in [chart](#glossary-6 "Glossary term") visualizations.

All measures are expressions. The difference between measures and expressions is that expressions have no name or descriptive data.

You can build visualizations that are more dynamic and powerful by using expressions for dimensions, titles, subtitles, and footnotes. This means, for example, that instead of a static text, the title of a visualization can be generated from an expression whose result changes depending on your [selections](#glossary-7 "Glossary term").

## Where can I use expressions?

When you are editing a visualization, if an ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol can be seen in the properties panel, you can use an expression. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor, which is designed to help you build and edit expressions. Expressions can also be entered directly into the expression field.

An expression cannot be saved directly as a [master item](#glossary-8 "Glossary term"). However, master measures and master dimensions can contain expressions. If an expression is used in a measure or dimension which is then saved as a master item, the expression in the measure or dimension is preserved.

## When are expressions evaluated?

In a [load script](#glossary-9 "Glossary term") an expression is evaluated as the script executes. In visualizations, expressions are evaluated automatically whenever any of the fields, [variables](#glossary-10 "Glossary term") or functions that the expression contains change value or logical status. A few differences exist between script expressions and chart expressions in terms of syntax and available functions.

## Learn more

- [*Script expressions*](../Scripting/script-expressions.htm)
