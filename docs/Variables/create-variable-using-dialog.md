---
title: "Creating a variable"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/create-variable-using-dialog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations", "Using variables in expressions"]
---

# Creating a variable

A [variable](#glossary-0 "Glossary term") in Qlik Sense is a named entity, containing a data value. When a variable is used in an expression, it is substituted by its value or the variable's definition. 
Variables are defined using the variables dialog or in the script using the data load editor.

You can create a new variable from the variables dialog when editing a duplicated or private [sheet](#glossary-1 "Glossary term") in an analytics application in managed, shared, or personal spaces.

You can duplicate an existing variable by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and selecting Duplicate.

Information note

Variables can be created in a [managed space](#glossary-3 "Glossary term") application, and are later removed when the application is republished.

For a visual demo about creating variables, see [Creating a variable](https://share.vidyard.com/watch/bts3r8FuehLRkd2THrQ98m?).

Do the following:

1. When editing a sheet, click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the edit bar on the sheet to open the variables dialog.

   The variables overview opens.
2. Click Create new.

   The following input fields for the variable are displayed:

   - Name (mandatory)
   - Definition
   - Description
   - Tags

   Press Esc or click Cancel if you want to cancel creating the new variable.
3. Type a name for the variable (mandatory). Use the following guidelines when choosing a name:

   - You cannot change the name once you have created the variable.
   - Use a letter as the first character, do not use a number or a symbol.
   - It is not recommended to name a variable identically to a field or a function in Qlik Sense.

     For more information, see
     [*How names are interpreted*](use-variables-expression.htm#How).
   - Do not use the following characters when naming a variable: $ ( ) [ ] "
   - The name must be unique. You cannot name a variable using a name used for a reserved variable or a system variable. These variables are not listed in the variables dialog, but if you are not allowed to use a certain name, even though you cannot find a duplicate in the variables dialog, a reserved variable or a system variable already has this name.
   - A long name is not recommended. If a variable's name is too long, the name cannot be fully displayed in the variables overview.
4. Optionally, type a description for the variable.
5. Create a definition for the variable. You can enter the expression editor by clicking ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg).

   For more information, see
   [*Working with the expression editor*](../Expressions/work-with-expression-editor.htm).

   Example:

   Set the variable's value to today's date, presented as a number:

   Num(Today())
6. Optionally, enter tags for the variable.
7. Optionally, select Include current value of variable when creating bookmarks if you want the current variable value to be included when a user creates a bookmark.

   For more information on variables and bookmarks, see [*Including variable states in bookmarks and reports*](using-variables-with-bookmarks.htm).
8. Click Create to save the variable.

## Learn more

- [*Working with variables in the data load editor*](../Scripting/work-with-variables-in-data-load-editor.htm)
- [*Working with the expression editor*](../Expressions/work-with-expression-editor.htm)
- [*System variables*](../Scripting/SystemVariables/system-variables.htm)
