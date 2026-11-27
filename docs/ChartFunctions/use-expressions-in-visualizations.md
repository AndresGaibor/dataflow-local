---
title: "Using expressions in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/use-expressions-in-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Using expressions in visualizations

[Visualizations](#glossary-0 "Glossary term") in Qlik Sense are built from [charts](#glossary-1 "Glossary term"), which in turn, are built from [dimensions](#glossary-2 "Glossary term") and [measures](#glossary-3 "Glossary term"), depending on the type of [chart](#glossary-4 "Glossary term"). Visualizations can have titles, subtitles, footnotes, and other elements to help convey information. All of the elements that make up a visualization can be simple: a dimension consisting of a [field](#glossary-5 "Glossary term") representing data, a title consisting of text, for example.

For visualizations that contain measures, the measures are aggregations based on fields. Specifically, the measures are calculations that span multiple records. For example Sum(Cost) means all the values of the field Cost are aggregated using the function Sum. In other words, Sum(Cost) is an expression.

## What is an expression?

An expression is a combination of functions, fields, and mathematical operators (+ \* / =), and other measures. Expressions are used to process data in the application in order to produce a result that can be seen in a visualization. They are not limited to use in measures. You can build visualizations that are more dynamic and powerful by using expressions for titles, subtitles, footnotes, and even [dimensions](#glossary-7 "Glossary term").

This means, for example, that instead of the title of a visualization being static text, it can be made from an expression whose result changes depending on the [selections](#glossary-8 "Glossary term") made.

## Where can I use expressions?

Expressions can be used in a visualization wherever the symbol ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) is seen in the properties panel while editing a visualization. The ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol indicates an expression field. By clicking ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg), you enter the expression editor, which is designed to help you build and edit expressions. Expressions can also be entered directly into the expression field, without using the expression editor.

An expression cannot be saved directly as a [master item](#glossary-9 "Glossary term") but if an expression is used in a measure or dimension, which is then saved as a master item, with its descriptive data, such as name, description, and tags, the expression in the measure or dimension is preserved.

Expressions are used both in scripts and in chart visualizations. They can be simple, involving only basic calculations, or complex, involving functions fields and operators. Expressions can be used in several different situations. The difference between measures and expressions is that expressions have no name or descriptive data.

Information noteIn a script, an expression is evaluated as the script execution passes it by. In visualizations (including charts and tables), expressions are evaluated automatically whenever any of the fields, [variables](#glossary-10 "Glossary term") or functions that the expression contains change value or logical status. A few differences exist between script expressions and chart expressions in terms of syntax and available functions.

## Learn more

- [*Script expressions*](../Scripting/script-expressions.htm)
- [*References to fields, measures, and variables*](../Expressions/references-fields-measures-variables.htm)
- [*Using master measures in expressions*](../Measures/use-master-measures-expressions.htm)
- [What is an expression?](/lnk/What_is_expression)
- [How do I configure an expression using the drop down menus in the Expression Editor?](/lnk/How_configure_expression_using_expression_editor)

Related learning:

- [What is an expression?](/lnk/What_is_expression)
- [How do I configure an expression using the drop down menus in the Expression Editor?](/lnk/How_configure_expression_using_expression_editor)
