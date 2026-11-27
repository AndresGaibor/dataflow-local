---
title: "Expression editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/expression-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Navigating in the application interface", "Sheet view"]
---

# Expression editor

An expression is a calculation that produces a value or data set. It can be a combination of functions, fields, and mathematical operators. Expressions are used to process data in the application in order to produce a result that can be seen in a [visualization](#glossary-1 "Glossary term").

Click Open Expression editor (![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg)) in the [properties](#glossary-2 "Glossary term") panel when editing a visualization or a [sheet](#glossary-3 "Glossary term").

The ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol indicates an expression [field](#glossary-4 "Glossary term"), for example titles, subtitles, footnotes, [dimensions](#glossary-5 "Glossary term"), and [measures](#glossary-6 "Glossary term").

Click Open Expression editor in the properties panel to open the expression editor

![Open expression editor in properties panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_open_expression_editor.png "Click to view full size")

Expression editor

![Expression editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_expression_editor_cloud.png "Click to view full size")

Type directly into the expression editor, or use the expression editor panel to build expressions.

In the expression editor, you can enter an expression by typing in the expression field. When you type the name of a function in the expression, a tooltip appears that provides information to help you enter the function correctly, including argument names and qualifiers. You can also click ![Icon to open the search and replace toolbar](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg) to open the search and replace toolbar.

See:

- [*Working with the expression editor*](work-with-expression-editor.htm)
- [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm)

## Fields

Select a field from a specific table and a common [aggregation](#glossary-7 "Glossary term") function to generate some common expressions to be inserted into the expression editor. You can also select system fields.

To learn more about aggregation functions, see [*Basic aggregation functions*](../Scripting/AggregationFunctions/basic-aggregation-functions.htm), [*Counter aggregation functions*](../Scripting/CounterAggregationFunctions/counter-aggregation-functions.htm) and [*Statistical aggregation functions*](../Scripting/StatisticalAggregationFunctions/statistical-aggregation-functions.htm).

To learn more about system fields, see
[*System fields*](../Scripting/system-fields.htm).

### Clauses and set expressions

Some aggregation functions might require a Distinct clause or a Total clause. Use the check box for each clause to insert it in the aggregation function. Each clause can be used independently.

Use the Set Expression check box to insert your current selection as a set expression in your aggregation. The current selection inserted will always be based on the default state. If you want to create an expression based on an alternate state use the Set Expressions section instead.

To learn more about how to use these set expressions, see [*Set modifiers*](../ChartFunctions/SetAnalysis/set-modifiers.htm).

To learn more about alternate states see [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm).

## Expression generator

When using the expression editor for creating measure expressions, you can generate expressions using natural language. Expand the expression generator, select a language, and type a description of the desired expression. In your description, include the names of the fields or master items, along with the basic aggregations and filters you need to use.

Under Expression preview, you can see the output expression that has been generated. Click Insert to add the expression.

Use the expression generator to create measure expressions for charts and master measures. You can also use it to create expressions to control coloring in your visualization.

Expression generator with natural language entered, and output measure expression ready to be inserted

![Expression editor with Expression generator tab open, showing natural langauge description of expression with the output expression ready to be added to the expression editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_expression_editor_expression_generator.png "Click to view full size")

### Limitations when using the expression generator

The expression generator has the following limitations:

- If custom business logic has been applied to the application, it will influence the expressions generated by your questions. Specifically, if a default calendar period has been defined for a measure within the application's business logic (under Behaviors), generic questions without references to temporal (date) information will automatically generate an expression with the autocalendar applied.

  For example, asking for total sales might generate an expression such as the following:

  ={<[OrderDate.autoCalendar.QuartersAgo]={0}>} sum([Sales])

  This is an example of a dynamic expression, but only appears when the application uses a relative calendar period as the default calendar period. Other generated expressions referencing autocalendar will be static, so do not update as periods naturally change over time.
- Questions referencing temporal (date) fields will generate expressions in which specific date values are represented as static numeric values. Asking a question with direct reference to date information will result in dates represented in this way, regardless of whether a default calendar period has been defined for the measure. These numeric date values do not adjust as periods naturally change over time.
- The following question types are not supported in the expression generator:

  - Questions using master measures with aggregations applied to them (in other words, aggregations applied to aggregations)
  - Questions referencing the top or bottom dimension values for a measure (for example, total sales for top 3 product names)
  - Questions using the 'trend' keyword (for example, Total sales trend for 2023)
  - Questions intending to generate period over period expressions (for example, compare total sales between 2022 and 2023)
- The expression generator supports natural language questions in the following languages:

  - German
  - English
  - Spanish
  - French
  - Italian
  - Dutch
  - Polish
  - Portuguese
  - Russian
  - Swedish

Information noteIf you have questions about how the application's business logic is affecting your ability to generate expressions using natural language, contact the application owner or a user with the required space permissions.

## Functions

Select a function from a specific category to insert it into the expression editor. You can use functions to generate more complex expressions. A small syntax template shows you how each function is used.

See: [*Script and chart functions*](../Scripting/functions-in-scripts-chart-expressions.htm)

## Set expressions

Select whether you want to insert the current selection or a [bookmark](#glossary-8 "Glossary term") as a set expression. If available, you can choose which alternate state on which to base the current selection or bookmark.

## Variables

Select [variables](#glossary-9 "Glossary term") and insert them in your expressions. If available, a definition and the value of each variable is shown.

See: [*Using variables in expressions*](../Variables/work-with-variables.htm)

Related learning:

- [What is an expression?](/lnk/What_is_expression)
- [How do I configure an expression using the drop down menus in the Expression Editor?](/lnk/How_configure_expression_using_expression_editor)
