---
title: "Dollar-sign expansions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---
# Dollar-sign expansions

Dollar-sign expansions are definitions of text replacements used in the script or in expressions. This process is known as expansion - even if the new text is shorter. The replacement is made just before the script statement or the expression is evaluated.
Technically it is a macro expansion.

The expansion always begins with '$(' and ends with ')'. For example: `$(variablename)`. The content between brackets defines how the text replacement will be done.

For more information and examples, see:

- [*Dollar-sign expansion using a variable*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-variable.htm)
- [*Dollar-sign expansion using parameters*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-parameters.htm)
- [*Dollar-sign expansion using an expression*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-expression.htm)
- [*Include*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/Include.htm)

> **Note:**  A dollar-sign expansion is limited in how many expansions it can calculate. Any expansion with over 1000 levels of nested expansions will not be calculated.
