---
title: "Let"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Let.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Let

The let statement is a complement to the set
statement, used for defining script variables.
The let statement, in opposition
to the set statement, evaluates
the expression on the right side of the ' =' at script run time before it is assigned to
the variable.

Syntax:

Let variablename=expression

Examples and results:

| Example | Result |
| --- | --- |
| Set x=3+4;  Let y=3+4;  z=$(y)+1; | $(x) will be evaluated as ' 3+4 '  $(y) will be evaluated as ' 7 '  $(z) will be evaluated as ' 8 '  Note the difference between the Set and Let statements. The Set statement assigns the string '3+4' to the [variable](#glossary-0 "Glossary term") whereas the Let statement evaluates the string and assigns 7 to the variable. |
| Let T=now( ); | $(T) will be given the value of the current time. |

## Learn more

- [*Set*](Set.htm)
- [*Working with variables in the data load editor*](../work-with-variables-in-data-load-editor.htm)
