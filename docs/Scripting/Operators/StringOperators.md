---
title: "String operators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Operators/StringOperators.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Operators"]
---
# String operators

There are two string operators.
One uses the string values of the operands and return a string as result. The other one compares the operands and returns a boolean value to indicate
match.

## &

String concatenation. The operation returns
a text string, that consists of the two operand strings, one after another.

Example:

`'abc'
& 'xyz'` returns 'abcxyz'

## like

String comparison
with wildcard characters. The operation returns a boolean True (-1) if
the string before the operator is matched by the string after the operator.
The second string may contain the wildcard characters \* (any number of
arbitrary characters) or ? (one arbitrary character).

Example:

`'abc'
like 'a*'` returns True (-1)

`'abcd'
like 'a?c*'` returns
True (-1)

`'abc'
like 'a??bc'` returns False (0)
