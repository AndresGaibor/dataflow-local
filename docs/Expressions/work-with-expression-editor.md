---
title: "Working with the expression editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Expressions/work-with-expression-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations"]
---

# Working with the expression editor

You can enter the expression editor to add or edit an expression wherever you see the symbol ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the [properties](#glossary-0 "Glossary term") panel while editing a [visualization](#glossary-1 "Glossary term"). The ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol indicates an expression [field](#glossary-2 "Glossary term"). Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to enter the expression editor.

You can add expressions in two ways. Expressions can be created using the Fields, Functions, Variables, and Set expressions sections by making [selections](#glossary-3 "Glossary term") and inserting them into the expression field. You can edit the inserted expressions and add more complex expressions by typing directly into the expression field. You can undo an action by clicking the Undo button ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back.svg) .

## Inserting an expression using Fields

You can insert an expression by making selections from the Fields section at the right-hand side of the expression editor dialog.

Do the following:

1. If you want to limit the available fields to those from a particular table in your data model, select a table from the Filter by table drop-down list.
2. Select a field from the Field drop-down list.
3. Select the aggregation function you want to use. The functions available are from the group of basic aggregation functions.
4. If you want to insert the current selection as a set expression in your aggregation, use the Set expression check box. The current selection is always based on the default state.
5. If you want to insert a Distinct or a Total clause together with the aggregation function, use the check boxes for each clause. Each clause can be used separately.
6. Click Insert to insert the field and the function into the expression field.

   Tip noteIf you do not select an aggregation function, only the field will be inserted into the expression. Clauses can only be added if you select an aggregation function.
7. Click Apply to close the Add expression dialog.

   For a dimension or measure, you continue by adding descriptive data for the dimension or measure.

## Inserting a measure expression using Expression generator

If you are creating an expression for a measure, you can build the expression using natural language. Expand the Expression generator section at the right-hand side of the expression editor dialog. Use field or master item names, basic aggregations, and filters to create the calculation needed. You can use this tool for building visualizations and master measures, as well as creating custom coloring rules for your visualizations.

Do the following:

1. If needed, change the language you are using to build the expression.
2. Under Describe an expression, summarize a combination of fields, master items, aggregations, and filters using natural language.
3. Under Expression summary, check to ensure that your input text was interpreted correctly. Fields and filters are color-coded distinctively.
4. View the output expression under Expression preview, and click Insert to add it to the expression editor.

For more information, see [*Expression generator*](expression-editor.htm#Expressi).

## Inserting a function using Functions

You can insert more than the basic aggregation functions by making selections from the Functions section at the right-hand side of the expression editor dialog.

1. If you want to filter the list of available functions, select a function category from the Function category drop-down list.
2. Select a function from the Function name drop-down list.

   You see a preview of the function.
3. Click Insert to insert the function and the first parenthesis into the expression field.
4. Type the rest of the expression in the expression editor according to the syntax.
5. Click Apply to close the Add expression dialog.

   For a dimension or measure, you continue by adding descriptive data for the dimension or measure.

## Inserting a variable using Variables

You can insert a [variable](#glossary-4 "Glossary term") by making selections from the Variables section at the right-hand side of the expression editor dialog.

1. If you want system variables to appear in the list of available variables use the Show system variables check-box.
2. Select a variable from the Variable drop-down list.

   You see a Definition and Value of the variable, if available.
3. Click Insert to insert the variable into the expression field.
4. Click Apply to close the Add expression dialog.

   For a dimension or measure, you continue by adding descriptive data for the dimension or measure.

## Inserting a set expression using Set expressions

You can insert a set expression by making selections from the Set expressions section at the right-hand side of the expression editor dialog.

1. Select whether to Use current selections or Use bookmark, as a set expression.

   You can only Use current selections if a selection has been made in the application. You can only Use bookmark if a bookmark is available. Use the Bookmark drop-down menu to choose between bookmarks.
2. If you have defined alternate states, you can change the alternate state which the set expression is based on. Select the alternate state from Alternate state drop-down menu.
3. Click Insert to insert the set expression into the expression field.
4. Click Apply to close the Add expression dialog.

   For a dimension or measure, you continue by adding descriptive data for the dimension or measure.

## Adding or editing an expression by typing

Do the following:

1. Type the expression directly in the expression field.

   The field names you use in the expression are checked, and the syntax of the expression is validated.

   Tip noteAs you type in the expression editor, the expression is validated. If there is an error, you see a hint about what is incorrect. Additional error information may be available by clicking the icon next to the hint.

   When you type the name of a function in the expression, a tooltip appears that provides information to help you enter the function correctly, including argument names and qualifiers.

   Information noteThe tooltip for some chart functions shows the ALL qualifier. It is recommended that you do not use the ALL qualifier. Instead, use the set expression {1}.

   Each line in the expression editor is numbered and syntax highlighting is used.
2. Click Apply to close the Add expression dialog.

   For a dimension or measure, you continue by adding descriptive data for the dimension or measure.

## Autocomplete, evaluation and color coding

When typing in the expression editor, you get an autocomplete list of matching fields, variables and functions to select from. The list is narrowed down as you continue to type. The color coding helps you to see where fields, variables and functions are used in the expression.

You can turn the autocomplete hints off or on by clicking ![Autocomplete hints on](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_autocomplete_on_outline.svg) or ![Autocomplete hints off](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_autocomplete_off_outline.svg).

The color coding applies both in the autocomplete list and in the expression itself.

You can verify that any dollar-sign expansions added in your expression give the correct result, by checking the expression evaluation, in the dollar-sign expansion preview.

## Search and replace

When using the expression editor, you can open the search and replace toolbar by clicking ![Icon to open the search and replace toolbar](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg). Type in the string you want to look for in the Search for field, using the Match case option if necessary. All the matching occurrences in the expression will be highlighted and you can navigate between all of them using the Previous and Next arrows. You can then optionally replace one or all of the occurrences with the string you enter in the Replace with field.

## Detailed syntax help

You can activate help mode by clicking the Help button ![Help](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_help.svg). When active, all functions in the expression editor act like hyperlinks. Clicking on a function opens a browser tab to the online help section with the full description of how to use the specific function. When a function is clicked, help mode is exited.

## Learn more

- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
- [*References to fields, measures, and variables*](references-fields-measures-variables.htm)
- [*Expression editor*](expression-editor.htm)
- [*Basic aggregation functions*](../Scripting/AggregationFunctions/basic-aggregation-functions.htm)
- [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm)
- [*Examples of using a variable in an expression*](../Variables/use-variables-expression.htm)
- [*Using variables in expressions*](../Variables/work-with-variables.htm)
- [How do I configure an expression using the drop down menus in the Expression Editor?](/lnk/How_configure_expression_using_expression_editor)

Related learning:

- [How do I configure an expression using the drop down menus in the Expression Editor?](/lnk/How_configure_expression_using_expression_editor)
