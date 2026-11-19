---
title: "Working with variables in the data load editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions"]
---
# Working with variables in the data load editor

A variable in Qlik Sense is a container storing a static value or a calculation, for example a numeric or alphanumeric value. When you use the variable in the application, any change made to the variable is applied everywhere the variable is used. You can define variables in the variables overview, or in the script using the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm#glossary-0 "Glossary term"). You set the value of a variable using Let or Set statements in the data load script.

> **Tip:** You can also work with the Qlik Sense variables from the variables overview when editing a sheet. [*Using variables in expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/work-with-variables.htm)

## Overview

If the first character
of a variable value is an equals
sign ' = ' Qlik Sense will try to evaluate the value as a formula (Qlik Sense
expression) and then display or return the result rather than the actual
formula text.

When used, the variable is substituted by its value. Variables
can be used in the script for dollar sign expansion and in various control statements.
This is very useful if the same string is repeated many times in the script,
for example, a path.

Some special system variables will be set by Qlik Sense at the start of the script
execution regardless of their previous values.

## Defining a variable

Variables provide the ability to store static values or the result of a calculation. When defining a variable, use the following syntax:

set variablename =
string

or

let variable = expression

The Set statement is used for string assignment. It assigns the text to the right of the equal sign
to the variable. The Let statement evaluates an expression to the right of the equal sign at script run time and assigns the result of the expression to the variable.

Variables are case sensitive.

> **Note:** It is not recommended to name a variable identically to a field or a function in Qlik Sense.

Examples:

`set x = 3 + 4; //` the variable will get the string '3 + 4' as the value.

`let x = 3 + 4; //` returns 7 as the value.

`set x = Today(); //` returns 'Today()' as the value.

`let x = Today(); //` returns today's date as the value, for example, ‘9/27/2021’.

### Naming your variables

As a best practice, consider using a standardized naming convention for the variables you create in an application. For example, you could make sure all of your variable names start with v. For example: vUserText. This helps to ensure variables are recognized quickly as variables and differentiated from measures, fields, and functions.

## Additional options when defining variables

This section lists additional features you can use to enhance the power of variables you define in the load script.

### Constraining variable values

You can use Constrain statements to restrict script variables to specific definitions, preventing unwanted values from being loaded. Constrain statements can be used for quality assurance, improved collaboration during script codevelopment, and elevated security for analytics applications. In Qlik Cloud, Constrain statements can also be used in combination with the developer API for dynamic, reload-time variable updates.

For more information, see [*Constrain*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Constrain.htm).

### Defining script-only variables

You can use the ScriptOnlyVariables system variable to set script-only variables. A script-only variable is only available in the load script and is not surfaced in, for example, sheet view in the application.

For more information, see [*ScriptOnlyVariables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/ScriptOnlyVariables.htm).

### Dropping variables

You can use a Drop variable statement to drop variables in the script. Dropping a variable is useful when you want to use a variable only for performing calculations or defining fields in the context of the data model.

For more information, see [*Drop variable*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop-Variable.htm).

## Deleting a variable

If you remove a variable from the script and reload the data, the variable stays in the application. If you want to fully remove the variable from the application, you can do any of the following:

- Delete the variable from the variables dialog.
- Drop the variable in the script using a [*Drop variable*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop-Variable.htm) statement.
- Set variables that are not needed in the variable dialog as script-only variables by using the [*ScriptOnlyVariables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/ScriptOnlyVariables.htm) system variable in the script.

For more information, see [*Deleting a variable*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/delete-variable-using-dialog.htm).

## Loading a variable value as a field value

If you want to load a variable value as a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm#glossary-1 "Glossary term") value in a LOAD statement and the result of the dollar expansion is text rather than numeric or an expression then you need to enclose the expanded variable in single quotes.

Example:

This example loads the system variable containing the list of script errors to a table. You can note that the expansion of ScriptErrorCount in the If clause does not require quotes, while the expansion of ScriptErrorList requires quotes.

IF $(ScriptErrorCount) >= 1 THEN
LOAD '$(ScriptErrorList)' AS Error AutoGenerate 1;
END IF

## Variable calculation

There are several ways to use variables with calculated values in Qlik Sense, and the result depends on how you define it and how you call it in an expression.

In this example, we load some inline data:

LOAD \* INLINE [
Dim, Sales
A, 150
A, 200
B, 240
B, 230
C, 410
C, 330
];

Let's define two variables:

Let vSales = 'Sum(Sales)' ;

Let vSales2 = '=Sum(Sales)' ;

In the second variable, we add an equal sign before the expression. This will cause the variable to be calculated before it is expanded and the expression is evaluated.

If you use the vSales variable as it is, for example in a measure, the result will be the string Sum(Sales), that is, no calculation is performed.

If you add a dollar-sign expansion and call $(vSales) in the expression, the variable is expanded, and the sum of Sales is displayed.

Finally, if you call $(vSales2), the variable will be calculated before it is expanded. This means that the result displayed is the total sum of Sales. The difference between using =$(vSales) and =$(vSales2) as measure expressions is seen in this chart showing the results:

Results

| Dim | $(vSales) | $(vSales2) |
| --- | --- | --- |
| A | 350 | 1560 |
| B | 470 | 1560 |
| C | 740 | 1560 |

As you can see, $(vSales) results in the partial sum for a dimension value, while $(vSales2) results in the total sum.

The following script variables are available:

- [*Error variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorVariables.htm)
- [*Number interpretation variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/number-interpretation-variables.htm)
- [*System variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/system-variables.htm)
- [*Value handling variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/value-handling-variables.htm)

## Learn more

- [*Dollar-sign expansions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansions.htm)
- [*Using variables in expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/work-with-variables.htm)
