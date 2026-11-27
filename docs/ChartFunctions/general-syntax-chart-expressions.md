---
title: "General syntax for chart expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/general-syntax-chart-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions"]
---

# General syntax for chart expressions

The following general syntax structure can be used for chart expressions, with many optional parameters:

expression
::= ( constant | expressionname | operator1 expression | expression operator2 expression | function | aggregation function | (expression )
)

where:

constant is a string (a text, a date or a time) enclosed by single straight quotation marks, or a number. Constants are written without thousands separator and with a decimal point as decimal separator.

expressionname is the name (label) of another expression in the same chart.

operator1 is a unary operator (working on one expression, the one to the right).

operator2 is a binary operator (working on two expressions, one on each side).

function ::= functionname (
parameters )

parameters ::= expression { , expression
}

The number and types of parameters are not arbitrary. They depend on the function used.

aggregationfunction ::= aggregationfunctionname
( parameters2 )

parameters2 ::=
aggrexpression { , aggrexpression }

The number and types of parameters are not arbitrary. They depend on the function used.

## Learn more

- [*Operators*](../Scripting/Operators/operators.htm)
