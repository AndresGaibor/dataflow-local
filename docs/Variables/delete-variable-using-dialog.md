---
title: "Deleting a variable"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/delete-variable-using-dialog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations", "Using variables in expressions"]
---

# Deleting a variable

You can delete [variables](#glossary-0 "Glossary term") by deleting them from the variables dialog.

Do the following:

1. When editing a sheet, click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the edit bar on the sheet to open the variables dialog.

   The variables dialog opens.
2. Select the variables you want to delete and click Delete. You can select up to 20 variables.

   You can also click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the row of the variable you want to delete and select Delete.

   Information note

   If you remove a variable from the script and reload the data, the variable stays in the application. If you want to fully remove the variable from the application, you can do any of the following:

   - Delete the variable from the variables dialog.
   - Drop the variable in the script using a [*Drop variable*](../Scripting/ScriptRegularStatements/Drop-Variable.htm) statement.
   - Set variables that are not needed in the variable dialog as script-only variables by using the [*ScriptOnlyVariables*](../Scripting/SystemVariables/ScriptOnlyVariables.htm) system variable in the script.

   Information noteDeleting a variable cannot be undone.
3. Click Delete.

## Learn more

- [*Working with variables in the data load editor*](../Scripting/work-with-variables-in-data-load-editor.htm)
