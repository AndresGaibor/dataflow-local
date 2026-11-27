---
title: "Variables dialog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/variables-dialog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Navigating in the application interface", "Sheet view"]
---

# Variables dialog

Define [variables](#glossary-0 "Glossary term") to store static values or calculations. Any change to the variable is applied everywhere in an application where the variable is used.

Click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) Variables in the assets panel to open the variables dialog. You have to be in edit mode.

You can also define variables in the data [load script](#glossary-2 "Glossary term") using [Data load editor](#glossary-3 "Glossary term"). Set the value of a variable using Let or Set statements in the data load script. Variables added in the load script will be marked with ![Script](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_script.svg) beside the name in the variables dialog.
It is also possible for these variables to be script-only variables, or to be dropped from the script before it finishes running. Script-only variables and dropped variables will not be shown in the dialog.

You can search the variables by name or tags by clicking ![Filter](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter.svg). Value displays the current state of the variables. The values in the variable dialog can change as changes are made in the application, such as by the variable input control.

Variables dialog

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_variablesOverview_rev2.png "Click to view full size")

See:

- [*Creating a variable*](../Variables/create-variable-using-dialog.htm)
- [*Using variables in expressions*](../Variables/work-with-variables.htm)
- [*Examples of using a variable in an expression*](../Variables/use-variables-expression.htm)
- [*Working with variables in the data load editor*](../Scripting/work-with-variables-in-data-load-editor.htm)
- [*Assets panel in edit mode*](sheet-view.htm#Assets)

Related learning:

- [What is a variable?](/lnk/What_is_variable)
- [How do I configure a Dashboard Bundle Variable input object?](/lnk/How_configure_Dashboard_Bundle_Variable_input_object)
