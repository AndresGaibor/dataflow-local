---
title: "Mathematical  functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MathConstantsAndParamFreeFunctions/mathematical-functions.htm#e?id=1426
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Mathematical functions

This section describes functions for mathematical constants and Boolean values. These functions do not have any parameters, but the parentheses are still
required.

All functions can be used in both the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MathConstantsAndParamFreeFunctions/mathematical-functions.htm#glossary-0 "Glossary term") and in chart expressions.

e

The function returns the base of the natural logarithms, e (
2.71828...).

e( )

false

The function returns a dual value with text value 'False'
and numeric value 0, which can be used as logical false in expressions.

false(
)

pi

The function returns the value of π (3.14159...).

pi(
)

rand

The function returns a random number between 0 and 1. This can be used to create sample data.

rand(
)

Example:

This example script creates a table of 1000 records with randomly selected upper case characters, that is, characters in the range 65 to 91 (65+26).

Load
Chr( Floor(rand() \* 26) + 65) as UCaseChar,
RecNo() as ID
Autogenerate 1000;

true

The function returns a dual value with text value 'True'
and numeric value -1, which can be used as logical true in expressions.

true(
)
